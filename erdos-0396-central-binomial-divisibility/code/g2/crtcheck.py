# Exact level-1 coefficient a_1 = [y^{rho0+1}] Q^2 by CRT (aur/deep.py ser_mod), for m too large for object series.
# Usage: python crtcheck.py m [k]
import sys
sys.path.insert(0, '../aur')
from deep import ser_mod, crt, PR
from core2 import phi
m = int(sys.argv[1]); k = int(sys.argv[2]) if len(sys.argv) > 2 else 2
n = m + 1 - k * phi(m)
res, prev = [], None
for i, P in enumerate(PR):
    res.append(int(ser_mod(2 * m, -k, n, P)[n]))   # [t^n]Phi_2m^-k = (-1)^n [y^n]Q^k, n even
    v = crt(res, PR[:i + 1])
    if i >= 2 and v == prev: break
    prev = v
print(f"m={m} k={k} n={n}: exact a_{k-1} = {v}  (sign {'+' if v > 0 else '-'}, {len(res)} primes)")
