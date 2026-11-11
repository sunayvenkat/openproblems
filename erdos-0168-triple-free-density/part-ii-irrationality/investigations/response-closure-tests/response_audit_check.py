"""Independent original-board/minimum-count audit; no companion imports."""
from fractions import Fraction as F


ONE, ZERO = (1, 0), (0, 0)
ROOTS = (ONE, (0, 1), (-1, -1))
STATES = ((0, 1, (0, -1)), (1, 1, ZERO),
          (2, 0, ONE), (2, 2, ONE))


def plus(z, w):
    return z[0] + w[0], z[1] + w[1]


def minus(z, w):
    return z[0] - w[0], z[1] - w[1]


def times(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c - b * d


def root_sum(indices):
    value = ZERO
    for k in indices:
        value = plus(value, ROOTS[k % 3])
    return value


def board_counts(t):
    counts = [0, 0, 0]
    b, power3 = 0, 1
    while power3 <= t:
        a, value = 0, power3
        while value <= t:
            counts[(a - b) % 3] += 1
            a, value = a + 1, value * 2
        b, power3 = b + 1, power3 * 3
    return counts


def axis_state(t, phase):
    c = board_counts(t)
    return times((c[0] - c[2], c[1] - c[2]), ROOTS[phase % 3])


def correction(a, b):
    return times(root_sum(-k for k in range(1, a + 1)),
                 root_sum(-2 * k for k in range(1, b + 1)))


def patch_vector(b):
    value = 3 ** b
    m = value.bit_length() - 1
    isolated = 3 * 2 ** m > 2 * value
    n = (value // 6).bit_length() - 1
    patch = 6 * 2 ** n <= value and 4 * value < 27 * 2 ** n
    assert not (isolated and patch)
    return ROOTS[(m - 2 * b) % 3] if isolated else (
        ROOTS[(n - 2 * b) % 3] if patch else ZERO)


def birth(z, b):
    # Minimum differences independently encode each accepted inequality.
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


def canonical(state, a, b, axes):
    p0, q0, endpoint = state
    aa, bb = axes
    gamma = ROOTS[(2 * p0 - q0) % 3]
    shifted = plus(endpoint, times(gamma, minus(aa[a], ONE)))
    shifted = plus(shifted, times(ROOTS[-q0 % 3], times(
        root_sum(2 * j for j in range(p0)),
        root_sum(-k for k in range(1, a + 1)))))
    z = minus(plus(plus(shifted, bb[b]), correction(a + q0, b)), ONE)
    if b >= 4:
        z = minus(z, patch_vector(b))
    g = -3 * (birth(z, b) - birth(minus(z, gamma), b))
    assert g in (-3, 0, 3)
    return g, z, gamma


def ray(z, gamma, b):
    x, y = z
    if b == 0:
        return 0
    if gamma == ROOTS[1]:
        test = (x >= 1 and y == 0) if b == 1 else (
            x == y and x <= -1) if b == 2 else (
            y == min(x, 0)) if b == 3 else (x == y and x <= 0)
        return -3 * int(test)
    assert gamma == ROOTS[2]
    if b == 1:
        return 3 * (int(x == 0 and y >= -1) + int(x >= 1 and y == -1))
    if b == 2:
        return -3 * int(x == -1 and y >= -1)
    if b == 3:
        return 3 * int(x >= 0 and y == -1)
    return -3 * int(x == 0 and y >= 0)


def cover(t):
    counts = board_counts(t)
    a, value = 1, 2
    while value <= t:
        if 3 * value > 2 * t or (6 * value <= t and 4 * t < 27 * value):
            counts[a % 3] -= 1
        a, value = a + 1, value * 2
    return min(counts)


def determinant(rows):
    mat, answer = [[F(x) for x in row] for row in rows], F(1)
    for k in range(len(mat)):
        pivot = next(i for i in range(k, len(mat)) if mat[i][k])
        if pivot != k:
            mat[k], mat[pivot] = mat[pivot], mat[k]
            answer = -answer
        answer *= mat[k][k]
        for i in range(k + 1, len(mat)):
            factor = mat[i][k] / mat[k][k]
            mat[i] = [x - factor * y for x, y in zip(mat[i], mat[k])]
    return answer


def grade_births(p, q, limit, sign):
    groups = {}
    for b in range(max(4, limit // q + 1)):
        for a in range(max(3, limit // p + 4)):
            effective = ((a - 1, 1) if b == 0 and a >= 1 else
                         (a - 3, 3) if b == 1 and a >= 2 else (a, b))
            if p * effective[0] + q * effective[1] <= limit:
                groups.setdefault(effective, []).append((a - b) % 3)
    counts, born = [0, 0, 0], {}
    for event in sorted(groups, key=lambda z: (p * z[0] + q * z[1], sign * z[0])):
        before = min(counts)
        for color in groups[event]:
            counts[color] += 1
        born[event] = min(counts) - before
        assert born[event] in (0, 1)
    assert born[(-1, 3)] == 0
    return born


def model_tail(a, b, p):
    return (6 * F(1, 2 ** a) * (F(3, 2) + F(3, 4 * p))
            + 6 * F(1, 3 ** b) * (F(3, 2) * (1 + F(b, p)) + F(3, 4 * p)))


def run():
    width = 24
    axes = ([axis_state(2 ** a, -a) for a in range(width)],
            [axis_state(3 ** b, -2 * b) for b in range(width)])
    representatives = ((0, 1, 0), (1, 1, 1), (2, 3, 2), (5, 8, 3))
    for p, q, index in representatives:
        endpoint = ONE
        for n in range(1, q + 1):
            endpoint = plus(endpoint, times(ROOTS[-n % 3],
                root_sum(2 * j for j in range(n * p // q + 1))))
        assert endpoint == STATES[index][2]
    for b in range(5):
        for gamma in ROOTS[1:]:
            for x in range(-6, 7):
                for y in range(-6, 7):
                    assert -3 * (birth((x, y), b) - birth(minus((x, y), gamma), b)) == ray((x, y), gamma, b)
    partials = []
    enclosure = ((F(9, 20), F(1, 2)), (-F(3, 50), -F(1, 20)),
                 (-F(11, 10), -F(1)), (F(7, 5), F(3, 2)))
    exterior = 9 * (F(1, 2 ** width) + F(1, 3 ** width))
    for state, (lo, hi) in zip(STATES, enclosure):
        value = F(0)
        for a in range(width):
            for b in range(width):
                g, z, gamma = canonical(state, a, b, axes)
                assert g == ray(z, gamma, b)
                value += F(g, 2 ** a * 3 ** b)
        assert lo < value - exterior < value + exterior < hi
        partials.append(value)
    points = ((4, 4), (4, 16), (4, 23), (5, 4), (5, 6), (5, 11))
    rows = []
    for a, b in points:
        t = 2 ** a * 3 ** b
        c = 1 - 3 * (cover(t) - cover(t - 1))
        rows.append([1, c] + [canonical(s, a, b, axes)[0] for s in STATES])
    assert abs(determinant(rows)) == 243
    for state, point in zip(STATES, ((4, 23), (5, 11), (5, 4), (4, 16))):
        assert canonical(state, *point, axes)[0] == -3
    for p, q, index in ((5, 8, 3), (12, 19, 0), (41, 65, 3), (53, 84, 2)):
        limit = p * (width - 1) + q * (width - 1) + p * q
        plus_birth, minus_birth = grade_births(p, q, limit, 1), grade_births(p, q, limit, -1)
        def difference(a, b):
            return -3 * (plus_birth.get((a, b), 0) - minus_birth.get((a, b), 0))
        value = F(0)
        for a in range(width):
            for b in range(width):
                coefficient = sum(difference(a + j * q, b - (j - 1) * p)
                                  for j in range(1, b // p + 2))
                if a < q and b < p:
                    assert coefficient == canonical(STATES[index], a, b, axes)[0]
                value += F(coefficient, 2 ** a * 3 ** b)
        a, b = min(q, width), min(p, width)
        response_bound = F(45, 2 * 2 ** a) + F(63, 2 * 3 ** b)
        assert abs(value - partials[index]) + model_tail(width, width, p) + exterior < response_bound
    print('PASS: independent board axes, four endpoint states, full response enclosures and rays')
    print('PASS: independent rational-grade coefficients and quantified quotient comparisons')
    print('PASS: six actual coefficient rows have determinant magnitude243; all high rays nonzero')


if __name__ == '__main__':
    run()
