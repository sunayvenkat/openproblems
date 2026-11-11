"""Per-level last mismatch x for one piece: python level_detail.py m d j X"""
import sys
from famplus import phi_poly, predicted_levels
m, d, j, X = map(int, sys.argv[1:])
pr = predicted_levels(m, d)
last = {}; binlast = None
for x in range(2, X + 1):
    N = j * (x ** m + 1); q = phi_poly(2 * d, x); t, pt = 1, q; any_c = False
    while pt <= 2 * N:
        c = 2 * (N % pt) >= pt; any_c |= c
        if c != (t in pr): last[t] = x
        t += 1; pt *= q
    for tt in pr:
        if q ** tt > 2 * N: last[tt] = x   # predicted level not even reached
    if any_c != bool(pr): binlast = x
print(f"m={m} d={d} j'={j} pred={sorted(pr)} last-mismatch per level: {dict(sorted(last.items()))} binary last={binlast}")
