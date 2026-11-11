# Exact check of Section 4: T(u+p) = w^q T(u) + w^-p X(u), X(u+p) = w^-p X(u), in the slope-p/q model.
# Eisenstein integers as pairs (x,y) = x + y*w, w^2 = -1 - w.
from fractions import Fraction as Fr
from math import floor
def wpow(k):
    return ((1, 0), (0, 1), (-1, -1))[k % 3]
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0] - a[1]*b[1])
def T(u, p, q):
    N = floor(u * q / p); s = (0, 0)
    for a in range(N + 1): s = add(s, wpow(a - floor(u - Fr(a * p, q))))
    return s
def X(u, p, q):
    s = (0, 0)
    for a in range(q): s = add(s, wpow(a - floor(u - Fr(a * p, q))))
    return s
bad = 0; n = 0
for p, q in ((5, 8), (12, 19), (41, 65), (53, 84), (7, 11), (2, 3), (19, 30)):
    for k in range(0, 6 * p * q, 7):
        u = Fr(2 * k + 1, 2 * q)          # generic point between model breakpoints
        lhs = T(u + p, p, q); rhs = add(mul(wpow(q), T(u, p, q)), mul(wpow(-p), X(u, p, q)))
        ok = lhs == rhs and X(u + p, p, q) == mul(wpow(-p), X(u, p, q))
        bad += not ok; n += 1
print("tests", n, "failures", bad)
