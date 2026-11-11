# Aurifeuillean factors of Phi_{2p}(p y^2), p = 3 mod 4 prime: F(y) F(-y) = Phi_{2p}(p y^2)
import numpy as np, itertools, sys
sys.path.insert(0,'..')
from poly import cyclo, mul
def legendre(a,p): return 1 if pow(a,(p-1)//2,p)==1 else -1
def aur(p):
    roots=[(-1j)*np.exp(1j*np.pi*a/p)/np.sqrt(p) for a in range(1,p)]
    for eps in (1,-1):
      for twist in range(4):
        s=[eps*legendre(a,p)*((-1)**(a*twist%2) if twist<2 else 1)*(1 if twist%2==0 else (-1)**a) for a in range(1,p)]
        ys=[s[i]*roots[i] for i in range(p-1)]
        c=np.poly(ys)[::-1]*p**((p-1)//2)   # low->high
        r=np.round(c.real)
        if np.max(np.abs(c-r))<1e-6*max(1,np.max(np.abs(r))):
            F=[int(v) for v in r]
            # exact check: F(y)F(-y) == Phi_{2p}(p y^2)
            Fm=[v*(-1)**i for i,v in enumerate(F)]
            lhs=mul(F,Fm); ph=cyclo(2*p); rhs=[0]*(2*len(ph)-1)
            for i,v in enumerate(ph): rhs[2*i]=v*p**i
            if lhs==rhs or lhs==[-v for v in rhs]: return F
    return None
if __name__=='__main__':
    for p in [3,7,11,19,23,31,43]:
        print(p, aur(p))
