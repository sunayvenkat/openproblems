"""Independent integer-grade and field-arithmetic audit; no companion imports."""
from fractions import Fraction as F
from math import gcd


def plus(z, w):
    return z[0] + w[0], z[1] + w[1]


def times(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0] - z[1] * w[1]


def rotate(z, k):
    roots = ((1, 0), (0, 1), (-1, -1))
    return times(z, roots[k % 3])


def quotient(z, w):
    conjugate = (w[0] - w[1], -w[1])
    numerator = times(z, conjugate)
    norm = times(w, conjugate)[0]
    assert norm
    return F(numerator[0], norm), F(numerator[1], norm)


def field_rank(rows):
    pivots = {}
    for values in rows:
        row = list(values)
        for j, known in sorted(pivots.items()):
            factor = row[j]
            row = [plus(x, tuple(-v for v in times(factor, y))) for x, y in zip(row, known)]
        j = next((j for j, z in enumerate(row) if z != (0, 0)), None)
        if j is not None:
            divisor = row[j]
            pivots[j] = [quotient(z, divisor) for z in row]
    return len(pivots)


def grade_births(p, q, side):
    width, height = 3 * q, 3 * p + 4
    cap = p * (width - 1) + q * (height - 1)
    events = {}
    for a in range(cap // p + 4):
        for b in range(cap // q + 2):
            aa, bb = (a - 1, 1) if b == 0 and a else (a - 3, 3) if b == 1 and a >= 2 else (a, b)
            grade = p * aa + q * bb
            if grade > cap:
                continue
            key = grade, side * aa
            if key not in events:
                events[key] = [aa, bb, [0, 0, 0]]
            assert events[key][:2] == [aa, bb]
            events[key][2][(a - b) % 3] += 1
    count, birth = [0, 0, 0], {}
    for key in sorted(events):
        aa, bb, increment = events[key]
        before = min(count)
        count = [n + delta for n, delta in zip(count, increment)]
        birth[aa, bb] = min(count) - before
    assert birth.get((-1, 3), 0) == 0
    horizontal, vertical = 1 - F(1, 2 ** width), 1 - F(1, 3 ** (3 * p))
    head = sum((F(1 - 3 * birth.get((a, b), 0) + 3 * int((a, b) == (0, 1)), 2 ** a * 3 ** b)
                for a in range(width) for b in range(4)), F(0))
    tile = sum((F(1 - 3 * birth.get((a, b + 4), 0), 2 ** a * 3 ** b)
                for a in range(width) for b in range(3 * p)), F(0))
    return birth, head / horizontal + tile / (81 * horizontal * vertical) - 1


def readout(p, q, side):
    def floor_side(n, numerator, denominator, direction):
        value, rem = divmod(n * numerator, denominator)
        return value - int(n > 0 and rem == 0 and direction < 0)

    aa, bb = [(1, 0)], [(1, 0)]
    for i in range(1, 6 * q + 1):
        m = floor_side(i, p, q, side) % 3
        block = tuple(sum(rotate((1, 0), 2 * j)[k] for j in range(m + 1)) for k in (0, 1))
        aa.append(plus(aa[-1], rotate(block, -i)))
    for j in range(1, 6 * p + 4):
        m = floor_side(j, q, p, -side) % 3
        block = tuple(sum(rotate((1, 0), i)[k] for i in range(m + 1)) for k in (0, 1))
        bb.append(plus(bb[-1], rotate(block, -2 * j)))
    assert aa[:3 * q + 1] == aa[3 * q:]
    assert bb[:3 * p + 4] == bb[3 * p:]
    center_first = ((p + q) % 3 == 1) == (side > 0)

    def coefficient(a, b, color):
        left = plus((1, 0), tuple(-t for t in rotate((1, 0), -a)))
        right = plus((1, 0), tuple(-t for t in rotate((1, 0), -2 * b)))
        cross = times(left, right)
        assert all(z % 3 == 0 for z in cross)
        x, y = plus(plus(aa[a], bb[b]), (cross[0] // 3 - 1, cross[1] // 3))
        m = lambda j: floor_side(j, q, p, -side)
        isolated = m(b) - m(b - 1) == 2
        patch = m(b - 1) - m(b - 3) == 4
        assert not (isolated and patch)
        event = rotate((1, 0), m(b) - 2 * b) if isolated else rotate((1, 0), m(b - 1) - 1 - 2 * b) if patch else (0, 0)
        x, y = x - event[0], y - event[1]
        if color:
            x, y = (-y, x - y - 1) if center_first else (1 - y, x - y)
        return 1 - 3 * int(x <= 0 and x - y <= 0)
    return coefficient


def case(p, q, ratio, bits):
    plus_birth, plus_value = grade_births(p, q, 1)
    minus_birth, minus_value = grade_births(p, q, -1)
    u, v = 2 ** q, 3 ** p
    clearing = 27 * (u ** 3 - 1) * (v ** 3 - 1)
    integer = clearing * (plus_value - minus_value)
    assert integer.denominator == 1 and integer.numerator % (u - v) == 0
    response = (plus_value - minus_value) / (F(1, u) - F(1, v))
    assert response == F(-u * v * (integer.numerator // (u - v)), clearing)
    assert clearing // response.denominator == ratio and response.denominator.bit_length() == bits

    readouts = [readout(p, q, side) for side in (1, -1)]
    for read, birth in zip(readouts, (plus_birth, minus_birth)):
        for a in range(3 * q):
            for b in range(4, 3 * p + 4):
                assert read(a, b, 0) == 1 - 3 * birth.get((a, b), 0)
    for zeta in ((1, 0), (0, 1)):
        rows, extended = [], []
        for a in range(q):
            for b in range(4, p + 4):
                values = []
                for read in readouts:
                    for color in (0, 1):
                        value = (0, 0)
                        for i in range(3):
                            root = (1, 0)
                            for j in range(3):
                                scalar = 2 ** i * read(a + i * q, b + j * p, color)
                                value = plus(value, (scalar * root[0], scalar * root[1]))
                                root = times(root, zeta)
                        values.append(value)
                divisor = (2 - zeta[0], -zeta[1])
                extra = [quotient(plus(values[j], tuple(-t for t in values[j + 2])), divisor) for j in (0, 1)]
                for j in (0, 1):
                    assert times(divisor, extra[j]) == plus(values[j], tuple(-t for t in values[j + 2]))
                rows.append(values)
                extended.append(values + extra)
        assert field_rank(rows) == field_rank(extended) == 4

    x, y = F(1, u), F(1, v)
    for a, b, k in ((0, 0, 0), (1, 0, 1), (3, 0, 3), (4, 0, 4), (5, -4, 1), (-2, 3, 1)):
        value = x ** a * y ** b * (1 - y ** 3) / (x - y) ** k
        raw = u ** max(a - k, 0) * v ** max(b + 3 - k, 0) * abs(u - v) ** k
        assert value.denominator == raw // gcd(raw, v ** 3 - 1)
        assert gcd(abs(u - v), 6) == 1
        assert gcd(abs(u - v), v ** 3 - 1) == gcd(abs(u - v), u ** 3 - 1, v ** 3 - 1)
    print({'p': p, 'q': q, 'denominator_bits': bits, 'nominal_over_reduced': ratio,
           'independent_vertical_ranks': (4, 4), 'token_grade_value_rebuilt': True})


if __name__ == '__main__':
    assert times((0, 1), (0, 1)) == (-1, -1)
    assert quotient((1, 0), (1, -1)) == (F(2, 3), F(1, 3))
    case(5, 8, 486, 44)
    case(53, 84, 1458, 499)
    print('PASS: independent token-grade, normalization, pole-rank and denominator audit')
