"""Standalone exact corrected-fan audit; prior finite-cover identities are inputs."""
from fractions import Fraction as F
from functools import cache


def add(z, w):
    return z[0]+w[0], z[1]+w[1]


def neg(z):
    return -z[0], -z[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c-b*d


def root(n):
    return ((1, 0), (0, 1), (-1, -1))[n % 3]


def divide(z, w):
    c, d = w
    z = mul(z, (c-d, -d))
    norm = c*c-c*d+d*d
    assert z[0] % norm == z[1] % norm == 0
    return z[0]//norm, z[1]//norm


@cache
def direct_floor(n):
    power, k = 1, 0
    while 3*power <= 2**n:
        power, k = 3*power, k+1
    return k


@cache
def reciprocal_floor(n):
    return (3**n).bit_length()-1


def board(t):
    counts, power, b = [0, 0, 0], 1, 0
    while power <= t:
        last = (t//power).bit_length()-1
        for color in range(3):
            counts[color] += max(0, (last-(color+b) % 3)//3+1)
        power, b = 3*power, b+1
    return counts


def axes(width):
    aa, bb = [], []
    for n in range(width):
        ka, kb = board(2**n), board(3**n)
        aa.append(mul(root(-n), (ka[0]-ka[2], ka[1]-ka[2])))
        bb.append(mul(root(n), (kb[0]-kb[2], kb[1]-kb[2])))
    return aa, bb


def minimum_cover(t):
    counts = board(t)
    a, power = 1, 2
    while power <= t:
        if 3*power > 2*t or (6*power <= t and 4*t < 27*power):
            counts[a % 3] -= 1
        a, power = a+1, 2*power
    return min(counts)


def birth(z, b):
    x, y = z
    if b == 0:
        return 0
    if b == 1:
        return 1+min(x-1, y, 0)-min(x, y+1, 0)
    if b == 2:
        return min(x+1, y+1, 0)-min(x, y+1, 0)
    if b == 3:
        return 1-min(x, y+1, 0)+min(x, y, 0)
    return min(x, y, 0)-min(x-1, y, 0)


def corner(a, b):
    z = mul(add((1, 0), neg(root(-a))), add((1, 0), neg(root(-2*b))))
    assert z[0] % 3 == z[1] % 3 == 0
    return z[0]//3, z[1]//3


def event(b, floor):
    if b < 4:
        return (0, 0)
    isolated = floor(b)-floor(b-1) == 2
    patch = floor(b-1)-floor(b-3) == 4
    assert not (isolated and patch)
    if isolated:
        return root(floor(b)-2*b)
    return root(floor(b-1)-1-2*b) if patch else (0, 0)


def coeff(a, b, aa, bb, floor=reciprocal_floor, shift=0, displacement=(0, 0)):
    z = add(add(aa[a], bb[b]), add(corner(a+shift, b), (-1, 0)))
    z = add(add(z, neg(event(b, floor))), neg(displacement))
    return 1-3*birth(z, b)


def weighted(na, nb, f):
    # Column-major integer Horner order differs from the supplied evaluator.
    total = 0
    for b in range(nb):
        column = 0
        for a in range(na):
            column = 2*column+f(a, b)
        total = 3*total+column
    return F(total, 2**(na-1)*3**(nb-1))


def transform(p, q):
    z = (0, 0)
    for a in range(q):
        z = add(z, root(a+p*a//q))
    return z


def response(state, width, bb):
    p, q, h = state
    w = add(add(h, (-1, 0)), root(p+q))
    conjugate = w[0]-w[1], -w[1]
    total = (0, 0)
    for j in range(q % 3):
        total = add(total, root(j-q))
    aa = [add((1, 0), divide(add(total, neg(mul(root(2), conjugate))), (2, 1)))]
    for a in range(1, width):
        step = (0, 0)
        for j in range((p+direct_floor(a)) % 3+1):
            step = add(step, root(-q-a+2*j))
        aa.append(add(aa[-1], step))
    gamma = root(2*p-q)
    return weighted(width, width,
                    lambda a, b: coeff(a, b, aa, bb, shift=q)
                    -coeff(a, b, aa, bb, shift=q, displacement=gamma))


BALANCED = {(0, 1): (1, 0), (1, 1): (1, 0),
            (2, 0): (2, 1), (2, 2): (2, 0)}


def parent_classes():
    start = ((2, 2), (0, 1), 0)
    seen, pending = {start}, [start]
    while pending:
        u, v, k = pending.pop()
        med = tuple((a+b) % 3 for a, b in zip(u, v))
        for nxt in ((med, v, k), (u, med, (k+sum(u)) % 3)):
            if nxt not in seen:
                seen.add(nxt)
                pending.append(nxt)
    assert len(seen) == 24
    result = []
    for u, v, k in sorted(seen):
        med = tuple((a+b) % 3 for a, b in zip(u, v))
        if med not in BALANCED:
            continue
        x, y = root(sum(u)), root(sum(v))
        hv = divide(add(mul(add((1, 0), neg(y)), BALANCED[med]),
                        neg(mul(root(k), (1, -1)))), add((1, 0), neg(mul(x, y))))
        hu = add(BALANCED[med], neg(mul(x, hv)))
        for side in (0, 1):
            if sum((u, v)[side]) % 3:
                result.append((u, v, side, hu, hv))
    assert len(result) == 16
    return result


def successor_state(row):
    u, v, side, hu, hv = row
    x, y = root(sum(u)), root(sum(v))
    if side == 0:
        pq = tuple((a+2*b) % 3 for a, b in zip(u, v))
        h = add(hu, mul(x, mul(add((1, 0), y), hv)))
    else:
        pq = tuple((2*a+b) % 3 for a, b in zip(u, v))
        h = add(mul(add((1, 0), x), hu), mul(mul(x, x), hv))
    return *pq, h


def variation(p, q, r, s):
    assert abs(p*s-r*q) == 1
    a, b = q+s, p+r
    return 9*(F(2, 2**a)*(1+F(a+1, q*s))
              +F(1, 3**b)*(F(3, 2)+F(6*b+3, 4*p*r)))


def remainder(p, q, pp, qq):
    r, s, w, t = p+pp, q+qq, p+2*pp, q+2*qq
    result = variation(r, s, w, t)+variation(w, t, pp, qq)
    result += 72*F(1, 2**(3*q+2*qq))/(1-F(1, 2**(2*q)))
    result += F(189, 4)*F(1, 3**(3*p+2*pp))/(1-F(1, 3**(2*p)))
    epsilon = F(45, 2*2**s)+F(63, 2*3**r)
    mass = F(1, 2**s)/(1-F(1, 2**q))+F(1, 3**r)/(1-F(1, 3**p))
    return result+epsilon*mass


def logarithm_interval(x):
    z = F(x-1, x+1)
    lo = 2*sum((z**(2*k+1)/F(2*k+1) for k in range(120)), F(0))
    tail = 2*z**241/(241*(1-z*z))
    return lo, lo+tail


def actual_prefix():
    a, b = logarithm_interval(2), logarithm_interval(3)
    lo, hi = a[0]/b[1], a[1]/b[0]
    digits, convergents = [], []
    pm, p, qm, q = 0, 1, 1, 0
    for _ in range(20):
        digit = lo.numerator//lo.denominator
        assert digit == hi.numerator//hi.denominator
        pm, p, qm, q = p, digit*p+pm, q, digit*q+qm
        digits.append(digit)
        convergents.append((p, q))
        lo, hi = 1/(hi-digit), 1/(lo-digit)
    return digits, convergents


def model(p, q, side):
    def floor(n, x, y, sign):
        return n*x//y-int(n > 0 and n*x % y == 0 and sign < 0)
    aa, bb = [(1, 0)], [(1, 0)]
    for a in range(1, 3*q):
        step = (0, 0)
        for j in range(floor(a, p, q, side) % 3+1):
            step = add(step, root(-a+2*j))
        aa.append(add(aa[-1], step))
    for b in range(1, 3*p+4):
        step = (0, 0)
        for j in range(floor(b, q, p, -side) % 3+1):
            step = add(step, root(-2*b+j))
        bb.append(add(bb[-1], step))
    beta = lambda n: floor(n, q, p, -side)
    horizontal = 1-F(1, 2**(3*q))
    head = weighted(3*q, 4, lambda a, b: coeff(a, b, aa, bb, floor=beta))/horizontal
    tile = weighted(3*q, 3*p, lambda a, b: coeff(a, b+4, aa, bb, floor=beta))
    return head+tile/(81*horizontal*(1-F(1, 3**(3*p))))-1


def check():
    digits, convergents = actual_prefix()
    states = {successor_state(row) for row in parent_classes()}
    assert len(states) == 10
    micro = {(0, 1, (1, 0)): 482747, (0, 2, (0, -1)): -56,
             (0, 2, (3, 2)): -1120067, (1, 0, (0, 0)): -169,
             (1, 0, (3, 0)): 425183, (1, 1, (1, 0)): -58734,
             (1, 2, (1, 1)): 777374, (2, 0, (2, 1)): -1071732,
             (2, 1, (1, 0)): -547828, (2, 2, (2, 0)): 1456689}
    assert states == set(micro)
    aa, bb = axes(260)
    for a, b in ((0, 1), (0, 4), (0, 9), (0, 28), (3, 9), (8, 12)):
        t = 2**a*3**b
        actual = coeff(a, b, aa, bb)-3*int((a, b) == (0, 1))
        assert actual == 1-3*(minimum_cover(t)-minimum_cover(t-1))
    values = {state: response(state, 48, bb) for state in states}
    tail = F(27, 2*2**48)+F(45, 2*3**48)
    for state, lo in micro.items():
        assert F(lo, 10**6) < values[state]-tail
        assert values[state]+tail < F(lo+1, 10**6)
        assert abs(values[state])-tail > F(1, 20000)
    for p, q, pp, qq in ((53, 84, 306, 485), (306, 485, 665, 1054)):
        index = convergents.index((p, q))
        assert convergents[index+1] == (pp, qq) and digits[index+2] >= 2
        assert (p+pp) % 3 or (q+qq) % 3
        med = ((p+pp) % 3, (q+qq) % 3)
        assert transform(p+pp, q+qq) == BALANCED[med]
        w, t = p+2*pp, q+2*qq
        state = w % 3, t % 3, transform(w, t)
        assert all(w*k//t == direct_floor(k) for k in range(1, 48))
        assert all(t*k//w == reciprocal_floor(k) for k in range(1, 48))
        sigma = 1 if 2**q > 3**p else -1
        assert (2**t > 3**w) == (sigma > 0)
        delta = F(1, 2**t)-F(1, 3**w)
        lead = abs(delta)*(abs(values[state])-tail)
        rest = remainder(p, q, pp, qq)
        assert rest < 1400*F(1, 2**(2*q+2*qq)) and lead > rest
        assert sigma*delta*values[state] > 0
        if q == 485:
            assert lead/rest > 2**400
        print('CORRECTED_CERTIFICATE', (p, q), 'child', (w, t), 'ratio_gt', lead//rest)
    p, q, pp, qq = 12, 19, 41, 65
    index = convergents.index((p, q))
    assert convergents[index+1] == (pp, qq) and digits[index+2] == 1
    assert 2**q < 3**p and 2**(q+2*qq) > 3**(p+2*pp)
    fan_states = [(p*j+pp, q*j+qq) for j in (1, 2, 3)]
    fan_states = [(r % 3, s % 3, transform(r, s)) for r, s in fan_states]
    gamma = [response(state, 192, bb) for state in fan_states]
    cs = [F(1, 2**(qq+j*q))/(1-F(1, 2**(3*q)))
          -F(1, 3**(pp+j*p))/(1-F(1, 3**(3*p))) for j in (1, 2, 3)]
    actual = weighted(260, 180, lambda a, b: coeff(a, b, aa, bb)-3*int((a, b) == (0, 1)))
    target_tail = 6*(F(1, 2**260)+F(1, 3**180)-F(1, 2**260*3**180))
    response_tail = 9*(F(1, 2**192)+F(1, 3**192))
    centre = actual-model(p, q, -1)+sum(c*g for c, g in zip(cs, gamma))
    uncertainty = target_tail+response_tail*sum(map(abs, cs))
    lo, hi = centre-uncertainty, centre+uncertainty
    assert -F(1, 2**175) < lo < hi < -F(1, 2**176)
    w, t = p+2*pp, q+2*qq
    state = w % 3, t % 3, transform(w, t)
    wrong_lead = abs(F(1, 2**t)-F(1, 3**w))*(abs(values[state])-tail)
    assert wrong_lead > remainder(p, q, pp, qq)
    assert -(F(1, 2**t)-F(1, 3**w))*values[state] > 0
    print('DIGIT_ONE: -2^(-175)<R_fan<-2^(-176); un-crossed retained jump gives wrong sign and estimate')
    print('PASS: independent original-board responses,16 classes,10 states,actual CF and complete residual certificates')


if __name__ == '__main__':
    check()
