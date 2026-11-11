"""Exact toric-division arithmetic and localized pole certificates; no scans."""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import importlib.util


def load_models():
    path = Path(__file__).resolve().parents[1] / 'Erdos 168 reflected return models/two_sided_models_check.py'
    spec = importlib.util.spec_from_file_location('archived_models', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def coefficient_denominator(u, v, a, b, k):
    """Exact reduced denominator for X^a Y^b (1-Y^3)/(X-Y)^k."""
    axis_denominator = u ** max(a - k, 0) * v ** max(b + 3 - k, 0)
    toric_denominator = abs(u - v) ** k
    cancellation = gcd(axis_denominator * toric_denominator, v ** 3 - 1)
    return axis_denominator * toric_denominator // cancellation


def audit_case(module, p, q, expected_ratio, expected_bits):
    plus, minus = module.model(p, q, 1), module.model(p, q, -1)
    u, v = 2 ** q, 3 ** p
    clearing = 27 * (u ** 3 - 1) * (v ** 3 - 1)
    jump = plus[4] - minus[4]
    integer_jump = clearing * jump
    assert integer_jump.denominator == 1
    assert integer_jump.numerator % (u - v) == 0
    divided_numerator = integer_jump.numerator // (u - v)
    quotient = jump / (F(1, u) - F(1, v))
    assert quotient == F(-u * v * divided_numerator, clearing)
    assert (clearing * quotient).denominator == 1
    assert quotient.denominator == clearing // gcd(clearing, u * v * divided_numerator)
    assert clearing // quotient.denominator == expected_ratio
    assert quotient.denominator.bit_length() == expected_bits

    # These named cases include both signs of monomial exponents and k>3.
    # The general asymptotic assertion is proved in the note, not by this list.
    x, y = F(1, u), F(1, v)
    examples = [(0, 0, 0), (1, 0, 1), (2, 0, 2), (3, 0, 3),
                (4, 0, 4), (5, -4, 1), (-2, 3, 1)]
    for a, b, k in examples:
        coefficient = x ** a * y ** b * (1 - y ** 3) / (x - y) ** k
        assert coefficient.denominator == coefficient_denominator(u, v, a, b, k)
        assert gcd(abs(u-v), v ** 3 - 1) <= gcd(u ** 3 - 1, v ** 3 - 1)
        assert gcd(abs(u-v) ** k, v ** 3 - 1) <= gcd(abs(u-v), v ** 3 - 1) ** k
    balanced = [x ** k * (1 - y ** 3) / (x - y) ** k for k in range(5)]
    balanced_bits = [value.denominator.bit_length() for value in balanced]
    balanced_height_bits = [max(abs(value.numerator), value.denominator).bit_length()
                            for value in balanced]

    # Old residue matrices retain rank after adjoining toric-divided columns.
    # The exact column relation uses the invertible element 2-zeta.
    for root, zeta in [('1', (1, 0)), ('omega', (0, 1))]:
        rows = list(module.root_rows(p, q, (plus, minus), 'v', root))
        basis = module.eisenstein_basis(rows)
        assert len(basis) == 4
        divisor = module.add((2, 0), (-zeta[0], -zeta[1]))
        for _, row in basis:
            q0 = module.divide(module.add(row[0], (-row[2][0], -row[2][1])), divisor)
            q1 = module.divide(module.add(row[1], (-row[3][0], -row[3][1])), divisor)
            assert module.mul(divisor, q0) == module.add(row[0], (-row[2][0], -row[2][1]))
            assert module.mul(divisor, q1) == module.add(row[1], (-row[3][0], -row[3][1]))
        extended = [(label, row + [module.divide(module.add(row[0], (-row[2][0], -row[2][1])), divisor),
                                  module.divide(module.add(row[1], (-row[3][0], -row[3][1])), divisor)])
                    for label, row in rows]
        # This helper stops at six columns only if the rank really reaches six.
        assert len(module.eisenstein_basis(extended)) == 4

    print({'p': p, 'q': q,
           'toric_quotient_denominator_bits': quotient.denominator.bit_length(),
           'nominal_over_quotient_denominator': expected_ratio,
           'gcd_toric_integer_factor_with_nominal': gcd(abs(u-v), clearing),
           'balanced_axis_factor_denominator_bits_k_0_through_4': balanced_bits,
           'balanced_axis_factor_height_bits_k_0_through_4': balanced_height_bits,
           'vertical_localized_rank': 4})


if __name__ == '__main__':
    module = load_models()
    audit_case(module, 5, 8, 486, 44)
    audit_case(module, 53, 84, 1458, 499)
    print('PASS: exact toric division retains the named axis arithmetic')
