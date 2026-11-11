"""Exact signed boundary classification and adjacent toric certificates."""

from fractions import Fraction as F
from functools import cache


def plus(*polys):
    result = {}
    for poly in polys:
        for power, coefficient in poly.items():
            result[power] = result.get(power, 0) + coefficient
    return {power: c for power, c in result.items() if c}


def times(P, Q):
    return plus(*({(a + aa, b + bb): c * cc}
                  for (a, b), c in P.items() for (aa, bb), cc in Q.items()))


def shift(P, a, b):
    return {(aa + a, bb + b): c for (aa, bb), c in P.items()}


def scale(P, c):
    return {power: c * value for power, value in P.items() if c * value}


def L(p, q):
    return {(2 * q, 0): 1, (q, p): 1, (0, 2 * p): 1}


def unit(a, b):
    return F(2) ** a * F(3) ** b


def evaluate(P):
    return sum((c * unit(a, b) for (a, b), c in P.items()), F())


def kernel(P, a, b):
    return sum((c * unit(aa - a, bb - b)
                for (aa, bb), c in P.items() if a < aa or b < bb), F())


Q_test = {(0, 0): 2, (2, 1): -3, (1, 3): 1}
test = plus({(0, 0): 7}, times({(1, 1): 1, (1, 0): -3,
                               (0, 1): -2, (0, 0): 6}, Q_test))
test_d = {(a, b): (2 * a + b) % 5 - 2 for a in range(9) for b in range(9)}
assert evaluate(test) == 7
assert sum(c * kernel(test, a, b) for (a, b), c in test_d.items()) == -6 * sum(
    c * test_d[a, b] for (a, b), c in Q_test.items())


P0 = {(3, 3): -1, (3, 0): 27, (0, 3): 8, (0, 0): -34}
assert evaluate(P0) == 182
for a in range(9):
    for b in range(9):
        assert kernel(P0, a, b) == (216 * unit(-a, -b) if a < 3 and b < 3 else 0)


def inverse_certificate(p, q, r, s, old_count, new_count):
    """Telescope a balanced word of U^3 and V^-3, with qr-ps=1."""
    assert q * r - p * s == 1
    total = old_count + new_count
    old, new = {}, {}
    a = b = 0
    for t in range(total):
        if (t + 1) * old_count // total > t * old_count // total:
            old = plus(old, {(a + q, b - 3 * p): 1, (a, b - 2 * p): -1})
            a, b = a + 3 * q, b - 3 * p
        else:
            new = plus(new, {(a - 2 * s, b): -1, (a - 3 * s, b + r): 1})
            a, b = a - 3 * s, b + 3 * r
    target = plus({(a, b): 1}, {(0, 0): -1})
    assert plus(times(old, L(p, q)), times(new, L(r, s))) == target
    return old, new, (a, b)


for p, q, r, s in ((5, 8, 12, 19), (41, 65, 12, 19), (306, 485, 53, 84)):
    assert q >= 3 and r >= 3 and q * r - p * s == 1
    ceil = lambda value: -((-value.numerator) // value.denominator)
    # Exact valuation lower bounds; the note proves their algebraic-root origin.
    assert max(2 * p, ceil(F(2 * s * p, q))) == 2 * max(p, r)
    assert max(2 * s, ceil(F(2 * p * s, r))) == 2 * max(q, s)
    mandatory = 2 ** (2 * max(q, s)) * 3 ** (2 * max(p, r))
    Ax, Bx, end_x = inverse_certificate(p, q, r, s, r, p)
    Ay, By, end_y = inverse_certificate(p, q, r, s, s, q)
    assert end_x == (3, 0) and end_y == (0, 3)
    factor = {(0, 0): 27, (0, 3): -1}
    A, B = plus(times(factor, Ax), scale(Ay, 7)), plus(times(factor, Bx), scale(By, 7))
    assert plus(times(A, L(p, q)), times(B, L(r, s))) == P0
    support = list(A) + list(B)
    a_min, a_max = min(a for a, b in support), max(a for a, b in support)
    b_min, b_max = min(b for a, b in support), max(b for a, b in support)
    assert a_max - a_min <= 6 * (q + s) and b_max - b_min <= 6 * (p + r)
    M, N = max(0, -a_min), max(0, -b_min)
    assert min(a for a, b in shift(A, M, N)) >= 0
    assert min(b for a, b in shift(A, M, N)) >= 0
    assert min(a for a, b in shift(B, M, N)) >= 0
    assert min(b for a, b in shift(B, M, N)) >= 0
    translated = shift(P0, M, N)
    assert evaluate(translated) == 182 * 2 ** M * 3 ** N
    assert M or N
    # A cleared shift of P0 has infinite sides, unlike P0 itself.
    assert any(kernel(translated, a, 3 + N) for a in range(3 + M))
    print({'pair': ((p, q), (r, s)), 'terms': len(A) + len(B),
           'support': (a_min, a_max, b_min, b_max),
           'quadrant_shift': (M, N),
           'translated_factor_bits': int(evaluate(translated)).bit_length(),
           'mandatory_finite_boundary_factor_bits': mandatory.bit_length()})


@cache
def tau(t):
    counts = [0, 0, 0]
    two, a = 1, 0
    while two <= t:
        three, b = 1, 0
        while two * three <= t:
            counts[(a - b) % 3] += 1
            three *= 3
            b += 1
        two *= 2
        a += 1
    root, a = 2, 1
    while root <= t:
        if 2 * t < 3 * root or 6 * root <= t and 4 * t < 27 * root:
            counts[a % 3] -= 1
        root *= 2
        a += 1
    return min(counts)


@cache
def actual_d(a, b):
    value = 2 ** a * 3 ** (b + 4)
    digit = 1 - 3 * (tau(value) - tau(value - 1))
    assert digit in (1, -2)
    return digit


A_cut, B_cut = 28, 20
head = sum((F(actual_d(a, b), 2 ** a * 3 ** b)
            for a in range(A_cut) for b in range(B_cut)), F())
corner = 216 * sum((F(actual_d(a, b), 2 ** a * 3 ** b)
                   for a in range(3) for b in range(3)), F())
assert corner.denominator == 1
outside = F(1, 2 ** A_cut) + F(1, 3 ** B_cut) - F(1, 2 ** A_cut * 3 ** B_cut)
low, high = 182 * (head - 6 * outside) - corner, 182 * (head + 3 * outside) - corner
assert high < 0 or low > 0
floor_low = (1024 * low).numerator // (1024 * low).denominator
ceil_high = -((-1024 * high).numerator // (-1024 * high).denominator)
assert F(floor_low, 1024) < low and high < F(ceil_high, 1024)
print({'fixed_corner': str(corner), '1024_R0_strict_bounds': (floor_low, ceil_high)})
print('PASS: signed finite boundaries, balanced Laurent certificates, actual fixed residual.')
