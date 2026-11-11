# Build the explicit refined family for one (s, model) found by scan.py and verify with the sympy analyzer.
import sys, sympy as sp
from math import prod
from sympy.ntheory.modular import crt
from quartic import family
from qint import integer_models
from refine import search, ev, nu
from check import w, analyze, crt_class
import check

def build(s, sub):
    fam = family(s)
    n0 = next(n for sb, n in integer_models(*fam[:4], maxopts=3) if sb == sub)
    (combo, aug), (sh, pcs, Rb, sig, js) = search(n0)
    A = {2: 6, 3: 4, 5: 3, 7: 2, 11: 2, 13: 2}
    mods, res = [], []
    for p, (e, rs) in zip(A, combo):
        if rs[0] is not None: mods.append(p ** A[p]); res.append(rs[0])
    for k, q in aug:
        f = pcs[k][1]
        r = next(r for r in range(q * q) if ev(f, r) % q == 0 and ev(f, r) % (q * q))
        mods.append(q * q); res.append(r)
    M = prod(mods); r = int(crt(mods, res)[0])
    return n0, M, r, sp.expand(n0.subs(w, M * w + r))

if __name__ == "__main__":
    s = tuple(int(t) for t in sys.argv[1].split(',')); sub = tuple(int(t) for t in sys.argv[2].split(','))
    n0, M, r, n1 = build(s, sub)
    print("n0(w) =", n0); print("w ->", M, "* w +", r)
    a = analyze(n1, 3)
    print("RESULT:", crt_class(*a[1:]) if a else ("fail", check.LAST))
