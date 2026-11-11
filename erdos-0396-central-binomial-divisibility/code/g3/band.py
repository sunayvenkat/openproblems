# For each non-top piece d of m with phi(d)/d <= 2/3 (the pieces A1(b) does not settle):
#   k_ex   : levels k with (k+1)phi(d) > (k-1)d+1 have [x^{phi-1}]D_k = -C(K,k) a_{k+1}/d exactly (any K)
#   kstar  : large-K first negative level (first k with a_{k+1} > 0)
#   first  : first negative level at the actual K = m/d (float residue method, resid.py)
#   badK   : odd K in [3, Kmax] with no negative level <= min(T_K - 1, kmax)  ('?' = T_K-1 > kmax, undecided)
#   Kroot  : largest odd K <= Kscan with S_{kstar}(K) >= 0  (so all larger K are good at level kstar)
import sys, numpy as np
from multiprocessing import Pool
from itertools import combinations
from resid import kpoly, first_neg, S_val, phi, pf

def divisors(m):
    ps = pf(m); out = []
    for r in range(len(ps) + 1):
        for c in combinations(ps, r):
            d = 1
            for p in c: d *= p
            out.append(d)
    return sorted(out)

def kex(d):
    dl = phi(d); return max(k for k in range(1, 60) if (k + 1) * dl > (k - 1) * d + 1)

def work(args):
    m, d, KMAX, KCAP = args
    th = phi(d) / d; K = m // d
    kmax = KCAP if d <= 2 * 10 ** 6 else min(10, (K * d) // phi(d) - 1)
    cj, L0 = kpoly(d, kmax)
    lead = [np.sign(cj[k][0][k]) if abs(cj[k][0][k]) > 1e-11 * cj[k][2][k] else 0 for k in range(1, kmax + 1)]
    kstar = next((k for k in range(1, kmax + 1) if lead[k - 1] < 0), None)
    first, sig = first_neg(cj, d, K, kmax)
    bad = []
    from math import gcd
    for KK in range(3, KMAX + 1, 2):
        if gcd(KK, d) > 1 or any(KK % (p * p) == 0 for p in range(3, 40, 2)): continue
        f, _ = first_neg(cj, d, KK, kmax)
        if f is None: bad.append(KK if (KK * d) // phi(d) - 1 <= kmax else -KK)
    kroot = None
    if kstar:
        for KK in range(3, 20001, 2):
            p, sc, mag = S_val(cj, kstar, KK)
            if p >= 0: kroot = KK
    return dict(d=d, K=K, th=th, kex=kex(d), kstar=kstar, first=first, sig=sig, bad=bad, kroot=kroot, kmax=kmax,
                lead=''.join('+' if x < 0 else ('-' if x > 0 else '0') for x in lead))  # lead: sign of a_{k+1}

if __name__ == '__main__':
    m = int(sys.argv[1]); KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 99
    KCAP = int(sys.argv[3]) if len(sys.argv) > 3 else 24
    DMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 8
    ds = [d for d in divisors(m) if 1 < d < m and phi(d) / d <= 2 / 3 and d <= DMAX]
    print('m =', m, pf(m), 'phi/m = %.4f' % (phi(m) / m), 'pieces to check:', len(ds), flush=True)
    with Pool(14) as P:
        for r in P.imap(work, [(m, d, KMAX, KCAP) for d in sorted(ds)]):
            print(f"d={r['d']} {pf(r['d'])} th={r['th']:.4f} K={r['K']} kex={r['kex']} a-signs(n=2..)={r['lead']} "
                  f"kstar={r['kstar']} first@K={r['first']} Kroot={r['kroot']} badK(<= {KMAX})={r['bad']}", flush=True)
