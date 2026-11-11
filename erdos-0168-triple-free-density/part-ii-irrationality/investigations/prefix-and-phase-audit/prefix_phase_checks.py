"""Exact finite endpoints used by the prefix-dominance proof candidate."""
from fractions import Fraction
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True


def board(limit):
    points = []
    power3 = 1
    b = 0
    while power3 <= limit:
        value = power3
        a = 0
        while value <= limit:
            points.append((value, a, b))
            value *= 2
            a += 1
        power3 *= 3
        b += 1
    return points


def counts_and_corrections(t):
    counts = [0, 0, 0]
    isolates = [0, 0, 0]
    patches = [0, 0, 0]
    for value, a, b in board(t):
        counts[(a-b) % 3] += 1
        if b == 0 and a >= 1:
            isolates[a % 3] += int(2*t < 3*value)
            patches[a % 3] += int(6*value <= t < Fraction(27*value, 4))
    assert sum(isolates) + sum(patches) <= 1
    return counts, isolates, patches


base_cases = [
    (3, 4, [1, 1, 1], [0, 0, 0], [0, 0, 0], 1),
    (4, 6, [1, 1, 2], [0, 0, 1], [0, 0, 0], 1),
    (6, 8, [2, 1, 2], [0, 0, 0], [0, 0, 0], 1),
    (8, 9, [3, 1, 2], [1, 0, 0], [0, 0, 0], 1),
    (9, 12, [3, 2, 2], [1, 0, 0], [0, 0, 0], 2),
    (12, Fraction(27, 2), [3, 3, 2], [0, 0, 0], [0, 1, 0], 2),
    (Fraction(27, 2), 16, [3, 3, 2], [0, 0, 0], [0, 0, 0], 2),
    (16, 18, [3, 4, 2], [0, 1, 0], [0, 0, 0], 2),
]
high_cases = [
    (54, 64, [6, 5, 5], [0, 0, 0], [0, 0, 0], 0),
    (64, 72, [7, 5, 5], [1, 0, 0], [0, 0, 0], 0),
    (216, 243, [9, 8, 9], [0, 0, 0], [0, 0, 0], 2),
    (576, 648, [12, 12, 11], [1, 0, 0], [0, 0, 0], 1),
    (5184, 5832, [20, 19, 20], [1, 0, 0], [0, 0, 0], 2),
]


def certify(row, high):
    low, upper, counts, isolates, patches, last = row
    low, upper = Fraction(low), Fraction(upper)
    assert counts_and_corrections(low) == (counts, isolates, patches)
    assert not any(low < value < upper for value, a, b in board(upper))
    for value, a, b in board(upper):
        if b == 0 and a >= 1:
            for event in (Fraction(value), Fraction(3*value, 2),
                          Fraction(6*value), Fraction(27*value, 4)):
                assert not low < event < upper
    adjusted = [counts[j] - isolates[j] - patches[j] for j in range(3)]
    if high:
        vertical = max((b for value, a, b in board(low) if a == 0))
        assert -vertical % 3 == last
        assert adjusted[last] > min(adjusted)
    else:
        cover = {2} if last == 1 else {3, 4}
        assert all(cover & {value, 2*value, 3*value}
                   for value, a, b in board(low) if 3*value <= low)
        assert min(adjusted) == last
    return {"interval": [str(low), str(upper)], "K": counts,
            "I": isolates, "P": patches, "adjusted": adjusted,
            "top_color" if high else "minimum_cover_size": last}


output = {"small_boards": [certify(row, False) for row in base_cases],
          "surviving_high_windows": [certify(row, True) for row in high_cases]}
Path(__file__).with_suffix(".json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
print("Verified eight exact base intervals and five high-window subintervals.")
