from collections import defaultdict
from fractions import Fraction as F
from math import lcm


def colour(z):
    return (z[0] - z[1]) % 3


def arrival(z, asym=False):
    a, b = z
    assert a >= 0 and b >= 0
    t = F(2) ** a * F(3) ** b
    if b == 0 and (asym or a >= 1):
        t *= F(3, 2)
    if b == 1 and (asym or a >= 2):
        t *= F(9, 8)
    return t


def tile(z, u, v, shift):
    d = u[0] * v[1] - u[1] * v[0]
    a, b = z[0] - shift[0], z[1] - shift[1]
    i, j = (v[1] * a - v[0] * b) // d, (-u[1] * a + u[0] * b) // d
    n, ri = divmod(i, 3)
    m, rj = divmod(j, 2)
    offsets = (((0, 0), (1, 0), (0, 1)) if (ri, rj) in
               ((0, 0), (1, 0), (0, 1)) else ((1, 1), (2, 0), (2, 1)))
    return tuple(((3*n+i)*u[0] + (2*m+j)*v[0] + shift[0],
                  (3*n+i)*u[1] + (2*m+j)*v[1] + shift[1]) for i, j in offsets)


def fractional_types(u, v, phases):
    weights = defaultdict(F)
    for phase, mass in phases:
        selected = set()
        for a in range(6):
            for b in range(6):
                g = set(tile((a, b), u, v, phase))
                found = []
                for sign in (1, -1):
                    for z in g:
                        if {z, (z[0]+sign*u[0], z[1]+sign*u[1]),
                            (z[0]+sign*v[0], z[1]+sign*v[1])} == g:
                            found.append((sign, z[0] % 6, z[1] % 6))
                assert len(found) == 1
                selected.add(found[0])
        assert len(selected) == 12
        for k in selected:
            weights[k] += mass
    assert sum(m for _, m in phases) == 1
    types = []
    for (sign, a0, b0), mass in sorted(weights.items()):
        off = ((0, 0), (sign*u[0], sign*u[1]), (sign*v[0], sign*v[1]))
        nodes = tuple(((a0+a) % 6, (b0+b) % 6) for a, b in off)
        assert len(set(nodes)) == 3
        types.append((off, nodes, mass, (a0, b0)))
    for a in range(6):
        for b in range(6):
            assert sum((m for _, nodes, m, _ in types if (a, b) in nodes), F(0)) == 1
    return types


def owner(z, typ):
    off, nodes, _, _ = typ
    residue = z[0] % 6, z[1] % 6
    if residue not in nodes:
        return None
    delta = off[nodes.index(residue)]
    anchor = z[0] - delta[0], z[1] - delta[1]
    return tuple((anchor[0]+a, anchor[1]+b) for a, b in off)


def residual(z, types):
    kept = F(0)
    for typ in types:
        g = owner(z, typ)
        if g is not None and min(a for a, _ in g) >= 0 and min(b for _, b in g) >= 0:
            kept += typ[2]
    assert 0 <= kept <= 1
    return 1 - kept


def rank_groups(points, denominator):
    lists = [sorted(((z, m) for z, m in points if colour(z) == j and m),
                    key=lambda item: (arrival(item[0]), item[0])) for j in range(3)]
    totals = [sum((m for _, m in row), F(0)) for row in lists]
    assert totals[0] == totals[1] == totals[2]
    if not totals[0]:
        return [], totals[0]
    pointers, remain = [0]*3, [row[0][1] for row in lists]
    groups, used = [], defaultdict(F)
    while pointers[0] < len(lists[0]):
        mass = min(remain)
        assert mass > 0 and (mass * denominator).denominator == 1
        g = tuple(lists[j][pointers[j]][0] for j in range(3))
        groups.append((g, mass))
        for j in range(3):
            used[g[j]] += mass
            remain[j] -= mass
            if not remain[j]:
                pointers[j] += 1
                if pointers[j] < len(lists[j]):
                    remain[j] = lists[j][pointers[j]][1]
        if pointers[0] == len(lists[0]):
            assert all(pointers[j] == len(lists[j]) for j in range(3))
    assert dict(used) == {z: m for z, m in points if m}
    for t in {arrival(z) for z, m in points if m}:
        done = sum((m for g, m in groups if max(map(arrival, g)) <= t), F(0))
        counts = [sum((m for z, m in points if colour(z) == j and arrival(z) <= t), F(0))
                  for j in range(3)]
        assert done == min(counts)
    return groups, totals[0]


def cost(groups):
    return sum((m / max(map(arrival, g)) for g, m in groups), F(0))


def root(typ):
    off, _, _, (a0, b0) = typ
    xmin, ymin = min(a for a, _ in off), min(b for _, b in off)
    a = a0 + 6*((-xmin-a0+5)//6)
    b = b0 + 6*((-ymin-b0+5)//6)
    return tuple((a+x, b+y) for x, y in off)


def bulk_cost(types):
    out = F(0)
    for typ in types:
        g, mass = root(typ), typ[2]
        act = max(map(arrival, g))
        asym = max(arrival(z, True) for z in g)
        raw = max(F(2)**a * F(3)**b for a, b in g)
        out += mass * (1/act + 1/(63*asym) + F(64, 63*728)/raw)
        for n, m in ((1, 0), (2, 0), (0, 1), (1, 1)):
            shifted = tuple((a+6*n, b+6*m) for a, b in g)
            expected = asym * 64**n if m == 0 else raw * 64**n * 729**m
            assert max(map(arrival, shifted)) == expected
    return out


def test(u, v, phases):
    h, k = max(u[0], v[0]), max(-u[1], -v[1])
    aend, bend = 6*((h+5)//6), 6*((k+5)//6)
    types = fractional_types(u, v, phases)
    s = lcm(*(typ[2].denominator for typ in types))
    regions = ((range(aend), range(bend)),
               (range(aend, aend+6), range(bend)),
               (range(aend), range(bend, bend+6)))
    components, totals = [], []
    for aa, bb in regions:
        points = [((a, b), residual((a, b), types)) for a in aa for b in bb]
        groups, mass = rank_groups(points, s)
        components.append(groups)
        totals.append(mass)
    corner, bottom, left = components
    for g, _ in bottom:
        assert max(arrival((a+6, b)) for a, b in g) == 64*max(map(arrival, g))
    for g, _ in left:
        assert max(arrival((a, b+6)) for a, b in g) == 729*max(map(arrival, g))
    for a in range(aend):
        for b in range(bend, bend+6):
            assert residual((a, b), types) == residual((a, b+6), types)
    for a in range(aend, aend+6):
        for b in range(bend):
            assert residual((a, b), types) == residual((a+6, b), types)
    q = bulk_cost(types) + cost(corner) + F(64, 63)*cost(bottom) + F(729, 728)*cost(left)
    clearing = s * 63*728*2**6*3**6 * 2**aend*3**bend
    assert (q*clearing).denominator == 1
    # shortcut: this checks a small genuine head, not feasibility of a super-two-span head.
    cap = 2**(h-2)
    events, counts = [], [0]*3
    for a in range(h):
        b = 0
        while 2**a * 3**b <= cap:
            z = a, b
            if arrival(z) <= cap:
                events.append((arrival(z), z))
                assert residual(z, types) == 1 and a < aend and b < bend
            b += 1
    for t in sorted({t for t, _ in events}):
        counts = [sum(colour(z) == j for time, z in events if time <= t) for j in range(3)]
        done = sum((m for g, m in corner if max(map(arrival, g)) <= t), F(0))
        assert done == min(counts)
    print({'basis': (u, v), 'types': len(types), 'weight_denominator': s,
           'corner_bottom_left_mass_per_colour': tuple(map(str, totals)),
           'complete_cost': str(q), 'clearing_bits': clearing.bit_length(),
           'checked_optimal_head': cap})


if __name__ == '__main__':
    assert arrival((2, 1)) == F(27, 2)
    test((8, -5), (3, -2), [((0, 0), F(1, 3)), ((2, 0), F(1, 3)), ((4, 0), F(1, 3))])
    test((19, -12), (27, -17), [((0, 0), F(1, 2)), ((1, 0), F(1, 2))])
    print('PASS: complete fractional costs, one S factor, balanced repairs and actual small heads')
