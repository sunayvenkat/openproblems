"""Check Laurent-sign level prediction at very large x: python bigx.py m X0 count  (all d | m, j' in 1..3)"""
import sys, random
from famplus import phi_poly, predicted_levels, actual_levels
from lemC import divisors
m, X0, cnt = map(int, sys.argv[1:]); random.seed(m)
for d in divisors(m):
    pr = predicted_levels(m, d); bad = []
    for _ in range(cnt):
        x = random.randrange(X0, 2 * X0); j = random.randrange(1, 4)
        ac = actual_levels(j * (x ** m + 1), phi_poly(2 * d, x))
        if ac != pr: bad.append((x, j, sorted(ac ^ pr)))
    print(f"m={m} d={d} pred={'GOOD' if pr else 'BAD'} #levels={len(pr)}  mismatches {len(bad)}/{cnt}", bad[:2])
