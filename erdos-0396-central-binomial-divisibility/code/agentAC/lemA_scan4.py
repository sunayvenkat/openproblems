# Lemma A in the critical band 1/2 < phi(d)/d < 2/3 (where all observed failures live):
# squarefree odd d in [lo,hi], K in Ks. Also report, for each failure, the least odd K<=25 that works.
import sys
from multiprocessing import Pool
from core import phi, factor
from fullgood import piece_good
Ks = (5, 7, 9)
def work(d):
    out = []
    for K in Ks:
        s, pat = piece_good(K * d, d)
        if s is None:
            K2 = next((k for k in range(K + 2, 27, 2) if piece_good(k * d, d)[0]), None)
            out.append((K, pat, K2))
    return d, out
def cand(lo, hi):
    for d in range(lo | 1, hi + 1, 2):
        f = factor(d)
        if len(f) >= 3 and all(e == 1 for e in f.values()) and 0.5 < phi(d) / d < 2 / 3: yield d
if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2]); tot = 0; nf = {K: 0 for K in Ks}
    with Pool(14) as pool:
        for d, out in pool.imap(work, cand(lo, hi), chunksize=4):
            tot += 1
            for K, pat, K2 in out:
                nf[K] += 1
                print('FAIL d', d, sorted(factor(d)), 'phi/d=%.3f' % (phi(d) / d), 'K', K, pat, 'least working K', K2, flush=True)
    print('band d tested', tot, 'failures per K', nf)
