"""Independent critical-state audit; no companion imports or floating times."""

from math import gcd


def canonical(coefficients):
    return tuple(value - coefficients[2] for value in coefficients)


def add(left, right):
    return canonical(tuple(a + b for a, b in zip(left, right)))


def neg(value):
    return tuple(-entry for entry in value)


def multiply(left, right):
    result = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            result[(i + j) % 3] += left[i] * right[j]
    return canonical(result)


def root(power):
    return canonical(tuple(int(i == power % 3) for i in range(3)))


def geometric(length, sign=1):
    return canonical(tuple(sum(int((sign * k) % 3 == i)
                               for k in range(length % 3)) for i in range(3)))


def staircase(n, modulus, a, b):
    """Recursively count by horizontal thresholds, using the last column."""
    if n == 0:
        return 0
    qa, a = divmod(a, modulus)
    qb, b = divmod(b, modulus)
    base = qa * n * (n - 1) // 2 + qb * n
    if a == 0:
        return base
    height = (a * (n - 1) + b) // modulus
    return base + n * height - staircase(
        height, a, modulus, modulus - b + a - 1)


def triangle(level, p, q):
    if level < 0:
        return 0
    last, remainder = divmod(level, q)
    return last + 1 + staircase(last + 1, p, q, remainder)


def prestate(p, q):
    counts = [0, 0, 0]
    for a_residue in range(3):
        for b_residue in range(3):
            level = (2 * p * q - p * a_residue - q * b_residue - 1) // 3
            counts[(a_residue - b_residue - 2) % 3] += triangle(level, p, q)
    for b, last in ((0, 2 * q + 2), (1, 2 * q + 1)):
        for color in range(3):
            first = (color + b) % 3
            counts[color] += max(0, (last - first) // 3 + 1)
    assert sum(counts) == 2 * p * q + p + 5 * q + 4
    return tuple(counts)


def floor_word(p, q):
    return ''.join('E' + 'N' * (p * (a + 1) // q - p * a // q)
                   for a in range(q))


def east_transform(word):
    counts = [0, 0, 0]
    for index, letter in enumerate(word):
        if letter == 'E':
            counts[index % 3] += 1
    return canonical(counts)


def cleared_imbalance(p, q, h):
    denominator = add(root(0), neg(root(-1)))
    rectangle = multiply(geometric(q), geometric(p, -1))
    numerator = add(geometric(q), neg(multiply(root(-p), h)))
    doubled = add(multiply(denominator, rectangle),
                  multiply(add(root(q), root(-p)), numerator))
    low = add(geometric(2 * q + 3), multiply(root(-1), geometric(2 * q + 2)))
    return add(multiply(root(1), doubled), multiply(denominator, low))


def word_state(digits):
    pp, qp, previous = 1, 0, 'N'
    p, q, current = 0, 1, 'E'
    for index, digit in enumerate(digits, 1):
        pn, qn = digit * p + pp, digit * q + qp
        word = current * digit + previous if index % 2 else previous + current * digit
        assert word == floor_word(pn, qn)
        pp, qp, previous, p, q, current = p, q, current, pn, qn, word
    state = (len(digits) % 2, pp % 3, qp % 3, east_transform(previous),
             p % 3, q % 3, east_transform(current))
    return state, p, q


def actual_interval(p, q):
    times = (9 * 3 ** (2 * p), 9 * 2 ** q * 3 ** p, 9 * 2 ** (2 * q))
    low, high = 2 * min(times), 2 * max(times)
    before, after, inside = [0, 0, 0], [0, 0, 0], []
    b, power_three = 0, 1
    while 2 * power_three <= high:
        a, power_two, ordinary = 0, 1, power_three
        while 2 * ordinary <= high:
            if b == 0 and a >= 1:
                arrival = 3 * power_two
            elif b == 1 and a >= 2:
                arrival = 27 * (power_two // 4)
            else:
                arrival = 2 * ordinary
            color = (a - b) % 3
            before[color] += arrival < low
            after[color] += arrival <= high
            if low <= arrival <= high:
                inside.append((a, b))
            a, power_two, ordinary = a + 1, 2 * power_two, 2 * ordinary
        b, power_three = b + 1, 3 * power_three
    assert set(inside) == {(0, 2 * p + 2), (q, p + 2), (2 * q, 2)}
    return tuple(before), tuple(after)


def check():
    for n in range(8):
        for modulus in range(1, 7):
            for a in range(7):
                for b in range(7):
                    assert staircase(n, modulus, a, b) == sum(
                        (a * index + b) // modulus for index in range(n))
    denominator = add(root(0), neg(root(-1)))
    for q in range(1, 19):
        for p in range(1, q + 1):
            if gcd(p, q) != 1:
                continue
            counts = [0, 0, 0]
            for a in range(2 * q + 1):
                for b in range(2 * p + 1):
                    if p * a + q * b < 2 * p * q:
                        counts[(a - b - 2) % 3] += 1
            for b, last in ((0, 2 * q + 2), (1, 2 * q + 1)):
                for a in range(last + 1):
                    counts[(a - b) % 3] += 1
            assert tuple(counts) == prestate(p, q)
            assert cleared_imbalance(p, q, east_transform(floor_word(p, q))) == multiply(
                denominator, canonical(counts))
    required = {(0, 1): (1, 0, 0), (1, 1): (1, 0, 0),
                (2, 0): (2, 1, 0), (2, 2): (2, 0, 0)}
    units = {root(k) for k in range(3)} | {neg(root(k)) for k in range(3)}
    for p in range(3):
        for q in range(3):
            if (p + q) % 3 == 0:
                continue
            coefficient = neg(multiply(root(1 - p), add(root(q), root(-p))))
            assert coefficient in units
            if (p, q) in required:
                assert cleared_imbalance(p, q, required[p, q]) == (0, 0, 0)
            else:
                assert (2 * p * q + p + 5 * q + 4) % 3 != 0
    prefix = [1, 1, 1, 2, 2]
    initial = word_state(prefix)[0]
    for block in ((3, 3), (1, 3, 2, 3)):
        for length in range(1, len(block) + 1):
            state, p, q = word_state(prefix + list(block[:length]))
            assert (p + q) % 3 != 0
            assert state[-1] == required[p % 3, q % 3]
            assert len(set(prestate(p, q))) == 1
        assert word_state(prefix + list(block))[0] == initial
    actual_digits = prefix + [3, 1, 5, 2]
    assert word_state(actual_digits)[1:] == (665, 1054)
    assert 2 ** 1054 < 3 ** 665 and 2 ** 1539 > 3 ** 971
    expected = {(5, 8): (43, 43, 43), (12, 19): (189, 189, 189),
                (41, 65): (1900, 1900, 1900), (53, 84): (3127, 3127, 3127),
                (306, 485): (99852, 99851, 99852)}
    for (p, q), counts in expected.items():
        u, v = 2 ** q, 3 ** p
        assert 3 * max(u * u, v * v) < 4 * min(u * u, v * v)
        before, after = actual_interval(p, q)
        assert before == counts == prestate(p, q)
        assert after == tuple(value + 1 for value in counts)
        print('ACTUAL', (p, q), before)
    print('PASS: independent actual intervals, Euclidean counts, literal words and balanced loops')


if __name__ == '__main__':
    check()
