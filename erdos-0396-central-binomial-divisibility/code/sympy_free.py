def factor_small(n):
    f=[];p=2
    while p*p<=n:
        while n%p==0: f.append(p); n//=p
        p+=1
    if n>1: f.append(n)
    return f
def sqfree_divisors_mu(primes):
    out=[(1,1)]
    for p in primes: out+= [(d*p,-mu) for d,mu in out]
    return out
