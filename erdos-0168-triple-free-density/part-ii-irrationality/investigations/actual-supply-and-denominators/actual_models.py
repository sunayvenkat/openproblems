"""Actual convergents of alpha=log2/log3: correct-side models, reduced denominators,
full cyclotomic survival, and exact consecutive-model differences."""
import sys, time, json, math
from fractions import Fraction as F
from math import gcd
import mpmath as mp
from sympy import factorint, divisors, mobius
from fastmodel import model_value
sys.set_int_max_str_digits(0)

mp.mp.dps = 3000
alpha = mp.log(2) / mp.log(3)


def convergents(nmax):
    x, a = alpha, []
    for _ in range(nmax + 2):
        k = int(mp.floor(x)); a.append(k); x = 1 / (x - k)
    P, Q = [0, 1], [1, 0]
    out = []
    for k in a:
        P.append(k * P[-1] + P[-2]); Q.append(k * Q[-1] + Q[-2])
    # p_n/q_n = P[n+2]/Q[n+2]
    for n in range(len(a) - 1):
        p, q = P[n + 2], Q[n + 2]
        assert (3 ** p < 2 ** q) == (n % 2 == 0) or q < 3 if q < 5000 else True
        out.append((n, p, q, a[n + 1]))
    return out


def cyclo(n, x):
    num = den = 1
    for d in divisors(n):
        m = mobius(n // d)
        if m == 1: num *= x ** d - 1
        elif m == -1: den *= x ** d - 1
    assert num % den == 0
    return num // den


if __name__ == '__main__':
    qmax = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
    cs = convergents(40)
    rows, models = [], {}
    for n, p, q, anext in cs:
        if q < 8 or q > qmax:
            continue
        s = (p + q) % 3
        sign = 1 if 2 ** q > 3 ** p else -1
        nxt = next(c for c in cs if c[0] == n + 1)
        row = dict(n=n, p=p, q=q, a_next=anext, Q=nxt[2], s=s, side='lower' if sign > 0 else 'upper',
                   Q_minus_5q=nxt[2] - 5 * q)
        if s:
            t = time.time()
            N, D = model_value(p, q, sign)
            g = gcd(N, D); d = D // g
            models[n] = F(N, D)
            c2, c3 = cyclo(3 * q, 2), cyclo(3 * p, 3)
            row.update(den_bits=d.bit_length(), D_bits=D.bit_length(),
                       log2_cleared_bound=round(math.log2(486) + 5 * q - nxt[2], 1),
                       full_Phi3q2=(d % c2 == 0), full_Phi3p3=(d % c3 == 0),
                       gcdN_Phi3q2_bits=gcd(N, c2).bit_length(), gcdN_Phi3p3_bits=gcd(N, c3).bit_length(),
                       secs=round(time.time() - t, 1))
        rows.append(row)
        print(row, flush=True)
    keys = sorted(models)
    for i, j in zip(keys, keys[1:]):
        diff = models[i] - models[j]
        r = next(x for x in rows if x['n'] == i)
        if diff:
            lg = math.log2(abs(diff.numerator)) - math.log2(diff.denominator)
            print('diff n=%d vs n=%d: log2|z_i-z_j| = %.2f ; -(q+Q) = %d ; normalized r=(z_j-z_i)2^(q+Q) = %.6g'
                  % (i, j, lg, -(r['q'] + r['Q']), float(-diff * 2 ** (r['q'] + r['Q']))))
        else:
            print('diff n=%d vs n=%d: EXACTLY EQUAL' % (i, j))
    json.dump(rows, open('actual_models.json', 'w'), indent=1)
