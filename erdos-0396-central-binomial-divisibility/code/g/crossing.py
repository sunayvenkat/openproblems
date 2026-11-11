# Crossing-prime lemma check.  M odd squarefree with M/phi(M) < 2, q prime, m = M*q with T(m) = 2.
# Claim: rho = m - 2 phi(m) = 2 phi(M) - q*delta (delta = 2 phi(M) - M), and the top-piece level-1
# coefficients satisfy  c_N = [t^N] Phi_{2m}(t)^{-2} = [t^N] Phi_{2M}(t)^2 * Psi_{2M}-part ...; in
# particular for N < q:  c_N = [t^N] Phi_{2M}(t)^2.   We compare the direct series with the formula
#   c_N = (-1)^N [y^N] Phi_M(y)^2 Psi_M(y^q)^2     (y = -t), valid for N < m.
from math import gcd
from sympy import primerange, factorint

def mobius(n):
    f = factorint(n)
    return 0 if any(e > 1 for e in f.values()) else (-1) ** len(f)

def phi(n):
    r = n
    for p in factorint(n): r = r // p * (p - 1)
    return r

def series_prod(n, k, N, sign_t=False):
    # coefficients of prod_{e|n} (1 - y^e)^{k*mu(n/e)} mod y^{N+1}  (= Phi_n(y)^k for n>1)
    c = [0] * (N + 1); c[0] = 1
    for e in [d for d in range(1, n + 1) if n % d == 0]:
        ex = k * mobius(n // e)
        for _ in range(abs(ex)):
            if ex > 0:   # multiply by (1 - y^e)
                for i in range(N, e - 1, -1): c[i] -= c[i - e]
            else:        # divide by (1 - y^e)
                for i in range(e, N + 1): c[i] += c[i - e]
    return c

def direct(m, N):     # [t^N] Phi_{2m}(t)^{-2} for t-series, via Phi_{2m}(t) = Phi_m(-t)
    c = series_prod(m, -2, N)
    return [(-1) ** i * v for i, v in enumerate(c)]

def formula(M, q, N): # (-1)^N [y^N] Phi_M(y)^2 Psi_M(y^q)^2,  Psi_M(z) = (z^M - 1)/Phi_M(z)
    a = series_prod(M, 2, N)                      # Phi_M(y)^2
    psi2 = series_prod(M, -2, N // q + 1)         # Phi_M(z)^{-2}; Psi_M^2 = (1-z^M)^2 Phi_M^{-2}
    for _ in range(2):
        for i in range(len(psi2) - 1, M - 1, -1): psi2[i] -= psi2[i - M]
    out = []
    for n in range(N + 1):
        s = sum(psi2[j] * a[n - j * q] for j in range(n // q + 1) if n - j * q < len(a))
        out.append((-1) ** n * s)
    return out

for M in (15, 21, 33, 35, 39, 255, 3 * 5 * 7 * 11 // 7 * 1) if __name__ == '__main__' else ():  # small cores
    F = phi(M)
    if M >= 2 * F: continue
    dl = 2 * F - M
    for q in primerange(3, 2 * F // dl + 1):
        if M % q == 0: continue
        m = M * q; fm = phi(m)
        if not (2 * fm <= m < 3 * fm): continue
        rho = m - 2 * fm; assert rho == 2 * F - q * dl
        N = min(m - fm, rho + 60)
        d, f = direct(m, N), formula(M, q, N)
        assert d == f, (M, q)
        first = next((i for i in range(rho + 1, N + 1) if d[i]), None)
        cross = 2 * F / (dl + 1) < q
        print(f'M={M} q={q} m={m} rho={rho} crossing={cross} first N={first} c={d[first] if first else None}'
              + (f'  Phi_2M^2 coeff={f[first]}' if cross else ''))
