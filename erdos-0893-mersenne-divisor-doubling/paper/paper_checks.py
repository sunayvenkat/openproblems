"""Reproduce every number in Section "Numerical data" of mersenne_doubling_paper.tex.

Usage: python paper_checks.py        (needs sympy; downloads OEIS b-files into ./oeis_cache)
"""
import math, os, urllib.request
from collections import Counter
from sympy import isprime, factorint, primerange, divisor_count

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "oeis_cache")


def bfile(num):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"b{num}.txt")
    if not os.path.exists(path):
        req = urllib.request.Request(f"https://oeis.org/A{num}/b{num}.txt", headers={"User-Agent": "paper-checks/1.0"})  # OEIS rejects urllib's default UA
        with urllib.request.urlopen(req, timeout=60) as resp, open(path, "wb") as out:
            out.write(resp.read())
    out = {}
    for line in open(path):
        s = line.split()
        if len(s) == 2 and s[0].isdigit():
            out[int(s[0])] = int(s[1])
    return out


T, W, Om, Tp = bfile("046801"), bfile("085021"), bfile("046800"), bfile("046798")  # tau(2^n-1), omega(Phi_n(2)), omega(2^n-1), tau(2^n+1)
N = max(T)
f = [0] * (N + 1)
for k in range(1, N + 1):
    f[k] = f[k - 1] + T[k]
r = lambda n: f[2 * n] / f[n]
H = N // 2

print("T(1..30):", [T[k] for k in range(1, 31)])
print("ratios n<=15:", [round(r(n), 3) for n in range(1, 16)])
assert all(f[2 * n] >= 3 * f[n] for n in range(1, H + 1))
print("equality f(2n)=3f(n), n<=%d:" % H, [n for n in range(1, H + 1) if f[2 * n] == 3 * f[n]])
print("min ratio 32<=n<=%d: %.3f; min 150<=n<=300: %.1f" % (H, min(r(n) for n in range(32, H + 1)), min(r(n) for n in range(150, 301))))
print("ratios at 8,16,32,64,128:", [round(r(n), 3) for n in (8, 16, 32, 64, 128)], " argmin 16..150:", min(range(16, 151), key=r))
rec, best = [], 0
for k in range(1, 601):
    if T[k] > best:
        best, rec = T[k], rec + [k]
print("T records k<=600:", rec)
mx = max(W[d] for d in range(2, 600))
print("max omega(Phi_d(2)), d<600:", mx, "at", [d for d in range(2, 600) if W[d] == mx], " omega(M_431) =", Om[431])

fac = [2383, 6353, 50023, 53993, 202471, 5877983, 814132872808522587940886856743,
       1234904213576000272542841146073, 6597485910270326519900042655193]
assert math.prod(fac) == 2**397 - 1 and all(isprime(q) and q % 794 == 1 for q in fac)
print("M_397 factorization verified (9 BPSW primes, all 1 mod 794)")

P4 = [p for p in primerange(5, max(Tp) + 1) if Tp[p] == 4]
assert all(Tp[p] % 4 == 0 for p in primerange(5, max(Tp) + 1))
print("P4:", P4, "\nomega(M_p) on P4:", [Om[p] for p in P4], " max on P8:", max((Om[p], p) for p in primerange(5, max(Tp) + 1) if Tp[p] <= 8))

print("gcd examples:", math.gcd(2 + 2**30 - 2**11 - 2**12, 2**43 - 1), math.gcd(2 + 2**87 - 2**4 - 2**26, 2**223 - 1))
print("omega(Phi_13(2^12)) =", len(factorint(sum(2**(12 * i) for i in range(13)))), " tau(12) =", divisor_count(12))

# D(2^J) and J(C), C = 4, 16, 10^4
M = 2**21
tau = [0] * (M + 1)
for d in range(1, M + 1):
    for m in range(d, M + 1, d):
        tau[m] += 1
D, best = [0] * (M + 1), 0
for m in range(1, M + 1):
    best = max(best, tau[m])
    D[m] = best
J = lambda C: next(j for j in range(1, 22) if D[2**j] - 2 > j * math.log2(C))
print("D(2^J), J=7,8,12,13,20,21:", [D[2**j] for j in (7, 8, 12, 13, 20, 21)], " J(4),J(16),J(1e4):", J(4), J(16), J(10**4))

# prime factors q <= p^2 of M_p versus Gillies' Poisson model
ps = list(primerange(3, 6001))
c = [sum(1 for k in range(1, (p * p - 1) // (2 * p) + 1) if pow(2, p, 2 * p * k + 1) == 1 and isprime(2 * p * k + 1)) for p in ps]
mu = [math.log(2 * math.log(p) / math.log(2 * p + 1)) for p in ps]
print("c_p histogram:", sorted(Counter(c).items()), " max:", max(zip(c, ps)), " mean: %.2f" % (sum(c) / len(c)))
print("Gillies mixture prediction k=0..4:", [round(sum(math.exp(-u) * u**k / math.factorial(k) for u in mu), 1) for k in range(5)])
