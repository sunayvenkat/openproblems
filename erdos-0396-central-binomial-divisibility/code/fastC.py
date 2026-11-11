import numpy as np, sys
from sympy_free import factor_small, sqfree_divisors_mu
def series(n_primes, ex, N):
    "Phi_n(t)^ex mod t^(N+1), n = product of n_primes (squarefree, n>1)"
    c=np.zeros(N+1,dtype=np.int64); c[0]=1
    n=1
    for p in n_primes: n*=p
    for d,mu in sqfree_divisors_mu(n_primes):   # d | n, mu = mu(d); factor (1-t^{n/d})^{mu(d)}
        e=n//d; k=ex*mu
        if e>N or k==0: continue
        for _ in range(abs(k)):
            if k>0:
                c[e:]=c[e:]-c[:-e].copy()
            else:
                L=((N+1+e-1)//e)*e
                b=np.zeros(L,dtype=np.int64); b[:N+1]=c
                b=np.cumsum(b.reshape(-1,e),axis=0).reshape(-1)
                c=b[:N+1].copy()
    return c
def top_sign(m, smax=None, extra=4000):
    ps=factor_small(m); assert len(set(ps))==len(ps) and m%2
    phi=1
    for p in ps: phi*=p-1
    S=m//phi-1; res=[]
    for s in range(1,(S if smax is None else min(S,smax))+1):
        E=m-(s+1)*phi; N=min(E+extra, 2*m)
        c=series([2]+ps,-(s+1),N)   # Phi_{2m}
        sg=None
        for t in range(E+1,N+1):
            v=int(c[t])+(int(c[t-m]) if t>=m else 0)
            if v: sg=(t-E, v); break
        res.append((s,E,sg, int(np.abs(c[E+1:N+1]).max())))
    return phi/m, res
if __name__=='__main__':
    for m in map(int,sys.argv[1:]):
        r=top_sign(m); print(m, round(r[0],4), r[1], flush=True)
