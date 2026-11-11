# Certificate pairs for the top piece of exponents with all prime factors > P (level 1, e = 2, T = 2).
# m0 = product of the primes in [P+1, Q] (Q minimal with m0/phi0 >= 2).  For prime r = 2 phi0 + 1 - i (i even, small) the
# end-window rule gives sign(top of m0 r) = sign(w_{m0}(0)) * sign(b), b = first nonzero of beta_i, beta_{i+1}, ...,
# beta = Phi_{m0}^2, whose coefficients below D depend only on the divisors of m0 below D.  Two such primes r+ (b > 0) and
# r- (b < 0): one of m0 r+, m0 r- is top-good, unless w_{m0}(0) = 0 (then both inherit m0's first window sign).
# Usage: python topcert.py P D [extra]
import sys, numpy as np
from sympy import primerange, isprime
from math import prod
P, D = int(sys.argv[1]), int(sys.argv[2]); extra = int(sys.argv[3]) if len(sys.argv) > 3 else 0   # extra primes beyond ratio 2
Q, ratio = [], 1.0
for p in primerange(P + 1, 10**7):
    Q.append(p); ratio *= p / (p - 1)
    if ratio >= 2:
        if extra == 0: break
        extra -= 1
m0 = prod(Q); phi0 = prod(p - 1 for p in Q); mu = (-1) ** len(Q)
print('P', P, 'primes', Q[0], '..', Q[-1], '(%d)' % len(Q), 'm0/phi0 %.5f' % (m0 / phi0), 'digits', len(str(m0)), 'mu', mu, flush=True)
assert 2 <= m0 / phi0 < 3
divs = [(1, 0)]                                  # (d, omega(d)) with d < D
for p in Q:
    if p >= D: break
    divs += [(d * p, w + 1) for d, w in divs if d * p < D]
print('divisors below D:', len(divs), flush=True)
beta = np.zeros(D, dtype=object); beta[0] = 1   # Phi_{m0}^2 mod y^D, exact
for d, w in sorted(divs):
    k = 2 * mu * (-1) ** w                      # exponent of (1 - y^d): 2*mu(m0/d)
    for _ in range(abs(k)):
        if k > 0: beta[d:] = beta[d:] - beta[:-d]
        else:
            for j in range(d, D): beta[j] += beta[j - d]
cands = []
for i in range(0, D - 50, 2):
    r = 2 * phi0 + 1 - i
    if isprime(r):
        b = next((int(x) for x in beta[i:] if x), None)
        if b is None: continue
        cands.append((i, b)); print('  i = %d: r = 2 phi0 + 1 - %d prime, b = %d' % (i, i, b), flush=True)
pos = [c for c in cands if c[1] > 0]; neg = [c for c in cands if c[1] < 0]
print('primes found', len(cands), ' b>0:', len(pos), ' b<0:', len(neg))
if pos and neg: print('CERTIFICATE: one of m0*(2phi0+1-%d), m0*(2phi0+1-%d) is top-good (unless w_m0(0) = 0)' % (pos[0][0], neg[0][0]))
