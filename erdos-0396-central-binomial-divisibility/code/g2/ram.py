# Check: log Q_1(y) = sum_{N<m} c_m(N) y^N / N  (mod y^m), c_m = Ramanujan sum = mu(m/g) phi(g), g = gcd(m,N);
# and the peak lemma  log|Psi_m(zeta_q^b)| = chi(b) (-1)^r 2^r B_q + log|1 - zeta_q^{bm}|  for p == chi-nonresidues.
import cmath, math
from fractions import Fraction as Fr
from math import gcd
from core2 import Qk_series, phi, pf, logQ
import numpy as np

def mu(n): return 0 if any(n % (p * p) == 0 for p in pf(n)) else (-1) ** len(pf(n))
for m in (105, 1155):
    N = m - 1; Q = [Fr(int(v)) for v in Qk_series(m, 1, N)]
    # log series of Q: L' = Q'/Q
    L = [Fr(0)] * (N + 1)
    for n in range(1, N + 1):   # n L_n = n Q_n - sum_{j=1}^{n-1} j L_j Q_{n-j}
        L[n] = (n * Q[n] - sum(j * L[j] * Q[n - j] for j in range(1, n))) / n
    assert all(L[n] == Fr(mu(m // gcd(m, n)) * phi(gcd(m, n)), n) for n in range(1, N + 1)), m
    print(m, 'log Q = sum c_m(N) y^N/N  OK')

B = {8: math.log(1 + 2 ** .5) / 2, 12: math.log(2 + 3 ** .5) / 2, 10: math.log((1 + 5 ** .5) / 2)}
chi = {8: {1: 1, 3: -1, 5: -1, 7: 1}, 12: {1: 1, 5: -1, 7: -1, 11: 1}, 10: {1: 1, 3: -1, 7: -1, 9: 1}}
for q, m in ((8, 2145), (8, 1181895), (8, 43730115), (12, 327845), (10, 106743), (10, 3949491)):
    r = len(pf(m))
    for b in chi[q]:
        num = logQ(m, np.array(0.0), np.array(b / q)).real
        pred = chi[q][b] * (-1) ** r * 2 ** r * B[q] + math.log(abs(1 - cmath.exp(2j * math.pi * b * m / q)))
        assert abs(num - pred) < 1e-8 * max(1, abs(pred)), (q, m, b, num, pred)
    print(q, m, 'r', r, 'peak lemma OK: log|Psi(zeta_q)| =', round(float(logQ(m, np.array(0.0), np.array(1 / q)).real), 4))
