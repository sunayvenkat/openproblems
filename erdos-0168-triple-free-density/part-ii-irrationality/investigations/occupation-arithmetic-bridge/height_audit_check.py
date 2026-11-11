"""Independent exact certificates for the state-height audit; no project imports."""
from fractions import Fraction as F


ROOT = ((1, 0), (0, 1), (-1, -1))


def plus(z, w):
    return z[0] + w[0], z[1] + w[1]


def minus(z, w):
    return z[0] - w[0], z[1] - w[1]


def times(z, w):
    x, y = z
    u, v = w
    return x*u-y*v, x*v+y*u-y*v


def rotate(z, n):
    return times(z, ROOT[n % 3])


def log_bounds(t):
    count = 100
    low = sum((2*t**(2*k+1)/(2*k+1) for k in range(count)), F(0))
    return low, low + 2*t**(2*count+1)/((2*count+1)*(1-t*t))


def beta_data():
    l2, u2 = log_bounds(F(1, 3))
    l3, u3 = log_bounds(F(1, 2))
    lower, upper = l3/u2, u3/l2
    lo, hi = lower, upper
    q0, q1, out = 1, 0, set()
    while True:
        digit = lo.numerator//lo.denominator
        assert digit == hi.numerator//hi.denominator
        q0, q1 = q1, digit*q1+q0
        if q1 > 306:
            break
        out.add(q1)
        lo, hi = 1/(hi-digit), 1/(lo-digit)
    assert out == {1, 2, 5, 12, 41, 53, 306}
    return lower, upper, sorted(out)


def all_phases(q, direction, beta_low, beta_high):
    # Isolate and sort every discontinuity x=r/3-k*(+/- beta) modulo one.
    events = []
    initial = [0, 0, 0]
    for k in range(q):
        exact_floor = (3**(3*k)).bit_length()-1
        if direction < 0 and k:
            exact_floor = -exact_floor-1
        initial[exact_floor % 3] += 1
        for r in range(3):
            if k == 0 and r == 0:
                continue
            if direction > 0:
                low, high = F(r, 3)-k*beta_high, F(r, 3)-k*beta_low
            else:
                low, high = F(r, 3)+k*beta_low, F(r, 3)+k*beta_high
            whole = low.numerator//low.denominator
            assert whole == high.numerator//high.denominator
            events.append((low-whole, high-whole, r))
    events.sort()
    assert len(events) == 3*q-1
    assert all(events[j][1] < events[j+1][0] for j in range(len(events)-1))
    assert 0 < events[0][0] and events[-1][1] < 1
    counts, maximum = initial[:], 0

    def certify():
        assert sum(counts) == q
        assert all(abs(3*c-q) <= 30 for c in counts)
        x, y = counts[0]-counts[2], counts[1]-counts[2]
        norm2 = x*x-x*y+y*y
        assert norm2 <= 900
        return norm2

    maximum = certify()
    for _, _, r in events:
        counts[(r-1) % 3] -= 1
        counts[r] += 1
        maximum = max(maximum, certify())
    # Right continuity assigns each endpoint to the cell just after its jump.
    counts[2] -= 1
    counts[0] += 1
    assert counts == initial
    return maximum


def board(t):
    colors = [0, 0, 0]
    power3, b = 1, 0
    while power3 <= t:
        value, a = power3, 0
        while value <= t:
            colors[(a-b) % 3] += 1
            value, a = 2*value, a+1
        power3, b = 3*power3, b+1
    return colors[0]-colors[2], colors[1]-colors[2]


def correction(a, b):
    value = times(minus((1, 0), ROOT[-a % 3]),
                  minus((1, 0), ROOT[-2*b % 3]))
    assert value[0] % 3 == value[1] % 3 == 0
    return value[0]//3, value[1]//3


def patch(b):
    floor = lambda k: (3**k).bit_length()-1
    isolated = floor(b)-floor(b-1) == 2
    patched = floor(b-1)-floor(b-3) == 4
    assert not (isolated and patched)
    if isolated:
        return ROOT[(floor(b)-2*b) % 3]
    if patched:
        return ROOT[(floor(b-1)-1-2*b) % 3]
    return 0, 0


def check():
    lo, hi, denominators = beta_data()
    maxima = {q: (all_phases(q, 1, lo, hi), all_phases(q, -1, lo, hi))
              for q in denominators}
    width = 86
    aa = [rotate(board(2**a), -a) for a in range(width)]
    bb = [rotate(board(3**b), b) for b in range(width)]
    assert aa[0] == aa[9] == (1, 0)
    assert minus(aa[3], aa[0]) == (0, -1)
    assert minus(aa[12], aa[9]) == (-1, -1)
    first = {}
    for total in range(4, width):
        for b in range(4, total+1):
            a = total-b
            state = minus(plus(minus(plus(aa[a], bb[b]), (1, 0)),
                               correction(a, b)), patch(b))
            first.setdefault(state, (total, a, b))
    for total, a, b in first.values():
        weight = F(1, 2**a*3**b)
        assert weight >= F(1, 3**total)
        tail = F(6, 2**total)-F(3, 3**total)
        assert weight <= tail
    for total in range(width):
        by_rows = sum((F(2, 2**(total-b)*3**b) for b in range(total)),
                      F(3, 3**total))
        assert by_rows == F(6, 2**total)-F(3, 3**total)
    print('PASS: exact ordered phase cells, both beta directions:', maxima)
    print('PASS: original-board axes, actual ambiguity, first arrivals:', len(first))


if __name__ == '__main__':
    check()
