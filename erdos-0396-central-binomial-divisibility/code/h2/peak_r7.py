# r = 7 exponents with all primes = +-3 mod 8, m/phi >= 2: exact sgn c(m) (series mod 6 primes + CRT) vs largest trace term.
import sys, numpy as np
from sympy import primerange
from toppiece_rscan import window, ALLP
from trace_peak import terms
def crt(rs, ps):
    x, M = 0, 1
    for r_, p in zip(rs, ps): x = x + M * ((r_ - x) * pow(M, -1, p) % p); M *= p
    return x - M if x > M // 2 else x
P = [p for p in primerange(3, 200) if p % 8 in (3, 5)]
ms = []
def rec(i, m, ra, n):
    if n == 7:
        if ra >= 2 and m <= int(sys.argv[1]): ms.append(m)
        return
    for j in range(i, len(P)):
        if m * P[j] > int(sys.argv[1]): break
        rec(j + 1, m * P[j], ra * P[j] / (P[j] - 1), n + 1)
rec(0, 1, 1.0, 0); ms.sort(); print(len(ms), 'm', flush=True)
for m in ms[:int(sys.argv[2])]:
    c = crt([int(window(m, 2, 0, p)[0]) for p in ALLP[:6]], ALLP[:6])
    a, phi, logR, S, th = terms(m); L = logR.max()
    v = -2 * np.exp(2 * (logR - L)) * ((m + phi - 1) * np.cos(th) + S * np.sin(th))
    j = np.argmax(np.abs(v)); share = abs(v[j]) / np.abs(v).sum()
    print(m, 'exact', 'good' if c < 0 else 'bad', '| float sum sign ok', np.sign(v.sum()) == np.sign(c), '| top-term ok', np.sign(v[j]) == np.sign(c), '| share %.2f' % share, flush=True)
