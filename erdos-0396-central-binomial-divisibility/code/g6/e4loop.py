# Loop: E_3 quartic families x curve points -> composed degree-8 n'(w) with all 5 shifts = quartic x quartic.
import sys, itertools, sympy as sp
from quartic import family
from e4curve import points, gamma_uv
from e4fam2 import build
from check import w
S, B = int(sys.argv[1]), int(sys.argv[2])
seen = set()
for s in itertools.permutations(range(1, S + 1), 4):
    if s[0] > s[3]: continue
    fam = family(s)
    if not fam or fam[1] == 0: continue
    p, q, r, h = fam[:4]
    from quartic import sqrt_fr
    if any(sqrt_fr(sv * sv - 4 * tv) is not None or sqrt_fr(sv * sv - 4 * uv) is not None for sv, tv, uv in fam[4]): continue
    lam = next(l for l in range(1, 10**6) if all((c * l**e).denominator == 1 for c, e in ((p, 2), (q, 3), (r, 4), (h, 4))))
    P, Q, R, H = int(p * lam**2), int(q * lam**3), int(r * lam**4), int(h * lam**4)
    for e in (-1, 4):
        if (P, Q, R, H, e) in seen: continue
        seen.add((P, Q, R, H, e))
        for c2, y in points(P, Q, R - e * H, B):
            if y == 0: continue
            for yy in (y, -y):
                u, v, _, _ = gamma_uv(sp.Rational(P), sp.Rational(Q), sp.Rational(R - e * H), sp.Rational(c2), sp.Rational(yy))
                if v <= 0: continue
                bl = build(P, Q, R, H, e, c2, yy, nZ=1)
                if not bl: continue
                Z0, xw, n = bl[0]
                degs = [[sp.degree(g, w) for g, _ in sp.factor_list(n - i)[1]] for i in range(5)]
                tag = "ALL44" if all(dg == [4, 4] for dg in degs) else ""
                print(s, (P, Q, R, H), "e", e, "pt", c2, yy, degs, tag, flush=True)
