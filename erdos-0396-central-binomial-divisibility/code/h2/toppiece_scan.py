# Exact top-piece level-1 sign for all odd m <= B with m/phi(m) >= 2 (T=2 => single level): c_1 = [y^{m-2phi+1}] Psi_m^2.
import sys, numpy as np
from sympy import divisors, totient
from sympy.functions.combinatorial.numbers import mobius
B = int(sys.argv[1]); good = bad = 0; rows = []
for m in range(3, B+1, 2):
    phi = int(totient(m))
    if m < 2*phi: continue
    K0 = m - 2*phi + 1; N = K0 + 2*max(1, m//100) + 2   # look for first nonzero at index >= K0
    a = np.zeros(N, dtype=object); a[0] = 1
    for d in divisors(m):
        if d >= N: continue
        mu = int(mobius(m//d))
        if mu == 1:
            for i in range(d, N): a[i] += a[i-d]
        elif mu == -1:
            for i in range(N-1, d-1, -1): a[i] -= a[i-d]
    psi = -a; c = 0; K = K0
    while K < N and c == 0:
        c = sum(int(psi[i])*int(psi[K-i]) for i in range(K+1)); K += 1
    rows.append((m, round(m/phi, 3), int(mobius(m)), K-1-K0, c)); good += c < 0; bad += c >= 0
print('eligible odd m <=', B, ':', len(rows), 'top-good', good, 'top-bad', bad)
for r in rows: print(r)
print('good:', [r[0] for r in rows if r[4] < 0])
