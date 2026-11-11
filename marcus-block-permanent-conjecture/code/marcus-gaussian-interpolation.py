"""Search for failure of the derivative at the polynomial endpoint.

This tests a sufficient monotonicity route, not Marcus's inequality itself.
"""
import argparse
import importlib.util
import itertools as it
import json
from pathlib import Path
import time

spec=importlib.util.spec_from_file_location("spectral",Path(__file__).with_name("marcus-chaos-spectral.py"))
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
np,la=base.np,base.la


def multiplier(pol,f,degree):
    indices,weights=pol.table(degree,pol.k)
    out=np.zeros((len(pol.basis(degree+pol.k)),len(pol.basis(pol.k))),complex)
    for j in range(out.shape[1]):
        out[indices[:,j],j]=weights[:,j]*f
    return out


def derivative(pol,forms):
    f=pol.product(forms)
    omitted=np.array([pol.product(np.delete(forms,i,axis=0)) for i in range(pol.m)])
    gram=forms.conj()@forms.T
    h=omitted.conj()@omitted.T
    return pol.m*np.vdot(f,f).real-np.sum(gram*h).real


def pencil(pol,other):
    f=pol.product(other)
    full=multiplier(pol,f,(pol.m-1)*pol.k)
    gram=other.conj()@other.T
    maps=[multiplier(pol,pol.product(np.delete(other,i,axis=0)),(pol.m-2)*pol.k) for i in range(pol.m-1)]
    b=np.vdot(f,f).real*np.eye(len(pol.basis(pol.k)),dtype=complex)
    for i,mi in enumerate(maps):
        for j,mj in enumerate(maps):
            b+=gram[i,j]*(mi.conj().T@mj)
        v=mi.conj().T@f
        cross=np.outer(v,other[i].conj())
        b+=cross+cross.conj().T
    return pol.m*(full.conj().T@full)-b


def moment(pol,forms,t):
    gram=forms.conj()@forms.T
    total=0j
    all_indices=set(range(pol.m))
    for size in range(pol.m+1):
        subsets=list(it.combinations(range(pol.m),size))
        products=[pol.product(forms[list(s)]) for s in subsets]
        for i,left in enumerate(subsets):
            lc=sorted(all_indices-set(left))
            for j,right in enumerate(subsets):
                rc=sorted(all_indices-set(right))
                total+=t**size*(1-t)**(pol.m-size)*np.vdot(products[i],products[j])*base.permanent(gram[np.ix_(lc,rc)])
    assert abs(total.imag)<1e-7*max(1,abs(total.real))
    return total.real


def run(m,k,r,restarts,cycles):
    start=time.time()
    pol=base.Polynomials(r,k,m)
    dim=len(pol.basis(k))
    rng=np.random.default_rng(867341)
    def random():
        q=rng.normal(size=(m,dim))+1j*rng.normal(size=(m,dim))
        return q/la.norm(q,axis=1)[:,None]
    forms=random()
    matrix=pencil(pol,forms[:-1])
    value=derivative(pol,forms)
    assert la.norm(matrix-matrix.conj().T)<1e-8
    assert abs(np.vdot(forms[-1],matrix@forms[-1]).real-value)<1e-8
    assert abs(moment(pol,forms,0)-base.permanent(forms.conj()@forms.T).real)<1e-9
    assert abs(moment(pol,forms,1)-np.vdot(pol.product(forms),pol.product(forms)).real)<1e-9
    step=1e-4
    finite=(3*moment(pol,forms,1)-4*moment(pol,forms,1-step)+moment(pol,forms,1-2*step))/(2*step)
    assert abs(finite-value)<1e-5*max(1,abs(value))
    print(json.dumps({"self_check":"pencil, endpoints and derivative agree","m":m,"k":k,"r":r}),flush=True)
    best=float("inf")
    minima=[]
    witness=None
    for trial in range(restarts):
        forms=random()
        previous=derivative(pol,forms)
        for cycle in range(cycles):
            for index in rng.permutation(m):
                matrix=pencil(pol,np.delete(forms,index,axis=0))
                values,vectors=la.eigh(matrix,subset_by_index=(0,0),driver="evr")
                forms[index]=vectors[:,0]
            value=derivative(pol,forms)
            assert value<=previous+1e-7
            if abs(value-previous)<1e-10:
                break
            previous=value
        minima.append(value)
        if value<best:
            best=value
            witness=np.stack((forms.real,forms.imag),axis=-1).tolist()
            print(json.dumps({"trial":trial,"derivative":best,"marcus_ratio":pol.value(forms)}),flush=True)
        if best < -1e-7:
            break
    out={"m":m,"k":k,"r":r,"restarts":len(minima),"cycles":cycles,"minima":minima,"best":best,"forms":witness,"basis":pol.basis(k),"seconds":time.time()-start,"scope":"numerical search for a negative endpoint derivative; not a Marcus counterexample"}
    target=Path(f"marcus-gaussian-interpolation-{m}-{k}-{r}.json")
    target.write_text(json.dumps(out,indent=2))
    print(json.dumps({"file":str(target),"best":best,"seconds":out["seconds"]}),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    for name in ("m","k","r"):
        parser.add_argument(name,type=int)
    parser.add_argument("--restarts",type=int,default=100)
    parser.add_argument("--cycles",type=int,default=100)
    args=parser.parse_args()
    run(args.m,args.k,args.r,args.restarts,args.cycles)
