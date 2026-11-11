# Level-2 top-piece coefficient for m = m1*r (r prime, r ∤ m1): c = [y^K] Psi_m^3 = -[y^K] Phi_m^{-3}, K = m-3phi(m)+1 < m.
# Phi_m(y) = Phi_{m1}(y^r)/Phi_{m1}(y) => Phi_m^{-3} = Phi_{m1}(y)^3 * Phi_{m1}(y^r)^{-3}.
import sys, numpy as np
from sympy import divisors, factorint
from sympy.functions.combinatorial.numbers import mobius
PRIMES = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549]
def cyclo_power_mod(m, e, N, p):   # Phi_m(y)^e mod y^N mod p, e integer (sign allowed)
    a = np.zeros(N, dtype=np.int64); a[0] = 1
    for d in divisors(m):
        if d >= N: continue
        k = e * int(mobius(m//d))      # multiply by (1-y^d)^k
        for _ in range(abs(k)):
            if k > 0: a[d:] = (a[d:] - a[:-d]) % p
            else:
                L = -(-N//d)*d; b = np.zeros(L, dtype=np.int64); b[:N] = a
                b = np.cumsum(b.reshape(-1, d), axis=0) % p; a = b.reshape(-1)[:N]
    return a
def crt(rs):
    x, M = 0, 1
    for r_, p in zip(rs, PRIMES):
        x = x + M * ((r_ - x) * pow(M, -1, p) % p); M *= p
    return x - M if x > M//2 else x
m1 = 111546435; r = int(sys.argv[1]); m = m1*r
phi = 1
for q, e in factorint(m).items(): phi *= (q-1)*q**(e-1)
K = m - 3*phi + 1; print('m', m, 'm/phi %.4f' % (m/phi), 'K', K, flush=True)
vals = []
for p in PRIMES:
    A = cyclo_power_mod(m1, 3, K+1, p)             # Phi_{m1}^3 mod y^{K+1}
    B = cyclo_power_mod(m1, -3, K//r + 1, p)       # Phi_{m1}^{-3} mod u^{K//r+1}
    idx = K - r*np.arange(0, K//r + 1)
    prod = (A[idx] * B) % p
    tot = 0
    for i in range(0, len(prod), 1 << 20): tot = (tot + int(prod[i:i+(1 << 20)].sum())) % p
    vals.append((-tot) % p); print('  prime done', flush=True)
c = crt(vals); print('level 2: c =', c, '->', 'GOOD' if c < 0 else 'bad', flush=True)
