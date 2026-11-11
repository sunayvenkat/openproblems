"""Exact arbitrary-shape repair and minimum-color head identity checks."""
from fractions import Fraction as F
from itertools import product


def canonical(points):
    a0 = min(a for a, _ in points)
    b0 = min(b for _, b in points)
    return tuple(sorted((a-a0, b-b0) for a, b in points))


def cf_palette(pairs, h, v):
    vectors = [(q, -p) for p, q in pairs if q <= h and p <= v]
    out = set()
    for i, u in enumerate(vectors):
        if (u[0]-u[1]) % 3 == 0:
            continue
        if 2*u[0] <= h and -2*u[1] <= v:
            out.add(canonical(((0, 0), u, (2*u[0], 2*u[1]))))
        for w in vectors[i+1:]:
            if {(u[0]-u[1]) % 3, (w[0]-w[1]) % 3} == {1, 2}:
                out.add(canonical(((0, 0), u, w)))
                out.add(canonical(((0, 0), (-u[0], -u[1]), (-w[0], -w[1]))))
    assert len(out) <= len(vectors)**2
    for shape in out:
        assert max(a for a, _ in shape) <= h
        assert max(b for _, b in shape) <= v
        assert len({(a-b) % 3 for a, b in shape}) == 3
    return out


def arrival(z, mode="actual"):
    a, b = z
    out = F(2**a * 3**b)
    if b == 0 and (mode == "asym" or (mode == "actual" and a >= 1)):
        out *= F(3, 2)
    if b == 1 and (mode == "asym" or (mode == "actual" and a >= 2)):
        out *= F(9, 8)
    return out


def rank_groups(points):
    lists = [sorted((arrival(z), z, mass) for z, mass in points
                    if (z[0]-z[1]) % 3 == j) for j in range(3)]
    totals = [sum((mass for _, _, mass in row), F(0)) for row in lists]
    assert totals[0] == totals[1] == totals[2]
    if totals[0] == 0:
        return []
    indices = [0, 0, 0]
    remaining = [lists[j][0][2] for j in range(3)]
    groups = []
    while indices[0] < len(lists[0]):
        mass = min(remaining)
        group = tuple(lists[j][indices[j]][1] for j in range(3))
        groups.append((group, mass))
        for j in range(3):
            remaining[j] -= mass
            if remaining[j] == 0:
                indices[j] += 1
                if indices[j] < len(lists[j]):
                    remaining[j] = lists[j][indices[j]][2]
    assert all(indices[j] == len(lists[j]) for j in range(3))
    return groups


def check_shape(shape, cutoff=2**18):
    shape = canonical(shape)
    assert len(shape) == 3 and len({(a-b) % 3 for a, b in shape}) == 3
    h = max(a for a, _ in shape)
    v = max(b for _, b in shape)
    m = 6
    a_bound = max(m, m*((h+m-1)//m))
    b_bound = max(m, m*((v+m-1)//m))
    weights = {(a, b): F(1, 3) for a, b in product(range(m), repeat=2)}
    for a, b in product(range(m), repeat=2):
        assert sum(weights[((a-da) % m, (b-db) % m)]
                   for da, db in shape) == 1

    def residual(z):
        a, b = z
        return 1-sum((weights[((a-da) % m, (b-db) % m)]
                      for da, db in shape if a >= da and b >= db), F(0))

    corner = [(a, b) for a in range(a_bound) for b in range(b_bound)]
    bottom = [(a, b) for a in range(a_bound, a_bound+m)
              for b in range(b_bound)]
    left = [(a, b) for a in range(a_bound)
            for b in range(b_bound, b_bound+m)]
    components = []
    for region in (corner, bottom, left):
        points = [(z, residual(z)) for z in region if residual(z)]
        groups = rank_groups(points)
        for group, mass in groups:
            assert (3*mass).denominator == 1
        reconstructed = {z: F(0) for z, _ in points}
        for group, mass in groups:
            for z in group:
                reconstructed[z] += mass
        assert reconstructed == dict(points)
        components.append((points, groups))

    for z in bottom:
        assert residual((z[0]+m, z[1])) == residual(z)
        assert arrival((z[0]+m, z[1])) == 2**m * arrival(z)
    for z in left:
        assert residual((z[0], z[1]+m)) == residual(z)
        assert arrival((z[0], z[1]+m)) == 3**m * arrival(z)

    bulk_cost = F(0)
    for a, b in weights:
        roots = [(a+da, b+db) for da, db in shape]
        maxima = [max(arrival(z, mode) for z in roots)
                  for mode in ("actual", "asym", "raw")]
        bulk_cost += weights[(a, b)] * (1/maxima[0]+F(1, 63)/maxima[1]
                                       + F(64, 63*728)/maxima[2])
    costs = [sum((mass/max(arrival(z) for z in group)
                  for group, mass in groups), F(0)) for _, groups in components]
    cost = bulk_cost+costs[0]+F(64, 63)*costs[1]+F(729, 728)*costs[2]
    clear = 3*63*728*2**6*3**6*2**a_bound*3**b_bound
    assert (clear*cost).denominator == 1

    a_max, b_max = cutoff.bit_length(), 0
    while 3**b_max <= cutoff:
        b_max += 1
    all_points = [(a, b) for a in range(a_max+1) for b in range(b_max+1)
                  if arrival((a, b)) <= cutoff]
    events = sorted({arrival(z) for z in all_points})
    bulk = []
    for a in range(a_max+1):
        for b in range(b_max+1):
            group = tuple((a+da, b+db) for da, db in shape)
            if min(arrival(z) for z in group) <= cutoff:
                bulk.append((group, weights[(a % m, b % m)]))
    expanded_components = [components[0]]
    for axis, component in ((0, components[1]), (1, components[2])):
        n = 0
        while True:
            shift = (m*n, 0) if axis == 0 else (0, m*n)
            points = [((z[0]+shift[0], z[1]+shift[1]), mass)
                      for z, mass in component[0]]
            if not points or min(arrival(z) for z, _ in points) > cutoff:
                break
            groups = [(tuple((z[0]+shift[0], z[1]+shift[1]) for z in group), mass)
                      for group, mass in component[1]]
            expanded_components.append((points, groups))
            n += 1
    first_loss = None
    prefix_end = None
    for t in events:
        counts = [sum((a-b) % 3 == j and arrival((a, b)) <= t
                      for a, b in all_points) for j in range(3)]
        tau = min(counts)
        j = counts.index(tau)
        g_bulk = sum((mass for group, mass in bulk
                      if max(arrival(z) for z in group) <= t), F(0))
        p = sum((mass for group, mass in bulk
                 if max(arrival(z) for z in group) > t
                 for z in group if (z[0]-z[1]) % 3 == j and arrival(z) <= t), F(0))
        minima = F(0)
        excess = F(0)
        local_condition = True
        repaired_mass = F(0)
        for points, groups in expanded_components:
            c = [sum((mass for z, mass in points
                      if (z[0]-z[1]) % 3 == ell and arrival(z) <= t), F(0))
                 for ell in range(3)]
            minima += min(c)
            excess += c[j]-min(c)
            local_condition &= c[j] == min(c)
            repaired_mass += sum((mass for group, mass in groups
                                  if max(arrival(z) for z in group) <= t), F(0))
        assert repaired_mass == minima
        g = g_bulk+repaired_mass
        assert tau-g == p+excess >= 0
        assert (g == tau) == (p == 0 and local_condition)
        if g != tau and first_loss is None:
            first_loss = t
        if first_loss is None:
            prefix_end = t
    assert F(27, 2) in events
    return cost, len(events), first_loss, prefix_end


def main():
    u, v = (8, -5), (3, -2)
    old = canonical([(0, 0), (-u[0], -u[1]), (-v[0], -v[1])])
    fake_new = canonical([(0, 0), u, (u[0]-v[0], u[1]-v[1])])
    assert old == fake_new
    # Exact CF-cylinder inclusion: 94/149 < log_3(2) < 53/84.
    assert 3**94 < 2**149 and 2**84 < 3**53
    pairs = []
    p_old, p, q_old, q = 1, 0, 0, 1
    pairs.append((p, q))
    for digit in (1, 1, 1, 2, 2, 3, 1):
        p_old, p = p, digit*p+p_old
        q_old, q = q, digit*q+q_old
        pairs.append((p, q))
    assert pairs[-2:] == [(41, 65), (53, 84)]
    for h, v in ((8, 5), (27, 17), (84, 53)):
        palette = cf_palette(pairs, h, v)
        print("CF palette", h, v, "shapes", len(palette), "variables", 36*len(palette))
    nonunimodular = ((0, 0), (2, 0), (0, 2))
    collinear = ((0, 4), (3, 2), (6, 0))
    for name, shape in (("determinant4", nonunimodular), ("collinear", collinear)):
        cost, events, first_loss, prefix_end = check_shape(shape)
        print(name, "cost", cost, "events", events,
              "first_loss", first_loss, "optimal_prefix_through", prefix_end)
    print("PASS: arbitrary-shape arithmetic and polynomial minimum-color criterion")


if __name__ == "__main__":
    main()
