"""Exact operator boundaries, actual column-head costs and rank-coupling checks."""

from fractions import Fraction as F
from pathlib import Path
import json


def times(P, Q):
    answer = {}
    for (a, b), c in P.items():
        for (aa, bb), cc in Q.items():
            key = a+aa, b+bb
            answer[key] = answer.get(key, 0)+c*cc
    return answer


def operator(q, p):
    return {(2*q, 0): 1, (q, p): 1, (0, 2*p): 1}


def evaluate(P):
    return sum(c*2**a*3**b for (a, b), c in P.items())


def weighted(d):
    return sum((F(c, 2**a*3**b) for (a, b), c in d.items()), F())


def apply(P, d):
    width = max(a for a, b in d)+1
    height = max(b for a, b in d)+1
    return {(a, b): sum(c*d.get((a+aa, b+bb), 0) for (aa, bb), c in P.items())
            for a in range(width) for b in range(height)}


def boundary_kernel(P, a, b):
    return sum((F(c*2**aa*3**bb, 2**a*3**b)
                for (aa, bb), c in P.items() if a < aa or b < bb), F())


def boundary(P, d):
    return sum((c*boundary_kernel(P, a, b) for (a, b), c in d.items()), F())


d = {(a, b): (3*a+2*b) % 5-2 for a in range(9) for b in range(8)}
for q1, p1, q2, p2 in ((1, 1, 3, 2), (2, 1, 5, 3)):
    L1, L2 = operator(q1, p1), operator(q2, p2)
    P = times(L1, L2)
    assert evaluate(P)*weighted(d) == boundary(P, d)+weighted(apply(P, d))
    assert boundary(P, d) == evaluate(L2)*boundary(L1, d)+boundary(L2, apply(L1, d))
    assert apply(P, d) == apply(L2, apply(L1, d))
    A, B = 2*(q1+q2), 2*(p1+p2)
    for b in (B, B+1, B+3):
        assert boundary_kernel(P, A-1, b) == F(2, 3**b)


def tau(t):
    counts = [0, 0, 0]
    two, a = 1, 0
    while two <= t:
        three, b = 1, 0
        while two*three <= t:
            counts[(a-b) % 3] += 1
            three *= 3
            b += 1
        two *= 2
        a += 1
    root, a = 2, 1
    while root <= t:
        if 2*t < 3*root or 6*root <= t and 4*t < 27*root:
            counts[a % 3] -= 1
        root *= 2
        a += 1
    return min(counts)


# Actual high-column coefficients, not freely chosen digits.
P = times(operator(1, 1), operator(3, 2))
head = F()
for b in range(12):
    value = 3**(b+4)
    digit = 1-3*(tau(value)-tau(value-1))
    assert digit in (1, -2)
    head += digit*boundary_kernel(P, 0, b)
    assert head.denominator == 3**b


# Existing audited 53/84 value remains uncleared by the specified two-factor repair.
source = Path(__file__).resolve().parents[1]/'Erdos augmentation and return attacks'/'returns_check.json'
rows = json.loads(source.read_text())
row = next(row for row in rows if row['q'] == 84)
value, nominal = F(row['rational_model']), int(row['clearing_denominator'])
assert value.denominator == nominal//6
candidate = 27*evaluate(operator(8, 5))*evaluate(operator(84, 53))
assert candidate < value.denominator
assert (candidate*value).denominator > 1
print({'two_factor_candidate_bits': candidate.bit_length(),
       'existing_model_reduced_denominator_bits': value.denominator.bit_length()})


# Equal rational color marginals do not determine the rank-coupled minimum.
A = ((2, 12), (6, 9), (6, 9))
B = ((3, 4), (6, 9), (6, 9))
assert [sum((F(1, t) for t in row), F()) for row in A] == [sum((F(1, t) for t in row), F()) for row in B]
cost = lambda rows: sum((F(1, max(triple)) for triple in zip(*rows)), F())
assert cost(A) == F(1, 4) and cost(B) == F(5, 18)
print('PASS: two-level boundaries, actual column heads through12, model repair, finite rank example.')
