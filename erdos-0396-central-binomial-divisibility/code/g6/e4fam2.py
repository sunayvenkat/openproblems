# E_4 by composition, explicit: x(w) = ((Z0 + V h w)^2 - U)/V with V X0 + U = Z0^2, f(X0) = 0 mod h.
# Then disc(x(w) - theta) = (2 h d gamma)^2, so f(x(w)) - e h splits into two rational quartics.
import sys, sympy as sp
from sympy.ntheory.residue_ntheory import sqrt_mod
from e4curve import gamma_uv
from check import w
from refine import search, nu
from math import prod

def build(p, q, r, h, e, c2, y, nZ=5, per=1):
    u, v, z2, z3 = gamma_uv(sp.Rational(p), sp.Rational(q), sp.Rational(r - e * h), sp.Rational(c2), sp.Rational(y))
    assert z2 == z3 == 0 and v != 0
    d = sp.ilcm(sp.Rational(u).q, sp.Rational(v).q); U, V = int(u * d * d), int(v * d * d)
    g = 1
    for P_, ex in sp.factorint(sp.igcd(U, V)).items(): g *= P_ ** (ex // 2)
    U, V = U // (g * g), V // (g * g)
    X = sp.Symbol('X'); f = X**4 + p * X**2 + q * X + r
    fx = lambda x: x**4 + p * x**2 + q * x + r
    mods, res = [], []
    for P_, eV in sp.factorint(abs(V) * h).items():
        a, b = nu(V, P_), nu(h, P_)
        roots = sqrt_mod(U % P_**a, P_**a, all_roots=True) if a else [0]
        hits = []
        for Z1 in roots or []:
            for t in range(P_**b if a else P_**(b + 1)):
                Z = Z1 + P_**a * t if a else t
                Xm = ((Z * Z - U) // P_**a) * pow(V // P_**a, -1, P_**b) % P_**b if b else 0
                if b == 0 or fx(Xm) % P_**b == 0: hits.append(Z)
                if len(hits) >= per: break
            if len(hits) >= per: break
        if not hits: print('      local obstruction at', P_); return []
        mods.append(P_**(a + b) if a else P_**(b + 1)); res.append(hits)
    from sympy.ntheory.modular import crt
    import itertools
    MZ = prod(mods); out = []
    for choice in itertools.islice(itertools.product(*res), nZ):
        Z0 = int(crt(mods, list(choice))[0])
        assert (Z0 * Z0 - U) % V == 0 and fx((Z0 * Z0 - U) // V) % h == 0
        xw = sp.expand(((Z0 + MZ * w)**2 - U) / V)
        n = sp.expand((f.subs(X, xw) - e * h) / h) if e < 0 else sp.expand(f.subs(X, xw) / h)
        out.append((Z0, xw, n))
    return out

if __name__ == "__main__":
    p, q, r, h, e = [int(t) for t in sys.argv[1:6]]
    c2, y = sp.Rational(sys.argv[6]), sp.Rational(sys.argv[7])
    for Z0, xw, n in build(p, q, r, h, e, c2, y):
        assert all(c.is_integer for c in sp.Poly(n, w).all_coeffs())
        degs = [[sp.degree(g, w) for g, _ in sp.factor_list(n - i)[1]] for i in range(5)]
        print("x(w) =", xw, " degrees", degs, flush=True)
        if any(dg != [4, 4] for dg in degs): continue
        res = search(n, k=4)
        print("   refine:", "no option" if not res or not res[0] else ("augment %s e-vectors %s" % (res[0][1], [ev for ev, _ in res[0][0]])), flush=True)
