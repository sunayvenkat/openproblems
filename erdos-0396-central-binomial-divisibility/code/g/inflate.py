# (1) Trace formula check: [t^(m-1)] Phi_2m(t)^-2 vs -a_2/m, a_2 = sum_zeta zeta (H(zeta)/2)^2,
#     H(zeta) = 2m/(zeta f'(zeta)), f'(zeta) = prod_{eta != zeta} (zeta - eta) over primitive 2m-th roots.
# (2) Inflation: for T = 2 and prime q > 2 phi(M), the decisive top coefficient of Mq equals that of M.
import mpmath as mp
from math import gcd
from sympy import nextprime
from top_exact import coeffs, phi
mp.mp.dps = 40

def a2_pred(m):
    z = [mp.exp(1j * mp.pi * a / m) for a in range(1, 2 * m, 2) if gcd(a, m) == 1]
    s = 0
    for w in z:
        fp = mp.fprod([w - e for e in z if e != w])
        s += w * (m / (w * fp)) ** 2
    return -s / m

def decisive(m):  # first nonzero [t^N] Phi_2m^-2 with N > rho (T = 2), and its offset
    f = phi(m); rho = m - 2 * f; c = coeffs(m, m - 1)
    N = next(i for i in range(rho + 1, m) if c[i])
    return c[N], N - rho - 1

for M in (105, 165, 195, 1155):
    print(M, 'c[m-1]', coeffs(M, M - 1)[M - 1], '-a2/m', mp.nstr(a2_pred(M), 12))
for M in (105, 165, 195, 1365):
    q = nextprime(2 * phi(M))
    for _ in range(2):
        if M % q:
            m = M * q
            if m // phi(m) == 2:
                print(M, q, 'decisive(Mq)', decisive(m), 'decisive(M)', decisive(M))
        q = nextprime(q)
