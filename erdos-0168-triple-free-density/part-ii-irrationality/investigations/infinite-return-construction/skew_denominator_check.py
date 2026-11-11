"""Targeted certificates for the skew center and denominator obstruction."""
import sys
sys.dont_write_bytecode = True

from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "old_returns", ROOT / "research_notes/Erdos augmentation and return attacks/returns_check.py")
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    return z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0] - z[1]*w[1]


def divide(z, w):
    conjugate = w[0] - w[1], -w[1]
    norm = mul(w, conjugate)
    assert norm[1] == 0 and norm[0] > 0
    numerator = mul(z, conjugate)
    return F(numerator[0], norm[0]), F(numerator[1], norm[0])


def check_center(p, q):
    sigma = 1 if 2**q > 3**p else -1
    ha = hb = (0, 0)
    for k in range(1, q + 1):
        ha = add(ha, old.rot((1, 0), 2*old.floor_side(k, p, q, sigma) + 2 - k))
    for k in range(1, p + 1):
        hb = add(hb, old.rot((1, 0), old.floor_side(k, q, p, -sigma) + 1 - 2*k))
    rho = old.rot((1, 0), 2*p - q)
    inverse = old.rot((1, 0), q - 2*p)
    ca = divide((-ha[0], -ha[1]), mul((2, 1), (1-rho[0], -rho[1])))
    cb = divide((-hb[0], -hb[1]), mul((1, -1), (1-inverse[0], -inverse[1])))
    center = add((F(2, 3), 0), add(ca, cb))
    minus_center = ((p+q) % 3 == 1) == (sigma > 0)
    expected = (F(1, 3), F(-1, 3)) if minus_center else (F(2, 3), F(1, 3))
    assert center == expected, (p, q, center)


def cone(z):
    return int(z[0] <= 0 and z[0]-z[1] <= 0)


if __name__ == "__main__":
    # Independent arithmetic checks guard the coordinate operations.
    assert mul((0, 1), (0, 1)) == (-1, -1)
    assert divide((1, 0), (1, -1)) == (F(2, 3), F(1, 3))
    for p, q in ((5, 8), (12, 19), (53, 84)):
        check_center(p, q)
    for x in range(-2, 3):
        for y in range(-2, 3):
            assert cone((x, y)) + cone((-y, x-y-1)) + cone((y-x+1, -x)) == 1
            assert cone((x, y)) + cone((1-y, x-y)) + cone((y-x+1, 1-x)) == 1
    eta, _, _ = old.model(5, 8)
    skew = lambda a, b, j: sum(eta(a+i*8, b+((j-i) % 3)*5) for i in range(3))
    assert [skew(3, 0, 1), skew(0, 1, 0), skew(0, 3, 0)] == [0, 2, 2]
    rows = json.loads((ROOT / "research_notes/Erdos augmentation and return attacks/returns_check.json").read_text())
    for row, cancellation in zip(rows, (702, 3510, 6), strict=True):
        assert F(row["rational_model"]).denominator == int(row["clearing_denominator"]) // cancellation
    print("PASS: three centers; two affine cone partitions; low-column counterexamples; exact denominator cancellations 702, 3510, 6.")
