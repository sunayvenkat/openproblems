"""Exact, dependency-free certificate for the failed weak spanning claim."""
import json
from pathlib import Path

T = 729
GROUPS = ({6, 8, 27, 48, 288}, {16, 72, 243, 324}, {4, 18, 81, 486})
MATCHINGS = (
    ((2, 4), (9, 3), (12, 18), (16, 32), (72, 24), (54, 81),
     (96, 192), (432, 144)),
    ((24, 8), (32, 48), (108, 36), (144, 216), (81, 162), (486, 729)),
    ((6, 2), (8, 12), (27, 9), (36, 54), (162, 324), (729, 243)),
)
STEPS = {(1, 1), (-1, -1), (2, -1), (-2, 1), (-1, 2), (1, -2)}


def exponents(u):
    a = b = 0
    while u % 2 == 0:
        a, u = a + 1, u // 2
    while u % 3 == 0:
        b, u = b + 1, u // 3
    assert u == 1
    return a, b


def certificate(groups):
    selected = set.union(*groups)
    assert all(not {u, 2 * u, 3 * u} <= selected for u in selected)
    answer = []
    for j, (group, matching) in enumerate(zip(groups, MATCHINGS)):
        coordinates = {exponents(u) for u in group}
        assert all(0 < u <= T and (a - b) % 3 == j
                   for u in group for a, b in [exponents(u)])
        assert any(a == 0 and b > 0 for a, b in coordinates)
        assert any(b == 0 and a > 0 for a, b in coordinates)
        assert any(3 * u > T for u in group)
        reached = {next(iter(coordinates))}
        while True:
            expanded = reached | {p for p in coordinates
                                  if any((p[0] - q[0], p[1] - q[1]) in STEPS
                                         for q in reached)}
            if expanded == reached:
                break
            reached = expanded
        assert reached == coordinates
        edges = set()
        for u in group:
            if u % 3 == 0:
                edges.add((u // 3, 2 * u // 3))
            if u % 2 == 0 and 3 * u <= 2 * T:
                edges.add((3 * u // 2, u // 2))
            if 3 * u <= T:
                edges.add((2 * u, 3 * u))
        left = {l for l, r in edges}
        right = {r for l, r in edges}
        assert set(matching) <= edges
        assert len({l for l, r in matching}) == len(matching)
        assert len({r for l, r in matching}) == len(matching)
        assert len(matching) == min(len(left), len(right))
        answer.append({'j': j, 'labels': sorted(group), 'left_size': len(left),
                       'right_size': len(right), 'matching': matching,
                       'matching_number': len(matching),
                       'deficiency': len(group) - len(matching)})
    return answer


if __name__ == '__main__':
    answer = {'t': T, 'origin_free_witness': certificate(GROUPS),
              'with_origin_added': certificate((GROUPS[0] | {1}, *GROUPS[1:]))}
    assert [x['deficiency'] for x in answer['origin_free_witness']] == [-3, -2, -2]
    assert [x['deficiency'] for x in answer['with_origin_added']] == [-2, -2, -2]
    Path(__file__).with_suffix('.json').write_text(json.dumps(answer, indent=2) + '\n')
    print('Exact independence, three boundary contacts, connectivity, and matching certificates passed.')
    print('Origin-free deficiencies: -3, -2, -2. With origin added: -2, -2, -2.')
