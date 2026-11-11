# For each piece Phi_{2d}(x) of x^m+1: best cofactor exponent nu0/(s+1) over levels s whose first Laurent coeff is negative.
# Lemma X (REPORT.md): a prime q || f(x) with cofactor c=f(x)/q < (x^nu0/(2 j'|a|))^(1/(s+1)) is automatically good.
import sys; sys.path.insert(0, '..')
from lemC import divisors, phi, series_pow_cyclo
def levels(m, d):
    delta = phi(2*d); out = []
    for s in range(1, m//delta):
        E = m - (s+1)*delta; N = m + 2*delta + 5
        c = series_pow_cyclo(2*d, -(s+1), N)
        for t in range(E+1, N+1):
            v = c[t] + (c[t-m] if t >= m else 0)
            if v:
                out.append((s, t-E, v)); break
    return out
for m in map(int, sys.argv[1:]):
    print('m', m)
    for d in divisors(m):
        L = levels(m, d); good = [(nu/(s+1), s, nu, a) for s, nu, a in L if a < 0]
        best = max(good) if good else None
        print(f'  d={d:4d} deg={phi(2*d):3d} best(nu0/(s+1), s, nu0, coeff)={best}')
