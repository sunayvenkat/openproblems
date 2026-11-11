from collections import defaultdict
from fractions import Fraction as F


def arrival(z):
    a, b = z
    assert a >= 0 and b >= 0
    value = F(2**a * 3**b)
    if b == 0 and a >= 1:
        value *= F(3, 2)
    if b == 1 and a >= 2:
        value *= F(9, 8)
    return value


def normalize(points):
    aa, bb = min(a for a, _ in points), min(b for _, b in points)
    return tuple(sorted((a-aa, b-bb) for a, b in points))


def palette(vectors, h, v):
    shapes = set()
    for u in vectors:
        for w in vectors:
            if {(u[0]-u[1]) % 3, (w[0]-w[1]) % 3} != {1, 2}:
                continue
            for sign in (1, -1):
                shape = normalize(((0, 0), (sign*u[0], sign*u[1]),
                                   (sign*w[0], sign*w[1])))
                if max(a for a, _ in shape) <= h and max(b for _, b in shape) <= v:
                    assert len({(a-b) % 3 for a, b in shape}) == 3
                    shapes.add(shape)
    for u in vectors:
        if (u[0]-u[1]) % 3:
            shape = normalize(((0, 0), u, (2*u[0], 2*u[1])))
            if max(a for a, _ in shape) <= h and max(b for _, b in shape) <= v:
                shapes.add(shape)
    return sorted(shapes)


def head_records(limit):
    records, a, power2 = [], 0, 1
    while power2 <= limit:
        b, raw = 0, power2
        while raw <= limit:
            z = a, b
            value = arrival(z)
            if value <= limit:
                records.append((value, z, (a-b) % 3))
            b, raw = b+1, raw*3
        a, power2 = a+1, power2*2
    return sorted(records)


def prepare(shapes, limit):
    records = head_records(limit)
    times = sorted({t for t, _, _ in records})
    index = {t: i for i, t in enumerate(times)}
    changes = defaultdict(lambda: [0, 0, 0])
    for t, _, color in records:
        changes[t][color] += 1
    counts, lags, running = [], [], [0]*3
    for t in times:
        running = [running[c]+changes[t][c] for c in range(3)]
        counts.append(tuple(running))
        lags.append(tuple(n-min(running) for n in running))
    aa = max(a for _, (a, _), _ in records)
    bb = max(b for _, (_, b), _ in records)
    types, profiles, completions = [], [], []
    for shape in shapes:
        for b0 in range(6):
            for a0 in range(6):
                nodes = tuple((a0+a) % 6 + 6*((b0+b) % 6) for a, b in shape)
                assert len(set(nodes)) == 3
                types.append((shape, (a0, b0), nodes))
                updates = defaultdict(lambda: [0, 0, 0])
                ends = defaultdict(int)
                for a in range(a0, aa+1, 6):
                    for b in range(b0, bb+1, 6):
                        triple = tuple((a+x, b+y) for x, y in shape)
                        events = tuple((arrival(z), (z[0]-z[1]) % 3) for z in triple)
                        last = max(t for t, _ in events)
                        for t, color in events:
                            if t <= limit:
                                updates[index[t]][color] += 1
                        if last <= limit:
                            ends[index[last]] += 1
                            for color in range(3):
                                updates[index[last]][color] -= 1
                partial, done, prof, completed = [0]*3, 0, [], []
                for i in range(len(times)):
                    partial = [partial[c]+updates[i][c] for c in range(3)]
                    done += ends[i]
                    assert min(partial) >= 0
                    prof.append(tuple(partial))
                    completed.append(done)
                profiles.append(prof)
                completions.append(completed)
    return types, times, records, counts, lags, profiles, completions


def kept_owners(z, types, allowed):
    node = z[0] % 6 + 6*(z[1] % 6)
    out = []
    for j, k in enumerate(allowed):
        shape, _, nodes = types[k]
        if node in nodes:
            dx, dy = shape[nodes.index(node)]
            if z[0] >= dx and z[1] >= dy:
                out.append(j)
    return out


def actual_system(data, allowed, h, v, aend=None, bend=None):
    types, times, records, counts, _, _, _ = data
    aend = 6*((h+5)//6) if aend is None else aend
    bend = 6*((v+5)//6) if bend is None else bend
    assert aend >= max(h, 6) and bend >= max(v, 6)
    n = len(allowed)
    eqs = [([int(node in types[k][2]) for k in allowed], 1) for node in range(36)]
    rectangles = ((range(aend), range(bend)),
                  (range(aend, aend+6), range(bend)),
                  (range(aend), range(bend, bend+6)))
    for aa, bb in rectangles:
        total, coefs = [0]*3, [[0]*n for _ in range(3)]
        for a in aa:
            for b in bb:
                c = (a-b) % 3
                total[c] += 1
                for j in kept_owners((a, b), types, allowed):
                    coefs[c][j] += 1
        for c in (1, 2):
            eqs.append(([coefs[0][j]-coefs[c][j] for j in range(n)], total[0]-total[c]))
    bytime = defaultdict(list)
    for t, z, c in records:
        bytime[t].append((z, c))
    components, states = {}, []
    for i, t in enumerate(times):
        for z, c in bytime[t]:
            a, b = z
            if a < aend and b < bend:
                key = ('C', 0)
            elif a >= aend and b < bend:
                key = ('R', (a-aend)//6)
            elif a < aend and b >= bend:
                key = ('L', (b-bend)//6)
            else:
                continue
            if key not in components:
                components[key] = ([0]*3, [[0]*n for _ in range(3)])
            total, coefs = components[key]
            total[c] += 1
            for j in kept_owners(z, types, allowed):
                coefs[c][j] += 1
        minimum = min(range(3), key=lambda c: counts[i][c])
        states.append((t, minimum, tuple((key, tuple(total), tuple(tuple(row) for row in coefs))
                       for key, (total, coefs) in components.items())))
    return eqs, states



CF = ((1, 0), (1, -1), (2, -1), (3, -2), (8, -5))
NUMERATORS = {
    1619: 1, 1799: 1, 2045: 2, 2231: 1, 2273: 1, 2625: 2, 2696: 1,
    2801: 1, 2806: 6, 2930: 4, 2940: 4, 2941: 5, 2944: 4, 3341: 2,
    3380: 5, 3381: 4, 3454: 1, 3455: 2, 3517: 3, 3689: 2, 3742: 1,
    3757: 5, 3759: 3, 3760: 3, 3765: 2, 3769: 4, 3850: 2, 3884: 1,
    3910: 1, 4005: 1, 4020: 6, 4211: 3,
}
HEAD17_DUAL = (
    -68, 66, 66, -139, 66, 66, 66, -68, 66, 66, -68, 62,
    60, 1, -68, -4, 66, -63, -132, 66, 19, -3, -33, -45,
    32, -143, 55, -45, 2, -33, 44, 32, 66, 66, -104, 66,
    -53, -77, 66, 66, 24, 36,
)


def combination_palette():
    vectors = sorted({(c*u[0]+d*v[0], c*u[1]+d*v[1])
        for u in CF for v in CF for c in range(-2, 3) for d in range(-2, 3)
        if (c, d) != (0, 0)
        and 0 <= c*u[0]+d*v[0] <= 8 and -5 <= c*u[1]+d*v[1] <= 0
        and (c*u[0]+d*v[0], c*u[1]+d*v[1]) != (0, 0)})
    shapes = palette(vectors, 8, 5)
    assert len(vectors) == 28 and len(shapes) == 118
    return shapes


def allowed_at(data, cutoff):
    return [k for k in range(len(data[0])) if not any(
        t <= cutoff and data[4][i][c] == 0 and data[5][k][i][c] > 0
        for i, t in enumerate(data[1]) for c in range(3))]


def check_smaller_capacity():
    shapes = palette(CF, 8, 5)
    assert len(shapes) == 11
    data = prepare(shapes, 2**16)
    chosen = (229, 240, 248, 250, 302, 303, 309, 313, 323, 334, 348, 391)
    assert all(sum(node in data[0][k][2] for k in chosen) == 1 for node in range(36))
    assert all(sum(data[5][k][i][c] for k in chosen) <= data[4][i][c]
               for i in range(len(data[1])) for c in range(3))
    print('CF_CAPACITY_PASS', len(shapes), 'shapes', 'head', 2**16)


def check_complete_cost(data, active, x):
    from pathlib import Path
    import runpy
    archive = Path(__file__).resolve().parent.parent / 'Erdos 168 fractional Farey transport'
    lib = runpy.run_path(str(archive / 'fractional_arithmetic_check.py'))
    weighted = []
    for k, mass in zip(active, x):
        shape, residue, nodes = data[0][k]
        weighted.append((shape, tuple((z % 6, z // 6) for z in nodes), mass, residue))
    regions = ((range(18), range(12)), (range(18, 24), range(12)),
               (range(18), range(12, 18)))
    groups, totals = [], []
    for aa, bb in regions:
        points = [((a, b), lib['residual']((a, b), weighted)) for a in aa for b in bb]
        batch, mass = lib['rank_groups'](points, 7)
        groups.append(batch)
        totals.append(mass)
    for group, _ in groups[1]:
        assert max(arrival((a+6, b)) for a, b in group) == 64*max(map(arrival, group))
    for group, _ in groups[2]:
        assert max(arrival((a, b+6)) for a, b in group) == 729*max(map(arrival, group))
    q = lib['bulk_cost'](weighted) + lib['cost'](groups[0])
    q += F(64, 63)*lib['cost'](groups[1]) + F(729, 728)*lib['cost'](groups[2])
    clearing = 7*63*728*2**6*3**6*2**18*3**12
    assert totals == [F(239, 7), F(50, 7), F(52, 7)]
    assert q == F(20605867009283, 34511190884352)
    assert clearing == 2086759741982823677952 and (clearing*q).denominator == 1
    print('COMPLETE_COST_PASS', q, 'clearing', clearing, 'mass/color', totals)


def check_complete_head(data):
    active = sorted(NUMERATORS)
    x = [F(NUMERATORS[k], 7) for k in active]
    assert len(active) == 32 and sum(x) == 12
    eqs, states = actual_system(data, active, 8, 5, 18, 12)
    assert all(sum(a*b for a, b in zip(row, x)) == rhs for row, rhs in eqs)
    first_loss, checked = None, 0
    for i, (t, minimum, components) in enumerate(states):
        done = sum(x[j]*data[6][k][i] for j, k in enumerate(active))
        for _, total, coefs in components:
            masses = [F(total[c])-sum(a*b for a, b in zip(coefs[c], x)) for c in range(3)]
            assert min(masses) >= 0
            done += min(masses)
        gap = min(data[3][i])-done
        assert gap >= 0
        if t <= 2**16:
            assert gap == 0
            checked += 1
        if gap and first_loss is None:
            first_loss = t, gap
    assert checked == 80 and first_loss == (F(73728), F(1))
    check_complete_cost(data, active, x)
    print('ACTUAL_HEAD_PASS', checked, 'events', 'head', 2**16, 'first loss', first_loss)


def check_minimal_component_obstruction(data):
    allowed = allowed_at(data, 2**16)
    assert len(allowed) == 339
    _, states = actual_system(data, allowed, 8, 5)
    t, minimum, components = next(state for state in states if state[0] == 729)
    _, total, coefs = next(item for item in components if item[0] == ('L', 0))
    assert minimum == 0 and total[0]-total[1] == 1
    assert coefs[0] == coefs[1] == (0,)*len(allowed)
    print('MINIMAL_CUT_OBSTRUCTION', t, 'C_L0,0=1 > C_L0,1=0')


def check_head17_balance_obstruction(data):
    allowed = allowed_at(data, 2**17)
    assert len(allowed) == 165
    eqs, _ = actual_system(data, allowed, 8, 5, 18, 12)
    assert len(eqs) == len(HEAD17_DUAL) == 42
    columns = [sum(y*row[j] for y, (row, _) in zip(HEAD17_DUAL, eqs))
               for j in range(len(allowed))]
    rhs = sum(y*b for y, (_, b) in zip(HEAD17_DUAL, eqs))
    assert rhs == 83 and max(columns) == 0
    assert all(value <= 0 for value in columns)
    # Every omitted variable is zero by an actual minimum-color partial-token constraint.
    assert all(k in allowed or any(data[4][i][c] == 0 and data[5][k][i][c] > 0
               for i in range(len(data[1])) for c in range(3)) for k in range(len(data[0])))
    print('HEAD17_BALANCE_OBSTRUCTION', len(allowed), 'survivors', 'dual RHS', rhs)


if __name__ == '__main__':
    assert arrival((2, 1)) == F(27, 2)
    check_smaller_capacity()
    data = prepare(combination_palette(), 2**17)
    assert len(data[0]) == 4248
    check_complete_head(data)
    check_minimal_component_obstruction(data)
    check_head17_balance_obstruction(data)
    print('PASS: exact adaptive capacity, complete rational coupling, actual head and scoped obstructions')
