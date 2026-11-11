# Faster E_2 search: B runs only over square roots of u^2 mod 4A.
import sys
from e2fam import admissible, good_large, check, split, val
from math import isqrt, gcd
from sympy.ntheory import sqrt_mod

def triples(Amax):
    for v in range(1, isqrt(4*Amax) + 2):
        for u in range(2 - v % 2 if v % 2 == 0 else 1, v, 2):
            A4 = v*v - u*u
            if A4 % 4 or A4 // 4 > Amax: continue
            A = A4 // 4
            w2 = u*u + 8*A
            if isqrt(w2)**2 == w2:
                yield A, u

def run(Amax, k=2):
    out = []
    for A, u in triples(Amax):
        roots = sqrt_mod(u*u % (4*A), 4*A, all_roots=True) or []
        for B in sorted({r % (2*A) for r in roots}):
            C = (B*B - u*u) // (4*A)
            sp = [split(A, B, C - i) for i in range(k + 1)]
            if not all(sp): continue
            parts = [(s[0], (s[1], s[2])) for s in sp]
            if good_large((A, B, C), parts) and admissible([f for _, F in parts for f in F]):
                out.append(((A, B, C), parts))
                print(out[-1], flush=True)
    return out

if __name__ == "__main__":
    Amax = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    fams = run(Amax)
    print(len(fams), "families with A <=", Amax)
    for f in fams[:5]:
        print(f, check(f, X=2*10**6))
