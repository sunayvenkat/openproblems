"""Exact phase alphabets and finite dual witnesses for state-only calibrations.

No project imports. Logarithms are isolated by positive rational series.
"""
from fractions import Fraction as Q
from functools import cmp_to_key
from pathlib import Path
import json


def log_bounds(n, terms=80):
    z = Q(n-1, n+1)
    lo = sum((2*z**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    return lo, lo+2*z**(2*terms+1)/((2*terms+1)*(1-z*z))


l2, u2 = log_bounds(2)
l3, u3 = log_bounds(3)
AB = (l2/u3, u2/l3)
BB = (l3/u2, u3/l2)
UNITS = ((1, 0), (0, 1), (-1, -1))


def add(z, w):
    return z[0]+w[0], z[1]+w[1]


def neg(z):
    return -z[0], -z[1]


def mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]-z[1]*w[1]


def bounds(z, interval):
    lo, hi = interval if z[1] >= 0 else interval[::-1]
    return z[0]+z[1]*lo, z[0]+z[1]*hi


def floor(z, interval):
    lo, hi = bounds(z, interval)
    a, b = lo.numerator//lo.denominator, hi.numerator//hi.denominator
    assert a == b, 'Unresolved logarithmic floor'
    return a


def frac(z, interval):
    return z[0]-floor(z, interval), z[1]


def compare(z, w, interval):
    if z == w:
        return 0
    lo, hi = bounds(add(z, neg(w)), interval)
    assert lo > 0 or hi < 0
    return 1 if lo > 0 else -1


def cells(offsets, interval):
    cuts = {frac((Q(k, 3), Q(-s, 3)), interval) for s in offsets for k in range(3)}
    cuts = sorted(cuts, key=cmp_to_key(lambda z, w: compare(z, w, interval)))
    for i, lo in enumerate(cuts):
        hi = cuts[(i+1) % len(cuts)]
        if compare(hi, lo, interval) <= 0:
            hi = add(hi, (Q(1), Q(0)))
        yield lo, frac(((lo[0]+hi[0])/2, (lo[1]+hi[1])/2), interval)


def digit(x, s, interval):
    return floor((3*x[0], 3*x[1]+s), interval)


def horizontal(x):
    z = (0, 0)
    # S=(1,-omega,0), with omega^(-s) coefficient.
    for s in (1, 2, 3):
        value = ((1, 0), (0, -1), (0, 0))[digit(x, s, AB) % 3]
        z = add(z, mul(UNITS[-s % 3], value))
    return z


def correction(x):
    m0, m1, m3 = (digit(x, s, BB) for s in (0, -1, -3))
    if m0-m1 == 2:
        return UNITS[m0 % 3]
    if m1-m3 == 4:
        return UNITS[(m1-1) % 3]
    return (0, 0)


def vertical(x):
    z = (0, 0)
    # P=(1,-omega^2,0), with omega^(-2s) coefficient.
    for s in (1, 2, 3):
        value = ((1, 0), (1, 1), (0, 0))[digit(x, s, BB) % 3]
        z = add(z, mul(UNITS[-2*s % 3], value))
    return add(add(z, correction(x)), neg(correction(add(x, (Q(0), Q(1))))))


def cone(z):
    return int(z[0] <= 0 and z[0] <= z[1])


def board(cutoff):
    counts, three, b = [0, 0, 0], 1, 0
    while three <= cutoff:
        last = (cutoff//three).bit_length()-1
        for color in range(3):
            first = (color+b) % 3
            counts[color] += max(0, (last-first)//3+1)
        three, b = 3*three, b+1
    return counts[0]-counts[2], counts[1]-counts[2]


def target_enclosure(length=96):
    aa = [mul(UNITS[-a % 3], board(2**a)) for a in range(length)]
    bb = [mul(UNITS[b % 3], board(3**b)) for b in range(length)]
    cc = [[mul(add((1, 0), neg(UNITS[-i % 3])),
               add((1, 0), neg(UNITS[-2*j % 3]))) for j in range(3)] for i in range(3)]
    assert all(x % 3 == y % 3 == 0 for row in cc for x, y in row)
    cc = [[(x//3, y//3) for x, y in row] for row in cc]
    events = []
    for b in range(length):
        event, root, exponent = (0, 0), 2, 1
        while root <= 3**b:
            if 3*root > 2*3**b or 6*root <= 3**b and 4*3**b < 27*root:
                assert event == (0, 0)
                event = UNITS[(exponent+b) % 3]
            root, exponent = 2*root, exponent+1
        events.append(event)
    for n in range((length-3)//3):
        assert add(aa[3*n+3], neg(aa[3*n])) == horizontal(frac((Q(0), Q(n)), AB))
    for m in range(2, (length-3)//3):
        old, new = add(bb[3*m], neg(events[3*m])), add(bb[3*m+3], neg(events[3*m+3]))
        assert add(new, neg(old)) == vertical(frac((Q(0), Q(m)), BB))
    denominator = 2**(length-1)*3**(length-1)
    numerator = 0
    for a in range(length):
        for b in range(length):
            z = add(add(aa[a], bb[b]), add((-1, 0), cc[a % 3][b % 3]))
            if b >= 4:
                value = cone(add(z, neg(events[b])))
            else:
                x, y = z
                value = (0 if b == 0 else int(x >= 1 and y >= 0) if b == 1
                         else int(x <= -1 and x <= y) if b == 2 else int(min(x, 0) <= y))
            numerator += value*2**(length-1-a)*3**(length-1-b)
    head = Q(numerator, denominator)
    tail = 3*(Q(1, 2**length)+Q(1, 3**length)-Q(1, 6**length))
    return 2-3*(head+tail), 2-3*head


def simplest(lo, hi):
    """A fraction of minimum positive denominator in a closed rational interval."""
    assert lo <= hi
    a = lo.numerator // lo.denominator
    if lo.denominator == 1:
        return lo
    if hi.numerator // hi.denominator > a:
        return Q(a+1)
    return a + 1/simplest(1/(hi-a), 1/(lo-a))


def farey_parents(value):
    p, q = value.numerator, value.denominator
    assert q > 1
    b = pow(p, -1, q)
    a = (p*b-1)//q
    c, d = p-a, q-b
    assert b*c-a*d == 1 and b+d == q
    return Q(a, b), Q(c, d)


def interval_certificate(row, omit_zero_row=False):
    s0, wa, wb = (Q(*map(int, row[key])) for key in ('Smin', 'WA', 'WB'))
    if omit_zero_row:
        assert all(int(cell['N']) == 1 for cell in row['low'] if cell['b'] == 0)
        dummy = sum((8*Q(1, 2**cell['i'])*Q(int(cell['N']), 7*8**cell['a'])
                     for cell in row['low'] if cell['b'] == 0), Q(0))
        s0, wa = s0-dummy, wa-dummy
    width = wa+wb
    assert wa >= 0 and wb > 0
    lo, hi = 2-3*(s0+width), 2-3*s0
    model = simplest(lo, hi)
    den = model.denominator
    model = Q((hi*den).numerator // (hi*den).denominator, den)
    assert lo <= model <= hi and model.denominator == den
    if den > 1:
        left, right = farey_parents(model)
        assert left < lo <= hi < right
        assert 3*width <= right-left
    source = (2-model)/3
    theta = (source-s0)/width
    assert 0 <= theta <= 1
    error = 3*den*(Q(9, 7)*wa+Q(191, 182)*wb+source-s0)
    assert error > 0
    exponent = error.denominator.bit_length()-error.numerator.bit_length()-1
    while exponent >= 0 and error*2**exponent >= 1:
        exponent -= 1
    while error*2**(exponent+1) < 1:
        exponent += 1
    if exponent >= 0:
        assert error.numerator*2**exponent < error.denominator
    return {'radius': row['radius'], 'omit_zero_row': omit_zero_row,
            'source': [str(source.numerator), str(source.denominator)],
            'theta': [str(theta.numerator), str(theta.denominator)],
            'model_Z': [str(model.numerator), str(model.denominator)],
            'WA': [str(wa.numerator), str(wa.denominator)],
            'WB': [str(wb.numerator), str(wb.denominator)],
            'cleared_error_bound': [str(error.numerator), str(error.denominator)],
            'denominator_bits': den.bit_length(), 'exclusion_bits': exponent}


def check():
    horizontal_cells = list(cells((1, 2, 3), AB))
    vertical_cells = list(cells((-3, -1, 0, 1, 2, 3), BB))
    aa = {horizontal(x) for _, x in horizontal_cells}
    bb = {vertical(x) for _, x in vertical_cells}
    assert all(horizontal(cut) == horizontal(sample) for cut, sample in horizontal_cells)
    assert all(vertical(cut) == vertical(sample) for cut, sample in vertical_cells)
    assert aa == set(UNITS) | {neg(u) for u in UNITS} | {(0, 0)}
    assert bb == set(UNITS) | {(0, 0)}
    assert horizontal((Q(1, 16), Q(0))) == (0, 0)
    assert horizontal((Q(1, 6), Q(0))) == (0, 1)
    assert vertical((Q(1, 100), Q(0))) == (0, 0)
    matrix = ((182, 0, 0, -1, 0), (0, 182, 0, -1, 0),
              (0, 0, 182, -1, 0), (208, -26, 0, 0, -1),
              (0, 208, -26, 0, -1))
    weights = (-8, 9, -1, 7, -7)
    rhs = (cone((0, -1)), cone((0, 0)), cone((0, 1)),
           cone((0, -1)), cone((0, 0)))
    assert all(sum(w*row[j] for w, row in zip(weights, matrix)) == 0 for j in range(5))
    assert sum(w*b for w, b in zip(weights, rhs)) == 1
    assert sum(map(abs, weights)) == 32
    for lo, hi in ((Q(3, 17), Q(5, 19)), (Q(1, 4), Q(2, 7)),
                   (Q(-7, 5), Q(-9, 7)), (Q(8, 13), Q(13, 21))):
        value = simplest(lo, hi)
        assert lo <= value <= hi
        for d in range(1, value.denominator):
            ceil = -((-lo*d).numerator // (-lo*d).denominator)
            assert Q(ceil, d) > hi
    print('PASS: actual phase alphabets/endpoints, five-row dual witness, minimum-denominator interval recursion')
    zlo, zhi = target_enclosure()
    assert Q(5201, 4303) < zlo
    assert 4303*(zhi-Q(5201, 4303)) < Q(1, 2**10)
    print('PASS: independent original-board 96-by-96 target head and complete tail verify R2 model orientation/bound')
    data_path = Path(__file__).with_name('renewal_source_data.json')
    if data_path.exists():
        data = json.loads(data_path.read_text(encoding='utf-8-sig'))
        results = [interval_certificate(row, omit) for row in data for omit in (False, True)]
        Path(__file__).with_name('convex_interval_results.json').write_text(
            json.dumps(results, indent=2)+'\n', encoding='utf-8')
        for row in results:
            print('INTERVAL', row['radius'], 'OMIT_ZERO_ROW', row['omit_zero_row'],
                  'MODEL_DEN_BITS', row['denominator_bits'],
                  'EXCLUSION_BITS', row['exclusion_bits'])


if __name__ == '__main__':
    check()
