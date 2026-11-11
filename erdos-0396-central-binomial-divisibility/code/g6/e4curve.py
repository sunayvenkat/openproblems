# E_4 by composition: n(w) = f(x(w))/h.  Shift 4: m(X) = f(X) - 4h = X^4 + pX^2 + qX + r'.  f(x(w)) - 4h splits into two
# rational quartics if disc(x(w) - theta) = gamma^2 in Q(theta), gamma = c0 + c1 th + c2 th^2 + th^3.  Eliminating c0, c1:
# need y^2 = m(c2) = c2^4 + p c2^2 + q c2 + r'  (genus 1), then c1 = c2^2 + p + y, c0 = (q + 2 p c2 - 2 c1 c2)/2.
import sys, sympy as sp
from fractions import Fraction as Fr
from math import isqrt, gcd
th, w = sp.symbols('theta w')

def points(p, q, rp, B):
    out = []
    for nn in range(1, B + 1):
        for m in range(-B, B + 1):
            if gcd(m, nn) != 1: continue
            Y2 = m**4 + p * m * m * nn * nn + q * m * nn**3 + rp * nn**4
            if Y2 >= 0 and isqrt(Y2) ** 2 == Y2: out.append((Fr(m, nn), Fr(isqrt(Y2), nn * nn)))
    return out

def gamma_uv(p, q, rp, c2, y):
    c1 = c2 * c2 + p + y; c0 = (q + 2 * p * c2 - 2 * c1 * c2) / 2
    m = sp.Poly(th**4 + p * th**2 + q * th + rp, th)
    g2 = sp.rem(sp.Poly((c0 + c1 * th + c2 * th**2 + th**3)**2, th), m)
    cs = [sp.Rational(c) for c in reversed(g2.all_coeffs())]
    return (cs + [0] * 4)[:4]                                          # [u, v, 0, 0] expected

if __name__ == "__main__":
    p, q, r, h = [Fr(sp.Rational(x)) for x in sys.argv[1:5]]
    rp = r - 4 * h
    assert p.denominator == q.denominator == rp.denominator == 1
    pts = points(int(p), int(q), int(rp), int(sys.argv[5]))
    print("points on y^2 = m(c):", [(str(a), str(b)) for a, b in pts[:10]], len(pts))
    for c2, y in pts[:6]:
        for yy in (y, -y):
            print(" c2 =", c2, "y =", yy, "gamma^2 = u + v theta + ...:", gamma_uv(sp.Rational(p), sp.Rational(q), sp.Rational(rp), sp.Rational(c2), sp.Rational(yy)))
