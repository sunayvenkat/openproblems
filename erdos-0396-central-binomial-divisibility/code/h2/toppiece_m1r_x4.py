# Extend a six-prime result of toppiece_m1r.py to ten primes: compute residues for 4 extra primes only,
# recover the six old residues as c6 mod p, and CRT over all ten.  Usage: python toppiece_m1r_x4.py r c6
import sys, numpy as np
from sympy import divisors, factorint
from sympy.functions.combinatorial.numbers import mobius
OLD = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549]
NEW = [2147483543, 2147483497, 2147483489, 2147483477]
def cyclo_power_mod(m, e, N, p):   # Phi_m(y)^e mod y^N mod p
    a = np.zeros(N, dtype=np.int64); a[0] = 1
    for d in divisors(m):
        if d >= N: continue
        k = e * int(mobius(m//d))
        for _ in range(abs(k)):
            if k > 0: a[d:] = (a[d:] - a[:-d]) % p
            else:
                L = -(-N//d)*d; b = np.zeros(L, dtype=np.int64); b[:N] = a
                b = np.cumsum(b.reshape(-1, d), axis=0) % p; a = b.reshape(-1)[:N]
    return a
def crt(rs, ps):
    x, M = 0, 1
    for r_, p in zip(rs, ps):
        x = x + M * ((r_ - x) * pow(M, -1, p) % p); M *= p
    return x - M if x > M//2 else x
m1 = 111546435; r = int(sys.argv[1]); c6 = int(sys.argv[2]); m = m1*r
phi = 1
for q, e in factorint(m).items(): phi *= (q-1)*q**(e-1)
K = m - 3*phi + 1; print('m', m, 'K', K, flush=True)
vals = [c6 % p for p in OLD]
for p in NEW:
    A = cyclo_power_mod(m1, 3, K+1, p); B = cyclo_power_mod(m1, -3, K//r + 1, p)
    prod = (A[K - r*np.arange(0, K//r + 1)] * B) % p
    tot = 0
    for i in range(0, len(prod), 1 << 20): tot = (tot + int(prod[i:i+(1 << 20)].sum())) % p
    vals.append((-tot) % p); print('  prime done', flush=True)
c = crt(vals, OLD + NEW)
print('level 2 (10 primes): c =', c, '->', 'GOOD' if c < 0 else 'bad', '| matches 6-prime:', c == c6, flush=True)
