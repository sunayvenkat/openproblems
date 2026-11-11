"""Independent exact audit; imports no companion checker and writes no files."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import cache
from itertools import product


def arrival(z, asym=False):
    a, b = z
    assert min(z) >= 0
    value = F(2**a * 3**b)
    if b == 0 and (a >= 1 or asym):
        value *= F(3, 2)
    elif b == 1 and (a >= 2 or asym):
        value *= F(9, 8)
    return value


def color(z):
    return (z[0] - z[1]) % 3


def events(cap):
    out = defaultdict(list)
    a = 0
    while 2**a <= cap:
        b = 0
        while 2**a * 3**b <= cap:
            z = a, b
            if arrival(z) <= cap:
                out[arrival(z)].append(z)
            b += 1
        a += 1
    return sorted(out.items())


def imbalance_head(cutoff):
    counts, last, integral = [0, 0, 0], F(1), F()
    e, jumps, births = 0, F(), F()
    for time, tokens in events(cutoff):
        integral += e * (1 / last - 1 / time)
        old_min = min(counts)
        for z in tokens:
            counts[color(z)] += 1
        next_e = sum(counts) - 3 * min(counts)
        jumps += (next_e - e) / time
        births += (min(counts) - old_min) / time
        e, last = next_e, time
    integral += e * (1 / last - F(1, cutoff))
    lower = F(19, 54) + integral
    assert lower == F(19, 54) + jumps - F(e, cutoff)
    return lower, e, births


def log3_floor(value):
    result, power = 0, 1
    while 3 * power <= value:
        result, power = result + 1, 3 * power
    return result


def ternary_exponent(denominator):
    result = 0
    while denominator % 3 == 0:
        result, denominator = result + 1, denominator // 3
    return result


def forcing_tail(cutoff):
    m = log3_floor(2 * cutoff)
    r = [(m + j + 1) % 3 for j in range(3)]
    return F(r[0], cutoff) + F(-8*r[0] + 6*r[1] + 2*r[2], 13*3**m)


def plane(u, v, phase=(0, 0)):
    """Build incidence by a 6x6 residue cell, rather than invert each point."""
    assert abs(u[0]*v[1] - v[0]*u[1]) == 1
    assert {color(u), color(v)} == {1, 2}
    shapes = [((0, 0), u, v),
              ((u[0]+v[0], u[1]+v[1]),
               (2*u[0], 2*u[1]), (2*u[0]+v[0], 2*u[1]+v[1]))]
    lattice = {((3*i*u[0]+2*j*v[0]) % 6,
                (3*i*u[1]+2*j*v[1]) % 6)
               for i in range(2) for j in range(3)}
    assert len(lattice) == 6
    families, incidence = [], {}
    for shape in shapes:
        lo = tuple(min(z[k] for z in shape) for k in range(2))
        offsets = tuple((z[0]-lo[0], z[1]-lo[1]) for z in shape)
        for residue in sorted(lattice):
            anchor = tuple((phase[k]+residue[k]+lo[k]) % 6 for k in range(2))
            families.append((anchor, offsets))
            for point in offsets:
                key = tuple((anchor[k]+point[k]) % 6 for k in range(2))
                assert key not in incidence
                incidence[key] = tuple((z[0]-point[0], z[1]-point[1]) for z in offsets)
    assert len(incidence) == 36

    def owner(z):
        return tuple(sorted((z[0]+d[0], z[1]+d[1])
                            for d in incidence[z[0] % 6, z[1] % 6]))

    def residual(z):
        return any(min(w) < 0 for w in owner(z))

    total = F()
    for anchor, offsets in families:
        group = tuple((anchor[0]+d[0], anchor[1]+d[1]) for d in offsets)
        assert owner(group[0]) == tuple(sorted(group))
        raw = max(2**a * 3**b for a, b in group)
        total += (1 / max(map(arrival, group))
                  + 1 / (63 * max(arrival(z, True) for z in group))
                  + F(64, 63*728*raw))
        for n, m in ((1, 0), (2, 0), (0, 1), (1, 2)):
            moved = [(a+6*n, b+6*m) for a, b in group]
            expected = (max(arrival(z, True) for z in group)*64**n if m == 0
                        else raw*64**n*729**m)
            assert max(map(arrival, moved)) == expected
    return owner, residual, total, lattice


def rank_groups(tokens):
    rows = [sorted((z for z in tokens if color(z) == c), key=lambda z: (arrival(z), z))
            for c in range(3)]
    assert len({len(row) for row in rows}) == 1
    return [tuple(sorted(g)) for g in zip(*rows)]


def cost(groups):
    return sum((1 / max(map(arrival, g)) for g in groups), F())


def repair(u, v, phase=(0, 0)):
    owner, residual, bulk, lattice = plane(u, v, phase)
    H, V = max(u[0], v[0]), max(-u[1], -v[1])
    A, B = 6*((H+5)//6), 6*((V+5)//6)
    corner = [z for z in product(range(A), range(B)) if residual(z)]
    left = [[z for z in product(range(A), range(B, B+6))
             if residual(z) and color(z) == c] for c in range(3)]
    bottom = [z for z in product(range(A, A+6), range(B)) if residual(z)]
    assert len({len(row) for row in left}) == 1
    assert len({sum(color(z) == c for z in bottom) for c in range(3)}) == 1
    n = len(left[0])
    assert n > 0 and abs(n-H) <= 10
    c = [sum(color(z) == j for z in corner) for j in range(3)]
    d = [max(c)-value for value in c]
    J = (max(d)+n-1)//n
    assert max(d) <= 36*(H+V+6)
    if H >= 20 and V <= H:
        assert J <= 180

    def token(j, index):
        m, r = divmod(index, n)
        a, b = left[j][r]
        return a, b+6*m

    head = rank_groups(corner + [token(j, i) for j in range(3) for i in range(d[j])])
    bottom_groups = rank_groups(bottom)
    head_owner = {z: g for g in head for z in g}
    bottom_owner = {z: g for g in bottom_groups for z in g}
    slots = [{z: k for k, z in enumerate(row)} for row in left]

    def complete_group(z):
        if not residual(z):
            return owner(z)
        if z in head_owner:
            return head_owner[z]
        a, b = z
        if a >= A:
            m, r = divmod(a-A, 6)
            return tuple(sorted((x+6*m, y) for x, y in bottom_owner[A+r, b]))
        j = color(z)
        m, r = divmod(b-B, 6)
        index = n*m + slots[j][a, B+r] - d[j]
        assert index >= 0
        return tuple(sorted(token(k, d[k]+index) for k in range(3)))

    left_phase = [tuple(token(j, d[j]+r) for j in range(3)) for r in range(n)]
    full = bulk + cost(head) + F(64, 63)*cost(bottom_groups) + F(729, 728)*cost(left_phase)
    clear = 63*728*2**6*3**6 * 2**A * 3**(B+6*J)
    assert (full*clear).denominator == 1
    for z in product(range(A+7), range(B+6*(J+2))):
        g = complete_group(z)
        assert z in g and {color(w) for w in g} == {0, 1, 2}
        assert all(complete_group(w) == g for w in g)
    return owner, residual, complete_group, bulk, full, lattice


def deficits(u, v, phase, cap):
    owner, residual, group, bulk, full, lattice = repair(u, v, phase)
    records = events(cap)
    tokens = [z for _, row in records for z in row]
    bulk_groups = {owner(z) for z in tokens if not residual(z)}
    all_groups = {group(z) for z in tokens}
    bulk_done = Counter(max(map(arrival, g)) for g in bulk_groups)
    all_done = Counter(max(map(arrival, g)) for g in all_groups)
    counts, remainder = [0, 0, 0], [0, 0, 0]
    done_bulk = done_all = 0
    first_forced = first_actual = None
    for position, (time, row) in enumerate(records):
        for z in row:
            counts[color(z)] += 1
            remainder[color(z)] += residual(z)
        done_bulk += bulk_done[time]
        done_all += all_done[time]
        forced = min(counts)-done_bulk-min(remainder)
        assert 0 <= forced <= min(counts)-done_all
        if first_forced is None and forced:
            following = records[position+1][0]
            first_forced = time, following, forced*(1/time-1/following)
        if first_actual is None and min(counts) > done_all:
            first_actual = time
    return first_forced, first_actual, bulk, full, lattice


assert arrival((2, 1)) == F(27, 2)
assert F(3)-F(1, 3)-F(1, 54) == F(143, 54)
assert F(3)-F(143, 54) == F(19, 54)
assert imbalance_head(8)[0] == F(119, 108)  # The zero convergent is excluded from IT11.
assert imbalance_head(64)[0] == F(2065, 1728)
for p, q, expected_v3 in ((5, 8, 15), (12, 19, 34), (41, 65, 123)):
    X = 2**(3*q)
    lower = imbalance_head(X)[0]
    upper = 2*imbalance_head(2*X)[0]-lower+forcing_tail(X)
    assert ternary_exponent(lower.denominator) == expected_v3
    assert (lower*2**(3*q)*3**max(log3_floor(X), 3)).denominator == 1
    assert (upper*13*2**(3*q+1)*3**max(log3_floor(2*X), 3)).denominator == 1

cases = [((8, -5), (3, -2), F(503, 108864), F(40448827, 67931136),
          F(243), F(288), F(5, 7776)),
         ((19, -12), (27, -17), F(5386433, 1497904875307008),
          F(538175119414808197, 901310762113302528),
          F(382205952), F(387420489), F(7153, 203119913336832)),
         ((84, -53), (65, -41), None, None, F(61966892988215484494118912),
          F(62812323716259432401731584),
          F(7153, 32931747576550225295039048712192))]
for u, v, bulk_expected, full_expected, t, following, gap in cases:
    forced, actual, bulk, full, lattice = deficits(u, v, (0, 0), 2**(max(u[0], v[0])+5))
    assert forced == (t, following, gap)
    if bulk_expected is not None:
        assert (bulk, full) == (bulk_expected, full_expected)
    print({'basis': (u, v), 'full_denominator_bits': full.denominator.bit_length(),
           'first_actual': str(actual), 'first_forced': tuple(map(str, forced))})

phase_cases = [((8, -5), (3, -2),
                {(0, 0): 243, (1, 0): 243, (2, 0): 486,
                 (3, 0): 1458, (4, 0): 2187, (5, 0): 4608},
                (5, 0), F(13501693, 22643712), 1458),
               ((19, -12), (27, -17),
                {(0, 0): 382205952, (0, 1): 129140163,
                 (1, 0): 429981696, (1, 1): 129140163,
                 (2, 0): 805306368, (2, 1): 258280326},
                (2, 0), F(11301677504582126401, 18927526004379353088), 429981696)]
for u, v, expected, best_phase, best_cost, best_actual in phase_cases:
    lattice = plane(u, v)[3]
    representatives = {min(((a-x) % 6, (b-y) % 6) for x, y in lattice)
                       for a, b in product(range(6), repeat=2)}
    assert representatives == set(expected)
    H = max(u[0], v[0])
    for phase, first in expected.items():
        forced, actual, _, full, _ = deficits(u, v, phase, 2**((5*H+1)//2))
        assert forced[0] == first < 2**(2*H)
        if phase == best_phase:
            assert full == best_cost and actual == best_actual
            assert full.denominator*forced[2] > 1
            assert 3*(3-3*full).denominator*forced[2] > 1
    print({'basis': (u, v), 'distinct_phases': len(representatives),
           'latest_first_forced': max(expected.values())})


def torus_capacity(u, v, cutoff, previous_witness):
    records = events(cutoff)
    times = [t for t, _ in records]
    points = [z for _, row in records for z in row]
    counts, lags = [0, 0, 0], []
    for _, row in records:
        for z in row:
            counts[color(z)] += 1
        lags.append(tuple(x-min(counts) for x in counts))
    profiles, masks = [], []
    for sign in (1, -1):
        offsets = ((0, 0), (sign*u[0], sign*u[1]), (sign*v[0], sign*v[1]))
        for b, a in product(range(6), repeat=2):
            nodes = tuple(((a+x) % 6)+6*((b+y) % 6) for x, y in offsets)
            assert len(set(nodes)) == 3
            masks.append(sum(1 << k for k in nodes))
            triples = set()
            for point in points:
                for dx, dy in offsets:
                    anchor = point[0]-dx, point[1]-dy
                    if (anchor[0] % 6, anchor[1] % 6) == (a, b):
                        g = tuple((anchor[0]+x, anchor[1]+y) for x, y in offsets)
                        if all(min(z) >= 0 for z in g):
                            triples.add(g)
            changes = defaultdict(lambda: [0, 0, 0])
            for g in triples:
                end = max(map(arrival, g))
                for z in g:
                    if arrival(z) <= cutoff:
                        changes[arrival(z)][color(z)] += 1
                if end <= cutoff:
                    for c in range(3):
                        changes[end][c] -= 1
            state, profile = [0, 0, 0], []
            for t in times:
                state = [state[c]+changes[t][c] for c in range(3)]
                assert min(state) >= 0
                profile.append(tuple(state))
            profiles.append(profile)
    assert len(profiles) == 72
    allowed = [k for k in range(72)
               if all(profiles[k][i][c] <= lags[i][c]
                      for i in range(len(times)) for c in range(3))]
    target = (1 << 36)-1

    @cache
    def exact_cover(used):
        if used == target:
            return True
        choices = [[k for k in allowed if masks[k] & (1 << j) and not masks[k] & used]
                   for j in range(36) if not used & (1 << j)]
        options = min(choices, key=len)
        return any(exact_cover(used | masks[k]) for k in options)

    assert not exact_cover(0)
    covered = 0
    for k in previous_witness:
        assert not covered & masks[k]
        covered |= masks[k]
    assert covered == target and len(previous_witness) == 12
    assert all(sum(profiles[k][i][c] for k in previous_witness) <= lags[i][c]
               for i in range(len(times)-1) for c in range(3))
    print({'basis': (u, v), 'first_torus_capacity_infeasibility': cutoff,
           'previous_event': str(times[-2]), 'allowed_types': len(allowed)})


torus_capacity((8, -5), (3, -2), 6561,
               (15, 17, 70, 14, 66, 13, 69, 16, 71, 67, 12, 68))
torus_capacity((19, -12), (27, -17), 3057647616,
               (5, 38, 3, 52, 9, 50, 56, 23, 27, 68, 21, 70))
print('PASS: independent scalar arithmetic, full repairs, six phases and torus capacity certificates')
