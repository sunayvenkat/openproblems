# Diagnose the k=4 refinement for a composed family: base R values, signs, per-prime local options.
import sys, sympy as sp
from e4fam2 import build
from refine import setup, local_options
from check import w
P, Q, R, H, e = [int(t) for t in sys.argv[1:6]]
c2, y = sp.Rational(sys.argv[6]), sp.Rational(sys.argv[7])
Z0, xw, n0 = build(P, Q, R, H, e, c2, y)[0]
sh, pcs, Rb, sig, js = setup(n0, 4)
print("j:", js); print("R:", [str(r) for r in Rb]); print("sig:", sig)
n0c = [int(c) for c in reversed(sp.Poly(n0, w).all_coeffs())]
for p, a in {2: 6, 3: 4, 5: 3, 7: 2}.items():
    o = local_options(n0c, pcs, js, p, a)
    print("p", p, "options:", {k: len(v) for k, v in list(o.items())[:6]}, "total e-vectors", len(o))
