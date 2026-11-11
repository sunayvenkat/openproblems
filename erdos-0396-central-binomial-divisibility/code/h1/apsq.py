# Complete enumeration of linear-form families via squares in AP.
# n = lam0 (a1 x+b1)(a2 x+b2), A = lam0 a1 a2, kappa = a1 b2 - a2 b1. disc(n - i) = (lam0 kappa)^2 + 4 A i.
# E1: (lam0 k)^2 + 4A = s^2.  E2: also + 8A = v^2  => (lam0 k)^2, s^2, v^2 in AP, diff 4A.
# E3 would need 4 squares in AP: impossible (Fermat). So quadratic families stop at E2.
import sys
from math import gcd, isqrt
from fractions import Fraction
def split(A, B, C):
    D = B*B - 4*A*C
    if D < 0: return None
    v = isqrt(D)
    if v*v != D: return None
    r1 = Fraction(-B + v, 2*A); r2 = Fraction(-B - v, 2*A)
    f1 = (r1.denominator, -r1.numerator); f2 = (r2.denominator, -r2.numerator)
    lam = Fraction(A, f1[0]*f2[0])
    if lam.denominator != 1: return None
    return int(lam), f1, f2
from search2 import frac_fail, admissible
def famfs(lam0, a1, b1, a2, b2, k):
    A = lam0*a1*a2; B = lam0*(a1*b2+a2*b1); C = lam0*b1*b2
    mem = [(lam0, (a1, b1), (a2, b2))]
    for i in range(1, k+1):
        s = split(A, B, C-i)
        if not s: return None
        mem.append(s)
    fs = []
    for lam, f, g in mem:
        x1 = frac_fail(f[0], f[1], g[0], g[1], lam); x2 = frac_fail(g[0], g[1], f[0], f[1], lam)
        if x1 is None or x2 is None: return None
        fs += [x1, x2]
    forms = [m[1] for m in mem] + [m[2] for m in mem]
    if any(a <= 0 for a, b in forms): return None
    return sum(fs), [round(f, 3) for f in fs], mem, admissible(forms)
def solve_b(a1, a2, kap):  # a1 b2 - a2 b1 = kap, gcd(a1,a2) | kap
    g = gcd(a1, a2)
    if kap % g: return None
    # extended gcd
    def eg(a, b):
        if b == 0: return (a, 1, 0)
        d, x, y = eg(b, a % b); return (d, y, x - (a//b)*y)
    d, u, v = eg(a1, a2)  # a1 u + a2 v = d
    t = kap//d; b2, b1 = u*t, -v*t
    # reduce shift: b1 -> b1 + a1 s, b2 -> b2 + a2 s
    s = -round(b1/a1); return b1 + a1*s, b2 + a2*s
def families(k, AMAX, LAMS):
    out = []; seen = set()
    for A in range(1, AMAX+1):
        # find w^2 = (lam0 kappa)^2 with w^2 + 4A i squares for i=1..k
        for w in range(0, 2*A+2):   # w^2 + 4A = s^2 => (s-w)(s+w) = 4A => w <= A-1 roughly
            ok = True
            for i in range(1, k+1):
                v = w*w + 4*A*i; r = isqrt(v)
                if r*r != v: ok = False; break
            if not ok: continue
            for lam0 in LAMS:
                if A % lam0 or w % lam0: continue
                kap = w//lam0; aa = A//lam0
                for a1 in range(1, isqrt(aa)+1):
                    if aa % a1: continue
                    a2 = aa//a1
                    for sg in (1, -1):
                        bb = solve_b(a1, a2, sg*kap)
                        if bb is None: continue
                        b1, b2 = bb
                        if gcd(a1, b1) != 1 or gcd(a2, b2) != 1: continue
                        r = famfs(lam0, a1, b1, a2, b2, k)
                        if r is None: continue
                        key = (lam0, a1, b1 % a1, a2, b2 % a2)
                        if key in seen: continue
                        seen.add(key); out.append(r)
    out.sort(key=lambda t: (not t[3], t[0]))
    return out
if __name__ == '__main__':
    k, AMAX = int(sys.argv[1]), int(sys.argv[2])
    LAMS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    fams = families(k, AMAX, LAMS)
    print('k', k, 'A<=', AMAX, 'families', len(fams), 'admissible', sum(f[3] for f in fams))
    for f in [f for f in fams if f[3]][:25]: print(f)
