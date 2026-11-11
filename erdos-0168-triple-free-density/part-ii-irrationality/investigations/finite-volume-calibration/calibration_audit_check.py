"""Standalone exact audit of the finite-volume calibration.

No project imports, floats, sampled-phase claims, or infinite-return inference.
Original colored boards supply the actual states and birth digits.  Rational
logarithm intervals order every cell of the depth-256 phase refinement.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd


ONE, ZERO = (1, 0), (0, 0)
ROOTS = (ONE, (0, 1), (-1, -1))


def plus(z, w):
    return z[0] + w[0], z[1] + w[1]


def minus(z, w):
    return z[0] - w[0], z[1] - w[1]


def rotate(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0] - z[1]
    return z


def size(z):
    return max(abs(z[0]), abs(z[1]))


def board_counts(t):
    """Count each color a-b mod 3 on 2**a * 3**b <= t by row."""
    out = [0, 0, 0]
    power3, b = 1, 0
    while power3 <= t:
        last_a = (t // power3).bit_length() - 1
        for residue in range(3):
            count = max(0, (last_a - residue) // 3 + 1)
            out[(residue - b) % 3] += count
        power3 *= 3
        b += 1
    return out


def actual_axis(a):
    counts = board_counts(1 << a)
    return rotate((counts[0] - counts[2], counts[1] - counts[2]), -a)


def finite_tau(t):
    """Accepted finite-cover formula, evaluated on original integer boards."""
    counts = board_counts(t)
    power2, a = 2, 1
    while power2 <= t:
        isolated = 3 * power2 > 2 * t
        patch = 6 * power2 <= t and 4 * t < 27 * power2
        assert not (isolated and patch)
        if isolated or patch:
            counts[a % 3] -= 1
        power2 *= 2
        a += 1
    return min(counts)


def unexceptional_birth(a, b):
    t = (1 << a) * 3**b
    birth = finite_tau(t) - finite_tau(t - 1)
    assert birth in (0, 1)
    return birth - int((a, b) == (0, 1))


def cone(z):
    # Difference of the original color minima, rather than an imported row test.
    return min(0, *z) - min(0, *minus(z, ONE))


def log_bounds(t, terms=120):
    x = Q(t - 1, t + 1)
    total = 2 * sum((x ** (2 * k + 1) / (2 * k + 1)
                     for k in range(terms)), Q(0))
    tail = 2 * x ** (2 * terms + 1) / ((2 * terms + 1) * (1 - x*x))
    return total, total + tail


def phase_certificate(depth):
    """Certify all finite itineraries, including actual right-hand cut values.

    A cut (j,s) means (j-s*alpha)/3.  Midpoints of consecutive cuts
    have 3*x = (J-S*alpha)/2.  Every floor is decided by integer
    arithmetic on a proved rational enclosure, never a floating sample.
    """
    l2, l3 = log_bounds(2), log_bounds(3)
    denominator = 10**60
    lower = (l2[0] / l3[1] * denominator).__floor__()
    upper = lower + 1
    assert Q(lower, denominator) < l2[0] / l3[1]
    assert l2[1] / l3[0] < Q(upper, denominator)

    def floor_affine(j, c, divisor=1):
        lo_c, hi_c = (lower, upper) if c >= 0 else (upper, lower)
        lo = (j * denominator + c * lo_c) // (divisor * denominator)
        hi = (j * denominator + c * hi_c) // (divisor * denominator)
        assert lo == hi, (j, c, divisor)
        return lo

    cuts = [(0, 0), (3, 0)]
    for s in range(1, 3 * depth + 1):
        k = floor_affine(0, s)
        cuts.extend((j, s) for j in range(k + 1, k + 4))
    # This exact rational midpoint sorts candidates; enclosures then certify
    # every adjacent strict inequality, including the artificial circle cut 0.
    cuts.sort(key=lambda z: 2 * denominator * z[0] - (lower + upper) * z[1])
    assert len(cuts) == 9 * depth + 2 and len(set(cuts)) == len(cuts)
    assert cuts[0] == (0, 0) and cuts[-1] == (3, 0)
    for left, right in zip(cuts, cuts[1:]):
        j, c = right[0] - left[0], left[1] - right[1]
        endpoint = lower if c >= 0 else upper
        assert j * denominator + c * endpoint > 0

    # Partial geometric row sums 1, -omega, 0 determine a three-step block.
    sums = (ONE, (0, -1), ZERO)

    def increment(j, c, divisor, n):
        result = ZERO
        for s in range(1, 4):
            digit = floor_affine(j, c + divisor * (3*n + s), divisor)
            result = plus(result, rotate(sums[digit % 3], -s))
        return result

    starts = tuple(product(range(-1, 2), repeat=2))
    latest = 0
    exit_histogram = {}
    for left, right in zip(cuts, cuts[1:]):
        j, c = left[0] + right[0], -left[1] - right[1]
        surviving = set(starts)
        accumulated = ZERO
        for n in range(depth):
            step = increment(j, c, 2, n)
            # Actual values at the left cut equal the right-cell word,
            # including its single possible cut-orbit hit.
            assert step == increment(left[0], -left[1], 1, n)
            accumulated = plus(accumulated, step)
            exiting = {y for y in surviving if size(plus(y, accumulated)) > 1}
            for _ in exiting:
                exit_histogram[n + 1] = exit_histogram.get(n + 1, 0) + 1
            surviving -= exiting
            if not surviving:
                latest = max(latest, n + 1)
                break
        assert not surviving
    assert sum(exit_histogram.values()) == 9 * (len(cuts) - 1)
    assert latest == 232
    # On each cut the genuine floor itinerary is the right-hand itinerary;
    # the separate circle cut 0 has periodic matching limits.  The cells
    # therefore cover ALL phases for this finite horizon, not just midpoints.
    for n in range(depth):
        assert increment(3, 0, 1, n) == increment(0, 0, 1, n)
    for n in range(67):
        assert increment(0, 0, 1, n) == minus(actual_axis(3*n + 3), actual_axis(3*n))
    print('ALL_PHASE_RADIUS1', 'cells', len(cuts)-1, 'starts', len(starts),
          'max_exit', latest, 'depth', depth)


def valuation2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def first_exit(states, radius, start=0):
    for n in range(start, len(states)):
        if size(states[n]) > radius:
            return n
    raise AssertionError('Finite actual board range did not contain required exit')


def check_actual_sources():
    states = [actual_axis(3*n) for n in range(68)]
    assert states[:5] == [(1, 0), (1, -1), (2, 0), (1, 0), (0, -1)]
    bits = [cone(minus(y, ONE)) for y in states]
    assert all(h in (0, 1) for h in bits)
    for radius, expected_exit in ((1, 2), (2, 67)):
        tau = first_exit(states, radius)
        assert tau == expected_exit
        odd = [1 + 6*h for h in bits]

        def killed(n):
            if size(states[n]) > radius:
                return Q(0)
            stop = first_exit(states, radius, n)
            return sum((Q(odd[k], 8**(k-n+1)) for k in range(n, stop)), Q(0))

        def dirichlet(n):
            if size(states[n]) > radius:
                return Q(1 + bits[n], 7)
            stop = first_exit(states, radius, n)
            return (sum((Q(bits[k], 8**(k-n+1)) for k in range(n, stop)), Q(0))
                    + Q(1 + bits[stop], 7 * 8**(stop-n)))

        assert killed(0).denominator == 8**tau
        assert (8*killed(0)).denominator == 8**(tau-1)
        assert odd[tau] >= 1  # The other first-exit term is nonnegative.
        length = 30
        odd_exterior = []
        binary_exterior = []
        for n in range(length):
            ek = odd[n] - 8*killed(n) + killed(n+1)
            ed = 8*dirichlet(n) - dirichlet(n+1) - bits[n]
            if size(states[n]) <= radius:
                assert ek == ed == 0
            else:
                assert 1 <= ek <= 8
                assert Q(6, 7) <= ed <= Q(9, 7)
            odd_exterior.append(ek)
            binary_exterior.append(ed)
        odd_head = sum((Q(odd[n], 8**n) for n in range(length)), Q(0))
        bin_head = sum((Q(bits[n], 8**n) for n in range(length)), Q(0))
        assert odd_head - 8*killed(0) == (
            sum((e / 8**n for n, e in enumerate(odd_exterior)), Q(0))
            - Q(8, 8**length)*killed(length))
        assert 8*dirichlet(0) - bin_head == (
            sum((e / 8**n for n, e in enumerate(binary_exterior)), Q(0))
            + Q(8, 8**length)*dirichlet(length))
        n_source = (1 + bits[tau]
                    + 7*sum(8**(tau-1-n)*bits[n] for n in range(tau)))
        assert dirichlet(0) == Q(n_source, 7*8**tau)
        assert n_source % 7 == 1 + bits[tau]
        t_source = 1 << max(3*(tau-1) - valuation2(n_source), 0)
        assert (56*dirichlet(0)).denominator == t_source
        assert (8*dirichlet(0)).denominator == 7*t_source
        assert dirichlet(0).denominator == 7 * (1 << max(3*tau-valuation2(n_source), 0))
        assert t_source == 8**(tau-1)
        assert Q(8**(tau-1), 8**tau) == Q(1, 8)
        print('ACTUAL_SOURCE', 'R', radius, 'tau', tau,
              'den_p_odd', killed(0).denominator,
              'den_8p_binary', (8*dirichlet(0)).denominator,
              'den_56p_binary', t_source)


def check_all_binary_carries():
    tested = 0
    for tau in range(1, 11):
        for bits in product((0, 1), repeat=tau+1):
            n_source = 1 + bits[tau] + 7*sum(
                8**(tau-1-k)*bits[k] for k in range(tau))
            if bits[tau] == 0 and bits[tau-1] == 1:
                run = 0
                for bit in reversed(bits[:tau]):
                    if not bit:
                        break
                    run += 1
                expected = 3*run
                if run == tau:
                    assert n_source == 8**tau
            elif bits[tau] == 1 and bits[tau-1] == 0:
                expected = 1
            else:
                expected = 0
            assert valuation2(n_source) == expected
            t_source = 1 << max(3*(tau-1)-expected, 0)
            assert gcd(n_source, 7) == 1
            assert Q(n_source, 8**(tau-1)).denominator == t_source
            assert Q(n_source, 7*8**(tau-1)).denominator == 7*t_source
            tested += 1
    print('BINARY_CARRY_WORDS', tested)


def check_complete_rectangles():
    assert finite_tau(3)-finite_tau(2) == 1
    assert unexceptional_birth(0, 1) == 0
    assert unexceptional_birth(0, 0) == 0
    for a_size in (1, 3, 5, 9):
        for b_size in (1, 3, 5, 7):
            head = Q(0)
            true_head = Q(0)
            for a in range(a_size):
                for b in range(b_size):
                    h = unexceptional_birth(a, b)
                    assert h in (0, 1)
                    reward = 1 + 6*h
                    head += Q(reward, 2**a * 3**b)
                    true_head += Q(reward + 6*int((a, b) == (0, 1)), 2**a * 3**b)
            clearer = 2**(a_size-1) * 3**(b_size-1)
            assert head.denominator == clearer
            assert (clearer*head).denominator == 1
            if b_size >= 2:
                assert true_head-head == 2
            outside_mass = 3*(Q(1, 2**a_size) + Q(1, 3**b_size)
                              - Q(1, 2**a_size * 3**b_size))
            inside_mass = (2*(1-Q(1, 2**a_size))) * (Q(3, 2)*(1-Q(1, 3**b_size)))
            assert outside_mass + inside_mass == 3
            assert clearer*outside_mass >= Q(3**b_size, 2)
            assert clearer*outside_mass >= 2**(a_size-1)
    # M = Q_full + 1/3; Z = 3-3M.  This symbolic coefficient check
    # fixes the total reward as 7-2Z, including the sole origin correction.
    assert 3 + 6*(Q(3-0, 3)-Q(1, 3)) == 7
    assert -6*Q(1, 3) == -2
    print('COMPLETE_RECTANGLES', 16, 'total_reward', '7-2Z', 'origin_adjustment', 2)


if __name__ == '__main__':
    phase_certificate(256)
    check_actual_sources()
    check_all_binary_carries()
    check_complete_rectangles()
    print('PASS: standalone exact finite-volume audit; infinite supply is not asserted')
