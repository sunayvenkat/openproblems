"""Exact shell witnesses and the signed exterior of compact state-Green cutoffs."""
from collections import defaultdict
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path


path = Path(__file__).resolve().parents[1] / 'Erdos 168 numerator and residuals' / 'response_arithmetic_check.py'
spec = spec_from_file_location('accepted_occupation', path)
ra = module_from_spec(spec)
spec.loader.exec_module(ra)
ONE, OM, OM2 = (1, 0), (0, 1), (-1, -1)


def radius(z):
    return max(abs(z[0]), abs(z[1]))


def green_radius(z):
    return max(abs(z[1]-z[0]), abs(z[0]))


def cone(z):
    return int(z[0] <= 0 and z[0] <= z[1])


def clipped(z, r):
    return cone(z) if radius(z) <= r else 0


def mixed(z, r):
    return (clipped(z, r) - clipped(ra.sub(z, OM), r)
            - clipped(ra.sub(z, OM2), r) + clipped(ra.add(z, ONE), r))


def exterior(z, r):
    return mixed(z, r) - int(z == (0, 0))


def check():
    for r in range(1, 7):
        rows, cols = defaultdict(int), defaultdict(int)
        values = []
        for x in range(-r-2, r+3):
            for y in range(-r-2, r+3):
                z = x, y
                value = mixed(z, r)
                rows[y-x] += value
                cols[-x] += value
                values.append(exterior(z, r))
                if radius(z) < r:
                    assert exterior(z, r) == 0
        assert not any(rows.values()) and not any(cols.values())
        assert sum(values) == -1 and min(values) < 0 < max(values)
        assert exterior((0, 0), r) == 0
    for n in range(33):
        exact = sum((F(2, 2**(n-b)*3**b) for b in range(n)), F(0)) + F(3, 3**n)
        assert exact == F(6, 2**n) - F(3, 3**n)
    for h, ha, hb, hab in product((0, 1), repeat=4):
        residual = 1+F(34*h-27*ha-8*hb+hab, 182)
        assert F(147, 182) <= residual <= F(217, 182)
    for h, ha in product((0, 1), repeat=2):
        residual = 1+F(h-ha, 7)
        assert F(6, 7) <= residual <= F(8, 7)

    width = 256
    aa, bb = ra.rr.axes(width)
    state = lambda a, b: ra.actual_state(a, b, aa, bb)
    for a in range(64):
        for b in range(4, 64):
            assert green_radius(ra.sub(state(a+3, b), state(a, b))) <= 3
            assert green_radius(ra.sub(state(a, b+3), state(a, b))) <= 5
            assert green_radius(ra.sub(state(a+3, b+3), state(a, b))) <= 8
    path_states = [(a, state(a, 4)) for a in range(0, width, 3)]
    for (_, z), (_, w) in zip(path_states, path_states[1:]):
        assert radius(ra.sub(w, z)) <= 3
        assert green_radius(ra.sub(w, z)) <= 3
    initial = green_radius(path_states[0][1])
    assert initial == 0
    shells = []
    for r in range(initial, max(green_radius(z) for _, z in path_states)):
        a, z = next((a, z) for a, z in path_states if green_radius(z) > r)
        assert r < green_radius(z) <= r+3
        assert F(1, 2**a*3**4) > 0
        shells.append((r, a, z))

    witnesses = {1: {}}
    first_outside = {}
    occupation = defaultdict(F)
    for n in range(4, width):
        for b in range(4, n+1):
            a, z = n-b, state(n-b, b)
            occupation[z] += F(1, 2**a*3**b)
            for r in witnesses:
                h = exterior(z, r)
                if h:
                    witnesses[r].setdefault(1 if h > 0 else -1, (a, b, z, h))
                if green_radius(z) > r:
                    first_outside.setdefault(r, n)
    for r, signed in witnesses.items():
        assert set(signed) == {-1, 1}, (r, signed)
        assert first_outside[r] >= 4
    qh = lambda t: sum((weight*cone(ra.add(z, t)) for z, weight in occupation.items()), F(0))
    boxes = []
    for r in range(9):
        direct = sum((w for z, w in occupation.items() if green_radius(z) <= r), F(0))
        corners = qh((-r, 0))-qh((-r, -2*r-1))-qh((r+1, 2*r+1))+qh((r+1, 0))
        assert direct == corners
        boxes.append(direct)
        if r < 6:
            for x in range(-r-3, r+4):
                for y in range(-2*r-3, 2*r+4):
                    z = x, y
                    cap = lambda w: int(0 <= w[1]-w[0] <= r and 0 <= -w[0] <= r)
                    d2 = cap(z)-cap(ra.sub(z, OM))-cap(ra.sub(z, OM2))+cap(ra.add(z, ONE))
                    formula = (int(z == (0, 0))-int(z == (0, r+1))
                               -int(z == (-r-1, -r-1))+int(z == (-r-1, 0)))
                    assert d2 == formula
    for r in range(6):
        shell = sum((w for z, w in occupation.items() if r < green_radius(z) <= r+3), F(0))
        assert shell == boxes[r+3]-boxes[r] >= 0
    print('PASS: compact marginals, signed exterior, full tails, four-corner boxes and eight-corner shells')
    print('ACTUAL_FIXED_ROW_INITIAL', path_states[0])
    print('ACTUAL_FIRST_SHELL_CROSSINGS', shells)
    print('ACTUAL_OCCUPIED_SIGN_WITNESSES', witnesses)
    print('ACTUAL_FIRST_OUTSIDE_GREEN_TOTAL_INDEX', first_outside)


if __name__ == '__main__':
    check()
