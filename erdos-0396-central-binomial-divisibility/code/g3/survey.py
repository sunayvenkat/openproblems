# Large-K first negative level kstar = (first n >= 3 with a_n > 0) - 1, from the trace a_n = Tr(zeta (H/2)^n),
# for 3-free squarefree band pieces d (1/2 < phi/d <= 2/3) built from primes 5..47, by omega(d).
# Sign accepted only if |a_n| > 1e-9 * sum |zeta (H/2)^n|.
import sys, random, numpy as np
from itertools import combinations
from multiprocessing import Pool
from tr import data, phi
PR = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def kstar(d, nmax=60):
    a, z, logH, h1 = data(d)
    L0 = logH.real.max()
    for n in range(3, nmax + 1):
        w = z * np.exp(n * (logH - L0)); v = w.sum().real; s = np.abs(w).sum()
        if v > 1e-9 * s: return d, n - 1, float(np.abs(h1.imag).max() / d)
    return d, None, float(np.abs(h1.imag).max() / d)
if __name__ == '__main__':
    random.seed(1); DMAX = int(sys.argv[1]); per = int(sys.argv[2])
    jobs = []
    for om in range(3, 8):
        c = [int(np.prod(t)) for t in combinations(PR, om)]
        c = [d for d in c if d <= DMAX and 0.5 < phi(d) / d <= 2 / 3]
        random.shuffle(c); jobs += [(om, d) for d in c[:per]]
    res = {}
    with Pool(9) as P:
        for (om, d), r in zip(jobs, P.map(kstar, [d for _, d in jobs])):
            res.setdefault(om, []).append(r)
    for om, rs in sorted(res.items()):
        ks = [99 if k is None else k for _, k, _ in rs]
        print('omega=%d n=%d kstar hist %s  frac>=5 %.2f  max %s  max tau %.2f' % (om, len(rs),
              sorted({k: ks.count(k) for k in ks}.items()), sum(k >= 5 for k in ks) / len(ks), max(ks), max(t for *_, t in rs)))
        print('    worst:', sorted(rs, key=lambda r: -(99 if r[1] is None else r[1]))[:4])
