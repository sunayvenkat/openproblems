"""Exact critical-return states: Euclidean floor sums and actual integer times."""

from math import gcd


def zadd(left, right):
    return left[0]+right[0], left[1]+right[1]


def zmul(left, right):
    a, b = left
    c, d = right
    return a*c-b*d, a*d+b*c-b*d


def omega(power):
    return ((1, 0), (0, 1), (-1, -1))[power % 3]


def geometric(length, phase=1):
    if phase % 3 == 0:
        return length, 0
    result = (0, 0)
    for k in range(length % 3):
        result = zadd(result, omega(k*phase))
    return result


def christoffel_transform(p, q):
    assert 0 < p <= q
    x, y, digits = q, p, []
    while y:
        digit, remainder = divmod(x, y)
        digits.append(digit)
        x, y = y, remainder
    previous_h, current_h = (0, 0), (1, 0)
    previous_length, current_length = 1, 1
    for index, digit in enumerate(digits, 1):
        repeated = zmul(geometric(digit, current_length), current_h)
        if index % 2:
            new_h = zadd(repeated, zmul(omega(digit*current_length), previous_h))
        else:
            new_h = zadd(previous_h, zmul(omega(previous_length), repeated))
        previous_h, current_h = current_h, new_h
        previous_length, current_length = current_length, (
            digit*current_length+previous_length) % 3
    return current_h


def critical_imbalance(p, q, h):
    subtraction = zmul(omega(-p), h)
    numerator = zadd(geometric(q), (-subtraction[0], -subtraction[1]))
    divided = zmul(numerator, (1, -1))
    assert divided[0] % 3 == divided[1] % 3 == 0
    triangle_one = divided[0]//3, divided[1]//3
    rectangle = zmul(geometric(q), geometric(p, -1))
    triangle_two = zadd(rectangle, zmul(zadd(omega(q), omega(-p)), triangle_one))
    return zadd(zmul(omega(1), triangle_two),
                zadd(geometric(2*q+3), zmul(omega(-1), geometric(2*q+2))))


def transform_prestate(p, q):
    imbalance = critical_imbalance(p, q, christoffel_transform(p, q))
    total = 2*p*q+p+5*q+4
    assert (total-imbalance[0]-imbalance[1]) % 3 == 0
    last = (total-imbalance[0]-imbalance[1])//3
    return last+imbalance[0], last+imbalance[1], last


BALANCED_H = {(0, 1): (1, 0), (1, 1): (1, 0),
              (2, 0): (2, 1), (2, 2): (2, 0)}


def advance_state(state, digit):
    parity, previous, current = state
    pp, qp, hp = previous
    p, q, h = current
    phase, previous_phase = (p+q) % 3, (pp+qp) % 3
    repeated = zmul(geometric(digit, phase), h)
    if parity:
        hn = zadd(hp, zmul(omega(previous_phase), repeated))
    else:
        hn = zadd(repeated, zmul(omega(digit*phase), hp))
    return 1-parity, current, ((digit*p+pp) % 3, (digit*q+qp) % 3, hn)


def floor_sum(n, modulus, a, b):
    total = 0
    while True:
        quotient, a = divmod(a, modulus)
        total += quotient * n * (n - 1) // 2
        quotient, b = divmod(b, modulus)
        total += quotient * n
        top = a * n + b
        if top < modulus:
            return total
        n, b, a, modulus = top // modulus, top % modulus, modulus, a


def triangle_count(p, q, level):
    if level < 0:
        return 0
    n, residue = divmod(level, p)
    n += 1
    return n + floor_sum(n, q, p, residue)


def row_counts(last_a, b, first_a=0):
    return [max(0, (last_a - (b + j) % 3) // 3 + 1)
            - max(0, (first_a - 1 - (b + j) % 3) // 3 + 1)
            for j in range(3)]


def rational_prestate(p, q):
    assert p > 0 and q > 0 and gcd(p, q) == 1
    counts = [0, 0, 0]
    for r in range(3):
        for s in range(3):
            level = (2*p*q - p*r - q*s - 1) // 3
            counts[(r-s-2) % 3] += triangle_count(p, q, level)
    for b, last_a in [(0, 2*q+2), (1, 2*q+1)]:
        counts = [x+y for x, y in zip(counts, row_counts(last_a, b))]
    assert sum(counts) == 2*p*q + p + 5*q + 4
    return tuple(counts)


def actual_counts(integer_time, inclusive):
    counts = [0, 0, 0]
    subtract = 0 if inclusive else 1
    for point, value in [((0, 0), 1), ((0, 1), 3), ((1, 1), 6)]:
        if value < integer_time or (inclusive and value == integer_time):
            counts[(point[0]-point[1]) % 3] += 1
    bound = (2*integer_time-subtract) // 3
    last_a = bound.bit_length()-1
    counts = [x+y for x, y in zip(counts, row_counts(last_a, 0, 1))]
    bound = (8*integer_time-subtract) // 27
    last_a = bound.bit_length()-1
    counts = [x+y for x, y in zip(counts, row_counts(last_a, 1, 2))]
    b, power_three = 2, 9
    while power_three <= integer_time:
        bound = (integer_time-subtract) // power_three
        last_a = bound.bit_length()-1
        counts = [x+y for x, y in zip(counts, row_counts(last_a, b))]
        b, power_three = b+1, power_three*3
    return tuple(counts)


def continuants(digits):
    previous, current = (1, 0), (0, 1)
    for digit in digits:
        previous, current = current, (digit*current[0]+previous[0],
                                     digit*current[1]+previous[1])
        yield current


def check():
    for n in range(9):
        for modulus in range(1, 8):
            for a in range(8):
                for b in range(8):
                    assert floor_sum(n, modulus, a, b) == sum(
                        (a*i+b)//modulus for i in range(n))
    for p in range(1, 8):
        for q in range(p, 13):
            if gcd(p, q) != 1:
                continue
            direct = [0, 0, 0]
            for a in range(2*q+1):
                for b in range(2*p+1):
                    if p*a+q*b < 2*p*q:
                        direct[(a-b-2) % 3] += 1
            for b, last in [(0, 2*q+2), (1, 2*q+1)]:
                for a in range(last+1):
                    direct[(a-b) % 3] += 1
            assert rational_prestate(p, q) == tuple(direct)
            direct_h = (0, 0)
            for a in range(q):
                direct_h = zadd(direct_h, omega(a+p*a//q))
            assert christoffel_transform(p, q) == direct_h
            assert transform_prestate(p, q) == tuple(direct)
    cases = [(5, 8, (43, 43, 43)), (12, 19, (189, 189, 189)),
             (41, 65, (1900, 1900, 1900)),
             (53, 84, (3127, 3127, 3127)),
             (306, 485, (99852, 99851, 99852))]
    for p, q, expected in cases:
        powers = 2**q, 3**p
        assert 3*max(x*x for x in powers) < 4*min(x*x for x in powers)
        times = (9*3**(2*p), 9*2**q*3**p, 9*2**(2*q))
        before = actual_counts(min(times), False)
        after = actual_counts(max(times), True)
        assert before == expected == rational_prestate(p, q) == transform_prestate(p, q)
        assert after == tuple(c+1 for c in before)
        print('ACTUAL', (p, q), before, 'BALANCED', len(set(before)) == 1)
    digits = [1, 1, 1, 2, 2, 3, 1, 5, 2]
    convergents = list(continuants(digits))
    assert convergents[-2:] == [(306, 485), (665, 1054)]
    assert 2**1054 < 3**665 and 2**1539 > 3**971
    for tail in ([3]*8, [6]*8, [3, 6]*4, [3, 6, 3, 3, 3, 6, 3, 3]):
        sequence = list(continuants([1, 1, 1, 2, 2]+tail))
        for p, q in sequence[5:]:
            counts = transform_prestate(p, q)
            assert counts == rational_prestate(p, q)
            assert len(set(counts)) == 1 and (p+q) % 3 == 1
    for (p, q), h in BALANCED_H.items():
        assert critical_imbalance(p, q, h) == (0, 0)
    initial = (1, (2, 2, (2, 0)), (0, 1, (1, 0)))
    assert initial[1][2] == christoffel_transform(5, 8)
    assert initial[2][2] == christoffel_transform(12, 19)
    for block in [(3, 3), (1, 3, 2, 3)]:
        state = initial
        trace = []
        for digit in block:
            state = advance_state(state, digit)
            p, q, h = state[2]
            assert (p+q) % 3 != 0 and BALANCED_H[p, q] == h
            trace.append((digit, state))
        assert state == initial
        print('BALANCED_LOOP', block, trace)
    print('PASS: Euclidean/Christoffel state formulas, actual counts and bounded-digit balanced loops')


if __name__ == '__main__':
    check()
