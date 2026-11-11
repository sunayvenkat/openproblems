# Exact Aurifeuillean factor F(y) of Phi_{2m}(m y^2), m = 3 mod 4 squarefree.
# Roots of F: r_c/sqrt(m), r_c = chi(c) zeta_{4m}^c, c in [1,2m) coprime to 2m; chi = (m/.) Jacobi.
# Power sums of r_c: k even -> c_{4m}(k)/2 ; k odd -> chi(k) sqrt(m). Newton identities in Q(sqrt m).
import sys
from fractions import Fraction as Fr
from math import gcd
sys.path.insert(0,'..')
from poly import cyclo, mul
from aurif2 import jacobi

def mobius(n):
    r=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0: return 0
            r=-r
        p+=1
    return -r if n>1 else r
def ramanujan(q,k):
    g=gcd(q,k); return sum(mobius(q//d)*d for d in range(1,g+1) if g%d==0)
def phi(n): return sum(1 for c in range(1,n+1) if gcd(c,n)==1)

def aur3(m):
    ph=phi(m)
    # element of Q(sqrt m) as (a,b) = a + b sqrt m
    p=[None]+[ (Fr(ramanujan(4*m,k),2),Fr(0)) if k%2==0 else (Fr(0),Fr(jacobi(m,k) if gcd(k,4*m)==1 else 0)) for k in range(1,ph+1)]
    def mlt(x,y): return (x[0]*y[0]+m*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
    e=[(Fr(1),Fr(0))]
    for j in range(1,ph+1):
        s=(Fr(0),Fr(0))
        for i in range(1,j+1):
            t=mlt(e[j-i],p[i]); sg=1 if i%2==1 else -1
            s=(s[0]+sg*t[0], s[1]+sg*t[1])
        e.append((s[0]/j, s[1]/j))
    # G(z) = sum_j (-1)^j e_j z^{ph-j};  F(y)=G(sqrt(m) y): coeff of y^i = g_i m^{i/2}
    F=[]
    for i in range(ph+1):
        j=ph-i; g=e[j]; sg=(-1)**j
        if i%2==0:
            assert g[1]==0; v=sg*g[0]*m**(i//2)
        else:
            assert g[0]==0; v=sg*g[1]*m**((i+1)//2)
        assert v.denominator==1; F.append(int(v))
    Fm=[v*(-1)**i for i,v in enumerate(F)]
    lhs=mul(F,Fm); phc=cyclo(2*m); rhs=[0]*(2*len(phc)-1)
    for i,v in enumerate(phc): rhs[2*i]=v*m**i
    assert lhs==rhs or lhs==[-v for v in rhs], "identity fails"
    return F
if __name__=='__main__':
    for m in [3,7,11,15,35,39,51,111]:
        F=aur3(m); print(m,'deg',len(F)-1, F[:6])
