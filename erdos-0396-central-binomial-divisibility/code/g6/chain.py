# Quartic route for general k.  f(X) = X^4 + pX^2 + qX + r, n = f/h.  Shift i factors as quad x quad
# (X^2 + sX + t)(X^2 - sX + u)  <=>  iota(s^2) = i  where  iota(z) = a z^2 + b z + c + d/z with
# a = -1/(4h), b = -p/(2h), c = (4r - p^2)/(4h), d = q^2/(4h).   So: find (a,b,c,d) with -d/a a rational square
# such that iota takes the values 0..k at rational squares.  Given 4 squares at 4 positions, (a,b,c,d) is
# determined (linear system); test the remaining positions: a z^3 + b z^2 + (c-m) z + d needs a square root z.
import sys, itertools, sympy as sp
from fractions import Fraction as Fr
from quartic import sqrt_fr

def solve4(zs, iv):
    """cubic P = a z^3+b z^2+c z+d through (z_j, i_j z_j) by Lagrange; returns (a,b,c,d) or None if -d/a not square."""
    ys = [i * z for i, z in zip(iv, zs)]
    co = [Fr(0)] * 4                              # highest first
    for j, (zj, yj) in enumerate(zip(zs, ys)):
        others = [zl for l, zl in enumerate(zs) if l != j]
        den = 1
        for zl in others: den *= zj - zl
        e1 = sum(others); e2 = others[0]*others[1] + others[0]*others[2] + others[1]*others[2]; e3 = others[0]*others[1]*others[2]
        wgt = Fr(yj, den)
        co[0] += wgt; co[1] -= wgt * e1; co[2] += wgt * e2; co[3] -= wgt * e3
    if co[0] == 0 or sqrt_fr(-co[3] / co[0]) is None: return None
    return co

def square_roots(a, b, c, d, m):
    z = sp.Symbol('z')
    P = sp.Poly([sp.Rational(x.numerator, x.denominator) for x in (a, b, c - m, d)], z)
    out = []
    for rt in P.ground_roots():
        rt = Fr(int(rt.p), int(rt.q))
        if rt > 0 and sqrt_fr(rt) is not None: out.append(sqrt_fr(rt))
    return out

def to_quartic(a, b, c, d):
    h = -1 / (4 * a); p = b / (2 * a); r = (p * p - c / a) / 4; q = sqrt_fr(-d / a)
    return p, q, r, h

if __name__ == "__main__":
    S, k = int(sys.argv[1]), int(sys.argv[2])
    pos_sets = [P for P in itertools.combinations(range(k + 1), 4) if P[0] == 0 and P[-1] >= 3]
    seen = set()
    for s in itertools.permutations(range(1, S + 1), 4):
        if s[0] > s[1] and False: continue
        zs = [x * x for x in s]
        for P in pos_sets:
            # fast exact float prefilter on -d/a > 0 is skipped; do exact solve
            sol = solve4(zs, list(P))
            if not sol: continue
            a, b, c, d = sol
            if a == 0 or sqrt_fr(-d / a) is None: continue
            got = {i: Fr(x) for i, x in zip(P, s)}
            for m in range(-2, k + 3):
                if m in got: continue
                r = square_roots(a, b, c, d, m)
                if r: got[m] = r[0]
            run, best = 0, (0, 0)
            for m in range(-2, k + 3):
                run = run + 1 if m in got else 0
                best = max(best, (run, m))
            if best[0] >= 5:
                key = (a, b, c, d)
                if key in seen: continue
                seen.add(key)
                print("RUN", best, {m: str(v) for m, v in sorted(got.items())}, "quartic p,q,r,h =", [str(x) for x in to_quartic(a, b, c, d)], flush=True)
