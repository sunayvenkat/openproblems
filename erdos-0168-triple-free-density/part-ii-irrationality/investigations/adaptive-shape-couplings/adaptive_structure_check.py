from collections import defaultdict
from fractions import Fraction as F
from itertools import product


def arrival(point):
    a, b = point
    value = F(2**a * 3**b)
    if b == 0 and a >= 1:
        value *= F(3, 2)
    if b == 1 and a >= 2:
        value *= F(9, 8)
    return value


def records_through(limit):
    records = []
    a, power_two = 0, 1
    while power_two <= limit:
        b, raw = 0, power_two
        while raw <= limit:
            point = a, b
            value = arrival(point)
            if value <= limit:
                records.append((value, point, (a-b) % 3))
            b, raw = b+1, raw*3
        a, power_two = a+1, power_two*2
    return sorted(records)


def events_and_bursts(records):
    changes = defaultdict(list)
    for value, point, color in records:
        changes[value].append((point, color))
    counts, events, bursts = [0, 0, 0], [], []
    previous, rank, points, local_events = F(0), 0, [], []
    for value in sorted(changes):
        for point, color in changes[value]:
            counts[color] += 1
            points.append(point)
        event = value, tuple(counts)
        events.append(event)
        local_events.append(event)
        if len(set(counts)) == 1:
            bursts.append((previous, value, rank, counts[0],
                           tuple(points), tuple(local_events)))
            previous, rank, points, local_events = value, counts[0], [], []
    return events, bursts


def span(triple):
    return (max(a for a, b in triple)-min(a for a, b in triple),
            max(b for a, b in triple)-min(b for a, b in triple))


def normalized(triple):
    a0 = min(a for a, b in triple)
    b0 = min(b for a, b in triple)
    return tuple(sorted((a-a0, b-b0) for a, b in triple))


def burst_cover(burst, horizontal, vertical):
    _, _, _, _, points, events = burst
    colors = [sorted(p for p in points if (p[0]-p[1]) % 3 == j)
              for j in range(3)]
    edges = []
    for triple in product(*colors):
        dx, dy = span(triple)
        if dx > horizontal or dy > vertical:
            continue
        last = max(map(arrival, triple))
        if any(arrival(p) <= t < last and
               counts[(p[0]-p[1]) % 3] == min(counts)
               for p in triple for t, counts in events):
            continue
        edges.append(triple)

    def search(todo, used):
        if not todo:
            return []
        choices = [([edge for edge in edges if edge[0] == p and
                     edge[1] not in used and edge[2] not in used], p)
                   for p in sorted(todo)]
        candidates, point = min(choices, key=lambda pair: len(pair[0]))
        for edge in candidates:
            rest = search(todo-{point}, used | {edge[1], edge[2]})
            if rest is not None:
                return [edge]+rest
        return None

    return search(set(colors[0]), set())


def check_short_head():
    records = records_through(2**20)
    events, bursts = events_and_bursts(records)
    witness, failure = [], None
    for burst in bursts:
        cover = burst_cover(burst, 8, 5)
        if cover is None:
            failure = burst
            break
        witness.extend(cover)
    assert len(witness) == 43
    assert failure[0:4] == (497664, 589824, 43, 44)
    assert set(failure[4]) == {(0, 12), (8, 7), (16, 2)}
    assert span(failure[4]) == (16, 10)
    assert len({p for edge in witness for p in edge}) == 129
    for t, counts in events:
        if t > 2**19:
            break
        assert sum(max(map(arrival, edge)) <= t for edge in witness) == min(counts)
    assert all(dx <= 8 and dy <= 5 for dx, dy in map(span, witness))
    palette = sorted(set(map(normalized, witness)))
    print('SHORT_HEAD', 2**19, 'TRIPLES', len(witness), 'SHAPES', len(palette))
    print('PALETTE', palette)
    print('HEAD_WITNESS', witness)

    # A genuine alternating trade, with every completion time retained.
    colors = [[p for _, p, j in records if j == c] for c in range(3)]
    original = [tuple(c[k] for c in colors) for k in (26, 27, 28)]
    traded = [((13, 1), (10, 3), (14, 0)),
              ((4, 7), (12, 2), (7, 5)),
              ((2, 8), (1, 9), (9, 4))]
    assert sorted(p for e in original for p in e) == sorted(p for e in traded for p in e)
    assert [max(map(arrival, e)) for e in original] == [27648, 36864, 41472]
    assert [max(map(arrival, e)) for e in traded] == [27648, 36864, 41472]
    assert all(dx <= 8 and dy <= 5 for dx, dy in map(span, traded))

    t, point = F(995328), (12, 5)
    pools = []
    for j in range(3):
        previous_zero = max(s for s, counts in events
                            if s < t and counts[j] == min(counts))
        pools.append([p for value, p, color in records
                      if color == j and previous_zero < value <= t])
    admissible = [(pools[1][0], p, q) for p, q in product(pools[0], pools[2])
                  if span((point, p, q))[0] <= 8 and span((point, p, q))[1] <= 5]
    assert pools[1] == [point]
    assert admissible == [((12, 5), (15, 3), (18, 1))]
    print('FORCED_LOCAL_COLLINEAR', admissible[0])
    return witness


def check_forced_corner_bounds(horizontal, vertical, expected):
    events, bursts = events_and_bursts(records_through(2**(2*horizontal)))
    forced = [burst for burst in bursts if burst[3] == burst[2]+1]
    bad = [burst for burst in forced if
           span(burst[4])[0] > horizontal or span(burst[4])[1] > vertical]
    assert all(len(burst[4]) == 3 for burst in forced)
    assert all(dx >= 6 and dy >= 6 for dx, dy in (span(b[4]) for b in bad))
    lower_a = max(max(a for a, b in burst[4]) for burst in bad)+1
    lower_b = max(max(b for a, b in burst[4]) for burst in bad)+1
    assert (len(forced), len(bad), lower_a, lower_b) == expected
    maximum_span = (max(span(b[4])[0] for b in bad),
                    max(span(b[4])[1] for b in bad))
    print('BOX', (horizontal, vertical), 'FORCED', len(forced),
          'OVESPAN', len(bad), 'MAX_SPAN', maximum_span,
          'NECESSARY_CORNER', (lower_a, lower_b))
    print('A_WITNESS', max(bad, key=lambda b: max(a for a, _ in b[4]))[:5])
    print('B_WITNESS', max(bad, key=lambda b: max(v for _, v in b[4]))[:5])


def check_progression(q, p, expected_before):
    triple = {(0, 2*p+2), (q, p+2), (2*q, 2)}
    first, last = min(map(arrival, triple)), max(map(arrival, triple))
    assert first.denominator == last.denominator == 1
    first, last = int(first), int(last)
    before, after, inside = [0, 0, 0], [0, 0, 0], []
    a, power_two = 0, 1
    while power_two <= last:
        b, raw = 0, power_two
        while raw <= last:
            numerator, denominator = ((3*raw, 2) if b == 0 and a >= 1 else
                                      (9*raw, 8) if b == 1 and a >= 2 else (raw, 1))
            color = (a-b) % 3
            if numerator < first*denominator:
                before[color] += 1
            if numerator <= last*denominator:
                after[color] += 1
                if numerator >= first*denominator:
                    inside.append((a, b))
            b, raw = b+1, raw*3
        a, power_two = a+1, power_two*2
    assert tuple(before) == expected_before
    assert set(inside) == triple and len(inside) == 3
    assert after == [value+1 for value in before]
    print('PROGRESSION', (q, p), 'BEFORE', before, 'AFTER', after,
          'BALANCED_RESET', len(set(before)) == 1)


if __name__ == '__main__':
    assert arrival((2, 1)) == F(27, 2)
    check_short_head()
    check_forced_corner_bounds(27, 17, (161, 29, 53, 34))
    check_forced_corner_bounds(84, 53, (1420, 82, 168, 96))
    for q, p, before in [(8, 5, (43, 43, 43)), (19, 12, (189, 189, 189)),
                         (65, 41, (1900, 1900, 1900)),
                         (84, 53, (3127, 3127, 3127)),
                         (485, 306, (99852, 99851, 99852))]:
        check_progression(q, p, before)
    print('PASS: actual short-shape head, zero-cost trade, forced bursts and corner bounds')
