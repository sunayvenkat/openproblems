"""Independent original-board audit of guarded transport; no bridge claim."""
from fractions import Fraction as Q
from functools import cmp_to_key


ZERO, ONE, W, W2 = (0, 0), (1, 0), (0, 1), (-1, -1)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[0], -a[1]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0] - a[1]*b[1]


def rotate(a, k):
    return mul(a, (ONE, W, W2)[k % 3])


def board_counts(t):
    counts = [0, 0, 0]
    b, three = 0, 1
    while three <= t:
        top = (t // three).bit_length() - 1
        for color in range(3):
            first = (color + b) % 3
            if first <= top:
                counts[color] += 1 + (top-first)//3
        b, three = b+1, three*3
    return counts


def imbalance(t):
    counts = board_counts(t)
    return counts[0]-counts[2], counts[1]-counts[2]


def correction_root(t):
    a = t.bit_length()-1
    if a >= 1 and 3*(1 << a) > 2*t:
        return a
    if t >= 12:
        a = (t//6).bit_length()-1
        if a >= 1 and 6*(1 << a) <= t and 4*t < 27*(1 << a):
            return a
    return None


def tau(t):
    if t < 3:
        return 0
    counts = board_counts(t)
    root = correction_root(t)
    if root is not None:
        counts[root % 3] -= 1
    return min(counts)


def color(i, j):
    value = mul(sub(ONE, rotate(ONE, -i)), sub(ONE, rotate(ONE, -2*j)))
    assert value[0] % 3 == value[1] % 3 == 0
    return value[0]//3, value[1]//3


def minimum(z):
    return min(0, z[0], z[1])


def cone(z):
    return minimum(z)-minimum(sub(z, ONE))


def row(z, b):
    if b == 0:
        return 0
    if b == 1:
        return cone(rotate(sub(z, ONE), 1))
    if b == 2:
        return cone(sub(z, W2))
    if b == 3:
        return 1-cone(rotate(add(z, W), 2))
    return cone(z)


def log_ratio(x, terms=75):
    r = Q(x-1, x+1)
    value = 2*sum((r**(2*k+1)/(2*k+1) for k in range(terms)), Q(0))
    tail = 2*r**(2*terms+1)/((2*terms+1)*(1-r*r))
    return value, value+tail


# ln(3)=ln(2)+ln(3/2), unlike the companion's direct ln(3) series.
l2 = log_ratio(Q(2))
l32 = log_ratio(Q(3, 2))
l3 = l2[0]+l32[0], l2[1]+l32[1]
ALPHA = l2[0]/l3[1], l2[1]/l3[0]
BETA = 1/ALPHA[1], 1/ALPHA[0]


def bounds(x, angle):
    r, s = x
    ends = r+s*angle[0], r+s*angle[1]
    return min(ends), max(ends)


def floor(x, angle):
    lo, hi = bounds(x, angle)
    a, b = lo.numerator//lo.denominator, hi.numerator//hi.denominator
    assert a == b
    return a


def phase(n, angle):
    return Q(-floor((0, n), angle)), Q(n)


def partial(m, vertical=False):
    return tuple(sum(rotate(ONE, (1 if vertical else 2)*k)[j]
                     for k in range(m % 3+1)) for j in range(2))


def displacement(x, length, angle, vertical=False):
    total = ZERO
    for s in range(1, length+1):
        digit = floor((3*x[0], 3*x[1]+s), angle)
        total = add(total, rotate(partial(digit, vertical), (-2 if vertical else -1)*s))
    return total


def phase_event(x, j):
    at = lambda k: floor((3*x[0], 3*x[1]+k), BETA)
    isolated = at(j)-at(j-1) == 2
    patched = at(j-1)-at(j-3) == 4
    assert not (isolated and patched)
    return rotate(ONE, at(j)-2*j) if isolated else (
        rotate(ONE, at(j-1)-1-2*j) if patched else ZERO)


def phase_cuts(angle, offsets):
    points = {(Q(0), Q(0)), (Q(1), Q(0))}
    for s in offsets:
        f = floor((0, s), angle)
        for k in range(f+1, f+4):
            point = Q(k, 3), Q(-s, 3)
            lo, hi = bounds(point, angle)
            if lo > 0 and hi < 1:
                points.add(point)
    def compare(a, b):
        if a == b:
            return 0
        lo, hi = bounds((a[0]-b[0], a[1]-b[1]), angle)
        assert lo > 0 or hi < 0
        return 1 if lo > 0 else -1
    return sorted(points, key=cmp_to_key(compare))


def check():
    width = 84
    aa = [rotate(imbalance(1 << a), -a) for a in range(width)]
    bb = [rotate(imbalance(3**b), b) for b in range(width)]
    def event(b):
        root = correction_root(3**b)
        return ZERO if root is None else rotate(ONE, root+b)
    def state(a, b):
        z = add(sub(add(aa[a], bb[b]), ONE), color(a % 3, b % 3))
        return sub(z, event(b)) if b >= 4 else z

    for n in range(24):
        for i in range(4):
            assert aa[3*n+i] == add(aa[3*n], displacement(phase(n, ALPHA), i, ALPHA))
            assert bb[3*n+i] == add(bb[3*n], displacement(phase(n, BETA), i, BETA, True))
        for j in range(3):
            if 3*n+j >= 4:
                assert phase_event(phase(n, BETA), j) == event(3*n+j)

    for a, b in ((0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (4, 5), (7, 3)):
        t = (1 << a)*3**b
        assert tau(t)-tau(t-1) == row(state(a, b), b)+int((a, b) == (0, 1))
    assert row(state(0, 1), 1) == 0 and tau(3)-tau(2) == 1

    # Independently check high correction on every vertical phase cell,
    # using fractional threshold inequalities from the original root windows.
    points = phase_cuts(BETA, range(-3, 4))
    for left, right in zip(points, points[1:]):
        x = (left[0]+right[0])/2, (left[1]+right[1])/2
        for j in range(3):
            fj = floor((3*x[0], 3*x[1]+j), BETA)
            fp = floor((3*x[0], 3*x[1]+j-1), BETA)
            iso = bounds((3*x[0]-fj+1, 3*x[1]+j-1), BETA)[1] < 0
            patch = bounds((3*x[0]-fp+3, 3*x[1]+j-3), BETA)[1] < 0
            assert not (iso and patch)
            direct = rotate(ONE, fj+j) if iso else rotate(ONE, fp-1+j) if patch else ZERO
            assert phase_event(x, j) == direct

    for length in range(1, 6):
        points = phase_cuts(ALPHA, range(1, 3*length+1))
        values = [displacement(((a[0]+b[0])/2, (a[1]+b[1])/2), 3*length, ALPHA)
                  for a, b in zip(points, points[1:])]
        assert len(points)-2 == 9*length
        assert all(x != y for x, y in zip(values, values[1:]))
        assert values[0] == values[-1]

    nmax, length = 4, 4
    starts = (2, 1, 1)
    for shift in (ZERO, ONE, W, W2, (2, -1)):
        corner = Q(0)
        for i in range(3):
            for j in range(3):
                first, stop = starts[j], starts[j]+length
                def h(n, m):
                    return cone(add(state(3*n+i, 3*m+j), shift))
                def block(du, dv):
                    return sum((Q(h(n+du, m+dv), 8**n*27**m)
                                for n in range(nmax) for m in range(first, stop)), Q(0))
                lhs = 216*block(0, 0)-27*block(1, 0)-8*block(0, 1)+block(1, 1)
                rhs = 216*(Q(h(0, first), 27**first)-Q(h(nmax, first), 8**nmax*27**first)
                           -Q(h(0, stop), 27**stop)+Q(h(nmax, stop), 8**nmax*27**stop))
                assert lhs == rhs
                corner += 216*Q(h(0, first), 2**i*3**(3*first+j))
        assert (27*corner).denominator == 1
        for i in range(3):
            for b in range(4):
                f = lambda n: row(add(state(3*n+i, b), shift), b)
                lhs = sum((Q(8*f(n)-f(n+1), 8**n) for n in range(9)), Q(0))
                assert lhs == 8*f(0)-Q(f(9), 8**8)

    assert aa[0] == aa[9] == ONE
    assert sub(aa[3], aa[0]) == neg(W)
    assert sub(aa[12], aa[9]) == W2
    assert 216-27*8-8*27+216 == 0
    print('PASS: original-board axes, lifted floors, all vertical guards and origin')
    print('PASS: 9L genuine cuts, complete high216/low8 identities with terminals')
    print('PASS: finite corner integrality and actual same-state transition ambiguity')


if __name__ == '__main__':
    check()
