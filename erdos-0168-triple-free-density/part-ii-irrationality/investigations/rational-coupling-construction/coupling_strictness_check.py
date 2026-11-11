"""Exact finite checks supporting the actual-coupling strictness proof."""
from fractions import Fraction as F


def arrival_exponents(a, b):
    if b == 0 and a >= 1:
        return a - 1, 1
    if b == 1 and a >= 2:
        return a - 3, 3
    return a, b


def monomial(v):
    return F(2) ** v[0] * F(3) ** v[1]


def group(n, b):
    tokens = [(3 * n + r, b) for r in range(3)]
    assert sorted((a - b) % 3 for a, b in tokens) == [0, 1, 2]
    return [arrival_exponents(a, b) for a, b in tokens]


groups = [group(n, b) for n in range(4) for b in range(5)]
events = {F(1): (0, 0)}
for triple in groups:
    for v in triple:
        time = monomial(v)
        assert time >= 1
        assert time not in events or events[time] == v
        events[time] = v
times = sorted(events)
integrated = [0, 0]
for left, right in zip(times, times[1:]):
    counts = [sum(monomial(v) <= left for v in triple) for triple in groups]
    partial = sum(k if k < 3 else 0 for k in counts)
    for j in range(2):
        integrated[j] += partial * (events[right][j] - events[left][j])
dispersion = [0, 0]
for triple in groups:
    latest = max(triple, key=monomial)
    gap = tuple(3 * latest[j] - sum(v[j] for v in triple) for j in range(2))
    assert monomial(gap) > 1
    for j in range(2):
        dispersion[j] += gap[j]
assert integrated == dispersion


def actual_counts(limit):
    tokens = []
    a, two = 0, 1
    while two <= limit:
        b, original = 0, two
        while original <= limit:
            time = monomial(arrival_exponents(a, b))
            if time <= limit:
                tokens.append((a, b, time))
            b, original = b + 1, original * 3
        a, two = a + 1, two * 2
    colors = [sum((a - b) % 3 == j for a, b, _ in tokens) for j in range(3)]
    touched = {(a // 3, b) for a, b, _ in tokens}
    completed = sum(max(map(monomial, group(n, b))) <= limit for n, b in touched)
    partial = len(tokens) - 3 * completed
    imbalance = len(tokens) - 3 * min(colors)
    deficit = min(colors) - completed
    assert deficit >= 0 and 3 * deficit == partial - imbalance
    bulk_partial, three = 0, 9
    while three <= limit:
        count, value = 0, three
        while value <= limit:
            count, value = count + 1, value * 2
        bulk_partial += count % 3
        three *= 3
    edge_partial = 0
    for n, b in touched:
        if b < 2:
            k = sum(monomial(v) <= limit for v in group(n, b))
            edge_partial += k if k < 3 else 0
    assert 0 <= edge_partial <= 4
    assert partial == bulk_partial + edge_partial
    return deficit, tokens


for cutoff in (F(3), F(27, 2), F(81), F(96), F(768), F(2**20)):
    actual_counts(cutoff)
deficit, _ = actual_counts(F(81))
_, tokens = actual_counts(F(96))
assert deficit == 2
assert not any(F(81) < time < F(96) for _, _, time in tokens)
assert deficit * (F(1, 81) - F(1, 96)) == F(5, 1296)
print("PASS: exact logarithmic dispersion identity, six actual cutoffs, canonical gap >= 5/1296")
