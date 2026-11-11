"""Alternating exact one-factor minimizations of the stronger polynomial bound.

A counterexample with nonsplit polynomials would not itself refute Marcus.
"""
import argparse
import itertools as it
import json
import math
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).parent / ".research-tools" / "python"))
import numpy as np
import scipy.linalg as la


def permanent(a):
    n=len(a)
    sums=np.zeros(1<<n, dtype=complex)
    sums[0]=1
    for mask in range(1,1<<n):
        row=mask.bit_count()-1
        sums[mask]=sum(a[row,j]*sums[mask^(1<<j)] for j in range(n) if mask&(1<<j))
    return sums[-1]


class Polynomials:
    def __init__(self,r,k,m):
        self.r,self.k,self.m=r,k,m
        self.bases={}
        self.tables={}

    def basis(self,d):
        if d not in self.bases:
            def comp(left,length):
                if length==1:
                    yield (left,)
                else:
                    for first in range(left+1):
                        for rest in comp(left-first,length-1):
                            yield (first,)+rest
            self.bases[d]=list(comp(d,self.r))
        return self.bases[d]

    def table(self,d,e):
        if (d,e) not in self.tables:
            left,right,total=self.basis(d),self.basis(e),self.basis(d+e)
            lookup={alpha:i for i,alpha in enumerate(total)}
            indices=np.empty((len(left),len(right)),dtype=int)
            weights=np.empty(indices.shape,dtype=float)
            for i,alpha in enumerate(left):
                for j,beta in enumerate(right):
                    gamma=tuple(a+b for a,b in zip(alpha,beta))
                    indices[i,j]=lookup[gamma]
                    weights[i,j]=math.sqrt(math.prod(math.comb(a+b,a) for a,b in zip(alpha,beta)))
            self.tables[d,e]=(indices,weights)
        return self.tables[d,e]

    def product(self,forms):
        value=np.array([1+0j])
        for i,q in enumerate(forms):
            indices,weights=self.table(i*self.k,self.k)
            next_value=np.zeros(len(self.basis((i+1)*self.k)),dtype=complex)
            np.add.at(next_value,indices.ravel(),(value[:,None]*q[None,:]*weights).ravel())
            value=next_value
        return value

    def pencil(self,other):
        f=self.product(other)
        indices,weights=self.table((self.m-1)*self.k,self.k)
        dim=len(self.basis(self.k))
        matrix=np.zeros((len(self.basis(self.m*self.k)),dim),dtype=complex)
        for j in range(dim):
            matrix[indices[:,j],j]=weights[:,j]*f
        numerator=matrix.conj().T@matrix
        gram=other.conj()@other.T
        denominator=permanent(gram).real*np.eye(dim,dtype=complex)
        for i in range(self.m-1):
            for j in range(self.m-1):
                minor=np.delete(np.delete(gram,i,axis=0),j,axis=1)
                denominator+=permanent(minor)*np.outer(other[j],other[i].conj())
        return numerator,denominator

    def value(self,forms):
        f=self.product(forms)
        return np.vdot(f,f).real/permanent(forms.conj()@forms.T).real


def run(m,k,r,restarts,cycles):
    start=time.time()
    pol=Polynomials(r,k,m)
    dim=len(pol.basis(k))
    rng=np.random.default_rng(702611)
    def random():
        q=rng.normal(size=(m,dim))+1j*rng.normal(size=(m,dim))
        return q/la.norm(q,axis=1)[:,None]
    check=random()
    n,d=pol.pencil(check[:-1])
    ratio=(np.vdot(check[-1],n@check[-1])/np.vdot(check[-1],d@check[-1])).real
    assert abs(ratio-pol.value(check))<1e-9
    assert la.norm(n-n.conj().T)<1e-8 and la.norm(d-d.conj().T)<1e-8
    print(json.dumps({"self_check":"pencil agrees with direct permanent and polynomial norms","dimension":dim}),flush=True)
    best=float("inf")
    witness=None
    minima=[]
    for trial in range(restarts):
        forms=random()
        previous=pol.value(forms)
        for cycle in range(cycles):
            for index in rng.permutation(m):
                other=np.delete(forms,index,axis=0)
                numerator,denominator=pol.pencil(other)
                vals,vectors=la.eigh(numerator,denominator,subset_by_index=(0,0),driver="gvx")
                forms[index]=vectors[:,0]/la.norm(vectors[:,0])
            value=pol.value(forms)
            assert value<=previous+1e-8
            if abs(previous-value)<1e-11:
                break
            previous=value
        minima.append(value)
        if value<best:
            best=value
            witness=np.stack((forms.real,forms.imag),axis=-1).tolist()
            print(json.dumps({"trial":trial,"ratio":best,"cycle":cycle}),flush=True)
        if best<1-1e-8:
            break
    out={"m":m,"k":k,"r":r,"restarts":len(minima),"cycles":cycles,"minima":minima,"best":best,"forms":witness,"basis":pol.basis(k),"seconds":time.time()-start}
    path=Path(f"marcus-chaos-spectral-{m}-{k}-{r}.json")
    path.write_text(json.dumps(out,indent=2))
    print(json.dumps({"file":str(path),"best":best,"seconds":time.time()-start}),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("m",type=int)
    parser.add_argument("k",type=int)
    parser.add_argument("r",type=int)
    parser.add_argument("--restarts",type=int,default=100)
    parser.add_argument("--cycles",type=int,default=50)
    args=parser.parse_args()
    run(args.m,args.k,args.r,args.restarts,args.cycles)
