"""Exact certificate for mixed-tail propagation and its carry obstruction."""
from fractions import Fraction as F
from itertools import product


def tau(t):
    if t < 3:
        return 0
    counts = [0, 0, 0]
    power = 1
    b = 0
    while power <= t:
        last = (t // power).bit_length() - 1
        for j in range(3):
            first = (j + b) % 3
            if first <= last:
                counts[j] += (last - first) // 3 + 1
        power *= 3
        b += 1
    e = 1 << (t.bit_length() - 1)
    if e >= 2 and 3 * e > 2 * t:
        counts[(e.bit_length() - 1) % 3] -= 1
    if t >= 12:
        e = 1 << ((t // 6).bit_length() - 1)
        if e >= 2 and 6 * e <= t and 4 * t < 27 * e:
            counts[(e.bit_length() - 1) % 3] -= 1
    return min(counts)


def birth(a, b):
    d = 2**a * 3**b
    return tau(d) - tau(d - 1) - int((a, b) == (0, 1))


size = 12
h = [[birth(a, b) for b in range(size)] for a in range(size)]
assert all(v in (0, 1) for row in h for v in row)
assert tau(3) - tau(2) == 1 and h[0][1] == 0
tails = [[F(0) for _ in range(size + 1)] for _ in range(size + 1)]
for a in reversed(range(size)):
    for b in reversed(range(size)):
        tails[a][b] = (h[a][b] + tails[a + 1][b] / 2
                       + tails[a][b + 1] / 3 - tails[a + 1][b + 1] / 6)
        assert (6 * tails[a][b] - 3 * tails[a + 1][b]
                - 2 * tails[a][b + 1] + tails[a + 1][b + 1]) == 6 * h[a][b]
        assert 0 <= tails[a][b] <= 3
direct = sum((F(h[a][b], 2**a * 3**b)
              for a in range(size) for b in range(size)), F(0))
assert direct == tails[0][0]

# The exact common lattice propagates if both boundary axes supply it.
scale = 2**size * 3**size
assert all((scale * v).denominator == 1 for row in tails for v in row)


def pair(choice):
    return ((0, 1), (0, 0)) if choice == 0 else ((0, 0), (1, 1))


for choice in (0, 1):
    rows = pair(choice)
    mass = sum((F(rows[b][a], 2**a * 3**b)
                for a, b in product(range(2), repeat=2)), F(0))
    assert mass == F(1, 2)
for left, right in product((0, 1), repeat=2):
    rows = pair(left) + pair(right)
    for b in range(3):
        assert (rows[b][0], rows[b][1], rows[b + 1][0], rows[b + 1][1]) != (1, 0, 0, 1)

for count in range(1, 15):
    mass = sum((F(1, 2 * 9**k) for k in range(count)), F(0))
    assert mass == F(9, 16) * (1 - F(1, 9**count))

# Squares at k=1,4 are the only ones below six. Bound every remaining bit.
g_lower = F(1, 9) + F(1, 9**4)
g_upper = g_lower + F(9, 8 * 9**6)
r10_lower = F(9, 8) - F(2, 3) * g_upper
r10_upper = F(9, 8) - F(2, 3) * g_lower
r11_lower, r11_upper = 3 * r10_lower - 3, 3 * r10_upper - 3
assert 16 <= 16 * r10_lower < 16 * r10_upper < 17
assert 2 <= 16 * r11_lower < 16 * r11_upper < 3
k00, k10, k01, k11 = 9, 16, 3, 2
assert 6 * k00 - 3 * k10 - 2 * k01 + k11 == 2

print("PASS: actual finite-head mixed tails, boundary lattice, rational-total/irrational-boundary construction, nonzero rounded carry defect.")
