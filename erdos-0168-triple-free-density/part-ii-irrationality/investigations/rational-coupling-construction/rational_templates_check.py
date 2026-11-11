"""Exact finite-head repairs of one bijective retimed-token coupling."""
from fractions import Fraction as F
from collections import Counter


def arrival(a, b):
    original = F(2**a * 3**b)
    if b == 0 and a >= 1:
        return original * F(3, 2)
    if b == 1 and a >= 2:
        return original * F(9, 8)
    return original


def row_group(n, b):
    return [(3*n+r, b) for r in range(3)]


def group_cost(group):
    assert len(group) == 3
    assert sorted((a-b) % 3 for a, b in group) == [0, 1, 2]
    return 1 / max(arrival(a, b) for a, b in group)


def tokens_below(limit):
    lists = [[], [], []]
    a, power_two = 0, 1
    while power_two <= limit:
        b, value = 0, power_two
        while value <= limit:
            time = arrival(a, b)
            if time <= limit:
                lists[(a-b) % 3].append((time, a, b))
            b, value = b+1, value*3
        a, power_two = a+1, power_two*2
    return [sorted(items) for items in lists]


def repair(limit):
    lists = tokens_below(limit)
    k = min(map(len, lists))
    heads = [items[:k] for items in lists]
    head = {(a, b) for items in heads for _, a, b in items}
    groups = {(a//3, b) for a, b in head}
    union = {point for n, b in groups for point in row_group(n, b)}
    parts = [sorted((arrival(a, b), a, b)
                    for a, b in union if (a-b) % 3 == j) for j in range(3)]
    assert all(len(items) == len(groups) for items in parts)
    assert all(parts[j][:k] == heads[j] for j in range(3))
    triples = [[(parts[j][i][1], parts[j][i][2]) for j in range(3)]
               for i in range(len(groups))]
    assert {p for triple in triples for p in triple} == union
    assert sum(map(len, triples)) == len(union)
    before = sum((group_cost(row_group(n, b)) for n, b in groups), F())
    after = sum((group_cost(triple) for triple in triples), F())
    value = F(61, 189) - before + after
    assert after >= before
    assert value >= sum((1/max(heads[j][i][0] for j in range(3))
                         for i in range(k)), F())
    bound_a = limit.bit_length()-1
    bound_b, power_three = 0, 1
    while power_three*3 <= limit:
        bound_b, power_three = bound_b+1, power_three*3
    denominator = 7 * 2**(bound_a+2) * 3**max(bound_b, 3)
    assert (denominator*value).denominator == 1
    return value, groups, k, denominator, max(items[-1][0] for items in heads)


for n in range(4):
    assert group_cost(row_group(n, 0)) == F(1, 6*8**n)
    assert group_cost(row_group(n, 1)) == F(2, 27*8**n)
    for b in (2, 3, 7):
        assert group_cost(row_group(n, b)) == F(1, 4*8**n*3**b)
assert F(1, 6)*F(8, 7) + F(2, 27)*F(8, 7) + F(1, 4)*F(8, 7)*F(1, 6) == F(61, 189)

previous_value, previous_groups = F(61, 189), set()
for cutoff in (3, 2**8, 2**19):
    value, groups, k, denominator, last_head = repair(cutoff)
    assert previous_groups <= groups
    assert previous_value <= value
    previous_value, previous_groups = value, groups
    print({"cutoff": cutoff, "K": k, "patch_groups": len(groups),
           "last_head": str(last_head), "cost": str(value),
           "reduced_denominator": value.denominator,
           "clearing_bound": denominator})
print("PASS: canonical coupling and three exact finite-head repairs")


def asymptotic_arrival(a, b):
    value = F(2**a * 3**b)
    return value * (F(3, 2) if b == 0 else F(9, 8) if b == 1 else 1)


def optimal_maxima(points, time):
    lists = [sorted(time(a, b) for a, b in points if (a-b) % 3 == j)
             for j in range(3)]
    assert len(set(map(len, lists))) == 1
    return [max(items) for items in zip(*lists)]


def skew_template(p, q):
    assert p >= 2 and q >= 3 and (p+q) % 3
    u, v = 2**q, 3**p
    low = [(a, b) for a in range(q) for b in range(2*p)]
    low += [(a, b) for a in range(q, 2*q) for b in range(p)]
    assert len(low) == 3*p*q
    assert [sum((a-b) % 3 == j for a, b in low) for j in range(3)] == [p*q]*3
    maxima0 = optimal_maxima(low, arrival)
    maximainf = optimal_maxima(low, asymptotic_arrival)
    opt0 = sum((1/t for t in maxima0), F())
    optinf = sum((1/t for t in maximainf), F())
    assert opt0-optinf == F(1, 27)
    ms = [max(F(v*v), F(u*v), factor*u*u)
          for factor in (F(3, 2), F(9, 8), F(1))]
    bulk = F(2*u*u, u*u+u+1) * (1/ms[0] + F(1, 3)/ms[1] + F(1, 6)/ms[2])
    cost = opt0 + optinf/F(u**3-1) + bulk
    denominator = 27*v*v*(u**3-1)
    assert (denominator*cost).denominator == 1
    return cost, denominator, maxima0, maximainf, ms


def first_skew_deficit(p, q, exponent):
    cost, denominator, maxima0, maximainf, ms = skew_template(p, q)
    limit, u = 2**exponent, 2**q
    completed = Counter(t for t in maxima0 if t <= limit)
    for t in maximainf:
        t *= u**3
        while t <= limit:
            completed[t] += 1
            t *= u**3
    scale = 1
    while scale*ms[2] <= limit:
        for r in range(q):
            b, factor = 0, F(2**r*scale)
            while factor*ms[min(b, 2)] <= limit:
                completed[factor*ms[min(b, 2)]] += 1
                b, factor = b+1, factor*3
        scale *= u**3
    events = Counter()
    for color, items in enumerate(tokens_below(limit)):
        for time, a, b in items:
            events[(time, color)] += 1
    times = sorted({time for time, color in events})
    assert set(completed) <= set(times)
    counts, groups, first = [0, 0, 0], 0, None
    for time in times:
        for color in range(3):
            counts[color] += events[(time, color)]
        groups += completed[time]
        assert groups <= min(counts)
        if groups < min(counts) and first is None:
            first = (time, min(counts), groups)
    assert sum((F(n)/time for time, n in completed.items()), F()) <= cost
    return cost, denominator, first


for p, q, exponent in ((5, 8, 27), (12, 19, 45)):
    value, denominator, first = first_skew_deficit(p, q, exponent)
    assert first is not None
    print({"skew": (p, q), "cost": str(value), "reduced_denominator": value.denominator,
           "clearing_bound": denominator, "first_deficit": tuple(map(str, first))})
print("PASS: two complete skew templates and exact first-deficit certificates")
