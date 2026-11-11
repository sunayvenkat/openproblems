"""Search dimension-independent tensor squares using individual Gram vectors.

Unlike the polynomial-tensor search, cuts may split factors of one block.
No Kronecker delta lifts are used, so coefficient equations do not depend
on the dimension of the Gram-vector space. Numerical output is discovery only.
"""
import argparse
import importlib.util
import itertools as it
import json
import math
from pathlib import Path
import time

spec=importlib.util.spec_from_file_location("engine",Path(__file__).with_name("marcus-invariant-sdp.py"))
engine=importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)
np,la,sp,cp=engine.np,engine.la,engine.sp,engine.cp


def wreath(m,k):
    result=[]
    local=list(it.permutations(range(k)))
    for blocks in it.permutations(range(m)):
        for internal in it.product(local,repeat=m):
            result.append(tuple(blocks[b]*k+internal[b][a] for b in range(m) for a in range(k)))
    return result


def inverse(p):
    out=[0]*len(p)
    for i,j in enumerate(p):
        out[j]=i
    return tuple(out)


def orbits(m,k):
    n=m*k
    group=wreath(m,k)
    inside=set(group)
    lookup,reps,target={},[],[]
    for perm in it.permutations(range(n)):
        if perm in lookup:
            continue
        orbit=set()
        for h in group:
            hinv=inverse(h)
            conjugate=tuple(h[perm[hinv[i]]] for i in range(n))
            orbit.add(conjugate)
            orbit.add(inverse(conjugate))
        o=len(target)
        for member in orbit:
            lookup[member]=o
        reps.append(min(orbit))
        target.append(0 if perm in inside else len(orbit))
    assert sum(target)==math.factorial(n)-len(group)
    return lookup,np.array(target,dtype=float),reps


def networks(m,k,counts,t):
    n=m*k
    hol=tuple(b*k+a for b,c in enumerate(counts) for a in range(c))
    anti=tuple(i for i in range(n) if i not in hol)
    labels=hol+anti
    cut=len(hol)
    left,right=cut-t,n-cut-t
    boundary=left+right
    out=[]
    for hs in it.combinations(range(cut),t):
        for ns in it.combinations(range(cut,n),t):
            for matched in it.permutations(ns):
                pairs=tuple(zip(hs,matched))
                if all(labels[a]//k==labels[b]//k for a,b in pairs):
                    continue
                legs=[None]*n
                for j,(a,b) in enumerate(pairs):
                    legs[a]=legs[b]=(boundary+j,)
                freeh=tuple(i for i in range(cut) if i not in hs)
                freen=tuple(i for i in range(cut,n) if i not in ns)
                for hp in it.permutations(freeh):
                    for ap in it.permutations(freen):
                        completed=legs.copy()
                        for j,a in enumerate(hp+ap):
                            completed[a]=(j,)
                        out.append((tuple(completed),()))
    return out,labels,left,right,cut


def solve(m,k,solver,dimension):
    started=time.time()
    lookup,target,reps=orbits(m,k)
    n=m*k
    variables,coefs,saved=[],[],[]
    print(json.dumps({"m":m,"k":k,"orbits":len(target)}),flush=True)
    for counts in it.combinations_with_replacement(range(k+1),m):
        cut=sum(counts)
        if cut==0 or cut>n//2:
            continue
        for t in ([0] if dimension else range(1,min(cut,n-cut)+1)):
            if dimension:
                hol=tuple(b*k+a for b,c in enumerate(counts) for a in range(c))
                labels=hol+tuple(i for i in range(n) if i not in hol)
                candidates,left,right=engine.networks(n,cut,1)
                nets=[]
                for net in candidates:
                    incident={}
                    for a,(index,) in enumerate(net[0]):
                        if index>=left+right:
                            incident.setdefault(index,[]).append(a)
                    if any(labels[a]//k!=labels[b]//k for a,b in incident.values()):
                        nets.append(net)
            else:
                nets,labels,left,right,cut=networks(m,k,counts,t)
            if not nets:
                continue
            entries=[[] for _ in target]
            for i,a in enumerate(nets):
                for j in range(i,len(nets)):
                    table,loops=engine.inner_diagram(a,nets[j],n,left+right,cut,1)
                    assert dimension or loops==0
                    perm=[None]*n
                    for row in range(n):
                        col=table[row*n:(row+1)*n].index(1)
                        perm[labels[row]]=labels[col]
                    orbit=lookup[tuple(perm)]
                    entries[orbit].append((i,j,dimension**loops if dimension else 1))
                    if i!=j:
                        entries[orbit].append((j,i,dimension**loops if dimension else 1))
            matrices=[]
            for items in entries:
                if items:
                    rows,cols,values=zip(*items)
                    matrices.append(sp.csc_matrix((values,(rows,cols)),shape=(len(nets),len(nets))))
                else:
                    matrices.append(sp.csc_matrix((len(nets),len(nets))))
            bases=engine.reduced_bases(nets,left,right)
            print(json.dumps({"counts":counts,"contractions":t,"networks":len(nets),"blocks":[(name,raw.shape[1]) for name,raw,_,_ in bases]}),flush=True)
            for name,raw,basis,transform in bases:
                name=f"{counts}/t{t}/{name}"
                x=cp.Variable((basis.shape[1],basis.shape[1]),symmetric=True,name=name)
                variables.append(x)
                coefs.append([basis.T@matrix@basis for matrix in matrices])
                saved.append({"name":name,"counts":counts,"contractions":t,"labels":labels,"networks":nets,"basis":raw.tolist(),"transform":transform})
    scale=max(target)
    equations=[sum(cp.sum(cp.multiply(c[o],x)) for c,x in zip(coefs,variables))==target[o]/scale for o in range(len(target))]
    problem=cp.Problem(cp.Minimize(0),[x>>0 for x in variables]+equations)
    options={"solver":solver,"verbose":False}
    if solver=="CLARABEL":
        options.update(tol_gap_abs=1e-9,tol_gap_rel=1e-9,tol_feas=1e-9,max_iter=150)
    else:
        options.update(eps=1e-7,max_iters=100000)
    problem.solve(**options)
    output={"m":m,"k":k,"dimension":dimension,"status":problem.status,"target":target.tolist(),"representatives":reps,"blocks":[],"seconds":time.time()-started}
    if all(x.value is not None for x in variables):
        values=[x.value*scale for x in variables]
        output["max_residual"]=float(max(abs(sum(np.sum(c[o]*v) for c,v in zip(coefs,values))-target[o]) for o in range(len(target))))
        output["minimum_eigenvalue"]=min(float(la.eigvalsh(v)[0]) for v in values)
        for block,value in zip(saved,values):
            transform=block.pop("transform")
            block["gram"]=(transform@value@transform.T).tolist()
            output["blocks"].append(block)
    Path(f"marcus-vector-sdp-{m}-{k}-{dimension}.json").write_text(json.dumps(output,indent=2))
    print(json.dumps({key:value for key,value in output.items() if key not in ("target","representatives","blocks")}),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--blocks",type=int,default=3)
    parser.add_argument("--size",type=int,default=2)
    parser.add_argument("--solver",choices=("CLARABEL","SCS"),default="CLARABEL")
    parser.add_argument("--dimension",type=int,default=0)
    args=parser.parse_args()
    solve(args.blocks,args.size,args.solver,args.dimension)
