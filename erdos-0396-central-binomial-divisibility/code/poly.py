# integer polynomial helpers: lists of ints, index = degree
def trim(a):
    while a and a[-1]==0: a.pop()
    return a
def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j]+=x*y
    return trim(r)
def sub(a,b):
    n=max(len(a),len(b)); return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(n)])
def add(a,b):
    n=max(len(a),len(b)); return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)])
def divmod_monic(a,f):
    a=a[:]; q=[0]*max(1,len(a)-len(f)+1); df=len(f)-1
    assert f[-1]==1
    while len(a)-1>=df and a:
        c=a[-1]; s=len(a)-1-df; q[s]=c
        for i,y in enumerate(f): a[s+i]-=c*y
        trim(a)
    return trim(q),a
from functools import lru_cache
@lru_cache(None)
def cyclo(n):
    p=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0: p,r=divmod_monic(p,list(cyclo(d))); assert not r
    return tuple(p)
def digits(w,f):
    "polynomial base-f digits of w (lowest first)"
    out=[]
    while w:
        w,r=divmod_monic(w,f); out.append(r)
    return out
