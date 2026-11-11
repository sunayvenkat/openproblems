from collections import defaultdict
from fractions import Fraction as F


P = (((2, 8), (10, 3), (14, 0)),
     ((13, 1), (12, 2), (7, 5)),
     ((4, 7), (1, 9), (9, 4)))
R = (((13, 1), (10, 3), (14, 0)),
     ((4, 7), (12, 2), (7, 5)),
     ((2, 8), (1, 9), (9, 4)))


def time2(z):
    a, b = z
    if b == 0 and a >= 1:
        return 3 * 2**a
    if b == 1 and a >= 2:
        return 27 * 2**(a-2)
    return 2**(a+1) * 3**b


def shifted(edge, da, db):
    return tuple((a+da, b+db) for a, b in edge)


def max2(edge):
    return max(map(time2, edge))


def make_roots(seed):
    excluded = {(a % 6, b % 6) for edge in seed for a, b in edge}
    groups = [[(a, b) for b in range(6) for a in range(6)
               if (a-b) % 3 == j and (a, b) not in excluded] for j in range(3)]
    initial = ((0, 0), (1, 0), (0, 1))
    extra = []
    if all(initial[j] in groups[j] for j in range(3)):
        extra.append(initial)
        for j in range(3):
            groups[j].remove(initial[j])
    extra.extend(zip(*groups))
    return [(shifted(e, d, 0), w) for d, w in enumerate((1, 2, 3, 2, 1))
            for e in tuple(seed)+tuple(extra)]


def residue_index(roots):
    cells = defaultdict(list)
    for edge, weight in roots:
        assert len({(a-b) % 3 for a, b in edge}) == 3
        for a, b in edge:
            cells[a % 6, b % 6].append((a, b, weight))
    assert len(cells) == 36
    assert all(sum(w for _, _, w in values) == 9 for values in cells.values())
    return cells


def moment_and_floor_check(roots):
    residue_index(roots)
    for i, k in ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)):
        totals = [sum(w*a**i*b**k for e, w in roots for a, b in e
                      if (a-b) % 3 == j) for j in range(3)]
        assert totals[0] == totals[1] == totals[2]
    A = 6 * (1 + max(a for e, _ in roots for a, b in e)//6)
    B = 6 * (1 + max(b for e, _ in roots for a, b in e)//6)
    left, bottom, corner = [], [], []
    for j in range(3):
        points = [(a, b, w) for e, w in roots for a, b in e if (a-b) % 3 == j]
        n = sum(w*(a//6) for a, b, w in points)
        h = sum(w*(b//6) for a, b, w in points)
        covered = sum(w*((A-a+5)//6)*((B-b+5)//6) for a, b, w in points)
        direct = 3*A*B-covered
        formula = (B//6)*n+(A//6)*h-sum(w*(a//6)*(b//6) for a, b, w in points)
        assert direct == formula >= 0
        left.append(n)
        bottom.append(h)
        corner.append(direct)
    assert len(set(left)) == len(set(bottom)) == 1
    return A, B, left[0], corner


def component(arange, brange, cells):
    lists = [[], [], []]
    for a in arange:
        for b in brange:
            weight = 9-sum(w for x, y, w in cells[a % 6, b % 6] if x <= a and y <= b)
            assert 0 <= weight <= 9
            lists[(a-b) % 3].extend([(a, b)]*weight)
    for row in lists:
        row.sort(key=lambda z: (time2(z), z))
    return lists


def event_cost(lists):
    assert len(set(map(len, lists))) == 1
    events = defaultdict(lambda: [0, 0, 0])
    for j, row in enumerate(lists):
        for z in row:
            events[time2(z)][j] += 1
    counts, done, value = [0, 0, 0], 0, F(0)
    for t, births in sorted(events.items()):
        counts = [counts[j]+births[j] for j in range(3)]
        new_done = min(counts)
        value += F(2*(new_done-done), t)
        done = new_done
    return value


def complete_cost(roots):
    A, B, n9, charges = moment_and_floor_check(roots)
    cells = residue_index(roots)
    head = component(range(A), range(B), cells)
    row = component(range(A, A+6), range(B), cells)
    col = component(range(A), range(B, B+6), cells)
    assert [len(x) for x in head] == charges
    assert all(len(x) == n9 for x in col)
    missing = [max(charges)-v for v in charges]
    J = (max(missing)+n9-1)//n9
    for j in range(3):
        head[j].extend((col[j][k % n9][0], col[j][k % n9][1]+6*(k//n9))
                       for k in range(missing[j]))
    bulk = sum((F(w, 9)*(F(2, max2(e))+F(128, 63*max2(shifted(e, 6, 0)))+
                        F(2*64*729, 63*728*max2(shifted(e, 0, 6))))
                for e, w in roots), F(0))
    tail = F(0)
    for k in range(n9):
        triple = tuple((col[j][(missing[j]+k) % n9][0],
                        col[j][(missing[j]+k) % n9][1]+6*((missing[j]+k)//n9))
                       for j in range(3))
        tail += F(2, max2(triple))
    value = bulk+(event_cost(head)+F(64, 63)*event_cost(row)+F(729, 728)*tail)/9
    D = 9*63*728*2**(A+6)*3**(B+6*J+6)
    assert (D*value).denominator == 1
    completed3 = min(sum(time2(z) <= 6 for z in points) for points in head)
    completed3 += sum(w for e, w in roots if max2(e) <= 6)
    return value, D, (A, B, J), F(completed3, 9), cells


def cone_certificate():
    fixed = ((10, 3), (12, 2), (9, 4))
    for rho in (F(3, 2), F(8, 5)):
        for family in (P, R):
            for edge, peak in zip(family, fixed):
                assert max(a+rho*b for a, b in edge) == peak[0]+rho*peak[1]
    for rho in (F(3, 2), F(14, 9)):
        bounds = (3*rho-4, 7-4*rho)
        for family, bound in zip((P, R), bounds):
            for edge in family:
                assert max(a+rho*b for a, b in edge)-min(a+rho*b for a, b in edge) <= bound
        assert 7*bounds[0] <= 6*bounds[1]
    # Every comparison above is affine in rho, so the two endpoints certify each interval.


def mapped_certificate(q, p, s, r):
    assert abs(q*r-p*s) == 1
    factors = (F(2**q, 3**p), F(2**s, 3**r))
    dominant = 0 if max(factors[0], 1/factors[0]) >= max(factors[1], 1/factors[1]) else 1
    sig = 1 if factors[dominant] > 1 else -1
    ca, cb = ((9, 2), (14, 3)) if dominant == 0 else ((2, 9), (3, 14))
    u = (sig*(ca[0]*q+ca[1]*s), -sig*(ca[0]*p+ca[1]*r))
    v = (sig*(cb[0]*q+cb[1]*s), -sig*(cb[0]*p+cb[1]*r))
    families = [tuple(tuple((a*u[0]+b*v[0], a*u[1]+b*v[1]) for a, b in e)
                      for e in family) for family in (P, R)]
    points = [z for e in families[0] for z in e]
    da = 6*((5-min(a for a, b in points))//6)
    db = 6*((7-min(b for a, b in points))//6)
    families = [tuple(shifted(e, da, db) for e in family) for family in families]
    assert min(b for e in families[0] for a, b in e) >= 2
    assert [max2(e) for e in families[0]] == [max2(e) for e in families[1]]
    for axis in range(2):
        widths = [max(max(z[axis] for z in e)-min(z[axis] for z in e) for e in family)
                  for family in families]
        assert 7*widths[0] <= 6*widths[1]
    results = [moment_and_floor_check(make_roots(family)) for family in families]
    assert results[0] == results[1]
    A, B, n9, corner9 = results[0]
    J = (max(corner9)-min(corner9)+n9-1)//n9
    assert J == 1
    print('mapped', (q, p, s, r), 'cuts', (A, B, J))


if __name__ == '__main__':
    cone_certificate()
    assert len({(a % 6, b % 6) for e in P for a, b in e}) == 9
    for da, db in ((0, 0), (6, 0), (0, 6), (12, 18)):
        assert [max2(shifted(e, da, db)) for e in P] == [max2(shifted(e, da, db)) for e in R]
    parent, child = complete_cost(make_roots(P)), complete_cost(make_roots(R))
    assert parent[:4] == child[:4]
    assert parent[0] == F(357544920809, 704310018048)
    assert parent[1] == 125176966099650799095250944
    assert parent[2:4] == ((24, 12, 1), F(7, 9))
    assert 9-sum(w for a, b, w in child[4][2, 0] if a <= 8 and b <= 6) == 1
    for args in ((8, 5, 3, 2), (19, 12, 27, 17), (84, 53, 65, 41)):
        mapped_certificate(*args)
    print('PASS independent doubled-time boundary/trade/cost certificate')
