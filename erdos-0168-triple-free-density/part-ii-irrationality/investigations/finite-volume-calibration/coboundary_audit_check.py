"""Standalone exact audit; stdlib only, no companion-note imports.

Finite checks certify algebra and actual-board examples. The infinite scalar
converse, orbit matching, and tail arguments are proved in coboundary_audit.md.
"""

from fractions import Fraction as Q
from functools import cmp_to_key


def log_bounds(q, terms=90):
    z = Q(q - 1, q + 1)
    acc = Q(0)
    for j in reversed(range(terms)):
        acc = Q(1, 2 * j + 1) + z * z * acc
    lo = 2 * z * acc
    return lo, lo + 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))


l2, u2 = log_bounds(2)
l3, u3 = log_bounds(3)
ALPHA = (l2 / u3, u2 / l3)


def bounds(a):
    p, q = a
    lo, hi = ALPHA if q >= 0 else ALPHA[::-1]
    return p + q * lo, p + q * hi


def floor(a):
    lo, hi = bounds(a)
    v, w = lo.numerator // lo.denominator, hi.numerator // hi.denominator
    assert v == w, "Logarithmic interval did not isolate a floor"
    return v


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(a, t):
    return a[0] * t, a[1] * t


def frac(a):
    return a[0] - floor(a), a[1]


def compare(a, b):
    if a == b:
        return 0
    lo, hi = bounds(add(a, scale(b, -1)))
    assert lo > 0 or hi < 0, "Logarithmic interval did not order cuts"
    return 1 if lo > 0 else -1


ZERO, ONE = (Q(0), Q(0)), (Q(1), Q(0))


def rotate(x):
    return frac(add(x, (Q(0), Q(1))))


def phase(n):
    return frac((Q(0), Q(n)))


def cut(s, k):
    return frac((Q(k, 3), Q(-s, 3)))


def cuts(m):
    data = [(cut(s, k), s, k) for s in range(1, m + 1) for k in range(3)]
    return sorted(data, key=cmp_to_key(lambda a, b: compare(a[0], b[0])))


def midpoint(a, b):
    if compare(b, a) <= 0:
        b = add(b, ONE)
    return frac(scale(add(a, b), Q(1, 2)))


def samples(data):
    return [midpoint(row[0], data[(i + 1) % len(data)][0]) for i, row in enumerate(data)]


def digit(x, s):
    return floor(add(scale(x, 3), (Q(0), Q(s)))) % 3


def arc(x, a, b):
    if compare(a, b) < 0:
        return int(compare(a, x) <= 0 and compare(x, b) < 0)
    return int(compare(a, x) <= 0 or compare(x, b) < 0)


ORBITS = [(3, 0)] + [(r, k) for r in range(1, 4) for k in range(3) if (r, k) != (3, 0)]


def basis(i, x):
    end = cut(6, 0) if i == 0 else cut(*ORBITS[i])
    return arc(x, cut(3, 0), end)


def jumps(h, m):
    data = cuts(m)
    pts = samples(data)
    return {(s, k): h(pts[i]) - h(pts[i - 1]) for i, (_, s, k) in enumerate(data)}


def charges(js, b=8):
    result = {o: Q(0) for o in ORBITS}
    for (s, k), d in js.items():
        r = (s - 1) % 3 + 1
        result[r, k] += b ** ((s - r) // 3) * d
    return [result[o] for o in ORBITS]


def determinant(matrix):
    a = [[Q(v) for v in row] for row in matrix]
    answer = Q(1)
    for j in range(len(a)):
        k = next(k for k in range(j, len(a)) if a[k][j])
        if k != j:
            a[j], a[k] = a[k], a[j]
            answer = -answer
        pivot = a[j][j]
        answer *= pivot
        for k in range(j + 1, len(a)):
            t = a[k][j] / pivot
            a[k] = [x - t * y for x, y in zip(a[k], a[j])]
    return answer


# Every basis arc is exactly a Boolean rule on the original six-offset code.
partition = cuts(6)
pts = samples(partition)
assert len({tuple(digit(x, s) for s in range(1, 7)) for x in pts}) == 18
columns = [charges(jumps(lambda x, i=i: Q(basis(i, x)), 6)) for i in range(9)]
matrix = [[columns[j][i] for j in range(9)] for i in range(9)]
assert determinant(matrix) == -7
assert columns[0] == [-7] + [0] * 8
for j in range(1, 9):
    assert columns[j] == [int(i == 0) - int(i == j) for i in range(9)]


# A mixed, non-Boolean guard: reduce its charges and reconstruct its transfer.
def guard(x):
    ds = [digit(x, s) for s in range(1, 13)]
    return Q(5, 7) + sum(Q((-1) ** s, s + 1) * ds[s - 1] for s in range(1, 13)) + Q(3, 11) * (ds[0] == ds[7])


c = charges(jumps(guard, 12))
coeff = [-sum(c) / 7] + [-v for v in c[1:]]


def remainder(x):
    return guard(x) - sum(coeff[i] * basis(i, x) for i in range(9))


ds = jumps(remainder, 12)
assert charges(ds) == [0] * 9
vs = {}
for r, k in ORBITS:
    orbit = {-(s - r) // 3: d for (s, kk), d in ds.items() if kk == k and (s - 1) % 3 + 1 == r}
    nxt = Q(0)
    for j in range(max(orbit), min(orbit) - 1, -1):
        nxt = orbit.get(j, 0) + nxt / 8
        vs[cut(r - 3 * j, k)] = nxt
    assert nxt == 0
assert sum(vs.values()) == 0


def transfer0(x):
    return sum(v for a, v in vs.items() if compare(a, x) <= 0)


constant = Q(8, 7) * (remainder(ZERO) - transfer0(ZERO) + transfer0(rotate(ZERO)) / 8)


def transfer(x):
    return constant + transfer0(x)


for x in [ZERO] + samples(cuts(15)) + [row[0] for row in cuts(15)]:
    assert remainder(x) == transfer(x) - transfer(rotate(x)) / 8


# Direct finite-support recurrence, including negative indices and both bases.
for b in (8, 27):
    v = dict(zip(range(-2, 3), map(Q, (1, -2, 4, -5, 2))))
    d = {j: v.get(j, 0) - v.get(j + 1, 0) / b for j in range(-3, 3)}
    assert sum(Q(b) ** (-j) * value for j, value in d.items()) == 0
    recovered, nxt = {}, Q(0)
    for j in reversed(range(-3, 3)):
        nxt = d[j] + nxt / b
        recovered[j] = nxt
    assert recovered == {j: v.get(j, 0) for j in range(-3, 3)}
    p = lambda x: basis(1, x)
    value, x, nterms = Q(0), ZERO, 35
    values = set()
    for n in range(nterms):
        h = b * p(x) - p(rotate(x))
        values.add(h)
        value += Q(b) ** (-n) * h
        x = rotate(x)
    assert value == b * p(ZERO) - Q(b) ** (1 - nterms) * p(x)
    assert len(values) >= 2 and values <= {-1, 0, b - 1, b}


# A singleton endpoint spike: infinitely many distinct rational transfer values.
spike = cut(3, 0)
assert all(phase(n) != spike for n in range(40))
for k in range(15):
    x, total = phase(-k - 1), Q(0)
    for n in range(k + 3):
        total += Q(8) ** (-n) * (x == spike)
        x = rotate(x)
    assert total == Q(8) ** (-k)


def zmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] - a[1] * b[1]


def zadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def zscale(a, t):
    return a[0] * t, a[1] * t


def zsum(items):
    ans = (Q(0), Q(0))
    for item in items:
        ans = zadd(ans, item)
    return ans


def unit(p):
    return ((1, 0), (0, 1), (-1, -1))[p % 3]


def psi(x, length):
    return zsum(zmul(unit(-s), ((1, 0), (0, -1), (0, 0))[digit(x, s)]) for s in range(1, length + 1))


# Derive each axis from original board row COLOR COUNTS, not a state recurrence.
def board_axis(a):
    bound, three, row = 2 ** a, 1, 0
    colors = [0, 0, 0]
    while three <= bound:
        max_col = (bound // three).bit_length() - 1
        for color in range(3):
            residue = (color + row) % 3
            colors[color] += max(0, (max_col - residue) // 3 + 1)
        three *= 3
        row += 1
    return zmul(unit(-a), (colors[0] - colors[2], colors[1] - colors[2]))


for length in range(1, 5):
    data = cuts(3 * length)
    cell = samples(data)
    for i, (_, s, k) in enumerate(data):
        jump = zadd(psi(cell[i], 3 * length), zscale(psi(cell[i - 1], 3 * length), -1))
        assert jump == unit(-s + 2 * k)
for x in samples(cuts(9)):
    assert zadd(psi(x, 6), zscale(psi(x, 3), -9)) == zadd(psi(rotate(x), 3), zscale(psi(x, 3), -8))
phi_charges = [unit(-r + 2 * k) for r, k in ORBITS]
assert (1, 0) in phi_charges and (0, 1) in phi_charges

N = 24
axes = [board_axis(a) for a in range(3 * N + 1)]
ys = axes[::3]
assert ys[:3] == [(1, 0), (1, -1), (2, 0)]
for n in range(N):
    for i in range(4):
        assert axes[3 * n + i] == zadd(ys[n], psi(phase(n), i))
moment = zsum(zscale(ys[n], Q(8) ** (-n)) for n in range(N))
gphi = zsum(zscale(psi(phase(n), 3), Q(8) ** (-n)) for n in range(N))
assert gphi == zsum((zscale(moment, 7), (-8, 0), zscale(ys[N], Q(8) ** (1 - N))))
all_moment = zsum(zscale(axes[a], Q(2) ** (-a)) for a in range(3 * N))
gh = zsum(zscale(zsum((psi(phase(n), 3), zscale(psi(phase(n), 1), 2), psi(phase(n), 2))), Q(8) ** (-n)) for n in range(N))
assert all_moment == zsum(((2, 0), zscale(gh, Q(1, 4)), zscale(ys[N], -2 * Q(8) ** (-N))))


def minimum(z):
    return min(0, *z)


def F(z):
    return int(z[0] <= 0 and z[0] <= z[1])


for z in axes:
    assert minimum(zmul(unit(1), z)) == minimum(z) - z[1]
    assert minimum(zmul(unit(2), z)) == minimum(z) - z[0]
fs = [F((y[0] - 1, y[1])) for y in ys]
gs = [int(digit(phase(n), 1) == 2) for n in range(N + 1)]
assert fs[:2] == [1, 0] and gs[:3] == [0, 1, 0]
flux = [Q(fs[n + 1] - fs[n], 8) * gs[n + 1] for n in range(N)]
assert flux[:2] == [Q(-1, 8), 0]
flux_sum = sum(Q(8) ** (-n) * flux[n] for n in range(N))
frozen_sum = sum(Q(8) ** (-n) * fs[n] * (gs[n] - Q(gs[n + 1], 8)) for n in range(N))
assert frozen_sum == -Q(8) ** (-N) * fs[N] * gs[N] + flux_sum
tail = Q(8) ** (-N) / 7
assert Q(-57, 448) < flux_sum - tail <= flux_sum + tail < Q(-55, 448)
print("PASS: exact orbit charges, determinant -7, mixed-guard transfer, both-base carries, endpoint spike")
print("PASS: original-board Phi/moments/minima and full-tail nonzero state flux")
print("Flux enclosure:", flux_sum - tail, flux_sum + tail)
