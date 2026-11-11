"""Narrow exact checks for the fixed-raw-phase excursion obstruction."""
from itertools import product


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def rot(z, count=1):
    for _ in range(count % 3):
        z = -z[1], z[0] - z[1]
    return z


def allowed(z):
    return z[0] <= 1 and z[0] - z[1] <= 1


errors = ((0, 0), (1, 0), (0, 1), (-1, -1),
          (-1, 0), (0, -1), (1, 1))
feasible = 0
for z in product(range(-12, 13), repeat=2):
    for s, t in product(errors, repeat=2):
        z1 = add(rot(z), s)
        z2 = add(rot(z1), t)
        if allowed(z) and allowed(z1) and allowed(z2):
            assert -2 <= z[0] <= 1 and -2 <= z[1] <= 3
            assert abs(z[0]) + abs(z[1]) <= 5
            feasible += 1
assert feasible > 0


def discrepancy(limit):
    z = (0, 0)
    two, a = 1, 0
    while two <= limit:
        three, b = 1, 0
        while two * three <= limit:
            z = add(z, rot((1, 0), a + 2 * b))
            three *= 3
            b += 1
        two *= 2
        a += 1
    return z


def floor_log_three(value):
    exponent, power = 0, 1
    while 3 * power <= value:
        exponent += 1
        power *= 3
    return exponent


partial = ((1, 0), (0, -1), (0, 0))
for cutoff in range(1, 51):
    strip = partial[floor_log_three(2 * cutoff) % 3]
    assert discrepancy(2 * cutoff) == add(rot(discrepancy(cutoff)), strip)
    increment = (0, 0)
    for step in range(1, 4):
        increment = add(increment,
                        rot(partial[floor_log_three(2 ** step * cutoff) % 3], -step))
    assert discrepancy(8 * cutoff) == add(discrepancy(cutoff), increment)

# Independent hand-calculated prefix: D_3={1,2,3}, one of each color.
assert discrepancy(3) == (0, 0)
assert discrepancy(1) == (1, 0)
print({'three_cutoff_feasible_cases': feasible,
       'exact_strip_and_three_doubling_checks': 50})
