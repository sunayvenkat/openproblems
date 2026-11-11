# Data checks for W1: alpha_k = 2^k - zeta_p family; Fermat-quotient/Stickelberger symbol; coprimality.
import random, math
def isprime(n):
    if n<2: return False
    for s in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%s==0: return n==s
    d,r=n-1,0
    while d%2==0: d//=2; r+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x=pow(a,d,n)
        if x in(1,n-1): continue
        for _ in range(r-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True
def rho(n):
    if n%2==0: return 2
    while True:
        x=y=random.randrange(2,n); c=random.randrange(1,n); d=1
        while d==1:
            x=(x*x+c)%n; y=(y*y+c)%n; y=(y*y+c)%n; d=math.gcd(abs(x-y),n)
        if d!=n: return d
def factor(n,out):
    if n==1: return
    if isprime(n): out[n]=out.get(n,0)+1; return
    for s in range(2,10**5):
        if n%s==0:
            factor(s,out); factor(n//s,out); return
        if s*s>n: break
    d=rho(n); factor(d,out); factor(n//d,out)
def Phi_p(x,p): return (x**p-1)//(x-1)
def tau(k): return sum(1 for d in range(1,k+1) if k%d==0)
# 1. alpha_k: omega(Phi_p(2^k)) >= tau(k), exactly one prime above each q (2^k has order p mod q)
for p,k in [(5,6),(7,6),(11,6),(13,4),(11,12),(13,12)]:
    N=Phi_p(2**k,p); f={}; factor(N,f)
    ok=all(q==p or pow(2**k,p,q)==1 and pow(2**k,1,q)!=1 for q in f)
    print("p",p,"k",k,"omega",len(f),"tau(k)",tau(k),"order-p check",ok)
    assert len(f)>=tau(k) and ok
# 2. Fermat-quotient = product of chi_q(2)=zeta^{2 m_q}: sum v m == F mod p
for p in [11,23,29,37,41,43,47,53]:
    f={}; factor(2**p-1,f)
    s=sum(v*((q-1)//(2*p)) for q,v in f.items())%p
    F=((2**(p-1)-1)//p)%p
    print("p",p,"sum v m mod p",s,"F mod p",F); assert s==F
# 3. (2-zeta^j),(2-zeta) coprime: gcd(2^{j-1}-1, M_p)=1
for p in [11,23,29]:
    assert all(math.gcd(2**(j-1)-1,2**p-1)==1 for j in range(2,p))
print("all checks passed")
