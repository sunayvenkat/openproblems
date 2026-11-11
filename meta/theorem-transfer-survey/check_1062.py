"""Check the published formula against a separate binary optimizer and signed jumps."""
import json
import sys
from fractions import Fraction
from math import gcd, log
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.research-tools' / 'python'))
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


def power_below(p, q, base):
    value, exponent = 1, 0
    while value * base * q <= p:
        value *= base
        exponent += 1
    return value, exponent


def h(p, q=1):
    if p < q:
        return 0
    u, e4 = power_below(p, q, 4)
    v, _ = power_below(p, q, 3)
    in_e = p >= 2 * u * q and p >= 2 * v * q
    in_c = False
    if p >= 10 * q:
        w, _ = power_below(p, 10 * q, 3)
        in_c = p < 12 * w * q
    in_d = 4 * p < 5 * u * q
    return e4 + int(in_e) - int(in_c and in_d)


def g(p, q=1):
    if p < q:
        return 0
    return 1 + power_below(p, q, 3)[1] + h(p, q)


def jumps(limit):
    endpoints = set()
    for base, start in [(4, 4), (4, 2), (4, 5), (3, 2), (3, 3), (3, 10), (3, 12)]:
        s = start
        while s <= limit:
            endpoints.add(s)
            s *= base
    return [(s, h(s) - h(2*s - 1, 2)) for s in sorted(endpoints)
            if h(s) != h(2*s - 1, 2)]


def n6(n):
    return n - n//2 - n//3 + n//6


def formula(n, js):
    return (n+1)//2 + sum(delta*n6(n//s) for s, delta in js if s <= n)


def direct(n):
    return sum(g(n, m) for m in range(1, n+1) if gcd(m, 6) == 1)


def optimize(n):
    rows = n//3
    matrix = lil_matrix((rows, n), dtype=float)
    upper = []
    for a in range(1, rows+1):
        t = n//a - 1
        matrix[a-1, a-1] = t-1
        for b in range(2*a, n+1, a):
            matrix[a-1, b-1] = 1
        upper.append(t)
    result = milp(-np.ones(n), integrality=np.ones(n), bounds=Bounds(0, 1),
                  constraints=LinearConstraint(matrix.tocsr(), -np.inf, upper),
                  options={'time_limit': 20, 'mip_rel_gap': 0})
    if not result.success:
        return {'n': n, 'status': result.message}
    chosen = {i+1 for i, value in enumerate(result.x) if value > .5}
    assert all(sum(b in chosen for b in range(2*a, n+1, a)) <= 1 for a in chosen)
    assert abs(result.fun + len(chosen)) < 1e-7
    return {'n': n, 'optimum': len(chosen), 'mip_gap': float(result.mip_gap),
            'dual_bound': float(result.mip_dual_bound)}


if __name__ == '__main__':
    limit = 10**70
    js = jumps(limit)
    for n in range(1, 401):
        assert formula(n, js) == direct(n), n
    assert g(270) == g(Fraction(539, 2)) - 1
    assert formula(10**6, js) == 672964
    assert formula(10**12, js) == 672965651200
    assert formula(10**24, js) == 672965651199489347471228
    checks = []
    for n in list(range(3, 31)) + [50, 100, 269, 270, 271, 319, 320, 321, 500]:
        record = optimize(n)
        record['formula'] = formula(n, js)
        if 'optimum' in record:
            assert record['optimum'] == record['formula'], record
        checks.append(record)
        print(json.dumps(record), flush=True)
    c_approx = Fraction(1, 2) + sum((Fraction(delta, 3*s) for s, delta in js), Fraction())
    samples = []
    for base in (2, 3, 4, 6, 10):
        for k in range(1, 65):
            n = base**k
            if n > 10**50:
                break
            for offset in (-1, 0, 1):
                m = n+offset
                if m == 1:
                    continue
                discrepancy = float(formula(m, js) - m*c_approx)
                samples.append({'n': str(m), 'error': discrepancy,
                                'error_over_log_n': discrepancy/log(m)})
    largest = sorted(samples, key=lambda row: abs(row['error']), reverse=True)[:15]
    output = {'signed_jump_direct_checks': 400, 'milp_checks': checks,
              'density_approximation': float(c_approx),
              'density_error_bound': str(Fraction(38, 9*limit)),
              'largest_sample_discrepancies': largest,
              'sharpness_status': 'Sampling does not establish an optimal error order.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2), encoding='utf-8')
    print(json.dumps({'density': float(c_approx), 'largest_errors': largest}), flush=True)
