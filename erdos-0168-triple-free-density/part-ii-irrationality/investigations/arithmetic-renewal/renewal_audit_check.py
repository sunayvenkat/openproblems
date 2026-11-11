"""Independent exact renewal audit. No project imports or infinite-case inference."""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd
from pathlib import Path
import json


ZERO, ONE = (0, 0), (1, 0)
ROOTS = (ONE, (0, 1), (-1, -1))
C = ((ZERO, ZERO, ZERO), (ZERO, ONE, (1, 1)), (ZERO, (0, -1), ONE))
WIDTH = 10000


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def sub(z, w):
    return z[0] - w[0], z[1] - w[1]


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0] - z[1] * w[1]


def rot(z, k):
    return mul(z, ROOTS[k % 3])


# Integer powers certify every logarithmic floor used by this audit.
af, bf, A, B = [0], [0], [ONE], [ONE]
two, three, alpha_power = 1, 1, 1
for k in range(1, WIDTH):
    two *= 2
    three *= 3
    f = af[-1]
    while alpha_power * 3 <= two:
        alpha_power *= 3
        f += 1
    assert alpha_power <= two < alpha_power * 3
    af.append(f)
    bf.append(three.bit_length() - 1)
    row = (ONE, (0, -1), ZERO)[f % 3]
    col = (ONE, (1, 1), ZERO)[bf[-1] % 3]
    A.append(add(A[-1], rot(row, -k)))
    B.append(add(B[-1], rot(col, -2 * k)))


def board(cutoff):
    out, power3, b = ZERO, 1, 0
    while power3 <= cutoff:
        for a in range((cutoff // power3).bit_length()):
            out = add(out, ROOTS[(a - b) % 3])
        power3 *= 3
        b += 1
    return out


def event(b):
    isolated = bf[b] - bf[b - 1] == 2
    patch = bf[b - 1] - bf[b - 3] == 4
    assert not (isolated and patch)
    return ROOTS[(bf[b] - 2 * b) % 3] if isolated else ROOTS[(bf[b - 1] - 1 - 2 * b) % 3] if patch else ZERO


@lru_cache(None)
def state(a, b):
    out = add(sub(add(A[a], B[b]), ONE), C[a % 3][b % 3])
    return sub(out, event(b)) if b >= 4 else out


def rho(z):
    return max(abs(z[1] - z[0]), abs(z[0]))


def reward(a, b):
    x, y = state(a, b)
    if b >= 4:
        return int(x <= 0 and x <= y)
    return (0, int(x >= 1 and y >= 0), int(x <= -1 and x <= y), int(min(x, 0) <= y))[b]


@lru_cache(None)
def q(a, b, r):
    depth, digits = 0, 0
    while rho(state(a + 3 * depth, b)) <= r:
        digits = 8 * digits + reward(a + 3 * depth, b)
        depth += 1
    num = 7 * digits + 1 + reward(a + 3 * depth, b)
    value = F(num, 7 * 8 ** depth)
    assert 0 <= value <= F(2, 7)
    return value, depth, num


@lru_cache(None)
def p(a, b, r):
    assert b >= 4
    depth = 0
    while rho(state(a, b + 3 * depth)) <= r:
        depth += 1
    rows = [q(a, b + 3 * m, r) for m in range(depth)]
    height = max((row[1] for row in rows), default=0)
    # Fold the defining recurrence backwards, independently of the numerator formula.
    value = F(8 + reward(a, b + 3 * depth), 182)
    for row in reversed(rows):
        value = (value + row[0]) / 27
    local_b = 8 ** height * (1 + reward(a, b + 3 * depth))
    local_b += 26 * sum(27 ** (depth - 1 - m) * 8 ** (height - row[1]) * row[2]
                        for m, row in enumerate(rows))
    num = local_b + 7 * 8 ** height
    assert value == F(num, 182 * 8 ** height * 27 ** depth)
    assert num % 13 and 0 <= value <= F(9, 182)
    return value, depth, height, local_b


def ea(a, b, r):
    out = 8 * q(a, b, r)[0] - q(a + 3, b, r)[0] - reward(a, b)
    assert out == 0 if rho(state(a, b)) <= r else F(6, 7) <= out <= F(9, 7)
    return out


def eb(a, b, r):
    out = 27 * p(a, b, r)[0] - p(a, b + 3, r)[0] - q(a, b, r)[0]
    assert out == 0 if rho(state(a, b)) <= r else F(90, 91) <= out <= F(191, 182)
    return out


def check():
    for a in range(19):
        assert A[a] == rot(board(2 ** a), -a)
    for b in range(37):
        assert B[b] == rot(board(3 ** b), -2 * b)
    for m in range(13):
        last = bf[3 * m]
        first = second = ZERO
        count = 0
        for a in range(last + 1):
            exponent = a + af[a] + int(a > 0)
            first = add(first, ROOTS[a % 3])
            second = add(second, ROOTS[exponent % 3])
            count += int(a > 0 and exponent % 3 == 0)
        assert mul((2, 1), B[3 * m]) == sub(first, rot(second, -1))
        assert 2 * second[0] - second[1] == 2 + 3 * count - last
    assert all(bf[3 * (m + 1)] - bf[3 * m] in (4, 5) for m in range(1000))
    assert state(0, 4) == ZERO
    data = json.loads(Path(__file__).with_name('renewal_source_data.json').read_text())
    expected = ((3, 3, 1, 504, 6, 10, 13, 26, 15),
                (200, 125, 32, 18, 599, 376, 91, 1202, 1097),
                (1282, 689, 1065, 468, 3844, 2068, 7, 7125, 3921))
    for r in range(3):
        highs = [(i, b, p(i, b, r)) for i in range(3) for b in (6, 4, 5)]
        lows = [(i, b, q(i, b, r)) for i in range(3) for b in range(4)]
        source = sum((F(216, 2 ** i * 3 ** b) * row[0] for i, b, row in highs), F())
        source += sum((F(8, 2 ** i * 3 ** b) * row[0] for i, b, row in lows), F())
        height = max([row[2] for _, _, row in highs] + [row[1] for _, _, row in lows])
        vertical = max(row[1] for _, _, row in highs)
        tau = q(0, 4, r)[1]
        common = 91 * 8 ** height * 27 ** (vertical + 1)
        integer = common * source
        assert integer.denominator == 1
        saving = gcd(common, integer.numerator)
        den = source.denominator
        assert den == common // saving
        h0, t0, tau0, g0, v2, v3, other, bits, lower_bits = expected[r]
        assert (height, vertical, tau, saving) == (h0, t0, tau0, g0)
        assert den == 2 ** v2 * 3 ** v3 * other and den.bit_length() == bits
        witness = F(6, 7 * 8 ** tau * 3 ** 4)
        assert common * witness == 26 * 8 ** (height - tau) * 27 ** vertical
        assert den * witness > 2 ** lower_bits
        record = data[r]
        assert (record['radius'], record['H'], record['T'], record['tau']) == (r, height, vertical, tau)
        assert record['high'] == [dict(i=i, b=b, t=row[1], H=row[2], B=str(row[3])) for i, b, row in highs]
        assert record['low'] == [dict(i=i, b=b, a=row[1], N=str(row[2])) for i, b, row in lows]
        # All nine product blocks: eB's horizontal terminal is essential.
        nn, mm = 3, 3
        for i in range(3):
            for b in (6, 4, 5):
                weighted = lambda f: sum((F(1, 8 ** n * 27 ** m) * f(i + 3 * n, b + 3 * m)
                                          for n in range(nn) for m in range(mm)), F())
                lhs = weighted(reward) + weighted(lambda a, c: ea(a, c, r))
                lhs += 8 * sum((eb(i, b + 3 * m, r) / 27 ** m for m in range(mm)), F())
                lhs -= F(8, 8 ** nn) * sum((eb(i + 3 * nn, b + 3 * m, r) / 27 ** m for m in range(mm)), F())
                rhs = 216 * (p(i, b, r)[0] - p(i + 3 * nn, b, r)[0] / 8 ** nn
                             - p(i, b + 3 * mm, r)[0] / 27 ** mm
                             + p(i + 3 * nn, b + 3 * mm, r)[0] / (8 ** nn * 27 ** mm))
                assert lhs == rhs
            for b in range(4):
                lhs = sum((F(1, 8 ** n) * (reward(i + 3 * n, b) + ea(i + 3 * n, b, r))
                           for n in range(nn)), F())
                assert lhs == 8 * (q(i, b, r)[0] - q(i + 3 * nn, b, r)[0] / 8 ** nn)
        print('PASS radius', r, 'H,T,tau,g', (height, vertical, tau, saving),
              'denominator_bits', bits, 'cleared_witness_gt_2_power', lower_bits, flush=True)
    assert F(9, 7) + 8 * F(191, 182) == F(881, 91)
    print('PASS original boards/column sums, exact integer floors, all nine/twelve sources, JSON source records, residual bounds and full finite terminals')


if __name__ == '__main__':
    check()
