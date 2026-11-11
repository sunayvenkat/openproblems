"""Finite certificates from exact actual models (all quantities exact rationals).

For each actual convergent model z_n we use the explicit rectangle bound
|Z - z_n| <= eps_n = 9(2^-R + 3^-S - 2^-R 3^-S), R = q_n+q_{n+1}, S = p_n+p_{n+1}
(complete model digits equal true digits on the floor-agreement rectangle).
"""
import sys, pickle, math, time
from fractions import Fraction as F
from fastmodel import model_value
sys.set_int_max_str_digits(0)
conv = [(5, 8), (12, 19), (41, 65), (53, 84), (306, 485), (665, 1054), (15601, 24727),
        (31867, 50508), (79335, 125743), (111202, 176251)]
nonres = [c for c in conv[:-1] if sum(c) % 3]
Z = {}
for i, (p, q) in enumerate(conv[:-1]):
    p2, q2 = conv[i + 1]
    eps = 9 * (F(1, 2 ** (q + q2)) + F(1, 3 ** (p + p2)) - F(1, 2 ** (q + q2) * 3 ** (p + p2)))
    if (p + q) % 3:
        t = time.time(); N, D = model_value(p, q, 1 if 2 ** q > 3 ** p else -1); z = F(N, D)
    else:
        a, b = pickle.load(open('res1054.pkl', 'rb')); z = F(a, b)
    Z[(p, q)] = (z, eps)
    print('model', (p, q), 'den bits', z.denominator.bit_length(), 'log2 eps', round(math.log2(9) - (q + q2), 2), flush=True)
best = (79335, 125743)
zb, eb = Z[best]
print('\nNonvanishing certificates: |z_n - z_best| - eps_n - eps_best > 0 implies z_n != Z')
for k, (z, e) in Z.items():
    if k == best: continue
    d = abs(z - zb)
    ok = d > e + eb
    lg = math.log2(d.numerator) - math.log2(d.denominator)
    print(k, 'log2|z_n - z_best| = %.2f' % lg, ' certified z_n != Z:', ok,
          ' implied den(Z) lower bound log2 >= %.1f' % (-(math.log2(d.numerator + 0.0 if False else 1) ) + lg * -1 - z.denominator.bit_length()) if ok else '')
pickle.dump({k: (v[0].numerator, v[0].denominator) for k, v in Z.items()}, open('models.pkl', 'wb'))
# certified CF of Z from best enclosure
lo, hi = zb - eb, zb + eb
n1, d1, n2, d2 = lo.numerator, lo.denominator, hi.numerator, hi.denominator
pre = []
while d1 and d2:
    a1, r1 = divmod(n1, d1); a2, r2 = divmod(n2, d2)
    if a1 != a2: break
    pre.append(a1); n1, d1, n2, d2 = d1, r1, d2, r2
h0, h1 = 0, 1; dens = []
for a in pre:
    h0, h1 = h1, a * h1 + h0; dens.append(h1.bit_length())
big = sorted(((x.bit_length(), i) for i, x in enumerate(pre)), reverse=True)[:5]
print('\ncertified CF terms of Z:', len(pre), ' last convergent den bits:', dens[-1])
print('largest partial quotients (bits, index, preceding convergent den bits):', [(b, i, dens[i - 1]) for b, i in big])
gm = math.exp(sum(math.log(a) for a in pre[1:]) / (len(pre) - 1))
print('geometric mean of a_1..:', round(gm, 4))
pickle.dump(pre, open('zcf_best.pkl', 'wb'))
