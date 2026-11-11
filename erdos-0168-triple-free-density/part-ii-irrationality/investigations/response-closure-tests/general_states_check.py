"""Exact compatible Farey states and complete current-child responses."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util


def load(name, folder, file):
    path = Path(__file__).resolve().parents[1] / folder / file
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ss = load('jump_certificate', 'Erdos 168 signed arithmetic returns', 'signed_scalar_check.py')
cf = load('return_states', 'Erdos 168 boundary return mechanisms', 'cf_return_state_check.py')


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def sub(z, w):
    return z[0] - w[0], z[1] - w[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c-b*d


def omega(n):
    return ((1, 0), (0, 1), (-1, -1))[n % 3]


def divide(z, w):
    c, d = w
    denominator = c*c-c*d+d*d
    a, b = mul(z, (c-d, -d))
    if a % denominator or b % denominator:
        return None
    return a//denominator, b//denominator


def commutator(hu, hv, u, v):
    return sub(mul(sub((1, 0), omega(sum(v))), hu),
               mul(sub((1, 0), omega(sum(u))), hv))


def compatible_children():
    """A conservative finite list; no arbitrary state is claimed reachable."""
    residues = [(p, q) for p in range(3) for q in range(3) if p or q]
    result = []
    for u in residues:
        for v in residues:
            if (u[0]*v[1]-v[0]*u[1]) % 3 != 2:
                continue
            med = ((u[0]+v[0]) % 3, (u[1]+v[1]) % 3)
            if med not in cf.BALANCED_H:
                continue
            hm = cf.BALANCED_H[med]
            ru, rv = omega(sum(u)), omega(sum(v))
            rm = mul(ru, rv)
            for phase in range(3):
                c = mul(omega(phase), (1, -1))
                hv = divide(sub(mul(sub((1, 0), rv), hm), c), sub((1, 0), rm))
                if hv is None:
                    continue
                hu = sub(hm, mul(ru, hv))
                assert commutator(hu, hv, u, v) == c
                assert add(hu, mul(ru, hv)) == hm
                for side in ('lower', 'upper'):
                    current = u if side == 'lower' else v
                    if sum(current) % 3 == 0:
                        continue
                    child = (((2*u[0]+v[0]) % 3, (2*u[1]+v[1]) % 3)
                             if side == 'lower' else
                             ((u[0]+2*v[0]) % 3, (u[1]+2*v[1]) % 3))
                    hc = add(hu, mul(ru, hm)) if side == 'lower' else add(hm, mul(rm, hv))
                    endpoint, response, tail = ss.limiting_response(*child, hc, 24)
                    _, med_response, med_tail = ss.limiting_response(*med, hm, 24)
                    result.append((u, v, phase, side, med, hm, child, hc,
                                   response, tail, med_response, med_tail))
    return result


def reachable_phases():
    assert commutator(cf.christoffel_transform(5, 8),
                      cf.christoffel_transform(12, 19), (5, 8), (12, 19)) == (1, -1)
    initial = ((2, 2), (0, 1), 0)
    seen, pending = {initial}, [initial]
    while pending:
        u, v, phase = pending.pop()
        med = ((u[0]+v[0]) % 3, (u[1]+v[1]) % 3)
        for nxt in [(med, v, phase), (u, med, (phase+sum(u)) % 3)]:
            if nxt not in seen:
                seen.add(nxt)
                pending.append(nxt)
    return seen


GOOD_CLASSES = {
    ((0, 1), (1, 0), 'upper'),
    ((0, 2), (2, 0), 'upper'),
    ((1, 2), (0, 2), 'upper'),
    ((2, 0), (1, 1), 'upper'),
    ((2, 2), (0, 1), 'upper'),
}

CHILD_BOUNDS = {
    ((2, 1), (1, 0)): (-F(11, 20), -F(27, 50)),
    ((1, 2), (1, 1)): (F(77, 100), F(79, 100)),
    ((1, 0), (0, 0)): (-F(1, 5000), -F(1, 10000)),
}


def direct_grade_response(p, q, width):
    """Finite retimed-token grade enumeration also permits resonance."""
    maximum = p*(q+width-1)+q*(width-1)
    points = {}

    def insert(a, b, color):
        grade = p*a+q*b
        if grade <= maximum:
            points.setdefault((grade, a, b), []).append(color % 3)

    insert(0, 0, 0)
    insert(0, 1, -1)
    insert(1, 1, 0)
    for a in range(maximum//p+1):
        insert(a, 1, a+1)
    for a in range(-1, maximum//p+1):
        insert(a, 3, a+2)
    for b in range(2, maximum//q+1):
        for a in range((maximum-q*b)//p+1):
            insert(a, b, a-b)
    births = []
    for direction in (1, -1):
        counts, table = [0, 0, 0], {}
        for grade, a, b in sorted(points, key=lambda item: (item[0], direction*item[1])):
            before = min(counts)
            for color in points[grade, a, b]:
                counts[color] += 1
            table[a, b] = min(counts)-before
        assert table[-1, 3] == 0
        births.append(table)
    return sum((F(-3*(births[0].get((q+a, b), 0)-births[1].get((q+a, b), 0)), 2**a*3**b)
                for a in range(width) for b in range(width)), F(0))


def two_node_certificate(current, successor):
    p, q = current
    pp, qq = successor
    med = p+pp, q+qq
    child = 2*p+pp, 2*q+qq
    intervals = []
    for r, s in (med, child):
        h = cf.christoffel_transform(r, s)
        _, value, tail = ss.limiting_response(r % 3, s % 3, h, 24)
        factor = F(1, 2**s)-F(1, 3**r)
        endpoints = factor*(value-tail), factor*(value+tail)
        intervals.append((min(endpoints), max(endpoints)))
    remainder = (ss.farey_variation(*current, *child)
                 +ss.farey_variation(*child, *med)
                 +ss.farey_variation(*med, *successor))
    lo = sum(row[0] for row in intervals)
    hi = sum(row[1] for row in intervals)
    assert lo > remainder or hi < -remainder
    return min(abs(lo), abs(hi))/remainder


def check_commutators():
    pairs = [((0, 1), (1, 0))]
    for _ in range(7):
        new = []
        for u, v in pairs:
            hu = (1, 0) if u == (0, 1) else cf.christoffel_transform(*u)
            hv = (0, 0) if v == (1, 0) else cf.christoffel_transform(*v)
            c = commutator(hu, hv, u, v)
            assert c in [mul(omega(k), (1, -1)) for k in range(3)]
            m = u[0]+v[0], u[1]+v[1]
            if 0 < m[0] <= m[1]:
                assert cf.christoffel_transform(*m) == add(hu, mul(omega(sum(u)), hv))
                new += [(u, m), (m, v)]
        pairs = new


if __name__ == '__main__':
    check_commutators()
    states = compatible_children()
    reachable = reachable_phases()
    print('REACHABLE_RESIDUE_PHASES', len(reachable))
    states = [row for row in states if (row[0], row[1], row[2]) in reachable]
    assert len(reachable) == 24
    assert len({(u, v) for u, v, phase in reachable}) == 24
    unique = {}
    for row in states:
        key = row[4], row[6], row[7]
        unique[key] = row
    print('COMPATIBLE_CASES', len(states), 'UNIQUE_MEDIANT_CHILD', len(unique))
    signs = {True: 0, False: 0, 'unresolved': 0}
    for key, row in sorted(unique.items()):
        response, tail, med_response, med_tail = row[8:]
        sign = 1 if response > tail else -1 if response < -tail else 0
        med_sign = 1 if med_response > med_tail else -1
        signs[sign == med_sign if sign else 'unresolved'] += 1
        assert abs(response)-tail > F(1, 10000)
        assert (sign == med_sign) == ((row[0], row[1], row[3]) in GOOD_CLASSES)
        if sign == med_sign:
            lo, hi = CHILD_BOUNDS[row[6], row[7]]
            assert lo < response-tail < response+tail < hi
    assert len(states) == 16 and signs == {True: 5, False: 11, 'unresolved': 0}
    print('SIGN_CASES', signs)
    h = cf.christoffel_transform(65, 103)
    _, value, _ = ss.limiting_response(65 % 3, 103 % 3, h, 8)
    assert direct_grade_response(65, 103, 8) == value
    for current, successor in [((12, 19), (41, 65)), ((53, 84), (306, 485)),
                               ((306, 485), (665, 1054))]:
        p, q = current
        pp, qq = successor
        lower, upper = sorted((current, successor), key=lambda pair: F(*pair))
        med = p+pp, q+qq
        child = 2*p+pp, 2*q+qq
        hm, hc = cf.christoffel_transform(*med), cf.christoffel_transform(*child)
        hu, hv = cf.christoffel_transform(*lower), cf.christoffel_transform(*upper)
        c = commutator(hu, hv, lower, upper)
        assert c in [mul(omega(k), (1, -1)) for k in range(3)]
        _, rm, tm = ss.limiting_response(med[0] % 3, med[1] % 3, hm, 24)
        _, rc, tc = ss.limiting_response(child[0] % 3, child[1] % 3, hc, 24)
        assert abs(rc) > tc
        print('ACTUAL_CHILD', current, successor, 'mediant', med, hm,
              'child', child, hc, 'resonant', sum(child) % 3 == 0,
              'same_response_sign', (rm > 0) == (rc > 0), 'C', c)
        if (rm > 0) == (rc > 0):
            ratio = two_node_certificate(current, successor)
            print('TWO_NODE_CERTIFICATE', current, 'leading/remainder >', ratio//1)
    assert states
    print('PASS: commutator states, resonant response and complete two-node clusters')
