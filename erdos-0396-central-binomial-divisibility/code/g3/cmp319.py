# compare exact level coefficients of d=319865, K=187 (aur/lev319865.txt) with
#   P0 = -K^k a_{k+1}/(d k!)  and the shifted predictor P1 = -M_k(K)/(d k!)
import numpy as np
from math import lgamma, log, exp
from tr import data, phi
d, K = 319865, 187
exact = {2: 4.485e15, 3: 1.996e24, 4: 6.900e31, 5: 1.434e38, 6: 1.331e46, 7: 1.363e53, 8: 5.175e60, 9: 6.559e67,
         10: 4.891e73, 11: 3.527e81, 12: 2.231e88, 13: 1.330e95, 14: -1.520e102}
a, z, logH, h1 = data(d)
th = phi(d) / d
L0 = logH.real.max() - log(2)
for k in range(2, 15):
    w = z * np.exp((k + 1) * (logH - log(2) - L0))
    beta = 1 / d + (k + 1) * (-th / 2 + 1j * h1.imag / d)
    s0 = np.sum(w).real; s1 = np.sum(w * ((K + beta) / K) ** k).real
    lg = (k + 1) * L0 + k * log(K) - log(d) - lgamma(k + 1)
    p0, p1 = -s0 * exp(lg), -s1 * exp(lg)
    print(f'k={k:2d} exact={exact[k]: .3e}  P0={p0: .3e} ({p0/exact[k]:.3f})  P1={p1: .3e} ({p1/exact[k]:.3f})')
