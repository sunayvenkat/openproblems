# Top-piece sign of m = m0*r at level s = e-1, for ALL primes r at once (r ∤ m0, r odd).
# Two-scale: Phi_{m0 r}(y) = Phi_{m0}(y^r)/Phi_{m0}(y)  =>  Phi_m^{-e} = Phi_{m0}(y)^e * Phi_{m0}(y^r)^{-e}.
# With phi0 = phi(m0), delta = m0 - e*phi0 >= 0, K_m = m - e*phi(m) + 1 = r*delta + e*phi0 + 1, and palindromy of
# beta = Phi_{m0}^e (degree e*phi0), the window coefficients w_m(t) = (-1)^e [y^{K_m+t}] Phi_m^{-e} (= [y^{K_m+t}] Psi_m^e)
# satisfy the sampled convolution
#     w_{m0 r}(t) = sum_{j >= 1, t+1 <= r j <= e*phi0+1+t}  w_{m0}(j-1) * beta_{r j - 1 - t}.
# Level s carries iff the first nonzero w(t) is negative ("GOOD").  For r > e*phi0 + 1 only j = 1 survives and the first
# nonzero is t = r-1-e*phi0 with value w_{m0}(0): m0 r inherits the sign of m0 (inflation).
# Usage: python toppiece_rscan.py m0 e rmin rmax nprimes [check]   -> writes rscan_<m0>_e<e>.txt
import sys, numpy as np
from sympy import divisors, factorint
from sympy.functions.combinatorial.numbers import mobius
ALLP = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549, 2147483543, 2147483497,
        2147483489, 2147483477, 2147483423, 2147483399, 2147483353, 2147483323]
TMAX = 3
def phi_of(n):
    r = 1
    for q, ex in factorint(n).items(): r *= (q-1)*q**(ex-1)
    return r
def cyclo_power(m, e, N, p=None):   # Phi_m(y)^e mod y^N (mod p, or exact if p is None)
    a = np.zeros(N, dtype=np.int64 if p else object); a[0] = 1
    for d in divisors(m):
        if d >= N: continue
        k = e * int(mobius(m//d))
        for _ in range(abs(k)):
            if k > 0:
                a[d:] = a[d:] - a[:-d]
                if p: a[d:] %= p
            else:
                L = -(-N//d)*d; b = np.zeros(L, dtype=a.dtype); b[:N] = a
                b = np.cumsum(b.reshape(-1, d), axis=0)
                if p: b %= p
                a = b.reshape(-1)[:N]
    return a
def window(m, e, tmax, p=None):    # w_m(0..tmax), direct
    K = m - e*phi_of(m) + 1
    a = cyclo_power(m, -e, K + tmax + 1, p)[K:]
    return [(-x) % p if (p and e % 2) else (-x if e % 2 else x) for x in a]
def scan_mod(m0, e, rs, p, jmax):
    phi0 = phi_of(m0); delta = m0 - e*phi0; D = e*phi0
    beta = cyclo_power(m0, e, D + 1, p)
    alpha = cyclo_power(m0, -e, delta + jmax + 1, p)
    w0 = alpha[delta+1: delta+1+jmax]
    if e % 2: w0 = (-w0) % p
    out = np.zeros((TMAX+1, len(rs)), dtype=np.int32)   # residues < 2^31
    for t in range(TMAX+1):
        J = (D + 1 + t) // rs                       # j runs 1..J (r > t always)
        i = 0
        while i < len(rs):
            Jv = int(J[i]); i2 = i
            cap = max(1, 10**7 // max(Jv, 1))
            while i2 < len(rs) and J[i2] == Jv and i2 - i < cap: i2 += 1
            if Jv > 0:
                R = rs[i:i2, None]; js = np.arange(1, Jv+1)[None, :]
                out[t, i:i2] = (((beta[R*js - 1 - t] * w0[:Jv][None, :]) % p).sum(axis=1) % p)
            i = i2
    return out
def crt(rs, ps):
    x, M = 0, 1
    for r_, p in zip(rs, ps):
        x = x + M * ((int(r_) - x) * pow(M, -1, p) % p); M *= p
    return (x - M if x > M//2 else x), M
if __name__ == '__main__':
    m0, e, rmin, rmax, npr = map(int, sys.argv[1:6]); check = len(sys.argv) > 6
    if m0 > 10**6: TMAX = 1                       # memory: offsets 0..1 only for huge m0 (zeros are flagged)
    phi0 = phi_of(m0); assert m0 - e*phi0 >= 0 and m0 % 2
    sieve = np.ones(rmax + 1, dtype=bool); sieve[:2] = False
    for q in range(2, int(rmax**0.5) + 1):
        if sieve[q]: sieve[q*q::q] = False
    rs = np.array([r for r in np.nonzero(sieve)[0] if r >= max(rmin, 3) and m0 % r], dtype=np.int64)
    jmax = (e*phi0 + 1 + TMAX) // int(rs[0]) + 1
    print('m0', m0, 'e', e, 'phi0', phi0, 'delta', m0 - e*phi0, 'primes r', len(rs), rs[0], '..', rs[-1], flush=True)
    PS = ALLP[:npr]; res = []
    for p in PS:
        res.append(scan_mod(m0, e, rs, p, jmax)); print('  CRT prime done', flush=True)
    res = np.array(res)                              # [prime, t, r]
    lines = []; ngood = nbad = 0; maxlog = 0
    for k, r in enumerate(rs):
        for t in range(TMAX+1):
            c, M = crt(res[:, t, k], PS)
            if c: break
        lg = len(str(abs(c))) - 1 if c else -1; maxlog = max(maxlog, lg)
        good = c < 0; ngood += good; nbad += (c > 0)
        lines.append('%d %d %s %d' % (r, t, 'GOOD' if good else ('bad' if c > 0 else 'zero'), lg))
        if check and m0 * r < 20000:
            ex = window(m0 * int(r), e, TMAX)
            tt = next((u for u in range(TMAX+1) if ex[u]), None)
            assert (tt is None and c == 0) or (tt == t and ex[t] == c), (r, t, c, tt, ex)
    out = 'rscan_%d_e%d.txt' % (m0, e)
    with open(out, 'w') as f:
        f.write('# m0 %d level %d (e=%d): r first_nonzero_offset sign log10|c|; CRT range 10^%d\n' % (m0, e-1, e, len(str(M))-1))
        f.write('\n'.join(lines) + '\n')
    print('GOOD', ngood, 'bad', nbad, 'max log10|c|', maxlog, 'CRT log10 range', len(str(M)) - 1, '->', out, flush=True)
    if check: print('exact check passed for m0*r < 20000')
