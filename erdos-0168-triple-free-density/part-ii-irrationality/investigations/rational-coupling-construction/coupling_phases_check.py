"""Exact phase averaging and one-block folding; reuses the certified template."""
from fractions import Fraction as F
from pathlib import Path
import runpy

base = runpy.run_path(str(Path(__file__).with_name("rational_templates_check.py")))
arrival, skew_template = base["arrival"], base["skew_template"]
V, delta = F(3, 13), F(1, 27)


def v2(value):
    numerator, denominator = abs(value.numerator), value.denominator
    assert numerator
    return ((numerator & -numerator).bit_length()-1
            - ((denominator & -denominator).bit_length()-1))


for a in (0, 1, 2, 8, 19):
    for m in (0, 1):
        points = [(a, 3*m+r) for r in range(3)]
        assert sorted((x-y) % 3 for x, y in points) == [0, 1, 2]
        assert max(arrival(x, y) for x, y in points) == 9*27**m*2**a

head = [(a, b) for a in (0, 1) for b in range(3)]
head_opt = sum((1/t for t in base["optimal_maxima"](head, arrival)), F())
assert head_opt - F(1, 6) == F(2, 9)
assert F(1, 6) * F(2, 9) == delta
assert F(2, 3) * (F(1, 3)-F(1, 9)) == F(4, 27)

for p, q in ((5, 8), (12, 19)):
    u, v = 2**q, 3**p
    q0, _, maxima0, maximainf, ms = skew_template(p, q)
    oi = sum((1/t for t in maximainf), F())
    qi = q0-delta
    s = 1/ms[0]+F(1, 3)/ms[1]+F(1, 6)/ms[2]
    q1, q2 = V+(qi-V)/u, V+(qi-V)/u**2
    mean = (q0+q1+q2)/3
    assert mean == V*(1-F(u*u+u+1, 3*u*u)) + F(u, 3*(u-1))*oi + F(2, 3)*s + F(1, 81)
    folded = oi+delta+F(2*(u-1), u)*s+V/u**3
    assert folded == q0-(qi-V)/u**3
    assert qi >= F(8, 27) > V
    assert folded < q0
    weight = F(1, u*u*(u-1))
    assert 0 < weight < 1
    assert folded == (1-weight)*q0+weight*(q1+delta)
    assert (1053*u*u*v*v*(u-1)*mean).denominator == 1
    assert (351*u**3*v*v*folded).denominator == 1
    assert v2(q0) >= 0
    assert q >= 4 and v*v <= F(9, 8)*u*u
    assert ms[0] == F(3, 2)*u*u and ms[1] == F(9, 8)*u*u
    expected_mean = 3-2*q if u > v else -2*q
    expected_fold = 3-3*q if u > v else -3*q
    assert v2(mean) == expected_mean
    assert v2(folded) == expected_fold
    print({"phase": (p, q), "mean_cost": str(mean),
           "mean_denominator": mean.denominator, "mean_v2": v2(mean),
           "folded_cost": str(folded), "folded_denominator": folded.denominator,
           "folded_v2": v2(folded), "original_minus_folded": str(q0-folded)})
print("PASS: phase ownership inputs, fixed head repair, exact costs and dyadic tradeoffs")
