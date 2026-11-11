"""Exact finite checks for the fixed-logarithm nonvanishing comparison.

The infinite theorem uses Matveev; these examples do not verify that input.
"""
from fractions import Fraction as F


def variation(p, q, r, s):
    a, b = q + s, p + r
    return 9 * (
        F(2, 2**a) * (1 + F(a + 1, q * s))
        + F(1, 3**b) * (F(3, 2) + F(6 * b + 3, 4 * p * r))
    )


def actual_direct_floor(n):
    value, exponent = 1, 0
    while 3 * value <= 2**n:
        value *= 3
        exponent += 1
    return exponent


balanced = {(0, 1, 1, 0), (1, 1, 1, 0), (2, 0, 2, 1), (2, 2, 2, 0)}
cases = ((12, 19, 41, 65), (53, 84, 306, 485), (306, 485, 665, 1054))

for p, q, P, Q in cases:
    assert abs(p * Q - P * q) == 1 and 0 < q < Q
    assert 3 * q < 5 * p and 3 * p < 2 * q
    assert 3 * Q < 5 * P and 3 * P < 2 * Q
    assert (p + q) % 3 != 0
    r, s = p + P, q + Q
    assert (2**q - 3**p) * (2**Q - 3**P) < 0
    assert (2**q - 3**p) * (2**s - 3**r) > 0
    counts = [0, 0, 0]
    for a in range(s):
        counts[(a + r * a // s) % 3] += 1
    state = (r % 3, s % 3, counts[0] - counts[2], counts[1] - counts[2])
    assert state in balanced and min(r, s) > 24
    for n in range(1, 24):
        assert n * r // s == actual_direct_floor(n)
        assert n * s // r == (3**n).bit_length() - 1

    remainder = variation(p, q, r, s) + variation(r, s, P, Q)
    assert remainder <= F(855, 2) * F(1, 2 ** (s + q))
    for a, b in ((q + s, p + r), (s + Q, r + P)):
        assert F(1, 3**b) < F(3, 2**a)
    jump_lower = abs(F(1, 2**s) - F(1, 3**r)) / 20
    assert jump_lower > remainder
    power = (jump_lower // remainder).bit_length() - 1
    print(f"{p}/{q}: mediant {r}/{s}, state {state}, jump/remainder > 2^{power}")

print("PASS: three exact state, floor, variation and nonvanishing checks")
