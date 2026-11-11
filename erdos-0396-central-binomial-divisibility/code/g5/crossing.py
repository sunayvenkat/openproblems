# Exact threshold for the large-prime carry inequalities.  For P | N = n-i with N/P = c*L,
# write c*L = q*P + r (q constant for large x); carry at P  <=>  0 <= r < P and 2r >= P.
# All three are linear in x; we print the largest real root, beyond which the truth is constant.
from fractions import Fraction as Fr

def thresholds(sides):          # sides: list of (c, f, g) meaning N = c*f*g, forms (a,b)
    worst = Fr(0)
    for c, f, g in sides:
        for P, L in ((f, g), (g, f)):
            a, b = P; al, bl = c*L[0], c*L[1]          # c*L = al x + bl
            q = al // a                                  # quotient for large x (adjust below)
            if al == q*a and bl - q*b < 0: q -= 1        # integer ratio, negative offset
            ra, rb = al - q*a, bl - q*b                  # r = ra x + rb
            conds = [(ra, rb), (a - ra, b - rb), (2*ra - a, 2*rb - b)]   # each must be >= 0
            for s, t in conds:
                if s > 0: worst = max(worst, Fr(-t, s))
                elif s == 0: assert t >= 0, (P, L, "fails for all large x")
                else: raise AssertionError((P, L, "fails for large x"))
    return worst

A = [(1, (14, 3), (24, 17)), (2, (24, 5), (7, 5))]
print("E_1 family: inequalities hold for x >", thresholds(A))
def sub(f): return (42*f[0], 9*f[0] + f[1])          # x = 42y+9
B0 = [(3, (70, 31), (252, 113)), (2, (84, 37), (315, 142)), (7, (180, 79), (42, 19))]
B = [(c, sub(f), sub(g)) for c, f, g in B0]
print("E_2 family (x=42y+9): inequalities hold for y >", thresholds(B))
