# Shared helpers for g2 (top piece of x^m+1, m odd squarefree).
# Q_k(y) = prod_{e|m,e<m} (1-y^e)^(-k mu(m/e)) = (-Psi_m(y))^k,  Psi_m = (y^m-1)/Phi_m.
# Level s (k=s+1) decisive coefficient a_s = c_{E_s+1} = [y^{m+1-k phi}] Q_k  (y=-t, index even).
import sys, numpy as np
sys.path.insert(0, '../agentV'); sys.path.insert(0, '..')
from fastgood import pf, phi, sqfree_divs, series, first_sign


def Qk_series(m, k, N):
    "[y^0..N] of Q_k = Phi_m(y)^(-k) mod y^m (exact ints); N < m"
    assert N < m
    return series(m, -k, N)


def psi_coeffs(m):
    "exact coefficients of Psi_m = prod_{e|m,e<m} (y^e-1)^(-mu(m/e)) (numpy object)"
    D = m - phi(m)
    c = np.zeros(D + 1, dtype=object); c[:] = 0; c[0] = 1
    sgn = 1
    for e, mu in sorted(sqfree_divs(m)):
        if e == m: continue
        k = -mu                      # exponent of (1 - y^e)
        if k > 0:
            c[e:] = c[e:] - c[:-e].copy()
        else:                        # (1-y^e)^{-1}: cumulative along residues (exact since result is a polynomial)
            L = -(-(D + 1) // e) * e
            b = np.zeros(L, dtype=object); b[:] = 0; b[:D + 1] = c
            c = b.reshape(-1, e).cumsum(axis=0).reshape(-1)[:D + 1]
        sgn *= (-1) ** abs(k)        # (y^e-1) = -(1-y^e)
    return sgn * c


def logQ(m, logr, turns):
    "complex log Q_1(y) = -sum_{e|m,e<m} mu(m/e) log(1-y^e), y = exp(logr) e^{2 pi i turns} (arrays)"
    out = np.zeros(np.broadcast(logr, turns).shape, dtype=complex)
    for e, mu in sqfree_divs(m):
        if e == m: continue
        ye = np.exp(e * logr + 2j * np.pi * np.mod(e * turns, 1.0))
        out -= mu * np.log(1 - ye)
    return out


def log_abs_psi_at_roots(m, a):
    "log|Psi_m(zeta_m^a)| = -sum_{d|m,d>1} mu(d) log|2 sin(pi a/d)|  (a int array)"
    out = np.zeros(len(a))
    for e, mu in sqfree_divs(m):          # e = m/d, mu = mu(d)
        if e == m: continue
        d = m // e
        out -= mu * np.log(np.abs(2 * np.sin(np.pi * (a % d) / d)))
    return out
