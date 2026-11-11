"""Lemma A scan (non-top pieces d<m) with fastgood: python lemmaA_fast.py MMIN MMAX  (odd m)"""
import sys
import fastgood as F
lo, hi = map(int, sys.argv[1:3]); bad = []
for m in range(lo | 1, hi + 1, 2):
    for d in range(1, m):
        if m % d == 0 and F.good(m, d) is None:
            bad.append((m, d, m // d)); print("BAD non-top piece: m=%d d=%d m/d=%d primes(m)=%s" % (m, d, m // d, F.pf(m)), flush=True)
print("done", lo, hi, "count", len(bad))
