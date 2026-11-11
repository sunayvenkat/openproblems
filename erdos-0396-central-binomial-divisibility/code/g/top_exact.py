# Exact top-piece check (T = 2) plus the reflection identity
#   [t^(rho+1)] Phi_2m(t)^-2 = [t^(m-1)] Phi_2m(t)^-2 = -a_2(m)/m,   rho = m - 2 phi(m),
# which follows from Psi_m^2 being reciprocal of degree 2(m - phi(m)).
from crossing import series_prod, phi

def coeffs(m, N):  # [t^i] Phi_2m(t)^-2, i <= N < m, exact integers
    c = series_prod(m, -2, N)
    return [(-1) ** i * v for i, v in enumerate(c)]

for m in () if __name__ != '__main__' else (105, 165, 195, 1155, 1365, 2145):
    f = phi(m); assert 2 * f <= m < 3 * f
    rho = m - 2 * f; c = coeffs(m, m - 1)
    assert c[rho + 1] == c[m - 1], m
    print(m, 'rho', rho, 'c[rho+1] = c[m-1] =', c[rho + 1])

if __name__ == '__main__':
    m = 59814755; f = phi(m); rho = m - 2 * f
    c = coeffs(m, rho + 1)
    print('m2 top: rho', rho, 'offset-0 coefficient', c[rho + 1])
