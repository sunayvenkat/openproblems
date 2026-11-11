"""Exact occupation factorization and state-Green identities; no closure claim."""
from collections import defaultdict
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load(name, folder, file):
    path = Path(__file__).resolve().parents[1] / folder / file
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rr = load('occupation_actual', 'Erdos 168 response closure tests', 'response_relations_check.py')
fan = load('occupation_fan', 'Erdos 168 correlated return arithmetic', 'farey_fan_check.py')
models = load('occupation_model', 'Erdos 168 reflected return models', 'two_sided_models_check.py')
add, sub, rot = rr.add, rr.sub, rr.rot
ONE, OM, OM2 = (1, 0), (0, 1), (-1, -1)
PMINUS = ((0, 0), (-1, -1), (-1, 0))
SMINUS = ((0, 0), (1, 0), (0, -1))


def mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]-z[1]*w[1]


def phi(z, row):
    x, y = z
    return (int(x <= 0 and x-y <= 0) if row >= 4 else rr.low_eta(z, row))


def d2(z, row, u, v):
    return phi(z, row)-phi(sub(z, u), row)-phi(sub(z, v), row)+phi(sub(sub(z, u), v), row)


def pair(measure, func):
    return sum((weight*func(z) for z, weight in measure.items()), F(0))


def convolution(a, b, shift=(0, 0), rotation=0):
    out = defaultdict(F)
    for x, wx in a.items():
        for y, wy in b.items():
            out[add(add(rot(x, rotation), y), shift)] += wx*wy
    return dict(out)


def add_measure(out, value, factor=1):
    for state, weight in value.items():
        out[state] += factor*weight


def axes_occupation(aa, bb, event, horizontal, vertical):
    a = [defaultdict(F) for _ in range(3)]
    b = [defaultdict(F) for _ in range(3)]
    for n, weight in horizontal:
        a[n % 3][aa[n]] += weight
    for n, weight in vertical:
        b[n % 3][sub(sub(bb[n], ONE), event(n))] += weight
    return a, b


def state_measures(state, a_occ, b_occ, bb):
    pr, qr, endpoint = state
    rotation = (2*pr-qr) % 3
    gamma = rot(ONE, rotation)
    out = {row: defaultdict(F) for row in (0, 1, 2, 3, 4)}
    for i in range(3):
        offset = add(sub(endpoint, gamma), rot(mul(SMINUS[pr], PMINUS[i]), -qr))
        for j in range(3):
            shift = add(offset, rr.CORRECTION[(i+qr) % 3][j])
            add_measure(out[4], convolution(a_occ[i], b_occ[j], shift, rotation))
        for row in range(4):
            shift = add(offset, rr.CORRECTION[(i+qr) % 3][row % 3])
            singleton = {sub(bb[row], ONE): F(1, 3**row)}
            add_measure(out[row], convolution(a_occ[i], singleton, shift, rotation))
    return out, gamma


def actual_state(a, b, aa, bb):
    z = add(sub(add(aa[a], bb[b]), ONE), rr.CORRECTION[a % 3][b % 3])
    return sub(z, rr.event(b)) if b >= 4 else z


def board_imbalance(exponent):
    counts = [0, 0, 0]
    cutoff, power3, b = 2**exponent, 1, 0
    while power3 <= cutoff:
        value, a = power3, 0
        while value <= cutoff:
            counts[(a-b) % 3] += 1
            value, a = 2*value, a+1
        power3, b = 3*power3, b+1
    return counts[0]-counts[2], counts[1]-counts[2]


def check():
    rules = {1: (ONE, OM, ONE, 1), 2: (OM, OM2, OM2, 1),
             3: (ONE, OM2, (0, -1), -1), 4: (OM, OM2, (0, 0), 1)}
    for row, (u, v, vertex, sign) in rules.items():
        for x in range(-9, 10):
            for y in range(-9, 10):
                z = x, y
                assert d2(z, row, u, v) == sign*int(z == vertex)
    width = 48
    aa, bb = rr.axes(width)
    horizontal = [(n, F(1, 2**n)) for n in range(width)]
    vertical = [(n, F(1, 3**n)) for n in range(4, width)]
    a_occ, b_occ = axes_occupation(aa, bb, rr.event, horizontal, vertical)
    states = set()
    for row in fan.gs.compatible_children():
        if row[:3] in fan.gs.reachable_phases():
            states.update(fan.states_from_class(row))
    assert len(states) == 8
    for state in sorted(states):
        measures, gamma = state_measures(state, a_occ, b_occ, bb)
        factored = -3*sum((pair(measure, lambda z, row=row: phi(z, row)-phi(sub(z, gamma), row))
                          for row, measure in measures.items()), F(0))
        direct = sum((F(rr.response(state, a, b, aa, bb)[0], 2**a*3**b)
                      for a in range(width) for b in range(width)), F(0))
        assert factored == direct
        for row, (u, v, vertex, sign) in rules.items():
            for t in ((0, 0), ONE, OM, OM2):
                lhs = pair(measures[row], lambda z: d2(add(z, t), row, u, v))
                assert lhs == sign*measures[row].get(sub(vertex, t), 0)
    # The target is the identity-axis case, with its sole origin birth paid once.
    target, _ = state_measures((0, 0, ONE), a_occ, b_occ, bb)
    eta = sum((pair(measure, lambda z, row=row: phi(z, row))
               for row, measure in target.items()), F(0))
    mass = 3*(1-F(1, 2**width))*(1-F(1, 3**width))
    target_value = mass-3*eta-1
    for a, b in ((0, 0), (0, 1), (0, 3), (1, 1), (4, 4), (5, 11), (9, 28)):
        z = add(sub(add(aa[a], bb[b]), ONE), rr.CORRECTION[a % 3][b % 3])
        if b >= 4:
            z = sub(z, rr.event(b))
        coefficient = 1-3*(phi(z, b)+int((a, b) == (0, 1)))
        assert coefficient == rr.original_c(a, b)
    # These finite checks support the exact board identity; unboundedness is a proved input.
    for a in range(0, width, 3):
        assert aa[a] == board_imbalance(a)
        assert sub(actual_state(a, 4, aa, bb), aa[a]) == sub(actual_state(0, 4, aa, bb), aa[0])
    seen, arrivals = set(), []
    for a in range(0, width-4, 3):
        vertex = actual_state(a, 4, aa, bb)
        if vertex in seen:
            continue
        seen.add(vertex)
        first = min(i+j for j in range(4, a+5) for i in range(a+5-j)
                    if actual_state(i, j, aa, bb) == vertex)
        upper = 6*F(1, 2**first)-3*F(1, 3**first)
        assert 0 < target[4][vertex] <= upper
        t = -vertex[0], -vertex[1]
        assert pair(target[4], lambda z: d2(add(z, t), 4, OM, OM2)) == target[4][vertex]
        arrivals.append((vertex, first))
    # Complete rational occupation products reproduce the full model, not a truncation.
    for p, q, side in ((12, 19, -1), (53, 84, 1)):
        ma, mb, event, _, value = models.model(p, q, side)
        h = [(n, F(1, 2**n)/(1-F(1, 2**(3*q)))) for n in range(3*q)]
        v = [(n, F(1, 3**n)/(1-F(1, 3**(3*p)))) for n in range(4, 4+3*p)]
        ao, bo = axes_occupation(ma, mb, event, h, v)
        measure, _ = state_measures((0, 0, ONE), ao, bo, mb)
        hit = sum((pair(m, lambda z, row=row: phi(z, row)) for row, m in measure.items()), F(0))
        assert 2-3*hit == value
    print('PASS: four complete state-Green kernels, all8 actual response products, low rows and full rational occupations')
    print('ACTUAL_FINITE_VERTEX_FIRST_ARRIVALS', arrivals)
    print('ACTUAL_RECTANGLE48_TARGET', target_value)


if __name__ == '__main__':
    check()
