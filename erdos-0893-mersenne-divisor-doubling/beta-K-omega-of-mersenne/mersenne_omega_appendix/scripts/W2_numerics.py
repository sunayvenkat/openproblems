"""W2 numerics: how far is M_p from the extremal (dense) configuration?
(1) For primes p <= PMAX: all primes q <= p^2 with q | M_p (exhaustive over q = 2pk+1, k <= p/2).
(2) Second-order trivial bound B(p) (Montgomery-Vaughan BT) vs naive bound vs (log2/2)p/log p.
"""
import math, sys

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

def is_prime(n):  # deterministic MR for n < 3.3e24
    if n < 2: return False
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
        if n % a == 0: return n == a
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

def small_factors(p, kmax):
    out = []
    for k in range(1, kmax + 1):
        q = 2 * p * k + 1
        if q % 8 not in (1, 7): continue
        if pow(2, p, q) == 1 and is_prime(q): out.append(q)
    return out

def bound_naive(p):
    # q_j >= 4p(j-1)+1 (two classes mod 8p), j>=2 ; q_1 >= 2p+1
    s, k = math.log(2 * p + 1), 1
    while True:
        t = math.log(4 * p * k + 1)
        if s + t >= p * math.log(2): return k
        s += t; k += 1

def bound_BT(p):
    # q_j >= max(4p(j-1)+1, j(p-1)log((j-1)/2)) for j>=8 (MV Brun-Titchmarsh), q_j>=4p(j-1)+1 otherwise
    s, k = 0.0, 0
    L = p * math.log(2)
    while True:
        j = k + 1
        lb = 2 * p + 1 if j == 1 else 4 * p * (j - 1) + 1
        if j >= 8: lb = max(lb, j * (p - 1) * math.log((j - 1) / 2))
        t = math.log(lb)
        if s + t >= L: return k
        s += t; k += 1

if __name__ == "__main__":
    PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    tot, worst = 0, (0, 0)
    rows = []
    for p in primes_upto(PMAX):
        if p < 3: continue
        f = small_factors(p, p // 2)
        tot += len(f)
        ext = math.log(2) / 2 * p / math.log(p)
        if len(f) > worst[0]: worst = (len(f), p)
        rows.append((p, len(f), ext))
    print("p<=%d: max #{q<=p^2, q|M_p} = %d at p=%d; mean = %.3f" % (PMAX, worst[0], worst[1], tot / len(rows)))
    print("largest ratio count/((log2/2)p/log p):", max(r[1] / r[2] for r in rows))
    for p, c, e in rows[-5:]:
        print("p=%d  count(q<=p^2)=%d  extremal ~%.1f" % (p, c, e))
    print("\nsecond-order bounds  p, naive, BT, (log2/2)p/log p, (log2/2)p/(log p-1.03)")
    for p in (10**3 + 9, 10**4 + 7, 10**5 + 3, 10**6 + 3, 10**7 + 19):
        print(p, bound_naive(p), bound_BT(p), round(math.log(2) / 2 * p / math.log(p), 1),
              round(math.log(2) / 2 * p / (math.log(p) - 1.0298), 1))
