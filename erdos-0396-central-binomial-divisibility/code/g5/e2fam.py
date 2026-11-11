# E_2 from 6 linear forms: Q(x)-i = c_i * L_{i1} * L_{i2}, i = 0,1,2.
# Needs disc(Q), disc(Q)+4A, disc(Q)+8A all squares (3 squares in AP).
from quad4 import split, val, carries_exact
from math import isqrt
from sympy import isprime, factorint

def admissible(forms):
    for l in (2, 3, 5, 7, 11):
        if not any(all(val(f, x) % l for f in forms) for x in range(l)):
            return False
    return True

def good_large(Q, parts):
    A, B, C = Q
    for x in (10**60 + 7, 10**61 + 13, 3 * 10**59 + 1):
        n = A*x*x + B*x + C
        for i, (c, F) in enumerate(parts):
            for f in F:
                if carries_exact(n, val(f, x)) < 1:
                    return False
    return True

def families(Amax, k=2):
    out = []
    for v in range(1, isqrt(4*Amax) * 3):
        for u in range(v % 2, v, 2):
            A4 = v*v - u*u
            if A4 % 4 or A4 // 4 > Amax or A4 == 0: continue
            A = A4 // 4
            ok = all(isqrt(u*u + 4*A*i)**2 == u*u + 4*A*i for i in range(k + 1))
            if not ok or u == 0: continue
            for B in range(0, 2*A):
                if (B*B - u*u) % (4*A): continue
                C = (B*B - u*u) // (4*A)
                sp = [split(A, B, C - i) for i in range(k + 1)]
                if not all(sp): continue
                parts = [(s[0], (s[1], s[2])) for s in sp]
                forms = [f for _, F in parts for f in F]
                if admissible(forms) and good_large((A, B, C), parts):
                    out.append(((A, B, C), parts))
    return out

def check(fam, X=3*10**6, want=3):
    (A, B, C), parts = fam
    forms = [f for _, F in parts for f in F]
    small = {}
    for i, (c, _) in enumerate(parts):
        for p, e in factorint(c).items():
            small[p] = small.get(p, 0) + e
    hits = []
    for x in range(1, X):
        vs = [val(f, x) for f in forms]
        if min(vs) <= 5 or not all(isprime(t) for t in vs): continue
        n = A*x*x + B*x + C
        fact = dict(small); fact.update({p: 1 for p in vs})
        if all(carries_exact(n, p) >= e for p, e in fact.items()):
            hits.append((x, n))
            if len(hits) >= want: break
    return hits

if __name__ == "__main__":
    fams = families(6000)
    print(len(fams), "E_2 families, A <= 6000")
    for f in fams[:8]:
        print(f, check(f))
