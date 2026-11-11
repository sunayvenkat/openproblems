# check Lemma X: for k <= kex(d) ((k+1)phi > (k-1)d + 1), S_k(K) = [x^{phi-1}]D_k is C(K,k) * const
# (float K-polynomial from resid.kpoly; ratio S_k(K)/C(K,k) printed for several K; constant <=> lemma)
from math import comb
from resid import kpoly, S_val
from band import kex
for d in (455, 6545, 319865, 629629):
    cj, _ = kpoly(d, 6)
    for k in range(2, 7):
        r = [S_val(cj, k, K)[0] / comb(K, k) for K in (7, 11, 31, 101)]
        print(d, 'kex', kex(d), 'k', k, 'S_k/C(K,k) rel spread %.1e' % ((max(r) - min(r)) / max(abs(x) for x in r)))
