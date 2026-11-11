"""Exact rational-order token certificates; run with Python -B."""
from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def exponents(a, b):
    if b == 0 and a >= 1:
        return a - 1, 1
    if b == 1 and a >= 2:
        return a - 3, 3
    return a, b


def arrival2(a, b):
    x, y = exponents(a, b)
    return (1 << (x + 1)) * 3**y


def grade_tokens(p, q, top):
    points = [(0, 0)]
    points += [(a, 0) for a in range(1, 2 + (top - q) // p)]
    points += [(a, 1) for a in (0, 1) if p*a + q <= top]
    points += [(a, 1) for a in range(2, 4 + (top - 3*q) // p)]
    for b in range(2, top // q + 1):
        points += [(a, b) for a in range((top - q*b) // p + 1)]
    assert len(points) == len(set(points))
    assert all(p*exponents(*z)[0] + q*exponents(*z)[1] <= top for z in points)
    return points


def model_lists(p, q, top):
    side = 1 if 2**q > 3**p else -1
    lists = [[] for _ in range(3)]
    for a, b in grade_tokens(p, q, top):
        x, y = exponents(a, b)
        lists[(a-b) % 3].append((p*x + q*y, side*x, a, b))
    return [[(a, b) for _, _, a, b in sorted(xs)] for xs in lists]


def frontier_min2(p, q, top):
    points = [(max(1, 2+(top-q)//p), 0),
              (max(2, 4+(top-3*q)//p), 1)]
    points += [(max(0, (top-q*b)//p+1), b) for b in range(2, top//q+2)]
    assert all(p*exponents(*z)[0]+q*exponents(*z)[1] > top for z in points)
    return min(arrival2(*z) for z in points)


def first_deficit(p, q, top, details=False):
    lists = model_lists(p, q, top)
    kmax = min(map(len, lists))
    triples = [tuple(xs[k] for xs in lists) for k in range(kmax)]
    events = defaultdict(lambda: [[], 0])
    for j, xs in enumerate(lists):
        for z in xs:
            events[arrival2(*z)][0].append(j)
    for zs in triples:
        events[max(arrival2(*z) for z in zs)][1] += 1
    counts, completed = [0, 0, 0], 0
    # All model lists contain an initial actual-time interval.  The first
    # omitted token of each row has larger actual time than this bound.
    safe = frontier_min2(p, q, top)
    ordered = sorted(events.items())
    for ei, (t2, (births, finishes)) in enumerate(ordered):
        if t2 >= safe:
            break
        for j in births:
            counts[j] += 1
        completed += finishes
        assert completed <= min(counts)
        if completed < min(counts):
            if details:
                next2 = ordered[ei+1][0]
                assert next2 < safe
                gap = (min(counts)-completed)*(Fraction(2, t2)-Fraction(2, next2))
                return Fraction(t2, 2), tuple(counts), completed, triples, Fraction(next2, 2), gap
            return Fraction(t2, 2), tuple(counts), completed, triples
    return None, None, None, triples


def prefix_order(p, q, successor, log_cut):
    """Compare the complete model restriction with actual order at 2**log_cut."""
    side = 1 if 2**q > 3**p else -1
    top = p*(log_cut + 4) + q*4
    points = grade_tokens(p, q, top)
    head = [z for z in points if arrival2(*z) <= 2**(log_cut + 1)]
    actual = sorted(head, key=lambda z: (arrival2(*z), z))
    model = sorted(head, key=lambda z: (
        p*exponents(*z)[0] + q*exponents(*z)[1], side*exponents(*z)[0], z))
    # Ties of identical physical times may appear in either order.
    assert [arrival2(*z) for z in actual] == [arrival2(*z) for z in model]
    whole_model = sorted(points, key=lambda z: (
        p*exponents(*z)[0]+q*exponents(*z)[1], side*exponents(*z)[0], z))
    assert whole_model[:len(head)] == model
    assert frontier_min2(p, q, top) > 2**(log_cut+1)
    assert log_cut <= q + successor - 1
    return len(head)


def model_value(p, q):
    path = (Path(__file__).resolve().parent.parent /
            'Erdos 168 reflected return models' / 'two_sided_models_check.py')
    spec = spec_from_file_location('audited_scalar_model', path)
    helper = module_from_spec(spec)
    spec.loader.exec_module(helper)
    sign = 1 if 2**q > 3**p else -1
    z = helper.model(p, q, sign)[-1]
    return (3-z)/3


def valuation(n, prime):
    answer = 0
    while n % prime == 0:
        answer += 1
        n //= prime
    return answer, n


def full_cost(p, q):
    """Finite grade head plus exact eventual cross-grade correction streams."""
    period, u, v = 3*p*q, 2**(3*q), 3**(3*p)
    points = grade_tokens(p, q, 3*period)
    births = defaultdict(lambda: [0, 0, 0])
    for a, b in points:
        x, y = exponents(a, b)
        births[p*x+q*y][(a-b) % 3] += 1
    cumulative = [[0, 0, 0]]
    for g in range(3*period):
        cumulative.append([cumulative[-1][j]+births[g][j] for j in range(3)])
    spread = max(max(cumulative[g])-min(cumulative[g]) for g in range(period, 2*period))
    common = None
    for g in range(period, 2*period):
        assert births[g+period] == [n+1 for n in births[g]]
        increments = [cumulative[g+period][j]-cumulative[g][j] for j in range(3)]
        assert len(set(increments)) == 1
        if common is not None:
            assert increments[0] == common+1
        common = increments[0]
    start = (2*spread+4)*period
    lists = model_lists(p, q, start+4*period)
    side = 1 if u > v else -1
    def key(z):
        x, y = exponents(*z)
        return p*x+q*y, side*x
    triples = [tuple(xs[k] for xs in lists) for k in range(min(map(len, lists)))]
    all_births = defaultdict(lambda: [0, 0, 0])
    for j, xs in enumerate(lists):
        for z in xs:
            all_births[key(z)[0]][j] += 1
    all_cumulative = [[0, 0, 0]]
    for g in range(start+4*period):
        all_cumulative.append([all_cumulative[-1][j]+all_births[g][j] for j in range(3)])
    cross = defaultdict(list)
    correction = Fraction(0)
    initial_cross = 0
    for zs in triples:
        gs = [key(z)[0] for z in zs]
        g = max(gs)
        if len(set(gs)) == 1:
            continue
        last = max(zs, key=key)
        d = Fraction(2, arrival2(*last)) - Fraction(2, max(map(lambda z: arrival2(*z), zs)))
        assert d >= 0
        if g < start:
            correction += d
            initial_cross += 1
        elif g < start+3*period:
            assert max(gs)-min(gs) == 1
            cross[g].append(zs)
    stream_count, latest_switch = 0, 0
    for g in range(start, start+period):
        roots = cross[g]
        assert len(roots) == max(all_cumulative[g])-min(all_cumulative[g])
        assert len(roots) == len(cross[g+period]) == len(cross[g+2*period])
        for i, zs in enumerate(roots):
            shifts = []
            for j, z in enumerate(zs):
                z1, z2 = cross[g+period][i][j], cross[g+2*period][i][j]
                delta = z1[0]-z[0], z1[1]-z[1]
                assert delta in ((3*q, 0), (0, 3*p))
                assert (z2[0]-z1[0], z2[1]-z1[1]) == delta
                shifts.append(u if delta[0] else v)
                gz = key(z)[0]
                trailing = int((side > 0 and delta[0] != 0) or
                               (side < 0 and delta[1] != 0))
                # Equal quadratic rank polynomials: old-grade suffix and
                # new-grade prefix have the identical g+trailing coefficient.
                assert gz+trailing == g
            last = max(range(3), key=lambda j: key(zs[j]))
            assert all(max(range(3), key=lambda j: key(cross[g+k*period][i][j])) == last
                       for k in (1, 2))
            times = [Fraction(arrival2(*z), 2) for z in zs]
            if len(set(shifts)) == 1:
                r = shifts[0]
                correction += (1/times[last]-1/max(times))/(1-Fraction(1, r))
            else:
                fast, slow = max(u, v), min(u, v)
                cf = max(t for t, r in zip(times, shifts) if r == fast)
                cs = max(t for t, r in zip(times, shifts) if r == slow)
                assert shifts[last] == slow and times[last] == cs
                switch, tf, ts = 0, cf, cs
                while tf < ts:
                    tf *= fast
                    ts *= slow
                    switch += 1
                latest_switch = max(latest_switch, switch)
                correction += 1/ts/(1-Fraction(1, slow))-1/tf/(1-Fraction(1, fast))
            stream_count += 1
    value = model_value(p, q)-correction
    assert value > 0 and correction > 0
    # Independently bound the actual coupling sum by a finite rank head and
    # one color's entire omitted reciprocal token mass.
    partial = sum((Fraction(2, max(arrival2(*z) for z in zs)) for zs in triples), Fraction(0))
    omitted = sum((Fraction(2, arrival2(*z)) for z in lists[0][len(triples):]), Fraction(0))
    # Raw omitted tokens have grade above start+4L.  Their entire reciprocal
    # mass is bounded by a rectangular union with half that grade cutoff.
    a0 = (start+4*period)//(2*p)
    b0 = (start+4*period)//(2*q)
    assert a0 >= 0 and b0 > 3
    omitted += Fraction(3, 2**a0)+Fraction(3, 3**b0)
    assert partial <= value <= partial+omitted
    return value, correction, (spread, start, initial_cross, stream_count, latest_switch)


if __name__ == '__main__':
    assert exponents(2, 1) == (-1, 3) and arrival2(2, 1) == 27
    for p, q, nxt in ((5, 8, 19), (12, 19, 65)):
        n = prefix_order(p, q, nxt, q+nxt-1)
        t, counts, done, triples = first_deficit(p, q, 6*p*q)
        print((p, q), 'prefix tokens', n, 'first deficit', t, counts, done,
              'model triples', len(triples))
    for p, q in ((5, 8), (12, 19)):
        value, correction, stats = full_cost(p, q)
        t, counts, done, triples, nxt, gap = first_deficit(p, q, 6*p*q, True)
        two, rest = valuation(value.denominator, 2)
        three, odd = valuation(rest, 3)
        if (p, q) == (5, 8):
            assert value == Fraction(84385048996040971880909606545935202648457,
                                     141324170955093527314663887572476341780480)
            assert (two, three, odd) == (54, 27, 1028780687935)
            assert (t, nxt, counts, done) == (2**27*3**7, 2**8*3**19, (163, 163, 163), 162)
        else:
            assert (two, three, odd) == (137, 121, 1351932287187751456719735745864595)
            assert (t, nxt, counts, done) == (2**103*3**2, 2**19*3**55, (1214, 1214, 1214), 1213)
        assert value.denominator*gap > 1
        print((p, q), 'full cost', value, 'reduced bits', value.denominator.bit_length(),
              'correction bits', correction.denominator.bit_length(), 'tail stats', stats,
              'v2,v3,odd', (two, three, odd), 'deficit interval', (t, nxt),
              'reduced denominator times gap', value.denominator*gap)
