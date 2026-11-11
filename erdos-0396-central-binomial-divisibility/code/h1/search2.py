# General search: n = P1 P2, n-1 = 2 P3 P4, forms a x + b (a>=1), rank by bad mass
# f_j = fraction of square classes u of (Z/a)^x where position-2 carry fails.
from math import gcd, log
from itertools import product
def squares_units(a):
    return sorted({(u*u) % a for u in range(1, a+1) if gcd(u, a) == 1}) if a > 1 else [0]
def frac_fail(a, b, ap, bp, lam):
    kappa = a*bp - ap*b
    if kappa == 0: return None
    lk = lam*kappa
    us = squares_units(a); bad = 0
    for u in us:
        r = (-lk*b*u) % a
        if 2*r > a: continue
        if 2*r == a and lk > 0: continue
        if r == 0 and lk < 0: continue
        bad += 1
    return bad/len(us)
def admissible(forms):
    for p in (2,3,5,7,11,13,17,19,23):
        if not any(all((a*x+b) % p for a,b in forms) for x in range(p)): return False
    return True
AMAX, BMAX = 30, 40
if __name__ == '__main__':
    res = []
    for a1 in range(1, AMAX+1):
      for a2 in range(a1, AMAX+1):
        if (a1*a2) % 2: continue
        half = a1*a2//2
        for a3 in range(1, AMAX+1):
            if half % a3: continue
            a4 = half//a3
            if a4 < a3 or a4 > AMAX: continue
            for b1 in range(-BMAX, BMAX+1):
              if b1 % 2 == 0: continue
              for b2 in range(-BMAX, BMAX+1):
                if b2 % 2 == 0: continue
                s = a1*b2 + a2*b1
                if s % 2: continue
                s //= 2; p34 = (b1*b2-1)//2
                for b3 in range(-BMAX, BMAX+1):
                    if (s - a4*b3) % a3: continue
                    b4 = (s - a4*b3)//a3
                    if b3*b4 != p34: continue
                    if b3 % 2 == 0 or b4 % 2 == 0: continue
                    forms = [(a1,b1),(a2,b2),(a3,b3),(a4,b4)]
                    fs = [frac_fail(a1,b1,a2,b2,1), frac_fail(a2,b2,a1,b1,1), frac_fail(a3,b3,a4,b4,2), frac_fail(a4,b4,a3,b3,2)]
                    if None in fs: continue
                    cost = 0.549*sum(fs) + 0.19
                    if cost < 0.95 and admissible(forms):
                        res.append((round(cost,3), fs, forms))
    res.sort()
    print(len(res))
    seen = set()
    for r in res[:60]:
        print(r)
