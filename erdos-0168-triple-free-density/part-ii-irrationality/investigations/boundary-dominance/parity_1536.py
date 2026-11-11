"""One exact test: can an odd-hit cover beat all pure phases at t=1536?"""
import json
from pathlib import Path
import runpy
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
exact = runpy.run_path(str(HERE.parent / 'Open conjecture transfer search/exact_168_diagonal.py'),
                      run_name='parity_check')
T = 1536
points = [p for p in exact['smooth_prefix'](100) if p[0] <= T]
rows = [[u for u, a, b in points if b == row]
        for row in range(max(b for _, _, b in points) + 1)]
assert all(len(rows[b + 1]) < len(rows[b]) for b in range(len(rows) - 1))
best = len(points) + 1
best_energy = len(points) * 3
best_covers = []
for seed in range(1 << len(rows[0])):
    bits = [(seed >> a) & 1 for a in range(len(rows[0]))]
    cover = {u for a, u in enumerate(rows[0]) if bits[a]}
    for row in rows[1:]:
        bits = [1 ^ bits[a] ^ bits[a + 1] for a in range(len(row))]
        cover.update(u for a, u in enumerate(row) if bits[a])
    hits = [len(cover & {u, 2*u, 3*u}) for u, _, _ in points if 3*u <= T]
    assert all(hit in (1, 3) for hit in hits)
    energy = sum(hit - 1 for hit in hits)
    score = (len(cover), energy)
    if score < (best, best_energy):
        best, best_energy = score
        best_covers = [sorted(cover)]
    elif score == (best, best_energy):
        best_covers.append(sorted(cover))
classes = [sum((a-b) % 3 == j for _, a, b in points) for j in range(3)]
assert classes == [15, 15, 15]
answer = {'t': T, 'vertices': len(points), 'bottom_width': len(rows[0]),
          'odd_covers_checked': 1 << len(rows[0]), 'color_sizes': classes,
          'minimum_odd_cover': best, 'minimum_energy_at_that_size': best_energy,
          'minimum_size_minimum_energy_covers': best_covers}
HERE.joinpath('parity_1536.json').write_text(json.dumps(answer, indent=2) + '\n')
print(json.dumps(answer, indent=2))
