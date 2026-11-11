"""Independent exact fan audit; accepted finite-cover/axis identities are inputs."""
from fractions import Fraction as F
from itertools import permutations
from math import prod


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def neg(z):
    return -z[0], -z[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c-b*d


def root(n):
    return ((1, 0), (0, 1), (-1, -1))[n % 3]


def div(z, w):
    c, d = w
    v = mul(z, (c-d, -d))
    norm = c*c-c*d+d*d
    assert v[0] % norm == v[1] % norm == 0
    return v[0]//norm, v[1]//norm


def fa(n):
    value, power = 2**n, 1
    k = 0
    while 3*power <= value:
        power *= 3
        k += 1
    return k


def fb(n):
    return (3**n).bit_length()-1


def board(t):
    result = [0, 0, 0]
    b, power = 0, 1
    while power <= t:
        last = (t//power).bit_length()-1
        for j in range(3):
            result[j] += max(0, (last-(j+b) % 3)//3+1)
        b, power = b+1, 3*power
    return result


def axes(width):
    aa, bb = [], []
    for n in range(width):
        ka, kb = board(2**n), board(3**n)
        aa.append(mul(root(-n), (ka[0]-ka[2], ka[1]-ka[2])))
        bb.append(mul(root(n), (kb[0]-kb[2], kb[1]-kb[2])))
    return aa, bb


def tau(t):
    counts = board(t)
    a, e = 1, 2
    while e <= t:
        if 3*e > 2*t or (6*e <= t and 4*t < 27*e):
            counts[a % 3] -= 1
        a, e = a+1, 2*e
    return min(counts)


def corner(a, b):
    z = mul(add((1, 0), neg(root(-a))), add((1, 0), neg(root(-2*b))))
    assert z[0] % 3 == z[1] % 3 == 0
    return z[0]//3, z[1]//3


def birth(z, b):
    # These minimum differences independently implement the four low-row rules.
    x, y = z
    if b == 0:
        return 0
    if b == 1:
        return 1 + min(x-1, y, 0)-min(x, y+1, 0)
    if b == 2:
        return min(x+1, y+1, 0)-min(x, y+1, 0)
    if b == 3:
        return 1-min(x, y+1, 0)+min(x, y, 0)
    return min(x, y, 0)-min(x-1, y, 0)


def event(b, floor):
    if b < 4:
        return (0, 0)
    isolated = floor(b)-floor(b-1) == 2
    patch = floor(b-1)-floor(b-3) == 4
    assert not (isolated and patch)
    return (root(floor(b)-2*b) if isolated else
            root(floor(b-1)-1-2*b) if patch else (0, 0))


def coefficient(a, b, aa, bb, floor=fb, shift=0, displacement=(0, 0)):
    z = add(add(aa[a], bb[b]), add(corner(a+shift, b), (-1, 0)))
    return 1-3*birth(add(add(z, neg(event(b, floor))), neg(displacement)), b)


def transform(p, q):
    z = (0, 0)
    for a in range(q):
        z = add(z, root(a+p*a//q))
    return z


def endpoint(p, q, h):
    w = add(add(h, (-1, 0)), root(p+q))
    conjugate = w[0]-w[1], -w[1]
    total = (0, 0)
    for j in range(q % 3):
        total = add(total, root(j-q))
    return add((1, 0), div(add(total, neg(mul(root(2), conjugate))), (2, 1)))


def response_grid(state, width, bb):
    p, q, h = state
    plus = [endpoint(p, q, h)]
    for a in range(1, width):
        inc = (0, 0)
        for j in range((p+fa(a)) % 3+1):
            inc = add(inc, root(-q-a+2*j))
        plus.append(add(plus[-1], inc))
    gamma = root(2*p-q)
    return [[coefficient(a, b, plus, bb, shift=q)
             -coefficient(a, b, plus, bb, shift=q, displacement=gamma)
             for b in range(width)] for a in range(width)]


def weighted(grid, na, nb):
    total = 0
    for a in range(na):
        column = 0
        for b in range(nb):
            column = 3*column+grid[a][b]
        total = 2*total+column
    return F(total, 2**(na-1)*3**(nb-1))


def variation(p, q, r, s):
    assert abs(p*s-r*q) == 1
    a, b = q+s, p+r
    return 9*(F(2, 2**a)*(1+F(a+1, q*s))
              +F(1, 3**b)*(F(3, 2)+F(6*b+3, 4*p*r)))


def matrix_rank(rows):
    pivots = {}
    for row in rows:
        row = list(map(F, row))
        for i, known in sorted(pivots.items()):
            scale = row[i]
            row = [a-scale*b for a, b in zip(row, known)]
        j = next((i for i, a in enumerate(row) if a), None)
        if j is not None:
            pivots[j] = [a/row[j] for a in row]
            if len(pivots) == len(row):
                return len(pivots)
    return len(pivots)


def fan_classes():
    one = (1, 0)
    start = ((2, 2), (0, 1), 0)
    reachable, pending = {start}, [start]
    while pending:
        u, v, k = pending.pop()
        med = tuple((a+b) % 3 for a, b in zip(u, v))
        for nxt in ((med, v, k), (u, med, (k+sum(u)) % 3)):
            if nxt not in reachable:
                reachable.add(nxt)
                pending.append(nxt)
    assert len(reachable) == 24
    balanced = {(0, 1): (1, 0), (1, 1): (1, 0),
                (2, 0): (2, 1), (2, 2): (2, 0)}
    classes = []
    for u, v, k in sorted(reachable):
        med = tuple((a+b) % 3 for a, b in zip(u, v))
        if med not in balanced:
            continue
        x, y = root(sum(u)), root(sum(v))
        c = mul(root(k), (1, -1))
        hv = div(add(mul(add(one, neg(y)), balanced[med]), neg(c)),
                 add(one, neg(mul(x, y))))
        hu = add(balanced[med], neg(mul(x, hv)))
        for current in (0, 1):
            if sum((u, v)[current]) % 3 == 0:
                continue
            states = []
            h = hv if current == 0 else hu
            for j in range(1, 7):
                if current == 0:
                    h = add(hu, mul(x, h))
                    residue = tuple((j*a+b) % 3 for a, b in zip(u, v))
                else:
                    h = add(h, mul(mul(x, root((j-1)*sum(v))), hv))
                    residue = tuple((a+j*b) % 3 for a, b in zip(u, v))
                states.append((*residue, h))
            assert states[:3] == states[3:]
            classes.append(states[:3])
    assert len(classes) == 16
    return classes


def model(p, q, side):
    floor = lambda n, x, y, sign: n*x//y-int(n > 0 and n*x % y == 0 and sign < 0)
    aa, bb = [(1, 0)], [(1, 0)]
    for a in range(1, 3*q):
        z = (0, 0)
        for j in range(floor(a, p, q, side) % 3+1):
            z = add(z, root(-a+2*j))
        aa.append(add(aa[-1], z))
    for b in range(1, 3*p+4):
        z = (0, 0)
        for j in range(floor(b, q, p, -side) % 3+1):
            z = add(z, root(-2*b+j))
        bb.append(add(bb[-1], z))
    beta = lambda n: floor(n, q, p, -side)
    grid = [[coefficient(a, b, aa, bb, floor=beta) for b in range(3*p+4)]
            for a in range(3*q)]
    head = weighted(grid, 3*q, 4)/(1-F(1, 2**(3*q)))
    tile = [[row[b+4] for b in range(3*p)] for row in grid]
    return head + weighted(tile, 3*q, 3*p)/(81*(1-F(1, 2**(3*q)))*(1-F(1, 3**(3*p))))-1


def direct_grade(p, q, width):
    maximum = p*(q+width-1)+q*(width-1)
    points = {}
    for a in range(maximum//p+5):
        for b in range(maximum//q+2):
            u, v = (a-1, 1) if b == 0 and a >= 1 else ((a-3, 3) if b == 1 and a >= 2 else (a, b))
            grade = p*u+q*v
            if grade <= maximum:
                points.setdefault((grade, u, v), []).append((a-b) % 3)
    tables = []
    for side in (1, -1):
        counts, table = [0, 0, 0], {}
        for grade, a, b in sorted(points, key=lambda k: (k[0], side*k[1])):
            before = min(counts)
            for color in points[grade, a, b]:
                counts[color] += 1
            table[a, b] = min(counts)-before
        assert table[-1, 3] == 0
        tables.append(table)
    return [[-3*(tables[0].get((q+a, b), 0)-tables[1].get((q+a, b), 0))
             for b in range(width)] for a in range(width)]


def check():
    aa, bb = axes(200)
    for x in range(-4, 5):
        for y in range(-4, 5):
            assert [birth((x, y), b) for b in range(5)] == [0, int(x >= 1 and y >= 0), int(x <= -1 and x <= y), int(min(x, 0) <= y), int(x <= 0 and x <= y)]
    target = [[coefficient(a, b, aa, bb) for b in range(140)] for a in range(200)]
    target[0][1] -= 3
    for a, b in [(0, 1), (0, 4), (0, 6), (0, 8), (0, 9), (0, 28), (3, 9), (8, 12)]:
        t = 2**a*3**b
        assert target[a][b] == 1-3*(tau(t)-tau(t-1))
    actual = weighted(target, 200, 140)
    tail_actual = 6*(F(1, 2**200)+F(1, 3**140)-F(1, 2**200*3**140))
    classes = fan_classes()
    states = {s for row in classes for s in row}
    assert len(states) == 8
    grids = {s: response_grid(s, 96, bb) for s in states}
    values = {s: weighted(g, 96, 96) for s, g in grids.items()}
    tail = 9*(F(1, 2**96)+F(1, 3**96))
    micro_bounds = {(0, 1, (1, 0)): 482747, (1, 1, (1, 0)): -58734,
                    (2, 0, (2, 1)): -1071732, (2, 2, (2, 0)): 1456689,
                    (1, 2, (1, 1)): 777374, (2, 1, (1, 0)): -547828,
                    (1, 0, (0, 0)): -169, (0, 2, (3, 2)): -1120067}
    for state, lo in micro_bounds.items():
        assert F(lo, 10**6) < values[state]-tail < values[state]+tail < F(lo+1, 10**6)
    expected = sorted([(-124, -123), (188, 189), (1113, 1114), (718, 719), (-163, -162)])
    cycles = {tuple(sorted(row)) for row in classes}
    assert len(cycles) == 5
    got = []
    for row in cycles:
        total = sum(values[s] for s in row)
        lo = (1000*(total-3*tail)).__floor__()
        assert total+3*tail < F(lo+1, 1000)
        got.append((lo, lo+1))
        assert min(values[s]+tail for s in row) < 0 < max(values[s]-tail for s in row)
    assert sorted(got) == expected and all(abs(v) > tail for v in values.values())
    for row in classes:
        rows = [[1, target[a][b]]+[grids[s][a][b] for s in row]
                for b in range(4, 40) for a in range(16)]
        assert matrix_rank(rows) == 5
    p, q, pp, qq = 12, 19, 41, 65
    row = [(p*j+pp, q*j+qq) for j in (1, 2, 3)]
    state = [(r % 3, s % 3, transform(r, s)) for r, s in row]
    witness = [[1, target[a][b]]+[grids[st][a][b] for st in state]
               for a, b in [(0, 4), (0, 6), (0, 8), (0, 9), (0, 28)]]
    det = sum((-1)**sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5))
              *prod(witness[i][p[i]] for i in range(5)) for p in permutations(range(5)))
    assert det == -81
    assert all(state[i] == (r % 3, s % 3, transform(r, s))
               for i, (r, s) in enumerate([(p*(j+3)+pp, q*(j+3)+qq) for j in (1, 2, 3)]))
    assert direct_grade(65, 103, 8) == [r[:8] for r in grids[state[1]][:8]]
    for parent, nxt in [((12, 19), (41, 65)), ((53, 84), (306, 485)), ((306, 485), (665, 1054))]:
        a, b = parent
        c, d = nxt
        for k in range(1, 7):
            r, s = k*a+c, k*b+d
            assert all(r*i//s == fa(i) for i in range(1, b+d))
            assert all(s*i//r == fb(i) for i in range(1, a+c))
    x, y, u, v = F(1, 2**q), F(1, 3**p), F(1, 2**qq), F(1, 3**pp)
    coeffs = [u*x**j/(1-x**3)-v*y**j/(1-y**3) for j in (1, 2, 3)]
    predicted = model(p, q, -1)-sum(c*values[s] for c, s in zip(coeffs, state))
    off = variation(p+pp, q+qq, pp, qq)+72*F(1, 2**(3*q+2*qq))/(1-x*x)+F(189, 4)*F(1, 3**(3*p+2*pp))/(1-y*y)
    epsilon = F(45, 2)*u*x+F(63, 2)*v*y
    remainder = off+epsilon*(u*x/(1-x)+v*y/(1-y))
    uncertainty = remainder+tail*sum(map(abs, coeffs))
    assert abs(actual-predicted)+tail_actual < uncertainty
    assert remainder < 300*F(1, 2**(q+2*qq))
    old = variation(p, q, p+pp, q+qq)+variation(p+pp, q+qq, pp, qq)
    assert remainder*2**46 < old < remainder*2**47
    print('PASS: independent original-board axes,16 classes,8 responses,5 nonzero weighted cycles,16 ranks, resonant grade and common floors')
    print('PASS: complete independent12/19 model/target/fan interval; real-bound gain46bits')


if __name__ == '__main__':
    check()
