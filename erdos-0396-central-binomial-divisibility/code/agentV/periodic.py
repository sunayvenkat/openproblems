"""Independent Laurent first-coefficient method via the inverse cyclotomic polynomial:
   1/Phi_P = -Psi_P/(1-t^P)  =>  [t^N] Phi_P^{-k} = (-1)^k sum_j C(j+k-1,k-1) [t^(N-jP)] Psi_P^k ,
so the coefficient at N ~ m needs only Psi_P^k (degree k(P-phi(P))), not a length-m series.
Level k (= s+1) of piece d in j'(x^m+1): first nonzero c_N = a_N + a_{N-m}, N > E = m - k*phi(d); NEG => carry."""
import sys, numpy as np
from math import comb
from fastgood import series, phi, pf

_psi = {}
def psi(P):
    if P not in _psi:
        dg = P - phi(P)
        _psi[P] = [-int(v) for v in series(P, -1, dg)]          # first P coeffs of 1/Phi_P are -Psi_P
    return _psi[P]

def polpow(a, k):
    out = np.array([1], dtype=object); A = np.array(a, dtype=object)
    for _ in range(k): out = np.convolve(out, A)
    return [int(v) for v in out]

def a_coef(pk, P, k, N):
    if N < 0: return 0
    deg = len(pk) - 1; s = 0
    j = max(0, -(-(N - deg) // P))
    while N - j * P >= 0:
        s += comb(j + k - 1, k - 1) * pk[N - j * P]; j += 1
    return (-1) ** k * s

def first(m, d, k, W=None):
    P = 2 * d; delta = phi(d); E = m - k * delta
    pk = polpow(psi(P), k)
    for N in range(E + 1, E + 1 + (W or 4 * P)):   # shortcut: window 4P, returns None beyond it
        v = a_coef(pk, P, k, N) + a_coef(pk, P, k, N - m)
        if v: return N - E, v
    return None

if __name__ == "__main__":
    m = int(sys.argv[1]); kmax = int(sys.argv[2])
    for d in map(int, sys.argv[3:]):
        out = []
        for k in range(2, min(kmax, m // phi(d)) + 1):
            r = first(m, d, k); out.append((k, r[0], '%.3e' % r[1] if r else None))
            if r and r[1] < 0: break
        print(f"m={m} d={d} {pf(d)} levels (k, offset, first coeff): {out}  -> {'GOOD at level %d' % out[-1][0] if out and out[-1][2] and float(out[-1][2]) < 0 else 'no carry up to level %d' % out[-1][0]}", flush=True)
