from collections import defaultdict
from bisect import bisect_left
from fractions import Fraction as F
from itertools import product


def arrival(point):
    a, b = point
    assert min(a, b) >= 0
    value = F(2**a * 3**b)
    if b == 0 and a >= 1:
        value *= F(3, 2)
    if b == 1 and a >= 2:
        value *= F(9, 8)
    return value


def actual_records(limit):
    records = []
    a, power_two = 0, 1
    while power_two <= limit:
        b, raw = 0, power_two
        while raw <= limit:
            point = a, b
            value = arrival(point)
            if value <= limit:
                records.append((point, value, (a-b) % 3))
            b, raw = b+1, raw*3
        a, power_two = a+1, power_two*2
    return records


def event_counts(records):
    changes = defaultdict(lambda: [0, 0, 0])
    for _, value, color in records:
        changes[value][color] += 1
    counts, result = [0, 0, 0], {}
    for value in sorted(changes):
        counts = [counts[c] + changes[value][c] for c in range(3)]
        result[value] = tuple(counts)
    return result


def incident(point, u, v):
    triples = []
    for sign in (1, -1):
        offsets = ((0, 0), (sign*u[0], sign*u[1]),
                   (sign*v[0], sign*v[1]))
        for delta in offsets:
            anchor = point[0]-delta[0], point[1]-delta[1]
            triples.append(tuple((anchor[0]+x, anchor[1]+y) for x, y in offsets))
    assert len({tuple(sorted(t)) for t in triples}) == 6
    return triples


def check_local_obstruction():
    point, u, v = (12, 5), (8, -5), (3, -2)
    first, second = F(839808), F(995328)
    counts = event_counts(actual_records(2**21))
    assert arrival((2, 1)) == F(27, 2)
    assert counts[first] == (46, 46, 46)
    assert counts[second] == (48, 47, 47)
    times = sorted(counts)
    after_first = times[times.index(first)+1]
    after_second = times[times.index(second)+1]
    assert (after_first, after_second) == (884736, 1062882)
    triples = incident(point, u, v)
    early, late = [], []
    for k, triple in enumerate(triples):
        assert all(min(z) >= 0 for z in triple)
        assert {(a-b) % 3 for a, b in triple} == {0, 1, 2}
        if (7, 8) in triple:
            assert arrival((7, 8)) == first
            assert max(map(arrival, triple)) == second
            early.append(k)
        else:
            assert arrival(point) == second
            assert max(map(arrival, triple)) > second
            late.append(k)
    assert (early, late) == ([1, 5], [0, 2, 3, 4])
    lower_bound = min(1/first-1/after_first, 1/second-1/after_second)
    assert lower_bound == F(13, 214990848)
    print('LOCAL_PERIOD_FREE', point, 'GROUPS', early, late,
          'COUNTS', counts[first], counts[second], 'GAP_AT_LEAST', lower_bound)


def check_signed_hall_certificate():
    u, v, cutoff = (19, -12), (27, -17), F(3057647616)
    records = actual_records(cutoff)
    counts = event_counts(records)
    zero_times = [[t for t in counts if counts[t][c] == min(counts[t])]
                  for c in range(3)]
    negative = {0, 1, 2, 3, 4, 9, 13, 16, 20, 23, 24, 27, 30, 31, 34}
    positive = {28, 35}
    assert len(negative)-len(positive) == 13
    surviving, witnesses = [], {}
    for sign, b0, a0 in product((1, -1), range(6), range(6)):
        k = (0 if sign == 1 else 36) + a0 + 6*b0
        offsets = ((0, 0), (sign*u[0], sign*u[1]),
                   (sign*v[0], sign*v[1]))
        nodes = tuple((a0+x) % 6 + 6*((b0+y) % 6) for x, y in offsets)
        assert len(set(nodes)) == 3
        # A type with signed charge >1 must be killed by an actual zero-lag event.
        charge = len(set(nodes) & negative)-len(set(nodes) & positive)
        witness = None
        for point, value, color in records:
            node = point[0] % 6 + 6*(point[1] % 6)
            if node not in nodes:
                continue
            dx, dy = offsets[nodes.index(node)]
            anchor = point[0]-dx, point[1]-dy
            triple = tuple((anchor[0]+x, anchor[1]+y) for x, y in offsets)
            if min(min(z) for z in triple) < 0:
                continue
            last = max(map(arrival, triple))
            i = bisect_left(zero_times[color], value)
            if i < len(zero_times[color]) and zero_times[color][i] < last:
                witness = zero_times[color][i], color, point, triple
                break
        if witness is None:
            surviving.append(k)
            assert charge <= 1
        elif charge > 1:
            witnesses[k] = witness
    assert len(surviving) == 53
    assert witnesses and all(value <= cutoff for value, _, _, _ in witnesses.values())
    print('SIGNED_HALL', 'SURVIVORS', len(surviving), 'BAD_CHARGE_ZERO_WITNESSES', witnesses)
    print('HALL_REQUIRED_MASS', 13, 'AVAILABLE_TRIANGLE_MASS', 12)


if __name__ == '__main__':
    check_local_obstruction()
    check_signed_hall_certificate()
    print('PASS: independent actual counts, nonperiodic local obstruction and signed Hall dual')
