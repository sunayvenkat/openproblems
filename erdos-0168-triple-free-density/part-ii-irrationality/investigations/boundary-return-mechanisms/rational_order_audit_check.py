"""Independent direct-cost audit; no companion imports. Run Python -B."""
from collections import defaultdict
from fractions import Fraction as F


def effective(z):
    a, b = z
    return (a - 1, 1) if b == 0 and a else ((a - 3, 3) if b == 1 and a >= 2 else z)


def time2(z):
    a, b = effective(z)
    return (1 << (a + 1)) * 3**b


def grade(z, p, q):
    a, b = effective(z)
    return p*a + q*b


def actual_head(limit2):
    result = []
    b = 0
    while 2*3**b <= limit2:
        a = 0
        while time2((a, b)) <= limit2:
            result.append((a, b))
            a += 1
        b += 1
    return result


def modular_lists(p, q, top):
    """Enumerate grade lines by modular inversion, including delayed rows."""
    inverse = pow(p, -1, q)
    side = 1 if 2**q > 3**p else -1
    lists = [[] for _ in range(3)]
    births = [[0, 0, 0] for _ in range(top + 1)]
    for g in range(top + 1):
        ordinary_a = (inverse*g) % q
        ordinary_b = (g - p*ordinary_a)//q
        points = [(ordinary_a + q*k, ordinary_b - p*k)
                  for k in range(max(0, (ordinary_b - 2)//p + 1))]
        if g == 0:
            points.append((0, 0))
        if g >= q and (g-q) % p == 0:
            points.append(((g-q)//p + 1, 0))
        if g in (q, p+q):
            points.append((0 if g == q else 1, 1))
        if (g-3*q) % p == 0 and (g-3*q)//p + 3 >= 2:
            points.append(((g-3*q)//p + 3, 1))
        for z in points:
            assert grade(z, p, q) == g
            j = (z[0]-z[1]) % 3
            lists[j].append(z)
            births[g][j] += 1
    for xs in lists:
        xs.sort(key=lambda z: (grade(z, p, q), side*effective(z)[0], z))
        assert len(xs) == len(set(xs))
    return lists, births


def cumulative(births):
    rows = [[0, 0, 0]]
    for row in births:
        rows.append([rows[-1][j] + row[j] for j in range(3)])
    return rows


def check_prefix(p, q, next_q):
    n = q + next_q - 1
    head = actual_head(2**(n+1))
    lists, _ = modular_lists(p, q, p*n + 1)
    side = 1 if 2**q > 3**p else -1
    key = lambda z: (grade(z, p, q), side*effective(z)[0], z)
    complete = sorted((z for xs in lists for z in xs), key=key)
    model_head = sorted(head, key=key)
    assert complete[:len(head)] == model_head
    assert list(map(time2, model_head)) == sorted(map(time2, head))
    return len(head)


def direct_cost(p, q):
    period = 3*p*q
    _, initial_births = modular_lists(p, q, 3*period)
    initial_counts = cumulative(initial_births)
    spread = max(max(row)-min(row) for row in initial_counts[period:2*period])
    start = (2*spread+4)*period
    lists, births = modular_lists(p, q, start+3*period)
    counts = cumulative(births)
    kappa = counts[2*period][0]-counts[period][0]-period
    for g in range(period, start+2*period):
        assert births[g+period] == [n+1 for n in births[g]]
        assert [counts[g+period][j]-counts[g][j] for j in range(3)] == [g+kappa]*3
    triples = list(zip(*lists))
    head = F(0)
    same = [F(0), F(0), F(0)]
    roots = defaultdict(list)
    for zs in triples:
        grades = [grade(z, p, q) for z in zs]
        g = max(grades)
        value = F(2, max(map(time2, zs)))
        if g < start:
            head += value
        elif len(set(grades)) == 1 and g < start+3*period:
            same[(g-start)//period] += value
        elif len(set(grades)) != 1 and start <= g < start+period:
            assert min(grades) == g-1
            roots[g].append(zs)
    # The all-m proof gives two poles for every same-grade interior run:
    # its expanding finite geometric sum has one leading and one trailing end.
    u, v = 2**(3*q), 3**(3*p)
    a, b = F(1, u), F(1, v)
    assert same[2] == (a+b)*same[1]-a*b*same[0]
    same_tail = (same[1]+(1-a-b)*same[0])/((1-a)*(1-b))
    cross_tail = F(0)
    fast, slow = max(u, v), min(u, v)
    for g in range(start, start+period):
        assert len(roots[g]) == max(counts[g])-min(counts[g])
        for zs in roots[g]:
            cs = max(F(time2(z), 2) for z in zs if grade(z, p, q) == g)
            cf = max(F(time2(z), 2) for z in zs if grade(z, p, q) == g-1)
            k, ts, tf = 0, cs, cf
            while tf < ts:
                k, ts, tf = k+1, ts*slow, tf*fast
            cross_tail += (1-F(1, slow**k))/cs/(1-F(1, slow))
            cross_tail += 1/tf/(1-F(1, fast))
    return head+same_tail+cross_tail, lists, triples


def check_deficit(p, q, lists, triples, first, next_event):
    limit2 = 2*next_event
    all_head = actual_head(limit2)
    assert set(all_head).issubset({z for xs in lists for z in xs})
    events = defaultdict(lambda: [[], 0])
    for z in all_head:
        events[time2(z)][0].append((z[0]-z[1]) % 3)
    for zs in triples:
        t2 = max(map(time2, zs))
        if t2 <= limit2:
            events[t2][1] += 1
    counts, done, found = [0, 0, 0], 0, None
    ordered = sorted(events.items())
    for i, (t2, (born, finishes)) in enumerate(ordered):
        for j in born:
            counts[j] += 1
        done += finishes
        assert done <= min(counts)
        if done < min(counts):
            found = (F(t2, 2), F(ordered[i+1][0], 2), min(counts)-done)
            break
    assert found == (first, next_event, 1)
    return 1/F(first)-1/F(next_event)


if __name__ == '__main__':
    examples = (
        (5, 8, 19, 2**27*3**7, 2**8*3**19,
         2**54*3**27*1028780687935),
        (12, 19, 65, 2**103*3**2, 2**19*3**55,
         2**137*3**121*1351932287187751456719735745864595),
    )
    assert time2((2, 1)) == 27
    for p, q, nxt, first, after, denominator in examples:
        nhead = check_prefix(p, q, nxt)
        value, lists, triples = direct_cost(p, q)
        assert value.denominator == denominator
        gap = check_deficit(p, q, lists, triples, first, after)
        assert denominator*gap > 1
        print((p, q), 'prefix', nhead, 'direct full cost', value,
              'reduced bits', denominator.bit_length(), 'cleared gap', denominator*gap)
