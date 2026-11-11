"""Scan Lemma A (non-top pieces d<m good) and Lemma C (top piece d=m good) with early exit.
python lemmaAC_scan.py A MMAX | C MMAX"""
import sys, os
sys.path.insert(0, '..')
from lemC import series_pow_cyclo, divisors, phi
from math import gcd

def first_sign(m, d, s):
    delta = phi(2 * d); E = m - (s + 1) * delta; N = m + 2 * delta + 5
    c = series_pow_cyclo(2 * d, -(s + 1), N)
    for t in range(E + 1, N + 1):
        v = c[t] + (c[t - m] if t >= m else 0)
        if v: return 1 if v > 0 else -1
    return 0

def good(m, d):
    delta = phi(2 * d)
    for s in range(1, m // delta):
        if first_sign(m, d, s) < 0: return s
    return None

mode, MM = sys.argv[1], int(sys.argv[2])
if mode == 'A':
    bad = []
    for m in range(3, MM + 1, 2):
        for d in divisors(m):
            if d < m and good(m, d) is None: bad.append((m, d))
    print("Lemma A counterexamples (m,d), d<m, m odd <=", MM, ":", bad)
else:
    rad = lambda n: [p for p in range(3, n + 1, 2) if n % p == 0 and all(p % q for q in range(3, int(p**.5) + 1, 2))]
    res = []
    for m in range(3, MM + 1, 2):
        if 2 * phi(m) < m:
            g = good(m, m); res.append((m, g)); print(m, rad(m), round(phi(m)/m, 3), 'GOOD at s=%s' % g if g else 'BAD', flush=True)
