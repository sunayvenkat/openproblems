# Enumerate quadruple families for E_1 (any contents c0,c1) and verify with real primes.
from quad4 import split, admissible, good_large, val, carries_exact, isqrt
from sympy import isprime, factorint

def families(Amax):
    out = []
    for A in range(1, Amax + 1):
        for d in range(1, isqrt(4*A) + 1):
            if (4*A) % d: continue
            e = 4*A // d
            if (d + e) % 2: continue
            v, u = (d + e)//2, (e - d)//2
            if u <= 0: continue
            for B in range(0, 2*A):
                if (B*B - u*u) % (4*A): continue
                C = (B*B - u*u)//(4*A)
                s0, s1 = split(A, B, C), split(A, B, C - 1)
                if not s0 or not s1: continue
                c0, f1, f2 = s0; c1, f3, f4 = s1
                if admissible([f1, f2, f3, f4]) and good_large(c0, (f1, f2), c1, (f3, f4)):
                    out.append((A, B, C, c0, f1, f2, c1, f3, f4))
    return out

def in_E1(n, fact):            # fact: dict prime->exponent of n(n-1)
    return all(carries_exact(n, p) >= e for p, e in fact.items())

def check(fam, X=10**6, want=5):
    A, B, C, c0, f1, f2, c1, f3, f4 = fam
    small = factorint(c0 * c1)
    hits, misses = [], 0
    for x in range(1, X):
        vs = [val(f, x) for f in (f1, f2, f3, f4)]
        if min(vs) <= max(small, default=1) or not all(isprime(t) for t in vs): continue
        n = A*x*x + B*x + C
        assert n == c0*vs[0]*vs[1] and n - 1 == c1*vs[2]*vs[3]
        fact = dict(small); fact.update({p: 1 for p in vs})
        if in_E1(n, fact): hits.append((x, n))
        else: misses.append(x) if isinstance(misses, list) else None; misses = misses
        if len(hits) >= want: break
    return hits

if __name__ == "__main__":
    fams = families(600)
    print(len(fams), "families, A <= 600")
    for f in fams:
        h = check(f)
        print(f, "first E_1 hits:", h[:3])
