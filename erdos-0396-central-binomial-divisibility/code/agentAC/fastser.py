# Fast modular series for Phi_n(u)^ex (two 31-bit primes + CRT, symmetric lift).
# Only additions are needed, so int64 cumsums of 31-bit residues never overflow for N < 2^32.
import numpy as np
from core import divisors, mu

P1, P2 = 2147483629, 2147483587   # primes < 2^31

def _ser_mod(n, ex, N, P):
    c = np.zeros(N + 1, dtype=np.int64); c[0] = 1
    for e in divisors(n):
        k = ex * mu(n // e)
        if k == 0 or e > N: continue
        if k > 0:
            for _ in range(k):
                c[e:] = (c[e:] - c[:-e]) % P
        else:
            L = N + 1; R = -(-L // e) * e
            for _ in range(-k):
                z = np.zeros(R, dtype=np.int64); z[:L] = c
                c = (np.cumsum(z.reshape(-1, e), axis=0) % P).reshape(-1)[:L]
    return c

def cyclo_pow_series_fast(n, ex, N):
    """Phi_n(u)^ex coefficients 0..N as python ints, valid if |true coeff| < P1*P2/2 (~2^61)."""
    a = _ser_mod(n, ex, N, P1); b = _ser_mod(n, ex, N, P2)
    # CRT: x = a + P1 * ((b - a) * inv(P1) mod P2)
    inv = pow(P1, -1, P2)
    t = ((b - a) % P2) * inv % P2       # fits: < 2^31 * 2^31 = 2^62
    out = []
    M = P1 * P2
    for ai, ti in zip(a.tolist(), t.tolist()):
        x = ai + P1 * ti
        if x > M // 2: x -= M
        out.append(x)
    return out

if __name__ == '__main__':
    from core import cyclo_pow_series
    for n, ex, N in [(105, -2, 300), (210, -3, 500), (1155, -2, 2000), (2310, -4, 3000)]:
        A = list(cyclo_pow_series(n, ex, N)); B = cyclo_pow_series_fast(n, ex, N)
        assert A == B, (n, ex)
    print('fastser agrees with exact series')
