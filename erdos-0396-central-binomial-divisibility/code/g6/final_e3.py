# E_3 family, presented in Y-language: n = g(Y)/H, n - i = F_i(Y) G_i(Y)/H with monic integer quadratics.
# For Y = M t + Y0 every piece is c * (prime candidate) with fixed content c; carry at a piece P = F/c iff
# frac(c^2/H) rule (lc ratio of cofactor to P), boundary cases by sign of the X-coefficient.
import sys, random, sympy as sp
from math import gcd, prod
from sympy import isprime, factorint
from sympy.ntheory.modular import crt
from check import w, analyze, crt_class, legendre
from refine import nu, low_carries

FAMS = {
  'A': (sp.Poly([1, 0, 1201, 630, 388600], w), 16800,
        [(7, 580, 670), (5, 550, 676), (3, 500, 710), (2, 445, 760)],
        (840 * 3460101837192000, 840 * 397799998725376 + 25)),       # class found by scan.py/build.py
  'B': (sp.Poly([1, 0, 1694, 50688, 22186017], w), 10483200,
        [(88, 4431, 5007), (72, 3087, 3791), (32, 567, 2151), (8, -2289, 4047)],
        (21840 * 649296648000, 21840 * 273012432261 + 21171)),
}

def contents_of_class(fam):
    g, H, sts, (M0, Y00) = fam
    cont = {}
    for k, F in enumerate(pieces(fam)):
        c = gcd(*[int(x) for x in sp.Poly(F.as_expr().subs(w, M0 * w + Y00), w).all_coeffs()])
        for p, e in factorint(c).items(): cont.setdefault(p, [0] * 8)[k] = e
    for p in sp.primerange(2, 17): cont.setdefault(p, [0] * 8)
    for p in factorint(H): cont.setdefault(p, [0] * 8)
    return cont

def pieces(fam):
    sts = fam[2]
    out = []
    for s, t, u in sts:
        out += [sp.Poly([1, s, t], w), sp.Poly([1, -s, u], w)]
    return out

def identities(fam):
    g, H = fam[0], fam[1]
    P = pieces(fam)
    return all((g - i * H - P[2 * i] * P[2 * i + 1]).is_zero for i in range(4))

def minimal_class(fam, cont):
    """cont: prime -> 8 exponents.  Returns (M, Y0) minimal per prime."""
    g, H = fam[0], fam[1]
    P = pieces(fam)
    mods, res = [], []
    for p, e in cont.items():
        vH = nu(H, p)
        need = sum(e) - 4 * vH                                 # nu_p of prod(n-i)
        for b in (b for b in range(1, 20) if p ** b <= 2 * 10 ** 6):
            hit = None
            for Y0 in range(p ** b):
                if any(nu(int(F.eval(Y0)), p) != e[k] or e[k] >= b for k, F in enumerate(P)): continue
                c = b - vH
                if need and c < need: continue
                if need:
                    q = p ** c; nm = (int(g.eval(Y0)) // p ** vH) * pow(H // p ** vH, -1, q) % q   # n mod p^c
                    if low_carries(nm, p, c) < need: continue
                hit = Y0; break
            if hit is not None: break
        mods.append(p ** b); res.append(hit)
    M = prod(mods)
    return M, int(crt(mods, res)[0])

def pointwise(fam, cont, M, Y0, trials=300, seed=1):
    """for random large t: identity, small-prime Legendre counts, and base-P carries for every piece value P."""
    g, H = fam[0], fam[1]
    P = pieces(fam)
    small = sorted(cont)
    rnd = random.Random(seed)
    for _ in range(trials):
        t = rnd.randrange(10 ** 6, 10 ** 30)
        Y = M * t + Y0
        G = int(g.eval(Y)); assert G % H == 0; n = G // H
        vals = [int(F.eval(Y)) for F in P]
        cs = [prod(p ** cont[p][k] for p in small) for k in range(8)]
        assert all(v % c == 0 for v, c in zip(vals, cs))
        prs = [v // c for v, c in zip(vals, cs)]
        assert all(pr % p for pr in prs for p in small)       # pieces coprime to the small primes
        for i in range(4):
            assert (n - i) * H == vals[2 * i] * vals[2 * i + 1]
        for p in small:
            assert legendre(n, p) >= sum(nu(n - i, p) for i in range(4)), (p, t)
        for Pv in prs:                                          # Kummer digit count in base Pv
            c = k = 0; m = n
            while m:
                c = 1 if 2 * (m % Pv) + c >= Pv else 0; k += c; m //= Pv
            assert k >= 1, (Pv, t)
    return True

if __name__ == "__main__":
    fam = FAMS[sys.argv[1]]
    g, H = fam[0], fam[1]
    cont = contents_of_class(fam)
    print("identities:", identities(fam))
    print("contents per prime:", cont)
    M, Y0 = minimal_class(fam, cont)
    print("class: Y = %d t + %d   (M = %s)" % (M, Y0, factorint(M)))
    cs = [prod(p ** cont[p][k] for p in cont) for k in range(8)]
    print("contents c:", cs, " j_i:", [sp.Rational(cs[2*i] * cs[2*i+1], H) for i in range(4)],
          " R = c^2/H:", [str(sp.Rational(c * c, H)) for c in cs])
    n = sp.expand(sp.Poly(g.as_expr().subs(w, M * w + Y0), w).as_expr() / H)
    a = analyze(n, 3)
    print("analyzer on n(t):", crt_class(*a[1:]) if a else "FAIL")
    print("pointwise checks:", pointwise(fam, cont, M, Y0))
