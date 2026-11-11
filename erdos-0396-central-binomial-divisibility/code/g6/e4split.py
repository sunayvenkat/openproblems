# Which old pieces F (root rho) split after composition: test u + v*rho in Q(rho)^2 via norm + trace criterion.
import sys, sympy as sp
from e4curve import points, gamma_uv
from quartic import sqrt_fr
from fractions import Fraction as Fr
from quartic import family
def is_sq_quad(a, b, s, t):
    """is a + b*rho a square in Q(rho), rho root of X^2 + sX + t (irreducible)?"""
    N = a * a - s * a * b + t * b * b          # norm of a + b rho
    rN = sqrt_fr(N)
    if rN is None: return False
    # a+b rho = (x + y rho)^2 ; trace condition: Tr = 2a - s b ; need (Tr +- 2 sqrtN) = Tr(x+y rho)^2... use: square iff
    # (Tr + 2 rN) is (x+y rho + conj)^2 = (2x - s y)^2  rational square for some sign, with discriminant factor:
    tr = 2 * a - s * b
    for sg in (1, -1):
        val = tr + 2 * sg * rN                # = (sigma + sigma')^2 where sigma^2 = a + b rho
        if val != 0 and sqrt_fr(val) is not None: return True
    return False
P, Q, R, H, e, B = [int(t) for t in sys.argv[1:7]]
s_list = [tuple(int(z) for z in t.split(',')) for t in sys.argv[7:]]   # (s,t,u) of old shifts in X-scaled form
for c2, y in points(P, Q, R - e * H, B):
    if y == 0: continue
    for yy in (y, -y):
        u, v, _, _ = gamma_uv(sp.Rational(P), sp.Rational(Q), sp.Rational(R - e * H), sp.Rational(c2), sp.Rational(yy))
        if v <= 0: continue
        u, v = Fr(int(u.p), int(u.q)), Fr(int(v.p), int(v.q))
        sp_ = [(is_sq_quad(u, v, s, t), is_sq_quad(u, v, -s, uu)) for s, t, uu in s_list]
        print(str(c2), str(yy), sp_)
