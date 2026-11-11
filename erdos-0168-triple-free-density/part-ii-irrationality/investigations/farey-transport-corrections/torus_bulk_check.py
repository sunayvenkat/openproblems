from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def arrival(x):
    a, b = x
    assert a >= 0 and b >= 0
    t = F(2**a * 3**b)
    if b == 0 and a >= 1:
        t *= F(3, 2)
    if b == 1 and a >= 2:
        t *= F(9, 8)
    return t


def node(x):
    return x[0] % 6 + 6*(x[1] % 6)


def tokens(limit):
    out = []
    a, x = 0, 1
    while x <= limit:
        b, d = 0, x
        while d <= limit:
            t = arrival((a, b))
            if t <= limit:
                out.append(((a, b), t, (a-b) % 3))
            b, d = b+1, d*3
        a, x = a+1, x*2
    return out


def prepare(u, v):
    assert abs(u[0]*v[1]-u[1]*v[0]) == 1
    assert {(u[0]-u[1]) % 3, (v[0]-v[1]) % 3} == {1, 2}
    h = max(0, u[0], v[0])-min(0, u[0], v[0])
    n = (5*h+1)//2
    recs = tokens(2**n)
    times = sorted({t for _, t, _ in recs})
    index = {t: i for i, t in enumerate(times)}
    counts = [0, 0, 0]
    changes = defaultdict(lambda: [0, 0, 0])
    for _, t, c in recs:
        changes[t][c] += 1
    lags = []
    for t in times:
        counts = [counts[c]+changes[t][c] for c in range(3)]
        low = min(counts)
        lags.append(tuple(x-low for x in counts))
    types = []
    for sign in (1, -1):
        offsets = ((0, 0), (sign*u[0], sign*u[1]), (sign*v[0], sign*v[1]))
        for b0 in range(6):
            for a0 in range(6):
                residues = tuple(node((a0+x, b0+y)) for x, y in offsets)
                assert len(set(residues)) == 3
                mask = sum(1 << k for k in residues)
                types.append((sign, (a0, b0), offsets, residues, mask))
    profiles, first_bad, witnesses = [], [], []
    for sign, residue, offsets, nodes, mask in types:
        seen, groups = set(), []
        for point, _, _ in recs:
            k = node(point)
            if k not in nodes:
                continue
            delta = offsets[nodes.index(k)]
            anchor = point[0]-delta[0], point[1]-delta[1]
            assert node(anchor) == node(residue)
            if anchor in seen:
                continue
            seen.add(anchor)
            triple = tuple(add(anchor, z) for z in offsets)
            if min(z[0] for z in triple) < 0 or min(z[1] for z in triple) < 0:
                continue
            assert {(a-b) % 3 for a, b in triple} == {0, 1, 2}
            groups.append(tuple((arrival(z), (z[0]-z[1]) % 3) for z in triple))
        updates = defaultdict(lambda: [0, 0, 0])
        for triple in groups:
            last = max(t for t, _ in triple)
            for t, c in triple:
                if t <= times[-1]:
                    updates[index[t]][c] += 1
            if last <= times[-1]:
                for c in range(3):
                    updates[index[last]][c] -= 1
        vals, profile, ban, witness = [0, 0, 0], [], len(times), None
        for i, t in enumerate(times):
            vals = [vals[c]+updates[i][c] for c in range(3)]
            assert min(vals) >= 0
            profile.append(tuple(vals))
            if ban == len(times):
                for c in range(3):
                    if vals[c] > lags[i][c]:
                        ban, witness = i, (t, c, vals[c], lags[i][c])
                        break
        profiles.append(profile)
        first_bad.append(ban)
        witnesses.append(witness)
    return types, times, lags, profiles, first_bad, witnesses


def cover_at(types, bans, end):
    masks = [x[4] for x in types]
    allowed = [k for k in range(72) if bans[k] > end]
    by_node = [[k for k in allowed if masks[k] >> j & 1] for j in range(36)]
    calls = 0

    @lru_cache(None)
    def solve(mask):
        nonlocal calls
        calls += 1
        if mask == (1 << 36)-1:
            return ()
        options = None
        for j in range(36):
            if not (mask >> j & 1):
                candidates = [k for k in by_node[j] if not (masks[k] & mask)]
                if not candidates:
                    return None
                if options is None or len(candidates) < len(options):
                    options = candidates
        for k in options:
            tail = solve(mask | masks[k])
            if tail is not None:
                return (k,) + tail
        return None

    result = solve(0)
    return result, calls, len(allowed), [j for j in range(36) if not by_node[j]]


if __name__ == '__main__':
    cases = (((8, -5), (3, -2), 6561),
             ((19, -12), (27, -17), 3057647616))
    for u, v, expected in cases:
        types, times, lags, profiles, bans, witnesses = prepare(u, v)
        assert cover_at(types, bans, -1)[0] is not None
        at_end = cover_at(types, bans, len(times)-1)
        print('TARGET', u, v, 'events', len(times), 'last', times[-1], 'cover', at_end)
        assert at_end[0] is None
        if at_end[0] is None:
            lo, hi = -1, len(times)-1
            while hi-lo > 1:
                mid = (lo+hi)//2
                if cover_at(types, bans, mid)[0] is None:
                    hi = mid
                else:
                    lo = mid
            result = cover_at(types, bans, hi)
            assert times[hi] == expected and result[0] is None
            print('FIRST_INDIVIDUAL_FILTER_OBSTRUCTION', times[hi], result)
            previous = cover_at(types, bans, hi-1)[0]
            assert previous is not None and len(previous) == 12
            union = 0
            for k in previous:
                assert not union & types[k][4]
                union |= types[k][4]
            assert union == (1 << 36)-1
            print('PREVIOUS_RELAXED_WITNESS', previous)
            print('PREVIOUS_EVENT', times[hi-1])
            failures = []
            for i, t in enumerate(times[:hi]):
                for c in range(3):
                    total = sum(profiles[k][i][c] for k in previous)
                    if total > lags[i][c]:
                        failures.append((t, c, total, lags[i][c]))
            print('PREVIOUS_WITNESS_JOINT_FAILURES', failures[:3])
            assert not failures
            print('BANNED_TYPES', [(k, types[k][0], types[k][1], witnesses[k])
                                   for k in range(72) if bans[k] <= hi])
        else:
            selected = at_end[0]
            failures = []
            for i, t in enumerate(times):
                for c in range(3):
                    total = sum(profiles[k][i][c] for k in selected)
                    if total > lags[i][c]:
                        failures.append((t, c, total, lags[i][c]))
            print('RELAXED_WITNESS_CAPACITY_FAILURES', failures[:3])
    print('PASS: exact retimed counts, individual-capacity bans and exhaustive torus cover replay')
