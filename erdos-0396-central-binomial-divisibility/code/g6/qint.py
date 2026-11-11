# Turn a rational quartic family (p,q,r,h) into integer polynomials n(w) = f(Mw+B)/h and analyze them.
import sys, itertools, sympy as sp
from fractions import Fraction as Fr
from math import lcm, prod
from sympy import factorint
from sympy.ntheory.modular import crt
import check
from check import w, analyze, crt_class, shifts
from quartic import family

def integer_models(p, q, r, h, maxopts=6):
    lam = next(l for l in range(1, 10**6) if all((c * l ** e).denominator == 1 for c, e in ((p, 2), (q, 3), (r, 4))))
    g = [1, 0, int(p * lam ** 2), int(q * lam ** 3), int(r * lam ** 4)]       # Y = lam X
    H = h * lam ** 4; H1, H2 = H.numerator, H.denominator
    Y = sp.Symbol('Y'); gY = sp.Poly(g, Y)
    opts = []
    for P, e in factorint(H1).items():
        if P ** e > 10 ** 5: return []
        o = []
        for a in range(e + 1):
            for y0 in range(P ** a):
                cs = sp.Poly(gY.as_expr().subs(Y, y0 + P ** a * w), w).all_coeffs()
                if all(int(c) % P ** e == 0 for c in cs): o.append((P ** a, y0))
            if o: break
        if not o: return []
        opts.append(o[:maxopts])
    out = []
    for combo in itertools.product(*opts):
        M = prod(m for m, _ in combo)
        B = int(crt([m for m, _ in combo], [y for _, y in combo])[0]) if combo else 0
        n = sp.expand(H2 * gY.as_expr().subs(Y, M * w + B) / H1)
        assert all(c.is_integer for c in sp.Poly(n, w).all_coeffs())
        out.append(((lam, M, B), n))
    return out

def R_values(n, k=3):
    out = []
    for i, (j, ps) in enumerate(shifts(n, k)):
        for f, e in ps:
            C = sp.div(sp.Poly(n - i, w), f)[0]
            out.append((i, f.degree(), sp.Rational(C.LC(), f.LC()) if C.degree() == f.degree() else None))
    return out

if __name__ == "__main__":
    S = int(sys.argv[1])
    for s in itertools.permutations(range(1, S + 1), 4):
        if s[0] > s[3]: continue
        fam = family(s)
        if not fam or fam[1] == 0: continue
        for sub, n in integer_models(*fam[:4]):
            res = analyze(n, 3, verbose=False)
            Rs = [str(R) for _, d, R in R_values(n)]
            tag = "GOOD " + str(crt_class(*res[1:])) if res else "fail " + str(check.LAST if isinstance(check.LAST, tuple) else "")
            print(s, sub, "R:", Rs, tag, flush=True)
