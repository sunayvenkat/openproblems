"""Independent original-board and minimum-difference shift audit; no imports of notes."""
from fractions import Fraction as F
from functools import cache

ROOT = ((1, 0), (0, 1), (-1, -1))
STATES = ((0, 1, (0, -1)), (1, 1, (0, 0)),
          (2, 0, (1, 0)), (2, 2, (1, 0)))


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def subtract(z, w):
    return z[0] - w[0], z[1] - w[1]


def multiply(z, w):
    x, y = z
    a, b = w
    return x * a - y * b, x * b + y * a - y * b


def rootsum(indices):
    z = (0, 0)
    for i in indices:
        z = add(z, ROOT[i % 3])
    return z


@cache
def counts(t):
    result, j, p3 = [0, 0, 0], 0, 1
    while p3 <= t:
        i, value = 0, p3
        while value <= t:
            result[(i - j) % 3] += 1
            i, value = i + 1, 2 * value
        j, p3 = j + 1, 3 * p3
    return tuple(result)


@cache
def cover(t):
    result = list(counts(t))
    a, root = 1, 2
    while root <= t:
        if 3 * root > 2 * t or (6 * root <= t and 4 * t < 27 * root):
            result[a % 3] -= 1
        a, root = a + 1, 2 * root
    return min(result)


@cache
def axis(t, phase):
    c = counts(t)
    return multiply((c[0] - c[2], c[1] - c[2]), ROOT[phase % 3])


def birth(z, b):
    x, y = z
    if b == 0:
        return 0
    if b == 1:
        return 1 + min(x - 1, y, 0) - min(x, y + 1, 0)
    if b == 2:
        return min(x + 1, y + 1, 0) - min(x, y + 1, 0)
    if b == 3:
        return 1 + min(x, y, 0) - min(x, y + 1, 0)
    return min(x, y, 0) - min(x - 1, y, 0)


@cache
def values(a, b):
    t = 2 ** a * 3 ** b
    target = 1 - 3 * (cover(t) - cover(t - 1))
    event = (0, 0)
    if b >= 4:
        v = 3 ** b
        m, n = v.bit_length() - 1, (v // 6).bit_length() - 1
        isolated, patched = 3 * 2 ** m > 2 * v, 6 * 2 ** n <= v and 4 * v < 27 * 2 ** n
        assert not (isolated and patched)
        event = ROOT[(m - 2 * b) % 3] if isolated else ROOT[(n - 2 * b) % 3] if patched else (0, 0)
    answer = [target]
    for p, q, endpoint in STATES:
        gamma = ROOT[(2 * p - q) % 3]
        shifted = add(endpoint, multiply(gamma, subtract(axis(2 ** a, -a), (1, 0))))
        shifted = add(shifted, multiply(ROOT[-q % 3], multiply(
            rootsum(2 * j for j in range(p)), rootsum(-k for k in range(1, a + 1)))))
        correction = multiply(rootsum(-k for k in range(1, a + q + 1)),
                              rootsum(-2 * k for k in range(1, b + 1)))
        z = subtract(subtract(add(add(shifted, axis(3 ** b, -2 * b)), correction), (1, 0)), event)
        g = -3 * (birth(z, b) - birth(subtract(z, gamma), b))
        assert g in (-3, 0, 3)
        answer.append(g)
    return tuple(answer)


def determinant(rows):
    a = [[F(x) for x in row] for row in rows]
    result = F(1)
    for k in range(len(a)):
        pivot = next(i for i in range(k, len(a)) if a[i][k])
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            result = -result
        p = a[k][k]
        result *= p
        for i in range(k + 1, len(a)):
            factor = a[i][k] / p
            if factor:
                for j in range(k, len(a)):
                    a[i][j] -= factor * a[k][j]
    assert result.denominator == 1
    return result.numerator


def run():
    unit = ([(0, b) for b in (*range(4, 40), *range(51, 55), *range(60, 81))]
            + [(1, b) for b in (*range(4, 15), 17)]
            + [(a, b) for a in (2, 3) for b in (4, 5, 11, 12)])
    block = ([(0, b) for b in (4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18,
              19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 37, 38,
              49, 50, 52, 55, 59, 62, 63, 66, 69, 70, 73, 76)] + [(1, b) for b in (5, 8, 11)])
    for indices, rows, expected in ((range(4), unit, 8649772697327523432457189461277550575610520),
                                    ((0, 3, 6), block, -259979518176473365480584)):
        shifts = [(u, v) for u in indices for v in indices]
        matrix = [[1] + [values(a + u, b + v)[j] for j in range(5) for u, v in shifts]
                  for a, b in rows]
        assert len(matrix) == len(matrix[0])
        assert determinant(matrix) == expected
        print('PASS: independent original-board response determinant, rank', len(matrix))
    polynomial = ((0, 0, F(2)), (1, 0, F(-1)), (0, 1, F(3)),
                  (2, 1, F(-2)), (3, 2, F(1, 2)))
    for j in range(5):
        finite = {(a, b): values(a, b)[j] for a in range(8) for b in range(15)}
        weight = lambda a, b: F(1, 2 ** a * 3 ** b)
        full = sum((value * weight(a, b) for (a, b), value in finite.items()), F(0))
        high = sum((value * weight(a, b) for (a, b), value in finite.items() if b >= 4), F(0))
        low = sum((value * weight(a, b) for (a, b), value in finite.items() if b < 4), F(0))
        assert full == high + low
        for u in (0, 1, 3, 6):
            for v in (0, 1, 3, 6):
                shifted = sum((finite.get((a + u, b + v), 0) * weight(a, b)
                               for a in range(8) for b in range(4, 15)), F(0))
                c = sum((x * weight(a, b) for (a, b), x in finite.items() if a < u and b >= 4), F(0))
                r = sum((x * weight(a, b) for (a, b), x in finite.items() if 4 <= b < 4 + v), F(0))
                k = sum((x * weight(a, b) for (a, b), x in finite.items() if a < u and 4 <= b < 4 + v), F(0))
                assert shifted == 2 ** u * 3 ** v * (high - c - r + k)
        lhs = sum((coefficient * sum((finite.get((a + u, b + v), 0) * weight(a, b)
                   for a in range(8) for b in range(4, 15)), F(0))) for u, v, coefficient in polynomial)
        rhs = sum(coefficient * 2 ** u * 3 ** v for u, v, coefficient in polynomial) * high
        for i in range(3):
            coefficient = sum(c * 2 ** u * 3 ** v for u, v, c in polynomial if u > i)
            rhs -= F(1, 2 ** i) * coefficient * sum((F(finite.get((i, b), 0), 3 ** b) for b in range(4, 15)), F(0))
        for ell in range(2):
            coefficient = sum(c * 2 ** u * 3 ** v for u, v, c in polynomial if v > ell)
            rhs -= F(1, 3 ** (4 + ell)) * coefficient * sum((F(finite.get((a, 4 + ell), 0), 2 ** a) for a in range(8)), F(0))
        rhs += sum((c * 2 ** u * 3 ** v * sum((x * weight(a, b)
                    for (a, b), x in finite.items() if a < u and 4 <= b < 4 + v), F(0)))
                   for u, v, c in polynomial)
        assert lhs == rhs
    print('PASS: complete shifts, polynomial boundary dictionary and low-row split')


if __name__ == '__main__':
    run()
