# E_4 composition for one E_3 family: try curve points, report piece degrees and the k=4 refinement search.
import sys, sympy as sp
from e4curve import points, gamma_uv
from e4fam2 import build
from check import w
from refine import search
P, Q, R, H, e, B = [int(t) for t in sys.argv[1:7]]
for c2, y in points(P, Q, R - e * H, B):
    if y == 0: continue
    for yy in (y, -y):
        u, v, _, _ = gamma_uv(sp.Rational(P), sp.Rational(Q), sp.Rational(R - e * H), sp.Rational(c2), sp.Rational(yy))
        bl = build(P, Q, R, H, e, c2, yy, nZ=2)
        print("point", c2, yy, "integral x(w) options:", len(bl), flush=True)
        for Z0, xw, n in bl:
            degs = [[sp.degree(g, w) for g, _ in sp.factor_list(n - i)[1]] for i in range(5)]
            print("   x(w) =", xw, degs, flush=True)
            if all(dg == [4, 4] for dg in degs):
                res = search(n, k=4)
                print("   refine:", "no option" if not res or not res[0] else ("augment %s" % (res[0][1],)), flush=True)
