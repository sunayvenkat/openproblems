"""Exact one-board test of the claimed implication from canonicality to phase."""
from itertools import combinations
import json
from pathlib import Path
import runpy
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
NOTES = HERE.parent
dual = runpy.run_path(str(NOTES / 'Erdos 168 boundary and arithmetic/dual_check.py'),
                     run_name='canonical_audit')
exact = runpy.run_path(str(NOTES / 'Open conjecture transfer search/exact_168_diagonal.py'),
                      run_name='canonical_audit')
points = [p for p in exact['smooth_prefix'](100) if p[0] <= 54]
board = {(a, b) for _, a, b in points}
values = {(a, b): u for u, a, b in points}
color0 = [p for p in board if (p[0] - p[1]) % 3 == 0]
records = []
for size in range(len(color0) + 1):
    for subset in combinations(color0, size):
        edges = [edge for u in subset for edge in dual['owned_edges'](u, board)]
        deficiency = size - len(dual['matching'](edges))
        records.append((deficiency, size, sorted(values[u] for u in subset)))
maximum = max(d for d, _, _ in records)
smallest = min(size for d, size, _ in records if d == maximum)
cover = {1, 6, 12, 16, 18}
assert all({u, 2*u, 3*u} & cover for u, _, _ in points if 3*u <= 54)
tau = exact['exact_tau'](points)
assert tau == len(cover) == 5
assert maximum == 1 and smallest == 4
assert len(cover & {values[p] for p in color0}) == len(color0) - smallest
phases = [{u for u, a, b in points if a == 0 and (-b) % 3 == j}
          for j in range(3)]
assert not any(phase <= cover for phase in phases)
answer = {'t': 54, 'tau': tau, 'cover': sorted(cover),
          'color0_size': len(color0), 'maximum_deficiency': maximum,
          'minimum_maximizer_size': smallest,
          'minimum_maximizers': [u for d, size, u in records
                                if d == maximum and size == smallest],
          'vertical_phases': [sorted(phase) for phase in phases]}
ranks = {frozenset(u): size - d for d, size, u in records}
for a, b in combinations(ranks, 2):
    if ranks[a] + ranks[b] < ranks[a | b] + ranks[a & b]:
        answer['submodularity_counterexample'] = {
            'a': sorted(a), 'b': sorted(b), 'union': sorted(a | b),
            'intersection': sorted(a & b),
            'ranks_a_b_union_intersection': [ranks[a], ranks[b],
                                            ranks[a | b], ranks[a & b]]}
        break
else:
    answer['submodularity_counterexample'] = None
HERE.joinpath('canonical_phase_check.json').write_text(json.dumps(answer, indent=2) + '\n')
print(json.dumps(answer, indent=2))
