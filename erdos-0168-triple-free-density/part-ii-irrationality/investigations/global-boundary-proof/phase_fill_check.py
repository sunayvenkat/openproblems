"""One exact falsification test of a proposed vertical critical-set filling lemma."""
from itertools import combinations
import json
from pathlib import Path
import runpy
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
dual = runpy.run_path(str(HERE.parent / 'Erdos 168 boundary and arithmetic/dual_check.py'),
                     run_name='fill_audit')
points = [p for p in dual['smooth_prefix'](100) if p[0] <= 1536]
board = {(a, b) for _, a, b in points}
values = {(a, b): u for u, a, b in points}
color = sorted((p for p in board if (p[0] - p[1]) % 3 == 2), key=values.get)
allowed = [p for p in color if values[p] != 256]


def deficiency(subset):
    edges = [edge for p in subset for edge in dual['owned_edges'](p, board)]
    return len(subset) - len(dual['matching'](edges))


assert len(color) == 15
full_deficiency = deficiency(color)
assert full_deficiency == 0
witness = None
checked = 0
for size in range(1, len(allowed) + 1):
    for subset in combinations(allowed, size):
        checked += 1
        if not any(b == 0 for a, b in subset):
            continue
        if deficiency(subset) > 0:
            witness = subset
            break
    if witness is not None:
        break
answer = {'t': 1536, 'j': 2, 'full_class_deficiency': full_deficiency,
          'excluded_patch_root': 256, 'subsets_checked': checked,
          'critical_witness': None if witness is None else [values[p] for p in witness]}
if witness is not None:
    assert deficiency(witness) == 1
    assert any(a == 0 for a, b in witness)
    assert all(deficiency(subset) <= 0 for size in range(len(witness))
               for subset in combinations(witness, size))
HERE.joinpath('phase_fill_check.json').write_text(json.dumps(answer, indent=2) + '\n')
print(json.dumps(answer, indent=2))
