# Test Lemma O: for gcd(s,N)=1, s>N^theta, any D' subset of divisors meeting R classes mod s:
# theta*w <= 1 + log2 R + log2(tau/|D'|).  Also compute R(s) for natural moduli.
import math, random, itertools
def isprime(n):
    if n<2: return False
    for q in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n%q==0: return n==q
    d,r=n-1,0
    while d%2==0: d//=2; r+=1
    for a in [2,3,5,7,11,13,17,19,23,29,31,37]:
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True
def rho(n):
    if n%2==0: return 2
    while True:
        c=random.randrange(1,n); x=y=random.randrange(2,n); d=1
        f=lambda v:(v*v+c)%n
        while d==1:
            x=f(x); y=f(f(y)); d=math.gcd(abs(x-y),n)
        if d!=n: return d
def factor(n,out):
    if n==1: return
    if isprime(n): out[n]=out.get(n,0)+1; return
    # trial small first
    d=rho(n); factor(d,out); factor(n//d,out)
def divisors(fac):
    ds=[1]
    for q,e in fac.items():
        ds=[d*q**i for d in ds for i in range(e+1)]
    return sorted(ds)
res=[]
for p in [11,23,29,37,41,43,47,53,59,67,71,73,79,83,97]:
    N=2**p-1; fac={}; factor(N,fac); ds=divisors(fac); w=len(fac); tau=len(ds)
    assert all((q-1)%(2*p)==0 and q%8 in (1,7) for q in fac)
    line=[p,w,tau]
    for th in [0.25,1/3,0.5]:
        s=int(N**th)+1
        while math.gcd(s,N)!=1: s+=1
        R=len({d%s for d in ds})
        # check lemma for D'=all divisors and D'=upper half
        assert th*w <= 1+math.log2(R)+1e-9
        up=[d for d in ds if d*d>N]; Ru=len({d%s for d in up})
        assert th*w <= 1+math.log2(Ru)+math.log2(tau/len(up))+1e-9
        line.append((round(th,3),R))
    # natural moduli: 2^k, k=ceil(p/4)+1 ; Phi_2p(2)
    k=p//4+2; R2=len({d%2**k for d in ds}); Q=(2**p+1)//3; RQ=len({d%Q for d in ds})
    line.append(('2^k',k,R2,'Phi2p',RQ))
    print(line)
print("all Lemma O checks passed")
