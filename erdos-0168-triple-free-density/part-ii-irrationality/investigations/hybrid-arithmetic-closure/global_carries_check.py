"""Exact certificate for grade reversal and the corrected retimed-token process."""
from fractions import Fraction as F
from itertools import permutations, product
import importlib.util
import sys

sys.dont_write_bytecode = True


def shifted(q, v):
    return tuple(a + b for a, b in zip(q, v))


def births(q, colors, reverse=False):
    state, answer = list(q), [0] * len(colors)
    indices = range(len(colors)-1, -1, -1) if reverse else range(len(colors))
    for i in indices:
        before = min(state)
        state[colors[i]] += 1
        answer[i] = min(state) - before
    return answer


def cyclic_gap(q, size, prefix):
    s, r = size % 3, prefix % 3
    if r == 0 or r == s:
        return 0
    if s == 0 and r == 1:
        return int(q[0] == min(q[1], q[2]))
    if s == 0 and r == 2:
        return int(q[2] == min(q[0], q[1]))
    if s == 1 and r == 2:
        return int(q[1] == q[2] <= q[0])
    assert s == 2 and r == 1
    return int(q[0] == q[1] < q[2])


cyclic_checks = balanced_checks = 0
for q in product(range(-2, 3), repeat=3):
    for size in range(1, 15):
        word = [i % 3 for i in range(size)]
        forward, reverse = births(q, word), births(q, word, True)
        gaps = [sum(reverse[:k])-sum(forward[:k]) for k in range(1, size+1)]
        assert gaps == [cyclic_gap(q, size, k) for k in range(1, size+1)]
        for ratio in (F(1, 2), F(2, 3)):
            direct = sum((ratio**i * (reverse[i]-forward[i]) for i in range(size)), F())
            telescoped = (1-ratio)*sum((gaps[k-1]*ratio**(k-1) for k in range(1, size)), F())
            assert direct == telescoped >= 0
        cyclic_checks += 1
    for word in set(permutations((0, 0, 1, 1, 2, 2))):
        forward, reverse = births(q, word), births(q, word, True)
        for k in range(1, 7):
            n = tuple(word[:k].count(j) for j in range(3))
            expected = 2*min(q)-min(shifted(q, n))-min(shifted(q, tuple(-a for a in n)))
            assert sum(reverse[:k])-sum(forward[:k]) == expected >= 0
        balanced_checks += 1


def points(t):
    answer, power2, a = [], 1, 0
    while power2 <= t:
        power3, b = 1, 0
        while power2*power3 <= t:
            answer.append((power2*power3, a, b))
            power3 *= 3
            b += 1
        power2 *= 2
        a += 1
    return sorted(answer)


def adjusted_counts(t):
    counts = [0, 0, 0]
    for _, a, b in points(t):
        counts[(a-b) % 3] += 1
    root, a = 2, 1
    while root <= t:
        if 2*t < 3*root <= 3*t or 6*root <= t and 4*t < 27*root:
            counts[a % 3] -= 1
        root *= 2
        a += 1
    return tuple(counts)


def retimed_counts(t):
    counts = [0, 0, 0]
    for value, a, b in points(t):
        arrival = F(3*2**(a-1)) if b == 0 and a >= 1 else F(27*2**a, 8) if b == 1 and a >= 2 else F(value)
        if arrival <= t:
            counts[(a-b) % 3] += 1
    return tuple(counts)


cutoffs = tuple(map(F, (1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 36, 48, 54, 728, 729, 768, 177147, 186624, 196608))) + (F(27, 2), F(1349, 100))
for t in cutoffs:
    assert retimed_counts(t) == adjusted_counts(t)
assert adjusted_counts(F(1349, 100)) == (3, 2, 2)
assert adjusted_counts(F(27, 2)) == (3, 3, 2)
assert F(3)-F(1, 3)-F(1, 54) == F(143, 54)

path = 'research_notes/Erdos 168 reflected return models/two_sided_models_check.py'
spec = importlib.util.spec_from_file_location('paired_model', path)
paired = importlib.util.module_from_spec(spec)
spec.loader.exec_module(paired)
plus, minus = paired.model(5, 8, 1), paired.model(5, 8, -1)
for grade, colors, expected in ((48, (0, 0), F(13, 186624)),
                                 (88, (1, 2, 2), -F(13, 45349632))):
    chain = [(a, (grade-5*a)//8) for a in range(grade//5+1) if (grade-5*a) % 8 == 0]
    values = [2**a*3**b for a, b in chain]
    assert values == sorted(values)
    assert [v for v, _, _ in points(values[-1]) if v >= values[0]] == values
    q = adjusted_counts(values[0]-1)
    forward, reverse = births(q, colors), births(q, colors, True)
    assert forward == [plus[3](a, b) for a, b in chain]
    assert reverse == [minus[3](a, b) for a, b in chain]
    assert forward == [min(adjusted_counts(v))-min(adjusted_counts(v-1)) for v in values]
    difference = sum((F(f-r, v) for f, r, v in zip(forward, reverse, values)), F())
    assert difference == expected
    print('actual grade', grade, 'initial Q', q, 'colors', colors, 'eta +/-', forward, reverse, 'weighted difference', difference)
assert -(plus[4]-minus[4])/3 == F(25199209663, 249993707168205) > 0
print('PASS:', cyclic_checks, 'cyclic words;', balanced_checks, 'balanced words;', len(cutoffs), 'retimed cutoffs; exact low-grade obstructions.')
