"""Window-limited signed identities and one explicit beyond-window repair."""

from fractions import Fraction as F
import importlib.util
from pathlib import Path


source = Path(__file__).with_name('signed_boundaries_check.py')
spec = importlib.util.spec_from_file_location('signed_cert', source)
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)


def specialize(P, coordinate, value):
    answer = {}
    for (a, b), c in P.items():
        power, factor = (a, value ** b) if coordinate == 'y' else (b, value ** a)
        answer[power] = answer.get(power, 0) + c * factor
    return {power: c for power, c in answer.items() if c}


# The written degree proof handles arbitrary coefficients and arbitrary depth.
pairs = ((5, 8, 19), (12, 19, 65), (41, 65, 84), (53, 84, 485))
for mask in range(1, 1 << len(pairs)):
    chosen = [row for i, row in enumerate(pairs) if mask & (1 << i)]
    for degree_rule in (lambda w: 0, lambda w: w - 1, lambda w: 2 * w - 1):
        P = {}
        for i, (p, q, successor) in enumerate(chosen):
            degree = degree_rule(successor - q)
            coefficient = {(degree, 0): (-1) ** i, (0, 1): i + 1}
            P = f.plus(P, f.times(coefficient, f.L(p, q)))
        p, q, successor = chosen[-1]
        g = specialize(coefficient, 'y', 3)
        restricted = specialize(P, 'y', 3)
        assert max(restricted) == max(g) + 2 * q > 0


p, q, r, s = 5, 8, 12, 19
Ax, Bx, _ = f.inverse_certificate(p, q, r, s, r, p)
Ay, By, _ = f.inverse_certificate(p, q, r, s, s, q)
factor = {(0, 0): 27, (0, 3): -1}
A0, B0 = f.plus(f.times(factor, Ax), f.scale(Ay, 7)), f.plus(f.times(factor, Bx), f.scale(By, 7))
swap = lambda P: {(b, a): c for (a, b), c in P.items()}
# Swap variables and generator order to obtain the opposite Laurent orientation.
Cx, Dx, _ = f.inverse_certificate(s, r, q, p, q, s)
Cy, Dy, _ = f.inverse_certificate(s, r, q, p, p, r)
Ar = f.plus(f.times(factor, swap(Dy)), f.scale(swap(Dx), 7))
Br = f.plus(f.times(factor, swap(Cy)), f.scale(swap(Cx), 7))
assert f.plus(f.times(Ar, f.L(p, q)), f.times(Br, f.L(r, s))) == f.P0
M = -min(a for a, b in list(A0) + list(B0))
N = -min(b for a, b in list(Ar) + list(Br))
assert M > 0 and N > 0
assert min(b for a, b in list(A0) + list(B0)) >= 0
assert min(a for a, b in list(Ar) + list(Br)) >= 0
first = {(0, N): 1, (0, 0): -3 ** N}
A = f.plus(f.times(first, f.shift(A0, M, 0)), f.scale(f.shift(Ar, 0, N), -2 ** M))
B = f.plus(f.times(first, f.shift(B0, M, 0)), f.scale(f.shift(Br, 0, N), -2 ** M))
R = {(M, N): 1, (M, 0): -3 ** N, (0, N): -2 ** M}
P = f.times(f.P0, R)
assert f.plus(f.times(A, f.L(p, q)), f.times(B, f.L(r, s))) == P
assert all(a >= 0 and b >= 0 for a, b in list(A) + list(B))
lam = -182 * 2 ** M * 3 ** N
assert f.evaluate(P) == lam
assert specialize(P, 'y', 3) == {0: lam}
assert specialize(P, 'x', 2) == {0: lam}
degree_A, degree_B = max(specialize(A, 'y', 3)), max(specialize(B, 'y', 3))
assert degree_A >= degree_B + 2 * (s - q)
assert degree_A >= 2 * (19 - 8)


# One fixed actual residual, including all of its infinite tail.
A_cut, B_cut = 28, 20
head = sum((F(sum(c * f.actual_d(a + aa, b + bb) for (aa, bb), c in P.items()),
              2 ** a * 3 ** b) for a in range(A_cut) for b in range(B_cut)), F())
outside = F(1, 2 ** A_cut) + F(1, 3 ** B_cut) - F(1, 2 ** A_cut * 3 ** B_cut)
error = 6 * sum(abs(c) for c in P.values()) * outside
low, high = head - error, head + error
assert low > 1 or high < -1
scale = 2 ** 64
lower = (low / scale).numerator // (low / scale).denominator
upper = -((-high / scale).numerator // (-high / scale).denominator)
assert F(lower * scale) < low and high < F(upper * scale)
print({'ordinary_repair': {'M': M, 'N': N, 'evaluation_bits': abs(lam).bit_length(),
                           'effective_X_degrees': (degree_A, degree_B),
                           'actual_origin_windows': (19 - 8, 65 - 19)},
       'actual_W_Pd_over_2^64_strict_bounds': (lower, upper)})
print('PASS: window degree barriers and one complete ordinary signed repair.')
