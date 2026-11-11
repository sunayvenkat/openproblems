# E_2: n = lam0 (a1 x+b1)(a2 x+b2); require n-1, n-2 to split into linear forms over Z. Rank by sum f_j.
from math import gcd, isqrt
from fractions import Fraction
from itertools import product
from search2 import frac_fail
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
res = []
for lam0 in (1, 3, 5, 7, 9, 11, 13, 15, 21):
  for a1 in range(1, 41):
    for a2 in range(a1, 41):
      A = lam0*a1*a2
      for b1 in range(-60, 61):
        for b2 in range(-60, 61):
          if gcd(a1, b1) != 1 or gcd(a2, b2) != 1: continue
          B = lam0*(a1*b2 + a2*b1); C = lam0*b1*b2
          if C % 2 == 0: continue  # n odd
          s1 = split(A, B, C-1); 
          if not s1: continue
          s2 = split(A, B, C-2)
          if not s2: continue
          mem = [(lam0, (a1,b1), (a2,b2)), s1, s2]
          # leading coefficient divisibility 2 for n-1: lam1 even
          fs = []
          for lam, f, g in mem:
              if f[0]*g[0] == 0: fs = None; break
              x1 = frac_fail(f[0], f[1], g[0], g[1], lam); x2 = frac_fail(g[0], g[1], f[0], f[1], lam)
              if x1 is None or x2 is None: fs = None; break
              fs += [x1, x2]
          if fs is None: continue
          res.append((round(sum(fs),3), fs, mem))
res.sort(key=lambda t: t[0])
print(len(res))
seen=set()
for r in res:
    key = tuple(sorted((m[0], m[1], m[2]) for m in r[2]))
    if key in seen: continue
    seen.add(key)
    print(r)
    if len(seen) > 40: break
