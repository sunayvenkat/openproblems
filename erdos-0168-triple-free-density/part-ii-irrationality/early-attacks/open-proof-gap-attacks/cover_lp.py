"""Look for an exact counterexample to ceil(fractional tau) = integer tau."""
import sys
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / '.research-tools/python'))
sys.path.insert(0, str(ROOT / 'research_notes/Open conjecture transfer search'))
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
from exact_168_diagonal import smooth_prefix, candidate_tau, exact_tau


def rational_certificate(points, x, y):
    xs = [Fraction(float(v)).limit_denominator(10**9) for v in x]
    ys = [Fraction(float(v)).limit_denominator(10**9) for v in y]
    index = {v: i for i, (v, _, _) in enumerate(points)}
    roots = [v for v, _, _ in points if 3*v <= points[-1][0]]
    assert all(v >= 0 for v in xs + ys)
    assert all(sum(xs[index[w]] for w in (v, 2*v, 3*v)) >= 1 for v in roots)
    assert all(sum(ys[k] for k, v in enumerate(roots) if n in (v, 2*v, 3*v)) <= 1
               for n, _, _ in points)
    assert sum(xs) == sum(ys)
    return {'value': str(sum(xs)),
            'primal': {str(v): str(x) for (v, _, _), x in zip(points, xs) if x},
            'dual': {str(v): str(y) for v, y in zip(roots, ys) if y}}


if __name__ == '__main__':
    points = smooth_prefix(int(sys.argv[1]) if len(sys.argv) > 1 else 500)
    previous = []
    for k in range(3, len(points)+1):
        present = points[:k]
        index = {v: i for i, (v, _, _) in enumerate(present)}
        roots = [v for v, _, _ in present if 3*v <= present[-1][0]]
        matrix = lil_matrix((len(roots), k))
        for i, v in enumerate(roots):
            matrix[i, [index[v], index[2*v], index[3*v]]] = 1
        result = linprog(np.ones(k), A_ub=-matrix.tocsr(), b_ub=-np.ones(len(roots)),
                         bounds=(0, None), method='highs')
        assert result.success
        candidate = candidate_tau(present)
        certificate = rational_certificate(present, result.x, -result.ineqlin.marginals)
        tau = exact_tau(present)
        assert tau == candidate
        if Fraction(certificate['value']) <= candidate-1:
            out = {'k': k, 't': present[-1][0], 'tau': tau,
                   'earlier_prefixes': previous, **certificate}
            Path(__file__).with_name('cover_lp_counterexample.json').write_text(json.dumps(out, indent=2))
            print(json.dumps(out), flush=True)
            break
        previous.append({'k': k, 't': present[-1][0], 'tau': tau,
                         'fractional_tau': certificate['value']})
    else:
        print(json.dumps({'checked': len(points), 'found': None}))
