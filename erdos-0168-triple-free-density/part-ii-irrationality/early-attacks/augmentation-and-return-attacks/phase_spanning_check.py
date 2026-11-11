"""Seek one counterexample to the three-color spanning claim; verify it exactly."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.research-tools/python'))
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

STEPS = ((1, 1), (-1, -1), (2, -1), (-2, 1), (-1, 2), (1, -2))


def board(t):
    points = []
    b, power3 = 0, 1
    while power3 <= t:
        a, value = 0, power3
        while value <= t:
            points.append((a, b, value))
            a, value = a + 1, value * 2
        b, power3 = b + 1, power3 * 3
    return sorted(points, key=lambda p: p[2])


def verify(t, chosen):
    points = {(a, b): u for a, b, u in board(t)}
    selected = {p for p, u in points.items() if u in chosen}
    assert len(selected) == len(chosen)
    assert not any({(a, b), (a + 1, b), (a, b + 1)} <= selected
                   for a, b in points)
    groups = []
    for j in range(3):
        group = {p for p in selected if (p[0] - p[1]) % 3 == j}
        assert any(a == 0 for a, b in group)
        assert any(b == 0 for a, b in group)
        assert any(3 * points[p] > t for p in group)
        reached = {next(iter(group))}
        pending = list(reached)
        while pending:
            a, b = pending.pop()
            for da, db in STEPS:
                neighbor = (a + da, b + db)
                if neighbor in group and neighbor not in reached:
                    reached.add(neighbor)
                    pending.append(neighbor)
        assert reached == group
        groups.append(sorted(points[p] for p in group))
    return groups


def solve(t):
    points = board(t)
    n = len(points)
    index = {(a, b): i for i, (a, b, _) in enumerate(points)}
    horizontal = [i for i, (_, b, _) in enumerate(points) if b == 0]
    arcs = [(i, index[a + da, b + db])
            for i, (a, b, _) in enumerate(points) for da, db in STEPS
            if (a + da, b + db) in index]
    h = len(horizontal)
    roots = {i: n + k for k, i in enumerate(horizontal)}
    supplies = {i: n + h + k for k, i in enumerate(horizontal)}
    arc_start = n + 2 * h
    size = arc_start + len(arcs)
    rows, lower, upper = [], [], []

    def add(row, lo, hi):
        rows.append(row)
        lower.append(lo)
        upper.append(hi)

    for a, b, u in points:
        if 3 * u <= t:
            add({index[a, b]: 1, index[a + 1, b]: 1,
                 index[a, b + 1]: 1}, -np.inf, 2)
    for j in range(3):
        group = [i for i, (a, b, _) in enumerate(points) if (a - b) % 3 == j]
        add({roots[i]: 1 for i in horizontal if i in group}, 1, 1)
        add({i: 1 for i in group if points[i][0] == 0}, 1, np.inf)
        add({i: 1 for i in group if 3 * points[i][2] > t}, 1, np.inf)
    balances = [{i: -1} for i in range(n)]
    for i in horizontal:
        add({roots[i]: 1, i: -1}, -np.inf, 0)
        add({supplies[i]: 1, roots[i]: -n}, -np.inf, 0)
        balances[i][supplies[i]] = 1
    for k, (i, j) in enumerate(arcs, arc_start):
        add({k: 1, i: -n}, -np.inf, 0)
        add({k: 1, j: -n}, -np.inf, 0)
        balances[i][k] = -1
        balances[j][k] = 1
    for row in balances:
        add(row, 0, 0)
    matrix = lil_matrix((len(rows), size))
    for r, row in enumerate(rows):
        for c, value in row.items():
            matrix[r, c] = value
    costs = np.zeros(size)
    costs[:n] = 1
    integrality = np.zeros(size)
    integrality[:n + h] = 1
    limits = np.full(size, n, dtype=float)
    limits[:n + h] = 1
    result = milp(costs, integrality=integrality,
                  bounds=Bounds(np.zeros(size), limits),
                  constraints=LinearConstraint(matrix.tocsr(), lower, upper),
                  options={'time_limit': 45})
    answer = {'t': t, 'board_size': n, 'solver_status': int(result.status),
              'solver_message': result.message}
    if result.x is not None:
        chosen = [u for i, (_, _, u) in enumerate(points) if result.x[i] > .5]
        answer['groups'] = verify(t, chosen)
        answer['exact_witness_verified'] = True
    return answer


if __name__ == '__main__':
    # The full board at t=3 contains an upward corner and must be rejected.
    try:
        verify(3, [1, 2, 3])
    except AssertionError:
        pass
    else:
        raise AssertionError('The independence verifier accepted an upward corner')
    answer = solve(int(sys.argv[1]) if len(sys.argv) > 1 else 729)
    print(json.dumps(answer, indent=2))
    Path(__file__).with_suffix('.json').write_text(json.dumps(answer, indent=2) + '\n')
