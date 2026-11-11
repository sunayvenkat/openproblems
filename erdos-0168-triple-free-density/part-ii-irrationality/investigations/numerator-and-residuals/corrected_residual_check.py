"""Exact state and complete-tail certificates for corrected fan residuals."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util


def load(name, folder, file):
    path = Path(__file__).resolve().parents[1] / folder / file
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


fan = load('residual_fan', 'Erdos 168 correlated return arithmetic', 'farey_fan_check.py')
gs, ss, cf = fan.gs, fan.ss, fan.cf


def successor_child_state(row, width=48):
    lower, upper, phase, side, med, hm = row[:6]
    x, y = gs.omega(sum(lower)), gs.omega(sum(upper))
    c = gs.mul(gs.omega(phase), (1, -1))
    hv = gs.divide(gs.sub(gs.mul(gs.sub((1, 0), y), hm), c),
                   gs.sub((1, 0), gs.mul(x, y)))
    hu = gs.sub(hm, gs.mul(x, hv))
    if side == 'lower':
        residue = tuple((a+2*b) % 3 for a, b in zip(lower, upper))
        hw = gs.add(hu, gs.mul(x, gs.mul(gs.add((1, 0), y), hv)))
    else:
        residue = tuple((2*a+b) % 3 for a, b in zip(lower, upper))
        hw = gs.add(gs.mul(gs.add((1, 0), x), hu),
                    gs.mul(gs.mul(x, x), hv))
    endpoint, value, tail = ss.limiting_response(*residue, hw, width)
    return (*residue, hw), (*residue, endpoint), value, tail


def corrected_bound(p, q, pp, qq):
    r, s = p+pp, q+qq
    wp, wq = p+2*pp, q+2*qq
    gaps = (72*F(1, 2**(3*q+2*qq))/(1-F(1, 2**(2*q)))
            +F(189, 4)*F(1, 3**(3*p+2*pp))/(1-F(1, 3**(2*p))))
    epsilon = F(45, 2*2**s)+F(63, 2*3**r)
    gap_mass = (F(1, 2**(qq+q))/(1-F(1, 2**q))
                +F(1, 3**(pp+p))/(1-F(1, 3**p)))
    return (ss.farey_variation(r, s, wp, wq)
            +ss.farey_variation(wp, wq, pp, qq)+gaps+epsilon*gap_mass)


def check():
    rows = [row for row in gs.compatible_children()
            if (row[0], row[1], row[2]) in gs.reachable_phases()]
    assert len(rows) == 16
    unique = {}
    for row in rows:
        state, endpoint, value, tail = successor_child_state(row)
        assert abs(value)-tail > F(1, 20000)
        unique[state] = (endpoint, value, tail)
    for state, (endpoint, value, tail) in sorted(unique.items()):
        lo = (10**6*(value-tail)).__floor__()
        assert value+tail < F(lo+1, 10**6)
        print('SUCCESSOR_CHILD_RESPONSE', state, endpoint, F(lo, 10**6), F(lo+1, 10**6))
    print('COMPATIBLE_CLASSES', len(rows), 'UNIQUE_CHILD_STATES', len(unique))
    assert len(unique) == 10
    aa, bb = fan.rr.axes(48)
    for _, (endpoint, value, _) in unique.items():
        assert fan.response_partial(endpoint, 48, aa, bb) == value
    for current, successor in [((53, 84), (306, 485)), ((306, 485), (665, 1054))]:
        p, q = current
        pp, qq = successor
        sigma = 1 if 2**q > 3**p else -1
        wp, wq = p+2*pp, q+2*qq
        assert abs(p*qq-pp*q) == 1
        assert (1 if 2**wq > 3**wp else -1) == sigma
        hw = cf.christoffel_transform(wp, wq)
        _, value, tail = ss.limiting_response(wp % 3, wq % 3, hw, 48)
        delta = F(1, 2**wq)-F(1, 3**wp)
        lower = abs(delta)*(abs(value)-tail)
        rest = corrected_bound(p, q, pp, qq)
        assert rest < 1400*F(1, 2**(2*q+2*qq))
        assert lower > rest
        if current == (306, 485):
            assert lower > rest*2**400
        sign = sigma*(1 if delta > 0 else -1)*(1 if value > 0 else -1)
        print('ACTUAL_CORRECTED_NONZERO', current, successor, 'child', (wp, wq),
              'state', (wp % 3, wq % 3, hw), 'leading_over_remainder_gt', lower//rest,
              'sign', sign)
    # The digit-one example certifies a true residual directly, without
    # pretending the un-crossed successor child belongs to the jump sum.
    p, q, pp, qq = 12, 19, 41, 65
    wp, wq = p+2*pp, q+2*qq
    assert 2**q < 3**p and 2**wq > 3**wp
    width = 192
    aa, bb = fan.rr.axes(width)
    states = [fan.fan_state((p, q), (pp, qq), j)[1] for j in (1, 2, 3)]
    values = [fan.response_partial(state, width, aa, bb) for state in states]
    tail = 9*(F(1, 2**width)+F(1, 3**width))
    coefficients = [F(1, 2**(qq+j*q))/(1-F(1, 2**(3*q)))
                    -F(1, 3**(pp+j*p))/(1-F(1, 3**(3*p))) for j in (1, 2, 3)]
    correction = sum((c*v for c, v in zip(coefficients, values)), F(0))
    uncertainty = sum(map(abs, coefficients))*tail
    z = fan.models.model(p, q, -1)[4]
    lo, hi = ss.actual_enclosure(260, 180)
    lo, hi = lo-z+correction-uncertainty, hi-z+correction+uncertainty
    assert lo > 0 or hi < 0
    absolute_lo, absolute_hi = (lo, hi) if lo > 0 else (-hi, -lo)
    k = 0
    while absolute_hi < F(1, 2**(k+1)):
        k += 1
    assert F(1, 2**(k+1)) < absolute_lo < absolute_hi < F(1, 2**k)
    print('DIGIT_ONE_DIRECT_ENCLOSURE', 'sign', 1 if lo > 0 else -1,
          'absolute_between', '2^(-%s)' % (k+1), '2^(-%s)' % k)
    wh = cf.christoffel_transform(wp, wq)
    _, wvalue, wtail = ss.limiting_response(wp % 3, wq % 3, wh, 48)
    wdelta = F(1, 2**wq)-F(1, 3**wp)
    wrong_leading = abs(wdelta)*(abs(wvalue)-wtail)
    assert wrong_leading > corrected_bound(p, q, pp, qq)
    assert -wdelta*wvalue > 0 and hi < 0
    print('DIGIT_ONE_UNCROSSED_JUMP_HAS_OPPOSITE_SIGN_AND_DOMINATES_FALSE_BOUND')
    print('PASS: all successor-child responses nonzero; complete corrected-fan criteria')


if __name__ == '__main__':
    check()
