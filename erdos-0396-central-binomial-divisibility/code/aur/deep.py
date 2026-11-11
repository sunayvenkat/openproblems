# Level-s sign of piece Phi_{2d} in x^m+1 (K = m/d), via the binomial reduction
#   tail((x^m+1)/f^{s+1}) = sum_{r=1}^{s} (-1)^{r+1} C(K,r) tail(w^r/f^{s+1}),  w = x^d+1,
#   [x^{-1-i}] tail(w^r/f^{s+1}) = [t^{rd-(s+1)phi+1+i}] (1+t^d)^r Phi_{2d}(t)^{-(s+1)}.
# Carry at level s iff the first nonzero coefficient (smallest i) is negative.
# Exact integers by CRT over 5 primes < 2^31 (consistency of 4-prime and 5-prime CRT is checked).
import sys, numpy as np
from math import comb
sys.path.insert(0, '../agentV'); sys.path.insert(0, '..')
from fastgood import pf, phi, sqfree_divs
PR = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563]

def ser_mod(n, ex, N, P):
    c = np.zeros(N + 1, dtype=np.int64); c[0] = 1
    for e, mu in sorted(sqfree_divs(n)):
        if e > N: continue
        k = ex * mu
        for _ in range(abs(k)):
            if k > 0:
                c[e:] = (c[e:] - c[:-e].copy()) % P
            else:
                L = -(-(N + 1) // e) * e
                b = np.zeros(L, dtype=np.int64); b[:N + 1] = c
                c = (np.cumsum(b.reshape(-1, e), axis=0) % P).reshape(-1)[:N + 1].copy()
    return c

def coeffs_mod(m, d, s, W, P):
    K, dl = m // d, phi(d)
    Imax = s * d - (s + 1) * dl + W
    ph = ser_mod(2 * d, -(s + 1), max(Imax, 1), P)
    out = np.zeros(W, dtype=np.int64)
    for r in range(1, s + 1):
        base = r * d - (s + 1) * dl + 1
        acc = np.zeros(W, dtype=np.int64)
        for a in range(r + 1):
            lo = base - a * d
            idx = np.arange(lo, lo + W)
            ok = idx >= 0
            vals = np.zeros(W, dtype=np.int64); vals[ok] = ph[idx[ok]]
            acc = (acc + (comb(r, a) % P) * vals) % P
        sg = 1 if r % 2 == 1 else -1
        out = (out + (sg * comb(K, r)) % P * acc) % P
    return out

def crt(res, ps):
    x, M = 0, 1
    for r, p in zip(res, ps):
        t = ((r - x) * pow(M, -1, p)) % p; x += M * t; M *= p
    return x - M if x > M // 2 else x

def primes_below(n, k):
    out, c = [], n - 1
    while len(out) < k:
        if all(c % q for q in range(3, int(c**0.5) + 1, 2)): out.append(c)
        c -= 2
    return out
PR = primes_below(2**31, 40)

def level(m, d, s, W=64):
    # adds primes until the symmetric CRT value is stable for two consecutive prime counts
    while True:
        R = [coeffs_mod(m, d, s, W, P) for P in PR[:3]]
        while True:
            nz = [i for i in range(W) if any(int(r[i]) for r in R)]
            if not nz: break
            i = nz[0]; rs = [int(r[i]) for r in R]; k = len(R)
            if k >= 3 and crt(rs[:-1], PR[:k-1]) == crt(rs, PR[:k]):
                # a nonzero residue mod some prime means the true value is nonzero
                return i, crt(rs, PR[:k])
            R.append(coeffs_mod(m, d, s, W, PR[len(R)]))
        W *= 4
        if W > 10**6: return None

def deep(m, d, smax=12):
    T = m // phi(d)
    for s in range(1, min(smax, T - 1) + 1):
        r = level(m, d, s)
        if r and r[1] < 0: return s, r
    return None, None

if __name__ == '__main__':
    m = int(sys.argv[1])
    for d in map(int, sys.argv[2:]):
        s, r = deep(m, d)
        print(f'd={d} {pf(d)} K={m//d}: first negative level {s} {"" if r is None else "(offset %d, coeff %.3e)" % (r[0], r[1])}', flush=True)
