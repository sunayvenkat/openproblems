"""Exact small checks for the boundary/alternating-network derivation."""
import sys
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'Open conjecture transfer search'))
from exact_168_diagonal import smooth_prefix

STEPS = ((1, 1), (-1, -1), (-2, 1), (2, -1), (1, -2), (-1, 2))


def owned_edges(u, points):
    a, b = u
    pairs = (((a, b-1), (a+1, b-1)),
             ((a-1, b+1), (a-1, b)),
             ((a+1, b), (a, b+1)))
    return [(left, right) for left, right in pairs if left in points and right in points]


def matching(edges):
    # Same augmenting-path algorithm as the existing cover_words.py checker.
    adj = {}
    for left, right in edges:
        adj.setdefault(left, []).append(right)
    matched = {}
    def augment(left, seen):
        for right in adj[left]:
            if right not in seen:
                seen.add(right)
                if right not in matched or augment(matched[right], seen):
                    matched[right] = left
                    return True
        return False
    for left in adj:
        augment(left, set())
    return matched


def rank(matrix):
    rows = [[Fraction(x) for x in row] for row in matrix]
    pivot = 0
    for col in range(len(rows[0]) if rows else 0):
        choice = next((i for i in range(pivot, len(rows)) if rows[i][col]), None)
        if choice is None:
            continue
        rows[pivot], rows[choice] = rows[choice], rows[pivot]
        for i in range(pivot+1, len(rows)):
            factor = rows[i][col]/rows[pivot][col]
            rows[i] = [x-factor*y for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
    return pivot


def boundary_matrix(shape, edges):
    core = {u for u in shape if u[1] > 0}
    indexed = [((a, b+1), (c-1, d+1)) for (a, b), (c, d) in edges]
    sources = sorted({x for x, _ in indexed}-core, reverse=True)
    sinks = sorted({y for _, y in indexed}-core, reverse=True)
    arcs = {}
    for x, y in indexed:
        if x != y:
            assert (y[0]-x[0], y[1]-x[1]) in ((-2, 1), (-1, -1))
            arcs.setdefault(x, []).append(y)
    matrix = []
    for source in sources:
        counts = {source: 1}
        for x in sorted(core | {source}, reverse=True):
            for y in arcs.get(x, []):
                counts[y] = counts.get(y, 0)+counts.get(x, 0)
        matrix.append([counts.get(y, 0)-int(y == source) for y in sinks])
    return sources, sinks, matrix


def connected(shape):
    seen = {next(iter(shape))}
    stack = list(seen)
    while stack:
        a, b = stack.pop()
        for da, db in STEPS:
            v = a+da, b+db
            if v in shape and v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(shape)


def holefree(shape):
    # Finite hex-coordinate box with a connected exterior boundary.
    base = next(iter(shape))
    def axial(v):
        a, b = v[0]-base[0], v[1]-base[1]
        return (a+2*b)//3, (b-a)//3
    transformed = {axial(v) for v in shape}
    lo = min(min(v) for v in transformed)-2
    hi = max(max(v) for v in transformed)+2
    outside = {(x, y) for x in range(lo, hi+1) for y in range(lo, hi+1)}-transformed
    stack = [(lo, lo)]
    seen = set(stack)
    while stack:
        x, y = stack.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)):
            v = x+dx, y+dy
            if v in outside and v not in seen:
                seen.add(v)
                stack.append(v)
    return seen == outside


if __name__ == '__main__':
    assert len(matching([((0, 0), (1, 0)), ((0, 0), (2, 0)), ((1, 1), (1, 0))])) == 2
    assert not holefree(set(STEPS))
    assert rank([[1, 2], [2, 4]]) == 1 and rank([[1, 2], [2, 3]]) == 2
    checked = 0
    critical_checked = 0
    first = None
    for k, (t, _, _) in enumerate(smooth_prefix(33 if '--rank' in sys.argv else 70), 1):
        points = {(a, b) for _, a, b in smooth_prefix(k)}
        for j in range(3):
            labels = sorted(u for u in points if (u[0]-u[1]) % 3 == j)
            if '--avoid-axis' in sys.argv:
                labels = [u for u in labels if u[0] > 0]
            if len(labels) > 17:
                continue
            for mask in range(1, 1 << len(labels)):
                shape = {u for i, u in enumerate(labels) if mask >> i & 1}
                if '--rank' not in sys.argv and not any(b == 0 for a, b in shape):
                    continue
                if not connected(shape) or not holefree(shape):
                    continue
                edges = [edge for u in shape for edge in owned_edges(u, points)]
                assert all((a-b) % 3 == (j+1) % 3 for (a, b), _ in edges)
                assert all((a-b) % 3 == (j-1) % 3 for _, (a, b) in edges)
                nu = len(matching(edges))
                left = {l for l, r in edges}
                right = {r for l, r in edges}
                checked += 1
                if '--rank' in sys.argv:
                    sources, sinks, matrix = boundary_matrix(shape, edges)
                    nr = len(shape)-sum(b == 0 for a, b in shape)
                    assert nr+rank(matrix) == nu, (t, shape, matrix, nu)
                    adjacency = [[int((l, r) in edges) for r in sorted(right)] for l in sorted(left)]
                    assert rank(adjacency) == nu, (t, shape, adjacency, nu)
                    if nu == len(shape)-1 and all(len(matching([edge for u in shape-{q}
                            for edge in owned_edges(u, points)])) == nu for q in shape):
                        critical_checked += 1
                        arcs = [((a, b+1), (c-1, d+1)) for (a, b), (c, d) in edges
                                if (a, b+1) != (c-1, d+1)]
                        reachable, coreachable = set(sources), set(sinks)
                        for x, y in sorted(arcs, reverse=True):
                            if x in reachable:
                                reachable.add(y)
                        for x, y in sorted(arcs):
                            if y in coreachable:
                                coreachable.add(x)
                        assert {q for q in shape if q[1] > 0} <= reachable | coreachable
                elif nu < min(len(left), len(right)) and ('--positive' not in sys.argv or nu < len(shape)):
                    first = (t, j, sorted(2**a*3**b for a, b in shape), nu,
                             sorted(2**a*3**b for a, b in left),
                             sorted(2**a*3**b for a, b in right))
                    break
            if first:
                break
        if first:
            break
    print({'checked': checked, 'boundary_rank_verified': '--rank' in sys.argv,
           'critical_reachability_verified': critical_checked,
           'first_smaller_side_failure': first})
