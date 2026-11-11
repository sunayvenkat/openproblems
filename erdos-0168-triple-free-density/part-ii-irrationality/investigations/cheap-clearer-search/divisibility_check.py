# Finite evidence for the non-degeneracy condition (ND) of notes.md section 8.
# K = nonresonant indices n with a_{n+1} >= 5 among the first ~590 convergents of log2/log3.
# For each prime l < LIM: does l divide D_n = 27(2^{3q_n}-1)(3^{3p_n}-1) for EVERY n in K (or a tail)?
import sys
from mpmath import mp, log, floor as mfloor
from sympy import primerange, n_order
sys.set_int_max_str_digits(0)
mp.dps = 1500
x = log(2) / log(3)
digs = []
for _ in range(700):
    a = int(mfloor(x)); digs.append(a); x = 1 / (x - a)
digs = digs[:592]                      # 600 digits are interval-certified in codex_review_check.py
assert digs[:16] == [0, 1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55]
P = [1, 0]; Q = [0, 1]; conv = []      # conv[n] = (p_n, q_n), n from 0
for a in digs:
    P.append(a * P[-1] + P[-2]); Q.append(a * Q[-1] + Q[-2]); conv.append((P[-1], Q[-1]))
K = [n for n in range(3, len(digs) - 1) if (conv[n][0] + conv[n][1]) % 3 and digs[n + 1] >= 5]
print("adequate nonresonant indices in prefix:", len(K), "first:", K[:12])
LIM = 20000
always = []; tail = []
half = K[len(K) // 2:]
for l in primerange(5, LIM):
    e2, e3 = n_order(2, l), n_order(3, l)
    div = lambda n: (3 * conv[n][1]) % e2 == 0 or (3 * conv[n][0]) % e3 == 0
    if all(div(n) for n in K): always.append(l)
    elif all(div(n) for n in half): tail.append(l)
print("primes 5<=l<%d dividing D_n for every n in K:" % LIM, always)
print("primes dividing D_n on the whole second half of K but not all of K:", tail)
# special primes: minimal valuations must occur
def v(n, l):
    k = 0
    while n % l == 0: n //= l; k += 1
    return k
podd = sum(conv[n][0] % 2 for n in K); qodd = sum(conv[n][1] % 2 for n in K)
v7 = [1 + v(conv[n][1], 7) + ((1 + v(conv[n][0], 7)) if conv[n][0] % 2 == 0 else 0) for n in K]
v13 = [1 + v(conv[n][0], 13) + ((1 + v(conv[n][1], 13)) if conv[n][1] % 4 == 0 else 0) for n in K]
print("p_n odd:", podd, " q_n odd:", qodd, " v7(D_n)<=2:", sum(t <= 2 for t in v7), " v13(D_n)<=2:", sum(t <= 2 for t in v13), "of", len(K))
# worst prime: largest fraction of K divisible
best = max(((sum(((3*conv[n][1]) % n_order(2,l) == 0 or (3*conv[n][0]) % n_order(3,l) == 0) for n in K), l) for l in primerange(5, 2000) if l not in (7, 13)))
print("most persistent other prime below 2000: l=%d divides D_n for %d of %d" % (best[1], best[0], len(K)))
