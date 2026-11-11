# Aurifeuillean factor F(y) of Phi_{2m}(m y^2), m = 3 mod 4 squarefree, via Galois orbit
import numpy as np, sys
from math import gcd
sys.path.insert(0,'..')
from poly import cyclo, mul
def jacobi(a,n):
    a%=n; r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
def aur2(m):
    ph=sum(1 for c in range(1,m) if gcd(c,m)==1)
    roots=[jacobi(m,c)*np.exp(2j*np.pi*c/(4*m))/np.sqrt(m) for c in range(1,2*m) if gcd(c,4*m)==1]
    assert len(roots)==ph
    c=np.poly(roots)[::-1]*m**(ph/2)
    r=np.round(c.real)
    F=[int(v) for v in r]
    Fm=[v*(-1)**i for i,v in enumerate(F)]
    lhs=mul(F,Fm); phc=cyclo(2*m); rhs=[0]*(2*len(phc)-1)
    for i,v in enumerate(phc): rhs[2*i]=v*m**i
    ok = lhs==rhs or lhs==[-v for v in rhs]
    return F if ok else None
if __name__=='__main__':
    for m in [3,7,11,15,19,23,35,39,51,55,91,119,143]:
        F=aur2(m); print(m, F if F is None or len(F)<12 else ('ok deg',len(F)-1))
