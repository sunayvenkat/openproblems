import numpy as np, sys
from sympy_free import factor_small, sqfree_divisors_mu
def series_mod(n_primes, ex, N, P):
    c=np.zeros(N+1,dtype=np.int64); c[0]=1; n=1
    for p in n_primes: n*=p
    for d,mu in sqfree_divisors_mu(n_primes):
        e=n//d; k=ex*mu
        if e>N or k==0: continue
        for _ in range(abs(k)):
            if k>0: c[e:]=(c[e:]-c[:-e].copy())%P
            else:
                L=((N+1+e-1)//e)*e; b=np.zeros(L,dtype=np.int64); b[:N+1]=c
                b=np.cumsum(b.reshape(-1,e),axis=0).reshape(-1)%P; c=b[:N+1].copy()
    return c
m=int(sys.argv[1]); ps=factor_small(m); phi=1
for p in ps: phi*=p-1
E=m-2*phi; N=E+3
for P in (2147483647,2147483629,2147483587):
    c=series_mod([2]+ps,-2,N,P); v=int(c[E+1]); print(P, v, v-P)
print('int64 claim', 82409319267826633 % 2147483647, 82409319267826633 % 2147483629)
