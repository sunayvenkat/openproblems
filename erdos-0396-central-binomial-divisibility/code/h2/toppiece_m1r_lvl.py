# Level-s top-piece coefficient for m = m1*r (r prime, r ∤ m1), ten-prime CRT.  Usage: python toppiece_m1r_lvl.py r s
# c_s = [y^K] Psi_m^{s+1} = (-1)^{s+1} [y^K] Phi_m^{-(s+1)},  K = m-(s+1)phi(m)+1 < m,
# Phi_m^{-e} = Phi_{m1}(y)^e * Phi_{m1}(y^r)^{-e};  Phi_{m1}^e is a polynomial of degree e*phi(m1), so A is finite.
import sys, numpy as np
from sympy import divisors, factorint
from sympy.functions.combinatorial.numbers import mobius
PRIMES = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549,
          2147483543, 2147483497, 2147483489, 2147483477]
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
def crt(rs):
    x, M = 0, 1
    for r_, p in zip(rs, PRIMES):
        x = x + M * ((r_ - x) * pow(M, -1, p) % p); M *= p
    return x - M if x > M//2 else x
m1 = int(sys.argv[3]) if len(sys.argv) > 3 else 111546435
phi1 = 1
for q, ex in factorint(m1).items(): phi1 *= (q-1)*q**(ex-1)
r = int(sys.argv[1]); s = int(sys.argv[2]); e = s + 1; m = m1*r
phi = 1
for q, ex in factorint(m).items(): phi *= (q-1)*q**(ex-1)
K = m - e*phi + 1; degA = e*phi1
a0 = max(0, -(-(K - degA)//r))                  # smallest a with K - r*a <= degA
print('m', m, 'm/phi %.4f' % (m/phi), 'level', s, 'K', K, 'degA', degA, 'a0', a0, flush=True)
vals = []
for p in PRIMES:
    A = cyclo_power_mod(m1, e, min(K, degA) + 1, p)
    B = cyclo_power_mod(m1, -e, K//r + 1, p)
    aa = np.arange(a0, K//r + 1)
    prod = (A[K - r*aa] * B[aa]) % p
    tot = 0
    for i in range(0, len(prod), 1 << 20): tot = (tot + int(prod[i:i+(1 << 20)].sum())) % p
    vals.append(tot if e % 2 == 0 else (-tot) % p); print('  prime done', flush=True)
c = crt(vals)
print('level %d: c = %d -> %s' % (s, c, 'GOOD' if c < 0 else 'bad'), flush=True)
