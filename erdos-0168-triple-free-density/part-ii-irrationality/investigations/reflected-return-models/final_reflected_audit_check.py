"""Independent synthetic-min and rotation-center certificates; run Python -B."""
from fractions import Fraction as F
from functools import lru_cache
from importlib.util import spec_from_file_location, module_from_spec
from itertools import permutations
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("paired_model", HERE / "two_sided_models_check.py")
paired = module_from_spec(spec)
spec.loader.exec_module(paired)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0] - z[1] * w[1]


def scale(z, k):
    return k * z[0], k * z[1]


def divide(z, w):
    numerator = mul(z, (w[0] - w[1], -w[1]))
    norm = w[0] ** 2 - w[0] * w[1] + w[1] ** 2
    return F(numerator[0], norm), F(numerator[1], norm)


UNITS = ((1, 0), (0, 1), (-1, -1))


@lru_cache(None)
def adjusted(p, q, sign, a, b):
    """Count synthetic ordered vertices directly; no optimum or axis formula."""
    grade = p * a + q * b

    def comparison(i, j):
        delta = p * i + q * j - grade
        return (delta > 0) - (delta < 0) if delta else sign * ((i > a) - (i < a))

    counts = [0, 0, 0]
    for i in range(grade // p + 1):
        for j in range((grade - p * i) // q + 1):
            if comparison(i, j) <= 0:
                counts[(i - j - a + b) % 3] += 1
    before = counts.copy()
    before[0] -= 1
    after = counts.copy()
    for root in range(1, grade // p + 4):
        color = (root - a + b) % 3
        for entry, exit in (((root, 0), (root - 1, 1)),
                            ((root + 1, 1), (root - 2, 3))):
            start, stop = comparison(*entry), comparison(*exit)
            before[color] -= int(start < 0 and stop >= 0)
            after[color] -= int(start <= 0 and stop > 0)
    return min(after) - min(before), (after[0] - after[2], after[1] - after[2])


def determinant(rows):
    result = (0, 0)
    for perm in permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        product = (1, 0)
        for i, j in enumerate(perm):
            product = mul(product, rows[i][j])
        result = add(result, scale(product, (-1) ** inversions))
    return result


assert mul((0, 1), (0, 1)) == (-1, -1)
assert divide((1, 0), (1, -1)) == (F(2, 3), F(1, 3))
assert determinant([[(int(i == j), 0) for j in range(4)] for i in range(4)]) == (1, 0)

for sign in (1, -1):
    model = paired.model(5, 8, sign)
    for a in range(25):
        for b in range(19):
            assert adjusted(5, 8, sign, a, b)[0] == model[3](a, b), (sign, a, b)
    assert adjusted(5, 8, sign, 0, 0)[0] == 0
    assert adjusted(5, 8, sign, 0, 1)[0] == 1

# Nonnegative residue bases remain independent even when y^p-zeta is reducible.
# The named minors are reconstructed from synthetic adjusted color counts.
witnesses = {
    (5, 8, 0): ((0, 4), (0, 5), (0, 8), (1, 4)),
    (5, 8, 1): ((0, 4), (0, 5), (0, 6), (1, 4)),
    (53, 84, 0): ((0, 4), (0, 8), (1, 4), (2, 4)),
    (53, 84, 1): ((0, 4), (0, 8), (0, 11), (1, 4)),
}
for (p, q, root), labels in witnesses.items():
    models = [paired.model(p, q, sign) for sign in (1, -1)]
    rows = []
    for a, b in labels:
        row = []
        for sign, model in zip((1, -1), models):
            center = (F(1, 3), F(-1, 3)) if ((p + q) % 3 == 1) == (sign > 0) else (F(2, 3), F(1, 3))
            for color in (0, 1):
                value = (0, 0)
                for i in range(3):
                    for j in range(3):
                        aa, bb = a + i * q, b + j * p
                        digit, z = adjusted(p, q, sign, aa, bb)
                        shifted = add(center, mul(UNITS[color], add(z, scale(center, -1))))
                        cone = int(shifted[0] <= 0 and shifted[0] <= shifted[1])
                        assert digit == model[3](aa, bb)
                        assert cone == model[3](aa, bb, color)
                        value = add(value, scale(UNITS[(root * j) % 3], (1 - 3 * cone) * 2 ** i))
                row.append(value)
        rows.append(row)
    det = determinant(rows)
    assert det != (0, 0)
    print((p, q), "vertical root exponent", root, "minor determinant", det)

# All admissible nonresonant phase/digit/parity cases: normalize old centers 0,1.
for parity in (0, 1):
    for r in (UNITS[1], UNITS[2]):
        for previous in (UNITS[1], UNITS[2]):
            for digit in range(3):
                power = (1, 0)
                for _ in range(digit):
                    power = mul(power, r)
                phase = mul(power, previous)
                if phase == (1, 0):
                    continue
                translated = add((1, 0), scale(power, -1))
                offset = translated if parity == 0 else mul(previous, translated)
                center = divide(offset, add((1, 0), scale(phase, -1)))
                difference = add(center, (-1, 0))
                assert difference[0] ** 2 - difference[0] * difference[1] + difference[1] ** 2 == 1
                copied_centers = ((1, 0), translated) if parity == 0 else ((0, 0), previous)
                for copied in copied_centers:
                    gap = add(center, scale(copied, -1))
                    assert gap[0] ** 2 - gap[0] * gap[1] + gap[1] ** 2 <= 1

print("PASS: direct synthetic minimum gives all retained low rows and origin; four vertical minors; nonresonant center/radius cases.")
