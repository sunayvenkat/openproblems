"""Exact finite searches for Erdos 624; SAT witnesses are checked directly."""

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import sys
import time


def subsets(mask):
    current = mask
    while current:
        yield current
        current = (current - 1) & mask
    yield 0


def build(n, h, q, symmetry=True, singleton_pattern=None, encoding="pair"):
    low = sorted((a for a in range(1 << n) if a.bit_count() < h),
                 key=lambda a: (a.bit_count(), a))
    variables = {a: [i * q + c + 1 for c in range(q)]
                 for i, a in enumerate(low)}
    next_variable = len(low) * q + 1
    clauses = []
    for row in variables.values():
        clauses.append(row[:])
        clauses.extend([-a, -b] for a, b in itertools.combinations(row, 2))
    # A repeated proper-subset color can be replaced by an absent color.
    for b in low:
        if b.bit_count() >= 2 and (1 << b.bit_count()) <= q:
            for a in subsets(b):
                if a != b:
                    clauses.extend([-variables[a][c], -variables[b][c]]
                                   for c in range(q))
    for points in itertools.combinations(range(n), h):
        y = sum(1 << x for x in points)
        proper = [a for a in subsets(y) if a != y]
        if encoding == "pair":
            for c, d in itertools.combinations(range(q), 2):
                clauses.append([variables[a][color]
                                for a in proper for color in (c, d)])
        else:
            missing = list(range(next_variable, next_variable + q))
            next_variable += q
            for c, flag in enumerate(missing):
                clauses.append([flag] + [variables[a][c] for a in proper])
            # A sequential at-most-one constraint on the missing-color flags.
            if q > 1:
                seen = list(range(next_variable, next_variable + q - 1))
                next_variable += q - 1
                clauses.append([-missing[0], seen[0]])
                for i in range(1, q - 1):
                    clauses.extend(([-missing[i], seen[i]],
                                    [-seen[i - 1], seen[i]],
                                    [-missing[i], -seen[i - 1]]))
                clauses.append([-missing[-1], -seen[-1]])
    base_clauses = len(clauses)
    if symmetry:
        clauses.append([variables[0][0]])
        # Canonical first use of colors, with the empty set first.
        for i, a in enumerate(low):
            for c in range(1, q):
                if c > i:
                    clauses.append([-variables[a][c]])
                elif c > 1:
                    clauses.append([-variables[a][c]] +
                                   [variables[b][c - 1] for b in low[:i]])
        # Ground points can be ordered by their singleton colors.
        if h >= 2:
            for x in range(n - 1):
                for c in range(q):
                    for d in range(c):
                        clauses.append([-variables[1 << x][c],
                                        -variables[1 << (x + 1)][d]])
    if singleton_pattern is not None:
        if len(singleton_pattern) != n or h < 2:
            raise ValueError("A singleton pattern must have n entries and h>=2")
        for x, c in enumerate(singleton_pattern):
            clauses.append([variables[1 << x][c]])
    return clauses, variables, base_clauses, next_variable - 1


def complete_and_verify(n, h, q, low_colors):
    colors = [0] * (1 << n)
    for a, c in low_colors.items():
        if not 0 <= a < (1 << n) or a.bit_count() >= h or not 0 <= c < q:
            raise ValueError("Invalid low-rank color")
        colors[a] = c
    if len(low_colors) != sum(a.bit_count() < h for a in range(1 << n)):
        raise ValueError("Incomplete low-rank assignment")
    for y in range(1 << n):
        if y.bit_count() == h:
            present = {colors[a] for a in subsets(y) if a != y}
            missing = set(range(q)) - present
            if len(missing) > 1:
                raise AssertionError(("Too many missing colors", y, missing))
            colors[y] = next(iter(missing), 0)
    # This check does not consult the clauses or the solver.
    checked = 0
    for y in range(1 << n):
        if y.bit_count() >= h:
            if {colors[a] for a in subsets(y)} != set(range(q)):
                raise AssertionError(("Coverage failed", y))
            checked += 1
    return colors, checked


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("h", type=int)
    parser.add_argument("--q", type=int)
    parser.add_argument("--solver", default="g42")
    parser.add_argument("--encoding", choices=("pair", "missing"), default="pair")
    parser.add_argument("--seconds", type=float, default=120)
    parser.add_argument("--pattern", help="Comma-separated singleton colors")
    parser.add_argument("--phases", type=Path, help="Prefer colors from a checked witness")
    parser.add_argument("--repair-from", type=Path,
                        help="Preserve a checked witness, relaxing conflicting assignments")
    parser.add_argument("--no-symmetry", action="store_true")
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    q = args.n if args.q is None else args.q
    if not 1 <= args.h <= args.n or not 1 <= q <= 256:
        parser.error("Require 1<=h<=n and 1<=q<=256")
    if args.seconds <= 0:
        parser.error("The time limit must be positive")
    if args.phases and args.repair_from:
        parser.error("Use either --phases or --repair-from")
    if not args.worker and not args.verify:
        # Native solver interruption can be delayed during processing.
        # A separate Python process enforces the wall-clock limit.
        started = time.monotonic()
        try:
            result = subprocess.run([sys.executable, __file__, *sys.argv[1:],
                                     "--worker"], timeout=args.seconds)
            if result.returncode:
                print(json.dumps({"status": "ERROR",
                                  "worker_returncode": result.returncode}), flush=True)
                sys.exit(1)
        except subprocess.TimeoutExpired:
            print(json.dumps({"status": "UNKNOWN", "reason": "wall_timeout",
                              "seconds": time.monotonic() - started}), flush=True)
        return
    if args.verify:
        data = json.loads(args.verify.read_text())
        if (data["n"], data["h"], data["q"]) != (args.n, args.h, q):
            raise ValueError("Witness parameters do not match the requested check")
        low = {int(a): c for a, c in data["low_colors"].items()}
        colors, checked = complete_and_verify(args.n, args.h, q, low)
        digest = hashlib.sha256(bytes(colors)).hexdigest()
        if digest != data["sha256"]:
            raise ValueError("Witness hash does not match the reconstructed coloring")
        print(json.dumps({"verified": True, "sets_checked": checked,
                          "sha256": digest}))
        return
    pattern = list(map(int, args.pattern.split(","))) if args.pattern else None
    clauses, variables, base, variable_count = build(
        args.n, args.h, q, not args.no_symmetry, pattern, args.encoding)
    print(json.dumps({"n": args.n, "h": args.h, "q": q,
                      "variables": variable_count,
                      "color_variables": len(variables) * q,
                      "base_clauses": base, "clauses": len(clauses),
                      "solver": args.solver, "encoding": args.encoding,
                      "pattern": pattern,
                      "repair_from": str(args.repair_from) if args.repair_from else None}),
          flush=True)
    sys.path.insert(0, str(Path(__file__).parent / "_deps"))
    from pysat.solvers import Solver
    started = time.monotonic()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        preferred = {}
        source = args.repair_from or args.phases
        if source:
            previous = json.loads(source.read_text())
            if previous["h"] != args.h or previous["q"] > q or previous["n"] > args.n:
                raise ValueError("Starting witness parameters do not match")
            preferred = {int(a): c for a, c in previous["low_colors"].items()}
            old_colors, _ = complete_and_verify(
                previous["n"], previous["h"], previous["q"], preferred)
            if hashlib.sha256(bytes(old_colors)).hexdigest() != previous["sha256"]:
                raise ValueError("Starting witness hash does not match")
            solver.set_phases([v if preferred.get(a) == c else -v
                               for a, row in variables.items()
                               for c, v in enumerate(row)])
        assumptions = {variables[a][c]: a for a, c in preferred.items()} if args.repair_from else {}
        initial_assumptions = len(assumptions)
        while True:
            result = solver.solve(assumptions=list(assumptions))
            if result or not assumptions:
                break
            core = solver.get_core()
            if not core:
                break
            # Release one high-rank assignment; the remaining ones stay fixed.
            released = max(core, key=lambda v: (assumptions[v].bit_count(), assumptions[v]))
            del assumptions[released]
            relaxed = initial_assumptions - len(assumptions)
            if relaxed <= 5 or relaxed & (relaxed - 1) == 0:
                print(json.dumps({"relaxed_assignments": relaxed,
                                  "core_size": len(core),
                                  "assignments_preserved": len(assumptions)}), flush=True)
        summary = {"status": "SAT" if result else
                   "UNSAT" if result is False else "UNKNOWN",
                   "seconds": time.monotonic() - started,
                   "stats": solver.accum_stats(),
                   "relaxed_assignments": initial_assumptions - len(assumptions)}
        if result:
            positive = {v for v in solver.get_model() if v > 0}
            low_colors = {a: next(c for c, v in enumerate(row) if v in positive)
                          for a, row in variables.items()}
            colors, checked = complete_and_verify(args.n, args.h, q, low_colors)
            data = {"n": args.n, "h": args.h, "q": q,
                    "low_colors": low_colors,
                    "sha256": hashlib.sha256(bytes(colors)).hexdigest()}
            path = Path(__file__).parent / (
                f"witness_{args.n}_{args.h}_{q}_{data['sha256']}.json")
            path.write_text(json.dumps(data, indent=2) + "\n")
            summary.update(witness=str(path), sets_checked=checked,
                           sha256=data["sha256"])
        print(json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
