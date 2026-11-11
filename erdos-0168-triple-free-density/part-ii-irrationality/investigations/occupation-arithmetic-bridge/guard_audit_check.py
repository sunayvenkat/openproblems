"""Independent exact guard audit; no occupation/density bridge is claimed."""
from fractions import Fraction as Q


def ln_bounds(t, terms=128):
    square, acc = t*t, Q(0)
    for j in reversed(range(terms)):
        acc = Q(1, 2*j+1) + square*acc
    lower = 2*t*acc
    return lower, lower + 2*t**(2*terms+1)/((2*terms+1)*(1-square))


l2, u2 = ln_bounds(Q(1, 3))
l3, u3 = ln_bounds(Q(1, 2))
ALPHA_LO, ALPHA_HI = l2/u3, u2/l3


def floor_actual(k):
    low = k*ALPHA_LO.numerator//ALPHA_LO.denominator
    high = k*ALPHA_HI.numerator//ALPHA_HI.denominator
    assert low == high
    return low


def cf_prefix(length=12):
    lo, hi = ALPHA_LO, ALPHA_HI
    previous_p, current_p, previous_q, current_q = 0, 1, 1, 0
    result = []
    for _ in range(length):
        digit = lo.numerator//lo.denominator
        assert digit == hi.numerator//hi.denominator
        new_p = digit*current_p + previous_p
        new_q = digit*current_q + previous_q
        result.append((new_p, new_q))
        previous_p, current_p = current_p, new_p
        previous_q, current_q = current_q, new_q
        lo, hi = 1/(hi-digit), 1/(lo-digit)
    return result


def rational_label(n, offsets, p, q, sigma):
    # Strict floors at positive arguments equal (numerator-1)//q.
    correction = int(sigma < 0)
    return tuple((((3*n+s)*p-correction)//q) % 3 for s in offsets)


def actual_label(n, offsets):
    return tuple(floor_actual(3*n+s) % 3 for s in offsets)


def discounted_head(bits):
    value = 0
    for bit in reversed(bits):
        value = bit + value/Q(8)
    return value


def discounted_period(bits):
    return discounted_head(bits)/(1-Q(1, 8**len(bits)))


def original_axis_multiple_three(index):
    assert index % 3 == 0
    cutoff, divisor, row = 1 << index, 1, 0
    counts = [0, 0, 0]
    while divisor <= cutoff:
        last = (cutoff//divisor).bit_length()-1
        for color in range(3):
            first = (color+row) % 3
            if first <= last:
                counts[color] += (last-first)//3+1
        row += 1
        divisor *= 3
    return counts[0]-counts[2], counts[1]-counts[2]


def check():
    prefix = cf_prefix()
    cases = ((12, 19, 41, 65, 1), (53, 84, 306, 485, 0),
             (665, 1054, 15601, 24727, 0))
    expected_matches = (27, 189, 8593)
    for case, expected in zip(cases, expected_matches):
        p, q, successor_p, successor_q, selected_residue = case
        position = prefix.index((p, q))
        assert prefix[position+1] == (successor_p, successor_q)
        sigma = 1 if (1 << q) > 3**p else -1
        assert successor_q-2*q > Q(q, 3)
        denominator = 8**q-1
        for offsets in ((1, 2, 3), (1, 3, max(4, q.bit_length()))):
            maximum = max(offsets)
            matched = (q+successor_q-1-maximum)//3+1
            width = 2*matched+73
            actual = [actual_label(n, offsets) for n in range(width)]
            period = [rational_label(n, offsets, p, q, sigma) for n in range(q)]
            assert all(actual[n] == period[n % q] for n in range(matched))
            assert all(rational_label(n+q, offsets, p, q, sigma) == period[n]
                       for n in range(q))
            tail = Q(8, 7*8**width)
            bound = Q(8, 7)*Q(2**(maximum+2*q), 2**successor_q)
            assert bound < 1
            labels = set(actual) | set(period)
            for label in labels:
                model = discounted_period([int(v == label) for v in period])
                assert (denominator*model).denominator == 1
                head = discounted_head([int(v == label) for v in actual])
                assert denominator*max(abs(head-model), abs(head+tail-model)) <= bound
            if offsets == (1, 2, 3):
                assert matched == expected and len(labels) == 9
                head = discounted_head([int(v[0] == selected_residue) for v in actual])
                model = discounted_period([int(v[0] == selected_residue) for v in period])
                assert (head-model)*(head+tail-model) > 0
        print('GUARD_AUDIT', (p, q), 'matched', expected,
              'resonant', (p+q) % 3 == 0, 'simultaneous bound and nonzero case PASS')

    width, total = 28, Q(8, 7)
    ys = [original_axis_multiple_three(3*n) for n in range(width)]
    guards = [int(floor_actual(3*n+1) % 3 == 0) for n in range(width)]
    vertex = [int(y == (1, 0)) for y in ys]
    cone = []
    for x, y in ys:
        x -= 1
        cone.append(min(0, x, y)-min(0, x-1, y))
    tail = Q(8, 7*8**width)
    guard_mass = discounted_head(guards)
    for readout in (vertex, cone):
        mass = discounted_head(readout)
        joint = discounted_head([g*h for g, h in zip(guards, readout)])
        lower = joint-(guard_mass+tail)*(mass+tail)/total
        upper = joint+tail-guard_mass*mass/total
        assert Q(1, 10) < lower <= upper < Q(1, 6)
    assert ys[0] == ys[3] == (1, 0)
    assert original_axis_multiple_three(3*1054) != ys[0]
    print('ACTUAL_CORRELATIONS', 'both complete intervals lie in(1/10,1/6)')
    print('PASS: standalone guard periods, all-label intervals, actual CF inputs and original-board correlations')


if __name__ == '__main__':
    check()
