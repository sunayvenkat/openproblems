"""Piece d of m = N*d (N = 3,5,7): which odd d give a BAD piece?  python lemmaA_N.py N DMAX"""
import sys
import fastgood as F
N, DM = map(int, sys.argv[1:3]); bad = []
for d in range(1, DM + 1, 2):
    if F.good(N * d, d) is None:
        bad.append(d); print(f"N={N} d={d} primes(d)={F.pf(d)} phi(d)/d={F.phi(d)/d:.3f}  m={N*d}: BAD", flush=True)
print("done N", N, "d<=", DM, "bad:", bad)
