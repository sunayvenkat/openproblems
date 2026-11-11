"""Exact checks for the complete current-side Farey fan; no infinite supply claim."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd, lcm
import importlib.util


def load(name, folder, file):
    path = Path(__file__).resolve().parents[1] / folder / file
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ss = load('fan_scalar', 'Erdos 168 signed arithmetic returns', 'signed_scalar_check.py')
gs = load('fan_states', 'Erdos 168 response closure tests', 'general_states_check.py')
rr = load('fan_actual', 'Erdos 168 response closure tests', 'response_relations_check.py')
models = load('fan_models', 'Erdos 168 reflected return models', 'two_sided_models_check.py')
cf = gs.cf


def fan_state(current, successor, k):
    p, q = current
    pp, qq = successor
    r, s = k*p+pp, k*q+qq
    h = cf.christoffel_transform(r, s)
    endpoint = ss.limiting_response(r % 3, s % 3, h, 1)[0]
    return (r % 3, s % 3, h), (r % 3, s % 3, endpoint)


def off_fan_bound(p, q, pp, qq):
    r, s = p+pp, q+qq
    return (ss.farey_variation(r, s, pp, qq)
            + 72*F(1, 2**(3*q+2*qq))/(1-F(1, 2**(2*q)))
            + F(189, 4)*F(1, 3**(3*p+2*pp))/(1-F(1, 3**(2*p))))


def response_partial(state, width, aa, bb):
    total = 0
    for b in reversed(range(width)):
        row = 0
        for a in reversed(range(width)):
            row = row+rr.response(state, a, b, aa, bb)[0]*2**(width-1-a)
        total += row*3**(width-1-b)
    return F(total, 2**(width-1)*3**(width-1))


def states_from_class(row):
    lower, upper, phase, side, med, hm = row[:6]
    x, y = gs.omega(sum(lower)), gs.omega(sum(upper))
    c = gs.mul(gs.omega(phase), (1, -1))
    hv = gs.divide(gs.sub(gs.mul(gs.sub((1, 0), y), hm), c),
                   gs.sub((1, 0), gs.mul(x, y)))
    hu = gs.sub(hm, gs.mul(x, hv))
    result = []
    for k in range(1, 7):
        if side == 'lower':
            residue = tuple((k*a+b) % 3 for a, b in zip(lower, upper))
            hk = gs.add(gs.mul(cf.geometric(k, sum(lower)), hu),
                        gs.mul(gs.omega(k*sum(lower)), hv))
        else:
            residue = tuple((a+k*b) % 3 for a, b in zip(lower, upper))
            hk = gs.add(hu, gs.mul(x, gs.mul(cf.geometric(k, sum(upper)), hv)))
        endpoint = ss.limiting_response(*residue, hk, 1)[0]
        result.append((*residue, endpoint))
    assert result[:3] == result[3:]
    return result[:3]


def check():
    examples = [((12, 19), (41, 65)), ((53, 84), (306, 485)),
                ((306, 485), (665, 1054))]
    for current, successor in examples:
        for k in range(1, 10):
            assert fan_state(current, successor, k) == fan_state(current, successor, k+3)
        p, q = current
        pp, qq = successor
        r, s = p+pp, q+qq
        for k in range(1, 7):
            rk, sk = k*p+pp, k*q+qq
            for a in range(1, s):
                assert a*rk//sk == ss.floor_alpha(a)
            for b in range(1, r):
                assert b*sk//rk == ss.floor_beta(b)
        print('PERIOD3_AND_COMMON_FLOORS', current, successor)

    aa, bb = rr.axes(96)
    p, q, pp, qq = 12, 19, 41, 65
    x, y, u, v = F(1, 2**q), F(1, 3**p), F(1, 2**qq), F(1, 3**pp)
    coefficients = [u*x**j/(1-x**3)-v*y**j/(1-y**3) for j in (1, 2, 3)]
    states = [fan_state((p, q), (pp, qq), j)[1] for j in (1, 2, 3)]
    partials = [response_partial(state, 96, aa, bb) for state in states]
    tail = 9*(F(1, 2**96)+F(1, 3**96))
    for j in (1, 2, 3, 4):
        rj, sj = j*p+pp, j*q+qq
        transform = cf.christoffel_transform(rj, sj)
        direct = gs.direct_grade_response(rj, sj, 8)
        assert direct == ss.limiting_response(rj % 3, sj % 3, transform, 8)[1]
    fan_series = sum((coefficients[j-1]*partials[j-1] for j in (1, 2, 3)), F(0))
    finite = sum(((u*x**k-v*y**k)*partials[(k-1) % 3] for k in range(1, 31)), F(0))
    assert abs(fan_series-finite) <= 9*(u*x**31/(1-x)+v*y**31/(1-y))
    r, s = p+pp, q+qq
    epsilon = F(45, 2*2**s)+F(63, 2*3**r)
    gap_sum_bound = u*x/(1-x)+v*y/(1-y)
    remainder = off_fan_bound(p, q, pp, qq)+epsilon*gap_sum_bound
    assert remainder < 300*F(1, 2**(q+2*qq))
    old = ss.farey_variation(p, q, r, s)+ss.farey_variation(r, s, pp, qq)
    assert remainder*2**40 < old
    z = models.model(p, q, -1)[4]
    lo, hi = ss.actual_enclosure()
    predicted = z-fan_series
    uncertainty = tail*sum(map(abs, coefficients))+remainder
    assert lo >= predicted-uncertainty and hi <= predicted+uncertainty
    improvement = 0
    while remainder*2**(improvement+1) < old:
        improvement += 1
    print('FULL_FAN_ENCLOSURE_PASS', 'bound_improvement_bits', improvement)
    d = 27*(2**(3*q)-1)*(3**(3*p)-1)
    clearing = lcm(d, *(c.denominator for c in coefficients))
    assert all((clearing*c).denominator == 1 for c in coefficients)
    assert clearing*remainder > 1
    determinant_cells = [(a, b) for a in range(20) for b in range(4, 40)]
    actual = {cell: rr.original_c(*cell) for cell in determinant_cells}
    rows = [(cell, [1, actual[cell]]+[rr.response(state, *cell, aa, bb)[0] for state in states])
            for cell in determinant_cells]
    selected = rr.basis_rows(rows)
    print('ACTUAL_THREE_FAN_CONSTANTS_POINTWISE_RANK', len(selected), 'of5')
    print('FIVE_ROW_WITNESS', selected, 'determinant', rr.determinant([r for _, r in selected]))
    print('FAN_STATES', states)
    classes = [row for row in gs.compatible_children() if (row[0], row[1], row[2]) in gs.reachable_phases()]
    assert len(classes) == 16
    response_cache = {state: value for state, value in zip(states, partials)}
    cycle_sums = {}
    for row in classes:
        triple = states_from_class(row)
        rows = [(cell, [1, actual[cell]]+[rr.response(state, *cell, aa, bb)[0] for state in triple])
                for cell in determinant_cells]
        selected = rr.basis_rows(rows)
        assert len(selected) == 5
        print('FAN_CLASS_RANK', row[:4], triple, len(selected),
              'G_SUM_CELL_WITNESS', next(((a, b, sum(rr.response(st, a, b, aa, bb)[0] for st in triple))
                                         for a, b in determinant_cells
                                         if sum(rr.response(st, a, b, aa, bb)[0] for st in triple)), None))
        for state in triple:
            if state not in response_cache:
                response_cache[state] = response_partial(state, 96, aa, bb)
        cycle_sums[tuple(sorted(triple))] = sum((response_cache[st] for st in triple), F(0))
    assert len(response_cache) == 8 and len(cycle_sums) == 5
    for state, value in sorted(response_cache.items()):
        assert abs(value) > tail
        low = (10**6*(value-tail)).__floor__()
        assert value+tail < F(low+1, 10**6)
        print('COMPLETE_RESPONSE_BOUND', state, F(low, 10**6), F(low+1, 10**6))
    for triple, value in sorted(cycle_sums.items()):
        assert abs(value) > 3*tail
        low = (1000*(value-3*tail)).__floor__()
        assert value+3*tail < F(low+1, 1000)
        print('COMPLETE_WEIGHTED_CYCLE_SUM', triple, F(low, 1000), F(low+1, 1000))
    print('SEPARATE_COEFFICIENT_CLEARING_BITS', clearing.bit_length(), 'cleared_remainder_gt1', clearing*remainder > 1)
    a, b, c, e = 2**q, 3**p, 2**qq, 3**pp
    n3 = e*(b**3-1)-c*(a**3-1)
    raw = c*e*(a**3-1)*(b**3-1)
    assert coefficients[2] == F(n3, raw)
    g = gcd(a**3-1, b**3-1)
    off_s = lambda n: remove(n, 2, 3)
    assert gcd(abs(n3), off_s(raw)) <= g*g
    assert remove(coefficients[2].denominator, 3) % c == 0
    assert remove(coefficients[2].denominator, 2) % e == 0
    print('PASS: fan periods, common floors, resonant grade, geometric resummation, full target and coefficient arithmetic')


def remove(n, *primes):
    for prime in primes:
        while n % prime == 0:
            n //= prime
    return n


if __name__ == '__main__':
    check()
