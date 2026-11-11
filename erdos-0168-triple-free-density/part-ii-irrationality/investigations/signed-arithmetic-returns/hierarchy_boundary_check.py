"""Actual dilation jumps and the complete finite-profile hierarchy boundary."""

from bisect import bisect_left, bisect_right
from collections import defaultdict
from fractions import Fraction as F


def actual_births(limit):
    events = defaultdict(list)
    for a in range(limit.bit_length()):
        power = 2**a
        b = 0
        while power <= limit:
            if b == 0 and a >= 1:
                clock = 3 * 2**a
            elif b == 1 and a >= 2:
                clock = 27 * 2**(a - 2)
            else:
                clock = 2 * power
            if clock <= 2 * limit:
                events[clock].append((a - b) % 3)
            power *= 3
            b += 1
    clocks, values, eta = [], [], {}
    counts = [0, 0, 0]
    for clock, colors in sorted(events.items()):
        before = min(counts)
        for color in colors:
            counts[color] += 1
        after = min(counts)
        clocks.append(clock)
        values.append(after)
        if after != before:
            assert after - before == 1 and clock % 2 == 0
            residue, a, b = clock // 2, 0, 0
            while residue % 2 == 0:
                residue //= 2
                a += 1
            while residue % 3 == 0:
                residue //= 3
                b += 1
            assert residue == 1
            eta[a, b] = 1

    def tau(time, strict=False):
        position = (bisect_left if strict else bisect_right)(clocks, 2 * time)
        return values[position - 1] if position else 0

    return eta, tau, clocks


def kappa(time, strict=False):
    power, answer = 9, 0
    while power < 2 * time or not strict and power == 2 * time:
        answer += 1
        power *= 27
    return answer


def moment(array):
    return sum((F(value, 2**a * 3**b) for (a, b), value in array.items()), F())


def check_doubling(limit):
    eta, tau, clocks = actual_births(limit)
    assert eta.get((0, 1)) == eta.get((0, 2)) == 1
    assert not any(b == 0 for a, b in eta)
    assert tau(F(27, 2)) == tau(F(27, 2), True)
    h = lambda t, strict=False: (
        tau(2 * t, strict) - tau(t, strict) - kappa(t, strict))
    candidates = {F(7), F(limit, 2)}
    for clock in clocks:
        candidates.update((F(clock, 2), F(clock, 4)))
    power = 9
    while power <= limit:
        candidates.add(F(power, 2))
        power *= 27
    for time in candidates:
        if 7 <= time <= F(limit, 2):
            assert h(time) in (0, 1)
    for a in range(limit.bit_length()):
        value, b = 2**a, 0
        while 2 * value <= limit:
            if value >= 7:
                assert h(F(value)) - h(F(value), True) == (
                    eta.get((a + 1, b), 0) - eta.get((a, b), 0))
            value *= 3
            b += 1
    for b in range(3, 20):
        value = 3**b
        if value > limit:
            break
        assert h(F(value, 2)) - h(F(value, 2), True) == (
            eta.get((0, b), 0) - int(b % 3 == 2))
    if limit >= 3**11:
        assert h(F(27, 2)) - h(F(27, 2), True) == 1
        assert h(F(3**11, 2)) - h(F(3**11, 2), True) == -1

    jumps = defaultdict(int)
    for (a, b), value in eta.items():
        time = 2**a * 3**b
        jumps[F(time, 2)] += value
        jumps[F(time)] -= value
    total = moment(eta)
    column = sum((F(value, 3**b) for (a, b), value in eta.items() if a == 0), F())
    grid = sum((value / time for time, value in jumps.items()
                if time.denominator == 1), F())
    exterior = sum((value / time for time, value in jumps.items()
                    if time.denominator != 1), F()) - F(3, 13)
    assert grid == total - 2 * column
    assert exterior == 2 * column - F(3, 13)
    assert grid + exterior == total - F(3, 13)
    assert exterior >= F(77, 117)
    return eta


def multiply(left, right):
    product = defaultdict(int)
    for (a, b), value in left.items():
        for (c, d), other in right.items():
            product[a + c, b + d] += value * other
    return dict(product)


def check_full_profile_boundary(polynomial):
    max_a = max(a for a, b in polynomial)
    max_b = max(b for a, b in polynomial)
    width, height = max_a + 2, max_b + 6
    eta, _, _ = actual_births(2**(width - 1) * 3**(height - 1))
    c = {(a, b): 1 - 3 * eta.get((a, b), 0)
         for a in range(width) for b in range(height)}
    d = {(a, b - 4): value for (a, b), value in c.items() if b >= 4}
    pi = sum(value * 2**a * 3**b for (a, b), value in polynomial.items())
    low = sum((F(value, 2**a * 3**b) for (a, b), value in c.items() if b < 4), F())
    direct = 81 * pi * low
    for (a, b), value in d.items():
        direct += sum((F(coefficient * 2**aa * 3**bb * value, 2**a * 3**b)
                       for (aa, bb), coefficient in polynomial.items()
                       if a < aa or b < bb), F())
    alpha = [81 * sum(value * 2**(aa - a) * 3**bb
                      for (aa, bb), value in polynomial.items() if aa > a)
             for a in range(max_a)]
    beta = [81 * pi // 3**b if b < 4 else
            sum(value * 2**aa * 3**(bb - b + 4)
                for (aa, bb), value in polynomial.items() if bb > b - 4)
            for b in range(max_b + 4)]
    correction = F()
    for (aa, bb), coefficient in polynomial.items():
        scale = coefficient * 2**aa * 3**bb
        correction -= 81 * scale * sum(
            (F(c[a, b], 2**a * 3**b) for a in range(aa) for b in range(4)), F())
        correction -= scale * sum(
            (F(c[a, b + 4], 2**a * 3**b)
             for a in range(aa) for b in range(bb)), F())
    assert correction.denominator == 1
    profiles = correction
    profiles += sum((alpha[a] * sum(
        (F(c[a, b], 3**b) for b in range(height)), F())
        for a in range(max_a)), F())
    profiles += sum((beta[b] * sum(
        (F(c[a, b], 2**a) for a in range(width)), F())
        for b in range(max_b + 4)), F())
    assert direct == profiles
    assert alpha[-1] == 162 and beta[-1] == 3


for cutoff in (2**12, 3**11):
    eta = check_doubling(cutoff)
    total = moment(eta)
    previous = F()
    for a in range(1, 5):
        exterior = 2**a * sum(
            (F(value, 2**i * 3**j) for (i, j), value in eta.items() if i < a), F())
        column = sum((F(value, 3**j) for (i, j), value in eta.items() if i == a - 1), F())
        assert exterior - 2 * previous == 2 * column
        previous = exterior
    previous = F()
    for b in range(1, 5):
        exterior = 3**b * sum(
            (F(value, 2**i * 3**j) for (i, j), value in eta.items() if j < b), F())
        row = sum((F(value, 2**i) for (i, j), value in eta.items() if j == b - 1), F())
        assert exterior - 3 * previous == 3 * row
        previous = exterior
    for a, b in ((1, 0), (0, 1), (0, 2), (3, 2)):
        scale = 2**a * 3**b
        exterior = scale * sum(
            (F(value, 2**i * 3**j) for (i, j), value in eta.items()
             if i < a or j < b), F())
        columns = 2**a * sum(
            (F(value, 2**i * 3**j) for (i, j), value in eta.items() if i < a), F())
        rows = 3**b * sum(
            (F(value, 2**i * 3**j) for (i, j), value in eta.items() if j < b), F())
        corner = scale * sum(
            (F(value, 2**i * 3**j) for (i, j), value in eta.items()
             if i < a and j < b), F())
        assert exterior == 3**b * columns + 2**a * rows - corner
    assert eta.get((0, 1)) == 1  # The second ternary dilation has an atom at1/3.

operator = lambda q, p: {(2*q, 0): 1, (q, p): 1, (0, 2*p): 1}
check_full_profile_boundary(operator(8, 5))
check_full_profile_boundary(multiply(operator(1, 1), operator(3, 2)))
print("PASS: actual fractional-axis jumps, Mellin split, mixed filters, full profile dictionary.")
