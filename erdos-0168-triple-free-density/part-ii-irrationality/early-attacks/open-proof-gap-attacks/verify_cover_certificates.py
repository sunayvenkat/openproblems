"""Verify the decisive finite certificates using exact arithmetic only."""
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE.parent / 'Open conjecture transfer search'))
from exact_168_diagonal import smooth_prefix, exact_tau

data = json.loads((HERE / 'cover_lp_counterexample.json').read_text())
points = smooth_prefix(data['k'])
assert points[-1][0] == data['t'] == 486
roots = [v for v, _, _ in points if 3*v <= 486]
x = {int(v): Fraction(w) for v, w in data['primal'].items()}
y = {int(v): Fraction(w) for v, w in data['dual'].items()}
assert set(x) <= {v for v, _, _ in points} and set(y) <= set(roots)
assert all(w >= 0 for w in [*x.values(), *y.values()])
assert all(sum(x.get(n, 0) for n in (v, 2*v, 3*v)) >= 1 for v in roots)
assert all(sum(y.get(v, 0) for v in roots if n in (v, 2*v, 3*v)) <= 1
           for n, _, _ in points)
assert sum(x.values()) == sum(y.values()) == Fraction(2468, 249)
assert exact_tau(points) == data['tau'] == 11
simple = json.loads((HERE / 'cover_lp_simple_primal.json').read_text())
w = {int(v): n for v, n in simple['weights'].items()}
assert simple['denominator'] == 2 and sum(w.values()) == 20
assert all(sum(w.get(n, 0) for n in (v, 2*v, 3*v)) >= 2 for v in roots)

edges = {4: [{2, 6}, {8, 12}], 18: [{6, 12}]}
assert edges[4][0].isdisjoint(edges[4][1])
assert all(not e.isdisjoint(edges[18][0]) for e in edges[4])
assert all(e & {6, 12} for es in edges.values() for e in es)
print('Verified: tau(486)=11, fractional tau=2468/249, half-integral cover cost10; t18 has no two-label rainbow matching.')
