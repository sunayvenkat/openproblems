"""Independent mixed-shape tail and minimum-color certificate; stdlib only."""
from collections import defaultdict
from fractions import Fraction as F
from functools import cache
from itertools import product


@cache
def clock(a, b):
    if b == 0 and a:
        return F(3 * 2**a, 2)
    if b == 1 and a >= 2:
        return F(27 * 2**a, 8)
    return F(2**a * 3**b)


def norm(points):
    amin, bmin = min(z[0] for z in points), min(z[1] for z in points)
    return tuple(sorted((a-amin, b-bmin) for a, b in points))


def rank_births(points):
    events = defaultdict(lambda: [F(0), F(0), F(0)])
    for a, b, mass in points:
        events[clock(a, b)][(a-b) % 3] += mass
    counts, births, previous = [F(0)]*3, [], F(0)
    for t, delta in sorted(events.items()):
        counts = [counts[j]+delta[j] for j in range(3)]
        now = min(counts)
        if now > previous:
            assert (9*(now-previous)).denominator == 1
            births.append((t, now-previous))
        previous = now
    assert counts[0] == counts[1] == counts[2]
    return births


def run(period, cutoff):
    shapes = (((0, 0), (2, 0), (0, 2)),
              ((0, 4), (3, 2), (6, 0)))
    weights = (F(1, 9), F(2, 9))
    a_cut = b_cut = period
    assert period in (6, 12)
    for a, b in product(range(period), repeat=2):
        owners = []
        for shape, weight in zip(shapes, weights):
            for da, db in shape:
                owners.append((((a-da) % period, (b-db) % period), weight))
        assert sum(weight for _, weight in owners) == 1

    def residue(a, b):
        kept = sum((weight for shape, weight in zip(shapes, weights)
                    for da, db in shape if a >= da and b >= db), F(0))
        return 1-kept

    roots = []
    regions = ((range(a_cut), range(b_cut)),
               (range(a_cut, a_cut+period), range(b_cut)),
               (range(a_cut), range(b_cut, b_cut+period)))
    for columns, rows in regions:
        points = [(a, b, residue(a, b)) for a, b in product(columns, rows)
                  if residue(a, b)]
        births = rank_births(points)
        roots.append((points, births))
    for a, b, mass in roots[1][0]:
        assert residue(a+period, b) == mass
        assert clock(a+period, b) == 2**period*clock(a, b)
    for a, b, mass in roots[2][0]:
        assert residue(a, b+period) == mass
        assert clock(a, b+period) == 3**period*clock(a, b)

    bulk_cost = F(0)
    for shape, weight in zip(shapes, weights):
        for a, b in product(range(period), repeat=2):
            first = max(clock(a+da, b+db) for da, db in shape)
            next_horizontal = max(clock(a+period+da, b+db) for da, db in shape)
            next_vertical = max(clock(a+da, b+period+db) for da, db in shape)
            bulk_cost += weight*(1/first
                + F(2**period, 2**period-1)/next_horizontal
                + F(2**period*3**period,
                    (2**period-1)*(3**period-1))/next_vertical)
    root_costs = [sum((mass/t for t, mass in births), F(0))
                  for _, births in roots]
    cost = (bulk_cost+root_costs[0]
            + F(2**period, 2**period-1)*root_costs[1]
            + F(3**period, 3**period-1)*root_costs[2])
    clearing = (9*(2**period-1)*(3**period-1)
                * 2**period*3**period*2**a_cut*3**b_cut)
    assert (clearing*cost).denominator == 1

    amax, bmax = cutoff.bit_length(), 0
    while 3**bmax <= cutoff:
        bmax += 1
    all_points = [(a, b) for a in range(amax+1) for b in range(bmax+1)
                  if clock(a, b) <= cutoff]
    events = sorted({clock(a, b) for a, b in all_points})
    bulk = []
    for shape, weight in zip(shapes, weights):
        for a, b in product(range(amax+1), range(bmax+1)):
            group = [(a+da, b+db) for da, db in shape]
            times = [(clock(aa, bb), (aa-bb) % 3) for aa, bb in group]
            if min(t for t, _ in times) <= cutoff:
                bulk.append((times, max(t for t, _ in times), weight))
    components = [(roots[0][0], roots[0][1])]
    for axis, (points, births) in zip((0, 1), roots[1:]):
        for n in range(1+amax//period):
            da, db = (period*n, 0) if axis == 0 else (0, period*n)
            scale = 2**da*3**db
            if not points or min(clock(a+da, b+db) for a, b, _ in points) > cutoff:
                break
            components.append(([(a+da, b+db, mass) for a, b, mass in points],
                               [(scale*t, mass) for t, mass in births]))
    for t in events:
        counts = [sum((a-b) % 3 == j for a, b in all_points if clock(a, b) <= t)
                  for j in range(3)]
        tau, j = min(counts), counts.index(min(counts))
        completed_bulk = sum((mass for _, end, mass in bulk if end <= t), F(0))
        partial = sum((mass for times, end, mass in bulk if end > t
                       for birth, color in times if color == j and birth <= t), F(0))
        repaired, local_defect, local_good = F(0), F(0), True
        for points, births in components:
            masses = [sum((mass for a, b, mass in points
                           if (a-b) % 3 == ell and clock(a, b) <= t), F(0))
                      for ell in range(3)]
            explicit = sum((mass for birth, mass in births if birth <= t), F(0))
            assert explicit == min(masses)
            repaired += explicit
            local_defect += masses[j]-min(masses)
            local_good &= masses[j] <= min(masses)
        deficit = tau-completed_bulk-repaired
        assert deficit == partial+local_defect >= 0
        assert (deficit == 0) == (partial == 0 and local_good)
    assert F(27, 2) in events
    print('period', period, 'mixed cost', cost, 'actual events', len(events))


def palette_check():
    vectors = ((1, 0), (1, -1), (2, -1), (3, -2), (8, -5))
    out = {norm(((0, 0), u, w)) for u, w in product(vectors, repeat=2)
           if {(u[0]-u[1]) % 3, (w[0]-w[1]) % 3} == {1, 2}}
    out |= {norm(tuple((-a, -b) for a, b in shape)) for shape in list(out)}
    out |= {norm(((0, 0), w, (2*w[0], 2*w[1]))) for w in vectors
            if (w[0]-w[1]) % 3 and 2*w[0] <= 8 and -2*w[1] <= 5}
    assert len(out) == 11
    candidates = {tuple(a*u[k]+b*v[k] for k in range(2))
                  for u, v in product(vectors, repeat=2)
                  for a, b in product(range(-2, 3), repeat=2)}
    candidates = {w for w in candidates if 0 <= w[0] <= 8
                  and 0 <= -w[1] <= 5 and w != (0, 0)}
    assert (4, -3) in candidates
    assert len(candidates) <= 25*len(vectors)**2
    print('independent pure palette', len(out), 'bounded-sum directions', len(candidates))


if __name__ == '__main__':
    palette_check()
    run(6, 2**30)
    run(12, 2**24)
    print('PASS: independent mixed-palette arithmetic and minimum-color identity')
