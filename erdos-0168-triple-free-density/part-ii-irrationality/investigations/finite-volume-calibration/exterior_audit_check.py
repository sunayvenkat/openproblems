"""Independent exact exterior audit: stdlib only, no project imports or floats.

Original colored-board counts reconstruct A, B and the actual states.  Original
root windows reconstruct E.  Finite checks supplement the proofs in the audit;
unboundedness and the global height theorem remain explicitly accepted inputs.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product

ZERO, ONE, OM, OM2 = (0, 0), (1, 0), (0, 1), (-1, -1)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def neg(z):
    return -z[0], -z[1]


def sub(z, w):
    return add(z, neg(w))


def mul(z, w):
    return z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0] - z[1]*w[1]


def rot(z, exponent):
    for _ in range(exponent % 3):
        z = -z[1], z[0] - z[1]
    return z


def green(z):
    x, y = z
    return y - x, -x


def rho(z):
    return max(map(abs, green(z)))


def cone(z):
    s, t = green(z)
    return int(s >= 0 and t >= 0)


def mixed(f, z):
    return f(z) - f(sub(z, OM)) - f(sub(z, OM2)) + f(add(z, ONE))


def board_counts(cutoff):
    """Original 2^a 3^b <= cutoff, with colors a-b mod 3."""
    counts, p3, b = [0, 0, 0], 1, 0
    while p3 <= cutoff:
        last = (cutoff // p3).bit_length() - 1
        for color in range(3):
            first = (color + b) % 3
            if first <= last:
                counts[color] += (last - first) // 3 + 1
        p3, b = 3*p3, b+1
    return counts


def board(cutoff):
    counts = board_counts(cutoff)
    return counts[0] - counts[2], counts[1] - counts[2]


def correction(a, b):
    numerator = mul(sub(ONE, rot(ONE, -a)), sub(ONE, rot(ONE, -2*b)))
    assert numerator[0] % 3 == numerator[1] % 3 == 0
    return numerator[0] // 3, numerator[1] // 3


def root_event(b):
    """Original isolate/patch windows at cutoff 3^b, before normalizing."""
    cutoff, roots, root, exponent = 3**b, [], 2, 1
    while root <= cutoff:
        isolate = 3*root > 2*cutoff
        patch = 6*root <= cutoff and 4*cutoff < 27*root
        if isolate or patch:
            roots.append((exponent, 'isolate' if isolate else 'patch'))
        root, exponent = 2*root, exponent+1
    assert len(roots) <= 1
    return (rot(ONE, roots[0][0] + b) if roots else ZERO), roots


def original_tau(clock):
    counts = board_counts(clock // 2)
    root, exponent = 2, 1
    while 2*root <= clock:
        if 3*root > clock or (12*root <= clock and 2*clock < 27*root):
            counts[exponent % 3] -= 1
        root, exponent = 2*root, exponent+1
    return min(counts)


def box_corners(radius):
    r = radius
    return [((-r, 0), 1), ((-r, -2*r-1), -1),
            ((r+1, 2*r+1), -1), ((r+1, 0), 1)]


def box_indicator(z, radius):
    return sum(sign*cone(add(z, shift)) for shift, sign in box_corners(radius))


def triangle_tail(m):
    # Sum all a >= max(m-b,0) first; b >= m is an infinite geometric tail.
    return (sum((Q(2, 2**(m-b)*3**b) for b in range(m)), Q(0))
            + Q(3, 3**m))


def main():
    width = 160
    aa = [rot(board(2**a), -a) for a in range(width)]
    bb = [rot(board(3**b), b) for b in range(width)]
    ee = [ZERO]*4 + [root_event(b)[0] for b in range(4, width)]

    def state(a, b):
        return sub(add(sub(add(aa[a], bb[b]), ONE), correction(a, b)), ee[b])

    # Independently compare original root windows with the closed floor tests.
    floors = [(3**b).bit_length()-1 for b in range(width)]
    root_kinds = set()
    for b in range(4, width):
        isolate = floors[b] - floors[b-1] == 2
        patch = floors[b-1] - floors[b-3] == 4
        assert not (isolate and patch)
        expected = (rot(ONE, floors[b]-2*b) if isolate else
                    rot(ONE, floors[b-1]-1-2*b) if patch else ZERO)
        assert ee[b] == expected
        root_kinds.update(kind for _, kind in root_event(b)[1])
    assert root_kinds == {'isolate', 'patch'}

    # Original minima, no imported row predicates.  The full finite optimum
    # formula is an accepted input; these are direct coefficient checks.
    minimum_samples = [(0, 0), (0, 1), (0, 3), (1, 1), (4, 4),
                       (5, 11), (12, 8), (22, 35), (96, 4)]
    for a, b in minimum_samples:
        x, y = state(a, b)
        low = (0 if b == 0 else int(x >= 1 and y >= 0) if b == 1 else
               int(x <= -1 and x <= y) if b == 2 else int(min(x, 0) <= y))
        h = cone((x, y)) if b >= 4 else low
        h += int((a, b) == (0, 1))
        clock = 2**(a+1)*3**b
        assert h == original_tau(clock) - original_tau(clock-1)

    grid = [(x, y) for x in range(-18, 19) for y in range(-18, 19)]
    for z in grid:
        x, y = z
        s, t = green(z)
        assert add((0, s), (-t, -t)) == z
        assert rho(z) <= 2*max(abs(x), abs(y))
        assert max(abs(x), abs(y)) <= 2*rho(z)
        assert cone(z) == min(0, x, y) - min(0, x-1, y)
        assert mixed(cone, z) == int(z == ZERO)
        for r in range(7):
            assert box_indicator(z, r) == int(rho(z) <= r)
            assert box_indicator(z, r+3)-box_indicator(z, r) == int(r < rho(z) <= r+3)

    # Complete infinite tail algebra, not a truncated geometric sum.
    for m in range(50):
        exact = 6*Q(1, 2**m) - 3*Q(1, 3**m)
        assert triangle_tail(m) == exact
        assert 0 < exact <= 6*Q(1, 2**m)
    # The radius-to-index direction uses only N+1 > u => N >= floor(u).
    for denominator in range(1, 9):
        for numerator in range(101):
            u = Q(numerator, denominator)
            for n in range(51):
                if n+1 > u:
                    assert n >= u.numerator // u.denominator

    occupation = defaultdict(Q)
    for b in range(4, 128):
        for a in range(128-b):
            occupation[state(a, b)] += Q(1, 2**a*3**b)

    def q(shift):
        return sum((weight*cone(add(z, shift)) for z, weight in occupation.items()), Q(0))

    def box_mass(r):
        return sum((weight for z, weight in occupation.items() if rho(z) <= r), Q(0))

    for r in range(9):
        assert sum((sign*q(shift) for shift, sign in box_corners(r)), Q(0)) == box_mass(r)
        assert (box_mass(r+3)-box_mass(r) ==
                sum((weight for z, weight in occupation.items() if r < rho(z) <= r+3), Q(0)))

    # All root-unit choices give uniform three-step bounds, independently of
    # phase.  Residue correction C is unchanged under either index += 3.
    units = {ZERO, ONE, OM, OM2, neg(ONE), neg(OM), neg(OM2)}
    three = {add(add(u, v), w) for u, v, w in product(units, repeat=3)}
    event_values = {ZERO, ONE, OM, OM2}
    event_diff = {sub(u, v) for u, v in product(event_values, repeat=2)}
    vertical = {add(u, v) for u, v in product(three, event_diff)}
    joint = {add(u, v) for u, v in product(three, vertical)}
    assert max(map(rho, three)) == 3
    assert max(map(rho, vertical)) == 5
    assert max(map(rho, joint)) == 8
    for n in range(1, width):
        assert rho(sub(aa[n], aa[n-1])) <= 1
        assert rho(sub(bb[n], bb[n-1])) <= 1
    for a in range(64):
        for b in range(4, 64):
            z = state(a, b)
            assert correction(a+3, b) == correction(a, b+3) == correction(a, b)
            assert rho(sub(state(a+3, b), z)) <= 3
            assert rho(sub(state(a, b+3), z)) <= 5
            assert rho(sub(state(a+3, b+3), z)) <= 8

    path = [(a, state(a, 4)) for a in range(0, width, 3)]
    assert path[0] == (0, ZERO)
    for (_, z), (_, w) in zip(path, path[1:]):
        assert rho(sub(w, z)) <= 3
    crossings = []
    for r in range(max(rho(z) for _, z in path)):
        a, z = next((a, z) for a, z in path if rho(z) > r)
        assert r < rho(z) <= r+3
        assert Q(1, 2**a*3**4) > 0
        crossings.append((r, a, z))
    assert crossings[:2] == [(0, 3, (0, -1)), (1, 96, (1, -1))]

    # Compact arbitrary potentials: every mixed-difference row/column is zero.
    def check_marginals(support):
        cells = set()
        for z in support:
            cells.update((z, add(z, OM), add(z, OM2), sub(z, ONE)))
        rows, columns = defaultdict(Q), defaultdict(Q)
        for z in cells:
            value = mixed(lambda w: support.get(w, 0), z)
            s, t = green(z)
            rows[s] += value
            columns[t] += value
        assert all(v == 0 for v in rows.values())
        assert all(v == 0 for v in columns.values())

    check_marginals({(x, y): Q(x-2*y, abs(x)+abs(y)+1)
                     for x in range(-3, 4) for y in range(-3, 4)})
    for r in range(7):
        compact = {z: cone(z) for z in grid if max(map(abs, z)) <= r}
        check_marginals(compact)
        if r > 0:
            residuals = [mixed(lambda w: compact.get(w, 0), z)-int(z == ZERO) for z in grid]
            assert min(residuals) < 0 < max(residuals)
        square = lambda z, r=r: int(all(0 <= k <= r for k in green(z)))
        expected = {ZERO: 1, rot((r+1, 0), 1): -1,
                    rot((r+1, 0), 2): -1, (-r-1, 0): 1}
        for z in grid:
            assert mixed(square, z) == expected.get(z, 0)
    clipped = lambda z: cone(z)*int(max(map(abs, z)) <= 1)
    witnesses = []
    for (a, b), target, sign in [((12, 8), (-2, -2), -1), ((22, 35), (-1, 1), 1)]:
        z = state(a, b)
        residual = mixed(clipped, z)-int(z == ZERO)
        assert z == target and residual == sign
        assert occupation[z] >= Q(1, 2**a*3**b) > 0
        witnesses.append((a, b, aa[a], bb[b], correction(a, b), ee[b], z, sign))

    # Pointwise estimates cover every Boolean successor assignment.  Affinity
    # in g proves intermediate values from these exact endpoint calculations.
    high = [34*h-27*ha-8*hb+hab for h, ha, hb, hab in product((0, 1), repeat=4)]
    low = [h-ha for h, ha in product((0, 1), repeat=2)]
    assert (min(high), max(high)) == (-35, 35)
    assert (min(low), max(low)) == (-1, 1)
    for cap in (Q(0), Q(1, 2), Q(3)):
        for g in (-cap, cap):
            for h, ha, hb, hab in product((0, 1), repeat=4):
                p = lambda value: (value+cap+1)/182
                value = 216*p(h)-27*p(ha)-8*p(hb)+p(hab)-h-g
                assert value == cap+1-g+Q(34*h-27*ha-8*hb+hab, 182)
                assert Q(147, 182) <= value <= 2*cap+Q(217, 182)
            for h, ha in product((0, 1), repeat=2):
                value = 8*Q(h+cap+1, 7)-Q(ha+cap+1, 7)-h-g
                assert Q(6, 7) <= value <= 2*cap+Q(8, 7)

    # Larger exterior offsets allow a bounded-real Dirichlet construction by
    # contraction.  These extremal inequalities cover arbitrary phase maps;
    # the Banach-space proof, not a finite simulation, proves existence.
    assert Q(27+8+1, 216) == Q(1, 6)
    assert Q(1, 8) < 1
    for cap in (Q(0), Q(1, 2), Q(3), Q(100)):
        c = cap+1
        outer = c+Q(1, 182)
        interior = outer/5+c/180
        assert interior <= outer
        lower = 216*c-36*outer-c
        assert lower == 179*c-Q(18, 91) > 0
        for h in (0, 1):
            for g in (-cap, cap):
                for pa, pb, pab in product((-outer, outer), repeat=3):
                    value = 216*(c+Q(h, 182))-27*pa-8*pb+pab-h-g
                    assert lower <= value <= 252*outer+c
        low_outer = c+Q(1, 7)
        assert (low_outer+c)/7 <= low_outer
        low_lower = 8*c-low_outer-c
        assert low_lower == 6*c-Q(1, 7) > 0
        for h, g, pa in product((0, 1), (-cap, cap), (-low_outer, low_outer)):
            value = 8*(c+Q(h, 7))-pa-h-g
            assert low_lower <= value <= 9*low_outer+c

    print('PASS: independent original-board/root-window/minimum reconstruction')
    print('PASS: Green geometry, complete box/shell coefficients, complete full tails')
    print('PASS: compact zero marginals, signed actual occupied cutoff witnesses')
    print('PASS: all-unit phase bounds 3/5/8; high margin 147/182; low margin 6/7')
    print('PASS: real Dirichlet contraction and all-interface positive bounds')
    print('FIXED_ROW_FIRST_CROSSINGS', crossings)
    print('WITNESSES (a,b,A,B,C,E,state,residual)', witnesses)
    print('ORIGIN_COMPONENTS', aa[0], bb[4], correction(0, 4), ee[4], state(0, 4))
    print('SCOPE: finite rational-step feasibility, rational/cheap sources, and product-phase arithmetic remain unproved')


if __name__ == '__main__':
    main()
