# Check: for T=2, level-1 first window coefficient c_{E+i} = (-1)^{i+1} A_i / m with
# A_i = -sum_{k in (Z/m)^*} |Psi_m(e^{2 pi i k/m})|^2 cos(2 pi k (i - phi)/m).
import numpy as np
from math import gcd
from core import phi
from fastser import cyclo_pow_series_fast
def Psi_abs2(m):
    # |Psi_m(z)|^2 = m^2 / |Phi_m'(z)|^2 at primitive roots z; use Psi_m(z) = prod over non-primitive m-th roots (z - eta)
    ks = [k for k in range(1, m) if gcd(k, m) == 1]
    eta = np.exp(2j * np.pi * np.array([k for k in range(m) if gcd(k, m) != 1]) / m)
    z = np.exp(2j * np.pi * np.array(ks) / m)
    W = np.array([np.exp(np.sum(2 * np.log(np.abs(zz - eta)))) for zz in z])  # log-sum avoids overflow
    return np.array(ks), W
for m in (105, 165, 195, 1155, 1365, 3003):
    ph = phi(m); E = m - 2 * ph
    e = cyclo_pow_series_fast(m, -2, E + 6)
    ks, W = Psi_abs2(m)
    for i in (1, 2, 3):
        N = E + i; c = e[N] if N % 2 == 0 else -e[N]
        A = -np.sum(W * np.cos(2 * np.pi * ks * (i - ph) / m))
        pred = (-1) ** (i + 1) * A / m
        assert abs(pred - c) < 1e-6 * max(1, abs(c)), (m, i, c, pred)
    print(m, 'ok: c_{E+1..3} =', [e[E + i] if (E + i) % 2 == 0 else -e[E + i] for i in (1, 2, 3)])
