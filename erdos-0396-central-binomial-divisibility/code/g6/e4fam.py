# E_4 attempt: n'(w) = (f(x(w)) - e*h)/h, e = shift index of the extra (composed) shift (e = -1 or 4).
# x(w) = a2 w^2 + a1 w + a0 in Z[w] with 4 a2 = mu^2 v, a1^2 - 4 a2 a0 = mu^2 u, where u + v theta = gamma^2 in Q(theta).
import sys, itertools, sympy as sp
from fractions import Fraction as Fr
from math import lcm, prod
from sympy import factorint
from sympy.ntheory.residue_ntheory import sqrt_mod
from e4curve import gamma_uv
from check import w, analyze, crt_class
from refine import search
import check

def xpolys(u, v, mus=range(1, 7), per=3):
    for mu in mus:
        a2, D = sp.Rational(v * mu * mu, 4), u * mu * mu
        if not (a2.is_integer and D.is_integer) or a2 <= 0: continue
        a2, D = int(a2), int(D)
        roots = sqrt_mod(D % (4 * a2), 4 * a2, all_roots=True) or []
        for a1 in sorted(roots)[:per]:
            yield a2, a1, (a1 * a1 - D) // (4 * a2)

def integralize(n, maxa=40):
    """w -> M w + B making all coefficients integers (per prime power of the denominators), or None."""
    P = sp.Poly(n, w)
    den = lcm(*[int(sp.Rational(c).q) for c in P.all_coeffs()])
    mods, res = [], []
    for p, e in factorint(den).items():
        hit = None
        for a in range(0, maxa):
            if p ** a > 3 * 10 ** 5: break
            for y0 in range(p ** a):
                cs = sp.Poly(P.as_expr().subs(w, y0 + p ** a * w), w).all_coeffs()
                if all(sp.Rational(c).q % p for c in cs): hit = (p ** a, y0); break
            if hit: break
        if not hit: return None
        mods.append(hit[0]); res.append(hit[1])
    from sympy.ntheory.modular import crt
    M = prod(mods); B = int(crt(mods, res)[0]) if mods else 0
    return M, B, sp.expand(P.as_expr().subs(w, M * w + B))

if __name__ == "__main__":
    p, q, r, h = [sp.Rational(x) for x in sys.argv[1:5]]
    e = sp.Rational(sys.argv[5]); c2, y = sp.Rational(sys.argv[6]), sp.Rational(sys.argv[7])
    u, v, z2, z3 = gamma_uv(p, q, r - e * h, c2, y)
    assert z2 == z3 == 0 and v > 0, (u, v)
    X = sp.Symbol('X'); f = X**4 + p * X**2 + q * X + r
    for a2, a1, a0 in xpolys(u, v):
        xw = a2 * w**2 + a1 * w + a0
        n = sp.expand((f.subs(X, xw) - e * h) / h)     # n' with shifts i = 0..4 <-> f - (e+i) h ... reindex below
        if e == 4: n = sp.expand(f.subs(X, xw) / h)       # n = f/h, shifts 0..4, shift 4 composed
        z = integralize(n)
        if not z: print((a2, a1, a0), "no integral model"); continue
        M, B, n0 = z
        degs = [[sp.degree(g, w) for g, _ in sp.factor_list(n0 - i)[1]] for i in range(5)]
        print("x(w) =", (a2, a1, a0), "w ->", M, "w +", B, "shift piece degrees", degs, flush=True)
        if any(dg != [4, 4] for dg in degs): continue
        res = search(n0, k=4)
        if not res or not res[0]: print("   refine: no option"); continue
        (combo, aug), st = res
        print("   refine: augment", aug, "e-vectors", [ev for ev, _ in combo], flush=True)
