"""One exact test of whether the one-step boundary signature closes twice."""
import itertools
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True


def powers(p, bound):
    result = []
    value = 1
    while value <= bound:
        result.append(value)
        value *= p
    return result


def run_cost(word):
    return sum((len(run) + 1) // 2 for run in "".join(map(str, word)).split("1"))


def initial_parity(word):
    return next((i % 2 for i, bit in enumerate(word) if bit), len(word) % 2)


def signature(cover, outer_t):
    horizontal = [int(n in cover) for n in powers(2, outer_t // 6)]
    vertical = [int(n in cover) for n in powers(3, outer_t // 9)]
    return (len(cover), run_cost(horizontal), run_cost(vertical),
            initial_parity(horizontal), initial_parity(vertical))


def extension(cover, outer_t):
    size, horizontal, vertical, h_parity, v_parity = signature(cover, outer_t)
    return horizontal + vertical + int(h_parity == v_parity == 0)


points24 = sorted({u * v for u in powers(2, 24) for v in powers(3, 24) if u*v <= 24})
axes24 = sorted(set(powers(2, 24) + powers(3, 24)))
corners24 = [{u, 2*u, 3*u} for u in points24 if 3*u <= 24]
results = []
for inner in ({2}, {3}):
    candidates = []
    for bits in itertools.product((0, 1), repeat=len(axes24)):
        cover = {6*n for n in inner} | {n for n, bit in zip(axes24, bits) if bit}
        if all(cover & corner for corner in corners24):
            candidates.append((len(cover) + extension(cover, 144), len(cover), sorted(cover)))
    best = min(candidates)
    assert min(item[1] for item in candidates) == len(inner) + extension(inner, 24)
    results.append({"inner_cover": sorted(inner), "one_step_signature": signature(inner, 24),
                    "two_step_total": best[0], "intermediate_cover": best[2],
                    "intermediate_size": best[1], "valid_intermediate_covers": len(candidates)})
assert results[0]["one_step_signature"] == results[1]["one_step_signature"]
def endpoint_matrix(word):
    matrix = [[0, 1000], [1000, 0]]
    for bit in word:
        step = [[0 if bit else 1000, 1], [0, 1]]
        matrix = [[min(matrix[i][k] + step[k][j] for k in range(2))
                   for j in range(2)] for i in range(2)]
    return matrix


def next_response(word):
    result = [1000, 1000]
    witnesses = [None, None]
    for bits in itertools.product((0, 1), repeat=len(word) + 1):
        if all(bit + bits[i] + bits[i+1] >= 1 for i, bit in enumerate(word)):
            cost = sum(bits) + run_cost(bits)
            if cost < result[bits[0]]:
                result[bits[0]] = cost
                witnesses[bits[0]] = bits
    return result, witnesses


def color(n):
    a = b = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    while n % 3 == 0:
        n //= 3
        b += 1
    assert n == 1
    return (a-b) % 3


points64 = {u*v for u in powers(2, 64) for v in powers(3, 64) if u*v <= 64}
inner_covers = [{3, 6, 8, 9, 12, 18, 24, 36, 48, 54},
                {2, 3, 6, 8, 9, 12, 24, 32, 36, 48}]
vertical_word = [0, 1, 1, 0]
vertical_response, _ = next_response(vertical_word)
assert vertical_response == [4, 4]
matrix_cases = []
for inner, expected in zip(inner_covers, ([7, 7], [7, 6])):
    assert all(inner & {u, 2*u, 3*u} for u in points64 if 3*u <= 64)
    counts = [sum(color(n) == j for n in inner) for j in range(3)]
    assert counts == [4, 3, 3]
    horizontal_word = [int(n in inner) for n in powers(2, 64)]
    assert [int(n in inner) for n in powers(3, 384//9)] == vertical_word
    matrix = endpoint_matrix(horizontal_word)
    assert matrix == [[4, 4], [3, 3]]
    horizontal_response, _ = next_response(horizontal_word)
    assert horizontal_response == expected
    two_step = len(inner) + min(horizontal_response[h] + vertical_response[v]
                               + 1 + int(h == v) for h in (0, 1) for v in (0, 1))
    matrix_cases.append({"inner_cover": sorted(inner), "color_counts": counts,
                         "horizontal_word": horizontal_word, "horizontal_matrix": matrix,
                         "one_step_total": len(inner) + extension(inner, 384),
                         "horizontal_response": horizontal_response,
                         "two_step_total": two_step})
assert [row["two_step_total"] for row in matrix_cases] == [22, 21]
assert endpoint_matrix(vertical_word) == [[2, 2], [1, 1]]
output = {"inner_t": 4, "middle_t": 24, "outer_t": 144, "cases": results,
          "matrix_counterexample": {"inner_t": 64, "middle_t": 384, "outer_t": 2304,
                                     "vertical_word": vertical_word,
                                     "vertical_response": vertical_response,
                                     "cases": matrix_cases}}
Path(__file__).with_suffix(".json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
print(json.dumps(output, indent=2))
