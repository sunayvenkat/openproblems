# Fix failing equal-degree pieces by content augmentation: w -> p*w + r with r a root of the piece mod p
# multiplies that piece's R by p^2 (j by p).  Greedy DFS; then full analysis incl. local primes.
import sys, itertools, sympy as sp
from math import lcm
from sympy import primerange
import check
from check import w, shifts, carry_levels, analyze, crt_class
from quartic import family
from qint import integer_models

def failing(n, k=3):
    bad, D = [], sp.Poly(n, w).degree()
    for i, (j, ps) in enumerate(shifts(n, k)):
        for f, e in ps:
            C = sp.div(sp.Poly(n - i, w), f)[0]
            L, cnt = carry_levels(f, C)
            if 2 * f.degree() > D or max(cnt) < e: bad.append((i, f))
    return bad

def fix(n, depth, primes=tuple(primerange(2, 60)), path=()):
    bad = failing(n)
    if not bad: return n, path
    if depth == 0: return None
    i, f = bad[0]
    for p in primes:
        for r in range(p):
            if f.eval(r) % p: continue
            m = sp.expand(n.subs(w, p * w + r))
            nb = failing(m)
            if len(nb) < len(bad):
                res = fix(m, depth - 1, primes, path + ((p, r),))
                if res: return res
    return None

if __name__ == "__main__":
    S, depth = int(sys.argv[1]), int(sys.argv[2])
    for s in itertools.permutations(range(1, S + 1), 4):
        if s[0] > s[3]: continue
        fam = family(s)
        if not fam or fam[1] == 0: continue
        for sub, n in integer_models(*fam[:4], maxopts=2):
            nb = len(failing(n))
            if nb > depth: continue
            res = fix(n, depth)
            if not res: continue
            m, path = res
            a = analyze(m, 3, verbose=False)
            print(s, sub, "fails", nb, "aug", path, "->", "GOOD " + str(crt_class(*a[1:])) if a else "local fail " + str(check.LAST), flush=True)
            if a: print("   n(w) =", m)
