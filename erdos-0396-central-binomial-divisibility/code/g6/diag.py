import sympy as sp
from check import w, shifts, low_carries
from quartic import family
from qint import integer_models
fam = family((2, 1, 5, 7))
for sub, n in integer_models(*fam[:4], maxopts=2):
    if sub[2] != 331: continue
    n = sp.expand(n.subs(w, 31*w + 7))
    sh = shifts(n, 3)
    for j, ps in sh: print(j, [f.as_expr() for f, _ in ps])
    nP = sp.Poly(n, w); pcs = [f for _, ps in sh for f, _ in ps]
    for r in range(16):
        odd = [int(f.eval(r)) % 2 for f in pcs]
        print(r, int(nP.eval(r)) % 64, odd, low_carries(int(nP.eval(r)), 2, 6))
