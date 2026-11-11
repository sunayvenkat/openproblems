# carry test for Aurifeuillean pieces F(+-y) of N=(p y^2)^p+1 at level t (F^t), y = 0 mod p^big
from fractions import Fraction as Fr
import sys
from aurif import aur
def pdivmod(a,b):  # a,b lists of Fractions low->high
    a=a[:]; q=[Fr(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        c=a[-1]/b[-1]; s=len(a)-len(b); q[s]=c
        for i,v in enumerate(b): a[s+i]-=c*v
        while a and a[-1]==0: a.pop()
    return q,a
def pmul(a,b):
    r=[Fr(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return r
def ev(a,y): return sum(c*y**i for i,c in enumerate(a))
def test(p,F,t,jp=1):
    N=[Fr(0)]*(2*p+1); N[0]=Fr(jp); N[2*p]=Fr(jp*p**p)
    G=[Fr(1)]
    for _ in range(t): G=pmul(G,[Fr(v) for v in F])
    P,R=pdivmod(N,G)
    f0=P[0]-(P[0].numerator//P[0].denominator)
    lcR=R[-1] if R else 0
    # direct integer check at y = p^K * 3
    K=60; y=p**K*3
    Ni=jp*((p*y*y)**p+1); Fi=int(ev([Fr(v) for v in F],y)); Gi=Fi**t
    carry = ((2*Ni)//Gi)%2==1
    return f0, (1 if lcR>0 else -1), carry
if __name__=='__main__':
    for p in [7,11,19,23]:
        F=aur(p); Fm=[v*(-1)**i for i,v in enumerate(F)]
        L=(2*p)//(p-1)   # max power t with F^t <= N (degree)
        for name,FF in (('F+',F),('F-',Fm)):
            for t in range(2,L+1):
                for jp in (1,2):
                    f0,sg,c=test(p,FF,t,jp)
                    print(p,name,'t',t,'jp',jp,'frac P(0)=',f0,'tail sign',sg,'direct carry',c)
