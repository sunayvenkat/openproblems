"""Segmented numpy brute force for a(k) = min n (n-k >= 2) with prod_{i<=k}(n-i) | C(2n,n), k <= KMAX.
Primes q > 2k are tested per N = n-i (Lemma 1, here re-checked independently by verify396);
primes p <= 2k are tested directly on n.  A prime factor q > sqrt(2N) is always bad (0 carries).
usage: python brute.py X [KMAX] [START]  (minima reported for n >= START only)"""
import sys, numpy as np
from math import isqrt

X = int(sys.argv[1]); KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 8
Q = isqrt(2 * X) + 1
sv = np.ones(Q + 1, bool); sv[:2] = False
for i in range(2, isqrt(Q) + 1):
    if sv[i]: sv[i * i::i] = False
PR = np.nonzero(sv)[0].tolist()
SP = [p for p in PR if p <= 2 * KMAX]
S = 1 << 23
from verify396 import verify
found = {}
counts = {k: 0 for k in range(KMAX + 1)}
trivial = {}                               # minima if n = k+1 (factor 1) is allowed
for n0 in range(1, KMAX + 2):              # tiny n done exactly, so segments start with base >= 2
    for k in range(min(KMAX, n0 - 1) + 1):
        if verify(n0, k)[0]:
            if n0 == k + 1: trivial.setdefault(k, n0); continue
            counts[k] += 1
            if k not in found: found[k] = n0; print(f"a({k}) = {n0}", flush=True)
print("n = k+1 works for k in", sorted(trivial))
lo = max(KMAX + 2, int(sys.argv[3]) if len(sys.argv) > 3 else 0)   # optional resume point
while lo <= X and len(found) <= KMAX:
    hi = min(X + 1, lo + S)
    base = lo - KMAX                       # N runs over [base, hi)
    N = np.arange(base, hi, dtype=np.int64)
    rem = N.copy(); mb = np.zeros(len(N), np.int64)   # mb = largest bad prime of N
    vsm = {}
    for q in PR:
        st = (-base) % q
        sub = N[st::q]
        t = sub // q; v = np.ones(len(sub), np.int64)
        m = t % q == 0
        while m.any():
            v[m] += 1; t[m] //= q; m = t % q == 0
        rem[st::q] //= sub // t
        if q <= 2 * KMAX:
            full = np.zeros(len(N), np.int64); full[st::q] = v; vsm[q] = full
        c = np.zeros(len(sub), np.int64); pt = q
        while pt <= 2 * hi:
            c += 2 * (sub % pt) >= pt; pt *= q
        seg = mb[st::q]; mb[st::q] = np.where(c < v, q, seg)
    mb = np.where(rem > 1, rem, mb)
    n = N[KMAX:]                           # n in [lo, hi)
    carr = {}
    for p in SP:
        c = np.zeros(len(n), np.int64); pt = p
        while pt <= 2 * hi:
            c += 2 * (n % pt) >= pt; pt *= p
        carr[p] = c
    for k in range(KMAX + 1):
        ok = n - k >= 2
        for i in range(k + 1):
            ok &= mb[KMAX - i: len(N) - i] <= 2 * k
        for p in SP:
            if p > 2 * k: break
            need = sum(vsm[p][KMAX - i: len(N) - i] for i in range(k + 1))
            ok &= need <= carr[p]
        idx = np.nonzero(ok)[0]
        counts[k] += len(idx)
        if len(idx) and k not in found:
            found[k] = int(n[idx[0]]); print(f"a({k}) = {found[k]}", flush=True)
    lo = hi
print("searched to", hi - 1, "found", found)
print("counts of E_k (n<=%d):" % (hi - 1), counts)
