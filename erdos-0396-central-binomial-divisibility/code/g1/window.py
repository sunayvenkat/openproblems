# Top piece, T = floor(m/phi(m)): last level s = T-1 has window start rho = m - T phi(m).
# Phi_{2m}(t)^{-T} = prod_{e|m} (1+t^e)^{-T mu(m/e)}  (m odd)  -> exact coefficients up to any N using
# only the divisors e <= N, so the decisive sign is computable for huge m whenever rho is small.
#   top_sign(primes, T, rho) -> (N, sign) of the first nonzero c_N, N > rho  (CRT over 3 primes; sign of the
#   symmetric residue is exact once two prime counts agree, as in aur/deep.py).
#   python window.py  -> window_out.txt : checks against fastgood.first_sign and Thm W.
import sys, numpy as np
from itertools import combinations
sys.path.insert(0, '../agentV'); sys.path.insert(0, '../aur'); sys.path.insert(0, '..')
from fastgood import pf, phi, first_sign
from deep import crt, PR

def divs_upto(primes, N):
    out = [(1, 1)]
    for p in primes:
        out += [(e * p, -s) for e, s in out if e * p <= N]
    return out            # (e, mu(e))

def ser_top_mod(primes, T, N, P):
    # prod_{e|m, e<=N} (1+t^e)^{-T mu(m/e)} mod (t^{N+1}, P);  mu(m/e) = mu(m) mu(e)
    mum = (-1) ** len(primes)
    c = np.zeros(N + 1, dtype=np.int64); c[0] = 1
    for e, me in sorted(divs_upto(primes, N)):
        k = -T * mum * me
        for _ in range(abs(k)):
            if k > 0:                                   # times (1+t^e)
                c[e:] = (c[e:] + c[:-e]) % P
            else:                                       # divided by (1+t^e): alternating running sums per residue class
                L = -(-(N + 1) // e) * e
                b = np.zeros(L, dtype=np.int64); b[:N + 1] = c
                b = b.reshape(-1, e); sg = np.where(np.arange(b.shape[0]) % 2 == 0, 1, P - 1)[:, None]
                b = (np.cumsum((b * sg) % P, axis=0) % P * sg) % P
                c = b.reshape(-1)[:N + 1].copy()
    return c

def top_sign(primes, T, rho, W=64, cap=10 ** 7):
    while True:
        N = rho + W
        R = [ser_top_mod(primes, T, N, P) for P in PR[:3]]
        nz = [i for i in range(rho + 1, N + 1) if any(int(r[i]) for r in R)]
        if nz:
            i = nz[0]
            while True:
                rs = [int(r[i]) for r in R]; k = len(R)
                if crt(rs[:-1], PR[:k - 1]) == crt(rs, PR[:k]):
                    v = crt(rs, PR[:k]); return i, (1 if v > 0 else -1), v
                R.append(ser_top_mod(primes, T, N, PR[k]))
        if N > cap: return None
        W *= 4

def thmW(primes, rho):
    # Thm W (T = 2): returns True (good) / False (bad) / None (not decided by the closed form)
    p1 = primes[0]; mu = (-1) ** len(primes)
    if rho > 2 * p1 - 3: return None
    if mu == -1:
        if rho == 1: return False
        return True if any(rho <= q <= 2 * p1 - 1 and not (q == rho == 2 * p1 - 1) for q in primes) else None
    N = rho + 1; S = sum(N + 1 - q for q in primes if q <= N)
    c = (N + 1) - 2 * S
    return None if c == 0 else c < 0

if __name__ == '__main__':
    # 1. top_sign vs fastgood.first_sign (level T-1 of the top piece) for odd squarefree m <= 30000 with T >= 2;
    #    Thm W closed form vs top_sign for m <= 2e6 where it applies (rho <= 2 p1 - 3)
    bad = cnt = 0; wcnt = wbad = 0; dec = {}
    for m in range(15, 2000001, 2):
        ps = pf(m)
        if len(ps) < 2 or any(m % (p * p) == 0 for p in ps): continue
        f = phi(m); T = m // f
        if T < 2: continue
        rho = m - T * f
        if m <= 30000:
            r = top_sign(ps, T, rho); fs = first_sign(m, m, T - 1)
            cnt += 1; bad += (r is None) or fs is None or (r[0], r[1]) != tuple(fs)
        if T == 2:
            w = thmW(ps, rho)
            if w is not None:
                r = top_sign(ps, 2, rho)
                wcnt += 1; wbad += w != (r[1] < 0)
                dec[(len(ps) % 2, w)] = dec.get((len(ps) % 2, w), 0) + 1
    print(f'top_sign vs fastgood.first_sign: {cnt} odd sqfree m<=30000 with T>=2, mismatches {bad}')
    print(f'Thm W closed form (T=2, rho<=2p1-3), m<=2e6: {wcnt} cases decided, mismatches {wbad}; (omega%2, good) counts {dec}')
    # 2. density of good rho (T=2) in [1, p1 p2) for sample prime sets with all primes > P
    from sympy import primerange
    for P in (3, 5, 7, 11):
        base = list(primerange(P + 1, 400))
        for parity in (0, 1):
            ps = base[:30 + parity]
            p1, p2 = ps[0], ps[1]
            g = [rho for rho in range(1, p1 * p2 - 40, 2) if (lambda r: r is not None and r[1] < 0)(top_sign(ps, 2, rho, cap=p1 * p2))]
            tot = len(range(1, p1 * p2 - 40, 2))
            print(f'P={P} omega={len(ps)} (mu={(-1)**len(ps):+d}) p1={p1}: good rho in [1,{p1*p2-40}): {len(g)}/{tot}; first good rho: {g[:12]}')
