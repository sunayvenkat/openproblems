# Exact level-2 audit of the 127 non-top pieces d | m2 (DRAFT §8.4 table), big integers only (python-flint).
#   w = x^d+1 = f g, f = Phi_{2d}, g = -Psi_d(-x) (monic, deg d-phi(d)).  x^m+1 = sum_r (-1)^{r+1} C(K,r) w^r gives
#   D_0 = 0, D_1 = K g, D_2 = -C(K,2) (g^2 mod f)  when deg g < phi(d) (phi(d)/d > 1/2).
#   A1(b): 3 phi(d) > 2d  =>  g^2 mod f = g^2, lc(D_2) = -C(K,2) < 0: no computation beyond the inequality and T >= 3.
#   else: good at level 2 iff lc(g^2 mod f) > 0 (exact here); the rest must be the 25 deep pieces of exact.py.
# Usage (from code/g4):  python level2.py
import sys, time
from itertools import combinations
from math import prod
from flint import fmpz_poly
from exact import psi, DEC, m2
from fastgood import phi

P = [5, 7, 11, 13, 17, 19, 37]
cnt = {'A1b': 0, 'good-L2': 0, 'deep': 0}
for d in sorted(prod(c) for r in range(len(P)) for c in combinations(P, r)):   # proper divisors only
    dl, K, T = phi(d), m2 // d, m2 // phi(d)
    assert 2 * dl > d and T >= 3 and K >= 3
    if 3 * dl > 2 * d:
        assert d not in DEC; cnt['A1b'] += 1; continue
    if d in DEC:   # certified at a deeper level by exact.py; its level-2 sign is not needed
        cnt['deep'] += 1; continue
    t0 = time.time()
    f = fmpz_poly.cyclotomic(2 * d)
    g = fmpz_poly([-c if i % 2 == 0 else c for i, c in enumerate(psi(d).coeffs())])   # -Psi_d(-x)
    assert g * f == fmpz_poly([1] + [0] * (d - 1) + [1])                                # w = f g exactly
    R = (g * g) % f
    lc = int(R.leading_coefficient())
    assert lc > 0, d
    cnt['good-L2'] += 1
    print(f'd={d} K={K} T={T} deg(g^2 mod f)={R.degree()} (phi-1={dl - 1}) lc={lc} good-L2 {time.time() - t0:.1f}s', flush=True)
print(cnt, flush=True)
assert cnt == {'A1b': 82, 'good-L2': 20, 'deep': 25}
