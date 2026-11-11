# Top piece of odd m: level s (1<=s<=T-1, T=floor(m/phi)) is good iff c_s := [y^K] Psi_m(y)^{s+1} < 0, K = m-(s+1)phi+1
# (calibrated: m=105 -> +3 bad; 165 -> -1 good; 195 -> -4 good, matching DRAFT §6.4).
import sys, numpy as np
from numpy.fft import rfft, irfft
from sympy import divisors, factorint
from sympy.functions.combinatorial.numbers import mobius
PRIMES = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549]
def inv_phi_mod(m, N, p):
    a = np.zeros(N, dtype=np.int64); a[0] = 1
    for d in divisors(m):
        if d >= N: continue
        mu = int(mobius(m//d))
        if mu == 1:
            L = -(-N//d)*d; b = np.zeros(L, dtype=np.int64); b[:N] = a
            b = np.cumsum(b.reshape(-1, d), axis=0) % p; a = b.reshape(-1)[:N]
        elif mu == -1:
            a[d:] = (a[d:] - a[:-d]) % p
    return a
def crt(rs):
    x, M = 0, 1
    for r, p in zip(rs, PRIMES):
        x = x + M * ((r - x) * pow(M, -1, p) % p); M *= p
    return x - M if x > M//2 else x
def conv_mod(u, v, N, p):   # exact (u*v) mod y^N mod p via 11-bit splits
    L = 1
    while L < 2*N: L *= 2
    parts = lambda w: [(w % 2048), ((w >> 11) % 2048), (w >> 22)]
    U = [rfft(x.astype(np.float64), L) for x in parts(u)]; V = [rfft(x.astype(np.float64), L) for x in parts(v)]
    res = np.zeros(N, dtype=np.int64)
    for i in range(3):
        for j in range(3):
            c = np.rint(irfft(U[i]*V[j], L)[:N]).astype(np.int64) % p
            res = (res + c * pow(2, 11*(i+j), p)) % p
    return res
m = int(sys.argv[1]); phi = 1
for q, e in factorint(m).items(): phi *= (q-1)*q**(e-1)
T = m // phi; print('m', m, 'phi', phi, 'm/phi %.3f' % (m/phi), 'T', T, flush=True)
for s in range(1, T):
    K = m - (s+1)*phi + 1; N = K + 1; vals = []
    for p in PRIMES:
        psi = (-inv_phi_mod(m, N, p)) % p
        if s == 1:
            prod = (psi[:K+1] * psi[K::-1]) % p
            tot = 0
            for i in range(0, K+1, 1 << 20): tot = (tot + int(prod[i:i+(1 << 20)].sum())) % p
            vals.append(tot)
        else:
            cur = psi.copy()
            for _ in range(s): cur = conv_mod(cur, psi, N, p)
            vals.append(int(cur[K]))
    c = crt(vals); print('level s=%d: K=%d  c_s = %d  -> %s' % (s, K, c, 'GOOD' if c < 0 else 'bad'), flush=True)
