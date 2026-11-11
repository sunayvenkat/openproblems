# Lemma A scan (fast): odd d <= dmax (d>1), K in Ks; is piece Phi_{2d} of x^{Kd}+1 good? Print failures
# and, for each failing d, the smallest odd K that works.
import sys
from multiprocessing import Pool
from core import phi, factor
from fullgood import piece_good

Ks = (3, 5, 7, 9, 11, 13)
def work(d):
    res = []
    for K in Ks:
        s, pat = piece_good(K * d, d)
        res.append((K, s, pat))
    return d, res

if __name__ == '__main__':
    dmax = int(sys.argv[1])
    nfail = {K: 0 for K in Ks}; tot = 0
    with Pool(15) as pool:
        for d, res in pool.imap(work, range(3, dmax + 1, 2), chunksize=8):
            tot += 1
            fails = [(K, pat) for K, s, pat in res if s is None]
            for K, _ in fails: nfail[K] += 1
            if fails:
                print('d', d, sorted(factor(d).items()), 'phi/d=%.3f' % (phi(d) / d), 'fails', fails,
                      'levels:', [(K, s) for K, s, _ in res], flush=True)
    print('d tested', tot, 'failures per K', nfail)
