# Route (d): n(w) = N(x(w)), N = g5 E_2 quadratic, x(w) = a2 w^2 + a1 w + a0 integer quadratic chosen so that
# N(x)-3 = 6*P(x), P = 8820x^2+7861x+1751 (disc 20041 = 49*409), also splits:  x(w)-alpha splits over K=Q(sqrt409)
# <=> disc(x - alpha) = (u + v sqrt409)^2  <=>  a2 = 1260uv, a1^2 - 4 a2 a0 = T := u^2 + 2246uv + 409v^2.
import sys, sympy as sp
from fractions import Fraction as Fr
from check import w, analyze, crt_class, shifts
N = lambda x: 52920*x**2 + 47166*x + 10509

def cands(H, A2max):
    seen = set()
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
                if (a1*a1 - T) % (4*a2) == 0:
                    key = (a2, a1, (a1*a1 - T)//(4*a2))
                    if key not in seen: seen.add(key); yield key

if __name__ == "__main__":
    H, A2max = int(sys.argv[1]), int(sys.argv[2])
    cs = sorted(cands(H, A2max))
    print(len(cs), "quadratics x(w)")
    for a2, a1, a0 in cs[:int(sys.argv[3])]:
        n = sp.expand(N(a2*w**2 + a1*w + a0))
        degs = [[f.degree() for f, _ in ps] for _, ps in shifts(n, 3)]
        print("x(w) =", (a2, a1, a0), "piece degrees", degs)
        r = analyze(n, 3, verbose=False)
        if r: print("   GOOD:", crt_class(*r[1:]))
