# Quadruples n=(a1x+b1)(a2x+b2), n-1=2(a3x+b3)(a4x+b4) with frac_fail=0 on all four forms. Wider a.
import sys
from math import gcd, isqrt
from search2 import frac_fail, admissible
def good_a(A):
    out = []
    for a in range(1, A+1):
        us = sorted({u*u % a for u in range(1, a+1) if gcd(u, a) == 1}) if a > 1 else [0]
        # exists coset g*H inside (a/2, a)?  (rough filter; frac_fail does the exact test)
        if a <= 2 or any(all(2*((g*u) % a) > a for u in us) for g in range(0, a)): out.append(a)
    return out
def split2(A, B, C):  # A x^2 + B x + C = 2 (a3 x+b3)(a4 x+b4) over Z?
    if A % 2 or B % 2 or C % 2: return None
    A, B, C = A//2, B//2, C//2
    D = B*B - 4*A*C
    if D < 0: return None
    s = isqrt(D)
    if s*s != D: return None
    # roots (-B±s)/(2A); linear factors (2A x + B - s)/g etc. Use content.
    r1n, r2n, den = -B+s, -B-s, 2*A
    g1 = gcd(den, r1n); a3, b3 = den//g1, -r1n//g1
    g2 = gcd(den, r2n); a4, b4 = den//g2, -r2n//g2
    k = A*2*2 // (a3*a4) if (a3*a4) and (4*A) % (a3*a4) == 0 else None
    # verify: 2(a3x+b3)(a4x+b4)*? == original
    if a3*a4 != A: return None  # need exactly 2*(..)(..) with no extra constant
    if a3*b4 + a4*b3 != B or b3*b4 != C: return None
    return (a3, b3), (a4, b4)
A = int(sys.argv[1]); Bm = int(sys.argv[2]); G = good_a(A); print('good a:', G)
found = []
for a1 in G:
    for a2 in G:
        if a2 < a1: continue
        for b1 in range(-Bm, Bm+1):
            if gcd(a1, b1) != 1: continue
            for b2 in range(-Bm, Bm+1):
                if gcd(a2, b2) != 1: continue
                sp = split2(a1*a2, a1*b2+a2*b1, b1*b2-1)
                if not sp: continue
                (a3, b3), (a4, b4) = sp
                if a3 <= 0 or a4 <= 0: continue
                forms = [(a1, b1), (a2, b2), (a3, b3), (a4, b4)]
                fs = [frac_fail(a1, b1, a2, b2, 1), frac_fail(a2, b2, a1, b1, 1), frac_fail(a3, b3, a4, b4, 2), frac_fail(a4, b4, a3, b3, 2)]
                if None in fs: continue
                if sum(fs) < 0.4 - 1e-9 and admissible(forms): found.append((sum(fs), fs, forms))
found.sort()
print(len(found))
for f in found[:40]: print(f)
