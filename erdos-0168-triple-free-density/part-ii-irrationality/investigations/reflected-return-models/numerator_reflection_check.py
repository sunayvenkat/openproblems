"""Exact targeted checks of opposite-side tile reflection; no density decimals."""
import sys
sys.dont_write_bytecode = True

from fractions import Fraction
from math import gcd
from pathlib import Path
import importlib.util
import json


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def neg(z):
    return -z[0], -z[1]


def conj(z):
    return z[0] - z[1], -z[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0] - z[1]
    return z


def floor_side(n, p, q, sign):
    quotient, remainder = divmod(n * p, q)
    return quotient - int(remainder == 0 and sign < 0)


def cone(z):
    return int(z[0] <= 0 and z[0] - z[1] <= 0)


S = ((1, 0), (0, -1), (0, 0))
T = ((1, 0), (1, 1), (0, 0))
C = (((0, 0), (0, 0), (0, 0)),
     ((0, 0), (1, 0), (1, 1)),
     ((0, 0), (0, -1), (1, 0)))


def model(p, q, sign):
    assert gcd(p, q) == 1 and (p + q) % 3
    assert Fraction(3, 5) < Fraction(p, q) < Fraction(2, 3)
    P, Q = 3 * q, 3 * p
    A, B = [(1, 0)], [(1, 0)]
    for k in range(1, P + 1):
        A.append(add(A[-1], rot(S[floor_side(k, p, q, sign) % 3], -k)))
    for k in range(1, Q + 1):
        B.append(add(B[-1], rot(T[floor_side(k, q, p, -sign) % 3], -2 * k)))
    assert A[P] == B[Q] == (1, 0)

    def state(a, b):
        return add(add(add(A[a % P], B[b % Q]), (-1, 0)), C[a % 3][b % 3])

    def correction(b):
        # Periodically extend the valid high-row rule, including to reflected axes.
        b = b % Q + Q
        m = lambda k: floor_side(k, q, p, -sign)
        isolated = m(b) - m(b - 1) == 2
        patch = m(b - 1) - m(b - 3) == 4
        assert not (isolated and patch)
        if isolated:
            return rot((1, 0), m(b) - 2 * b)
        if patch:
            return rot((1, 0), m(b - 1) - 1 - 2 * b)
        return 0, 0

    def reflected_correction(b):
        m = lambda k: floor_side(k, q, p, -sign)
        isolated = m(b + 2) - m(b + 1) == 2
        patch = m(b + 4) - m(b + 2) == 4
        assert not (isolated and patch)
        if isolated:
            return rot((1, 0), m(b + 1) - 2 * b - 1)
        if patch:
            return rot((1, 0), m(b + 2) - 2 * b)
        return 0, 0

    def high(a, b):
        return 1 - 3 * cone(add(state(a, b), neg(correction(b))))

    def coefficient(a, b):
        x, y = state(a, b)
        if b == 0:
            eta = 0
        elif b == 1:
            eta = int(x >= 1 and y >= 0)
        elif b == 2:
            eta = int(x <= -1 and x - y <= 0)
        elif b == 3:
            eta = int(min(x, 0) <= y)
        else:
            return high(a, b)
        return 1 - 3 * eta

    U, V = 2 ** P, 3 ** Q
    H = sum(coefficient(a, b) * 2 ** (P - a) * 3 ** (3 - b)
            for a in range(P) for b in range(4))
    J = sum(high(a, b + 4) * 2 ** (P - a) * 3 ** (Q - b)
            for a in range(P) for b in range(Q))
    D = 27 * (U - 1) * (V - 1)
    assert J % 3 == 0
    N = H * (V - 1) + J // 3 - D
    return A, B, state, correction, high, coefficient, N, D, reflected_correction


def valuation(n, prime):
    assert n
    power = 0
    while n % prime == 0:
        power += 1
        n //= prime
    return power


if __name__ == "__main__":
    # Independent small coordinate and rational-sum checks.
    assert conj((2, 3)) == (-1, -3) and conj(conj((2, 3))) == (2, 3)
    assert rot((0, 1), 1) == (-1, -1)
    assert all(cone((x, y)) == cone(conj((x, y)))
               for x in range(-2, 3) for y in range(-2, 3))
    for x in range(-2, 3):
        for y in range(-2, 3):
            rays = (-int(x - 1 == min(y, 0)), int(x == y and x <= 0),
                    int(x == 0 and y >= 0))
            for j in range(3):
                assert 1 - 3 * cone(add((x, y), neg(rot((1, 0), j)))) == (
                    1 - 3 * cone((x, y)) + 3 * rays[j])
    root = Path(__file__).resolve().parents[2]
    spec = importlib.util.spec_from_file_location(
        "old_returns", root / "research_notes/Erdos augmentation and return attacks/returns_check.py")
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    results = []
    for p, q in ((5, 8), (12, 19), (53, 84)):
        P, Q = 3 * q, 3 * p
        plus, minus = model(p, q, 1), model(p, q, -1)
        sigma = 1 if 2 ** q > 3 ** p else -1
        actual, opposite = (plus, minus) if sigma > 0 else (minus, plus)
        for sign, current, reflected in ((1, plus, minus), (-1, minus, plus)):
            A, B, state, correction, high = current[:5]
            for a in range(P):
                assert A[a] == add(conj(reflected[0][P - 1 - a]),
                                   add(S[a % 3], (-int(sign > 0), 0)))
            for b in range(Q):
                assert current[8](b) == conj(reflected[3](Q - 1 - b))
                assert B[b] == add(conj(reflected[1][Q - 1 - b]),
                                   add(T[b % 3], (-int(sign < 0), 0)))
                for a in range(P):
                    ar, br = P - 1 - a, Q - 1 - b
                    assert state(a, b) == conj(reflected[2](ar, br))
                    da = add(A[a], neg(A[(a - 1) % P]))
                    db = add(B[b], neg(B[(b - 1) % Q]))
                    dc = add(C[a % 3][b % 3], neg(C[(a - 1) % 3][(b - 1) % 3]))
                    assert add(state(a, b), neg(conj(reflected[2](P - a, Q - b)))) == (
                        add(add(da, db), dc))
                    assert high(a, b) - reflected[4](ar, br) == -3 * (
                        cone(add(state(a, b), neg(correction(b)))) -
                        cone(add(state(a, b), neg(conj(reflected[3](br))))))
        old_eta, old_value, old_D = old.model(p, q)
        assert Fraction(actual[6], actual[7]) == old_value and actual[7] == old_D
        assert all(actual[5](a, b) == 1 - 3 * old_eta(a, b, False)
                   for a in range(P) for b in range(Q + 4))
        U, V = 2 ** P, 3 ** Q
        W = sum(actual[4](a, b) * 2 ** (P - 1 - a) * 3 ** (Q - 1 - b)
                for a in range(P) for b in range(Q))
        low = sum((actual[5](a, b) - actual[4](a, b)) *
                  2 ** (P - 1 - a) * 3 ** (3 - b)
                  for a in range(P) for b in range(4))
        assert actual[6] == 162 * W + 2 * low * (V - 1) - old_D
        opposite_positive = sum(opposite[4](a, b) * 2 ** a * 3 ** b
                                for a in range(P) for b in range(Q))
        ray_difference = sum((actual[4](a, b) - opposite[4](P - 1 - a, Q - 1 - b)) *
                             2 ** (P - 1 - a) * 3 ** (Q - 1 - b)
                             for a in range(P) for b in range(Q))
        assert W == opposite_positive + ray_difference and ray_difference % 3 == 0
        witnesses = [(a, b, actual[4](a, b), opposite[4](P - 1 - a, Q - 1 - b),
                      list(actual[2](a, b)), list(actual[3](b)),
                      list(conj(opposite[3](Q - 1 - b))))
                     for b in range(4, Q - 4) for a in range(P)
                     if actual[4](a, b) != opposite[4](P - 1 - a, Q - 1 - b)]
        results.append({"p": p, "q": q, "sigma": sigma,
                        "high_reflection_failure": witnesses[0] if witnesses else None,
                        "nominal_numerator_v2_v3": [valuation(actual[6], r) for r in (2, 3)],
                        "denominator_v2_v3": [valuation(actual[7], r) for r in (2, 3)],
                        "nominal_cancellation": gcd(actual[6], actual[7])})
    # Palindromic alphabet-{1,-2} periodic tiles can approach rational zero
    # without acquiring growing 2-adic or 3-adic divisibility of the numerator.
    for n in (0, 1, 2):
        P, Q = 6 * n + 3, 6 * n + 6
        U, V = 2 ** P, 3 ** Q
        tile = lambda a, b: -2 if (a, b) in ((0, 0), (P - 1, Q - 1)) else 1
        numerator = -3 * (U + V + 5)
        assert all(tile(a, b) == tile(P - 1 - a, Q - 1 - b)
                   for a in range(P) for b in range(Q))
        assert sum(Fraction(tile(a, b), 2 ** a * 3 ** b)
                   for a in range(P) for b in range(Q)) / (
                       (1 - Fraction(1, U)) * (1 - Fraction(1, V))) == Fraction(
                           numerator, (U - 1) * (V - 1))
        assert valuation(numerator, 2) == valuation(numerator, 3) == 1
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))
    print("PASS: opposite-side state reciprocity; exact corrected discrepancy; saved model values; palindromic countermodel.")
