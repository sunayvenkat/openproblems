"""Exact certificates for the specific vertical-critical lemmas and obstructions."""
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "existing_boundary_checker",
    HERE.parent / "Erdos 168 boundary and arithmetic" / "dual_check.py",
)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def value(point):
    a, b = point
    return 2**a * 3**b


def board(t):
    return {(a, b) for a in range(t.bit_length()) for b in range(t.bit_length())
            if 2**a * 3**b <= t}


def graph(owners, points):
    return [edge for owner in owners for edge in checker.owned_edges(owner, points)]


def matching_pairs(edges):
    return sorted((value(left), value(right))
                  for right, left in checker.matching(edges).items())


def certify_critical(t, values, cover):
    points = board(t)
    owners = {u for u in points if value(u) in values}
    assert len(owners) == len(values)
    edges = graph(owners, points)
    matching = matching_pairs(edges)
    assert len(matching) == len(owners) - 1 == len(cover)
    assert all(value(left) in cover or value(right) in cover for left, right in edges)
    labels = sorted(owners)
    for mask in range(1 << len(labels)):
        if mask == (1 << len(labels)) - 1:
            continue
        subset = {labels[i] for i in range(len(labels)) if mask >> i & 1}
        assert len(checker.matching(graph(subset, points))) >= len(subset)
    return {"t": t, "owners": sorted(values), "cover": sorted(cover),
            "matching": matching, "all_proper_subsets_checked": 2**len(labels)-1}


def critical_lists_216():
    points = board(216)
    output = []
    for color in range(3):
        labels = sorted(u for u in points if (u[0]-u[1]) % 3 == color)
        critical = []
        for mask in sorted(range(1, 1 << len(labels)), key=int.bit_count):
            owners = {labels[i] for i in range(len(labels)) if mask >> i & 1}
            if any(previous <= owners for previous in critical):
                continue
            if len(checker.matching(graph(owners, points))) < len(owners):
                critical.append(owners)
        output.append({"color": color, "K": len(labels),
                       "critical": sorted(sorted(map(value, U)) for U in critical)})
    assert [len(row["critical"]) for row in output] == [1, 0, 3]
    return output


def filling_obstruction():
    points = board(1536)
    colors = [{u for u in points if (u[0]-u[1]) % 3 == j} for j in range(3)]
    F = ({value(u) for u in colors[2]} - {256, 1152, 1536}) | {384, 512}
    assert len(F) == 14
    assert all({value(u), 2*value(u), 3*value(u)} & F
               for u in points if 3*value(u) <= 1536)
    full_matching = matching_pairs(graph(colors[0], points))
    assert len(colors[0]) == len(full_matching) == 15
    U = {u for u in colors[0] if value(u) not in F}
    W = F - {value(u) for u in colors[0]}
    edges = graph(U, points)
    partial_matching = matching_pairs(edges)
    assert len(U) == 13 and len(W) == len(partial_matching) == 12
    assert all(value(left) in W or value(right) in W for left, right in edges)
    return {"t": 1536, "cover_F": sorted(F), "owners_U": sorted(map(value, U)),
            "cover_W": sorted(W), "matching_U": partial_matching,
            "matching_full_C0": full_matching, "d_U": 1, "d_full_C0": 0}


if __name__ == "__main__":
    cases = [
        certify_critical(6, {3, 4}, {2}),
        certify_critical(24, {9, 12, 16}, {6, 8}),
        certify_critical(54, {8, 27, 36, 48}, {12, 16, 18}),
        certify_critical(216, {32, 81, 108, 144, 192}, {48, 54, 64, 72}),
        certify_critical(216, {1, 6, 27, 36, 162, 216}, {2, 9, 12, 54, 72}),
        certify_critical(576, {16, 72, 96, 243, 324, 432, 576},
                         {24, 32, 108, 144, 162, 192}),
    ]
    result = {"critical_certificates": cases, "critical_lists_216": critical_lists_216(),
              "full_class_filling_obstruction": filling_obstruction()}
    (HERE / "vertical_critical_check.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print({"critical_certificates": len(cases), "t216_counts": [1, 0, 3],
           "full_class_filling_deficiencies": [1, 0]})
