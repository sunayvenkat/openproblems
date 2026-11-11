# E_4: composed family -> k=4 refinement search -> explicit class -> independent analyzer (k=4).
import sys, sympy as sp
from math import prod
from sympy.ntheory.modular import crt
from e4fam2 import build
from refine import search, ev
from check import w, analyze, crt_class
import check
P, Q, R, H, e = [int(t) for t in sys.argv[1:6]]
c2, y = sp.Rational(sys.argv[6]), sp.Rational(sys.argv[7])
Z0, xw, n0 = build(P, Q, R, H, e, c2, y)[0]
print("x(w) =", xw)
res = search(n0, k=4)
if not res or not res[0]: print("refine: no option"); sys.exit()
(combo, aug), (sh, pcs, Rb, sig, js) = res
print("refine ok; augmentation primes:", aug, " base R:", [str(r) for r in Rb])
A = {2: 6, 3: 4, 5: 3, 7: 2, 11: 2, 13: 2}
mods, rs = [], []
for p, (evec, lst) in zip(A, combo):
    if lst[0] is not None: mods.append(p ** A[p]); rs.append(lst[0])
for k, q in aug:
    f = pcs[k][1]
    rr = next(r for r in range(q * q) if ev(f, r) % q == 0 and ev(f, r) % (q * q))
    mods.append(q * q); rs.append(rr)
M = prod(mods); r0 = int(crt(mods, rs)[0])
n1 = sp.expand(n0.subs(w, M * w + r0))
a = analyze(n1, 4)
print("ANALYZER k=4:", crt_class(*a[1:]) if a else ("FAIL", check.LAST))
