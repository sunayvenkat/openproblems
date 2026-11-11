"""Certified enclosure and continued fraction of Z from the actual model at 15601/24727.

Error bound (rectangle bound R13 of resonant_models.md): if model floors equal true floors
for a<R, b<S then |Z - z| <= 9(2^-R + 3^-S - 2^-R 3^-S).  For the actual convergent
15601/24727 with successor 31867/50508: R = 24727+50508, S = 15601+31867.
"""
import sys, pickle, math
from fractions import Fraction as F
from fastmodel import model_value
sys.set_int_max_str_digits(0)
p, q, p2, q2 = 15601, 24727, 31867, 50508
sign = 1 if 2 ** q > 3 ** p else -1
N, D = model_value(p, q, sign)
z = F(N, D)
R, S = q + q2, p + p2
eps = 9 * (F(1, 2 ** R) + F(1, 3 ** S) - F(1, 2 ** R * 3 ** S))
lo, hi = z - eps, z + eps
pickle.dump((N, D, R, S), open('z24727.pkl', 'wb'))


def cf_terms(x, limit):
    n, d = x.numerator, x.denominator
    out = []
    while d and len(out) < limit:
        a, r = divmod(n, d); out.append(a); n, d = d, r
    return out


def common_prefix(x, y):
    # walk both Euclid expansions in lockstep
    n1, d1, n2, d2 = x.numerator, x.denominator, y.numerator, y.denominator
    out = []
    while d1 and d2:
        a1, r1 = divmod(n1, d1); a2, r2 = divmod(n2, d2)
        if a1 != a2: break
        out.append(a1); n1, d1, n2, d2 = d1, r1, d2, r2
    return out


pre = common_prefix(lo, hi)
# convergent denominators
h0, h1 = 0, 1
bits = []
for a in pre:
    h0, h1 = h1, a * h1 + h0
    bits.append(h1.bit_length())
big = sorted(((x.bit_length(), i) for i, x in enumerate(pre)), reverse=True)[:8]
print('certified CF terms of Z:', len(pre), '; last convergent denominator bits:', bits[-1])
print('first 30:', pre[:30])
print('largest partial quotients (bits, index):', big)
print('index of largest -> convergent den bits before it:', [(b, i, bits[i - 1]) for b, i in big[:4]])
gm = math.exp(sum(math.log(a) for a in pre[1:] if a > 0) / (len(pre) - 1))
print('geometric mean of terms 1..:', round(gm, 4), ' (Khinchin 2.6854)')
pickle.dump(pre, open('zcf.pkl', 'wb'))
