"""Independent integer-only CF, state, and complete-variation certificates.

Matveev and the previously proved four-state jump bounds are theorem inputs.
"""
from fractions import Fraction


def linear_sign(a, b):
    left = 2 ** max(a, 0) * 3 ** max(b, 0)
    right = 2 ** max(-a, 0) * 3 ** max(-b, 0)
    return (left > right) - (left < right)


def actual_convergents():
    # The complete quotient is (a*alpha+b)/(c*alpha+d), with positive denominator.
    a, b, c, d = 1, 0, 0, 1
    p0, p1, q0, q1 = 0, 1, 1, 0
    values = []
    while True:
        digit = 0
        while linear_sign(a - (digit + 1) * c, b - (digit + 1) * d) > 0:
            digit += 1
        assert linear_sign(a - digit * c, b - digit * d) > 0
        p, q = digit * p1 + p0, digit * q1 + q0
        values.append((p, q))
        if q > 2000:
            return values
        p0, p1, q0, q1 = p1, p, q1, q
        a, b, c, d = c, d, a - digit * c, b - digit * d


def floor_alpha(n):
    result = 0
    while linear_sign(n, -(result + 1)) > 0:
        result += 1
    return result


def complete_variation(a, b, c, d):
    assert abs(a * d - b * c) == 1
    A, B = b + d, a + c
    return 9 * (
        Fraction(1, 2 ** (A - 1)) * (1 + Fraction(A + 1, b * d))
        + Fraction(1, 3 ** B)
        * (Fraction(3, 2) + Fraction(6 * B + 3, 4 * a * c))
    )


F = Fraction
convergents = actual_convergents()
pairs = set(zip(convergents, convergents[1:]))
balanced = {(0, 1, 1, 0), (1, 1, 1, 0), (2, 0, 2, 1), (2, 2, 2, 0)}
cases = (((12, 19), (41, 65)), ((53, 84), (306, 485)), ((306, 485), (665, 1054)))
for current, successor in cases:
    assert (current, successor) in pairs
    p, q = current
    P, Q = successor
    r, s = p + P, q + Q
    assert (p + q) % 3 and (r + s) % 3
    assert linear_sign(q, -p) == linear_sign(s, -r)
    assert linear_sign(q, -p) == -linear_sign(Q, -P)
    counts = [0, 0, 0]
    for j in range(s):
        counts[(j + (r * j) // s) % 3] += 1
    state = (r % 3, s % 3, counts[0] - counts[2], counts[1] - counts[2])
    assert state in balanced and min(r, s) > 24
    for n in range(1, 24):
        assert n * r // s == floor_alpha(n)
        assert n * s // r == (3 ** n).bit_length() - 1
    remainder = complete_variation(p, q, r, s) + complete_variation(r, s, P, Q)
    assert remainder <= F(855, 2 ** (s + q + 1)) < F(432, 2 ** (s + q))
    gap = F(1, 2 ** s) - F(1, 3 ** r)
    assert abs(gap) / 20 > remainder
    print(f"PASS {p}/{q}: actual successor {P}/{Q}; balanced mediant {r}/{s}; full jump dominates")

print("PASS: independent exact CF, state, short-floor, endpoint, and complete-variation checks")
