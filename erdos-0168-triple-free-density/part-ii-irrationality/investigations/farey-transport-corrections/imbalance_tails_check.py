"""Exact checks for positive imbalance tails and one doubling counterterm."""
from bisect import bisect_right
from collections import Counter
from fractions import Fraction as F


def arrival2(a, b):
    if b == 0 and a >= 1:
        return 3 * 2**a
    if b == 1 and a >= 2:
        return 27 * 2**(a-2)
    return 2 * 2**a * 3**b


class Events:
    def __init__(self, limit):
        self.limit = F(limit)
        self.by_color = [[], [], []]
        increments = Counter()
        a, two = 0, 1
        while two <= limit:
            b, original = 0, two
            while original <= limit:
                time2 = arrival2(a, b)
                if time2 <= 2*limit:
                    color = (a-b) % 3
                    self.by_color[color].append(time2)
                    increments[time2, color] += 1
                b, original = b+1, original*3
            a, two = a+1, two*2
        for row in self.by_color:
            row.sort()
        self.times = sorted({time2 for time2, _ in increments})
        counts = [0, 0, 0]
        self.records = []
        for time2 in self.times:
            old_min = min(counts)
            old_e = sum(counts)-3*old_min
            for color in range(3):
                counts[color] += increments[time2, color]
            new_min = min(counts)
            new_e = sum(counts)-3*new_min
            assert new_min-old_min in (0, 1)
            self.records.append((F(time2, 2), new_e-old_e,
                                 new_min-old_min, new_e))

    def counts(self, time):
        assert 0 <= time <= self.limit
        return [bisect_right(row, 2*time) for row in self.by_color]

    def e(self, time):
        counts = self.counts(time)
        return sum(counts)-3*min(counts)

    def integral_e(self, left, right):
        left, right = F(left), F(right)
        assert 1 <= left <= right <= self.limit
        value, current, previous = F(), self.e(left), left
        for time, _, _, new_e in self.records:
            if left < time < right:
                value += current*(1/previous-1/time)
                current, previous = new_e, time
        return value + current*(1/previous-1/right)

    def lower(self, cutoff):
        cutoff = F(cutoff)
        jumps = sum((change/time for time, change, _, _ in self.records
                     if time <= cutoff), F())
        value = F(19, 54)+jumps-F(self.e(cutoff), cutoff)
        assert value == F(19, 54)+self.integral_e(1, cutoff)
        weighted_n = sum((1/F(time2, 2) for row in self.by_color
                          for time2 in row if time2 <= 2*cutoff), F())
        weighted_tau = sum((birth/time for time, _, birth, _ in self.records
                            if time <= cutoff), F())
        assert value == F(19, 54)+weighted_n-3*weighted_tau-F(self.e(cutoff), cutoff)
        return value


def log3_floor(value):
    assert value >= 1
    m, power = 0, F(1)
    while 3*power <= value:
        m, power = m+1, 3*power
    return m


def r_value(time):
    return (log3_floor(2*time)+1) % 3


def r_tail(time):
    time = F(time)
    m = log3_floor(2*time)
    r0, r1, r2 = ((m+j+1) % 3 for j in range(3))
    compact = F(r0, time)+F(-8*r0+6*r1+2*r2, 13*3**m)
    boundary = F(3**(m+1), 2)
    periodic = sum((F(4*((m+j+1) % 3), 3**(m+j+1))
                    for j in range(1, 4)), F()) / (1-F(1, 27))
    assert compact == r0*(1/time-1/boundary)+periodic
    return compact


def valuation(value, prime):
    def exponent(integer):
        result = 0
        while integer and integer % prime == 0:
            integer //= prime
            result += 1
        return result
    assert value
    return exponent(abs(value.numerator))-exponent(value.denominator)


events = Events(4374)
breaks = {F(7), F(243)}
for time, _, _, _ in events.records:
    for point in (time, time/2):
        if 7 <= point <= 243:
            breaks.add(point)
for m in range(10):
    point = F(3**m, 2)
    if 7 <= point <= 243:
        breaks.add(point)
breaks = sorted(breaks)
for time in breaks + [(a+b)/2 for a, b in zip(breaks, breaks[1:])]:
    left, right = events.counts(time), events.counts(2*time)
    m = log3_floor(2*time)
    strip = [sum((-b) % 3 == j for b in range(m+1)) for j in range(3)]
    assert right == [left[(j-1) % 3]+strip[j] for j in range(3)]
    r = r_value(time)
    h = F(r-events.e(2*time)+events.e(time), 3)
    assert h in (0, 1) and (r or h == 0)
    if r:
        assert events.e(time)+events.e(2*time) >= 1
for cutoff in (7, 81):
    assert events.integral_e(cutoff, 54*cutoff) >= F(2, 81*cutoff)
    assert r_tail(cutoff) > 0
assert events.integral_e(7, 243) > 0

for p, q, lower_side in ((5, 8, True), (12, 19, False), (41, 65, True)):
    n, cutoff = 3*q, 2**(3*q)
    events = Events(8*cutoff)
    lower = events.lower(cutoff)
    upper = 2*events.lower(2*cutoff)-lower+r_tail(cutoff)
    b = log3_floor(cutoff)
    b2 = log3_floor(2*cutoff)
    assert (2**n*3**max(b, 3)*lower).denominator == 1
    assert (13*2**(n+1)*3**max(b2, 3)*upper).denominator == 1
    assert upper > lower
    if lower_side:
        assert 3**(3*p) < cutoff < 2*3**(3*p)
        assert valuation(lower, 3) == -3*p
    for multiplier in (1, 2, 3, 8):
        # 188+2 log(multiplier)/log(3) is bounded above by this integer.
        assert events.e(multiplier*cutoff) <= 188+2*multiplier
    print({"p": p, "q": q, "E_at_DK": events.e(cutoff),
           "lower_v3": valuation(lower, 3),
           "lower_denominator_bits": lower.denominator.bit_length(),
           "upper_denominator_bits": upper.denominator.bit_length()})
print("PASS: exact imbalance, doubling counterterm, and lower-CF ternary denominators")
