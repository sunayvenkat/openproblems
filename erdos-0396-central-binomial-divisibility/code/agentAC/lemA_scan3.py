# Lemma A scan over squarefree odd d in [lo,hi] with omega(d)>=2, K in (3,5,7).
import sys
from multiprocessing import Pool
from core import phi, factor
from fullgood import piece_good
Ks = (3, 5, 7)
def work(d):
    return d, [(K,) + piece_good(K * d, d) for K in Ks]
def cand(lo, hi):
    for d in range(lo | 1, hi + 1, 2):
        f = factor(d)
        if len(f) >= 2 and all(e == 1 for e in f.values()): yield d
if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    nf = {K: 0 for K in Ks}; tot = 0
    with Pool(12) as pool:
        for d, res in pool.imap(work, cand(lo, hi), chunksize=8):
            tot += 1
            for K, s, pat in res:
                if s is None:
                    nf[K] += 1; print('FAIL d', d, sorted(factor(d)), 'phi/d=%.3f' % (phi(d)/d), 'K', K, pat, flush=True)
    print('squarefree d tested', tot, 'failures per K', nf)
