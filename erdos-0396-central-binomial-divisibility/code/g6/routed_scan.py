# Fast shift-3 screen for route (d): F = (X-u)^2 - 409v^2, G = (X+u)^2 - 409v^2, X = 2 a2 w + a1 (up to 4a2^2).
# R_F = 52920 a2^2 / lc(F')^2 where F' = primitive integer multiple of F; carry needs frac(R) > 1/2 (boundary -> full check).
import sys, sympy as sp
from fractions import Fraction as Fr
from math import gcd, lcm
from routed import cands, N
from check import w, analyze, crt_class

def prim_lc(c2, c1, c0):            # Fractions -> lc of primitive integer multiple
    L = lcm(c2.denominator, c1.denominator, c0.denominator)
    a = [int(c * L) for c in (c2, c1, c0)]
    return a[0] // gcd(*a)

def uv_of(H, A2max):
    for u1 in range(1, H+1):
      for u2 in range(1, H+1):
        for v1 in range(1, H+1):
          for v2 in range(1, H+1):
            u, v = Fr(u1, u2), Fr(v1, v2)
            if u.numerator != u1 or v.numerator != v1: continue
            a2 = 1260*u*v; T = u*u + 2246*u*v + 409*v*v
            if a2.denominator != 1 or T.denominator != 1 or a2 > A2max: continue
            a2, T = int(a2), int(T)
            for a1 in range(0, 2*a2):
                if (a1*a1 - T) % (4*a2) == 0: yield a2, a1, (a1*a1 - T)//(4*a2), u, v

if __name__ == "__main__":
    H, A2max = int(sys.argv[1]), int(sys.argv[2])
    hits = seen = 0
    for a2, a1, a0, u, v in uv_of(H, A2max):
        seen += 1
        Rs = []
        for sg in (1, -1):
            b = a1 - sg*u                    # (2a2 w + b)^2 - 409 v^2
            lam = prim_lc(Fr(4*a2*a2), Fr(4*a2)*b, b*b - 409*v*v)
            Rs.append(Fr(52920*a2*a2, lam*lam))
        if all(R % 1 >= Fr(1, 2) for R in Rs):
            hits += 1
            n = sp.expand(N(a2*w**2 + a1*w + a0))
            r = analyze(n, 3, verbose=False)
            print((a2, a1, a0), "u,v", u, v, "R3 =", [str(R) for R in Rs], "FULL:", r is not None and crt_class(*r[1:]))
    print(seen, "screened,", hits, "pass shift 3")
