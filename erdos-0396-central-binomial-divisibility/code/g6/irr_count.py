# Count E_3 quartic families (s_i <= S) whose 8 X-pieces are irreducible; test m(c) square for small c (shift -1 and 4).
import sys, itertools
from quartic import family, sqrt_fr
from e4curve import points
S, B = int(sys.argv[1]), int(sys.argv[2])
tot = irr = withpt = 0
for s in itertools.permutations(range(1, S + 1), 4):
    if s[0] > s[3]: continue
    fam = family(s)
    if not fam or fam[1] == 0: continue
    tot += 1
    if any(sqrt_fr(a*a - 4*b) is not None or sqrt_fr(a*a - 4*c) is not None for a, b, c in fam[4]): continue
    irr += 1
    p, q, r, h = fam[:4]
    lam = next(l for l in range(1, 10**6) if all((c * l**e).denominator == 1 for c, e in ((p, 2), (q, 3), (r, 4), (h, 4))))
    P, Q, R, H = int(p*lam**2), int(q*lam**3), int(r*lam**4), int(h*lam**4)
    for e in (-1, 4):
        pts = [pt for pt in points(P, Q, R - e*H, B) if pt[1] != 0]
        if pts: withpt += 1; print(s, e, (P, Q, R, H), [(str(a), str(b)) for a, b in pts[:3]], flush=True)
print("families", tot, "all-irreducible", irr, "with curve point", withpt)
