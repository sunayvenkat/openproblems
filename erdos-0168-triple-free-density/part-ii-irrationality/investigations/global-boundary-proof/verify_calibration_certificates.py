"""Verify the two saved calibration certificates without an optimizer."""
import json
import sys
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'Open conjecture transfer search'))
from exact_168_diagonal import smooth_prefix, candidate_tau

FAMILIES = {'corner': ((1, 2, 3), 1),
            'six': ((1, 2, 3, 4, 6, 9), 2),
            'nine': ((2, 3, 4, 6, 8, 9, 12, 18, 27), 3)}


def constraints(points):
    t = points[-1][0]
    return [(name, v, tuple(v*m for m in multipliers), rhs)
            for name, (multipliers, rhs) in FAMILIES.items()
            for v, _, _ in points if v*max(multipliers) <= t]


small = json.loads((HERE/'calibration_486.json').read_text())
points = smooth_prefix(small['vertices'])
rows = constraints(points)
x = {int(v): Fraction(w) for v, w in small['primal'].items()}
y = {(row['family'], row['root']): Fraction(row['weight']) for row in small['dual']}
assert points[-1][0] == small['t'] == 486
assert all(w >= 0 for w in list(x.values())+list(y.values()))
assert all(sum(x.get(v, 0) for v in support) >= rhs for _, _, support, rhs in rows)
assert all(sum(y.get((name, root), 0) for name, root, support, _ in rows if v in support) <= 1
           for v, _, _ in points)
assert sum(x.values()) == sum(y.get((name, root), 0)*rhs for name, root, _, rhs in rows)
assert sum(x.values()) == Fraction(235, 23)

large = json.loads((HERE/'calibration_cap_probe.json').read_text())
points = smooth_prefix(large['vertices'])
rows = constraints(points)
denominator = large['denominator']
x = {int(v): w for v, w in large['primal_numerators'].items()}
assert points[-1][0] == large['t'] == 990677827584
assert len(rows) == large['constraints'] == 1367
assert all(0 <= x.get(v, 0) <= denominator for v, _, _ in points)
assert all(sum(x.get(v, 0) for v in support) >= rhs*denominator
           for _, _, support, rhs in rows)
classes = [sum((a-b) % 3 == j for _, a, b in points) for j in range(3)]
assert classes == large['K'] == [178, 178, 178]
assert candidate_tau(points) == large['candidate'] == 178
assert large['I'] == large['P'] == [0, 0, 0]
assert Fraction(sum(x.values()), denominator) == Fraction(176511563, 1000000) < 177
print('Verified both certificates exactly; all 1367 large-cap inequalities passed.')
