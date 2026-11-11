"""Exact digit threshold, parent cylinders, and resonant mediant responses."""
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load(name, folder, filename):
    path = Path(__file__).resolve().parents[1] / folder / filename
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gs = load('state_graph', 'Erdos 168 response closure tests', 'general_states_check.py')
cf, ss = gs.cf, gs.ss
ONE = (1, 0)
add, sub, mul, omega, divide = gs.add, gs.sub, gs.mul, gs.omega, gs.divide


def resonant_states():
    result = {}
    for u, v, phase in sorted(gs.reachable_phases()):
        med = ((u[0] + v[0]) % 3, (u[1] + v[1]) % 3)
        if sum(med) % 3:
            continue
        x, y = omega(sum(u)), omega(sum(v))
        assert x != ONE and y != ONE and mul(x, y) == ONE
        commutator = mul(omega(phase), (1, -1))
        hm = divide(mul((-1, 0), mul(x, commutator)), sub(ONE, x))
        assert hm is not None
        endpoint, value, tail = ss.limiting_response(*med, hm, 32)
        result[u, v, phase] = med, hm, endpoint, value, tail
    return result


def balanced_parent_cylinders():
    result = []
    for u, v, phase in sorted(gs.reachable_phases()):
        med = ((u[0] + v[0]) % 3, (u[1] + v[1]) % 3)
        if med not in cf.BALANCED_H:
            continue
        hm = cf.BALANCED_H[med]
        x, y = omega(sum(u)), omega(sum(v))
        c = mul(omega(phase), (1, -1))
        hv = divide(sub(mul(sub(ONE, y), hm), c), sub(ONE, mul(x, y)))
        assert hv is not None
        hu = sub(hm, mul(x, hv))
        for side, current in [('lower', u), ('upper', v)]:
            if sum(current) % 3:
                result.append((u, v, phase, hu, hv, side))
    return result


def displaced_response(pr, qr, width):
    """Use original axes and periodic state shifts, retaining every low row."""
    aa, bb = [ONE], [ONE]
    st = ((1, 0), (0, -1), (0, 0))
    for a in range(1, width):
        aa.append(add(aa[-1], mul(omega(-a), st[ss.floor_alpha(a) % 3])))
    for b in range(1, width):
        bb.append(add(bb[-1], mul(omega(-2 * b), ss.rootsum(ss.floor_beta(b) + 1))))
    correction = (((0, 0), (0, 0), (0, 0)),
                  ((0, 0), (1, 0), (1, 1)),
                  ((0, 0), (0, -1), (1, 0)))
    offsets = ((0, 0), (1, 0), (0, -1)) if (pr, qr) == (1, 2) else ((0, 0), (1, 1), (1, 0))

    def phi(z, b):
        x, y = z
        if b == 0:
            return 0
        if b == 1:
            return int(x >= 1 and y >= 0)
        if b == 2:
            return int(x <= -1 and x - y <= 0)
        if b == 3:
            return int(min(x, 0) <= y)
        return int(x <= 0 and x - y <= 0)

    total = F(0)
    for b in range(width):
        event = (0, 0)
        if b >= 4:
            isolated = ss.floor_beta(b) - ss.floor_beta(b - 1) == 2
            patch = ss.floor_beta(b - 1) - ss.floor_beta(b - 3) == 4
            assert not (isolated and patch)
            if isolated:
                event = omega(ss.floor_beta(b) - 2 * b)
            if patch:
                event = omega(ss.floor_beta(b - 1) - 1 - 2 * b)
        for a in range(width):
            state = sub(add(add(aa[a], bb[b]), correction[a % 3][b % 3]), add(ONE, event))
            plus = add(state, offsets[(a - b) % 3])
            total += F(-3 * (phi(plus, b) - phi(sub(plus, ONE), b)), 2 ** a * 3 ** b)
    return total


def check():
    # The exact implication is uniform over the earlier denominator.
    for q in range(2, 70):
        for old in range(1, q):
            for digit in range(1, 12):
                Q = digit * q + old
                assert ((Q - 5 * q) > 0) == (digit >= 5)
                if digit >= 5:
                    assert Q - 5 * q >= old
    cylinders = balanced_parent_cylinders()
    assert len(cylinders) == 16
    print('BALANCED_PARENT_CYLINDERS', len(cylinders))
    for row in cylinders:
        print('BALANCED', row)
    states = resonant_states()
    unique = {(value[0], value[1]) for value in states.values()}
    assert len(states) == 6
    assert unique == {((1, 2), (1, 1)), ((2, 1), (1, 0))}
    print('RESONANT_PARENT_CYLINDERS', len(states), 'RESPONSE_STATES', len(unique))
    for row in sorted(states):
        print('RESONANT_PARENT', row)
    for med, hm in sorted(unique):
        endpoint, value, tail = ss.limiting_response(*med, hm, 32)
        assert endpoint == ONE
        assert value == displaced_response(*med, 32)
        lower, upper = (F(77, 100), F(79, 100)) if med == (1, 2) else (-F(11, 20), -F(27, 50))
        assert lower < value - tail < value + tail < upper
        print('RESONANT', med, hm, 'ENDPOINT', endpoint,
              'BOUND', (value - tail, value + tail),
              'LOWER_ABS_GT_1e4', abs(value) - tail > F(1, 10000))
    # A direct Christoffel sum verifies the resonant endpoint independently.
    for p, q, P, Q in [(41, 65, 53, 84), (665, 1054, 15601, 24727)]:
        lower, upper = sorted([(p, q), (P, Q)], key=lambda z: F(*z))
        hu, hv = cf.christoffel_transform(*lower), cf.christoffel_transform(*upper)
        c = gs.commutator(hu, hv, lower, upper)
        phase = next(k for k in range(3) if mul(omega(k), (1, -1)) == c)
        key = ((lower[0] % 3, lower[1] % 3),
               (upper[0] % 3, upper[1] % 3), phase)
        r, s = p + P, q + Q
        if (r + s) % 3:
            continue
        expected = states[key][1]
        counts = [0, 0, 0]
        for a in range(s):
            counts[(a + r * a // s) % 3] += 1
        actual = counts[0] - counts[2], counts[1] - counts[2]
        assert actual == expected == cf.christoffel_transform(r, s)
        _, value, tail = ss.limiting_response(r % 3, s % 3, actual, 32)
        gap = abs(F(1, 2 ** s) - F(1, 3 ** r))
        remainder = ss.farey_variation(p, q, r, s) + ss.farey_variation(r, s, P, Q)
        print('ACTUAL_RESONANT_MEDIANT', (p, q), (P, Q), (r, s), actual,
              'DOMINANCE', gap * (abs(value) - tail) > remainder)
        assert gap * (abs(value) - tail) > remainder
        _, low, _ = ss.limiting_response(r % 3, s % 3, actual, 8)
        assert gs.direct_grade_response(r, s, 8) == low
    initial = (1, (2, 2, (2, 0)), (0, 1, (1, 0)))
    for block in [(3, 3), (2, 1, 1, 2, 1, 1)]:
        state = initial
        trace = []
        for digit in block:
            state = cf.advance_state(state, digit)
            assert (sum(state[1][:2]) + sum(state[2][:2])) % 3
            trace.append(state[2])
        assert state == initial
        print('RESONANT_AVOIDANCE_FULL_LOOP', block, trace)
    # Disjoint block images and derivative bounds support the 1/12 measure proof.
    assert F(12, 31) - F(4, 13) == F(32, 403)
    assert 1 * 10 - 3 * 3 == 1 and 7 * 31 - 12 * 18 == 1
    assert 49 ** 2 == 2401 < 2 ** 12
    print('PASS: digit threshold, exact parent cylinders and resonant state reconstruction')


if __name__ == '__main__':
    check()
