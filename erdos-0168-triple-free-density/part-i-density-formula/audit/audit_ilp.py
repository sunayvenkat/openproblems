"""ILP sampling of inclusion-minimal maximisers of D*_j over A_j for larger t (beyond exhaustive range).

Max |U|-|W| s.t. W covers B(U) gives D*_j. A minimum-cardinality set attaining D*_j inside A_j \\ X (X a forbidden set)
is an inclusion-minimal maximiser of A_j whenever it attains D*_j. We explore forbidden sets by BFS (depth <= 2)
and check the section 6 conclusions (6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 6.9, 6.10) on every maximiser found.
Usage: python audit_ilp.py N
"""
import sys
import numpy as np
from fractions import Fraction as Fr
from scipy.optimize import milp, LinearConstraint, Bounds
from audit_struct import board, edges_for, exceptional, col, val, in_cone, WINDOWS, matching
from audit_formula import smooth_upto


def solve(t, j, own, Aj, forb, Dfix=None):
    owners = [u for u in Aj if u not in forb]
    verts = sorted({p for u in owners for (l, r, _) in own[u] for p in (l, r)})
    ui = {u: i for i, u in enumerate(owners)}
    vi = {v: len(owners) + i for i, v in enumerate(verts)}
    nv = len(owners) + len(verts)
    rows = []
    for u in owners:
        for (l, r, _) in own[u]:
            row = np.zeros(nv)
            row[ui[u]] = 1
            row[vi[l]] -= 1
            row[vi[r]] -= 1
            rows.append(row)
    cons = []
    if rows:
        cons.append(LinearConstraint(np.array(rows), -np.inf, 0))
    c = np.zeros(nv)
    if Dfix is None:
        c[:len(owners)] = -1
        c[len(owners):] = 1
    else:
        c[:len(owners)] = 1
        row = np.zeros(nv)
        row[:len(owners)] = 1
        row[len(owners):] = -1
        cons.append(LinearConstraint(row.reshape(1, -1), Dfix, np.inf))
    res = milp(c, constraints=cons, integrality=np.ones(nv), bounds=Bounds(0, 1))
    if res.status != 0:
        return None, None
    U = [owners[i] for i in range(len(owners)) if res.x[i] > 0.5]
    if Dfix is None:
        return int(round(-res.fun)), U
    return Dfix, U


def classify(t, j, U, D):
    Us = set(U)
    d = len(U) - matching(U, edges_for_cache[(t, j)])
    assert d == D, ("ILP d mismatch", t, j, U, d, D)
    bz = [u for u in U if u[1] == 0]
    az = [u for u in U if u[0] == 0]
    assert bz and az, ("6.1", t, j, U)
    x, y = min(bz, key=val), min(az, key=val)
    mj = {0: (1, 1), 1: (2, 1), 2: (1, 2)}[j]
    if x == (0, 0):
        assert j == 0 and (t < 18 or (1, 1) in Us), ("6.10 O", t, U)
        return "O"
    A, B = x[0], y[1]
    r, s = (2 * A - B) // 3, (2 * B - A) // 3
    assert (2 * A - B) % 3 == 0 and r >= 0 and s >= 0, ("6.2", t, j, U)
    assert all(in_cone(u, x) or in_cone(u, y) for u in U), ("(6.1)", t, j, U)
    jtop = (-max(b for (a, b) in board(t))) % 3
    if s == 0:
        assert B <= 2 and (t < 18 or mj in Us), ("6.4/6.10", t, j, U)
        return "D1"
    if r == 0:
        assert A <= 2 and (t < 18 or mj in Us), ("6.5/6.10", t, j, U)
        return "D2"
    assert 3 * val(y) > t and r in (1, 2) and az == [y] and j == jtop and D == 1, ("6.6", t, j, U)
    assert any(lo <= t < hi for lo, hi in WINDOWS) and (r == 2 or s <= 3), ("6.8/6.9", t, j, U)
    return "I(r=%d,s=%d)" % (r, s)


edges_for_cache = {}

if __name__ == "__main__":
    N = int(sys.argv[1])
    tally = {}
    for t in [t for t in smooth_upto(N) if t >= 18]:
        e, _ = exceptional(t)
        for j in range(3):
            own = edges_for(t, j)
            edges_for_cache[(t, j)] = own
            Aj = [u for u in own if u != e]
            D, _ = solve(t, j, own, Aj, set())
            if D <= 0:
                continue
            seen, frontier = set(), [frozenset()]
            for depth in range(3):
                nxt = []
                for X in frontier:
                    _, U = solve(t, j, own, Aj, X, Dfix=D)
                    if U is None:
                        continue
                    key = frozenset(U)
                    if key not in seen:
                        seen.add(key)
                        k = classify(t, j, U, D)
                        tally[k] = tally.get(k, 0) + 1
                        if k.startswith("I"):
                            print("case (I):", t, j, k, sorted(U, key=val))
                    nxt += [X | {u} for u in U]
                frontier = list(set(nxt))[:40]
    print("ILP sampling up to", N, "all assertions passed; tally", tally)
