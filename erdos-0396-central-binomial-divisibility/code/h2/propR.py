# Checks for §13.6: G = {m : m | C(2m,m)} is not stable under m -> pm, and Proposition R (n in E_k iff n-i in G_{>2k}, primes > 2k part).
from sympy import factorint
import random
def carries(n, q):
    c = 0; t = 2*n
    while t:
        t //= q
        if t & 1: c += 1
    return c
def inG(m, z=1):
    return all(carries(m, q) >= e for q, e in factorint(m).items() if q > z)
G = [m for m in range(2, 100001) if inG(m)]
print('density', len(G)/1e5, 'P(2m in G | m in G)', sum(inG(2*m) for m in G)/len(G), 'P(3m in G | m in G)', sum(inG(3*m) for m in G)/len(G))
random.seed(1); k = 3; bad = 0
for _ in range(3000):
    n = random.randrange(10**6, 10**7)
    primes = set().union(*[factorint(n-i) for i in range(k+1)])
    lhs = all(carries(n, q) >= sum(factorint(n-i).get(q, 0) for i in range(k+1)) for q in primes if q > 2*k)
    rhs = all(inG(n-i, 2*k) for i in range(k+1))
    bad += (lhs != rhs)
print('Prop R mismatches:', bad, 'of 3000')
