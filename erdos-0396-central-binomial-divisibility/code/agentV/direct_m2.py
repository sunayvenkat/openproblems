"""Direct integer carry test for pieces q = Phi_{2d}(x) of N = j(x^m+1), m = 59814755, via modular exponentiation:
N mod q^t = j*(pow(x, m, q^t) + 1) mod q^t.  python direct_m2.py x j tmax d [d ...]"""
import sys
from famplus import phi_poly
m = 59814755
x, j, tmax = map(int, sys.argv[1:4])
for d in map(int, sys.argv[4:]):
    q = phi_poly(2 * d, x); lv = []
    for t in range(2, tmax + 1):
        Q = q ** t
        r = j * (pow(x, m, Q) + 1) % Q
        if 2 * r >= Q: lv.append(t)
    print(f"x={x} j'={j} d={d}: carry levels among 2..{tmax}: {lv}", flush=True)
