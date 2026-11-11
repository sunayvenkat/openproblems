# Check: top-piece level-1 first coefficient c_{E+1} = -R(phi-1), R = autocorrelation of the
# coefficients of the inverse cyclotomic polynomial Psi_m = (y^m-1)/Phi_m.  Also re-test the
# Aurifeuillean integrality claim at random y (not divisible by m).
import sys, random
sys.path.insert(0, '..')
from poly import cyclo, divmod_monic
from aurif3 import aur3, phi
from frac import pdivmod, pmul, ev
from fractions import Fraction as Fr

def psi(m):
    q, r = divmod_monic([-1] + [0] * (m - 1) + [1], list(cyclo(m))); assert not r; return q
for m, expect in ((105, 3), (165, -1), (195, -4), (1155, 263), (1365, -75)):
    ps = psi(m); h = phi(m) - 1
    R = sum(ps[i] * ps[i + h] for i in range(len(ps) - h))
    print(m, 'c_{E+1} =', -R, 'expected', expect, 'OK' if -R == expect else 'MISMATCH')

m = 123; F = aur3(m); Fm = [v * (-1) ** i for i, v in enumerate(F)]
for FF, name in ((F, 'F(y)'), (Fm, 'F(-y)')):
    for t in (2, 3):
        N = [Fr(0)] * (2 * m + 1); N[0] = Fr(1); N[2 * m] = Fr(m ** m)
        G = [Fr(1)]
        for _ in range(t): G = pmul(G, [Fr(v) for v in FF])
        P, Rm = pdivmod(N, G)
        for _ in range(5):
            y = random.randrange(10**6, 10**9)
            Py = ev(P, y)
            assert Py.denominator == 1, (name, t, y, Py)
            Ni = (m * y * y) ** m + 1; Gi = int(ev([Fr(v) for v in FF], y)) ** t
            assert Ni // Gi == Py or Ni // Gi == Py - 1
            carry = (2 * Ni // Gi) % 2 == 1
            tailneg = Ni // Gi == Py - 1
            assert carry == tailneg
        print(name, 't', t, 'P(y) integral at random y; carry' if tailneg else 'P(y) integral at random y; no carry')
