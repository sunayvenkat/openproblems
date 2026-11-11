# Hunt: irreducible E_3 families x curve points (both e = -1, 4) -> locally solvable integral x(w) with all-[4,4] shifts.
import sys, itertools, io, contextlib, sympy as sp
from quartic import family, sqrt_fr
from e4curve import points
from e4fam2 import build
from check import w
S, B = int(sys.argv[1]), int(sys.argv[2])
for s in itertools.permutations(range(1, S + 1), 4):
    if s[0] > s[3]: continue
    fam = family(s)
    if not fam or fam[1] == 0: continue
    if any(sqrt_fr(a*a - 4*b) is not None or sqrt_fr(a*a - 4*c) is not None for a, b, c in fam[4]): continue
    p, q, r, h = fam[:4]
    lam = next(l for l in range(1, 10**6) if all((c * l**e).denominator == 1 for c, e in ((p, 2), (q, 3), (r, 4), (h, 4))))
    P, Q, R, H = int(p*lam**2), int(q*lam**3), int(r*lam**4), int(h*lam**4)
    for e in (-1, 4):
        for c2, y in points(P, Q, R - e*H, B):
            if y == 0: continue
            for yy in (y, -y):
                with contextlib.redirect_stdout(io.StringIO()):
                    bl = build(P, Q, R, H, e, c2, yy)
                if not bl: continue
                Z0, xw, n = bl[0]
                degs = [[sp.degree(g, w) for g, _ in sp.factor_list(n - i)[1]] for i in range(5)]
                print(s, (P, Q, R, H), "e", e, "pt", c2, yy, degs, flush=True)
