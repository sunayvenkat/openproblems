# Empirical counts of D_0 = {n : n | C(2n,n)} and E_1 = {n : n(n-1) | C(2n,n)} up to N.
import sys
from quad4 import carries_exact
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2*10**6
spf = list(range(N + 1))
for p in range(2, int(N**0.5) + 1):
    if spf[p] == p:
        for m in range(p*p, N + 1, p):
            if spf[m] == m: spf[m] = p
def fac(m):
    f = {}
    while m > 1:
        p = spf[m]; f[p] = f.get(p, 0) + 1; m //= p
    return f
def ok(n, m):          # m | C(2n,n) ?
    return all(carries_exact(n, p) >= e for p, e in fac(m).items())
inD = [False]*(N + 1)
e1 = 0; marks = {}
for n in range(2, N + 1):
    inD[n] = ok(n, n)
    if inD[n] and ok(n, n - 1): e1 += 1
    if n in (10**4, 10**5, 10**6, 2*10**6, 5*10**6, 10**7):
        d0 = sum(inD[2:n+1])
        marks[n] = (d0 / n, e1 / n, e1 / n / (d0 / n)**2)
for n, (a, b, c) in marks.items():
    print(f"N={n:>9}: dens D0={a:.4f}  dens E1={b:.5f}  E1/D0^2={c:.3f}")
