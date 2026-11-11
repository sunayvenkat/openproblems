# Route (a): monic depressed quartic f(X) = X^4 + pX^2 + qX + r.  f - c = (X^2+sX+t)(X^2-sX+u) with
# t+u-s^2 = p, s(u-t) = q, tu = r-c  <=>  r - c = phi(s),  4 phi(s) = (p+s^2)^2 - q^2/s^2.
# n(X) = f(X)/h has 4 factoring shifts iff phi(s_i) = r - i h: two AP conditions, LINEAR in (p, Q = q^2).
# So every s in Q^4 gives (p, Q); we need Q to be a rational square.
import sys
from fractions import Fraction as Fr
from math import isqrt

def sqrt_fr(Q):
    if Q < 0: return None
    a, b = isqrt(Q.numerator), isqrt(Q.denominator)
    return Fr(a, b) if a * a == Q.numerator and b * b == Q.denominator else None

def solve(s):
    S2 = [Fr(x * x) for x in s]
    W = ((1, -2, 1, 0), (0, 1, -2, 1))
    a = [sum(c * x for c, x in zip(wt, S2)) for wt in W]
    b = [sum(c * x * x for c, x in zip(wt, S2)) for wt in W]
    c = [sum(c / x for c, x in zip(wt, S2)) for wt in W]
    det = a[0] * c[1] - a[1] * c[0]
    if det == 0 or a[0] == 0: return None
    Q = (a[0] * b[1] - a[1] * b[0]) / det
    p = (Q * c[0] - b[0]) / (2 * a[0])
    return p, Q

def phi(p, q, s): return ((p + s * s) ** 2 - q * q / (s * s)) / 4

def family(s):
    """(p, q, r, h, [(s_i, t_i, u_i)]) with f(X) - i h = prod over shift i, or None."""
    sol = solve(s)
    if not sol: return None
    p, Q = sol
    q = sqrt_fr(Q)
    if q is None: return None
    ph = [phi(p, q, Fr(x)) for x in s]
    h = ph[0] - ph[1]
    if h == 0: return None
    if h < 0: s, ph, h = s[::-1], ph[::-1], -h
    assert all(ph[0] - ph[i] == i * h for i in range(4))
    fac = [(Fr(x), (p + x * x - q / x) / 2, (p + x * x + q / x) / 2) for x in s]
    return p, q, ph[0], h, fac

if __name__ == "__main__":
    S = int(sys.argv[1])
    out = []
    for s0 in range(1, S + 1):
        for s1 in range(1, S + 1):
            for s2 in range(1, S + 1):
                for s3 in range(1, S + 1):
                    if len({s0, s1, s2, s3}) < 4 or (s0, s1) > (s3, s2): continue
                    fam = family((s0, s1, s2, s3))
                    if fam and fam[1] != 0: out.append(((s0, s1, s2, s3), fam[:4]))
    print(len(out), "families with q != 0, s_i <=", S)
    for s, f in out[:40]: print(s, [str(v) for v in f])
