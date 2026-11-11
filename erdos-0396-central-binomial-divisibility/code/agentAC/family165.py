# Cross-check: 165p and 195p are fully good for primes p beyond the inheritance bound (2*phi(seed)).
from sympy import primerange
from fullgood import full_good
for seed, lo in ((165, 161), (195, 193)):
    res = [(p, full_good(seed * p)) for p in primerange(lo, lo + 260)]
    print(seed, 'primes tested', len(res), 'all fully good:', all(not b for _, b in res), [p for p, b in res if b])
