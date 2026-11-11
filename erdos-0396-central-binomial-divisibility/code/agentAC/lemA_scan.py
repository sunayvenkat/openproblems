# Lemma A scan: for odd d and odd K>=3, m = K*d, is piece Phi_{2d} of x^m+1 good?
# Prints, per (d,K), the first level s with a negative leading coefficient, and the sign pattern.
import sys
from collections import Counter
from core import *

def first_good_level(m, d):
    delta = phi(d); T = m // delta
    pat = []
    for s in range(1, T):
        r = level_sign(m, d, s)
        pat.append(0 if r is None else r[1])
        if r and r[1] < 0: return s, pat
    return None, pat

if __name__ == '__main__':
    dmax = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    Ks = [3, 5, 7, 9, 11, 15, 21]
    ds = [d for d in range(1, dmax + 1, 2)]
    # also force some d with many prime factors
    ds += [1155, 1365, 1785, 2145, 3003, 3315, 5005, 15015]
    stats = Counter(); bad = []
    for d in ds:
        for K in Ks:
            m = K * d
            if m > 50000: continue
            s, pat = first_good_level(m, d)
            stats[s] += 1
            if s is None or s > 2:
                print('d', d, 'K', K, 'phi(d)/d=%.3f' % (phi(d) / d), 'first neg level', s, 'pattern', pat, flush=True)
            if s is None: bad.append((d, K))
    print('first-negative-level histogram:', dict(stats))
    print('BAD (d,K):', bad)
