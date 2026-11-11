"""Exact checks for the finite high-case comparisons and prefix repair."""
import json
from fractions import Fraction
from pathlib import Path


def points(t):
    out = []
    power3 = 1
    b = 0
    while power3 <= t:
        value = power3
        a = 0
        while value <= t:
            out.append((value, a, b))
            value *= 2
            a += 1
        power3 *= 3
        b += 1
    return sorted(out)


def indicators(t):
    isolated = [0, 0, 0]
    patch = [0, 0, 0]
    roots = []
    value, a = 1, 0
    while value <= t:
        if 3 * value > 2 * t:
            isolated[a % 3] += 1
            roots.append(("isolate", value))
        if a >= 1 and 6 * value <= t and 4 * t < 27 * value:
            patch[a % 3] += 1
            roots.append(("patch", value))
        value *= 2
        a += 1
    assert sum(isolated) + sum(patch) <= 1
    return isolated, patch, roots


def counts(t):
    result = [0, 0, 0]
    for _, a, b in points(t):
        result[(a - b) % 3] += 1
    return result


def row_counts(t):
    result = [0, 0, 0]
    power3, b = 1, 0
    while power3 <= t:
        maximum_a = (t // power3).bit_length() - 1
        for j in range(3):
            r = (j + b) % 3
            if r <= maximum_a:
                result[j] += (maximum_a - r) // 3 + 1
        power3 *= 3
        b += 1
    return result


def events(lo, hi):
    out = {Fraction(lo), Fraction(hi)}
    out.update(Fraction(v) for v, _, _ in points(hi) if lo <= v <= hi)
    value, a = 1, 0
    while value <= hi:
        out.add(Fraction(3 * value, 2))
        if a >= 1:
            out.update((Fraction(6 * value), Fraction(27 * value, 4)))
        value *= 2
        a += 1
    return sorted(x for x in out if lo <= x <= hi)


def finite_cases():
    expected = [
        (6, 8, 2, [2, 1, 2], [0, 0, 0], [0, 0, 0]),
        (8, 9, 2, [3, 1, 2], [1, 0, 0], [0, 0, 0]),
        (24, 27, 1, [3, 4, 4], [0, 0, 0], [0, 0, 1]),
        (54, 64, 0, [6, 5, 5], [0, 0, 0], [0, 0, 0]),
        (64, 72, 0, [7, 5, 5], [1, 0, 0], [0, 0, 0]),
        (216, 243, 2, [9, 8, 9], [0, 0, 0], [0, 0, 0]),
        (576, 648, 1, [12, 12, 11], [1, 0, 0], [0, 0, 0]),
        (5184, 5832, 2, [20, 19, 20], [1, 0, 0], [0, 0, 0]),
    ]
    output = []
    for lo, hi, top, K, I, P in expected:
        assert events(lo, hi) == [lo, hi]
        for t in (Fraction(lo), Fraction(lo + hi, 2)):
            assert counts(t) == K
            assert indicators(t)[:2] == (I, P)
        assert row_counts(lo) == K
        Q = [K[j] - I[j] - P[j] for j in range(3)]
        assert Q[top] > min(Q)
        output.append({"interval": [lo, hi], "top": top, "K": K,
                       "I": I, "P": P, "adjusted": Q})
    return output


def prefix_geometry(s):
    t = 64 * 9 ** (s - 1)
    A, k0 = s + 2, 2 * s + 4
    j = A % 3
    board = {(a, b): v for v, a, b in points(t)}
    P = {p for p in board if (p[0] - p[1]) % 3 == j
         and 2 * p[0] + p[1] <= k0 - 3}
    R = {p for p in board if (p[0] - p[1]) % 3 == (j + 1) % 3
         and 2 * p[0] + p[1] <= k0 - 4}
    y = (0, 2 * s + 1)
    frontier = {(s + 1 - n, 2 * n + 1) for n in range(s)}
    assert y in P and frontier <= set(board)
    assert len(P) - len(R) - 1 == (s + 2) // 3 - 1
    for a, b in P - {y}:
        endpoints = []
        if b >= 1:
            endpoints.append((a, b - 1))
        if a >= 1 and (a - 1, b + 1) in board:
            endpoints.append((a - 1, b + 1))
        if (a, b + 1) in board:
            endpoints.append((a + 1, b))
        assert set(endpoints) <= R | frontier
    for _, e in indicators(t)[2]:
        assert e not in {board[p] for p in P}
    return {"s": s, "prefix": len(P), "repair": len(R),
            "gain": len(P) - len(R) - 1}


def base_boards():
    rows = []
    cuts = events(3, 18)
    for lo, hi in zip(cuts, cuts[1:]):
        board = points(lo)
        labels = {v for v, _, _ in board}
        corners = [{v, 2 * v, 3 * v} for v in labels if 3 * v <= lo]
        I, P, _ = indicators(lo)
        K = counts(lo)
        M = min(K[j] - I[j] - P[j] for j in range(3))
        witness = {2} if lo < 9 else {3, 4}
        assert witness <= labels and all(witness & c for c in corners)
        assert len(witness) == M
        if M == 2:
            assert not set.intersection(*corners)
        else:
            assert M == 1 and corners
        rows.append({"interval": [str(lo), str(hi)], "K": K,
                     "I": I, "P": P, "M": M, "cover": sorted(witness)})
    return rows


if __name__ == "__main__":
    t = 64 * 9**16
    assert counts(t) == row_counts(t) == [354, 354, 354]
    I, P, roots = indicators(t)
    assert I == [0, 0, 0] and P == [1, 0, 0]
    assert roots == [("patch", 2**54)]
    output = {
        "finite_cases": finite_cases(),
        "prefix_checks": [prefix_geometry(s) for s in (2, 3, 4, 17)],
        "base_boards": base_boards(),
        "large_raw_tie": {"s": 17, "t": t, "top": 1, "K": counts(t),
                          "I": I, "P": P, "adjusted": [353, 354, 354],
                          "patch_root": 2**54},
    }
    Path(__file__).with_suffix(".json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print({"finite_case_intervals": len(output["finite_cases"]),
           "prefix_samples": [2, 3, 4, 17],
           "base_intervals": len(output["base_boards"]),
           "large_raw_tie_adjusted": [353, 354, 354]})

