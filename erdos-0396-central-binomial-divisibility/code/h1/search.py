# Search quadruples P1P2 - 2 P3P4 = 1 of linear forms with "automatic carry" design.
# Form P=ax+b, partner P'=a'x+b', constant lam (n-i = lam*P*P'). kappa = a b' - a' b.
# For prime q | P(x), q large, c=P/q < q: W mod q = ((r q + lam*kappa*c)/a) mod q,
# r = (-lam*kappa*b*u) mod a with u = qbar^2 mod a (u ranges over squares of units mod a).
# Automatic carry for all such q iff for all u: r>a/2, or r==a/2 and lam*kappa>0, or r==0 and lam*kappa<0.
from math import gcd
from itertools import product

def squares_units(a):
    return sorted({(u*u) % a for u in range(1, a+1) if gcd(u, a) == 1}) if a > 1 else [0]

def auto_ok(a, b, ap, bp, lam):
    kappa = a*bp - ap*b
    if kappa == 0: return False
    lk = lam*kappa
    for u in squares_units(a):
        r = (-lk*b*u) % a
        if 2*r > a: continue
        if 2*r == a and lk > 0: continue
        if r == 0 and lk < 0: continue
        return False
    return True

def admissible(forms, lam3):
    # need a residue class mod small primes avoiding all forms; check primes 2,3,5,7 and parity constraints
    for p in (2, 3, 5, 7, 11, 13):
        ok = False
        for x in range(p):
            if all((a*x+b) % p != 0 for a, b in forms): ok = True; break
        if not ok: return False
    return True

A = [1,2,3,4,6,8,12,24]
sols = []
B = range(-30, 31)
for a1, a2, a3, a4 in product(A, repeat=4):
    if a1*a2 != 2*a3*a4: continue
    if a1 > a2 or a3 > a4: continue   # symmetry
    for b1, b2 in product(B, B):
        if b1*b2 % 2 == 0: continue  # n odd
        # a1 b2 + a2 b1 = 2(a3 b4 + a4 b3), b1 b2 - 2 b3 b4 = 1
        if (b1*b2 - 1) % 2: continue
        prod34 = (b1*b2 - 1)//2
        s = a1*b2 + a2*b1
        if s % 2: continue
        s //= 2  # = a3 b4 + a4 b3
        for b3 in B:
            if b3 % 2 == 0: continue
            # a4 b3 + a3 b4 = s -> b4 = (s - a4 b3)/a3
            if (s - a4*b3) % a3: continue
            b4 = (s - a4*b3)//a3
            if b3*b4 != prod34 or b4 % 2 == 0: continue
            forms = [(a1,b1),(a2,b2),(a3,b3),(a4,b4)]
            if not (auto_ok(a1,b1,a2,b2,1) and auto_ok(a2,b2,a1,b1,1) and auto_ok(a3,b3,a4,b4,2) and auto_ok(a4,b4,a3,b3,2)): continue
            if not admissible(forms, 2): continue
            sols.append(forms)
print(len(sols))
for f in sols[:40]: print(f)
