from fractions import Fraction as F


CASES = (
    ((8, -5), (3, -2), 6561, 6144, 50,
     (-2, -1, -2, -2, -1, -2, -1, 0, -2, -1, 1, 2,
      -2, -1, -1, 2, 1, 1, 0, 1, 0, 2, 3, 0,
      -1, 2, 2, 1, 1, 0, 0, 1, -1, -1, -2, 1),
     ((729, 0, 4), (1458, 1, 2), (2916, 1, 1), (6561, 2, 1),
      (2187, 1, 3), (6561, 1, 4), (864, 2, 2), (3456, 1, 3),
      (4608, 1, 2), (243, 1, 1), (486, 2, 3), (1458, 2, 3), (2187, 2, 2)),
     (15, 17, 70, 14, 66, 13, 69, 16, 71, 67, 12, 68)),
    ((19, -12), (27, -17), 3057647616, 2902376448, 53,
     (-2, -2, -2, -2, -2, 1, 1, 1, 1, -2, 1, 1,
      1, -2, 1, 1, -2, 1, 1, 1, -2, 1, 1, -2,
      -2, 1, 1, -2, 4, 1, -2, -2, 1, 1, -2, 4),
     ((382205952, 1, 6), (764411904, 2, 3), (1528823808, 0, 3),
      (3057647616, 1, 3), (129140163, 1, 6), (258280326, 0, 3),
      (1019215872, 2, 3), (2293235712, 0, 6), (258280326, 2, 6),
      (429981696, 0, 3), (805306368, 1, 3)),
     (5, 38, 3, 52, 9, 50, 56, 23, 27, 68, 21, 70)),
)


def time_at(a, b):
    assert a >= 0 and b >= 0
    if b == 0 and a:
        return F(3 * 2**(a-1))
    if b == 1 and a >= 2:
        return F(27 * 2**max(a-3, 0), 2**max(3-a, 0))
    return F(2**a * 3**b)


def exponent_bound(base, limit):
    n = 0
    while base**(n+1) <= limit:
        n += 1
    return n


def head_records(limit):
    return [(a, b, time_at(a, b))
            for a in range(exponent_bound(2, limit)+1)
            for b in range(exponent_bound(3, limit)+1)
            if time_at(a, b) <= limit]


def profiles(u, v, limit):
    records = head_records(limit)
    times = sorted({t for _, _, t in records})
    counts = {t: tuple(sum(s <= t and (a-b) % 3 == c for a, b, s in records)
                       for c in range(3)) for t in times}
    lag = {t: tuple(n-min(counts[t]) for n in counts[t]) for t in times}
    masks, partials = [], []
    for sign in (1, -1):
        offsets = ((0, 0), (sign*u[0], sign*u[1]), (sign*v[0], sign*v[1]))
        lo_a, lo_b = min(a for a, _ in offsets), min(b for _, b in offsets)
        normalized = tuple((a-lo_a, b-lo_b) for a, b in offsets)
        for b0 in range(6):
            for a0 in range(6):
                nodes = {(a0+a) % 6 + 6*((b0+b) % 6) for a, b in offsets}
                assert len(nodes) == 3
                masks.append(nodes)
                # Enumerate coordinatewise minima directly, not anchors recovered from tokens.
                groups = []
                for a in range((a0+lo_a) % 6, exponent_bound(2, limit)+1, 6):
                    for b in range((b0+lo_b) % 6, exponent_bound(3, limit)+1, 6):
                        triple = tuple((a+x, b+y) for x, y in normalized)
                        assert {(x-y) % 3 for x, y in triple} == {0, 1, 2}
                        group = tuple((time_at(x, y), (x-y) % 3) for x, y in triple)
                        if min(s for s, _ in group) <= limit:
                            groups.append(group)
                partials.append({t: tuple(sum(s <= t and color == c
                    for group in groups if max(s for s, _ in group) > t
                    for s, color in group) for c in range(3)) for t in times})
    assert len(masks) == len(partials) == 72
    return times, counts, lag, masks, partials


def periodic_certificate(case):
    u, v, limit, previous, expected, weights, rows, cover = case
    times, _, lag, masks, partials = profiles(u, v, limit)
    assert times[-2:] == [previous, limit] and F(27, 2) in times
    allowed = [k for k in range(72) if not any(lag[t][c] == 0 and partials[k][t][c]
               for t in times for c in range(3))]
    assert len(allowed) == expected
    charges = [sum(weights[j] for j in mask) for mask in masks]
    assert sum(weights) in (-2, -3) and min(charges[k] for k in allowed) >= 0
    assert all(t <= limit and lag[t][c] == 0 and n > 0 for t, c, n in rows)
    full = [charges[k]+sum(n*partials[k][t][c] for t, c, n in rows) for k in range(72)]
    assert min(full) >= 0
    assert len(set(cover)) == 12
    assert all(sum(j in masks[k] for k in cover) == 1 for j in range(36))
    assert all(sum(partials[k][t][c] for k in cover) <= lag[t][c]
               for t in times[:-1] for c in range(3))
    if limit == 3057647616:
        s = {0, 1, 2, 3, 4, 9, 13, 16, 20, 23, 24, 27, 30, 31, 34}
        t = {28, 35}
        assert len(s)-len(t) == 13
        assert all(len(masks[k] & s)-len(masks[k] & t) <= 1 for k in allowed)
    print('INDEPENDENT_PERIODIC_PASS', limit, 'previous', previous,
          'events', len(times), 'survivors', len(allowed), 'dual', sum(weights))


def local_certificate():
    z, u, v = (12, 5), (8, -5), (3, -2)
    records = head_records(2**21)
    times = sorted({t for _, _, t in records})
    cutoffs, nexts, colors = (F(839808), F(995328)), (F(884736), F(1062882)), (2, 1)
    assert time_at(2, 1) == F(27, 2)
    assert time_at(*z) == cutoffs[1]
    groups = []
    for sign in (1, -1):
        offsets = ((0, 0), (sign*u[0], sign*u[1]), (sign*v[0], sign*v[1]))
        for dx, dy in offsets:
            groups.append(tuple((z[0]-dx+x, z[1]-dy+y) for x, y in offsets))
    assert len({frozenset(g) for g in groups}) == 6
    intervals = []
    for i, (start, stop, c) in enumerate(zip(cutoffs, nexts, colors)):
        counts = tuple(sum(t <= start and (a-b) % 3 == j for a, b, t in records) for j in range(3))
        assert counts == ((46, 46, 46), (48, 47, 47))[i]
        assert counts[c] == min(counts)
        assert times[times.index(start)+1] == stop
        intervals.append({k for k, triple in enumerate(groups)
            if any((a-b) % 3 == c and time_at(a, b) <= start for a, b in triple)
            and max(time_at(a, b) for a, b in triple) >= stop})
    assert intervals == [{1, 5}, {0, 2, 3, 4}]
    assert all(min(min(point) for point in g) >= 0 for g in groups)
    assert cutoffs[0] < nexts[0] <= cutoffs[1] < nexts[1]
    gap = min(1/a-1/b for a, b in zip(cutoffs, nexts))
    assert gap == F(13, 214990848)
    print('INDEPENDENT_PERIOD_FREE_PASS', intervals, 'gap', gap)


if __name__ == '__main__':
    for case in CASES:
        periodic_certificate(case)
    local_certificate()
    print('PASS: independent normalized geometry, full fractional duals, firstness and local gap')
