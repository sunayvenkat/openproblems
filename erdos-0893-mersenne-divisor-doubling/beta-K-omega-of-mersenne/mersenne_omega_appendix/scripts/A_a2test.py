# Test Lemma A2 on trinomials P = 1 + x - x^s:
#   sum_q n_q(P) log q  <=  log|N(P(zeta_p))|,  n_q = #{b in (Z/p)^*: q | P(2^b)}
import math, random, cmath

def is_prime(n):
    if n < 2: return False
    for sp in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % sp == 0: return n == sp
    d, r = n-1, 0
    while d % 2 == 0: d//=2; r+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def rho(n):
    if n % 2 == 0: return 2
    while True:
        c = random.randrange(1,n); f = lambda x:(x*x+c)%n
        x=y=random.randrange(2,n); d=1
        while d==1:
            x=f(x); y=f(f(y)); d=math.gcd(abs(x-y),n)
        if d!=n: return d

def factor(n, out):
    if n==1: return
    if is_prime(n): out[n]=out.get(n,0)+1; return
    d=rho(n); factor(d,out); factor(n//d,out)

def logabsnorm(coeffs, p):  # coeffs: dict exp->coef ; log|prod_k P(zeta^k)|
    s=0.0
    for k in range(1,p):
        z=sum(c*cmath.exp(2j*math.pi*k*e/p) for e,c in coeffs.items())
        s+=math.log(abs(z))
    return s

for p in [29,43,47,53,71,73,79]:
    f={}; factor(2**p-1,f)
    qs=sorted(f)
    best=[]
    # solutions E_q = {(x,y): 1+2^x == 2^y mod q}
    cnt={}  # s -> weighted LHS
    for q in qs:
        dl={pow(2,j,q):j for j in range(p)}
        for x in range(1,p):
            y=dl.get((1+pow(2,x,q))%q)
            if y is not None:
                s=y*pow(x,-1,p)%p
                cnt[s]=cnt.get(s,0)+math.log(q)
    ratios=[]
    for s,l in cnt.items():
        r=logabsnorm({0:1,1:1,s:-1},p)
        ratios.append((l/r,s,l,r))
    ratios.sort(reverse=True)
    print(p, qs, 'lines hit:',len(cnt), 'top ratios:',[(round(a,3),s) for a,s,_,_ in ratios[:4]])
