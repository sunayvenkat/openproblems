"""One adversarial test of the proposed uniform cut bound, at a saved cap."""
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.research-tools/python'))
sys.path.insert(0, str(ROOT / 'research_notes/Open conjecture transfer search'))
import numpy as np
from scipy.optimize import linprog
from exact_168_diagonal import smooth_prefix, candidate_tau

points = smooth_prefix(534)
t = points[-1][0]
assert t == 990677827584
index = {v: i for i, (v, _, _) in enumerate(points)}
families = [('corner', (1, 2, 3), 1),
            ('six', (1, 2, 3, 4, 6, 9), 2),
            ('nine', (2, 3, 4, 6, 8, 9, 12, 18, 27), 3)]
rows = [(name, v, tuple(v*m for m in multiples), rhs)
        for name, multiples, rhs in families
        for v, _, _ in points if v*max(multiples) <= t]
matrix = np.zeros((len(rows), len(points)))
for i, (_, _, support, _) in enumerate(rows):
    matrix[i, [index[v] for v in support]] = 1
result = linprog(np.ones(len(points)), A_ub=-matrix,
                 b_ub=-np.array([row[3] for row in rows]),
                 bounds=(0, 1), method='highs')
assert result.success, result.message
# Upward rational rounding gives a verifiable feasible upper certificate.
denominator = 10**6
numerators = [min(denominator, math.ceil(max(0, float(x))*denominator)+1)
              for x in result.x]
assert all(0 <= x <= denominator for x in numerators)
assert all(sum(numerators[index[v]] for v in support) >= rhs*denominator
           for _, _, support, rhs in rows)
value = Fraction(sum(numerators), denominator)
candidate = candidate_tau(points)
classes = [sum((a-b) % 3 == j for _, a, b in points) for j in range(3)]
isolated, patch = [0, 0, 0], [0, 0, 0]
exponent = t.bit_length()-1
if 3*(1 << exponent) > 2*t:
    isolated[exponent % 3] = 1
exponent = (t//6).bit_length()-1
if exponent >= 1 and 4*t < 27*(1 << exponent):
    patch[exponent % 3] = 1
assert candidate == min(classes[j]-isolated[j]-patch[j] for j in range(3))
assert classes == [178, 178, 178] and isolated == patch == [0, 0, 0]
output = {'t': t, 'vertices': len(points), 'constraints': len(rows),
          'K': classes, 'I': isolated, 'P': patch,
          'candidate': candidate, 'certified_feasible_weight': str(value),
          'refutes_uniform_ceiling_bound': value <= candidate-1,
          'denominator': denominator,
          'primal_numerators': {str(v): x for (v, _, _), x in zip(points, numerators) if x}}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps({k: output[k] for k in output if k != 'primal_numerators'}))
