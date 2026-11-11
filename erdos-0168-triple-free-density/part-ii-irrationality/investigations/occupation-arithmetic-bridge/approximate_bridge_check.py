"""Exact phase-guard approximants; no occupation arithmetic bridge is claimed."""
from fractions import Fraction as F


def log_interval(x, terms=90):
    value = 2 * sum((x ** (2*k+1) / (2*k+1) for k in range(terms)), F(0))
    tail = 2*x**(2*terms+1)/((2*terms+1)*(1-x*x))
    return value, value+tail


def actual_cf(count=12):
    l2, u2 = log_interval(F(1, 3))
    l3, u3 = log_interval(F(1, 2))
    lo, hi = l2/u3, u2/l3
    pm, p, qm, q, out = 0, 1, 1, 0, []
    for _ in range(count):
        digit = lo.numerator//lo.denominator
        assert digit == hi.numerator//hi.denominator
        pn, qn = digit*p+pm, digit*q+qm
        out.append((pn, qn))
        pm, p, qm, q = p, pn, q, qn
        lo, hi = 1/(hi-digit), 1/(lo-digit)
    return out


def floors(maximum):
    out, p2, p3, value = [0], 1, 1, 0
    for _ in range(maximum):
        p2 *= 2
        while 3*p3 <= p2:
            p3 *= 3
            value += 1
        out.append(value)
    return out


def rational_floor(k, p, q, side):
    assert k > 0
    value, remainder = divmod(k*p, q)
    return value-int(side < 0 and remainder == 0)


def code(n, fl):
    return tuple(fl[3*n+s] % 3 for s in (1, 2, 3))


def rational_code(n, p, q, side):
    return tuple(rational_floor(3*n+s, p, q, side) % 3 for s in (1, 2, 3))


def prefix_value(bits):
    numerator = 0
    for bit in bits:
        numerator = 8*numerator+bit
    return F(numerator, 8**(len(bits)-1))


def periodic_value(bits):
    numerator = 0
    for bit in bits:
        numerator = 8*numerator+bit
    return F(8*numerator, 8**len(bits)-1)


def board_axis(a):
    cutoff, p3, b = 2**a, 1, 0
    count = [0, 0, 0]
    while p3 <= cutoff:
        value, j = p3, 0
        while value <= cutoff:
            count[(j-b) % 3] += 1
            value *= 2
            j += 1
        p3 *= 3
        b += 1
    z = count[0]-count[2], count[1]-count[2]
    for _ in range((-a) % 3):
        z = -z[1], z[0]-z[1]
    return z


def check():
    cf = actual_cf()
    cases = ((12, 19, 41, 65, 1), (53, 84, 306, 485, 0),
             (665, 1054, 15601, 24727, 0))
    for p, q, pp, qq, residue in cases:
        i = cf.index((p, q))
        assert cf[i+1] == (pp, qq)
        assert qq >= 2*q+cf[i-1][1]
        side = 1 if 2**q > 3**p else -1
        match = (q+qq-1-3)//3+1
        width = 2*match+100
        fl = floors(3*max(width, 300)+3)
        period = [rational_code(n, p, q, side) for n in range(q)]
        for n in range(match):
            assert code(n, fl) == period[n % q]
        for n in range(q):
            assert rational_code(n+q, p, q, side) == period[n]
        labels = {code(n, fl) for n in range(300)}
        assert len(labels) == 9
        denominator = 8**q-1
        generic = F(8, 7)*2**3*F(2**(2*q), 2**qq)
        assert generic < 1
        for label in labels:
            model = periodic_value([int(v == label) for v in period])
            assert denominator % model.denominator == 0
            head = prefix_value([int(code(n, fl) == label) for n in range(width)])
            tail = F(8, 7*8**width)
            error = max(abs(head-model), abs(head+tail-model))
            assert denominator*error <= generic
        model = periodic_value([int(v[0] == residue) for v in period])
        head = prefix_value([int(fl[3*n+1] % 3 == residue) for n in range(width)])
        tail = F(8, 7*8**width)
        assert (head-model)*(head+tail-model) > 0
        assert denominator*max(abs(head-model), abs(head+tail-model)) < 1
        print('GUARD_RETURN', (p, q), 'resonant_current', (p+q) % 3 == 0,
              'period', q, 'matched', match, 'cleared_error_bound_below_one')

    # The actual state and phase guard are correlated, so pure guard masses do
    # not replace the guarded state readouts in physical transport.
    width = 28
    fl = floors(3*width+3)
    guard = [int(fl[3*n+1] % 3 == 0) for n in range(width)]
    axes = [board_axis(3*n) for n in range(width)]
    reads = ([int(z == (1, 0)) for z in axes],
             [int(z[0]-1 <= 0 and z[0]-1-z[1] <= 0) for z in axes])
    for state in reads:
        joint = prefix_value([g*h for g, h in zip(guard, state)])
        mg, mh = prefix_value(guard), prefix_value(state)
        tail, mass = F(8, 7*8**width), F(8, 7)
        lower = joint-(mg+tail)*(mh+tail)/mass
        upper = joint+tail-mg*mh/mass
        assert F(1, 10) < lower <= upper < F(1, 6)
    print('ACTUAL_GUARD_STATE_AND_CONE_CORRELATIONS', 'both strictly between1/10 and1/6')
    print('PASS: simultaneous Boolean guard errors, nonzero arithmetic guard returns, exact actual correlation')


if __name__ == '__main__':
    check()
