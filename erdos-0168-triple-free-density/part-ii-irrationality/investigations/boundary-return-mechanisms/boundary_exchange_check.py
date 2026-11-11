from collections import defaultdict
from fractions import Fraction as F


OLD = (((2, 8), (10, 3), (14, 0)),
       ((13, 1), (12, 2), (7, 5)),
       ((4, 7), (1, 9), (9, 4)))
NEW = (((13, 1), (10, 3), (14, 0)),
       ((4, 7), (12, 2), (7, 5)),
       ((2, 8), (1, 9), (9, 4)))


def arrival(z):
    a, b = z
    assert min(a, b) >= 0
    value = F(2**a * 3**b)
    if b == 0 and a >= 1:
        value *= F(3, 2)
    if b == 1 and a >= 2:
        value *= F(9, 8)
    return value


def move(edge, a, b):
    return tuple((x+a, y+b) for x, y in edge)


def span(edges, axis):
    return max(max(z[axis] for z in e)-min(z[axis] for z in e)
               for e in edges)


def completion(edge):
    return max(map(arrival, edge))


def check_trade():
    assert sorted(z for e in OLD for z in e) == sorted(z for e in NEW for z in e)
    assert len({(a % 6, b % 6) for e in OLD for a, b in e}) == 9
    for edges in (OLD, NEW):
        assert all(len({(a-b) % 3 for a, b in e}) == 3 for e in edges)
        assert [max(2**a*3**b for a, b in e) for e in edges] == [27648, 36864, 41472]
    for n in range(4):
        for m in range(4):
            assert [completion(move(e, 6*n, 6*m)) for e in OLD] == [
                completion(move(e, 6*n, 6*m)) for e in NEW]


def complete_roots(seed):
    taken = {(a % 6, b % 6) for e in seed for a, b in e}
    extra = [[(a, b) for b in range(6) for a in range(6)
              if (a-b) % 3 == j and (a, b) not in taken] for j in range(3)]
    first = ((0, 0), (1, 0), (0, 1))
    if not all(first[j] in extra[j] for j in range(3)):
        return tuple(seed)+tuple(zip(*extra))
    for j in range(3):
        extra[j].remove(first[j])
    return tuple(seed)+(first,)+tuple(zip(*extra))


def averaged_roots(seed):
    base = complete_roots(seed)
    return [(move(e, shift, 0), F(weight, 9))
            for shift, weight in enumerate((1, 2, 3, 2, 1)) for e in base]


def root_moments(roots):
    for ra, rb in ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)):
        totals = [sum(w*a**ra*b**rb for e, w in roots for a, b in e
                      if (a-b) % 3 == j) for j in range(3)]
        assert len(set(totals)) == 1, (ra, rb, totals)
    for aa in range(6):
        for bb in range(6):
            assert sum(w for e, w in roots for a, b in e
                       if (a % 6, b % 6) == (aa, bb)) == 1


def analytic_boundary(roots):
    aa = 6*((max(a for e, _ in roots for a, b in e)+6)//6)
    bb = 6*((max(b for e, _ in roots for a, b in e)+6)//6)
    horizontal = [sum(w*(a//6) for e, w in roots for a, b in e
                      if (a-b) % 3 == j) for j in range(3)]
    vertical = [sum(w*(b//6) for e, w in roots for a, b in e
                    if (a-b) % 3 == j) for j in range(3)]
    assert len(set(horizontal)) == len(set(vertical)) == 1
    corner = [F(bb, 6)*horizontal[j]+F(aa, 6)*vertical[j]-
              sum(w*(a//6)*(b//6) for e, w in roots for a, b in e
                  if (a-b) % 3 == j) for j in range(3)]
    assert min(corner) >= 0 and horizontal[0] > 0
    ratio = (max(corner)-min(corner))/horizontal[0]
    periods = (ratio.numerator+ratio.denominator-1)//ratio.denominator
    return aa, bb, periods


def residual(z, roots):
    return 1-sum(w for e, w in roots for a, b in e
                 if z[0] >= a and z[1] >= b and
                 (z[0]-a) % 6 == (z[1]-b) % 6 == 0)


def units(aa, bb, roots):
    out = [[], [], []]
    for a in aa:
        for b in bb:
            mass = residual((a, b), roots)
            assert mass >= 0 and (9*mass).denominator == 1
            out[(a-b) % 3].extend([(a, b)]*int(9*mass))
    return [sorted(points, key=lambda z: (arrival(z), z)) for points in out]


def rank_triples(lists):
    assert len(set(map(len, lists))) == 1
    return tuple(zip(*lists))


def bulk_cost(roots):
    result = F(0)
    for e, w in roots:
        actual = completion(e)
        stabilized = completion(move(e, 6, 0))/64
        ordinary = max(2**a*3**b for a, b in e)
        result += w*(1/actual+1/(63*stabilized)+F(64, 63*728*ordinary))
    return result


def repaired(roots):
    aa = 6*((max(a for e, _ in roots for a, b in e)+6)//6)
    bb = 6*((max(b for e, _ in roots for a, b in e)+6)//6)
    corner = units(range(aa), range(bb), roots)
    bottom = units(range(aa, aa+6), range(bb), roots)
    left = units(range(aa), range(bb, bb+6), roots)
    assert len(set(map(len, bottom))) == len(set(map(len, left))) == 1
    n = len(left[0])
    target = max(map(len, corner))
    donors = [target-len(points) for points in corner]
    periods = (max(donors)+n-1)//n if n else 0
    assert n or max(donors) == 0
    for j in range(3):
        corner[j].extend((left[j][k % n][0], left[j][k % n][1]+6*(k//n))
                         for k in range(donors[j]))
    head = rank_triples([sorted(p, key=lambda z: (arrival(z), z)) for p in corner])
    row = rank_triples(bottom)
    vertical = tuple(tuple((left[j][(donors[j]+k) % n][0],
                            left[j][(donors[j]+k) % n][1]+6*((donors[j]+k)//n))
                           for j in range(3)) for k in range(n))
    cost = bulk_cost(roots)+sum((1/completion(e) for e in head), F(0))/9
    cost += F(64, 63*9)*sum((1/completion(e) for e in row), F(0))
    cost += F(729, 728*9)*sum((1/completion(e) for e in vertical), F(0))
    clearing = 9*63*728*2**(aa+6)*3**(bb+6*periods+6)
    assert (clearing*cost).denominator == 1
    return cost, clearing, (aa, bb, periods), (head, row, vertical)


def event_profile(roots, repairs, limit):
    completed = defaultdict(F)
    for e, w in roots:
        n = 0
        while completion(move(e, 6*n, 0)) <= limit:
            m = 0
            while completion(move(e, 6*n, 6*m)) <= limit:
                completed[completion(move(e, 6*n, 6*m))] += w
                m += 1
            n += 1
    for e in repairs[0]:
        if completion(e) <= limit:
            completed[completion(e)] += F(1, 9)
    for edges, da, db in ((repairs[1], 6, 0), (repairs[2], 0, 6)):
        for e in edges:
            k = 0
            while completion(move(e, da*k, db*k)) <= limit:
                completed[completion(move(e, da*k, db*k))] += F(1, 9)
                k += 1
    births = defaultdict(lambda: [0, 0, 0])
    for a in range(limit.bit_length()):
        b, raw = 0, 2**a
        while raw <= limit:
            t = arrival((a, b))
            if t <= limit:
                births[t][(a-b) % 3] += 1
            b, raw = b+1, raw*3
    counts, done, profile = [0, 0, 0], F(0), []
    for t in sorted(births):
        counts = [counts[j]+births[t][j] for j in range(3)]
        done += completed[t]
        assert done <= min(counts)
        profile.append((t, min(counts), done))
    return profile


def transformed_trade(q, p, s, r):
    assert abs(q*r-p*s) == 1 and {(q+p) % 3, (s+r) % 3} == {1, 2}
    ratios = (F(2**q, 3**p), F(2**s, 3**r))
    dominant = max(range(2), key=lambda j: max(ratios[j], 1/ratios[j]))
    sign = 1 if ratios[dominant] > 1 else -1
    ca, cb = ((9, 2), (14, 3)) if dominant == 0 else ((2, 9), (3, 14))
    u = (sign*(ca[0]*q+ca[1]*s), -sign*(ca[0]*p+ca[1]*r))
    v = (sign*(cb[0]*q+cb[1]*s), -sign*(cb[0]*p+cb[1]*r))
    assert abs(u[0]*v[1]-u[1]*v[0]) == 1
    mapped = [tuple(tuple(a*u[j]+b*v[j] for j in range(2)) for a, b in e)
              for e in OLD]
    other = [tuple(tuple(a*u[j]+b*v[j] for j in range(2)) for a, b in e)
             for e in NEW]
    points = [z for e in mapped for z in e]
    dx = 6*((-min(a for a, b in points)+5)//6)
    dy = 6*((2-min(b for a, b in points)+5)//6)
    child = tuple(move(e, dx, dy) for e in mapped)
    parent = tuple(move(e, dx, dy) for e in other)
    assert min(a for e in child for a, b in e) >= 0
    assert min(b for e in child for a, b in e) >= 2
    assert [completion(e) for e in parent] == [completion(e) for e in child]
    assert len({(a % 6, b % 6) for e in parent for a, b in e}) == 9
    assert all(len({(a-b) % 3 for a, b in e}) == 3 for e in parent+child)
    for axis in range(2):
        assert 7*span(child, axis) <= 6*span(parent, axis)
    embedded_parent, embedded_child = averaged_roots(parent), averaged_roots(child)
    root_moments(embedded_parent)
    root_moments(embedded_child)
    assert analytic_boundary(embedded_parent) == analytic_boundary(embedded_child)
    print('CF_COMPRESSION', (q, p, s, r),
          tuple(span(parent, j) for j in range(2)),
          tuple(span(child, j) for j in range(2)),
          'CHARGED_CUTS', analytic_boundary(embedded_parent))


if __name__ == '__main__':
    check_trade()
    old_roots, new_roots = averaged_roots(OLD), averaged_roots(NEW)
    root_moments(old_roots)
    root_moments(new_roots)
    old, new = repaired(old_roots), repaired(new_roots)
    assert old[2] == analytic_boundary(old_roots)
    assert old[:3] == new[:3] and old[3] == new[3]
    assert residual((8, 6), new_roots) > 0
    before = event_profile(old_roots, old[3], 2**20)
    after = event_profile(new_roots, new[3], 2**20)
    assert before == after
    first = next(row for row in before if row[1] != row[2])
    print('COMPLETE_EMBEDDING', old[0], 'CLEARING', old[1], 'CUTS', old[2])
    print('FIRST_DEFICIT', first, 'INTERIOR_RESIDUAL', residual((8, 6), new_roots))
    for args in ((8, 5, 3, 2), (19, 12, 27, 17), (84, 53, 65, 41)):
        transformed_trade(*args)
    print('PASS: repeated trade, moment-balanced complete embedding and CF compression')
