# Core helpers for the Laurent-sign carry criterion (agentAC).
# Piece f = Phi_{2d}(x), d | m odd, delta = phi(d) (=1 for d=1).
# Level s>=1 (needs (s+1)*delta <= m): c_N = [t^N] Phi_{2d}(t)^{-(s+1)} for E < N <= m - delta,
# E = m-(s+1)delta.  (For N < m the factor (1+t^m) is invisible; the first nonzero c_N, if any,
# has N <= m - delta.)  Carry at level s  <=>  first nonzero c_N is negative.
import numpy as np
from math import gcd
from functools import lru_cache

def factor(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def divisors(n):
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return sorted(ds)

def mu(n):
    f = factor(n)
    return 0 if any(e > 1 for e in f.values()) else (-1) ** len(f)

def phi(n):
    r = n
    for p in factor(n): r = r // p * (p - 1)
    return r

def _mul1(c, e, k, P):
    "multiply series c by (1-t^e)^k, k>=0"
    for _ in range(k):
        c[e:] = c[e:] - c[:-e]
        if P: c %= P
    return c

def _div1(c, e, k, P):
    "divide series c by (1-t^e)^k"
    L = len(c); R = -(-L // e) * e
    for _ in range(k):
        z = np.zeros(R, dtype=c.dtype); z[:L] = c
        z = np.cumsum(z.reshape(-1, e), axis=0).reshape(-1)
        c = z[:L]
        if P: c = c % P
    return c

def cyclo_pow_series(n, ex, N, P=None):
    """[t^0..t^N] of Phi_n(t)^ex (n>1, ex any int). Exact (python ints) if P is None, else mod P (int64)."""
    c = np.zeros(N + 1, dtype=object if P is None else np.int64); c[0] = 1
    ops = []
    for e in divisors(n):
        k = ex * mu(n // e)
        if k and e <= N: ops.append((e, k))
    # multiplications first keeps the object path simple; mod path does not care
    for e, k in ops:
        if k > 0: c = _mul1(c, e, k, P)
    for e, k in ops:
        if k < 0: c = _div1(c, e, -k, P)
    return c

def level_sign(m, d, s, c=None):
    """first nonzero c_N (E<N<=m-delta) for piece d, level s: returns (N, sign) or None."""
    delta = phi(d)
    E = m - (s + 1) * delta
    Nmax = m - delta
    if c is None: c = cyclo_pow_series(2 * d, -(s + 1), Nmax)
    for N in range(E + 1, Nmax + 1):
        v = c[N]
        if v: return (N, 1 if v > 0 else -1)
    return None

def piece_report(m, d, stop_at_good=False):
    delta = phi(d); T = m // delta
    res = []
    for s in range(1, T):
        r = level_sign(m, d, s)
        res.append((s, r))
        if stop_at_good and r and r[1] < 0: break
    good = any(r and r[1] < 0 for _, r in res)
    return good, res

if __name__ == '__main__':
    # self-check against the main thread's lemC.py on a few cases
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    import lemC
    for m in (15, 21, 45, 105, 165, 195):
        for d in divisors(m):
            g1, r1 = piece_report(m, d)
            g2, r2 = lemC.piece_report(m, d)
            assert g1 == g2, (m, d, r1, r2)
            assert [x[1] for x in r1] == [x[1] for x in r2], (m, d, r1, r2)
    print('core.py agrees with lemC.py')
