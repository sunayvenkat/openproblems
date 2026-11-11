"""Exact two-index response elimination; all affine denominators are charged."""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
import importlib.util


def load(name, relative):
    path = Path(__file__).resolve().parents[1] / relative
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


responses = load('responses', 'Erdos 168 response closure tests/response_relations_check.py')
models = load('models', 'Erdos 168 reflected return models/two_sided_models_check.py')


def birth(x, y, b):
    return (0 if b == 0 else int(x >= 1 and y >= 0) if b == 1
            else int(x <= -1 and x - y <= 0) if b == 2
            else int(min(x, 0) <= y) if b == 3 else int(x <= 0 and x - y <= 0))


def rectangle(aa, bb, events, width, height, bstart=0):
    total = 0
    for b in range(bstart, bstart + height):
        e = events[b] if b >= 4 else (0, 0)
        bx, by = bb[b][0] - 1 - e[0], bb[b][1] - e[1]
        row = 0
        for a in range(width):
            cx, cy = responses.CORRECTION[a % 3][b % 3]
            eta = birth(aa[a][0] + bx + cx, aa[a][1] + by + cy, b)
            row = 2 * row + 1 - 3 * eta
        total = 3 * total + row
    return F(total, 2 ** (width - 1) * 3 ** (height - 1))


def rational_model(p, q, sign):
    aa, bb = [(1, 0)], [(1, 0)]
    for a in range(1, 3 * q):
        aa.append(models.add(aa[-1], models.rot(((1, 0), (0, -1), (0, 0))[
            models.side(a, p, q, sign) % 3], -a)))
    for b in range(1, 3 * p + 4):
        bb.append(models.add(bb[-1], models.rot(((1, 0), (1, 1), (0, 0))[
            models.side(b, q, p, -sign) % 3], -2 * b)))
    events = [(0, 0)] * 4
    m = lambda b: models.side(b, q, p, -sign)
    for b in range(4, 3 * p + 4):
        isolated, patch = m(b) - m(b - 1) == 2, m(b - 1) - m(b - 3) == 4
        assert not (isolated and patch)
        events.append(models.rot((1, 0), m(b) - 2 * b) if isolated else
                      models.rot((1, 0), m(b - 1) - 1 - 2 * b) if patch else (0, 0))
    horizontal, vertical = 1 - F(1, 2 ** (3 * q)), 1 - F(1, 3 ** (3 * p))
    head = rectangle(aa, bb, events, 3 * q, 4)
    tile = rectangle(aa, bb, events, 3 * q, 3 * p, 4)
    return head / horizontal + tile / (81 * horizontal * vertical) - 1


def gap(r, s, sign):
    return sign * (3 ** r - 2 ** s), 2 ** s * 3 ** r


def primitive_pair(r1, s1, sign1, r2, s2, sign2):
    a1, k1 = gap(r1, s1, sign1)
    a2, k2 = gap(r2, s2, sign2)
    assert k2 % k1 == 0 and gcd(abs(a1 * a2), 6) == 1
    g = gcd(abs(a1), abs(a2))
    determinant = abs(s1 * r2 - s2 * r1)
    assert determinant and (2 ** determinant - 1) % g == (3 ** determinant - 1) % g == 0
    lam, mu = a2 // g, -a1 * (k2 // k1) // g
    assert gcd(abs(lam), abs(mu)) == 1
    assert lam * F(a1, k1) + mu * F(a2, k2) == 0
    return lam, mu, g, determinant


def log2_floor(value):
    assert value > 0
    result = value.numerator.bit_length() - value.denominator.bit_length()
    if value < F(2) ** result:
        result -= 1
    assert F(2) ** result <= value < F(2) ** (result + 1)
    return result


def run():
    # The integer Horner evaluator is checked against complete archived models.
    for p, q, sign in ((5, 8, 1), (12, 19, -1), (53, 84, -1)):
        assert rational_model(p, q, sign) == models.model(p, q, sign)[4]
    pairs = ((12, 19, -1, 53, 84), (306, 485, 1, 971, 1539))
    for p, q, sign, r, s in pairs:
        assert ((2 ** q > 3 ** p) - (2 ** q < 3 ** p)) == sign
        h = (0, 0)
        for a in range(s):
            h = models.add(h, models.rot((1, 0), a + (a * r) // s))
        assert (r % 3, s % 3, h) == (2, 0, (2, 1))
    lam, mu, g, determinant = primitive_pair(53, 84, -1, 971, 1539, 1)
    assert determinant == 3 and g == 1
    z1, z2 = [rational_model(p, q, sign) for p, q, sign, _, _ in pairs]
    common = lcm(z1.denominator, z2.denominator)
    m1, m2 = int(common * z1), int(common * z2)
    k, j = lam + mu, lam * m1 + mu * m2
    assert k and gcd(abs(k), abs(j)) == gcd(abs(k), abs(m1 - m2))
    prediction = F(j, k * common)
    assert prediction.denominator == abs(k) * common // gcd(abs(j), abs(k) * common)

    width, height = 1800, 1200
    aa, bb = responses.axes(max(width, height))
    events = [(0, 0)] * 4 + [responses.event(b) for b in range(4, height)]
    center = rectangle(aa, bb, events, width, height) - 1
    tail = 6 * (F(1, 2 ** width) + F(1, 3 ** height) - F(1, 2 ** width * 3 ** height))
    residual = k * center - F(j, common)
    radius = abs(k) * tail
    assert abs(residual) > radius + 1
    low, high = abs(residual) - radius, abs(residual) + radius
    cleared_low = prediction.denominator * low / abs(k)
    cleared_high = prediction.denominator * high / abs(k)
    assert cleared_low > 1
    print({'gap_determinant': determinant, 'gap_numerator_gcd': g,
           'primitive_coefficient_bits': (abs(lam).bit_length(), abs(mu).bit_length()),
           'model_denominator_bits': (z1.denominator.bit_length(), z2.denominator.bit_length()),
           'affine_prediction_denominator_bits': prediction.denominator.bit_length(),
           'primitive_residual_power_two_bounds': (log2_floor(low), log2_floor(high) + 1),
           'fully_cleared_error_power_two_bounds': (log2_floor(cleared_low), log2_floor(cleared_high) + 1)})
    print('PASS: same-state response elimination is exact but this complete return is large')


if __name__ == '__main__':
    run()
