"""Exact certificates for the two prescribed floor sides; no density decimals."""
from fractions import Fraction as F
from math import gcd
import json
from pathlib import Path


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0] - z[1]
    return z


def side(n, p, q, sign):
    k, r = divmod(n * p, q)
    return k - int(n > 0 and r == 0 and sign < 0)


def model(p, q, sign):
    assert gcd(p, q) == 1 and (p + q) % 3 and F(3, 5) < F(p, q) < F(2, 3)
    a_axis = [(1, 0)]
    b_axis = [(1, 0)]
    for a in range(1, 6 * q + 1):
        a_axis.append(add(a_axis[-1], rot(((1, 0), (0, -1), (0, 0))[side(a, p, q, sign) % 3], -a)))
    for b in range(1, 6 * p + 1):
        b_axis.append(add(b_axis[-1], rot(((1, 0), (1, 1), (0, 0))[side(b, q, p, -sign) % 3], -2 * b)))
    assert a_axis[:3 * q + 1] == a_axis[3 * q:]
    assert b_axis[:3 * p + 1] == b_axis[3 * p:]
    center = (F(1, 3), F(-1, 3)) if ((p + q) % 3 == 1) == (sign > 0) else (F(2, 3), F(1, 3))
    correction = (((0, 0), (0, 0), (0, 0)), ((0, 0), (1, 0), (1, 1)), ((0, 0), (0, -1), (1, 0)))

    def event(b):
        m = lambda k: side(k, q, p, -sign)
        isolated = m(b) - m(b - 1) == 2
        patch = m(b - 1) - m(b - 3) == 4
        assert not (isolated and patch)
        return rot((1, 0), m(b) - 2 * b) if isolated else rot((1, 0), m(b - 1) - 1 - 2 * b) if patch else (0, 0)

    def eta(a, b, color=0):
        x, y = add(add(a_axis[a % (3 * q)], b_axis[b % (3 * p)]), correction[a % 3][b % 3])
        x -= 1
        if b < 4:
            assert color == 0
            return (0 if b == 0 else 1 if b == 1 and a == 0 else int(x >= 1 and y >= 0) if b == 1
                    else int(x <= -1 and x - y <= 0) if b == 2 else int(min(x, 0) <= y))
        e = event(b)
        z = add((x - e[0], y - e[1]), (-center[0], -center[1]))
        x, y = add(center, rot(z, color))
        assert x.denominator == y.denominator == 1
        return int(x <= 0 and x - y <= 0)

    horizontal = 1 - F(1, 2 ** (3 * q))
    vertical = 1 - F(1, 3 ** (3 * p))
    # Remove the exceptional origin digit before periodic horizontal summation.
    head = sum((F(1 - 3 * (eta(a, b) if (a, b) != (0, 1) else 0), 2 ** a * 3 ** b)
                for a in range(3 * q) for b in range(4)), F(0))
    tile = sum((F(1 - 3 * eta(a, b + 4), 2 ** a * 3 ** b) for a in range(3 * q) for b in range(3 * p)), F(0))
    value = head / horizontal + tile / (81 * horizontal * vertical) - 1
    return a_axis, b_axis, event, eta, value


def rank(rows):
    basis = {}
    for raw in rows:
        row = list(map(F, raw))
        for pivot, known in sorted(basis.items()):
            factor = row[pivot]
            row = [a - factor * b for a, b in zip(row, known)]
        pivot = next((i for i, v in enumerate(row) if v), None)
        if pivot is not None:
            factor = row[pivot]
            basis[pivot] = [v / factor for v in row]
    return len(basis)


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0] - z[1] * w[1]


def divide(z, w):
    conjugate = w[0] - w[1], -w[1]
    norm = mul(w, conjugate)
    assert norm[0] != 0 and norm[1] == 0
    numerator = mul(z, conjugate)
    return F(numerator[0], norm[0]), F(numerator[1], norm[0])


def eisenstein_basis(rows):
    basis, selected = {}, []
    for label, raw in rows:
        row = list(raw)
        for pivot, known in sorted(basis.items()):
            factor = row[pivot]
            row = [add(a, tuple(-v for v in mul(factor, b))) for a, b in zip(row, known)]
        pivot = next((i for i, v in enumerate(row) if v != (0, 0)), None)
        if pivot is not None:
            factor = row[pivot]
            basis[pivot] = [divide(v, factor) for v in row]
            selected.append((label, raw))
            if len(basis) == len(row):
                return selected
    return selected


def root_rows(p, q, models, axis, root):
    for a in range(q):
        for b in range(4, 4 + p):
            row = []
            for m in models:
                for color in (0, 1):
                    v = (0, 0)
                    for i in range(3):
                        for j in range(3):
                            power = i if axis == 'h' else j
                            other = j if axis == 'h' else i
                            scalar = (1 - 3 * m[3](a + i * q, b + j * p, color)) * 2 ** other
                            v = add(v, rot((scalar, 0), power) if root == 'omega' else (scalar, 0))
                    row.append(v)
            yield (a, b), row


if __name__ == '__main__':
    # Independent checks for the only coordinate and elimination primitives.
    assert rot((0, 1), 1) == (-1, -1) and rot((7, -2), 3) == (7, -2)
    assert rank([(1, 2, 3), (2, 4, 6), (0, 1, 1)]) == 2
    assert mul((0, 1), (0, 1)) == (-1, -1)
    assert divide((1, 0), (1, -1)) == (F(2, 3), F(1, 3))
    p, q = 5, 8
    plus, minus = model(p, q, 1), model(p, q, -1)
    rho = 2 * p - q
    for a in range(6 * q + 1):
        delta = tuple(sum(rot((1, 0), k * rho)[j] for k in range(1, a // q + 1)) for j in range(2))
        assert plus[0][a] == add(minus[0][a], delta)
    for b in range(6 * p + 1):
        delta = tuple(-sum(rot((1, 0), -k * rho)[j] for k in range(1, b // p + 1)) for j in range(2))
        assert plus[1][b] == add(minus[1][b], delta)
    for b in range(4, 6 * p + 1):
        k, r = divmod(b, p)
        delta = rot((-1, 0), -k * rho) if r == 0 else rot((-2, -1), -k * rho) if r == 1 else rot((-1, -1), -k * rho) if r == 3 else (0, 0)
        assert plus[2](b) == add(minus[2](b), delta)
    vec = lambda a, b: tuple(1 - 3 * m[3](a, b, color) for m in (plus, minus) for color in (0, 1))
    data = [vec(a, b) for a in range(3 * q) for b in range(4, 4 + 3 * p)]
    h_sum = [tuple(sum(vec(a + i * q, b)[j] for i in range(3)) for j in range(4)) for a in range(q) for b in range(4, 4 + 3 * p)]
    h_period = [tuple(vec(a + q, b)[j] - vec(a, b)[j] for j in range(4)) for a in range(2 * q) for b in range(4, 4 + 3 * p)]
    v_sum = [tuple(sum(vec(a, b + i * p)[j] for i in range(3)) for j in range(4)) for a in range(3 * q) for b in range(4, 4 + p)]
    v_period = [tuple(vec(a, b + p)[j] - vec(a, b)[j] for j in range(4)) for a in range(3 * q) for b in range(4, 4 + 2 * p)]
    ranks = tuple(map(rank, (data, h_sum, h_period, v_sum, v_period)))
    print('5/8 ranks: full, horizontal sum/period, vertical sum/period =', ranks)
    assert ranks == (4, 4, 4, 4, 4)
    for axis in ('h', 'v'):
        for root in ('1', 'omega'):
            basis = eisenstein_basis(root_rows(p, q, (plus, minus), axis, root))
            assert len(basis) == 4
            print('5/8 pole basis', axis, root, ':', basis)
    first = next((a, b) for a in range(3 * q) for b in range(4) if plus[3](a, b) != minus[3](a, b))
    print('5/8 first differing digit in lexicographic low-column scan:', first)
    for p, q in ((5, 8), (53, 84)):
        plus, minus = model(p, q, 1), model(p, q, -1)
        d = 27 * (2 ** (3 * q) - 1) * (3 ** (3 * p) - 1)
        values = (plus[4], minus[4], (plus[4] + minus[4]) / 2, plus[4] - minus[4])
        assert all((d * value).denominator <= 2 for value in values)
        rows = json.loads((Path(__file__).resolve().parents[1] / 'Erdos augmentation and return attacks/returns_check.json').read_text())
        saved = next(row for row in rows if (row['p'], row['q']) == (p, q))
        assert (plus[4] if 2 ** q > 3 ** p else minus[4]) == F(saved['rational_model'])
        n_diff = d * (plus[4] - minus[4])
        assert n_diff.denominator == 1 and n_diff.numerator % (2 ** q - 3 ** p) == 0
        # Independently test the finite numerator's binomial divisibility by grading.
        graded = {}
        for a in range(3 * q):
            for b in range(3 * p + 4):
                delta = lambda k: -3 * (plus[3](a, k) - minus[3](a, k)) if k >= 0 else 0
                coefficient = delta(b) - delta(b - 3 * p)
                grade = p * a + q * b
                graded[grade] = graded.get(grade, 0) + coefficient
        assert not any(graded.values())
        print((p, q), 'PASS: full formal numerator divisible by x^q-y^p; scalar Ndiff divisible by u-v')
        print((p, q), 'nominal/reduced denominator (plus, minus, mean, difference) =', tuple(F(d, value.denominator) for value in values))
        candidates = {(a, b) for a in range(q, q + 4) for b in range(4)} | {(a, b) for a in range(4) for b in range(p, p + 4)}
        first = min((2 ** a * 3 ** b, a, b, plus[3](a, b), minus[3](a, b)) for a, b in candidates if plus[3](a, b) != minus[3](a, b))
        assert first[0] < min(16 * 2 ** q, 16 * 3 ** p)
        assert first[1:] == ((0, 6, 1, 0) if (p, q) == (5, 8) else (85, 1, 1, 0))
        print((p, q), 'first differing digit by physical weight (a,b,plus,minus) =', first[1:])
        if (p, q) == (53, 84):
            for axis in ('h', 'v'):
                for root in ('1', 'omega'):
                    basis = eisenstein_basis(root_rows(p, q, (plus, minus), axis, root))
                    assert len(basis) == 4
                    print('53/84 pole basis', axis, root, ':', basis)
