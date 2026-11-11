"""Marcus search for translation-invariant pairs with three-site support.

The permanent of a cyclic band matrix is a trace of a finite transfer matrix.
All flux sectors are included, not just the sector of zero winding number.
"""
import argparse
import itertools as it
import json
import math
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).parent/".research-tools"/"python"))
import numpy as np
import scipy.linalg as la
import scipy.optimize as opt


def permanent(a):
    n=len(a)
    values=np.zeros(1<<n,dtype=complex)
    values[0]=1
    for mask in range(1,1<<n):
        row=mask.bit_count()-1
        values[mask]=sum(a[row,j]*values[mask^(1<<j)] for j in range(n) if mask&(1<<j))
    return values[-1]


def transitions(k,radius=2):
    width=2*radius*k
    groups=[]
    for occupancy in range(width+1):
        states=[s for s in range(1<<width) if s.bit_count()==occupancy]
        lookup={s:i for i,s in enumerate(states)}
        edges=[]
        for i,state in enumerate(states):
            available=[j for j in range(width+k) if not(state&(1<<j))]
            for chosen in it.combinations(available,k):
                filled=state|sum(1<<j for j in chosen)
                if filled&((1<<k)-1)!=(1<<k)-1:
                    continue
                next_state=filled>>k
                edges.append((i,lookup[next_state],chosen))
        groups.append((len(states),edges))
    return groups


TRANS={k:transitions(k) for k in (1,2)}


def spectrum(blocks,k):
    values=[]
    for size,edges in TRANS[k]:
        matrix=np.zeros((size,size),dtype=complex)
        for i,j,chosen in edges:
            if k==1:
                weight=blocks[chosen[0]-2][0,0]
            else:
                a,b=chosen
                da,ca=a//2-2,a%2
                db,cb=b//2-2,b%2
                weight=blocks[da][0,ca]*blocks[db][1,cb]+blocks[db][0,cb]*blocks[da][1,ca]
            matrix[i,j]+=weight
        values.extend(la.eigvals(matrix))
    return np.array(values)


def band(u):
    return {d:np.array([[sum(np.conj(u[a,l])*u[b,l-d] for l in range(3) if 0<=l-d<3)
                         for b in range(2)] for a in range(2)]) for d in range(-2,3)}


def trace_log(values,m):
    scale=max(abs(values))
    value=sum((values/scale)**m)
    assert value.real>0 and abs(value.imag)<1e-7*value.real,(m,value)
    return m*math.log(scale)+math.log(value.real)


LENGTHS=(5,6,7,8,9,10,12,16,24,32,64,128)


def evaluate(u):
    blocks=band(u)
    large=spectrum(blocks,2)
    small=spectrum({d:np.array([[permanent(v)]]) for d,v in blocks.items()},1)
    gaps=[trace_log(large,m)-trace_log(small,m) for m in LENGTHS]
    return min(gaps),LENGTHS[int(np.argmin(gaps))],gaps


def direct(u,m):
    vectors=np.zeros((2*m,m),dtype=complex)
    for i in range(m):
        for a in range(2):
            for l in range(3):
                vectors[2*i+a,(i+l)%m]=u[a,l]
    a=vectors.conj()@vectors.T
    g=np.array([[permanent(a[2*i:2*i+2,2*j:2*j+2]) for j in range(m)] for i in range(m)])
    return permanent(a).real,permanent(g).real


def run(samples,refine):
    started=time.time()
    rng=np.random.default_rng(924760)
    def normalize(u):
        return u/la.norm(u,axis=1)[:,None]
    for _ in range(4):
        u=normalize(rng.normal(size=(2,3))+1j*rng.normal(size=(2,3)))
        _,_,gaps=evaluate(u)
        p,q=direct(u,5)
        assert abs(gaps[0]-math.log(p/q))<1e-9
    print("Self-check: cyclic transfers agree with independent order-ten permanent DP.",flush=True)
    best=float("inf")
    witness=None
    length=None
    candidates=[]
    for trial in range(samples):
        u=normalize(rng.normal(size=(2,3))+1j*rng.normal(size=(2,3)))
        gap,m,gaps=evaluate(u)
        if gap<best:
            best,witness,length=gap,u.copy(),m
            print(json.dumps({"trial":trial,"ratio":math.exp(best),"length":length}),flush=True)
        candidates.append((gap,u.copy()))
    def unpack(x):
        return normalize(x[:6].reshape(2,3)+1j*x[6:].reshape(2,3))
    for index,(_,u) in enumerate(sorted(candidates,key=lambda x:x[0])[:refine]):
        x=np.r_[u.real.ravel(),u.imag.ravel()]
        fit=opt.minimize(lambda x:evaluate(unpack(x))[0],x,method="L-BFGS-B",options={"maxiter":250,"ftol":1e-12,"gtol":1e-7})
        u=unpack(fit.x)
        gap,m,gaps=evaluate(u)
        if gap<best:
            best,witness,length=gap,u.copy(),m
            print(json.dumps({"refinement":index,"ratio":math.exp(best),"length":length}),flush=True)
    output={"samples":samples,"refinements":refine,"best_ratio":math.exp(best),"length":length,
            "vectors":np.stack((witness.real,witness.imag),axis=-1).tolist(),"lengths":LENGTHS,"log_ratios":evaluate(witness)[2],"seconds":time.time()-started}
    if length<=7:
        p,q=direct(witness,length)
        assert abs(math.log(p/q)-best)<1e-8
        output["independent_permanents"]={"A":p,"G":q}
    Path("marcus-banded-transfer-results.json").write_text(json.dumps(output,indent=2))
    print(json.dumps({key:value for key,value in output.items() if key not in ("vectors","log_ratios","lengths")}),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--samples",type=int,default=2000)
    parser.add_argument("--refine",type=int,default=30)
    args=parser.parse_args()
    run(args.samples,args.refine)
