"""Small exact checks for the periodic floor model and double-return identity."""
from fractions import Fraction as F
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORRECTION = (((0, 0), (0, 0), (0, 0)),
              ((0, 0), (1, 0), (1, 1)),
              ((0, 0), (0, -1), (1, 0)))


def add(z, w):
    return z[0]+w[0], z[1]+w[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0]-z[1]
    return z


def floor_side(n, p, q, sign):
    quotient, rem = divmod(n*p, q)
    return quotient-int(rem == 0 and sign < 0)


def exact_power_floor(n, powerbase, logbase):
    v, k, power = powerbase**n, 0, 1
    while power*logbase <= v:
        power *= logbase
        k += 1
    return k


def model(p, q):
    assert (p+q) % 3 and F(1, 2) < F(p, q) < F(2, 3)
    sign = 1 if 2**q > 3**p else -1
    P, Q = 3*q, 3*p
    A, B = [(1, 0)], [(1, 0)]
    for k in range(1, 2*P+1):
        s = ((1, 0), (0, -1), (0, 0))[floor_side(k, p, q, sign) % 3]
        A.append(add(A[-1], rot(s, -k)))
    for k in range(1, 2*Q+1):
        s = ((1, 0), (1, 1), (0, 0))[floor_side(k, q, p, -sign) % 3]
        B.append(add(B[-1], rot(s, -2*k)))
    assert A[:P+1] == A[P:] and B[:Q+1] == B[Q:]

    def eta(a, b, small_correction=True):
        x, y = add(add(A[a % P], B[b % Q]), CORRECTION[a % 3][b % 3])
        x -= 1
        if b == 0:
            return 0
        if b == 1:
            return 1 if a == 0 and small_correction else int(x >= 1 and y >= 0)
        if b == 2:
            return int(x <= -1 and x-y <= 0)
        if b == 3:
            return int(min(x, 0) <= y)
        m = lambda k: floor_side(k, q, p, -sign)
        epsilon = [0, 0, 0]
        isolated = m(b)-m(b-1) == 2
        patch = m(b-1)-m(b-3) == 4
        assert not (isolated and patch)
        if isolated:
            epsilon[(m(b)-2*b) % 3] = 1
        if patch:
            epsilon[(m(b-1)-1-2*b) % 3] = 1
        return int(x <= epsilon[0]-epsilon[2] and x-y <= epsilon[0]-epsilon[1])

    coefficient = lambda a, b: 1-3*eta(a, b, False)
    horizontal = 1-F(1, 2**P)
    vertical = 1-F(1, 3**Q)
    head = sum((F(coefficient(a, b), 2**a*3**b) for a in range(P) for b in range(4)), F(0))
    tile = sum((F(coefficient(a, b+4), 2**a*3**b) for a in range(P) for b in range(Q)), F(0))
    value = head/horizontal + tile/(81*horizontal*vertical)-1
    denominator = 27*(2**P-1)*(3**Q-1)
    assert (denominator*value).denominator == 1
    for a in range(q):
        for b in range(4, 4+p):
            assert eta(a, b) == eta(a+P, b) == eta(a, b+Q)
    return eta, value, denominator


def check_double_return():
    c = {(a, b): ((a+2*b) % 4)-1 for a in range(5) for b in range(6)}
    at = lambda a, b: c.get((a, b), 0)
    P, Q, p, q = 2, 3, 4, 27
    total = sum((F(v, 2**a*3**b) for (a, b), v in c.items()), F(0))
    corner = p*q*sum((F(at(a, b), 2**a*3**b) for a in range(P) for b in range(Q)), F(0))
    side_a = p*sum((F(at(a, b+Q)-at(a, b), 2**a*3**b)
                   for a in range(P) for b in range(6)), F(0))
    side_b = q*sum((F(at(a+P, b)-at(a, b), 2**a*3**b)
                   for a in range(5) for b in range(Q)), F(0))
    mixed = sum((F(at(a+P, b+Q)-at(a+P, b)-at(a, b+Q)+at(a, b), 2**a*3**b)
                 for a in range(5) for b in range(6)), F(0))
    assert (p-1)*(q-1)*total == corner+side_a+side_b+mixed
    assert corner.denominator == 1


if __name__ == '__main__':
    check_double_return()
    rows = json.loads((HERE.parent/'Open conjecture transfer search/168_exact_diagonal_results.json').read_text())['exactDp']
    results = []
    for p, q, next_p, next_q in ((5, 8, 12, 19), (12, 19, 41, 65), (53, 84, 306, 485)):
        eta, value, denominator = model(p, q)
        sign = 1 if 2**q > 3**p else -1
        first_a, first_b = q+next_q, p+next_p
        assert all(exact_power_floor(n, 2, 3) == floor_side(n, p, q, sign) for n in range(1, first_a))
        assert exact_power_floor(first_a, 2, 3) != floor_side(first_a, p, q, sign)
        assert all(exact_power_floor(n, 3, 2) == floor_side(n, q, p, -sign) for n in range(1, first_b))
        assert exact_power_floor(first_b, 3, 2) != floor_side(first_b, q, p, -sign)
        last, checked = 0, 0
        for row in rows:
            v, a, b = row['t'], 0, 0
            while v % 2 == 0:
                v //= 2
                a += 1
            while v % 3 == 0:
                v //= 3
                b += 1
            if a < first_a and b < first_b:
                assert eta(a, b) == row['tau']-last, (p, q, row)
                checked += 1
            last = row['tau']
        skew_sums = sorted({sum(eta(a+i*q, b+((j-i) % 3)*p) for i in range(3))
                            for a in range(q) for b in range(4, 4+p) for j in range(3)})
        results.append({'p': p, 'q': q, 'first_floor_mismatches': [first_a, first_b],
                        'periods': [3*q, 3*p], 'exact_optima_compared': checked,
                        'skew_triple_sums': skew_sums, 'rational_model': str(value),
                        'clearing_denominator': str(denominator)})
    (HERE/'returns_check.json').write_text(json.dumps(results, indent=2)+'\n')
    print([{k: v for k, v in result.items() if k not in ('rational_model', 'clearing_denominator')}
           for result in results])
