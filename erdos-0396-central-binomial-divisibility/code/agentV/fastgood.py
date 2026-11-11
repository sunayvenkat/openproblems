"""Faster exact 'good exponent' test (same rule as lemC.piece_report, NOTES/DRAFT §5).
Series of Phi_n(t)^ex are computed only up to the window just past E_s, using only divisors e <= N,
with numpy object arrays (exact Python ints).  python fastgood.py m [m ...]   (top piece only: add --top)"""
import sys, numpy as np
from itertools import combinations


def pf(n):
    out, p = [], 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0: n //= p
        p += 1
    return out + ([n] if n > 1 else [])


def sqfree_divs(n):
    "divisors e of n with mu(n/e) != 0, as (e, mu(n/e))"
    ps = pf(n); out = []
    for r in range(len(ps) + 1):
        for c in combinations(ps, r):
            q = 1
            for p in c: q *= p
            out.append((n // q, (-1) ** r))
    return out


def phi(n):
    r = n
    for p in pf(n): r = r // p * (p - 1)
    return r


def series(n, ex, N):
    "Phi_n(t)^ex mod t^(N+1), n > 1"
    c = np.zeros(N + 1, dtype=object); c[:] = 0; c[0] = 1
    for e, mu in sorted(sqfree_divs(n)):
        if e > N: continue
        k = ex * mu
        for _ in range(abs(k)):
            if k > 0:                      # times (1 - t^e)
                c[e:] = c[e:] - c[:-e]
            else:                          # divided by (1 - t^e): running sums along residue classes
                L = -(-(N + 1) // e) * e
                b = np.zeros(L, dtype=object); b[:] = 0; b[:N + 1] = c
                c = b.reshape(-1, e).cumsum(axis=0).reshape(-1)[:N + 1]
    return c


def first_sign(m, d, s):
    delta = phi(2 * d); E = m - (s + 1) * delta; cap = m + 2 * delta + 5; W = 64
    while True:
        N = min(E + W, cap)
        c = series(2 * d, -(s + 1), N)
        for t in range(E + 1, N + 1):
            v = c[t] + (c[t - m] if t >= m else 0)
            if v: return (t, 1 if v > 0 else -1)
        if N == cap: return None
        W *= 8


def good(m, d):
    delta = phi(2 * d)
    for s in range(1, m // delta):
        r = first_sign(m, d, s)
        if r and r[1] < 0: return s
    return None


if __name__ == "__main__":
    top = "--top" in sys.argv
    for m in [int(a) for a in sys.argv[1:] if a != "--top"]:
        divs = [d for d in range(1, m + 1) if m % d == 0] if (not top and m < 10**6) else [m]  # shortcut: m >= 1e6 -> top piece only
        res = {d: good(m, d) for d in divs}
        bad = [d for d, g in res.items() if g is None]
        print(f"m={m} primes={pf(m)} phi/m={phi(m)/m:.4f} checked {len(divs)} pieces; "
              f"top: {'GOOD s=%d' % res[m] if res[m] else 'BAD'} first-coeff(s=1)={first_sign(m, m, 1)}; BAD pieces: {bad}", flush=True)
