# Closed form for the level-1 top coefficient c(m) = [y^{m-2phi+1}] Psi_m^2 = [y^{m-1}] Phi_m^{-2} (T = 2 convention of 13.7).
# Partial fractions of Phi_m^{-2} at N = m-1, with Phi_m * Psi_m = y^m - 1, give
#   c(m) = (1/m^2) sum_{zeta primitive} zeta Psi(zeta)^2 [ (2m-1) - 2 zeta Psi'(zeta)/Psi(zeta) ],
# and Psi_m(zeta_a) = prod_{e|m, e<m} (zeta_a^e - 1)^{-mu(m/e)} is explicit.  Checks against the series; reports how
# concentrated the sum is (share of the largest terms).
import sys, cmath, math
from sympy import divisors, totient
from sympy.functions.combinatorial.numbers import mobius
from toppiece_rscan import window
def terms(m):
    phi = int(totient(m)); E = [(e, int(mobius(m // e))) for e in divisors(m) if e < m]
    out = []
    for a in range(1, m):
        if math.gcd(a, m) != 1: continue
        z = cmath.exp(2j * math.pi * a / m)
        logpsi = sum(-mu * cmath.log(z**e - 1) for e, mu in E if mu)
        psi = cmath.exp(logpsi)
        dlog = sum(-mu * e * z**e / (z**e - 1) for e, mu in E if mu)     # zeta Psi'/Psi
        out.append((a, z * psi * psi * ((2*m - 1) - 2 * dlog) / m**2))
    return out
for m in map(int, sys.argv[1:]):
    t = terms(m); c = sum(v for _, v in t)
    ex = window(m, 2, 0)[0]
    mags = sorted((abs(v) for _, v in t), reverse=True); tot = sum(mags)
    print('m', m, 'formula %.6f%+.1ej' % (c.real, c.imag), 'series', ex,
          '| top-2 share %.3f top-10 share %.3f of sum|.|' % (sum(mags[:2]) / tot, sum(mags[:10]) / tot), flush=True)
