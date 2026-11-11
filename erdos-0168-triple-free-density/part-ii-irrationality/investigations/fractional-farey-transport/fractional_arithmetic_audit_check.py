"""Independent actual-event replay of fractional periodic repairs (stdlib only)."""
from bisect import bisect_right
from collections import defaultdict
from fractions import Fraction as F
from math import lcm


def col(z):
    return (z[0] - z[1]) % 3


def time(z):
    a, b = z
    t = F(2**a * 3**b)
    if b == 0 and a:
        t *= F(3, 2)
    elif b == 1 and a >= 2:
        t *= F(9, 8)
    return t


def physical_owner(z, u, v, phase):
    det = u[0]*v[1] - u[1]*v[0]
    found = []
    for sign in (1, -1):
        origin = phase if sign == 1 else (phase[0]+2*u[0]+v[0], phase[1]+2*u[1]+v[1])
        offsets = ((0, 0), (sign*u[0], sign*u[1]), (sign*v[0], sign*v[1]))
        for da, db in offsets:
            anchor = z[0]-da, z[1]-db
            a, b = anchor[0]-origin[0], anchor[1]-origin[1]
            i, j = (a*v[1]-b*v[0])//det, (u[0]*b-u[1]*a)//det
            if i % 3 == j % 2 == 0:
                found.append((sign, anchor, tuple((anchor[0]+x, anchor[1]+y) for x, y in offsets)))
    assert len(found) == 1
    return found[0]


def overlay(points, s):
    rows = [sorted(((time(z), z, m) for z, m in points if col(z) == j and m)) for j in range(3)]
    ends = []
    for row in rows:
        acc, cumulative = F(0), []
        for _, _, m in row:
            acc += m
            cumulative.append(acc)
        ends.append(cumulative)
    assert len({r[-1] if r else F(0) for r in ends}) == 1
    cuts = sorted({F(0), *(x for r in ends for x in r)})
    groups, used = [], defaultdict(F)
    for lo, hi in zip(cuts, cuts[1:]):
        mass = hi-lo
        vertices = tuple(rows[j][bisect_right(ends[j], lo)][1] for j in range(3))
        assert (mass*s).denominator == 1
        groups.append((vertices, mass))
        for z in vertices:
            used[z] += mass
    assert dict(used) == {z: m for z, m in points if m}
    return groups


def run(u, v, phases, cap, expected):
    h, k = max(u[0], v[0]), max(-u[1], -v[1])
    aend, bend = 6*((h+5)//6), 6*((k+5)//6)
    weights = defaultdict(F)
    for phase, mass in phases:
        keys = {(sign, anchor[0] % 6, anchor[1] % 6)
                for a in range(6) for b in range(6)
                for sign, anchor, _ in [physical_owner((a, b), u, v, phase)]}
        assert len(keys) == 12
        for key in keys:
            weights[key] += mass
    s = lcm(*(x.denominator for x in weights.values()))

    def residual(z):
        total = F(0)
        for phase, mass in phases:
            _, _, vertices = physical_owner(z, u, v, phase)
            if any(a < 0 or b < 0 for a, b in vertices):
                total += mass
        return total

    region_points = [[((a, b), residual((a, b))) for a in aa for b in bb]
                     for aa, bb in ((range(aend), range(bend)),
                                    (range(aend, aend+6), range(bend)),
                                    (range(aend), range(bend, bend+6))) ]
    roots = [overlay(points, s) for points in region_points]
    root_costs = [sum((mass/max(map(time, g)) for g, mass in row), F(0)) for row in roots]
    full_cost = root_costs[0]+F(64, 63)*root_costs[1]+F(729, 728)*root_costs[2]
    completed = []
    for (sign, a0, b0), mass in weights.items():
        offsets = ((0, 0), (sign*u[0], sign*u[1]), (sign*v[0], sign*v[1]))
        amin, bmin = min(a for a, _ in offsets), min(b for _, b in offsets)
        anchor = a0+6*((-amin-a0+5)//6), b0+6*((-bmin-b0+5)//6)
        root = tuple((anchor[0]+a, anchor[1]+b) for a, b in offsets)
        actual = max(map(time, root))
        high_a = max(time((a+6, b)) for a, b in root)/64
        high_b = max(time((a, b+6)) for a, b in root)/729
        full_cost += mass*(1/actual+1/(63*high_a)+F(64, 63*728)/high_b)
        for n in range(cap.bit_length()//6+2):
            for m in range(cap.bit_length()//9+2):
                g = tuple((a+6*n, b+6*m) for a, b in root)
                t = max(map(time, g))
                if t <= cap:
                    completed.append((t, mass, 'bulk'))
    assert full_cost == expected
    assert (full_cost*s*63*728*2**6*3**6*2**aend*3**bend).denominator == 1
    for kind, row in enumerate(roots):
        for g, mass in row:
            t = max(map(time, g))
            n = 0
            while t <= cap:
                completed.append((t, mass, 'repair'))
                if kind == 0:
                    break
                n += 1
                shifted = tuple((a+6*n*(kind == 1), b+6*n*(kind == 2)) for a, b in g)
                t = max(map(time, shifted))
                assert t == max(map(time, g))*(64 if kind == 1 else 729)**n
    events = defaultdict(list)
    for a in range(cap.bit_length()):
        b = 0
        while 2**a*3**b <= cap:
            z = a, b
            if time(z) <= cap:
                events[time(z)].append(z)
            b += 1
    by_complete = defaultdict(lambda: [F(0), F(0)])
    for t, mass, kind in completed:
        by_complete[t][kind == 'repair'] += mass
    assert set(by_complete) <= set(events)
    counts, component, done, bulk = [0]*3, defaultdict(lambda: [F(0)]*3), F(0), F(0)
    for t, vertices in sorted(events.items()):
        for a, b in vertices:
            z = a, b
            counts[col(z)] += 1
            if a < aend and b < bend:
                key = 'C', 0
            elif b < bend:
                key = 'R', (a-aend)//6
            elif a < aend:
                key = 'L', (b-bend)//6
            else:
                assert residual(z) == 0
                continue
            component[key][col(z)] += residual(z)
        inc_bulk, inc_repair = by_complete[t]
        bulk += inc_bulk
        done += inc_bulk+inc_repair
        assert done == bulk+sum((min(row) for row in component.values()), F(0))
        assert done <= min(counts)
    assert any(kind == 'R' and n >= 1 for kind, n in component)
    assert any(kind == 'L' and n >= 1 for kind, n in component)
    print({'basis': (u, v), 'actual_events': len(events), 'head_cap': cap,
           'complete_cost': str(full_cost), 'weight_denominator': s,
           'checked_components': len(component)})


if __name__ == '__main__':
    assert time((2, 1)) == F(27, 2)
    run((8, -5), (3, -2), [((0, 0), F(1, 3)), ((2, 0), F(1, 3)), ((4, 0), F(1, 3))],
        2**24, F(60728105, 101896704))
    run((19, -12), (27, -17), [((0, 0), F(1, 2)), ((1, 0), F(1, 2))],
        2**48, F(22603355036644932679, 37855052008758706176))
    print('PASS: independent full costs and all-event global sum-min functional beyond both edge roots')
