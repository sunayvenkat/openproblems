"""Discover invariant tensor-square certificates for products of quadratics.

Numerical feasibility is not a proof.  The coefficient equations below are
constructed by exact Einstein-index contractions; a found solution still needs
an exact positive-semidefinite reconstruction.
"""

import argparse
import itertools as it
import json
import math
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).parent / ".research-tools" / "python"))
import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import cvxpy as cp


def allocations(positions, counts):
    if len(counts) == 0:
        yield (), tuple(positions)
        return
    for first in it.combinations(positions, counts[0]):
        rest = tuple(x for x in positions if x not in first)
        for groups, leftover in allocations(rest, counts[1:]):
            yield (first,) + groups, leftover


def networks(m, cut=2, degree=2):
    p, n = tuple(range(cut)), tuple(range(cut, m))
    left, right = degree * len(p) - 1, degree * len(n) - 1
    boundary = left + right
    out = []
    for flat in it.product(range(degree + 1), repeat=len(p) * len(n)):
        h = np.array(flat, dtype=int).reshape(len(p), len(n))
        row, col = h.sum(axis=1), h.sum(axis=0)
        t = int(h.sum())
        if t < 1 or max(row) > degree or max(col) > degree:
            continue
        internal = [[] for _ in range(m)]
        index = boundary
        for a, i in enumerate(p):
            for b, j in enumerate(n):
                for _ in range(h[a, b]):
                    internal[i].append(index)
                    internal[j].append(index)
                    index += 1
        for hol, hd in allocations(tuple(range(left)), degree - row):
            for anti, ad in allocations(tuple(range(left, boundary)), degree - col):
                for matched in it.permutations(ad):
                    legs = [list(v) for v in internal]
                    for i, free in zip(p + n, hol + anti):
                        legs[i].extend(free)
                    out.append((tuple(tuple(sorted(x)) for x in legs),
                                tuple(sorted(zip(hd, matched)))))
    assert len(out) == len(set(out))
    return out, left, right


def contingency_tables(m, degree=2):
    rows = []
    for indices in it.combinations_with_replacement(range(m), degree):
        row = [0] * m
        for i in indices:
            row[i] += 1
        rows.append(tuple(row))

    def visit(current, capacities):
        if len(current) == m:
            yield tuple(x for row in current for x in row)
            return
        for row in rows:
            if all(a <= b for a, b in zip(row, capacities)):
                yield from visit(current + [row], tuple(b - a for a, b in zip(row, capacities)))

    return list(visit([], (degree,) * m))


def orbits_and_target(m, degree=2):
    permutations = list(it.permutations(range(m)))
    lookup, targets, representatives = {}, [], []
    for table in contingency_tables(m, degree):
        if table in lookup:
            continue
        orbit = set()
        for perm in permutations:
            orbit.add(tuple(table[perm[i] * m + perm[j]] for i in range(m) for j in range(m)))
            orbit.add(tuple(table[perm[j] * m + perm[i]] for i in range(m) for j in range(m)))
        idx = len(targets)
        for member in orbit:
            lookup[member] = idx
        representative = min(orbit)
        wreath = all(x in (0, degree) for x in representative)
        coefficient = 0 if wreath else math.factorial(degree) ** (2 * m) // math.prod(math.factorial(x) for x in representative)
        targets.append(coefficient * len(orbit))
        representatives.append(representative)
    assert sum(targets) == math.factorial(degree * m) - math.factorial(degree) ** m * math.factorial(m)
    return lookup, np.array(targets, dtype=float), representatives


def inner_diagram(a, b, m, boundary, cut=2, degree=2):
    # Free indices are shared; internal indices in a and b are independent.
    shift = degree * m
    size = boundary + 2 * shift
    parents = list(range(size))

    def root(i):
        while parents[i] != i:
            parents[i] = parents[parents[i]]
            i = parents[i]
        return i

    def union(i, j):
        parents[root(i)] = root(j)

    def translate(i, side):
        return i if i < boundary else i + side * shift

    used = set()
    for side, net in enumerate((a, b)):
        for i, j in net[1]:
            x, y = translate(i, side), translate(j, side)
            used.update((x, y))
            union(x, y)
        for pair in net[0]:
            used.update(translate(i, side) for i in pair)
    components = {root(i): [] for i in used}
    for side, net in enumerate((a, b)):
        for block, pair in enumerate(net[0]):
            holomorphic = (block < cut) == (side == 1)
            for i in pair:
                components[root(translate(i, side))].append((holomorphic, block))
    table = [0] * (m * m)
    loops = 0
    for legs in components.values():
        if not legs:
            loops += 1
            continue
        assert len(legs) == 2 and legs[0][0] != legs[1][0], legs
        hol, anti = sorted(legs, reverse=True)
        table[hol[1] * m + anti[1]] += 1
    assert all(sum(table[i*m:(i+1)*m]) == degree for i in range(m))
    assert all(sum(table[j::m]) == degree for j in range(m))
    return tuple(table), loops


def permutation_action(nets, positions):
    lookup = {net: i for i, net in enumerate(nets)}
    actions = []
    for perm in it.permutations(positions):
        substitutions = dict(zip(positions, perm))
        mapped = []
        for legs, deltas in nets:
            changed = (tuple(tuple(sorted(substitutions.get(i, i) for i in pair)) for pair in legs),
                       tuple(sorted((substitutions.get(i, i), substitutions.get(j, j)) for i, j in deltas)))
            mapped.append(lookup[changed])
        parity = (-1) ** sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1, len(perm)))
        matrix = sp.csc_matrix((np.ones(len(nets), dtype=int), (mapped, range(len(nets)))), shape=(len(nets), len(nets)))
        actions.append((perm, parity, matrix))
    return actions


def boundary_projectors(nets, positions):
    if len(positions) == 1:
        return [("1", sp.eye(len(nets), dtype=int, format="csc"))]
    if len(positions) != 3:
        # A primitive Young projector from commuting Jucys--Murphy operators.
        # Denominators are positive/negative scalars irrelevant to its range.
        def partitions(total, ceiling=None):
            if not total:
                yield ()
                return
            for first in range(min(total, ceiling or total), 0, -1):
                for rest in partitions(total - first, first):
                    yield (first,) + rest

        lookup = {net: i for i, net in enumerate(nets)}
        identity = sp.eye(len(nets), dtype=np.int64, format="csc")
        jm = [None, None]
        for k in range(2, len(positions) + 1):
            matrix = sp.csc_matrix(identity.shape, dtype=np.int64)
            for j in range(k - 1):
                substitutions = {positions[j]: positions[k-1], positions[k-1]: positions[j]}
                mapped = []
                for legs, deltas in nets:
                    changed = (tuple(tuple(sorted(substitutions.get(i, i) for i in pair)) for pair in legs),
                               tuple(sorted((substitutions.get(i, i), substitutions.get(j, j)) for i, j in deltas)))
                    mapped.append(lookup[changed])
                matrix += sp.csc_matrix((np.ones(len(nets), dtype=np.int64), (mapped, range(len(nets)))), shape=identity.shape)
            jm.append(matrix)
        result = []
        for shape in partitions(len(positions)):
            projector = identity.copy()
            prefix = []
            k = 0
            for row, width in enumerate(shape):
                for col in range(width):
                    k += 1
                    if k > 1:
                        addable = [prefix[r] - r for r in range(len(prefix)) if r == 0 or prefix[r] < prefix[r-1]]
                        addable.append(-len(prefix))
                        chosen = col - row
                        assert chosen in addable
                        for alternative in addable:
                            if alternative != chosen:
                                projector = projector @ (jm[k] - alternative * identity)
                    if row == len(prefix):
                        prefix.append(0)
                    prefix[row] += 1
            result.append((str(shape), projector))
        return result
    actions = permutation_action(nets, positions)
    trivial = sum(matrix for _, _, matrix in actions)
    sign = sum(parity * matrix for _, parity, matrix in actions)
    swap = (positions[1], positions[0], positions[2])
    transposition = next(matrix for perm, _, matrix in actions if perm == swap)
    standard = 3 * (sp.eye(len(nets), dtype=int, format="csc") - transposition) - sign
    return [("trivial", trivial), ("sign", sign), ("standard", standard)]


def reduced_bases(nets, left, right, channels="all"):
    bases = []
    def allowed(name):
        if channels == "all" or name in ("1", "trivial"):
            return True
        if name == "standard":
            return channels == "hook"
        if name == "sign":
            return False
        shape = tuple(int(x.strip()) for x in name.strip("()").split(",") if x.strip())
        return len(shape) == 1 or (channels == "hook" and len(shape) == 2 and shape[1] == 1)
    for hn, hp in boundary_projectors(nets, tuple(range(left))):
        if not allowed(hn):
            continue
        for an, ap in boundary_projectors(nets, tuple(range(left, left + right))):
            if not allowed(an):
                continue
            full = (hp @ ap).toarray()
            _, qr, pivots = la.qr(full, pivoting=True, mode="economic")
            rank = int(np.sum(np.abs(np.diag(qr)) > 1e-7))
            if not rank:
                continue
            raw = full[:, pivots[:rank]]
            basis, triangular = la.qr(raw, mode="economic")
            transform = la.solve_triangular(triangular, np.eye(rank))
            bases.append((hn + "/" + an, raw, basis, transform))
    return bases


def solve(m, dimension, solver, cuts, objective, degree, channels):
    started = time.time()
    lookup, target, representatives = orbits_and_target(m, degree)
    bases, all_nets = [], {}
    variables, coefficients, constraints = [], [], []
    for cut in cuts:
        nets, left, right = networks(m, cut, degree)
        all_nets[cut] = nets
        print(json.dumps({"m": m, "degree": degree, "dimension": dimension, "cut": cut, "covariants": len(nets), "orbits": len(target)}), flush=True)
        diagrams = [[] for _ in target]
        for i, a in enumerate(nets):
            for j in range(i, len(nets)):
                table, loops = inner_diagram(a, nets[j], m, left + right, cut, degree)
                orbit = lookup[table]
                value = dimension ** loops
                diagrams[orbit].append((i, j, value))
                if i != j:
                    diagrams[orbit].append((j, i, value))
        matrices = []
        for entries in diagrams:
            if entries:
                i, j, data = zip(*entries)
                matrices.append(sp.csc_matrix((data, (i, j)), shape=(len(nets), len(nets))))
            else:
                matrices.append(sp.csc_matrix((len(nets), len(nets))))
        cut_bases = reduced_bases(nets, left, right, channels)
        cut_bases = [(f"cut{cut}/{name}", raw, basis, norms) for name, raw, basis, norms in cut_bases]
        bases.extend(cut_bases)
        print(json.dumps({"blocks": [(name, raw.shape[1]) for name, raw, _, _ in cut_bases], "setup_seconds": time.time() - started}), flush=True)
        for name, raw, basis, norms in cut_bases:
            x = cp.Variable((basis.shape[1], basis.shape[1]), symmetric=True, name=name)
            variables.append(x)
            constraints.append(x >> 0)
            coefficients.append([basis.T @ matrix @ basis for matrix in matrices])
    scale = max(target)
    equations = [sum(cp.sum(cp.multiply(coefs[o], x)) for coefs, x in zip(coefficients, variables)) == target[o] / scale for o in range(len(target))]
    cost = sum(cp.trace(x) for x in variables) if objective == "trace" else 0
    problem = cp.Problem(cp.Minimize(cost), constraints + equations)
    options = {"solver": solver, "verbose": False}
    if solver == "CLARABEL":
        options.update(tol_gap_abs=1e-9, tol_gap_rel=1e-9, tol_feas=1e-9, max_iter=150)
    elif solver == "SCS":
        options.update(eps=1e-7, max_iters=100000)
    problem.solve(**options)
    output = {"m": m, "degree": degree, "dimension": dimension, "status": problem.status,
              "seconds": time.time() - started, "objective": problem.value,
              "target": target.tolist(), "representatives": representatives,
              "networks": all_nets, "cuts": cuts, "channels": channels, "blocks": []}
    if all(x.value is not None for x in variables):
        values = [x.value * scale for x in variables]
        reconstructed = [sum(np.sum(c[o] * value) for c, value in zip(coefficients, values)) for o in range(len(target))]
        output["max_residual"] = max(abs(np.array(reconstructed) - target))
        output["minimum_eigenvalue"] = min(float(la.eigvalsh(value)[0]) for value in values)
        for (name, raw, basis, transform), value in zip(bases, values):
            output["blocks"].append({"name": name, "basis": raw.tolist(),
                                     "gram": (transform @ value @ transform.T).tolist(),
                                     "eigenvalues": la.eigvalsh(value).tolist()})
    suffix = "" if degree == 2 else f"-k{degree}"
    if channels != "all":
        suffix += f"-{channels}"
    path = Path(f"marcus-invariant-sdp-{m}-{dimension}-{'-'.join(map(str,cuts))}{suffix}.json")
    path.write_text(json.dumps(output, indent=2))
    print(json.dumps({key: value for key, value in output.items() if key not in ("networks", "blocks", "target", "representatives")}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--blocks", type=int, choices=(3, 4), default=3)
    parser.add_argument("--dimension", type=int, default=5)
    parser.add_argument("--degree", type=int, default=2)
    parser.add_argument("--solver", choices=("CLARABEL", "SCS"), default="CLARABEL")
    parser.add_argument("--cuts", type=int, nargs="+", default=[2])
    parser.add_argument("--objective", choices=("trace", "feasible"), default="trace")
    parser.add_argument("--channels", choices=("all", "hook", "trivial"), default="all")
    args = parser.parse_args()
    solve(args.blocks, args.dimension, args.solver, args.cuts, args.objective, args.degree, args.channels)
