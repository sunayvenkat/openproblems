"""Independent exact scalar audit: no companion imports or numerical logs."""
from fractions import Fraction as F


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def scale(z, k):
    return k * z[0], k * z[1]


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0] - z[1] * w[1]


def root(n):
    return ((1, 0), (0, 1), (-1, -1))[n % 3]


def roots(n, sign=1):
    return tuple(sum(root(sign * j)[k] for j in range(n % 3)) for k in (0, 1))


def divide(z, w):
    conjugate = w[0] - w[1], -w[1]
    numerator, norm = mul(z, conjugate), mul(w, conjugate)
    assert norm[1] == 0 and norm[0]
    return F(numerator[0], norm[0]), F(numerator[1], norm[0])


def alpha_floor(n):
    m = 0
    while 3 ** (m + 1) <= 2 ** n:
        m += 1
    return m


def beta_floor(n):
    return (3 ** n).bit_length() - 1


def raw_board(value):
    result, power3, b = (0, 0), 1, 0
    while power3 <= value:
        amax = (value // power3).bit_length() - 1
        result = add(result, mul(root(-b), roots(amax + 1)))
        power3 *= 3
        b += 1
    return result


def corner(a, b):
    value = divide(mul(add((1, 0), scale(root(-a), -1)),
                       add((1, 0), scale(root(-2 * b), -1))), (3, 0))
    assert all(v.denominator == 1 for v in value)
    return tuple(int(v) for v in value)


def digit(a, b, aa, bb, reciprocal, origin=True):
    x, y = add(add(aa, bb), add((-1, 0), corner(a, b)))
    if b == 0:
        return 0
    if b == 1:
        return 1 if origin and a == 0 else int(x >= 1 and y >= 0)
    if b == 2:
        return int(x <= -1 and x - y <= 0)
    if b == 3:
        return int(min(x, 0) <= y)
    isolate = reciprocal(b) - reciprocal(b - 1) == 2
    patch = reciprocal(b - 1) - reciprocal(b - 3) == 4
    assert not (isolate and patch)
    event = (root(reciprocal(b) - 2 * b) if isolate else
             root(reciprocal(b - 1) - 1 - 2 * b) if patch else (0, 0))
    x, y = x - event[0], y - event[1]
    return int(x <= 0 and x - y <= 0)


def response(pr, qr, h, width=24):
    conjugate = h[0] - 1 + root(pr + qr)[0], h[1] + root(pr + qr)[1]
    conjugate = conjugate[0] - conjugate[1], -conjugate[1]
    e = tuple(sum(root(-a)[i] for a in range(1, qr + 1)) for i in (0, 1))
    aq = add((1, 0), divide(add(e, scale(mul(root(2), conjugate), -1)), (2, 1)))
    assert all(F(v).denominator == 1 for v in aq)
    ap, am = tuple(map(int, aq)), tuple(map(int, add(aq, scale(root(2 * pr - qr), -1))))
    total = F(0)
    for a in range(width):
        if a:
            increment = mul(root(-qr - a), roots(pr + alpha_floor(a) + 1, 2))
            ap, am = add(ap, increment), add(am, increment)
        row = 0
        for b in range(width):
            bb = mul(root(-2 * b), raw_board(3 ** b))
            dp = digit(qr + a, b, ap, bb, beta_floor, origin=False)
            dm = digit(qr + a, b, am, bb, beta_floor, origin=False)
            row = 3 * row - 3 * (dp - dm)
        total += F(row, 2 ** a * 3 ** (width - 1))
    tail = F(27, 2 ** (width + 1)) + F(45, 2 * 3 ** width)
    return total, tail


def variation(a, b, c, d):
    assert abs(a * d - b * c) == 1
    n, m = b + d, a + c
    return 9 * (F(2, 2 ** n) * (1 + F(n + 1, b * d))
                + F(1, 3 ** m) * (F(3, 2) + F(6 * m + 3, 4 * a * c)))


def rational_axis(p, q, side, index, horizontal):
    grade = (p if horizontal else q) * index
    result = (0, 0)
    for b in range(grade // q + 1):
        amax = (grade - q * b) // p
        row = mul(root(-b), roots(amax + 1))
        tie = p * amax + q * b == grade
        reject = tie and ((horizontal and side < 0 and amax < index)
                          or (not horizontal and side > 0 and amax > 0))
        if reject:
            row = add(row, scale(root(amax - b), -1))
        result = add(result, row)
    return mul(root(-index if horizontal else -2 * index), result)


def rational_value(p, q, side):
    aa = [rational_axis(p, q, side, a, True) for a in range(3 * q)]
    bb = [rational_axis(p, q, side, b, False) for b in range(3 * p + 4)]
    reciprocal = lambda n: (n * q) // p - int(n > 0 and (n * q) % p == 0 and side > 0)
    sums = [F(0), F(0)]
    for b in range(3 * p + 4):
        row = 0
        for a in range(3 * q):
            eta = digit(a, b, aa[a], bb[b], reciprocal, origin=False)
            row = 2 * row + 1 - 3 * eta
        sums[int(b >= 4)] += F(row, 2 ** (3 * q - 1) * 3 ** b)
    horizontal, vertical = 1 - F(1, 2 ** (3 * q)), 1 - F(1, 3 ** (3 * p))
    return sums[0] / horizontal + sums[1] / (horizontal * vertical) - 1


def corrected_minimum(counts, doubled_time):
    counts = list(counts)
    largest = doubled_time // 2
    if largest >= 2:
        a = largest.bit_length() - 1
        if doubled_time < 3 * 2 ** a:
            counts[a % 3] -= 1
    eligible = doubled_time // 12
    if eligible >= 2:
        a = eligible.bit_length() - 1
        if 2 * doubled_time < 27 * 2 ** a:
            counts[a % 3] -= 1
    return min(counts)


def actual_digit(a, b):
    value, counts, power3, row = 2 ** a * 3 ** b, [0, 0, 0], 1, 0
    while power3 <= value:
        top = (value // power3).bit_length() - 1
        for color in range(3):
            first = (color + row) % 3
            if first <= top:
                counts[color] += (top - first) // 3 + 1
        power3 *= 3
        row += 1
    after = corrected_minimum(counts, 2 * value)
    counts[(a - b) % 3] -= 1
    before = corrected_minimum(counts, 2 * value - 1)
    assert after - before in (0, 1)
    return after - before


def true_enclosure(width=160, height=110):
    total = 0
    for b in range(height):
        row = 0
        for a in range(width):
            row = 2 * row + 1 - 3 * actual_digit(a, b)
        total = 3 * total + row
    partial = F(total, 2 ** (width - 1) * 3 ** (height - 1))
    outside = F(1, 2 ** width) + F(1, 3 ** height) - F(1, 2 ** width * 3 ** height)
    return partial - 6 * outside, partial + 3 * outside


if __name__ == '__main__':
    states = {(0, 1): (1, 0), (1, 1): (1, 0), (2, 0): (2, 1), (2, 2): (2, 0)}
    windows = [(F(9, 20), F(1, 2)), (-F(3, 50), -F(1, 20)),
               (-F(11, 10), -F(1)), (F(7, 5), F(3, 2))]
    for ((pr, qr), h), (lo, hi) in zip(states.items(), windows):
        center, error = response(pr, qr, h)
        assert lo < center - error < center + error < hi
        assert abs(center) - error > F(1, 20)
    for p, q, pp, qq in [(12, 19, 41, 65), (53, 84, 306, 485), (306, 485, 665, 1054)]:
        r, s = p + pp, q + qq
        h = tuple(sum(root(n + (r * n) // s)[i] for n in range(s)) for i in (0, 1))
        assert h == states[r % 3, s % 3]
        assert all((n * r) // s == alpha_floor(n) and (n * s) // r == beta_floor(n)
                   for n in range(1, 24))
        center, error = response(r % 3, s % 3, h)
        factor = F(1, 2 ** s) - F(1, 3 ** r)
        low = abs(factor) * (abs(center) - error)
        rest = variation(p, q, r, s) + variation(r, s, pp, qq)
        assert low > rest
        print('Cluster', p, q, 'leading/rest >', low // rest)
        if (p, q) == (12, 19):
            model = rational_value(p, q, -1)
            truth_low, truth_high = true_enclosure()
            assert 27 * (2 ** (3 * q) - 1) * (3 ** (3 * p) - 1) * model % 1 == 0
            assert truth_low - model > low - rest > 0
            assert truth_high - model < abs(factor) * (abs(center) + error) + rest
        if (p, q) == (53, 84):
            clearing = 27 * (2 ** (3 * q) - 1) * (3 ** (3 * p) - 1)
            outside = F(1, 2 ** s) + F(1, 3 ** r) - F(1, 2 ** s * 3 ** r)
            assert 0 < clearing * (low - rest) < 9 * clearing * outside < F(1, 2 ** 56)
    print('PASS: four ring responses, three full clusters, direct-cover true enclosure and2^56 exclusion')
