"""Independent board-count and boundary-kernel audit; no companion imports."""

from collections import defaultdict
from fractions import Fraction as Q
from functools import cache


@cache
def tau(t):
    counts = [0, 0, 0]
    a, two = 0, 1
    while two <= t:
        b, value = 0, two
        while value <= t:
            counts[(a - b) % 3] += 1
            b, value = b + 1, value * 3
        if a and 2 * t < 3 * two:
            counts[a % 3] -= 1
        if a and 6 * two <= t < Q(27 * two, 4):
            counts[a % 3] -= 1
        a, two = a + 1, two * 2
    return min(counts)


def eta(a, b):
    t = 2**a * 3**b
    jump = tau(Q(t)) - tau(Q(4 * t - 1, 4))
    assert jump in (0, 1)
    return jump


def kappa(t):
    answer, power = 0, 9
    while power <= 2 * t:
        answer, power = answer + 1, power * 27
    return answer


def h(t):
    return tau(2 * t) - tau(t) - kappa(t)


def atoms(limit):
    out = {}
    a, two = 0, 1
    while two <= limit:
        b, value = 0, two
        while value <= limit:
            if eta(a, b):
                out[a, b] = 1
            b, value = b + 1, value * 3
        a, two = a + 1, two * 2
    return out


def moment(values):
    return sum((Q(v, 2**a * 3**b) for (a, b), v in values.items()), Q())


def check_clock_and_filters():
    values = atoms(3**11)
    assert eta(0, 1) == eta(0, 2) == 1
    assert all(eta(a, 0) == 0 for a in range(19))
    assert tau(Q(27, 2)) == tau(Q(107, 8))
    for b, expected in ((3, 1), (11, -1)):
        t = Q(3**b, 2)
        assert h(t) - h(t - Q(1, 8)) == expected
    candidates = set()
    for a, b in values:
        d = Q(2**a * 3**b)
        candidates.update((d, d / 2))
    for b in range(2, 12, 3):
        candidates.add(Q(3**b, 2))
    for t in candidates:
        if 2 * t <= 3**11:
            jump = h(t) - h(t - Q(1, 8))
            if t.denominator == 1:
                n, a, b = t.numerator, 0, 0
                while n % 2 == 0:
                    a, n = a + 1, n // 2
                while n % 3 == 0:
                    b, n = b + 1, n // 3
                assert n == 1
                assert jump == eta(a + 1, b) - eta(a, b)
            else:
                n, b = t.numerator, 0
                while n % 3 == 0:
                    b, n = b + 1, n // 3
                assert n == 1 and t.denominator == 2
                assert jump == eta(0, b) - int(b % 3 == 2)

    total = moment(values)
    f0 = sum((Q(v, 3**b) for (a, b), v in values.items() if a == 0), Q())
    grid, outside = Q(), Q()
    for (a, b), v in values.items():
        d = Q(2**a * 3**b)
        if (d / 2).denominator == 1:
            grid += v / (d / 2)
        else:
            outside += v / (d / 2)
        grid -= v / d
    outside -= Q(3, 13)
    assert grid == total - 2 * f0
    assert outside == 2 * f0 - Q(3, 13)
    assert outside >= Q(77, 117)
    assert grid + outside == total - Q(3, 13)

    exteriors = {}
    for a, b in ((0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (0, 2), (0, 3), (3, 2)):
        scale = 2**a * 3**b
        down = {Q(2**i * 3**j, scale): v for (i, j), v in values.items()}
        exteriors[a, b] = sum((v / t for t, v in down.items()
                              if t.denominator != 1), Q())
        assert sum((v / t for t, v in down.items()), Q()) - total == (scale - 1) * total
    for a in range(1, 4):
        column = sum((Q(v, 3**j) for (i, j), v in values.items() if i == a - 1), Q())
        assert exteriors[a, 0] - 2 * exteriors[a - 1, 0] == 2 * column
    for b in range(1, 4):
        row = sum((Q(v, 2**i) for (i, j), v in values.items() if j == b - 1), Q())
        assert exteriors[0, b] - 3 * exteriors[0, b - 1] == 3 * row
    assert exteriors[0, 1] == 0
    assert values[0, 1] == 1 and Q(3, 9) == Q(1, 3)
    corner = sum((Q(v, 2**i * 3**j) for (i, j), v in values.items() if i < 3 and j < 2), Q())
    assert exteriors[3, 2] == 9 * exteriors[3, 0] + 8 * exteriors[0, 2] - 72 * corner


def product(left, right):
    out = defaultdict(int)
    for (a, b), x in left.items():
        for (c, d), y in right.items():
            out[a + c, b + d] += x * y
    return dict(out)


def check_dictionary():
    p = {(0, 0): 1}
    for q, r in ((1, 1), (2, 1), (3, 2)):
        p = product(p, {(2 * q, 0): 1, (q, r): 1, (0, 2 * r): 1})
    max_a = max(a for a, b in p)
    max_b = max(b for a, b in p)
    pi = sum(v * 2**a * 3**b for (a, b), v in p.items())
    width, height = max_a + 3, max_b + 7

    def kernel(a, b):
        factor = pi if b < 4 else sum(v * 2**u * 3**w for (u, w), v in p.items()
                                                if a < u or b - 4 < w)
        return Q(81 * factor, 2**a * 3**b)

    # Extract profile coefficients from independent far-column/far-row values.
    alpha = [kernel(a, height) * 3**height for a in range(max_a)]
    beta = [kernel(width, b) * 2**width for b in range(max_b + 4)]
    assert all(v.denominator == 1 for v in alpha + beta)
    assert alpha[-1] == 162 and beta[-1] == 3 and beta[0] == 81 * pi
    c = {(a, b): 1 - 3 * eta(a, b) for a in range(width) for b in range(height)}
    direct, profiles, correction = Q(), Q(), Q()
    for (a, b), value in c.items():
        weight = (alpha[a] / 3**b if a < max_a else Q())
        weight += beta[b] / 2**a if b < max_b + 4 else Q()
        residual = kernel(a, b) - weight
        if a >= max_a or b >= max_b + 4:
            assert residual == 0
        direct += kernel(a, b) * value
        profiles += weight * value
        correction += residual * value
    explicit = Q()
    for (a, b), value in p.items():
        low = sum((Q(c[i, j], 2**i * 3**j) for i in range(a) for j in range(4)), Q())
        corner = sum((Q(c[i, j + 4], 2**i * 3**j) for i in range(a) for j in range(b)), Q())
        explicit -= value * 2**a * 3**b * (81 * low + corner)
    assert correction == explicit and correction.denominator == 1
    assert direct == profiles + correction
    assert all(c[a, 0] == 1 for a in range(width))
    assert 2 * beta[0] == 162 * pi


if __name__ == "__main__":
    check_clock_and_filters()
    check_dictionary()
    print("PASS: independent board clocks, fractional moments, mixed filters and three-factor dictionary.")
