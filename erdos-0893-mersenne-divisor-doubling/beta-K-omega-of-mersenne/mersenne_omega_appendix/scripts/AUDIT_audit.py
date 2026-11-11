import itertools, math, cmath, random
from math import gcd, comb, log
random.seed(7)
B=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def sprp(n):
    if n<2: return False
    for q in B:
        if n%q==0: return n==q
    d,r=n-1,0
    while d%2==0: d//=2; r+=1
    for a in B+[random.randrange(2,n-1) for _ in range(10)]:
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True

# 1. Lemma O brute force on random N, s
def divisors(fac):
    ds=[1]
    for q,e in fac:
        ds=[d*q**k for d in ds for k in range(e+1)]
    return ds
smallp=[q for q in range(3,200) if sprp(q)]
viol=0;tests=0
for trial in range(3000):
    w=random.randint(2,6); qs=random.sample(smallp,w)
    fac=[(q,random.randint(1,2)) for q in qs]; N=1
    for q,e in fac: N*=q**e
    ds=divisors(fac); tau=len(ds)
    s=random.randint(2,N+5)
    if gcd(s,N)!=1: continue
    th=min(1.0, math.log(s-0.5)/math.log(N))  # s>N^th
    # worst D': largest fibre classes; check every prefix of classes sorted by size
    cls={}
    for d in ds: cls.setdefault(d%s,[]).append(d)
    sz=sorted((len(v) for v in cls.values()),reverse=True)
    tot=0
    for R,c in enumerate(sz,1):
        tot+=c; tests+=1
        if th*w > 1+math.log2(R)+math.log2(tau/tot)+1e-9: viol+=1
print("1 LemmaO tests",tests,"violations",viol)

# 2. incidence/norm lemma p=29,43
def vq(n,q):
    k=0
    while n%q==0: n//=q;k+=1
    return k
for p,qs in [(29,[233,1103,2089]),(43,[431,9719,2099863]),(11,[23,89])]:
    M=2**p-1
    for q in qs:
        assert M%q==0
        roots=[pow(2,j,q) for j in range(1,p)]; assert len(set(roots))==p-1
        # v_Q(zeta-2^j): via Phi_p(2^j)
        for j in range(1,p):
            Pj=(2**(j*p)-1)//(2**j-1); assert vq(Pj,q)==vq(M,q)
    ok=True
    for t in range(200):
        T=random.randint(1,6); P={random.randrange(p):random.choice([-1,1,2,-3]) for _ in range(T)}
        l1=sum(abs(c) for c in P.values())
        Nlog=sum(math.log(abs(sum(c*cmath.exp(2j*math.pi*e*k/p) for e,c in P.items()))) for k in range(1,p))
        lhs=sum(math.log(gcd(sum(c*2**(e*j) for e,c in P.items()),M)) for j in range(1,p))
        if not (lhs<=Nlog+1e-6 and Nlog<=(p-1)*math.log(l1)+1e-6): ok=False;print("2 FAIL",p,P,lhs,Nlog)
    print("2 norm-lemma p",p,"ok",ok)
# M_11 = 23*89, v check with square: none; test LTE on 1093^2 | 2^364-1? skip

# 3 Minkowski constant for Q(zeta_p)
for p in [43,223,397]:
    n=p-1; lC=(n/2)*math.log(4/math.pi)+math.lgamma(n+1)-n*math.log(n)+(p-2)/2*math.log(p)
    print(f"3 p={p} log C_K={lC:.1f}  log M_p={p*math.log(2):.1f}")

# 5 explicit u
def find(p,q,T):
    seen={}
    for A in itertools.combinations(range(p),T):
        r=sum(pow(2,a,q) for a in A)%q
        if r in seen: return seen[r],A
        seen[r]=A
for p,q in [(43,9719),(223,196687)]:
    A,Bs=find(p,q,3); u=sum(2**a for a in A)-sum(2**b for b in Bs)
    print("5 p",p,"A",A,"B",Bs,"gcd",gcd(u,2**p-1), "u%q",u%q)

# 7 E4 and Jacobi identity
def prim_root(q):
    f=[r for r in range(2,q) if (q-1)%r==0 and sprp(r)]
    for g in range(2,q):
        if all(pow(g,(q-1)//r,q)!=1 for r in f): return g
bad=0;cnt=0
for q in [x for x in range(5,400) if sprp(x)]:
    g=prim_root(q); ind={pow(g,k,q):k for k in range(q-1)}
    for o in [d for d in range(3,q) if (q-1)%d==0]:
        for t in [1]:
            chi=lambda a,o=o: 0 if a%q==0 else cmath.exp(2j*math.pi*ind[a%q]/o)
            rho=lambda a: 0 if a%q==0 else (-1)**ind[a%q]
            J1=sum(chi(a)*chi(1-a) for a in range(q)); J2=sum(chi(a)*rho(1-a) for a in range(q))
            cnt+=1
            if abs(J1-chi(4).conjugate()*J2)>1e-6: bad+=1
print("7 Jacobi identity tests",cnt,"bad",bad)
# E4: q|M_p, n|q-1, p∤n => 2 n-th power
e4bad=0
for p,qs in [(29,[233,1103,2089]),(43,[431,9719,2099863]),(23,[47,178481])]:
    for q in qs:
        for n in range(1,min(q,5000)):
            if (q-1)%n==0 and n%p and pow(2,(q-1)//n,q)!=1: e4bad+=1
print("7 E4 bad",e4bad)

# 9 Phi_{2p}(2) mod 8 and factor residues (use small factors only, full for small p)
def factor(n):
    out=[];d=2
    while d*d<=n and d<10**6:
        while n%d==0: out.append(d); n//=d
        d+=1
    return out,n
b9=0
for p in [x for x in range(5,90) if sprp(x)]:
    Phi=(2**p+1)//3; assert Phi%8==3
    fs,rest=factor(Phi)
    if rest>1 and sprp(rest): fs.append(rest); rest=1
    if rest!=1: continue
    for Q in fs:
        if (Q%8==3)!=(((Q-1)//(2*p))%2==1) or Q%8 not in (1,3): b9+=1
    if sum(1 for Q in fs if Q%8==3)%2!=1: b9+=1
print("9 bad",b9)

# 10 M_397
fs=[2383,6353,50023,53993,202471,5877983,814132872808522587940886856743,1234904213576000272542841146073,6597485910270326519900042655193]
M=2**397-1; prod=1
for f in fs: prod*=f
print("10 all divide",all(M%f==0 for f in fs),"prps",[sprp(f) for f in fs])
print("10 pairwise coprime",all(gcd(a,b)==1 for a,b in itertools.combinations(fs,2)),"cofactor bits",(M//prod).bit_length() if M%prod==0 else "prod does not divide", "cof prp", sprp(M//prod) if M%prod==0 else None)
for f in fs: assert (f-1)%(2*397)==0 and f%8 in (1,7)

# 11 trivial bound
for p in [10**3,10**5,10**7,10**9]:
    k=1
    while k*math.log(2*p*k/math.e)<p*math.log(2): k+=1
    print("11 p",p,"kmax*log p/p",(k-1)*math.log(p)/p, "target",math.log(2)/2)

# 12 Wagstaff
W=[p for p in range(5,2001) if sprp(p) and sprp((2**p+1)//3)]
print("12",W)
