"""k=0 witnesses n = x^m + 1 in E_0 for GOOD m (165, 195): F+ with k=0, j'=1.  python k0good.py m XMAX"""
import sys
from search import check, pieces_of
from famplus import phi_poly, predicted_levels, actual_levels
from verify396 import is_prime
from lemC import divisors
m, X = map(int, sys.argv[1:3])
for x in range(2, X + 1):
    n = x ** m + 1
    r = check(n, 0, [pieces_of(1, x, m)])
    if r == "IN" or r == "UNDECIDED":
        info = []
        for d in divisors(m):
            q = phi_poly(2 * d, x)
            if is_prime(q): info.append(f"d={d}: prime, pred {sorted(predicted_levels(m, d))} actual {sorted(actual_levels(n, q))}")
        print(f"x={x}: {r}; prime pieces: {info}", flush=True)
