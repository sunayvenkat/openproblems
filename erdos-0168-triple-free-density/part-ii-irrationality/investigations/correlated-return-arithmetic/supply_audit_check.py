"""Independent exact reconstruction of resonant jumps and avoidance states."""
from fractions import Fraction as F


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def sub(z, w):
    return z[0] - w[0], z[1] - w[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c - b * d


def omega(k):
    return ((1, 0), (0, 1), (-1, -1))[k % 3]


def divide(z, w):
    c, d = w
    norm = c * c - c * d + d * d
    a, b = mul(z, (c - d, -d))
    assert norm and a % norm == b % norm == 0
    return a // norm, b // norm


def transform(p, q):
    counts = [0, 0, 0]
    for a in range(q):
        counts[(a + p * a // q) % 3] += 1
    return counts[0] - counts[2], counts[1] - counts[2]


def floor_alpha(n):
    value, power, exponent = 2 ** n, 1, 0
    while power * 3 <= value:
        power *= 3
        exponent += 1
    return exponent


def floor_beta(n):
    return (3 ** n).bit_length() - 1


def board_imbalance(cutoff):
    counts, b, power = [0, 0, 0], 0, 1
    while power <= cutoff:
        last = (cutoff // power).bit_length() - 1
        for color in range(3):
            counts[color] += max(0, (last - (b + color) % 3) // 3 + 1)
        b, power = b + 1, power * 3
    return counts[0] - counts[2], counts[1] - counts[2]


def color_correction(a, b):
    x, y = mul(sub((1, 0), omega(-a)), sub((1, 0), omega(-2 * b)))
    assert x % 3 == y % 3 == 0
    return x // 3, y // 3


def row_birth(z, b):
    """Minimum differences, independent of the companion inequality tests."""
    x, y = z
    if b == 0:
        return 0
    if b == 1:
        return min(x - 1, y, 0) - min(x - 1, y, -1)
    if b == 2:
        return min(x, y, -1) - min(x - 1, y, -1)
    if b == 3:
        return 1 - (min(x, y + 1, 0) - min(x, y, 0))
    return min(x, y, 0) - min(x - 1, y, 0)


def response_rectangle(pr, qr, width):
    # Original colored boards construct both actual axes without their recurrences.
    aa = [mul(omega(-a), board_imbalance(2 ** a)) for a in range(width)]
    bb = [mul(omega(b), board_imbalance(3 ** b)) for b in range(width)]
    shifted = [(1, 0)]
    for a in range(1, width):
        roots = (0, 0)
        for j in range(pr + floor_alpha(a) + 1):
            roots = add(roots, omega(2 * j))
        shifted.append(add(shifted[-1], mul(omega(-qr - a), roots)))
    offsets = ((0, 0), (1, 0), (0, -1)) if (pr, qr) == (1, 2) else (
        (0, 0), (1, 1), (1, 0))
    data = {}
    for b in range(width):
        event = (0, 0)
        if b >= 4:
            isolate = floor_beta(b) - floor_beta(b - 1) == 2
            patch = floor_beta(b - 1) - floor_beta(b - 3) == 4
            assert not (isolate and patch)
            if isolate:
                event = omega(floor_beta(b) - 2 * b)
            if patch:
                event = omega(floor_beta(b - 1) - 1 - 2 * b)
        for a in range(width):
            original = sub(add(add(aa[a], bb[b]), color_correction(a, b)), add((1, 0), event))
            plus = sub(add(add(shifted[a], bb[b]), color_correction(a + qr, b)), add((1, 0), event))
            assert plus == add(original, offsets[(a - b) % 3])
            data[a, b] = -3 * (row_birth(plus, b) - row_birth(sub(plus, (1, 0)), b))
    value = sum((F(c, 2 ** a * 3 ** b) for (a, b), c in data.items()), F(0))
    return data, value


def grade_rectangle(p, q, width):
    """Original tokens, retimed once, grouped by actual simultaneous arrivals."""
    maximum = p * (q + width - 1) + q * (width - 1)
    events = {}
    for b in range(maximum // q + 2):
        for a in range(maximum // p + 4):
            A, B = a, b
            if b == 0 and a >= 1:
                A, B = a - 1, 1
            elif b == 1 and a >= 2:
                A, B = a - 3, 3
            g = p * A + q * B
            if g <= maximum:
                events.setdefault((g, A, B), []).append((a - b) % 3)
    born = []
    for sign in (1, -1):
        counts, table = [0, 0, 0], {}
        for grade, a, b in sorted(events, key=lambda row: (row[0], sign * row[1])):
            before = min(counts)
            for color in events[grade, a, b]:
                counts[color] += 1
            table[a, b] = min(counts) - before
        assert table[-1, 3] == 0
        assert all((q + a, b) in table for a in range(width) for b in range(1, width))
        born.append(table)
    # Dyadic tokens have moved to row one, leaving no row-zero birth here.
    return {(a, b): -3 * (born[0].get((q + a, b), 0) - born[1].get((q + a, b), 0))
            for a in range(width) for b in range(width)}


def variation(p, q, r, s):
    assert abs(p * s - r * q) == 1
    A, B = q + s, p + r
    return 9 * (F(2, 2 ** A) * (1 + F(A + 1, q * s))
                + F(1, 3 ** B) * (F(3, 2) + F(6 * B + 3, 4 * p * r)))


def actual_cf():
    def log_interval(a):
        x, terms = F(a - 1, a + 1), 50
        value = 2 * sum((x ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), F(0))
        tail = 2 * x ** (2 * terms + 1) / ((2 * terms + 1) * (1 - x * x))
        return value, value + tail
    l2, u2 = log_interval(2)
    l3, u3 = log_interval(3)
    lo, hi = l2 / u3, u2 / l3
    previous, current, result = (0, 1), (1, 0), []
    for _ in range(11):
        digit = lo.numerator // lo.denominator
        assert digit == hi.numerator // hi.denominator
        previous, current = current, (digit * current[0] + previous[0], digit * current[1] + previous[1])
        result.append(current)
        lo, hi = 1 / (hi - digit), 1 / (lo - digit)
    return result


def state_checks():
    initial = ((2, 2), (0, 1), 0)
    assert transform(5, 8) == (2, 0) and transform(12, 19) == (1, 0)
    assert sub(mul(sub((1, 0), omega(31)), transform(5, 8)),
               mul(sub((1, 0), omega(13)), transform(12, 19))) == (1, -1)
    seen, todo = {initial}, [initial]
    while todo:
        u, v, k = todo.pop()
        med = ((u[0] + v[0]) % 3, (u[1] + v[1]) % 3)
        for nxt in ((med, v, k), (u, med, (k + sum(u)) % 3)):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    assert len(seen) == 24
    balanced = {(0, 1): (1, 0), (1, 1): (1, 0), (2, 0): (2, 1), (2, 2): (2, 0)}
    oriented, rows, resonant = 0, 0, []
    for u, v, k in seen:
        x, y, C = omega(sum(u)), omega(sum(v)), mul(omega(k), (1, -1))
        med = ((u[0] + v[0]) % 3, (u[1] + v[1]) % 3)
        if med in balanced:
            h = balanced[med]
            hv = divide(sub(mul(sub((1, 0), y), h), C), sub((1, 0), mul(x, y)))
            hu = sub(h, mul(x, hv))
            assert sub(mul(sub((1, 0), y), hu), mul(sub((1, 0), x), hv)) == C
            rows += 1
            oriented += int(sum(u) % 3 != 0) + int(sum(v) % 3 != 0)
        if sum(med) % 3 == 0:
            assert x != (1, 0) and y != (1, 0) and mul(x, y) == (1, 0)
            h = divide(mul((-1, 0), mul(x, C)), sub((1, 0), x))
            resonant.append((med, h))
    assert (rows, oriented, len(resonant)) == (12, 16, 6)
    assert set(resonant) == {((1, 2), (1, 1)), ((2, 1), (1, 0))}
    traces = {(3, 3): ((2, 2, (2, 0)), (0, 1, (1, 0))),
              (2, 1, 1, 2, 1, 1): ((2, 1, (1, 0)), (2, 2, (2, 0)),
                                    (1, 0, (3, 0)), (1, 2, (1, 1)),
                                    (2, 2, (2, 0)), (0, 1, (1, 0)))}
    for block in ((3, 3), (2, 1, 1, 2, 1, 1), (3, 3, 2, 1, 1, 2, 1, 1),
                  (2, 1, 1, 2, 1, 1, 3, 3), (2, 1, 1, 2, 1, 1) * 2):
        old, cur = (5, 8), (12, 19)
        trace = []
        for digit in block:
            old, cur = cur, (digit * cur[0] + old[0], digit * cur[1] + old[1])
            assert (sum(old) + sum(cur)) % 3
            if block in traces:
                trace.append((cur[0] % 3, cur[1] % 3, transform(*cur)))
        if block in traces:
            assert tuple(trace) == traces[block]
        assert tuple(v % 3 for v in old) == (2, 2) and transform(*old) == (2, 0)
        assert tuple(v % 3 for v in cur) == (0, 1) and transform(*cur) == (1, 0)
        assert len(block) % 2 == 0
    for block, expected in (((3, 3), (1, 3, 3, 10)), ((2, 1, 1, 2, 1, 1), (7, 12, 18, 31))):
        a, b, c, d = 1, 0, 0, 1
        for digit in block:
            a, b, c, d = b, a + b * digit, d, c + d * digit
        assert (a, b, c, d) == expected and a * d - b * c == 1
    assert F(12, 31) - F(4, 13) == F(32, 403)
    assert 49 ** 2 == 2401 < 2 ** 12
    print('STATE_COUNTS', rows, oriented, len(resonant), 'FULL_LOOPS_AND_CANTOR_CONSTANTS_PASS')


def check():
    for q in range(2, 35):
        for old in range(1, q):
            for digit in range(1, 10):
                assert (digit * q + old - 5 * q > 0) == (digit >= 5)
    state_checks()
    values = {}
    tail = F(27, 2 * 2 ** 32) + F(45, 2 * 3 ** 32)
    for p, q, bounds in ((94, 149, (F(77, 100), F(79, 100))), (65, 103, (-F(11, 20), -F(27, 50)))):
        assert transform(p, q) == ((1, 1) if p % 3 == 1 else (1, 0))
        for a in range(1, 32):
            assert p * a // q == floor_alpha(a) and q * a // p == floor_beta(a)
        data, value = response_rectangle(p % 3, q % 3, 32)
        assert data == grade_rectangle(p, q, 32)
        assert bounds[0] < value - tail < value + tail < bounds[1]
        values[p, q] = value
        print('FULL_ORIGINAL_TOKEN_RECTANGLE', p, q, 'MATCHES_ALL_1024_COEFFICIENTS')
    prefix = actual_cf()
    index = prefix.index((41, 65))
    assert prefix[index + 1] == (53, 84)
    remainder = variation(41, 65, 94, 149) + variation(94, 149, 53, 84)
    lower = abs(F(1, 2 ** 149) - F(1, 3 ** 94)) * (abs(values[94, 149]) - tail)
    assert lower > remainder
    print('ACTUAL_RESONANT_MEDIANT_94_149_DOMINANCE_RATIO_GT', lower // remainder)
    print('PASS: independent full resonant response, CF, cylinders, loops and threshold')


if __name__ == '__main__':
    check()
