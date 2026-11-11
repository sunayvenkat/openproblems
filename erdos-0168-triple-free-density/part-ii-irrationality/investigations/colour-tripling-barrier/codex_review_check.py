"""Bounded exact checks for the new Claude report; not a global proof audit."""
from fractions import Fraction as Fr
from functools import lru_cache
from math import gcd
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
W = [(1, 0), (0, 1), (-1, -1)]
S = [(1, 0), (0, -1), (0, 0)]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def mul(a, b):
    x, y = a
    u, v = b
    return x * u - y * v, x * v + y * u - y * v


def wp(n):
    return W[n % 3]


def geo(n):
    return [(0, 0), wp(-1), add(wp(-1), wp(-2))][n % 3]


def actual_axis(n):
    floors = [0]
    axis = [(1, 0)]
    power2 = power3 = 1
    b = 0
    for i in range(1, n + 1):
        power2 *= 2
        while 3 * power3 <= power2:
            power3 *= 3
            b += 1
        floors.append(b)
        axis.append(add(axis[-1], mul(wp(-i), S[b % 3])))
    return floors, axis


floors, axis = actual_axis(1600)
for p, q, next_q in [(12, 19, 65), (41, 65, 84), (53, 84, 485), (306, 485, 1054)]:
    cp = (0, 0)
    for k in range(p):
        cp = add(cp, wp(2 * k))
    u = wp(2 * p - q)
    for a in range(next_q):
        predicted = add(axis[q], add(mul(u, sub(axis[a], (1, 0))),
                                     mul(mul(cp, wp(-q)), geo(a))))
        assert predicted == axis[a + q], (p, q, a)
    predicted = add(axis[q], add(mul(u, sub(axis[next_q], (1, 0))),
                                 mul(mul(cp, wp(-q)), geo(next_q))))
    assert predicted != axis[next_q + q]
    safe = max(0, next_q - 2 * q)
    for a in range(safe):
        assert axis[a + 3 * q] == axis[a]
    print(f"actual affine shift {p}/{q}: valid a<{next_q}; guaranteed 3q window length {safe}")

# A minimal digit period does not force the full nominal denominator.
x = Fr(7, 2**6 - 1)
assert x == Fr(1, 9)
assert next(k for k in range(1, 7) if pow(2, k, x.denominator) == 1) == 6
print("period-versus-denominator check: minimal binary period 6, reduced denominator 9, not 63")


@lru_cache(None)
def cyclotomic_value(n, base):
    value = base**n - 1
    for d in range(1, n):
        if n % d == 0:
            divisor = cyclotomic_value(d, base)
            assert value % divisor == 0
            value //= divisor
    return value


sys.path.insert(0, str(HERE))
from modelval import val

for p, q, expected_loss in [(11, 17, 103), (33, 52, 1249)]:
    phi_h = cyclotomic_value(3 * q, 2)
    phi_v = cyclotomic_value(3 * p, 3)
    minus = val(p, q, -1)
    plus = val(p, q, 1)
    loss = phi_h // gcd(phi_h, minus.denominator)
    assert loss == expected_loss
    assert minus.denominator % phi_v == 0
    assert plus.denominator % phi_h == 0
    assert plus.denominator % phi_v == 0
    assert 2**q < 3**p
    print(f"cyclotomic example {p}/{q}: minus loses {loss}; plus retains both tested factors")

# These slopes are not actual convergents: earlier denominators give strictly
# better second-kind approximation, using an integer-certified alpha enclosure.
lo_alpha, hi_alpha = Fr(6309, 10000), Fr(631, 1000)
assert 2**10000 > 3**6309 and 2**1000 < 3**631
assert max(abs(8 * lo_alpha - 5), abs(8 * hi_alpha - 5)) < 11 - 17 * hi_alpha
assert max(abs(19 * lo_alpha - 12), abs(19 * hi_alpha - 12)) < 33 - 52 * hi_alpha
print("both exceptional tested slopes are upper approximants, not actual convergents")


def cf(x, limit=400):
    result = []
    for _ in range(limit):
        a = x.numerator // x.denominator
        result.append(a)
        x -= a
        if not x:
            break
        x = 1 / x
    return result


def common_prefix(a, b):
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]:
        n += 1
    return a[:n]


sys.path.insert(0, str(ROOT / "research_notes" / "Erdos 168 part i consolidation"))
from c_digits import enclosure

lo, hi, *_ = enclosure(10**130)
certified = common_prefix(cf(9 * lo - 6), cf(9 * hi - 6))
assert len(certified) == 127 and max(certified) == 283
print("Z interval: 127 certified common CF terms, maximum partial quotient 283")

# Add a complete infinite tail before interpreting the toy's rational truncation.
n = 400
toy = sum((Fr(1, 3**b * 2**((3**b).bit_length() - 1)) for b in range(n)), Fr(0))
toy_tail = Fr(9, 4 * 9**n)
toy_raw = cf(toy, 60)
toy_certified = common_prefix(toy_raw, cf(toy + toy_tail, 60))
print("toy: common CF terms certified by complete tail", len(toy_certified))
print("toy: largest raw quotient bit length", max(toy_raw).bit_length(),
      "; largest certified quotient bit length", max(toy_certified).bit_length())
print("PASS: bounded algebra and numerical claims checked; no infinite supply or irrationality established")
