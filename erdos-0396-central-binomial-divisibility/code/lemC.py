# Laurent-sign carry criterion for pieces Phi_{2d}(x) of n-i = j'(x^m+1), m odd.
import sys
from math import gcd
def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def mu(n):
    r=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0: return 0
            r=-r
        p+=1
    return -r if n>1 else r
def phi(n): return sum(1 for k in range(1,n+1) if gcd(k,n)==1)
def series_pow_cyclo(n, ex, N):
    "coeffs of Phi_n(t)^ex up to t^N (n>1), ex may be negative"
    c=[0]*(N+1); c[0]=1
    for e in divisors(n):
        k=ex*mu(n//e)
        if k>0:   # multiply by (1-t^e)^k
            for _ in range(k):
                for i in range(N,e-1,-1): c[i]-=c[i-e]
        elif k<0: # divide by (1-t^e)^|k|
            for _ in range(-k):
                for i in range(e,N+1): c[i]+=c[i-e]
    return c
def piece_report(m,d):
    delta=phi(2*d); S=m//delta-1; res=[]
    for s in range(1,S+1):
        E=m-(s+1)*delta; N=m+2*delta+5
        c=series_pow_cyclo(2*d,-(s+1),N)
        sg=None
        for t in range(E+1,N+1):
            v=c[t]+(c[t-m] if t>=m else 0)
            if v: sg=(t, 1 if v>0 else -1); break
        res.append((s,sg))
    good=any(r[1] and r[1][1]<0 for r in res)
    return good,res
if __name__=='__main__':
    for m in map(int,sys.argv[1:]):
        print('m',m,'phi/m',round(phi(m)/m,3))
        for d in divisors(m):
            g,res=piece_report(m,d)
            print('  d',d,'good' if g else 'BAD', res if (not g or d==m) else '')
