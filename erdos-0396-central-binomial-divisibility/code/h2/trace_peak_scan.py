# For all squarefree m <= MMAX built from primes = +-3 mod 8 with m/phi >= 2: does the single largest trace term
# predict sgn c(m)?  Exact c(m) from the series (window) when m <= EXACT, else float trace sum.
import sys, itertools, math, numpy as np
from sympy import primerange
from trace_peak import terms
from toppiece_rscan import window
MMAX = int(sys.argv[1]); EXACT = int(sys.argv[2])
P = [p for p in primerange(3, 400) if p % 8 in (3, 5)]
ms = []
def rec(i, m, ratio):
    if ratio >= 2: ms.append(m)
    for j in range(i, len(P)):
        if m * P[j] > MMAX: break
        rec(j + 1, m * P[j], ratio * P[j] / (P[j] - 1))
rec(0, 1, 1.0); ms.sort()
agree = tot = 0; rows = []
for m in ms:
    a, phi, logR, S, th = terms(m); L = logR.max()
    v = -2 * np.exp(2 * (logR - L)) * ((m + phi - 1) * np.cos(th) + S * np.sin(th))
    j = np.argmax(np.abs(v)); share = abs(v[j]) / np.abs(v).sum()
    c = window(m, 2, 0)[0] if m <= EXACT else v.sum()
    ok = np.sign(v[j]) == np.sign(c); agree += ok; tot += 1
    rows.append((m, int(math.log2(m) and len([p for p in P if m % p == 0])), '%.2f' % share, 'good' if c < 0 else 'bad', ok))
for r in rows: print(*r)
print('top-term predicts sign:', agree, '/', tot)
