"""One exact adversarial actual-convergent bracket check: p/q=12/19."""
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


path = Path(__file__).with_name("hybrid_compression_check.py")
spec = spec_from_file_location("hybrid_certificate", path)
h = module_from_spec(spec)
spec.loader.exec_module(h)
p, q = 12, 19
# This exact continued-fraction cylinder contains the logarithmic slope.
assert 2**27 > 3**17 and 2**19 < 3**12
h0, h1, k0, k1 = 0, 1, 1, 0
for digit in (0, 1, 1, 1, 2, 2):
    h0, h1, k0, k1 = h1, digit*h1+h0, k1, digit*k1+k0
assert (h0, k0, h1, k1) == (5, 8, 12, 19)
plus, minus = h.paired.model(p, q, 1)[4], h.paired.model(p, q, -1)[4]
A, B = 160, 110
floor_h = lambda a: h.floor_power(a, 2, 3)
floor_v = lambda b: h.floor_power(b, 3, 2)
AT, BT = h.axis(A, floor_h), h.axis(B, floor_v, True)
partial = sum((F(h.coefficient(AT[a], BT[b], a, b, floor_v, True), 2**a*3**b)
               for a in range(A) for b in range(B)), F(0))
weight = F(1, 2**A)+F(1, 3**B)-F(1, 2**A*3**B)
lower, upper = partial-6*weight, partial+3*weight
D = 27*(2**(3*q)-1)*(3**(3*p)-1)
assert (D*plus).denominator == (D*minus).denominator == 1
assert upper-lower < F(1, D*2**20)


def enclosure(lo, hi):
    left = lo.numerator//lo.denominator
    right = -((-hi.numerator)//hi.denominator)
    assert left < lo < hi < right
    return left, right


print("p/q=12/19; actual rectangle a<160,b<110; full E and low rows")
print("D=", D)
print("D*Z_plus=", D*plus)
print("D*Z_minus=", D*minus)
print("D*(Z-Z_plus) lies strictly between integers", enclosure(D*(lower-plus), D*(upper-plus)))
print("D*(Z-Z_minus) lies strictly between integers", enclosure(D*(lower-minus), D*(upper-minus)))
print("bracket certified:", plus < lower and upper < minus)
assert minus < lower and upper < plus
print("PASS: ordered candidate is false; exact counterexample Z_minus < Z < Z_plus at12/19")
