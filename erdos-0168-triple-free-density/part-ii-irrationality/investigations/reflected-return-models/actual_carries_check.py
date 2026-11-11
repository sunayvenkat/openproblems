"""Exact narrow certificate for the actual 2x2 birth language and carry audit."""
from fractions import Fraction
from itertools import combinations, product


ZERO = (0, 0)
W = ((1, 0), (0, 1), (-1, -1))


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def neg(z):
    return -z[0], -z[1]


def mul(z, w):
    x, y = z
    s, t = w
    return x*s - y*t, x*t + y*s - y*t


def cone(z):
    return int(z[0] <= 0 and z[0] - z[1] <= 0)


def direct_q(t, counts):
    correction = [0, 0, 0]
    for exponent in range(1, t.bit_length()):
        root = 2**exponent
        if 2*t < 3*root <= 3*t or 6*root <= t and 4*t < 27*root:
            correction[exponent % 3] += 1
    assert sum(correction) <= 1
    return tuple(counts[j] - correction[j] for j in range(3))


def row_q(t):
    counts = [0, 0, 0]
    power3 = 1
    b = 0
    while power3 <= t:
        width = (t // power3).bit_length() - 1
        for j in range(3):
            first = (j + b) % 3
            if first <= width:
                counts[j] += (width - first) // 3 + 1
        b += 1
        power3 *= 3
    top = t.bit_length() - 1
    correction = [0, 0, 0]
    if top >= 1 and 2*t < 3*2**top:
        correction[top % 3] = 1
    elif top >= 3 and 16*t < 27*2**top:
        correction[(top - 2) % 3] = 1
    return tuple(counts[j] - correction[j] for j in range(3))


# The first method updates a sorted smooth prefix and tests every exceptional
# root. The second counts complete exponent rows and uses mantissa intervals.
limit = 6 * 2**13 * 3**25
points = sorted((2**a * 3**b, a, b)
                for a in range(limit.bit_length())
                for b in range(limit.bit_length())
                if 2**a * 3**b <= limit)
counts = [0, 0, 0]
eta, state, optima = {}, {}, {}
previous = 0
for t, a, b in points:
    counts[(a-b) % 3] += 1
    q = direct_q(t, counts)
    current = min(q)
    eta[a, b] = current - previous
    assert eta[a, b] in (0, 1)
    optima[t] = current
    j = (a-b) % 3
    state[a, b] = (q[j] - q[(j+2) % 3],
                   q[(j+1) % 3] - q[(j+2) % 3])
    previous = current

# Independent tiny optimization, with no color/min formula in the search.
for t, _, _ in points:
    if t > 36:
        break
    vertices = [d for d, _, _ in points if d <= t]
    corners = [{d, 2*d, 3*d} for d in vertices if 3*d <= t]
    brute = next(size for size in range(len(vertices)+1)
                 if any(all(corner.intersection(chosen) for corner in corners)
                        for chosen in combinations(vertices, size)))
    assert brute == optima[t]

offsets = ((0, 0), (1, 0), (0, 1), (1, 1))
witnesses = {}
for t, a, b in points:
    if b < 4 or (a+1, b+1) not in eta:
        continue
    z, z10, z01, z11 = [state[a+i, b+k] for i, k in offsets]
    pattern = tuple(eta[a+i, b+k] for i, k in offsets)
    assert pattern != (1, 0, 0, 1)
    assert pattern == tuple(cone(state[a+i, b+k]) for i, k in offsets)
    j = (a-b) % 3
    assert add(z11, z) == add(add(z10, z01), W[-j % 3])
    u = add(z10, neg(z))
    alphabet = {ZERO, W[(-j-1) % 3], neg(W[-j % 3])}
    assert u in alphabet
    witnesses.setdefault(pattern, (a, b, t))
assert set(witnesses) == set(product((0, 1), repeat=4)) - {(1, 0, 0, 1)}
for pattern, (a, b, t) in witnesses.items():
    for i, k in offsets:
        s = 2**(a+i) * 3**(b+k)
        q = row_q(s)
        assert q == direct_q(s, [sum(1 for d, c, e in points
                                    if d <= s and (c-e) % 3 == j)
                                 for j in range(3)])

# Exact five-interval vertical-edge alphabet. Every endpoint is left-closed.
breaks = (Fraction(1), Fraction(9, 8), Fraction(4, 3),
          Fraction(3, 2), Fraction(27, 16), Fraction(2))
vertical = [set() for _ in range(3)]


def exception(mantissa, color):
    if mantissa < Fraction(3, 2):
        return W[color % 3]
    if mantissa < Fraction(27, 16):
        return W[(color+1) % 3]
    return ZERO


for j, k in product(range(3), repeat=2):
    for left, right in zip(breaks, breaks[1:]):
        values = []
        for mantissa in (left, (left+right)/2):
            h = 1 if mantissa < Fraction(4, 3) else 2
            n = (j+k+h) % 3
            partial = (W[0], neg(W[2]), ZERO)[n]
            strip = mul(W[(1-j) % 3], partial)
            old = exception(mantissa, k)
            new = exception(3*mantissa/2**h, k+h+1)
            values.append(add(add(strip, old), neg(new)))
        assert values[0] == values[1]
        vertical[j].add(values[0])
assert vertical == [
    {(-1, -1), (-1, 0), (-1, 1), (0, 0), (0, 1), (1, 1)},
    {(0, -1), (0, 0), (0, 1), (1, 0), (1, 1), (2, 1)},
    {(-1, -2), (-1, -1), (-1, 0), (0, -1), (0, 0), (1, 0)},
]

# Regression check for the infinite-state hand proof (not itself that proof).
for j in range(3):
    alphabet = {ZERO, W[(-j-1) % 3], neg(W[-j % 3])}
    for u, x, y, s, t in product(alphabet, range(-3, 4), range(-3, 4),
                               range(-3, 4), range(-3, 4)):
        z, z01 = (x, y), (s, t)
        z10, z11 = add(z, u), add(add(z01, u), W[-j % 3])
        assert tuple(map(cone, (z, z10, z01, z11))) != (1, 0, 0, 1)

# All pair-boundary possibilities of the rational aperiodic countermodel.
def pair(kind, a):
    return (0, 1) if kind == 0 else (a % 2, 0)


for left_kind, right_kind, a in product(range(2), repeat=3):
    left0, left1 = pair(left_kind, a), pair(left_kind, a+1)
    right0, right1 = pair(right_kind, a), pair(right_kind, a+1)
    inside = left0[0], left1[0], left0[1], left1[1]
    across = left0[1], left1[1], right0[0], right1[0]
    assert inside != (1, 0, 0, 1) != across
assert Fraction(2, 3) / (1-Fraction(1, 9)) == Fraction(3, 4)
assert Fraction(1, 2) == Fraction(1, 3) + Fraction(1, 6)
assert 1 == Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 6)

# One genuine carry survives every adjacent forbidden-pattern check.
changes = {(2, 5): 1, (1, 6): 0, (2, 6): 0}
assert tuple(eta[cell] for cell in changes) == (0, 1, 1)
starts = {(a-i, b-j) for a, b in changes for i, j in offsets
          if a-i >= 0 and b-j >= 4}
for a, b in starts:
    pattern = tuple(changes.get((a+i, b+j), eta[a+i, b+j])
                    for i, j in offsets)
    assert pattern != (1, 0, 0, 1)
assert sum(Fraction(value-eta[a, b], 2**a * 3**b)
           for (a, b), value in changes.items()) == 0

print('PASS: actual 15-pattern language, forbidden1001, edge tables, tiny optima, rational countermodel.')
for pattern, witness in sorted(witnesses.items()):
    print(''.join(map(str, pattern)), witness)
