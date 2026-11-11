"""Integer diagonal DP for #168; independently check a boundary-patch candidate.

This verifies finite instances only. It does not prove the candidate for all t,
nor the irrationality conjecture. The published comparison data use Gurobi.
"""
import heapq
import json
from pathlib import Path


def smooth_prefix(count):
    queue = [(1, 0, 0)]
    seen = {1}
    points = []
    for _ in range(count):
        v, a, b = heapq.heappop(queue)
        points.append((v, a, b))
        for w, i, j in ((2*v, a+1, b), (3*v, a, b+1)):
            if w not in seen:
                seen.add(w)
                heapq.heappush(queue, (w, i, j))
    return points


def exact_tau(points):
    """Exact min cover, using only Python integers and exhaustive DP states."""
    layers = {}
    for _, a, b in points:
        layers.setdefault(a+b, []).append(a)
    top = max(layers)
    left = min(layers[top])
    width = len(layers[top])
    dp = [mask.bit_count() for mask in range(1 << width)]
    for k in range(top-1, -1, -1):
        next_left, next_width = left, width
        left = min(layers[k])
        width = len(layers[k])
        assert sorted(layers[k]) == list(range(left, k+1))
        mandatory_cost = [len(points)+1] * (1 << width)
        for upper, cost in enumerate(dp):
            # Two adjacent undeleted children force their lower parent deleted.
            missing = (~(upper | (upper >> 1))) & ((1 << (next_width-1))-1)
            required = missing << (next_left-left)
            mandatory_cost[required] = min(mandatory_cost[required], cost)
        # Each current mask may contain any mandatory mask included in it.
        for bit in range(width):
            step = 1 << bit
            for mask in range(1 << width):
                if mask & step:
                    mandatory_cost[mask] = min(mandatory_cost[mask], mandatory_cost[mask ^ step])
        dp = [mask.bit_count()+mandatory_cost[mask] for mask in range(1 << width)]
    return min(dp)


def candidate_tau(points):
    t = points[-1][0]
    if t < 3:
        return 0
    counts = [sum((a+2*b) % 3 == c for _, a, b in points) for c in range(3)]
    a = t.bit_length()-1
    if 3*(1 << a) > 2*t:
        counts[a % 3] -= 1  # Unique isolated pure power of 2.
    a = (t//6).bit_length()-1
    if a >= 1 and 4*t < 27*(1 << a):
        counts[a % 3] -= 1  # Replace {x,9x/2,6x} by {3x/2,2x}.
    return min(counts)


if __name__ == '__main__':
    directory = Path(__file__).parent
    points = smooth_prefix(5000)
    certificate = json.loads((directory/'168_1536_simple_dual.json').read_text())
    numerators = {int(v): w for v, w in certificate['rootNumerators'].items()}
    denominator = certificate['denominator']
    assert sum(numerators.values()) == 53 and denominator == 4
    assert all(v*3 <= 1536 for v in numerators)
    for n, _, _ in points[:45]:
        assert sum(w for v, w in numerators.items() if n in (v, 2*v, 3*v)) <= denominator
    cover = {3,4,18,24,32,81,108,144,192,384,486,512,648,864}
    assert len(cover) == 14
    assert all({v,2*v,3*v} & cover for v, _, _ in points[:45] if 3*v <= 1536)
    exact = []
    for k in range(1, 121):
        tau = exact_tau(points[:k])
        candidate = candidate_tau(points[:k])
        assert tau == candidate, (k, points[k-1][0], tau, candidate)
        exact.append({'k': k, 't': points[k-1][0], 'tau': tau})
    hits = [int(line.split()[1]) for line in
            (directory/'168_oeis_full_first_hits.txt').read_text().splitlines()
            if line and not line.startswith('#')]
    f = 0
    mismatches = []
    for k in range(1, 5001):
        if f < len(hits) and hits[f] == k:
            f += 1
        candidate = k-candidate_tau(points[:k])
        if candidate != f:
            mismatches.append({'k': k, 't': points[k-1][0], 'published': f, 'candidate': candidate})
    result = {'exactDp': exact, 'exact1536Certificate': '53/4 > 13, and size-14 cover',
              'publishedPrefixesCompared': 5000,
              'publishedMismatches': mismatches}
    (directory/'168_exact_diagonal_results.json').write_text(json.dumps(result, indent=2))
    print(json.dumps({'exactDpPrefixes': len(exact), 'lastExact': exact[-1],
                      'publishedPrefixesCompared': 5000, 'publishedMismatches': mismatches[:5]}))
