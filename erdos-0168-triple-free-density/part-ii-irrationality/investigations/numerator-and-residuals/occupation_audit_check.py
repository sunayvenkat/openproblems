"""Independent exact occupation/Green audit; no project imports."""
from collections import defaultdict
from fractions import Fraction as Q

ONE, OMEGA, OMEGA2 = (1, 0), (0, 1), (-1, -1)
STATES = ((0, 1, (0, -1)), (1, 1, (0, 0)), (2, 0, ONE),
          (2, 2, ONE), (1, 2, ONE), (2, 1, ONE),
          (1, 0, (0, -1)), (0, 2, ONE))


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[0], -a[1]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]-a[1]*b[1]


def root(k):
    return (ONE, OMEGA, OMEGA2)[k % 3]


def rotate(z, k):
    return mul(z, root(k))


def counts(t):
    out, value3, b = [0, 0, 0], 1, 0
    while value3 <= t:
        value, a = value3, 0
        while value <= t:
            out[(a-b) % 3] += 1
            value, a = 2*value, a+1
        value3, b = 3*value3, b+1
    return out


def imbalance(t):
    v = counts(t)
    return v[0]-v[2], v[1]-v[2]


def actual_axes(width):
    return ([rotate(imbalance(2**a), -a) for a in range(width)],
            [rotate(imbalance(3**b), b) for b in range(width)])


def correction(i, j):
    z = mul(sub(ONE, root(-i)), sub(ONE, root(-2*j)))
    assert z[0] % 3 == z[1] % 3 == 0
    return z[0]//3, z[1]//3


def event(b, floor_beta):
    m = floor_beta
    isolate, patch = m(b)-m(b-1) == 2, m(b-1)-m(b-3) == 4
    assert not (isolate and patch)
    return root(m(b)-2*b) if isolate else root(m(b-1)-1-2*b) if patch else (0, 0)


def minimum(z):
    return min(0, *z)


def cone(z):
    return minimum(z)-minimum(sub(z, ONE))


def phi(z, b):
    if b == 0:
        return 0
    if b == 1:
        return cone(rotate(sub(z, ONE), 1))
    if b == 2:
        return cone(sub(z, OMEGA2))
    if b == 3:
        return 1-cone(rotate(add(z, OMEGA), 2))
    return cone(z)


def green(z, b, u, v):
    return phi(z, b)-phi(sub(z, u), b)-phi(sub(z, v), b)+phi(sub(sub(z, u), v), b)


def offset(state, i, j):
    p, q, endpoint = state
    gamma = root(2*p-q)
    s = tuple(sum(root(-k)[d] for k in range(p)) for d in range(2))
    prefix = tuple(sum(root(-k)[d] for k in range(1, i+1)) for d in range(2))
    return add(add(sub(endpoint, gamma), rotate(mul(s, prefix), -q)), correction(i+q, j))


def point(state, a, b, aa, bb, ev):
    p, q, _ = state
    z = add(add(rotate(aa[a], 2*p-q), sub(bb[b], ONE)), offset(state, a % 3, b % 3))
    return sub(z, ev(b)) if b >= 4 else z


def occupations(state, aa, bb, ev, hw, vw):
    horizontal = [defaultdict(Q) for _ in range(3)]
    vertical = [defaultdict(Q) for _ in range(3)]
    for a, w in hw:
        horizontal[a % 3][aa[a]] += w
    for b, w in vw:
        vertical[b % 3][sub(sub(bb[b], ONE), ev(b))] += w
    out = [defaultdict(Q) for _ in range(5)]
    p, q, _ = state
    for i in range(3):
        for x, wx in horizontal[i].items():
            x = rotate(x, 2*p-q)
            for j in range(3):
                shift = offset(state, i, j)
                for y, wy in vertical[j].items():
                    out[4][add(add(x, y), shift)] += wx*wy
            for b in range(4):
                z = add(add(x, sub(bb[b], ONE)), offset(state, i, b % 3))
                out[b][z] += wx*Q(1, 3**b)
    return out


def hit(measures):
    return sum((w*phi(z, b) for b, measure in enumerate(measures)
                for z, w in measure.items()), Q(0))


def tau(t):
    c, e, a = counts(t), 2, 1
    while e <= t:
        if 3*e > 2*t or (6*e <= t and 4*t < 27*e):
            c[a % 3] -= 1
        e, a = 2*e, a+1
    return min(c)


def floored(n, p, q, side):
    v, r = divmod(n*p, q)
    return v-int(n > 0 and r == 0 and side < 0)


def partial_roots(m, direction):
    return tuple(sum(((m+3-r)//3)*root(direction*r)[d] for r in range(3)) for d in range(2))


def rational_axes(p, q, side):
    # Each axis point is rebuilt as its own complete colored triangle.
    aa = [tuple(sum(rotate(partial_roots(floored(k, p, q, side), -1), -k)[d]
                    for k in range(a+1)) for d in range(2)) for a in range(3*q)]
    bb = [tuple(sum(rotate(partial_roots(floored(k, q, p, -side), 1), k)[d]
                    for k in range(b+1)) for d in range(2)) for b in range(4+3*p)]
    ev = lambda b: event(b, lambda k: floored(k, q, p, -side))
    return aa, bb, ev


def main():
    rules = ((1, ONE, OMEGA, ONE, 1), (2, OMEGA, OMEGA2, OMEGA2, 1),
             (3, ONE, OMEGA2, neg(OMEGA), -1), (4, OMEGA, OMEGA2, (0, 0), 1))
    for b, u, v, vertex, sign in rules:
        for x in range(-12, 13):
            for y in range(-12, 13):
                assert green((x, y), b, u, v) == sign*int((x, y) == vertex)
    width = 48
    aa, bb = actual_axes(width)
    ev = lambda b: event(b, lambda k: (3**k).bit_length()-1)
    hw, vw = [(a, Q(1, 2**a)) for a in range(width)], [(b, Q(1, 3**b)) for b in range(4, width)]
    for state in STATES:
        measures = occupations(state, aa, bb, ev, hw, vw)
        gamma = root(2*state[0]-state[1])
        product = -3*sum((w*(phi(z, b)-phi(sub(z, gamma), b))
                         for b, measure in enumerate(measures) for z, w in measure.items()), Q(0))
        direct = -3*sum((Q(phi(point(state, a, b, aa, bb, ev), b)-phi(sub(point(state, a, b, aa, bb, ev), gamma), b), 2**a*3**b)
                        for a in range(width) for b in range(width)), Q(0))
        assert product == direct
        for b, u, v, vertex, sign in rules:
            for t in ((0, 0), ONE, OMEGA, OMEGA2):
                assert sum((w*green(add(z, t), b, u, v) for z, w in measures[b].items()), Q(0)) == sign*measures[b].get(sub(vertex, t), 0)
    target_state = (0, 0, ONE)
    target = occupations(target_state, aa, bb, ev, hw, vw)
    for a, b in ((0, 0), (0, 1), (0, 3), (1, 1), (4, 4), (5, 11), (9, 28)):
        eta = phi(point(target_state, a, b, aa, bb, ev), b)+int((a, b) == (0, 1))
        d = 2**a*3**b
        assert eta == tau(d)-tau(d-1)
    arrivals, seen = [], set()
    for a in range(0, width-4, 3):
        z = point(target_state, a, 4, aa, bb, ev)
        assert sub(z, aa[a]) == sub(point(target_state, 0, 4, aa, bb, ev), aa[0])
        if z in seen:
            continue
        seen.add(z)
        first = next(n for n in range(4, a+5) if any(point(target_state, n-b, b, aa, bb, ev) == z for b in range(4, n+1)))
        mass = target[4][z]
        assert 0 < mass <= 6*Q(1, 2**first)-3*Q(1, 3**first)
        t = neg(z)
        assert sum((w*green(add(v, t), 4, OMEGA, OMEGA2) for v, w in target[4].items()), Q(0)) == mass
        arrivals.append(first)
    assert arrivals == [4, 5, 7, 7, 12, 26]
    for m in range(1, 16):
        a = 3*m
        assert aa[a] == imbalance(2**a)
        cutoff, power, B = 2**a, 1, 0
        while 3*power <= cutoff:
            power, B = 3*power, B+1
        term1 = tuple(sum(root(-b)[d] for b in range(B+1)) for d in range(2))
        term2 = tuple(sum(root(-b-((3**b).bit_length() if b else 0))[d] for b in range(B+1)) for d in range(2))
        assert mul(sub(ONE, OMEGA), aa[a]) == sub(term1, rotate(term2, 1))
    expected = (
        (12, 19, -1, Q(201116241599904565211114506221741, 166391666115415563903967476414104)),
        (53, 84, 1, Q(1106793835140114365492535503121476894594518310415517554033885988368224891718553541788520178420055314260469385348488993481337318090511671013266912038039, 915695663414394258127824526994549076312198308171469312633289353616390697978024573371286542119417810828829150116694961649996528870660370694500217403585)))
    for p, q, side, value in expected:
        ma, mb, me = rational_axes(p, q, side)
        horizontal = [(a, Q(1, 2**a)/(1-Q(1, 2**(3*q)))) for a in range(3*q)]
        vertical = [(b, Q(1, 3**b)/(1-Q(1, 3**(3*p)))) for b in range(4, 4+3*p)]
        model = occupations(target_state, ma, mb, me, horizontal, vertical)
        assert 2-3*hit(model) == value
    print('PASS: independent board axes, all8 occupation products, low-row kernels, origin and complete rational models')
    print('FINITE_FIRST_ARRIVALS', arrivals, '; independent actual row-sum/Kesten sampling checks pass')


if __name__ == '__main__':
    main()
