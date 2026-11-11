"""Independent exact replay; imports certificate data, never companion helpers."""
import ast
from bisect import bisect_left
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def data_constant(name):
    tree = ast.parse(Path(__file__).with_name("adaptive_capacity_check.py").read_text())
    for stmt in tree.body:
        if isinstance(stmt, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == name for t in stmt.targets):
            return ast.literal_eval(stmt.value)
    raise AssertionError(name)


def time2(z):
    a, b = z
    if b == 0 and a:
        return 3 * 2**a
    if b == 1 and a >= 2:
        return 27 * 2**(a-2)
    return 2 * 2**a * 3**b


def color(z):
    return (z[0]-z[1]) % 3


def records(cap2):
    out = []
    b, p3 = 0, 1
    while 2*p3 <= cap2:
        a, raw2 = 0, 2*p3
        while raw2 <= cap2:
            z = a, b
            if time2(z) <= cap2:
                out.append((time2(z), z))
            a, raw2 = a+1, raw2*2
        b, p3 = b+1, p3*3
    return sorted(out)


def event_counts(rec):
    changes = defaultdict(list)
    for t, z in rec:
        changes[t].append(z)
    counts = [0]*3
    out = []
    for t, points in sorted(changes.items()):
        for z in points:
            counts[color(z)] += 1
        out.append((t, tuple(counts), tuple(points)))
    return out


def norm(points):
    x, y = map(min, zip(*points))
    return tuple(sorted((a-x, b-y) for a, b in points))


def shapes(combined):
    seed = [(1, 0), (1, -1), (2, -1), (3, -2), (8, -5)]
    pool = set(seed)
    if combined:
        pool = {(i*u[0]+j*v[0], i*u[1]+j*v[1])
                for u, v, i, j in product(seed, seed, range(-2, 3), range(-2, 3))}
        pool = {z for z in pool if z != (0, 0) and 0 <= z[0] <= 8 and -5 <= z[1] <= 0}
        assert len(pool) == 28
    out = set()
    for u, v in product(pool, repeat=2):
        if color(u) and (color(u)+color(v)) % 3 == 0:
            for sign in (-1, 1):
                out.add(norm(((0, 0), (sign*u[0], sign*u[1]), (sign*v[0], sign*v[1]))))
    for u in pool:
        if color(u):
            out.add(norm(((0, 0), u, (2*u[0], 2*u[1]))))
    out = sorted(s for s in out if max(a for a, _ in s) <= 8 and max(b for _, b in s) <= 5)
    assert len(out) == (118 if combined else 11)
    assert all(len(set(map(color, s))) == 3 for s in out)
    return out


def types(palette):
    return [(s, (a, b)) for s in palette for b in range(6) for a in range(6)]


def incident(z, typ):
    s, residue = typ
    hits = [(z[0]-a, z[1]-b) for a, b in s
            if z[0] >= a and z[1] >= b
            and ((z[0]-a) % 6, (z[1]-b) % 6) == residue]
    assert len(hits) <= 1
    return int(bool(hits))


def tiles(typ, amax, bmax):
    s, (a0, b0) = typ
    for a in range(a0, amax+1, 6):
        for b in range(b0, bmax+1, 6):
            yield tuple((a+x, b+y) for x, y in s)


def zero_survivors(all_types, cap2):
    rec = records(cap2)
    events = event_counts(rec)
    zeros = [[t for t, counts, _ in events if counts[j] == min(counts)] for j in range(3)]
    amax = max(z[0] for _, z in rec)
    bmax = max(z[1] for _, z in rec)
    allowed = []
    for k, typ in enumerate(all_types):
        banned = False
        for g in tiles(typ, amax, bmax):
            end = max(map(time2, g))
            for z in g:
                zs = zeros[color(z)]
                i = bisect_left(zs, time2(z))
                if i < len(zs) and zs[i] < end:
                    banned = True
                    break
            if banned:
                break
        if not banned:
            allowed.append(k)
    return allowed


def check_full_coupling(all_types):
    nums = data_constant("NUMERATORS")
    assert len(nums) == 32 and sum(nums.values()) == 84
    active = [(all_types[k], n) for k, n in nums.items()]
    for a, b in product(range(6), repeat=2):
        total = sum(n for (s, (a0, b0)), n in active
                    if any(((a0+x) % 6, (b0+y) % 6) == (a, b) for x, y in s))
        assert total == 7

    def remaining(z):
        n = 7-sum(n*incident(z, typ) for typ, n in active)
        assert 0 <= n <= 7
        return n

    def clone_groups(aa, bb):
        rows = [[], [], []]
        for z in product(aa, bb):
            rows[color(z)].extend([z]*remaining(z))
        for row in rows:
            row.sort(key=lambda z: (time2(z), z))
        assert len(rows[0]) == len(rows[1]) == len(rows[2])
        return list(zip(*rows))

    batches = [clone_groups(range(18), range(12)),
               clone_groups(range(18, 24), range(12)),
               clone_groups(range(18), range(12, 18))]
    assert list(map(len, batches)) == [239, 50, 52]
    for z in product(range(18, 24), range(12)):
        assert remaining(z) == remaining((z[0]+6, z[1]))
    for z in product(range(18), range(12, 18)):
        assert remaining(z) == remaining((z[0], z[1]+6))
    assert all(remaining(z) == 0 for z in product(range(18, 30), range(12, 24)))

    qbulk = F(0)
    for (s, (a0, b0)), n in active:
        root = tuple((a0+a, b0+b) for a, b in s)
        th = max(time2((a+6, b)) for a, b in root)
        tv = max(time2((a, b+6)) for a, b in root)
        assert max(time2((a+12, b)) for a, b in root) == 64*th
        assert max(time2((a+6, b+6)) for a, b in root) == 64*tv
        assert max(time2((a, b+12)) for a, b in root) == 729*tv
        qbulk += F(n, 7)*(F(2, max(map(time2, root))) + F(64, 63)*F(2, th)
                           + F(64, 63)*F(729, 728)*F(2, tv))
    costs = [sum((F(2, 7*max(map(time2, g))) for g in batch), F(0)) for batch in batches]
    q = qbulk + costs[0] + F(64, 63)*costs[1] + F(729, 728)*costs[2]
    d = 7*63*728*2**6*3**6*2**18*3**12
    assert q == F(20605867009283, 34511190884352)
    assert d == 2086759741982823677952 and (d*q).denominator == 1

    cap2 = 2**18
    rec = records(cap2)
    amax, bmax = map(max, zip(*(z for _, z in rec)))
    completions = Counter()
    for typ, n in active:
        for g in tiles(typ, amax, bmax):
            if max(map(time2, g)) <= cap2:
                completions[max(map(time2, g))] += n
    for j, batch in enumerate(batches):
        for g in batch:
            t = max(map(time2, g))
            while t <= cap2:
                completions[t] += 1
                if j == 0:
                    break
                t *= (64 if j == 1 else 729)
    done, checked, first = 0, 0, None
    for t, counts, _ in event_counts(rec):
        done += completions[t]
        gap7 = 7*min(counts)-done
        assert gap7 >= 0
        if t <= 2**17:
            assert gap7 == 0
            checked += 1
        if gap7 and first is None:
            first = t, gap7
    assert checked == 80 and first == (2*73728, 7)
    print("COMPLETE", q, "D", d, "HEAD_EVENTS", checked, "FIRST_LOSS", first)


def check_dual(all_types):
    allow16 = zero_survivors(all_types, 2**17)
    allow17 = zero_survivors(all_types, 2**18)
    assert (len(allow16), len(allow17)) == (339, 165)
    assert all(incident((0, 6), all_types[k]) == 0 for k in allow16)
    c729 = next(c for t, c, _ in event_counts(records(2*729)) if t == 2*729)
    assert c729[0] == min(c729)
    y = data_constant("HEAD17_DUAL")
    cols = [[int(any(((a0+x) % 6, (b0+y0) % 6) == (a, b) for x, y0 in s))
             for k in allow17 for s, (a0, b0) in [all_types[k]]]
            for b in range(6) for a in range(6)]
    rhs = [1]*36
    for aa, bb in ((range(18), range(12)), (range(18, 24), range(12)),
                   (range(18), range(12, 18))):
        region = list(product(aa, bb))
        raw = [sum(color(z) == c for z in region) for c in range(3)]
        owned = [[sum(incident(z, all_types[k]) for z in region if color(z) == c)
                  for k in allow17] for c in range(3)]
        for c in (1, 2):
            cols.append([a-b for a, b in zip(owned[0], owned[c])])
            rhs.append(raw[0]-raw[c])
    assert len(cols) == len(y) == 42
    assert sum(a*b for a, b in zip(y, rhs)) == 83
    values = [sum(y[i]*cols[i][j] for i in range(42)) for j in range(len(allow17))]
    assert max(values) == 0 and all(v <= 0 for v in values)
    print("FULL_ZERO_BAN_AND_DUAL", len(all_types), len(allow16), len(allow17), "RHS", 83)


HEAD43 = [
((0,0),(1,0),(0,1)), ((1,1),(0,2),(2,0)), ((3,0),(2,1),(1,2)),
((0,3),(4,0),(3,1)), ((2,2),(1,3),(5,0)), ((4,1),(3,2),(0,4)),
((6,0),(5,1),(2,3)), ((1,4),(7,0),(4,2)), ((3,3),(0,5),(6,1)),
((5,2),(2,4),(8,0)), ((7,1),(4,3),(1,5)), ((0,6),(6,2),(3,4)),
((9,0),(8,1),(5,3)), ((6,3),(3,5),(0,7)), ((2,5),(1,6),(7,2)),
((4,4),(10,0),(9,1)), ((8,2),(5,4),(2,6)), ((10,1),(7,3),(11,0)),
((1,7),(9,2),(4,5)), ((12,0),(11,1),(8,3)), ((3,6),(0,8),(6,4)),
((5,5),(2,7),(10,2)), ((7,4),(4,6),(1,8)), ((9,3),(13,0),(12,1)),
((11,2),(6,5),(3,7)), ((0,9),(8,4),(5,6)), ((2,8),(1,9),(9,4)),
((4,7),(12,2),(7,5)), ((13,1),(10,3),(14,0)), ((15,0),(14,1),(11,3)),
((6,6),(3,8),(0,10)), ((8,5),(5,7),(13,2)), ((10,4),(7,6),(2,9)),
((1,10),(9,5),(4,8)), ((12,3),(16,0),(15,1)), ((14,2),(11,4),(6,7)),
((3,9),(0,11),(8,6)), ((5,8),(2,10),(10,5)), ((16,1),(13,3),(17,0)),
((9,6),(4,9),(1,11)), ((7,7),(15,2),(12,4)), ((11,5),(6,8),(3,10)),
((18,0),(17,1),(14,3))]


def span(g):
    return tuple(max(v)-min(v) for v in zip(*g))


def check_finite_head_and_bursts():
    rec = records(2**21)
    assert len(HEAD43) == 43 and len({z for g in HEAD43 for z in g}) == 129
    assert len(set(map(norm, HEAD43))) == 10
    assert all(set(map(color, g)) == {0, 1, 2} and span(g)[0] <= 8 and span(g)[1] <= 5
               for g in HEAD43)
    for j in range(3):
        assert {z for g in HEAD43 for z in g if color(z) == j} == {
            z for _, z in [r for r in rec if color(r[1]) == j][:43]}
    for t, counts, _ in event_counts(rec):
        if t <= 2**20:
            assert sum(max(map(time2, g)) <= t for g in HEAD43) == min(counts)
    rows = [[z for _, z in rec if color(z) == j] for j in range(3)]
    old = [tuple(row[k] for row in rows) for k in (26, 27, 28)]
    new = [((13,1),(10,3),(14,0)), ((4,7),(12,2),(7,5)), ((2,8),(1,9),(9,4))]
    assert Counter(z for g in old for z in g) == Counter(z for g in new for z in g)
    assert [max(map(time2, g)) for g in old] == [2*27648, 2*36864, 2*41472]
    assert [max(map(time2, g)) for g in old] == [max(map(time2, g)) for g in new]
    for h, v, expected in [(27, 17, (161,29,53,34)), (84, 53, (1420,82,168,96))]:
        forced, bad, points, previous = [], [], [], 0
        for t, counts, fresh in event_counts(records(2**(2*h+1))):
            points.extend(fresh)
            if len(set(counts)) == 1:
                if counts[0] == previous+1:
                    assert len(points) == 3
                    forced.append(tuple(points))
                    if span(points)[0] > h or span(points)[1] > v:
                        bad.append(tuple(points))
                previous, points = counts[0], []
        assert all(span(g)[0] >= 6 and span(g)[1] >= 6 for g in bad)
        got = len(forced), len(bad), max(a for g in bad for a,b in g)+1, max(b for g in bad for a,b in g)+1
        assert got == expected
    print("FINITE_HEAD", 2**19, "TRIPLES", len(HEAD43), "FORCED_CORNER_BOUNDS", "PASS")


def counts_at2(cap2):
    out = [0]*3
    def add_row(b, lo, hi):
        for j in range(3):
            residue = (j+b) % 3
            out[j] += (hi-residue)//3-(lo-1-residue)//3
    if cap2 >= 2:
        out[0] += 1
    add_row(0, 1, max(0, (cap2//3).bit_length()-1))
    if cap2 >= 6:
        out[2] += 1
    if cap2 >= 12:
        out[0] += 1
    add_row(1, 2, max(1, (cap2//27).bit_length()+1))
    b, p3 = 2, 9
    while 2*p3 <= cap2:
        add_row(b, 0, (cap2//(2*p3)).bit_length()-1)
        b, p3 = b+1, p3*3
    return tuple(out)


def check_cf_and_progressions():
    def positive(pair):
        a, b = pair
        return 2**max(a,0)*3**max(b,0) > 2**max(-a,0)*3**max(-b,0)
    num, den = (1,0), (0,1)
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    conv = []
    while not conv or conv[-1][1] < 1054:
        k = 0
        while positive((num[0]-(k+1)*den[0], num[1]-(k+1)*den[1])):
            k += 1
        p, q = k*pm1+pm2, k*qm1+qm2
        conv.append((p,q))
        pm2, pm1, qm2, qm1 = pm1,p,qm1,q
        num, den = den, (num[0]-k*den[0], num[1]-k*den[1])
    assert conv[-2:] == [(306,485),(665,1054)] and 1054 > 2*485
    cases = [(8,5,(43,43,43)), (19,12,(189,189,189)), (65,41,(1900,1900,1900)),
             (84,53,(3127,3127,3127)), (485,306,(99852,99851,99852))]
    for q,p, expected in cases:
        assert (p,q) in conv
        g = ((0,2*p+2),(q,p+2),(2*q,2))
        first, last = min(map(time2,g)), max(map(time2,g))
        before, after = counts_at2(first-1), counts_at2(last)
        assert before == expected and after == tuple(n+1 for n in expected)
        assert len(set(map(color,g))) == 3
    print("EXACT_CF_AND_ROW_COUNTS", "485_COUNTEREXAMPLE", counts_at2(
          min(map(time2,((0,614),(485,308),(970,2))))-1))


if __name__ == "__main__":
    assert time2((2,1)) == 27
    all_types = types(shapes(True))
    assert len(all_types) == 4248
    check_full_coupling(all_types)
    check_dual(all_types)
    check_finite_head_and_bursts()
    check_cf_and_progressions()
    print("PASS: independent complete cost/head, all-type dual, finite trade/reset and CF counterexample")
