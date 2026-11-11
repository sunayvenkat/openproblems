"""Exact finite certificate checks; the general proof is in transfer.md."""

from heapq import heappop, heappush


def edge(x, y):
    return tuple(sorted((x, y)))


def mycielski_cycle(n):
    return ({edge(i, (i + 1) % n) for i in range(n)}
            | {edge(n + i, (i + sign) % n)
               for i in range(n) for sign in (-1, 1)}
            | {edge(2 * n, n + i) for i in range(n)})


def check_certificates(n, certificates):
    edges = mycielski_cycle(n)
    checked = set()
    for deleted, colors in certificates:
        for sign in (-1, 1):
            for shift in range(n):
                perm = [(sign * i + shift) % n for i in range(n)]
                perm += [n + (sign * i + shift) % n for i in range(n)]
                perm += [2 * n]
                assert {edge(perm[x], perm[y]) for x, y in edges} == edges
                moved = [None] * len(colors)
                for vertex, color in enumerate(colors):
                    moved[perm[vertex]] = color
                removed = edge(perm[deleted[0]], perm[deleted[1]])
                assert {e for e in edges if moved[e[0]] == moved[e[1]]} == {removed}
                checked.add(removed)
    assert checked == edges
    assert all(any(v in e for e in edges) for v in range(2 * n + 1))
    print(f"M(C{n}): all {len(edges)} edge-deletion certificates verified")


def conductor(generators):
    modulus = min(generators)
    distance = [float('inf')] * modulus
    distance[0] = 0
    queue = [(0, 0)]
    while queue:
        value, residue = heappop(queue)
        if value != distance[residue]:
            continue
        for generator in generators:
            candidate = value + generator
            target = candidate % modulus
            if candidate < distance[target]:
                distance[target] = candidate
                heappush(queue, (candidate, target))
    assert all(value < float('inf') for value in distance)
    return max(distance) - modulus + 1


check_certificates(5, [
    ((0, 1), (1, 1, 0, 1, 0, 2, 2, 2, 1, 2, 0)),
    ((5, 1), (0, 1, 0, 1, 2, 1, 1, 2, 1, 2, 0)),
    ((10, 5), (0, 1, 0, 1, 2, 0, 1, 2, 1, 2, 0)),
])
check_certificates(3, [
    ((0, 1), (2, 2, 0, 1, 1, 0, 2)),
    ((3, 1), (0, 1, 2, 1, 1, 2, 0)),
    ((6, 3), (0, 1, 2, 0, 1, 2, 0)),
])
assert conductor((3, 5)) == 8
assert conductor((4, 7)) == 18
for g in range(4, 129):
    a, b, c = 5 * g - 2, 9 * g - 4, 19 * g - 9
    base = 6 * g - 2
    if g % 2:
        bound = base + (a - 1) * (b - 1)
        assert bound == 45 * g * g - 46 * g + 13
        assert bound - a == 45 * g * g - 51 * g + 15
    else:
        bound = base + c + 2 * (a // 2 - 1) * (b // 2 - 1)
        assert bound == 45 * g * g // 2 - 8 * g + 1
        assert bound - a == 45 * g * g // 2 - 13 * g + 3
    assert base + conductor((a, b, c)) <= bound <= 45 * g * g
    d, e = 4 * g - 2, 11 * g - 5
    optional = (20 * g * g - 21 * g + 7 if g % 2
                else 10 * g * g - g + 1)
    assert base + conductor((a, d, e)) <= optional <= 20 * g * g
print("Exact semigroup conductors and threshold identities checked for 4 <= g <= 128")
