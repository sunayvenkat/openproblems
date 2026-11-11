# Pointwise test at the smallest t (t = 0..T): carries in base every piece value and small-prime Legendre counts.
import sys, sympy as sp
from math import prod
from final_e3 import FAMS, pieces, contents_of_class, minimal_class
from check import legendre
from refine import nu
fam = FAMS[sys.argv[1]]; T = int(sys.argv[2])
g, H = fam[0], fam[1]; cont = contents_of_class(fam); M, Y0 = minimal_class(fam, cont)
P = pieces(fam); cs = [prod(p ** cont[p][k] for p in cont) for k in range(8)]
bad = []
for t in range(T):
    Y = M * t + Y0; n = int(g.eval(Y)) // H
    for k, F in enumerate(P):
        Pv = int(F.eval(Y)) // cs[k]
        c = cnt = 0; m = n
        while m: c = 1 if 2 * (m % Pv) + c >= Pv else 0; cnt += c; m //= Pv
        if cnt < 1: bad.append((t, k))
    for p in cont:
        if legendre(n, p) < sum(nu(n - i, p) for i in range(4)): bad.append((t, 'p%d' % p))
print(sys.argv[1], "t in [0,%d): failures" % T, bad[:10], len(bad))
