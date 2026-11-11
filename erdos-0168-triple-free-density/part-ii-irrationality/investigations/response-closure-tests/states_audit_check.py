"""Independent exact replay of the two-node Farey extension; no companion imports."""
from fractions import Fraction


ONE = (1, 0)
ZERO = (0, 0)
ROOTS = (ONE, (0, 1), (-1, -1))


def plus(z, w):
    return z[0] + w[0], z[1] + w[1]


def minus(z, w):
    return z[0] - w[0], z[1] - w[1]


def times(z, w):
    a, b = z
    c, d = w
    return a*c - b*d, a*d + b*c - b*d


def root(k):
    return ROOTS[k % 3]


def roots_through(n, stride=1):
    z = ZERO
    for k in range(n + 1):
        z = plus(z, root(stride*k))
    return z


def literal_word(p, q):
    if not q:
        assert p == 1
        return 'N'
    return ''.join('E' + 'N'*((p*(a+1))//q - (p*a)//q) for a in range(q))


def word_transform(word):
    z = ZERO
    for position, letter in enumerate(word):
        if letter == 'E':
            z = plus(z, root(position))
    return z


def transform(p, q):
    return word_transform(literal_word(p, q))


def commutator(hu, hv, u, v):
    return minus(times(minus(ONE, root(sum(v))), hu),
                 times(minus(ONE, root(sum(u))), hv))


BALANCED = {(0, 1): ONE, (1, 1): ONE, (2, 0): (2, 1), (2, 2): (2, 0)}
GOOD = {
    ((0, 1), (1, 0), 'upper'),
    ((0, 2), (2, 0), 'upper'),
    ((1, 2), (0, 2), 'upper'),
    ((2, 0), (1, 1), 'upper'),
    ((2, 2), (0, 1), 'upper'),
}


def finite_states():
    initial = ((2, 2), (0, 1), 0)
    todo, seen = [initial], {initial}
    while todo:
        u, v, phase = todo.pop()
        m = tuple((a+b) % 3 for a, b in zip(u, v))
        for state in ((m, v, phase), (u, m, (phase + sum(u)) % 3)):
            if state not in seen:
                seen.add(state)
                todo.append(state)
    pairs = {(u, v) for u, v, _ in seen}
    all_pairs = {((p, q), (r, s)) for p in range(3) for q in range(3)
                 for r in range(3) for s in range(3) if (p*s-r*q) % 3 == 2}
    assert len(seen) == len(pairs) == 24 and pairs == all_pairs
    return sorted(seen)


def alpha_floor(n):
    # Both sides are exact integers; no logarithm rounding is used.
    a, power = 0, 1
    while power*3 <= 2**n:
        a, power = a+1, power*3
    return a


def beta_floor(n):
    return (3**n).bit_length() - 1


def quotient_rectangle(pr, qr, h, width=24):
    # Solve the endpoint identity directly in the ring, rather than divide it.
    conjugate = lambda z: (z[0]-z[1], -z[1])
    e_q = ZERO
    for a in range(1, qr+1):
        e_q = plus(e_q, root(-a))
    endpoint_term = plus(minus(h, ONE), root(pr+qr))
    rhs = minus(e_q, times(root(2), conjugate(endpoint_term)))
    endpoints = [(a, b) for a in range(-8, 9) for b in range(-8, 9)
                 if times(minus((a, b), ONE), minus(ONE, root(2))) == rhs]
    assert len(endpoints) == 1
    a_plus = [endpoints[0]]
    a_minus = [minus(endpoints[0], root(2*pr-qr))]
    b_axis = [ONE]
    for a in range(1, width):
        inc = times(root(-qr-a), roots_through(pr+alpha_floor(a), 2))
        a_plus.append(plus(a_plus[-1], inc))
        a_minus.append(plus(a_minus[-1], inc))
    for b in range(1, width):
        inc = times(root(-2*b), roots_through(beta_floor(b)))
        b_axis.append(plus(b_axis[-1], inc))

    def birth(axis, a, b):
        numerator = times(minus(ONE, root(-qr-a)), minus(ONE, root(-2*b)))
        assert numerator[0] % 3 == numerator[1] % 3 == 0
        rectangle = numerator[0]//3, numerator[1]//3
        x, y = minus(plus(plus(axis[a], b_axis[b]), rectangle), ONE)
        if b == 0:
            return 0
        if b == 1:
            return int(x >= 1 and y >= 0)
        if b == 2:
            return int(x <= -1 and x-y <= 0)
        if b == 3:
            return int(min(x, 0) <= y)
        isolate = beta_floor(b) - beta_floor(b-1) == 2
        patch = beta_floor(b-1) - beta_floor(b-3) == 4
        assert not (isolate and patch)
        correction = (root(beta_floor(b)-2*b) if isolate else
                      root(beta_floor(b-1)-1-2*b) if patch else ZERO)
        x, y = minus((x, y), correction)
        return int(x <= 0 and x-y <= 0)

    total = sum((Fraction(-3*(birth(a_plus, a, b)-birth(a_minus, a, b)),
                          2**a*3**b)
                 for a in range(width) for b in range(width)), Fraction(0))
    tail = Fraction(27, 2**(width+1)) + Fraction(45, 2*3**width)
    return total, tail


def original_token_quotient(p, q, width):
    # Retiming only raises the rational grade in the required slope interval.
    cap = p*(q+width-1) + q*(width-1)
    groups = {}
    for a in range(cap//p+1):
        for b in range((cap-p*a)//q+1):
            point = ((a-1, 1) if b == 0 and a >= 1 else
                     (a-3, 3) if b == 1 and a >= 2 else (a, b))
            grade = p*point[0] + q*point[1]
            if grade <= cap:
                groups.setdefault(point, [0, 0, 0])[(a-b) % 3] += 1
    births = []
    for orientation in (1, -1):
        counts, table = [0, 0, 0], {}
        points = sorted(groups, key=lambda z: (p*z[0]+q*z[1], orientation*z[0]))
        for point in points:
            before = min(counts)
            counts = [x+y for x, y in zip(counts, groups[point])]
            table[point] = min(counts)-before
        assert table[-1, 3] == 0
        births.append(table)
    return sum((Fraction(-3*(births[0].get((q+a, b), 0)
                              -births[1].get((q+a, b), 0)), 2**a*3**b)
                for a in range(width) for b in range(width)), Fraction(0))


def variation(p, q, r, s):
    assert abs(p*s-r*q) == 1
    a, b = q+s, p+r
    return 9*(Fraction(2, 2**a)*(1+Fraction(a+1, q*s))
              +Fraction(1, 3**b)*(Fraction(3, 2)
                +Fraction(6*b+3, 4*p*r)))


def check():
    # Literal word concatenation checks the convention independently.
    for u, v in [((0, 1), (1, 0)), ((5, 8), (12, 19)), ((41, 65), (12, 19)),
                 ((306, 485), (53, 84))]:
        m = u[0]+v[0], u[1]+v[1]
        assert literal_word(*m) == literal_word(*u)+literal_word(*v)
        c = commutator(transform(*u), transform(*v), u, v)
        assert c in {times(root(k), (1, -1)) for k in range(3)}
        assert commutator(transform(*u), transform(*m), u, m) == times(root(sum(u)), c)
        assert commutator(transform(*m), transform(*v), m, v) == c

    cases, same, resonant_same = [], set(), 0
    for u, v, phase in finite_states():
        med = tuple((a+b) % 3 for a, b in zip(u, v))
        if med not in BALANCED:
            continue
        hm = BALANCED[med]
        rho = root(sum(u))
        c = times(root(phase), (1, -1))
        solutions = []
        for a in range(-6, 7):
            for b in range(-6, 7):
                hu = a, b
                hv = times(root(-sum(u)), minus(hm, hu))
                if commutator(hu, hv, u, v) == c:
                    solutions.append((hu, hv))
        assert len(solutions) == 1
        hu, hv = solutions[0]
        mr, mt = quotient_rectangle(*med, hm)
        assert abs(mr) > mt
        for side, current in [('lower', u), ('upper', v)]:
            if sum(current) % 3 == 0:
                continue
            if side == 'lower':
                child = tuple((2*a+b) % 3 for a, b in zip(u, v))
                hc = plus(hu, times(rho, hm))
            else:
                child = tuple((a+2*b) % 3 for a, b in zip(u, v))
                hc = plus(hm, times(root(sum(med)), hv))
            response, tail = quotient_rectangle(*child, hc)
            assert abs(response)-tail > Fraction(1, 10000)
            cases.append((u, v, phase, side, med, hm, child, hc))
            if (response > 0) == (mr > 0):
                same.add((u, v, side))
                resonant_same += sum(child) % 3 == 0
    assert len(cases) == 16 and same == GOOD and resonant_same == 4
    print('FINITE_STATES 24; CHILD_CASES 16; SAME_SIGN 5; RESONANT_SAME_SIGN 4')

    # This enumeration starts from original tokens, not pre-retimed streams.
    assert transform(65, 103) == ONE
    assert original_token_quotient(65, 103, 24) == quotient_rectangle(2, 1, ONE)[0]
    print('RESONANT_65_103_FULL_24_RECTANGLE_PASS')

    for current, successor, ratio_floor in [((12, 19), (41, 65), 18318776),
                                           ((53, 84), (306, 485),
                                            18168129295004104279455783313574041127430456078)]:
        p, q = current
        pp, qq = successor
        med, child = (p+pp, q+qq), (2*p+pp, 2*q+qq)
        assert 2**q < 3**p and 2**qq > 3**pp
        assert 2**med[1] < 3**med[0] and 2**child[1] < 3**child[0]
        lower, upper = Fraction(0), Fraction(0)
        for r, s in (med, child):
            center, tail = quotient_rectangle(r % 3, s % 3, transform(r, s))
            factor = Fraction(1, 2**s)-Fraction(1, 3**r)
            ends = sorted((factor*(center-tail), factor*(center+tail)))
            lower, upper = lower+ends[0], upper+ends[1]
        remainder = (variation(*current, *child)+variation(*child, *med)
                     +variation(*med, *successor))
        assert lower > remainder or upper < -remainder
        ratio = min(abs(lower), abs(upper))/remainder
        assert ratio//1 == ratio_floor
        print('TWO_NODE', current, 'RATIO_FLOOR', ratio_floor)
    print('PASS: independent commutator, child responses and full two-node clusters')


if __name__ == '__main__':
    check()
