from fractions import Fraction as F
from pathlib import Path
import runpy


CASES = (
    dict(u=(8, -5), v=(3, -2), cutoff=6561, previous=6144,
         survivors=50, rhs=-2,
         weights=(-2, -1, -2, -2, -1, -2,
                  -1, 0, -2, -1, 1, 2,
                  -2, -1, -1, 2, 1, 1,
                  0, 1, 0, 2, 3, 0,
                  -1, 2, 2, 1, 1, 0,
                  0, 1, -1, -1, -2, 1),
         zero_rows=((729, 0, 4), (1458, 1, 2), (2916, 1, 1),
                    (6561, 2, 1), (2187, 1, 3), (6561, 1, 4),
                    (864, 2, 2), (3456, 1, 3), (4608, 1, 2),
                    (243, 1, 1), (486, 2, 3), (1458, 2, 3), (2187, 2, 2)),
         prior_cover=(15, 17, 70, 14, 66, 13, 69, 16, 71, 67, 12, 68)),
    dict(u=(19, -12), v=(27, -17), cutoff=3057647616, previous=2902376448,
         survivors=53, rhs=-3,
         weights=(-2, -2, -2, -2, -2, 1,
                  1, 1, 1, -2, 1, 1,
                  1, -2, 1, 1, -2, 1,
                  1, 1, -2, 1, 1, -2,
                  -2, 1, 1, -2, 4, 1,
                  -2, -2, 1, 1, -2, 4),
         zero_rows=((382205952, 1, 6), (764411904, 2, 3), (1528823808, 0, 3),
                    (3057647616, 1, 3), (129140163, 1, 6), (258280326, 0, 3),
                    (1019215872, 2, 3), (2293235712, 0, 6), (258280326, 2, 6),
                    (429981696, 0, 3), (805306368, 1, 3)),
         prior_cover=(5, 38, 3, 52, 9, 50, 56, 23, 27, 68, 21, 70)),
)


def build_case(u, v):
    source = Path(__file__).parent.parent / 'Erdos 168 Farey transport corrections' / 'torus_bulk_check.py'
    return runpy.run_path(str(source))['prepare'](u, v)


def check_case(case):
    types, times, lags, profiles, _, _ = build_case(case['u'], case['v'])
    end = times.index(case['cutoff'])
    assert times[end-1] == case['previous'] and F(27, 2) in times
    zero_bans = {k for k in range(72) if any(
        lags[i][c] == 0 and profiles[k][i][c] > 0
        for i in range(end+1) for c in range(3))}
    allowed = set(range(72)) - zero_bans
    assert len(allowed) == case['survivors']
    weights = case['weights']
    assert len(weights) == 36 and sum(weights) == case['rhs'] < 0
    edge_weights = [sum(weights[j] for j in types[k][3]) for k in range(72)]
    assert min(edge_weights[k] for k in allowed) >= 0
    # Full Farkas replay on all 72 variables, without deleting any forbidden type.
    rows = [(times.index(t), c, multiplier) for t, c, multiplier in case['zero_rows']]
    assert all(i <= end and lags[i][c] == 0 and multiplier > 0
               for i, c, multiplier in rows)
    full_columns = [edge_weights[k] + sum(
        multiplier*profiles[k][i][c] for i, c, multiplier in rows) for k in range(72)]
    assert min(full_columns) >= 0
    assert sum(weights) + sum(multiplier*lags[i][c] for i, c, multiplier in rows) < 0
    # The earlier integer cover is also an exact fractional witness, at every earlier event.
    cover = case['prior_cover']
    assert len(set(cover)) == 12
    assert all(sum(j in types[k][3] for k in cover) == 1 for j in range(36))
    assert all(sum(profiles[k][i][c] for k in cover) <= lags[i][c]
               for i in range(end) for c in range(3))
    print('EXACT FIRST FRACTIONAL OBSTRUCTION', case['u'], case['v'], case['cutoff'],
          'previous', case['previous'], 'zero survivors', len(allowed),
          'Farkas RHS', sum(weights), 'minimum column', min(full_columns))
    return types, allowed


if __name__ == '__main__':
    for case in CASES:
        types, allowed = check_case(case)
        if case['rhs'] == -3:
            s = {0, 1, 2, 3, 4, 9, 13, 16, 20, 23, 24, 27, 30, 31, 34}
            t = {28, 35}
            assert len(s)-len(t) == 13
            assert all(sum(j in s for j in types[k][3]) -
                       sum(j in t for j in types[k][3]) <= 1 for k in allowed)
    print('PASS: integer Farkas rows over all72 types and all earlier joint-capacity witnesses')
