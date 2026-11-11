"""Exact fan coefficient arithmetic and the newly resonant response interface."""
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd, lcm
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load(name, relative):
    spec = spec_from_file_location(name, ROOT / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rr = load('accepted_responses', 'research_notes/Erdos 168 response closure tests/response_relations_check.py')
models = load('accepted_models', 'research_notes/Erdos 168 reflected return models/two_sided_models_check.py')


def valuation(value, prime):
    result = 0
    while value and value % prime == 0:
        value //= prime
        result += 1
    return result


def coefficients(p, q, pp, qq):
    a, b, u, v = 2**q, 3**p, 2**qq, 3**pp
    return tuple(F(a**(3-j), u*(a**3-1)) - F(b**(3-j), v*(b**3-1))
                 for j in (1, 2, 3))


def arithmetic_checks():
    for p, q, pp, qq, side in ((12, 19, 41, 65, -1),
                                (53, 84, 306, 485, -1),
                                (306, 485, 665, 1054, 1)):
        a, b, u, v = 2**q, 3**p, 2**qq, 3**pp
        aa, bb = a**3-1, b**3-1
        cc = coefficients(p, q, pp, qq)
        x, y = F(1, a), F(1, b)
        assert cc == tuple(F(1, u)*x**j/(1-x**3)-F(1, v)*y**j/(1-y**3)
                           for j in (1, 2, 3))
        den = cc[2].denominator
        assert valuation(den, 2) == qq and valuation(den, 3) == pp
        a0, b0 = aa // 3**valuation(aa, 3), bb // 2**valuation(bb, 2)
        cross = gcd(a0, b0)
        assert den % (u*v*(a0//cross)*(b0//cross)) == 0
        common = lcm(*(value.denominator for value in cc))
        assert (u*v*aa*bb) % common == 0
        assert common % den == 0
        scaled_majorant = F(common, 2**(q+2*qq))
        assert scaled_majorant > 2**(4*q)
        z = models.model(p, q, side)[4]
        n = z * (27*aa*bb)
        assert n.denominator == 1
        # The signs are deliberately arbitrary here: this is a denominator identity,
        # not a claim that the trial rational vector equals the actual responses.
        for h in ((1, 1, 1), (1, -1, 0), (1, 0, 0), (0, 0, 1), (1, 2, -3)):
            poly = lambda t: h[0]*t*t+h[1]*t+h[2]
            value = sum((h[j]*cc[j] for j in range(3)), F(0))
            numerator = v*bb*poly(a)-u*aa*poly(b)
            assert value == F(numerator, u*v*aa*bb)
            full_numerator = u*v*int(n)+27*side*numerator
            full_denominator = 27*u*v*aa*bb
            prediction = z+side*value
            assert prediction == F(full_numerator, full_denominator)
            assert prediction.denominator == full_denominator//gcd(abs(full_numerator), full_denominator)
        print('FAN_COEFFICIENTS', (p, q), 'C3_bits', den.bit_length(),
              'vector_common_bits', common.bit_length())


def resonant_interface():
    width = 96
    axes = rr.axes(width)
    new_states = ((1, 2, (1, 0)), (2, 1, (1, 0)))
    displacements = (((0, 0), (1, 0), (0, -1)),
                     ((0, 0), (1, 1), (1, 0)))
    for a in range(width):
        for b in range(width):
            z = rr.sub(rr.add(rr.add(axes[0][a], axes[1][b]),
                             rr.CORRECTION[a % 3][b % 3]), (1, 0))
            if b >= 4:
                z = rr.sub(z, rr.event(b))
            birth = lambda t: int(t[0] <= 0 and t[0]-t[1] <= 0) if b >= 4 else rr.low_eta(t, b)
            for state, ds in zip(new_states, displacements):
                plus = rr.add(z, ds[(a-b) % 3])
                expected = -3*(birth(plus)-birth(rr.sub(plus, (1, 0))))
                assert rr.response(state, a, b, *axes)[0] == expected
    def candidates():
        for a in range(32):
            for b in range(4, width):
                row = [1, rr.original_c(a, b)]
                row += [rr.response(state, a, b, *axes)[0] for state in rr.STATES+new_states]
                yield (a, b), row
    chosen = rr.basis_rows(candidates())
    assert len(chosen) == 8
    determinant = rr.determinant([row for _, row in chosen])
    assert determinant
    print('RESONANT_INTERFACE_ROWS', [point for point, _ in chosen])
    print('RESONANT_INTERFACE_DETERMINANT', determinant)


if __name__ == '__main__':
    arithmetic_checks()
    resonant_interface()
    print('PASS: complete fan coefficient and affine gcd identities; resonant displacement and rank8')
