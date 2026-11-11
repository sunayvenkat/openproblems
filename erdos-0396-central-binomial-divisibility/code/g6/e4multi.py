# Try many local choices of x(w) for E_4 candidates; report any that pass the k=4 refinement search.
import sys, random, itertools, sympy as sp
from e4fam2 import build
from refine import search
from check import w
cands = [(1694, 50688, 22186017, 10483200, 4, '183/2', '33267/4'), (11550, 2928640, 701582049, 318689280, 4, '-166', '4275'),
         (11550, 2928640, 701582049, 318689280, 4, '152', '-25935'), (-2842, 45760, 182105, 123648, -1, '38', '161'),
         (-2842, 45760, 182105, 123648, -1, '38', '-161'), (-2842, 45760, 182105, 123648, -1, '19/3', '6256/9'),
         (-2842, 45760, 182105, 123648, -1, '19/3', '-6256/9'), (1694, 50688, 22186017, 10483200, 4, '183/2', '-33267/4')]
for c in cands:
    P, Q, R, H, e = c[:5]
    opts = build(P, Q, R, H, e, sp.Rational(c[5]), sp.Rational(c[6]), nZ=40, per=6)
    ok = 0
    for Z0, xw, n in opts:
        if any([sp.degree(g, w) for g, _ in sp.factor_list(n - i)[1]] != [4, 4] for i in range(5)): continue
        res = search(n, k=4)
        if res and res[0]:
            ok += 1; print("PASS", c, "Z0", Z0, "aug", res[0][1], flush=True); break
    print("candidate", c, "options", len(opts), "pass", ok, flush=True)
