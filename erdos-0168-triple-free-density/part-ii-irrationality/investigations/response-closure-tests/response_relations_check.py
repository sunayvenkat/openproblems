"""Exact actual-axis response arrays and a narrowly scoped closure test."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def sub(z, w):
    return z[0] - w[0], z[1] - w[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0] - z[1]
    return z


def floor_alpha(n):
    return _floor_power(2 ** n, 3)


def _floor_power(value, base):
    power, result = 1, 0
    while power * base <= value:
        power *= base
        result += 1
    return result


def floor_beta(n):
    return (3 ** n).bit_length() - 1


def axes(width):
    aa, bb = [(1, 0)], [(1, 0)]
    for n in range(1, width):
        aa.append(add(aa[-1], rot(((1, 0), (0, -1), (0, 0))[floor_alpha(n) % 3], -n)))
        bb.append(add(bb[-1], rot(((1, 0), (1, 1), (0, 0))[floor_beta(n) % 3], -2 * n)))
    return aa, bb


STATES = ((0, 1, (0, -1)), (1, 1, (0, 0)), (2, 0, (1, 0)), (2, 2, (1, 0)))
CORRECTION = (((0, 0), (0, 0), (0, 0)),
              ((0, 0), (1, 0), (1, 1)),
              ((0, 0), (0, -1), (1, 0)))


def low_eta(z, b):
    x, y = z
    return (0 if b == 0 else int(x >= 1 and y >= 0) if b == 1
            else int(x <= -1 and x - y <= 0) if b == 2
            else int(min(x, 0) <= y))


def event(b):
    isolated = floor_beta(b) - floor_beta(b - 1) == 2
    patch = floor_beta(b - 1) - floor_beta(b - 3) == 4
    assert not (isolated and patch)
    return (rot((1, 0), floor_beta(b) - 2 * b) if isolated else
            rot((1, 0), floor_beta(b - 1) - 1 - 2 * b) if patch else (0, 0))


def response(state, a, b, aa, bb):
    pr, qr, endpoint = state
    gamma = (2 * pr - qr) % 3
    pminus = ((0, 0), (-1, -1), (-1, 0))[a % 3]  # sum_(k=1)^a omega^(-k)
    sm = ((0, 0), (1, 0), (0, -1))[pr]
    residue_term = rot((sm[0] * pminus[0] - sm[1] * pminus[1],
                        sm[0] * pminus[1] + sm[1] * pminus[0] - sm[1] * pminus[1]), -qr)
    shifted = add(add(endpoint, rot(sub(aa[a], (1, 0)), gamma)), residue_term)
    z = add(add(shifted, bb[b]), CORRECTION[(a + qr) % 3][b % 3])
    z = sub(z, (1, 0))
    if b >= 4:
        z = sub(z, event(b))
    minus = sub(z, rot((1, 0), gamma))
    birth = lambda v: int(v[0] <= 0 and v[0] - v[1] <= 0) if b >= 4 else low_eta(v, b)
    return -3 * (birth(z) - birth(minus)), z, gamma


def ray_response(z, gamma, b):
    x, y = z
    if b == 0:
        return 0
    if gamma == 1:
        hit = (x >= 1 and y == 0) if b == 1 else (x == y and x <= -1) if b == 2 else (y == min(x, 0)) if b == 3 else (x == y and x <= 0)
        return -3 * int(hit)
    assert gamma == 2
    if b == 1:
        return 3 * (int(x == 0 and y >= -1) + int(x >= 1 and y == -1))
    if b == 2:
        return -3 * int(x == -1 and y >= -1)
    if b == 3:
        return 3 * int(x >= 0 and y == -1)
    return -3 * int(x == 0 and y >= 0)


def tau(clock):
    counts = [0, 0, 0]
    j, p3 = 0, 1
    while 2 * p3 <= clock:
        i, value = 0, p3
        while 2 * value <= clock:
            counts[(i - j) % 3] += 1
            i, value = i + 1, value * 2
        j, p3 = j + 1, p3 * 3
    a, root = 1, 2
    while 2 * root <= clock:
        if 3 * root > clock or (12 * root <= clock and 2 * clock < 27 * root):
            counts[a % 3] -= 1
        a, root = a + 1, root * 2
    return min(counts)


def original_c(a, b):
    clock = 2 ** (a + 1) * 3 ** b
    return 1 - 3 * (tau(clock) - tau(clock - 1))


def basis_rows(rows):
    basis, selected = {}, []
    for label, raw in rows:
        row = list(map(F, raw))
        for pivot, known in sorted(basis.items()):
            factor = row[pivot]
            row = [x - factor * y for x, y in zip(row, known)]
        pivot = next((j for j, value in enumerate(row) if value), None)
        if pivot is not None:
            factor = row[pivot]
            basis[pivot] = [x / factor for x in row]
            selected.append((label, raw))
            if len(basis) == len(row):
                return selected
    return selected


def determinant(rows):
    matrix = [list(map(F, row)) for row in rows]
    result = F(1)
    for column in range(len(matrix)):
        pivot = next(i for i in range(column, len(matrix)) if matrix[i][column])
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            result = -result
        value = matrix[column][column]
        result *= value
        for i in range(column + 1, len(matrix)):
            ratio = matrix[i][column] / value
            matrix[i] = [x - ratio * y for x, y in zip(matrix[i], matrix[column])]
    return result


def run():
    width = 96
    aa, bb = axes(width)
    # These are cone identities on all integer cells, not orbit extrapolations.
    for b in (0, 1, 2, 3, 4):
        for gamma in (1, 2):
            for x in range(-5, 6):
                for y in range(-5, 6):
                    z = x, y
                    minus = sub(z, rot((1, 0), gamma))
                    birth = lambda v: int(v[0] <= 0 and v[0] - v[1] <= 0) if b >= 4 else low_eta(v, b)
                    assert ray_response(z, gamma, b) == -3 * (birth(z) - birth(minus))
    for state in STATES:
        for a in range(width):
            for b in range(width):
                value, z, gamma = response(state, a, b, aa, bb)
                assert value == ray_response(z, gamma, b)
    path = Path(__file__).resolve().parents[1] / 'Erdos 168 signed arithmetic returns/signed_scalar_check.py'
    spec = importlib.util.spec_from_file_location('archived_scalar', path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    transforms = ((1, 0), (1, 0), (2, 1), (2, 0))
    for state, transform in zip(STATES, transforms):
        exact = sum((F(response(state, a, b, aa, bb)[0], 2 ** a * 3 ** b)
                     for a in range(width) for b in range(width)), F(0))
        assert exact == old.limiting_response(state[0], state[1], transform, width)[1]
    points = ((4, 4), (4, 16), (4, 23), (5, 4), (5, 6), (5, 11))
    expected = ([1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, -3],
                [1, 1, -3, 0, 0, -3], [1, 1, 0, 0, -3, 0],
                [1, -2, 0, 0, 0, 0], [1, 1, 0, -3, 0, 0])
    rows = [(point, [1, original_c(*point)] +
             [response(state, *point, aa, bb)[0] for state in STATES]) for point in points]
    assert tuple(row for _, row in rows) == expected
    selected = basis_rows(rows)
    assert len(selected) == 6
    assert abs(determinant(expected)) == 243
    print('PASS: six actual high-row rows have rank six (determinant magnitude243)')
    partials = []
    bounds = ((F(9, 20), F(1, 2)), (-F(3, 50), -F(1, 20)),
              (-F(11, 10), -F(1)), (F(7, 5), F(3, 2)))
    exterior = 9 * (F(1, 2 ** width) + F(1, 3 ** width))
    for state, (lo, hi) in zip(STATES, bounds):
        low = sum((F(response(state, a, b, aa, bb)[0], 2 ** a * 3 ** b)
                   for a in range(width) for b in range(4)), F(0))
        high = sum((F(response(state, a, b, aa, bb)[0], 2 ** a * 3 ** b)
                    for a in range(width) for b in range(4, width)), F(0))
        assert high < 0
        partials.append(low + high)
        assert lo < low + high - exterior < low + high + exterior < hi
    path = Path(__file__).resolve().parents[1] / 'Erdos 168 reflected return models/two_sided_models_check.py'
    spec = importlib.util.spec_from_file_location('archived_models', path)
    models = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(models)
    for p, q, index in ((5, 8, 3), (12, 19, 0), (41, 65, 3), (53, 84, 2)):
        plus, minus = models.model(p, q, 1), models.model(p, q, -1)
        quotient = (plus[4] - minus[4]) / (F(1, 2 ** q) - F(1, 3 ** p))
        a_count, b_count = min(q, width), min(p, width)
        for a in range(a_count):
            for b in range(b_count):
                assert response(STATES[index], a, b, aa, bb)[0] == -3 * (plus[3](q + a, b) - minus[3](q + a, b))
        error = F(45, 2 * 2 ** a_count) + F(63, 2 * 3 ** b_count)
        assert abs(quotient - partials[index]) <= error + exterior
    print('PASS: four full rational quotients satisfy the fixed-response error bound')
    print('PASS: limiting coefficients, complete enclosures and exact ray dictionary')


if __name__ == '__main__':
    run()
