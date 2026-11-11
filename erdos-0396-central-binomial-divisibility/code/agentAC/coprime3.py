# Top-piece level-1 check for odd squarefree m coprime to 3 (all primes >= 5) with phi(m)/m < 1/2,
# T = 2 and rho0 = m - 2 phi(m) small enough to compute (the window starts at rho0+1).
import sys
from multiprocessing import Pool
from sympy import primerange
from core import phi, mu
from topscan import top_levels
P = list(primerange(5, 80)); Mmax = int(float(sys.argv[1])); Rmax = int(float(sys.argv[2]))
def gen():
    out = []
    def rec(i, m, ph, ps):
        if 2 * ph < m and m - 2 * ph <= Rmax and 3 * ph > m: out.append((m, tuple(ps)))
        for j in range(i, len(P)):
            p = P[j]
            if m * p > Mmax: break
            rec(j + 1, m * p, ph * (p - 1), ps + [p])
    rec(0, 1, 1, [])
    return sorted(out)
def work(c):
    m, ps = c
    T, lv = top_levels(m)
    return m, ps, mu(m), m - 2 * phi(m), lv
if __name__ == '__main__':
    cs = gen(); print('candidates', len(cs), flush=True)
    with Pool(14) as pool:
        for m, ps, u, r, lv in pool.imap(work, cs):
            g = any(x and x[1] < 0 for _, x in lv)
            print(m, list(ps), 'mu', u, 'rho0', r, 'top', 'good' if g else 'BAD', lv, flush=True)
