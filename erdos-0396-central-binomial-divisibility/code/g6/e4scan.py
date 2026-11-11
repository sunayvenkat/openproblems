# Scan E_3 quartic families for rational points on the shift-4 curve y^2 = c^4 + q c + r'  (after integral scaling).
import sys, itertools
from fractions import Fraction as Fr
from quartic import family
from e4curve import points
S, B = int(sys.argv[1]), int(sys.argv[2])
seen = set()
for s in itertools.permutations(range(1, S + 1), 4):
    if s[0] > s[3]: continue
    fam = family(s)
    if not fam or fam[1] == 0: continue
    p, q, r, h = fam[:4]
    for rp, tag in ((r - 4 * h, "+4"), (r + h, "-1")):          # extend AP on either end
        lam = next(l for l in range(1, 10**6) if all((c * l**e).denominator == 1 for c, e in ((p, 2), (q, 3), (rp, 4))))
        P, Q, RP = int(p * lam**2), int(q * lam**3), int(rp * lam**4)
        if (P, Q, RP) in seen: continue
        seen.add((P, Q, RP))
        pts = points(P, Q, RP, B)
        if pts: print(s, tag, "p,q,r,h =", [str(x) for x in fam[:4]], "lam", lam, "points", [(str(a), str(b)) for a, b in pts[:4]], flush=True)
print("curves tested", len(seen))
