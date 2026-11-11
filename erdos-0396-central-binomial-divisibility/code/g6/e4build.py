# Build x(w) from a curve point and verify f(x(w)) + c factors into two quartics (and shifts keep their pieces).
import sys, sympy as sp
from e4curve import gamma_uv
w, X = sp.symbols('w X')
p, q, r, h = [sp.Rational(v) for v in sys.argv[1:5]]
shift = sp.Rational(sys.argv[5])               # m(X) = f(X) - shift*h
c2, y = sp.Rational(sys.argv[6]), sp.Rational(sys.argv[7])
rp = r - shift * h
for yy in (y, -y):
    u, v, z2, z3 = gamma_uv(p, q, rp, c2, yy)
    assert z2 == 0 and z3 == 0
    if v <= 0: print("y =", yy, "v =", v, "<= 0, skip"); continue
    # x(w) = a2 w^2 + a0 (a1 = 0):  -4 a2 a0 = mu^2 u, 4 a2 = mu^2 v.  Take mu = 1.
    a2 = v / 4; a0 = -u / v
    xw = a2 * w**2 + a0
    m = sp.expand((xw**4 + p * xw**2 + q * xw + rp))
    fl = sp.factor_list(m)
    print("y =", yy, "u, v =", u, v, " x(w) =", xw, " factor degrees:", [sp.degree(f, w) for f, e in fl[1]])
    for f, e in fl[1]: print("    ", sp.expand(f))
