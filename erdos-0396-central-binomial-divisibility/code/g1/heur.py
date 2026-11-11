# Heuristic count of P-rough squarefree odd m with T=2 and 0 < rho = m - 2 phi(m) <= X.
# Random squarefree model: prime p > P divides m with prob 1/(p+1), independently.
# E(Y) ~ 2 c_P f_r(2) X ln Y,  c_P = density of P-rough squarefree integers, f_r = density of r = m/phi(m) at 2.
#   python heur.py   -> heur_out.txt
import numpy as np
from math import log, pi
from sympy import primerange

def density_at_2(P, B=200000, h=2e-6):
    L = log(2.0) + 0.05
    nb = int(L / h) + 1
    dist = np.zeros(nb); dist[0] = 1.0
    for p in primerange(P + 1, B):
        w = 1.0 / (p + 1); s = int(round(log(p / (p - 1)) / h))
        if s == 0: break
        new = dist * (1 - w)
        new[s:] += dist[:-s] * w
        dist = new
    # density of log r at log 2 (average over +-0.01 to smooth the lattice), then f_r(2) = f_log / 2
    i0, k = int(log(2.0) / h), int(0.01 / h)
    f_log = dist[i0 - k:i0 + k].sum() / (2 * k * h)
    tail = dist[i0:].sum()           # P(r >= 2) (truncated at log2+0.05)
    return f_log / 2, tail

if __name__ == '__main__':
    for P in (3, 5, 7, 11, 13):
        f, tail = density_at_2(P)
        cP = 6 / pi ** 2
        for p in primerange(2, P + 1): cP *= p / (p + 1)
        A = 2 * cP * f
        print(f'P={P}: f_r(2)={f:.3e}  P(2<=r<2.05)={tail:.3e}  c_P={cP:.3f}  E(Y) ~ {A:.3e} * X * lnY')
        for X in (P + 2, 2 * P + 4, 10 ** 6):
            print(f'    X={X:>7}: ln Y needed for E=1: {1 / (A * X):.3e}  (decimal digits {1 / (A * X) / log(10):.3e})')
