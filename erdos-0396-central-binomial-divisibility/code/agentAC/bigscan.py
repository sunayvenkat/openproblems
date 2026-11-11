# Parallel scan: odd squarefree m in [lo, hi] with phi(m)/m < 1/2. Top piece level data, then full goodness.
import sys
from multiprocessing import Pool
from core import factor, phi, mu
from fullgood import piece_good, full_good

def cands(lo, hi):
    for m in range(lo | 1, hi + 1, 2):
        f = factor(m)
        if all(e == 1 for e in f.values()) and 2 * phi(m) < m: yield m

def work(m):
    s, pat = piece_good(m, m)
    ps = sorted(factor(m))
    if s is None: return (m, ps, mu(m), m - (m // phi(m)) * phi(m), 'topBAD', pat, None)
    return (m, ps, mu(m), m - (m // phi(m)) * phi(m), 'topgood', s, full_good(m))

if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    with Pool(15) as pool:
        for r in pool.imap(work, cands(lo, hi), chunksize=4):
            print(*r, flush=True)
