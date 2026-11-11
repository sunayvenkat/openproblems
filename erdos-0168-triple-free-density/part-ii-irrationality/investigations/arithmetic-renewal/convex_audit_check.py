"""Independent exact convex audit; standard library only, no project imports.

Reads the two supplied JSON files, independently rebuilding their source totals.
Writes nothing. Infinite exit, pairing and normalization are accepted proof inputs.
"""
from fractions import Fraction as F
from functools import cache, cmp_to_key
from pathlib import Path
import json


ROOT = Path(__file__).parent
U = ((1, 0), (0, 1), (-1, -1))


def plus(z, w):
    return z[0] + w[0], z[1] + w[1]


def times(z, w):
    return z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0] - z[1]*w[1]


def minus(z, w):
    return z[0] - w[0], z[1] - w[1]


def reward(z, b=4):
    x, y = z
    if b >= 4:
        return int(x <= 0 and y >= x)
    return (0, int(x >= 1 and y >= 0), int(x <= -1 and y >= x),
            int(y >= min(x, 0)))[b]


def log_interval(n):
    t = F(n-1, n+1)
    count = 100
    low = sum((2*t**(2*k+1)/(2*k+1) for k in range(count)), F())
    return low, low + 2*t**(2*count+1)/((2*count+1)*(1-t*t))


L2, L3 = log_interval(2), log_interval(3)
ALPHA = L2[0]/L3[1], L2[1]/L3[0]
BETA = L3[0]/L2[1], L3[1]/L2[0]


def enclosure(z, interval):
    ends = [z[0] + z[1]*x for x in interval]
    return min(ends), max(ends)


def floor_pair(z, interval):
    a, b = enclosure(z, interval)
    assert a // 1 == b // 1
    return a // 1


def reduced_pair(z, interval):
    return z[0] - floor_pair(z, interval), z[1]


def comparison(z, w, interval):
    if z == w:
        return 0
    a, b = enclosure(minus(z, w), interval)
    assert a > 0 or b < 0
    return 1 if a > 0 else -1


def phase_samples(offsets, interval):
    cuts = {reduced_pair((F(k, 3), F(-s, 3)), interval)
            for s in offsets for k in range(3)}
    ordered = sorted(cuts, key=cmp_to_key(lambda z, w: comparison(z, w, interval)))
    for n, cut in enumerate(ordered):
        upper = ordered[(n+1) % len(ordered)]
        if comparison(upper, cut, interval) <= 0:
            upper = plus(upper, (1, 0))
        sample = reduced_pair(((cut[0]+upper[0])/2, (cut[1]+upper[1])/2), interval)
        yield cut, sample


def digit(x, s, interval):
    return floor_pair((3*x[0], 3*x[1]+s), interval)


def a_drift(x):
    ans = (0, 0)
    for s in range(1, 4):
        ans = plus(ans, times(U[-s % 3],
                             ((1, 0), (0, -1), (0, 0))[digit(x, s, ALPHA) % 3]))
    return ans


def phase_event(x):
    k, l, m = [digit(x, s, BETA) for s in (0, -1, -3)]
    return U[k % 3] if k-l == 2 else U[(l-1) % 3] if l-m == 4 else (0, 0)


def b_drift(x):
    ans = minus(phase_event(x), phase_event(plus(x, (0, 1))))
    for s in range(1, 4):
        ans = plus(ans, times(U[-2*s % 3],
                             ((1, 0), (1, 1), (0, 0))[digit(x, s, BETA) % 3]))
    return ans


def check_witness():
    for drift, offsets, interval, expected in (
        (a_drift, (1, 2, 3), ALPHA, set(U) | {minus((0, 0), u) for u in U} | {(0, 0)}),
        (b_drift, (-3, -1, 0, 1, 2, 3), BETA, set(U) | {(0, 0)}),
    ):
        samples = list(phase_samples(offsets, interval))
        assert {drift(sample) for _, sample in samples} == expected
        assert all(drift(cut) == drift(sample) for cut, sample in samples)
    assert a_drift((F(1, 16), 0)) == b_drift((F(1, 100), 0)) == (0, 0)
    assert a_drift((F(1, 6), 0)) == (0, 1)
    for x, offsets, interval in (((F(1, 16), 0), (1, 2, 3), ALPHA),
                                 ((F(1, 6), 0), (1, 2, 3), ALPHA),
                                 ((F(1, 100), 0), (-3, -1, 0, 1, 2, 3), BETA)):
        assert all(comparison(x, cut, interval) != 0 for cut, _ in phase_samples(offsets, interval))
    states = ((0, -1), (0, 0), (0, 1))
    rows = []
    for z, a, phase in [(z, (0, 0), 0) for z in states] + [(z, (0, 1), 1) for z in states[:2]]:
        row = [0]*5
        for coefficient, point in ((216, z), (-27, plus(z, a)), (-8, z), (1, plus(z, a))):
            row[states.index(point)] += coefficient
        row[3+phase] = -1
        rows.append(row)
    dual = (-8, 9, -1, 7, -7)
    assert all(sum(dual[i]*rows[i][j] for i in range(5)) == 0 for j in range(5))
    assert sum(w*reward(z) for w, z in zip(dual, (*states, *states[:2]))) == 1
    assert sum(map(abs, dual)) == 32


def axes(count):
    # Exact integer comparisons determine every floor, independently of log bounds.
    aa, bb = [(1, 0)], [(1, 0)]
    three, exponent, power = 1, 0, 1
    for k in range(1, count):
        while 3*three <= 1 << k:
            three *= 3
            exponent += 1
        aa.append(plus(aa[-1], times(U[-k % 3], ((1, 0), (0, -1), (0, 0))[exponent % 3])))
        power *= 3
        bb.append(plus(bb[-1], times(U[-2*k % 3], ((1, 0), (1, 1), (0, 0))[(power.bit_length()-1) % 3])))
    return aa, bb


def original_board(cutoff):
    counts = [0, 0, 0]
    divisor, b = 1, 0
    while divisor <= cutoff:
        last = (cutoff // divisor).bit_length()-1
        for color in range(3):
            start = (b+color) % 3
            counts[color] += max(0, (last-start)//3+1)
        divisor, b = 3*divisor, b+1
    return counts[0]-counts[2], counts[1]-counts[2]


@cache
def original_event(b):
    cutoff = 3**b
    candidates = {cutoff.bit_length()-1, (cutoff//6).bit_length()-1}
    hits = [U[(a+b) % 3] for a in candidates if a >= 1
            and ((3*(1 << a) > 2*cutoff and (1 << a) <= cutoff)
                 or (6*(1 << a) <= cutoff and 4*cutoff < 27*(1 << a)))]
    assert len(hits) <= 1
    return hits[0] if hits else (0, 0)


COEFF = [[times(minus((1, 0), U[-i % 3]), minus((1, 0), U[-2*j % 3]))
          for j in range(3)] for i in range(3)]
assert all(x % 3 == y % 3 == 0 for row in COEFF for x, y in row)
COEFF = [[(x//3, y//3) for x, y in row] for row in COEFF]


def target_enclosure(aa, bb, count=96):
    ax = [times(U[-a % 3], original_board(2**a)) for a in range(count)]
    bx = [times(U[b % 3], original_board(3**b)) for b in range(count)]
    assert ax == aa[:count] and bx == bb[:count]
    denominator = 2**(count-1)*3**(count-1)
    numerator = 0
    for a in range(count):
        for b in range(count):
            z = plus(minus(plus(ax[a], bx[b]), (1, 0)), COEFF[a % 3][b % 3])
            if b >= 4:
                z = minus(z, original_event(b))
            numerator += reward(z, b)*2**(count-1-a)*3**(count-1-b)
    head = F(numerator, denominator)
    # Complete union of the two omitted strips for a Boolean reward.
    tail = 3*(F(1, 2**count) + F(1, 3**count) - F(1, 6**count))
    return 2-3*(head+tail), 2-3*head


def cheapest(lo, hi):
    # Iterative Euclid; unroll the common integer parts in reverse order.
    stack = []
    lower, upper = lo, hi
    while True:
        integer = -((-lower) // 1)
        if integer <= upper:
            value = F(integer)
            break
        part = lower // 1
        stack.append(part)
        lower, upper = 1/(upper-part), 1/(lower-part)
    for part in reversed(stack):
        value = part + 1/value
    denominator = value.denominator
    value = F((hi*denominator) // 1, denominator)
    assert value.denominator == denominator and lo <= value <= hi
    # Exhaustively rule out every smaller denominator of the actual certificates.
    for d in range(1, denominator):
        assert -((-lo*d) // 1) > (hi*d) // 1
    if denominator > 1:
        p, q = value.numerator, denominator
        b = pow(p, -1, q)
        a, d = (p*b-1)//q, q-b
        c = p-a
        assert b*c-a*d == 1 and b+d == q
        assert F(a, b) < lo <= hi < F(c, d)
        assert hi-lo < F(1, b*d)
        assert q*(hi-lo) < F(1, b) + F(1, d)
    return value


def check_bounds():
    assert 7*F(1, 7)-F(1, 7) == F(6, 7)
    assert 8*F(2, 7)+F(1, 7) == F(17, 7)
    assert F(2, 26)+F(3, 7*26) == F(17, 182)
    assert 26*F(1, 26)-F(3, 7*26) == F(179, 182)
    assert 27*F(2, 26)+F(3, 7*26) == F(381, 182)
    assert (F(6, 7)/F(8, 7), F(90, 91)/F(95, 91)) == (F(3, 4), F(18, 19))
    assert F(18, 19) > F(3, 4)
    assert F(191, 182) < F(9, 7)
    assert 3*(1+F(9, 7)) == F(48, 7)
    assert 1/F(48, 7) == F(7, 48)


def check_sources(data, certificates, aa, bb, zlo, zhi):
    @cache
    def state(a, b):
        z = plus(minus(plus(aa[a], bb[b]), (1, 0)), COEFF[a % 3][b % 3])
        return minus(z, original_event(b)) if b >= 4 else z

    def outside(a, b, radius):
        x, y = state(a, b)
        return max(abs(x), abs(y-x)) > radius

    @cache
    def horizontal(a, b, radius):
        stop, total = 0, 0
        while not outside(a+3*stop, b, radius):
            total = 8*total + 7*reward(state(a+3*stop, b), b)
            stop += 1
        num = total + 1 + reward(state(a+3*stop, b), b)
        return F(num, 7*8**stop), stop, num

    expected = {0: (-7, -1), 1: (F(0), F(9, 8)), 2: (F(5201, 4303), F(5201, 4303))}
    for row in data:
        radius = row['radius']
        assert len(row['high']) == 9 and {(c['i'], c['b']) for c in row['high']} == {(i, b) for i in range(3) for b in (6, 4, 5)}
        assert len(row['low']) == 12 and {(c['i'], c['b']) for c in row['low']} == {(i, b) for i in range(3) for b in range(4)}
        baseline = wa = wb = F()
        for cell in row['high']:
            i, b = cell['i'], cell['b']
            t = 0
            while not outside(i, b+3*t, radius):
                t += 1
            values = [horizontal(i, b+3*m, radius) for m in range(t)]
            height = max((a for _, a, _ in values), default=0)
            hlast = reward(state(i, b+3*t))
            p = sum((q/27**(m+1) for m, (q, _, _) in enumerate(values)), F()) + F(8+hlast, 182*27**t)
            raw = 26*sum(27**(t-1-m)*8**(height-a)*n for m, (_, a, n) in enumerate(values)) + 8**height*(1+hlast)
            assert (t, height, raw) == (cell['t'], cell['H'], int(cell['B']))
            assert p == F(raw+7*8**height, 182*8**height*27**t)
            weight = F(216, 2**i*3**b)
            baseline += weight*p
            wa += weight/F(7)*(sum((F(1, 8**a*27**(m+1)) for m, (_, a, _) in enumerate(values)), F()) + F(1, 26*27**t))
            wb += weight*F(1, 26*27**t)
        dummy = F()
        for cell in row['low']:
            i, b = cell['i'], cell['b']
            q, a, n = horizontal(i, b, radius)
            assert (a, n) == (cell['a'], int(cell['N']))
            weight = F(8, 2**i*3**b)
            baseline += weight*q
            wa += weight*F(1, 7*8**a)
            if b == 0:
                assert n == 1
                dummy += weight*q
        assert (baseline, wa, wb) == tuple(F(*map(int, row[key])) for key in ('Smin', 'WA', 'WB'))
        assert baseline+wb == F(*map(int, row['Smax_B_only']))
        assert baseline+wa+wb == F(*map(int, row['Smax_AB']))
        for omit in (False, True):
            s0, a = (baseline-dummy, wa-dummy) if omit else (baseline, wa)
            width = a+wb
            assert a > 0 and wb > 0
            assert F(3, 4)*width <= s0-(2-zlo)/3
            assert s0-(2-zhi)/3 <= F(9, 7)*a+F(191, 182)*wb
            model = cheapest(2-3*(s0+width), 2-3*s0)
            assert model == expected[radius][int(omit)]
            source = (2-model)/3
            theta = (source-s0)/width
            bound = 3*model.denominator*(F(9, 7)*a+F(191, 182)*wb+source-s0)
            cert = next(c for c in certificates if c['radius'] == radius and c['omit_zero_row'] == omit)
            for key, value in (('source', source), ('theta', theta), ('WA', a), ('WB', wb), ('model_Z', model), ('cleared_error_bound', bound)):
                assert value == F(*map(int, cert[key]))
            assert 0 <= theta <= 1 and 0 < bound <= F(48, 7)*model.denominator*width
            if radius == 2:
                assert model < zlo and 0 < model.denominator*(zhi-model) < F(1, 1024)
                assert bound < F(1, 1024)
            print('PASS source/interval/least denominator:', radius, 'omit_zero_row', omit, 'model', model)


def main():
    data = json.loads((ROOT/'renewal_source_data.json').read_text(encoding='utf-8-sig'))
    certs = json.loads((ROOT/'convex_interval_results.json').read_text(encoding='utf-8-sig'))
    assert len(data) == 3 and {r['radius'] for r in data} == {0, 1, 2}
    assert len(certs) == 6 and {(r['radius'], r['omit_zero_row']) for r in certs} == {(r, o) for r in range(3) for o in (False, True)}
    count = max(96, 3*max(row['H'] for row in data)+4, 3*max(row['T'] for row in data)+10)
    aa, bb = axes(count)
    check_witness()
    check_bounds()
    zlo, zhi = target_enclosure(aa, bb)
    check_sources(data, certs, aa, bb, zlo, zhi)
    for a, b, c, d in ((3, 17, 5, 19), (1, 4, 2, 7), (-7, 5, -9, 7), (8, 13, 13, 21), (0, 1, 0, 1)):
        cheapest(F(a, b), F(c, d))
    print('PASS exact phase endpoints, five-row dual, boundary constants and Farey algebra')
    print('PASS independent original-board 96x96 target head plus full geometric tails')
    print('Conditional only: least_denominator*width -> 0 iff Z is irrational; no completion claim')


if __name__ == '__main__':
    main()
