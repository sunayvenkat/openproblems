"""Task 3: stress-test family '+' (toy exponents, size condition ignored).
(b) every prime piece q = Phi_{2d}(A): actual carry levels of n in base q vs Laurent-sign prediction.
(a)/(c) when all pieces are < CAP, full factorisation + verifier + anomaly census."""
import sys
from math import gcd, isqrt
from collections import Counter, defaultdict
from famplus import family, pieces, predicted_levels, actual_levels, is_prime, factor, vp, carries
from verify396 import verify

CAP = 10**22


def run(k, ms, Bs, label):
    M0, L, c, e = family(k, ms)
    print(f"\n=== k={k} m={ms} {label}: n = {M0}*B^{L} + {k+1}, e_p={e}, c={c}")
    stat = defaultdict(lambda: [0, 0, 0, None])   # (j',d) -> [#prime pieces, #mismatch, #good-status flips, last bad A]
    anomalies = Counter(); members = []; nfact = 0
    for B in Bs:
        n = M0 * B ** L + k + 1
        P = pieces(k, ms, c, L, B)
        for i, (j, A, pcs) in enumerate(P):
            assert j * (A ** ms[j - 1] + 1) == n - i
            m = ms[j - 1]
            for d, q in pcs:
                if q > 2 * k + 1 and is_prime(q):
                    pr, ac = predicted_levels(m, d), actual_levels(n, q)
                    st = stat[(j, d)]; st[0] += 1
                    if pr != ac:
                        st[1] += 1; st[3] = A
                        if bool(pr) != bool(ac): st[2] += 1
        if all(q < CAP for _, _, pcs in P for _, q in pcs):
            nfact += 1
            facs = []
            for i, (j, A, pcs) in enumerate(P):
                f = factor(j)
                for d, q in pcs:
                    for p, ex in factor(q).items(): f[p] = f.get(p, 0) + ex
                facs.append(f)
                # anomaly census
                for (d1, q1) in pcs:
                    for (d2, q2) in pcs:
                        if d1 < d2 and gcd(q1, q2) > 1: anomalies[f"pieces of n-{i} share prime(s) {sorted(factor(gcd(q1,q2)))}"] += 1
            ok, rows = verify(n, k, facs)
            for p, need, have in rows:
                if need > have:
                    if p <= k + 1: anomalies[f"small prime p={p}<=k+1 fails"] += 1
                    elif p <= 2 * k: anomalies[f"prime p={p} in (k+1,2k] fails"] += 1
                    elif need >= 2: anomalies["repeated prime q>2k (v>=2) fails"] += 1
                    elif p * p > 2 * n: anomalies["prime > sqrt(2n) (no carry possible)"] += 1
                    else: anomalies["prime <= sqrt(2n) with no carry"] += 1
            if ok: members.append(n)
    print(" (b) prime pieces: (j',d): #prime, #level-set mismatch, #good/bad flip, last A with mismatch")
    for key in sorted(stat):
        j, d = key; m = ms[j - 1]
        print(f"     j'={j} m={m} d={d:4d} pred={sorted(predicted_levels(m, d))}: {stat[key][:3]} lastA={stat[key][3]}")
    print(f" (a/c) fully factored n: {nfact}; failure causes (count over all failing primes): {dict(anomalies)}")
    print(f"       n in E_k: {members[:5]}{' ...' if len(members) > 5 else ''} ({len(members)})")
    return stat, members


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("k0", "all"):
        for m, X in [(3, 4000), (5, 1500), (9, 400), (15, 200), (105, 60), (165, 40), (195, 40)]:
            run(0, [m], range(1, X + 1), "(n = x^m+1, x = B)")
    if which in ("k1", "all"):
        for ms, X in [((3, 5), 120), ((5, 3), 80), ((3, 7), 60), ((7, 3), 60), ((5, 7), 25), ((7, 5), 25)]:
            run(1, list(ms), range(1, X + 1), "")
