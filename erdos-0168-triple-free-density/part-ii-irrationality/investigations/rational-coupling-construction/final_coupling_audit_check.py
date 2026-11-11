"""Independent narrow audit: direct token ownership/events and actual P0 tail."""
from bisect import bisect_right
from collections import Counter
from fractions import Fraction as F


def time2(a, b):
    if b == 0 and a:
        return 3 * 2**a
    if b == 1 and a >= 2:
        return 27 * 2**(a - 2)
    return 2 ** (a + 1) * 3**b


def records(limit):
    result = []
    a, two = 0, 1
    while two <= limit:
        b, value = 0, two
        while value <= limit:
            t = time2(a, b)
            if t <= 2 * limit:
                result.append((t, (a - b) % 3, a, b))
            b, value = b + 1, value * 3
        a, two = a + 1, two * 2
    return sorted(result)


def block(p, q, n):
    points = [(a + 3*q*n, b) for a in range(q) for b in range(2*p)]
    points += [(a + 3*q*n, b) for a in range(q, 2*q) for b in range(p)]
    colors = [sorted((time2(a, b), a, b) for a, b in points
                     if (a-b) % 3 == j) for j in range(3)]
    assert [len(c) for c in colors] == [p*q] * 3
    return [[(c[i][1], c[i][2]) for c in colors] for i in range(p*q)]


def maximum(triple):
    assert sorted((a-b) % 3 for a, b in triple) == [0, 1, 2]
    return max(time2(a, b) for a, b in triple)


def cost(groups):
    return sum((F(2, maximum(g)) for g in groups), F())


def bulk(p, q, n, r, b):
    return [(r+3*q*n, b+2*p), (r+q+3*q*n, b+p),
            (r+2*q+3*q*n, b)]


for p, q, exponent, expected in ((5, 8, 27, (59049, 31, 30)),
                                (12, 19, 45, (293534171136, 163, 162))):
    u, v = 2**q, 3**p
    zero, one = block(p, q, 0), block(p, q, 1)
    assert cost(zero) - u**3 * cost(one) == F(1, 27)
    # Sum the first horizontal bulk block directly, using only b>=2 scaling.
    base = sum((F(2, maximum(bulk(p, q, 0, r, 0)))
                + F(2, maximum(bulk(p, q, 0, r, 1)))
                + F(3, maximum(bulk(p, q, 0, r, 2)))
                for r in range(q)), F())
    value = cost(zero) + (cost(one) + base) / (1 - F(1, u**3))
    assert (27 * v**2 * (u**3 - 1) * value).denominator == 1
    V, qi = F(3, 13), value - F(1, 27)
    mean = (value + V + (qi-V)/u + V + (qi-V)/u**2) / 3
    folded = cost(zero) + base + V/u**3
    assert folded == value + (V-qi)/u**3 < value
    assert (1053*u**2*v**2*(u-1)*mean).denominator == 1
    assert (351*u**3*v**2*folded).denominator == 1
    for comparison, expected_v2 in ((mean, 3-2*q if u > v else -2*q),
                                    (folded, 3-3*q if u > v else -3*q)):
        n, d = abs(comparison.numerator), comparison.denominator
        assert (n & -n).bit_length() - (d & -d).bit_length() == expected_v2

    arrivals = records(2**exponent)
    blocks, keys = set(), set()
    for _, _, a, b in arrivals:
        n, local = divmod(a, 3*q)
        phase, r = divmod(local, q)
        if phase < 2 and b < (2-phase)*p:
            blocks.add(n)
        else:
            keys.add((n, r, b-(2-phase)*p))
    groups = [g for n in blocks for g in block(p, q, n)]
    groups += [bulk(p, q, *key) for key in keys]
    ownership = Counter(point for group in groups for point in group)
    assert set(ownership.values()) == {1}
    assert all(ownership[a, b] == 1 for _, _, a, b in arrivals)
    completed = Counter(maximum(g) for g in groups)
    counts, total, first = [0, 0, 0], 0, None
    by_time = {}
    for t, color, _, _ in arrivals:
        by_time.setdefault(t, []).append(color)
    for t, colors in by_time.items():
        for color in colors:
            counts[color] += 1
        total += completed[t]
        assert total <= min(counts)
        if total < min(counts) and first is None:
            first = (F(t, 2), min(counts), total)
    assert first == expected
    print({'pair': (p, q), 'direct_cost': str(value), 'first_deficit': first})


def minimum_tables(limit):
    times, minima, counts = [], [], [0, 0, 0]
    for t, color, _, _ in records(limit):
        counts[color] += 1
        if times and times[-1] == t:
            minima[-1] = min(counts)
        else:
            times.append(t)
            minima.append(min(counts))
    return times, minima


# Build the actual minimum independently from delayed-token arrivals.
A, B = 28, 20
times, minima = minimum_tables(2**(A-1) * 3**(B+3))


def tau(t):
    i = bisect_right(times, 2*t) - 1
    return minima[i] if i >= 0 else 0


def digit(a, b):
    v = 2**a * 3**(b+4)
    d = 1 - 3 * (tau(v) - tau(v-1))
    assert d in (1, -2)
    return d


head = sum((F(digit(a, b), 2**a * 3**b)
            for a in range(A) for b in range(B)), F())
corner = 216 * sum((F(digit(a, b), 2**a * 3**b)
                    for a in range(3) for b in range(3)), F())
assert corner == -552
tail = F(1, 2**A) + F(1, 3**B) - F(1, 2**A * 3**B)
low, high = 182 * (head - 6*tail) - corner, 182 * (head + 3*tail) - corner
assert F(139875, 1024) < low < high < F(139876, 1024)

# The sole fixed beyond-window example, with all shifted digits and the full tail.
P0 = {(3, 3): -1, (3, 0): 27, (0, 3): 8, (0, 0): -34}
T = {(78, 48): 1, (78, 0): -3**48, (0, 48): -2**78}
P = Counter()
for (a, b), c in P0.items():
    for (x, y), d in T.items():
        P[a+x, b+y] += c*d
P = {point: c for point, c in P.items() if c}
times, minima = minimum_tables(2**(A-1+max(a for a, b in P))
                               * 3**(B+3+max(b for a, b in P)))
head = sum((F(sum(c*digit(a+x, b+y) for (x, y), c in P.items()),
              2**a * 3**b) for a in range(A) for b in range(B)), F())
error = 6 * tail * sum(abs(c) for c in P.values())
assert -699753 * 2**64 < head-error < head+error < -699752 * 2**64
print('PASS: independent ownership, costs, deficits, phase valuations, P0 and WC7 tails')
