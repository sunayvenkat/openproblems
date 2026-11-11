# Float evaluation of S_k(K) = [x^{delta-1}] D_k for piece d, as a polynomial in K (any odd K):
#   S_k(K) = sum_zeta Res_{x=zeta} (x^{Kd}+1)/Phi_{2d}(x)^{k+1}
#          = -(1/(2^{k+1} d)) sum_zeta zeta H(zeta)^{k+1} sum_{j=1}^k K^j/j! [w^{k-j}] Q_zeta(w),
#   Q_zeta(w) = exp(w/d + (k+1) Lam_zeta(w)),  Lam = log(H(zeta e^{w/d})/H(zeta)) - log((e^{2w}-1)/(2w)).
# [w^i] log((c e^{s w}-1)/(c-1)) = s^i/i! sum_{n=1}^i (-1)^{n+1} (n-1)! S2(i,n) A^n,  A = c/(c-1).
# Returns coefficient vectors cj[k] (cj[k][j] = coefficient of K^j) plus a per-k float error scale.
import sys, numpy as np
from math import factorial, lgamma, log, exp
from tr import sqfree_divs, phi, pf

def stirling2(N):
    S = [[0] * (N + 1) for _ in range(N + 1)]; S[0][0] = 1
    for i in range(1, N + 1):
        for n in range(1, i + 1): S[i][n] = n * S[i - 1][n] + S[i - 1][n - 1]
    return S

def kpoly(d, kmax, chunk=1 << 17):
    n2 = 2 * d; th = phi(d) / d
    a = np.arange(1, d, 2, dtype=np.int64); a = a[np.gcd(a, d) == 1]   # one of each conjugate pair
    es = [(e, mu) for e, mu in sqfree_divs(n2) if e != n2]
    logH = np.zeros(len(a), np.complex128)
    for e, mu in es: logH -= mu * np.log(np.exp(1j * np.pi * ((a * e) % n2) / d) - 1)
    L0 = logH.real.max() - log(2)
    S2 = stirling2(kmax)
    # scalar series log((e^{2w}-1)/(2w)) = log(e^{2w}-1)/(2w): via log of (sum (2w)^j/(j+1)!)
    B = np.array([2.0 ** j / factorial(j + 1) for j in range(kmax + 1)])
    lb = np.zeros(kmax + 1)
    for n in range(1, kmax + 1):   # log series recurrence (B0 = 1)
        lb[n] = B[n] - sum(j * lb[j] * B[n - j] for j in range(1, n)) / n
    acc = np.zeros((kmax + 1, kmax + 1), np.complex128); accb = np.zeros((kmax + 1, kmax + 1)); err = np.zeros(kmax + 1)
    for c0 in range(0, len(a), chunk):
        aa = a[c0:c0 + chunk]; lH = logH[c0:c0 + chunk]
        Lam = np.zeros((kmax + 1, len(aa)), np.complex128)
        for e, mu in es:
            c = np.exp(1j * np.pi * ((aa * e) % n2) / d); A = c / (c - 1); s = e / d
            Ap = [None, A]
            for n in range(2, kmax + 1): Ap.append(Ap[-1] * A)
            for i in range(1, kmax + 1):
                t = sum(((-1) ** (n + 1) * factorial(n - 1) * S2[i][n]) * Ap[n] for n in range(1, i + 1))
                Lam[i] -= mu * (s ** i / factorial(i)) * t
        Lam[1:] -= lb[1:, None]
        z = np.exp(1j * np.pi * aa / d)
        for k in range(1, kmax + 1):
            F = (k + 1) * Lam; F[1] += 1 / d
            Q = np.zeros_like(F); Q[0] = 1
            for n in range(1, k + 1):
                Q[n] = sum(i * F[i] * Q[n - i] for i in range(1, n + 1)) / n
            wgt = z * np.exp((k + 1) * (lH - log(2) - L0))
            for j in range(1, k + 1):
                acc[k, j] += 2 * np.sum(wgt * Q[k - j]); accb[k, j] += 2 * np.sum(np.abs(wgt * Q[k - j]))
            err[k] += np.sum(np.abs(wgt))
    cj = {}
    for k in range(1, kmax + 1):
        sc = (k + 1) * L0 - log(d)       # log of common factor
        cj[k] = (np.array([0.0] + [-(acc[k, j].real) / factorial(j) for j in range(1, k + 1)]), sc,
                 np.array([0.0] + [accb[k, j] / factorial(j) for j in range(1, k + 1)]))
    return cj, L0

def S_val(cj, k, K):
    v, sc, vb = cj[k]
    p = sum(v[j] * float(K) ** j for j in range(1, len(v)))
    mag = sum(vb[j] * float(K) ** j for j in range(1, len(v)))   # sum of |summands|: float error ~ 1e-16 * mag
    return p, sc, mag      # true value = p * exp(sc);  mag = scale for cancellation check

def first_neg(cj, d, K, kmax, rel=1e-11):
    T = (K * d) // phi(d)
    out = []
    for k in range(1, min(kmax, T - 1) + 1):
        p, sc, mag = S_val(cj, k, K)
        sg = 0 if abs(p) <= rel * mag else (1 if p > 0 else -1)
        out.append(sg)
        if sg < 0: return k, out
    return None, out

if __name__ == '__main__':
    d, kmax = int(sys.argv[1]), int(sys.argv[2])
    Ks = [int(x) for x in sys.argv[3:]]
    cj, L0 = kpoly(d, kmax)
    for K in Ks:
        print('K', K, 'T-1', (K * d) // phi(d) - 1, 'first neg level, signs:', first_neg(cj, d, K, kmax))
        for k in range(1, min(kmax, (K * d) // phi(d) - 1) + 1):
            p, sc, mag = S_val(cj, k, K)
            print('   k=%d  S=%.4e  (cancel ratio %.1e)' % (k, p * exp(sc) if abs(sc) < 700 else float('nan'), abs(p) / mag if mag else 0))
