# Audit of notes.md Section 8 (Lemmas 8.1-8.3). Exact integer arithmetic.
import sys, pickle
from math import gcd
from sympy import primerange, n_order, factorint
sys.set_int_max_str_digits(0)
def v(n, l):
    k = 0
    while n % l == 0: n //= l; k += 1
    return k
bad = 0; tests = 0
# (a) valuation formulas and the prime criterion, all coprime (p,q) with 1<=p,q<=120
primes = [l for l in primerange(5, 400) if l not in (7, 13)]
ords = {l: (n_order(2, l), n_order(3, l)) for l in primes}
for p in range(1, 121):
    for q in range(1, 121):
        if gcd(p, q) != 1: continue
        X, Y = 2 ** (3 * q) - 1, 3 ** (3 * p) - 1
        D = 27 * X * Y
        tests += 1
        if p % 2 and v(D, 2) != 1: bad += 1
        if q % 2 and v(D, 3) != 3: bad += 1
        if v(D, 7) != 1 + v(q, 7) + ((1 + v(p, 7)) if p % 2 == 0 else 0): bad += 1
        if v(D, 13) != 1 + v(p, 13) + ((1 + v(q, 13)) if q % 4 == 0 else 0): bad += 1
        for l in primes:
            e2, e3 = ords[l]
            m, m2 = e2 // gcd(e2, 3), e3 // gcd(e3, 3)
            assert m >= 2 and m2 >= 2
            if (D % l == 0) != (q % m == 0 or p % m2 == 0): bad += 1
print("(a) pairs", tests, "failures", bad)
# (b) Lemma 8.2 by brute force: every divisor B > 447174 of D must fall in one of the five cases
def cases(B, p, q):
    f = factorint(B)
    for l in f:
        if l in (2, 3, 7, 13): continue
        e2, e3 = n_order(2, l), n_order(3, l)
        if q % (e2 // gcd(e2, 3)) == 0 or p % (e3 // gcd(e3, 3)) == 0: return True
    return (B % 4 == 0 and p % 2 == 0) or (B % 81 == 0 and q % 2 == 0) or \
           (B % 343 == 0 and (q % 7 == 0 or p % 2 == 0)) or (B % 2197 == 0 and (p % 13 == 0 or q % 4 == 0))
from sympy import divisors
bad2 = 0; n2 = 0
for p, q in ((2, 3), (3, 5), (5, 8), (7, 11), (12, 19), (4, 7), (14, 4), (13, 21), (26, 28)):
    if gcd(p, q) != 1: continue
    D = 27 * (2 ** (3 * q) - 1) * (3 ** (3 * p) - 1)
    for B in divisors(D):
        if B > 447174:
            n2 += 1
            if not cases(B, p, q): bad2 += 1
print("(b) divisors B > 447174 tested", n2, "outside all five cases:", bad2)
# (c) stored models: reduced denominator divides D_n; size of gcd(N_n, D_n)
M = pickle.load(open(r"../actual-supply-and-denominators/models.pkl", "rb"))
for (p, q), (N, Dred) in sorted(M.items(), key=lambda t: t[0][1]):
    if (p + q) % 3 == 0: continue
    D = 27 * (2 ** (3 * q) - 1) * (3 ** (3 * p) - 1)
    g = gcd(N, Dred)
    print(f"(c) {p}/{q}: stored den | D_n: {D % (Dred // g) == 0}; D_n bits {D.bit_length()}, reduced den bits {(Dred // g).bit_length()}")
