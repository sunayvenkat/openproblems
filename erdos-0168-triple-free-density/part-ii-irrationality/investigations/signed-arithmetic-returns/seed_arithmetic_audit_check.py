"""Independent integer-coordinate and continued-fraction audit; no imports from companions."""
from fractions import Fraction as F
from itertools import product
from math import gcd


def bezout(a, b):
    old_r, r, old_s, s = a, b, 1, 0
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    assert old_r == 1
    return old_s


def positive_form(n):
    assert n >= 2 and n % 2 == 0
    two, three = 2**n, 3**n
    a = bezout(three, two) % two
    b, remainder = divmod(two * three + 1 - a * three, two)
    assert remainder == 0 and 0 < a < two and 0 < b < three
    coordinates = []
    binary, ternary, power_two, power_three = a, b, 1, 1
    while binary or ternary:
        binary, bit = divmod(binary, 2)
        ternary, digit = divmod(ternary, 3)
        if bit:
            coordinates.append(power_two * three)
        if digit:
            coordinates.append(digit * power_three * two)
        power_two *= 2
        power_three *= 3
    height = two * three
    assert len(coordinates) <= 2 * n
    assert len(coordinates) == len(set(coordinates))
    assert all(0 < x < height for x in coordinates)
    assert two in coordinates and three in coordinates
    content = height
    for x in coordinates:
        content = gcd(content, x)
    assert content == 1
    assert min(coordinates) == two and sum(coordinates) == height + 1
    assert F(1, min(coordinates)) ** 4 * height == F(3, 8) ** n
    if n <= 4:
        sums = {0}
        for x in coordinates:
            sums |= {y + x for y in sums}
        assert height not in sums
    return len(coordinates)


def literal_cf(word, tail):
    value = tail
    for digit in reversed(word):
        value = 1 / (digit + value)
    return value


def loop_geometry():
    block_a, block_b = (3, 3), (1, 3, 2, 3)
    prefix = (1, 1, 1, 2, 2)
    for x in (F(0), F(1, 3), F(1, 2), F(1)):
        assert literal_cf(block_a, x) == (x + 3) / (3 * x + 10)
        assert literal_cf(block_b, x) == (7 * x + 24) / (9 * x + 31)
        assert literal_cf(prefix, x) == (5 * x + 12) / (8 * x + 19)
    gap = literal_cf(block_b, F(0)) - literal_cf(block_a, F(1))
    assert gap == F(188, 403)
    for c, d in ((3, 10), (9, 31)):
        assert F(1, 1600) <= F(1, (c + d) ** 2)
        assert F(1, d**2) <= F(1, 100)
    assert 5 * 19 - 12 * 8 == -1
    assert F(1, 27**2) == F(1, 729)
    assert 1600 < 2**11
    for depth in (1, 2, 4):
        intervals = []
        for choices in product((block_a, block_b), repeat=depth):
            word = tuple(digit for block in choices for digit in block)
            intervals.append((literal_cf(word, F(0)), literal_cf(word, F(1))))
        intervals.sort()
        assert all(right[0] - left[1] >= gap / 1600 ** (depth - 1)
                   for left, right in zip(intervals, intervals[1:]))
    return gap


def one_unit_height():
    for p, q in ((5, 8), (12, 19), (53, 84)):
        numerator, denominator = 2**q, 3**p
        assert gcd(numerator, denominator) == 1
        unit = F(numerator, denominator)
        assert F(1, 2) <= unit <= 2 and unit != 1
        assert max(numerator, denominator) <= 2 ** (q + 1)
        # The primitive projective coordinates are (3^p,2^q).
        assert min(F(1), unit) >= F(1, 2)


if __name__ == "__main__":
    one_unit_height()
    for n in (2, 4, 8, 16, 32, 64):
        print(f"n={n}: {positive_form(n)} distinct positive units, exact primitive height: PASS")
    print(f"Literal CF branch geometry and prefix distortion: PASS; gap={loop_geometry()}")
    print("PASS. Infinite estimates are established in the written audit.")
