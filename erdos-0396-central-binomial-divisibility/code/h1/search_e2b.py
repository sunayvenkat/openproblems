# E2 sextuples: wider search; require every leading coeff a_j^2 < 2*lam0*a1*a2 (no q^2>2n regime) and admissibility.
import sys
from math import gcd
from search_e2 import split
from search2 import frac_fail, admissible
AM, BM = int(sys.argv[1]), int(sys.argv[2])
res = []
for lam0 in (1, 3, 5, 7):
  for a1 in range(1, AM+1):
    for a2 in range(a1, AM+1):
      A = lam0*a1*a2
      for b1 in range(-BM, BM+1):
        if gcd(a1, b1) != 1: continue
        for b2 in range(-BM, BM+1):
          if gcd(a2, b2) != 1: continue
          B = lam0*(a1*b2 + a2*b1); C = lam0*b1*b2
          if C % 2 == 0: continue
          s1 = split(A, B, C-1)
          if not s1: continue
          s2 = split(A, B, C-2)
          if not s2: continue
          mem = [(lam0, (a1,b1), (a2,b2)), s1, s2]
          forms = [m[1] for m in mem] + [m[2] for m in mem]
          pass
          fs = []
          for lam, f, g in mem:
              x1 = frac_fail(f[0], f[1], g[0], g[1], lam); x2 = frac_fail(g[0], g[1], f[0], f[1], lam)
              if x1 is None or x2 is None: fs = None; break
              fs += [x1, x2]
          if fs is None or sum(fs) > 0.8: continue
          if not admissible(forms): continue
          res.append((round(sum(fs),3), [round(f,3) for f in fs], mem))
res.sort(key=lambda t: t[0]); print(len(res))
for r in res[:20]: print(r)
