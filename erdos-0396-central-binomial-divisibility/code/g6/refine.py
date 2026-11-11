# Fast search over class refinements w -> M w + r of an integer quartic model n0(w) with quad x quad shifts.
# For piece f in shift i (partner g): R_f = j lc(g)/lc(f).  Refinement multiplies R_f by c_f^2 (c_f = new content
# of f), so status(f) = rule(frac(R_f * c_f^2), sigma_f), sigma_f = sign of lc(j g - R_f f) (refinement-invariant).
# Small primes p <= 13: options r mod p^a with all nu_p(piece(r)) < a, local carries of n(r) mod p^a >= need.
# Larger primes ("augmentation"): one piece with a root mod p gets c_f = p, costing one carry at p.
import sys, itertools, sympy as sp
from fractions import Fraction as Fr
from math import gcd, prod
from sympy import primerange
from check import w, shifts, low_carries

def ev(c, x): return sum(a * x ** e for e, a in enumerate(c))      # c lowest-first
def nu(x, p):
    if x == 0: return 99
    v = 0
    while x % p == 0: x //= p; v += 1
    return v

def rule(R, sig):
    t = R % 1
    return t > Fr(1, 2) or (t == Fr(1, 2) and sig >= 0) or (t == 0 and sig < 0)

def setup(n0, k=3):
    sh = shifts(n0, k)
    d = sp.Poly(n0, w).degree() // 2
    if any([f.degree() for f, _ in ps] != [d, d] or any(e != 1 for _, e in ps) for _, ps in sh): return None
    pcs, Rb, sig, js = [], [], [], []
    for i, (j, ps) in enumerate(sh):
        js.append(j)
        f, g = [[int(c) for c in reversed(q.all_coeffs())] for q, _ in ps]
        for a, b in ((f, g), (g, f)):
            R = Fr(j * b[d], a[d])
            rem = [j * y - R * x for x, y in zip(a, b)]
            s = next((1 if c > 0 else -1 for c in reversed(rem[:d]) if c != 0), 0)
            pcs.append((i, a)); Rb.append(R); sig.append(s)
    return sh, pcs, Rb, sig, js

def local_options(n0c, pcs, js, p, a):
    """dict e-vector -> list of r mod p^a"""
    opts = {}
    for r in range(p ** a):
        e = tuple(nu(ev(f, r), p) for _, f in pcs)
        if max(e) >= a: continue
        need = sum(nu(j, p) for j in js) + sum(e)
        if need and low_carries(ev(n0c, r) % p ** a, p, a) < need: continue
        if not need and p > 7: continue          # nothing to gain from such a prime here (handled by admissibility)
        opts.setdefault(e, []).append(r)
    return opts

def search(n0, k=3, A=None):
    st = setup(n0, k)
    if not st: return None
    sh, pcs, Rb, sig, js = st
    n0c = [int(c) for c in reversed(sp.Poly(n0, w).all_coeffs())]
    A = A or {2: 6, 3: 4, 5: 3, 7: 2, 11: 2, 13: 2}
    per, NP = {}, len(pcs)
    for p, a in A.items():
        o = local_options(n0c, pcs, js, p, a)
        if p <= 2 * k and not o: return None
        if p > 2 * k: o.setdefault((0,) * NP, [None])       # None = no refinement needed at p
        per[p] = o
    best = None
    for combo in itertools.product(*[list(per[p].items()) for p in A]):
        mult = [prod(p ** (2 * e[k]) for p, (e, _) in zip(A, combo)) for k in range(NP)]
        bad = [k for k in range(NP) if not rule(Rb[k] * mult[k], sig[k])]
        # augmentation: each bad piece needs a split prime q > 13 with rule(R q^2) true
        aug = []
        for k in bad:
            R = Rb[k] * mult[k]
            if R.denominator == 1: aug = None; break
            f = pcs[k][1]
            used = {qq for _, qq in aug}
            q = next((q for q in primerange(17, 400) if q not in used and rule(R * q * q, sig[k]) and
                      any(ev(f, r) % q == 0 for r in range(q))), None)
            if q is None: aug = None; break
            aug.append((k, q))
        if aug is None: continue
        if best is None or len(aug) < len(best[1]): best = (combo, aug)
        if not aug: break
    return best, st
