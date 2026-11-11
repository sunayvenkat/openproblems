"""Exact named-model hybrid intervals; run with Python -B. No density decimals."""
from fractions import Fraction as F
from functools import cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


old = Path(__file__).resolve().parents[1] / "Erdos 168 reflected return models/two_sided_models_check.py"
spec = spec_from_file_location("paired_certificate", old)
paired = module_from_spec(spec)
spec.loader.exec_module(paired)
ZERO, ONE = (0, 0), (1, 0)
C = ((ZERO, ZERO, ZERO), (ZERO, ONE, (1, 1)), (ZERO, (0, -1), ONE))


@cache
def floor_power(n, source, target):
    value, exponent = source**n, 0
    while target**(exponent + 1) <= value:
        exponent += 1
    return exponent


def axis(limit, floor, vertical=False):
    states = [ONE]
    table = (ONE, (1, 1), ZERO) if vertical else (ONE, (0, -1), ZERO)
    for k in range(1, limit + 1):
        states.append(paired.add(states[-1], paired.rot(table[floor(k) % 3], -2*k if vertical else -k)))
    return states


def coefficient(A, B, a, b, reciprocal, origin=False):
    x, y = paired.add(paired.add(A, B), C[a % 3][b % 3])
    x -= 1
    if b == 0:
        eta = 0
    elif b == 1:
        eta = 1 if origin and a == 0 else int(x >= 1 and y >= 0)
    elif b == 2:
        eta = int(x <= -1 and x-y <= 0)
    elif b == 3:
        eta = int(min(x, 0) <= y)
    else:
        isolated = reciprocal(b) - reciprocal(b-1) == 2
        patch = reciprocal(b-1) - reciprocal(b-3) == 4
        assert not (isolated and patch)
        E = paired.rot(ONE, reciprocal(b)-2*b) if isolated else paired.rot(ONE, reciprocal(b-1)-1-2*b) if patch else ZERO
        eta = int(x <= E[0] and x-y <= E[0]-E[1])
    return 1-3*eta


def check(p, q):
    sign = 1 if 2**q > 3**p else -1
    AM, BM, event, eta, MM = paired.model(p, q, sign)
    P, Q = 3*q, 3*p
    U, V = 2**P, 3**Q
    D = 27*(U-1)*(V-1)
    extra = 30 if (p, q) == (5, 8) else 240
    A_cut, B_cut = 6*q+extra, 6*p+extra
    true_h = lambda a: floor_power(a, 2, 3)
    true_v = lambda b: floor_power(b, 3, 2)
    model_h = lambda a: paired.side(a, p, q, sign)
    model_v = lambda b: paired.side(b, q, p, -sign)
    AT, BT = axis(A_cut, true_h), axis(B_cut, true_v, True)
    R, S = q+(19 if q == 8 else 485), p+(12 if q == 8 else 306)
    assert all(true_h(a) == model_h(a) for a in range(R))
    assert all(true_v(b) == model_v(b) for b in range(S))
    assert true_h(R) != model_h(R) and true_v(S) != model_v(S)

    def row(B, b, reciprocal):
        S = sum(coefficient(AM[a], B, a, b, reciprocal)*2**(P-1-a) for a in range(P))
        assert -2*(U-1) <= S <= U-1 and (S-(U-1)) % 3 == 0
        return F(2*S, U-1)

    def column(A, a, origin=False):
        low = sum((F(coefficient(A, BM[b], a, b, model_v, origin), 3**b) for b in range(4)), F(0))
        high = sum((F(coefficient(A, BM[(4+r) % Q], a, 4+r, model_v), 3**(4+r))
                    for r in range(Q)), F(0))
        result = low + high / (1-F(1, V))
        assert (27*(V-1)*result).denominator == 1
        assert -81*(V-1) <= 27*(V-1)*result <= F(81*(V-1), 2)
        return result

    # Both independent one-axis resummations recover the complete old model.
    MM_rows = sum((row(BM[b], b, model_v)/3**b for b in range(4)), F(0))
    MM_rows += sum((row(BM[(4+r) % Q], 4+r, model_v)/3**(4+r) for r in range(Q)), F(0))/(1-F(1, V))
    MM_rows -= 1
    MM_columns = sum((column(AM[a], a)/2**a for a in range(P)), F(0))/(1-F(1, U))-1
    assert MM_rows == MM_columns == MM

    MT_partial = sum((row(BT[b], b, true_v)/3**b for b in range(B_cut)), F(0))-1
    TM_partial = sum((column(AT[a], a, True)/2**a for a in range(A_cut)), F(0))
    partial = MT_partial + TM_partial-MM
    weight = F(1, 3**B_cut)+F(1, 2**A_cut)
    lower, upper = D*(partial-6*weight), D*(partial+3*weight)
    integer_part = lower.numerator//lower.denominator
    assert integer_part < lower < upper < integer_part+1
    scale = 2**20
    lower_tick = ((lower-integer_part)*scale).numerator//((lower-integer_part)*scale).denominator
    upper_tick = -((-((upper-integer_part)*scale).numerator)//((upper-integer_part)*scale).denominator)
    assert F(lower_tick, scale) < lower-integer_part
    assert upper-integer_part < F(upper_tick, scale)
    print(f"p/q={p}/{q}; D={D}; cutoffs=({A_cut},{B_cut})")
    print(f"floor(DJ)={integer_part}; fractional part strictly between {lower_tick}/{scale} and {upper_tick}/{scale}")
    print(f"interval width < 1/{(upper-lower).denominator//(upper-lower).numerator}; DJ is not an integer")
    model_integer = D*MM
    assert model_integer.denominator == 1
    mixed = D*F(18, 2**R*3**S)
    gap_lower, gap_upper = lower-model_integer, upper-model_integer
    print(f"floor(DJ)-D*Z_MM={integer_part-model_integer}")
    print("actual Z-Z_MM certified sign:", "positive" if gap_lower-mixed > 0 else "negative" if gap_upper+mixed < 0 else "not certified")
    if q == 84:
        assert -F(1, 2**60) < gap_lower < gap_upper < -F(1, 2**100)
        assert gap_upper+mixed < 0
        print("-2^-60 < D*(J-Z_MM) < -2^-100; any rational DJ has reduced denominator > 2^60")
    else:
        assert gap_lower-mixed > 0
        conjugate = lambda z: (z[0]-z[1], -z[1])
        table = (((2, 0), (2, 1), ONE), ((2, 1), (1, 1), ONE), (ONE, ONE, ONE))
        boundary = [(a, true_h(a)) for a in range(41)] + [(true_v(b), b) for b in range(26)]
        for a, b in boundary:
            assert paired.add(BT[b], conjugate(AT[a])) == table[a % 3][b % 3]

        def corrected(a, b):
            x, y = paired.add(paired.add(AT[a], BT[b]), C[a % 3][b % 3])
            isolated = true_v(b)-true_v(b-1) == 2
            patch = true_v(b-1)-true_v(b-3) == 4
            E = paired.rot(ONE, true_v(b)-2*b) if isolated else paired.rot(ONE, true_v(b-1)-1-2*b) if patch else ZERO
            return x-1-E[0], y-E[1]

        states = tuple(corrected(a, b) for a, b in ((0, 4), (1, 4), (0, 5), (1, 5)))
        assert states == ((0, 0), (0, -1), (0, 0), (0, 0))
        mu = lambda z: min(z[0], z[1], 0)
        assert 3*mu(states[1])+2*mu(states[2])+mu(states[3])-6*mu(states[0]) == -3
        cone = lambda x, y: int(x <= 0 and x <= y)
        for x in range(-4, 5):
            for y in range(-4, 5):
                assert cone(x, y)-cone(x, y-1)-cone(x-1, y-1)+cone(x-1, y-2) == -int(x == y == 1)
        print("PASS: exact merged-boundary reciprocity, actual discounted-potential defect, and localized cone curvature")


if __name__ == "__main__":
    check(5, 8)
    check(53, 84)
