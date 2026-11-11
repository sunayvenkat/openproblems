"""Exact checks for seed budgets and countermodels; no external dependencies."""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm


def projective_height(values):
    scale = lcm(*(x.denominator for x in values))
    nums = [x.numerator * (scale // x.denominator) for x in values]
    content = 0
    for value in nums:
        content = gcd(content, abs(value))
    return max(map(abs, nums)) // content


def mixed_form(n):
    assert n >= 2 and n % 2 == 0
    two, three = 2**n, 3**n
    a = pow(three, -1, two)
    b = (two * three + 1 - a * three) // two
    assert 0 < a < two and 0 < b < three
    assert a % 2 == 1 and b % 3 == 1
    units = []
    for k in range(1, n + 1):
        if (a >> (n - k)) & 1:
            units.append(F(1, 2**k))
        digit = (b // 3 ** (n - k)) % 3
        if digit:
            units.append(F(digit, 3**k))
    assert len(units) <= 2 * n and len(units) == len(set(units))
    assert all(0 < u < 1 for u in units)
    assert F(1, two) in units and F(1, three) in units
    error, minimum = sum(units, F()) - 1, min(units)
    height = projective_height([F(1)] + units)
    assert error == F(1, 6**n) and minimum == F(1, 3**n)
    assert height == 6**n
    assert (error / minimum) ** 4 * height == F(3, 8) ** n
    if n <= 4:
        for mask in range(1 << len(units)):
            assert sum((u for k, u in enumerate(units) if mask >> k & 1), F()) != 1
    return len(units), height.bit_length()


def multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def word_matrix(word):
    matrix = ((1, 0), (0, 1))
    for digit in word:
        matrix = multiply(matrix, ((0, 1), (1, digit)))
    return matrix


def apply(matrix, x):
    return (matrix[0][0] * x + matrix[0][1]) / (
        matrix[1][0] * x + matrix[1][1])


def cantor_constants():
    a, b = word_matrix((3, 3)), word_matrix((1, 3, 2, 3))
    prefix = word_matrix((1, 1, 1, 2, 2))
    assert a == ((1, 3), (3, 10))
    assert b == ((7, 24), (9, 31))
    assert prefix == ((5, 12), (8, 19))
    gap = apply(b, F(0)) - apply(a, F(1))
    assert gap == F(188, 403) > 0
    for matrix in (a, b):
        assert matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] == 1
        for endpoint in (0, 1):
            denominator = matrix[1][0] * endpoint + matrix[1][1]
            assert F(1, 1600) <= F(1, denominator**2) <= F(1, 100)
    assert F(1, 27**2) == F(1, (prefix[1][0] + prefix[1][1]) ** 2)
    assert 1600 < 2**11
    for depth in range(1, 6):
        intervals = []
        for choices in product((a, b), repeat=depth):
            matrix = ((1, 0), (0, 1))
            for choice in choices:
                matrix = multiply(matrix, choice)
            intervals.append((apply(matrix, F(0)), apply(matrix, F(1))))
        intervals.sort()
        assert all(intervals[k + 1][0] - intervals[k][1]
                   >= gap / 1600 ** (depth - 1)
                   for k in range(len(intervals) - 1))
    for degree in (1, 2, 3, 10):
        assert degree + 1 - F(11 * (degree + 2), 11) == -1
    return gap


if __name__ == "__main__":
    for n in (2, 4, 8, 16, 32, 64):
        terms, bits = mixed_form(n)
        print(f"n={n}: m={terms}, projective H has {bits} bits: PASS")
    print(f"Loop constants and root-count exponent PASS; gap={cantor_constants()}")
    print("PASS. Infinite statements use the written proofs.")
