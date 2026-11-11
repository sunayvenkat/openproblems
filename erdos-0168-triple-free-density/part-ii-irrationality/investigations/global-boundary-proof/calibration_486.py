"""One exact-certificate check of two valid integer cuts at the known LP gap."""
import json
import sys
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.research-tools/python'))
sys.path.insert(0, str(ROOT / 'research_notes/Open conjecture transfer search'))
import numpy as np
from scipy.optimize import linprog
from exact_168_diagonal import smooth_prefix, exact_tau


def check():
    # Check the local binary implications independently of the LP solver.
    local = (1, 2, 3, 4, 6, 8, 9, 12, 18, 27)
    for mask in range(1 << len(local)):
        chosen = {v for i, v in enumerate(local) if mask & (1 << i)}
        if all(chosen.intersection((v, 2*v, 3*v)) for v in (1, 2, 3, 4, 6, 9)):
            assert len(chosen.intersection((1, 2, 3, 4, 6, 9))) >= 2
            assert len(chosen.intersection(local[1:])) >= 3

    points = smooth_prefix(33)
    assert points[-1][0] == 486
    index = {v: i for i, (v, _, _) in enumerate(points)}
    families = [('corner', (1, 2, 3), 1),
                ('six', (1, 2, 3, 4, 6, 9), 2),
                ('nine', (2, 3, 4, 6, 8, 9, 12, 18, 27), 3)]
    rows = [(name, v, tuple(v*m for m in multiples), rhs)
            for name, multiples, rhs in families
            for v, _, _ in points if v*max(multiples) <= 486]
    matrix = np.zeros((len(rows), len(points)))
    for i, (_, _, support, _) in enumerate(rows):
        matrix[i, [index[v] for v in support]] = 1
    rhs = np.array([row[3] for row in rows])
    result = linprog(np.ones(len(points)), A_ub=-matrix, b_ub=-rhs,
                     bounds=(0, None), method='highs')
    assert result.success, result.message
    primal = [Fraction(float(v)).limit_denominator(10**8) for v in result.x]
    dual = [Fraction(float(v)).limit_denominator(10**8)
            for v in -result.ineqlin.marginals]
    assert all(x >= 0 for x in primal + dual)
    assert all(sum(primal[index[v]] for v in support) >= bound
               for _, _, support, bound in rows)
    assert all(sum(y for y, (_, _, support, _) in zip(dual, rows) if v in support) <= 1
               for v, _, _ in points)
    lower = sum(y*row[3] for y, row in zip(dual, rows))
    assert lower == sum(primal)
    output = {'t': 486, 'vertices': len(points), 'constraints': len(rows),
              'integer_tau': exact_tau(points), 'strengthened_lp': str(lower),
              'primal': {str(v): str(x) for (v, _, _), x in zip(points, primal) if x},
              'dual': [{'family': name, 'root': v, 'weight': str(y)}
                       for y, (name, v, _, _) in zip(dual, rows) if y]}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: output[k] for k in ('t', 'vertices', 'constraints',
                                             'integer_tau', 'strengthened_lp')}))


if __name__ == '__main__':
    check()
