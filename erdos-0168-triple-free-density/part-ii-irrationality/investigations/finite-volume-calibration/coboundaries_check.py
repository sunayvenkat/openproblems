"""Exact certificates for scalar discounted guard cancellation; no density bridge."""
from fractions import Fraction as Q


def log_bounds(x, terms=80):
    t = Q(x - 1, x + 1)
    s = sum((t ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), Q()) * 2
    tail = 2 * t ** (2 * terms + 1) / ((2 * terms + 1) * (1 - t * t))
    return s, s + tail


l2, u2 = log_bounds(2)
l3, u3 = log_bounds(3)
AL, AU = l2 / u3, u2 / l3


def bounds(p):
    a, b = p
    return (a + b * AL, a + b * AU) if b >= 0 else (a + b * AU, a + b * AL)


def floor_affine(p):
    lo, hi = bounds(p)
    a, b = lo.numerator // lo.denominator, hi.numerator // hi.denominator
    assert a == b
    return a


def norm_phase(p):
    k = floor_affine(p)
    return p[0] - k, p[1]


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def scale(c, z):
    return c * z[0], c * z[1]


def sub(z, w):
    return add(z, scale(-1, w))


UNITS = ((1, 0), (0, 1), (-1, -1))
S = ((1, 0), (0, -1), (0, 0))


def mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c - b * d


def drift(p, length=1):
    z = (0, 0)
    for s in range(1, 3 * length + 1):
        k = floor_affine((3 * p[0], 3 * p[1] + s))
        z = add(z, mul(UNITS[-s % 3], S[k % 3]))
    return z


def prefix(p, i):
    z = (0, 0)
    for s in range(1, i + 1):
        k = floor_affine((3 * p[0], 3 * p[1] + s))
        z = add(z, mul(UNITS[-s % 3], S[k % 3]))
    return z


def cuts(length):
    data = []
    for s in range(1, 3 * length + 1):
        for k in range(3):
            p = norm_phase((Q(k, 3), Q(-s, 3)))
            data.append((p, s, k))
    data.sort(key=lambda row: sum(bounds(row[0])))
    assert len(data) == 9 * length
    assert bounds(data[0][0])[0] > 0 and bounds(data[-1][0])[1] < 1
    for left, right in zip(data, data[1:]):
        assert bounds(left[0])[1] < bounds(right[0])[0]
    return data


def charge(h, base):
    return sum((Q(base) ** (-j) * value for j, value in h.items()), Q())


def reconstruct(h, base):
    lo, hi = min(h), max(h)
    v = {}
    carry = Q()
    for j in range(hi, lo - 1, -1):
        carry = h.get(j, 0) + carry / base
        v[j] = carry
    assert (v[lo] == 0) == (charge(h, base) == 0)
    return v


# Finite jump-orbit reconstruction, including rational carry cancellations.
for base in (8, 27):
    v = {-2: Q(2, 3), 0: Q(-5, 7), 3: Q(11, 4)}
    h = {j: Q(v.get(j, 0)) - Q(v.get(j + 1, 0)) / base for j in range(-3, 4)}
    assert charge(h, base) == 0
    rec = reconstruct(h, base)
    assert all(rec[j] == v.get(j, 0) for j in rec)
    assert charge({0: Q(1)}, base) == 1


# Every actual cut has the predicted unit jump; each orbit charge is explicit.
for length in range(1, 5):
    data = cuts(length)
    endpoints = [(Q(), Q())] + [p for p, _, _ in data] + [(Q(1), Q())]
    values = []
    for left, right in zip(endpoints, endpoints[1:]):
        x = (bounds(left)[1] + bounds(right)[0]) / 2
        values.append(drift((x, Q()), length))
    assert values[0] == values[-1]
    orbits = {}
    for i, (_, s, k) in enumerate(data):
        jump = sub(values[i + 1], values[i])
        assert jump == UNITS[(-s + 2 * k) % 3]
        r, m = (s - 1) % 3 + 1, (s - 1) // 3
        orbits.setdefault((r, k), {})[-m] = jump
    factor = Q(8 ** length - 1, 7)
    for (r, k), h in orbits.items():
        for coordinate in range(2):
            assert charge({j: z[coordinate] for j, z in h.items()}, 8) == factor * UNITS[(-r + 2 * k) % 3][coordinate]


# Phi_2-9Phi_1 is an actual nonconstant integer guard with rational readout.
for p, _, _ in cuts(2):
    lo, hi = bounds(p)
    # The exact identity also holds at rational cell points; no cut value is guessed.
    # Move away from the isolated cut to a certified adjacent rational point.
    x = lo - Q(1, 10**20)
    lhs = sub(drift((x, Q()), 2), scale(9, drift((x, Q()))))
    rhs = sub(drift((x, Q(1))), scale(8, drift((x, Q()))))
    assert lhs == rhs


def board_axis(a):
    t, total, power3, b = 2 ** a, (0, 0), 1, 0
    while power3 <= t:
        power2, j = 1, 0
        while power2 * power3 <= t:
            total = add(total, UNITS[(j - b) % 3])
            power2 *= 2
            j += 1
        power3 *= 3
        b += 1
    return mul(UNITS[-a % 3], total)


count = 16
ys = [board_axis(3 * n) for n in range(count + 1)]
mom = (Q(), Q())
gphi = (Q(), Q())
gh = (Q(), Q())
all_axes = (Q(), Q())
for n in range(count):
    point = norm_phase((Q(), Q(n)))
    phi = drift(point)
    assert sub(ys[n + 1], ys[n]) == phi
    weight = Q(8) ** (-n)
    mom = add(mom, scale(weight, ys[n]))
    gphi = add(gphi, scale(weight, phi))
    h = add(phi, add(scale(2, prefix(point, 1)), prefix(point, 2)))
    gh = add(gh, scale(weight, h))
    for i in range(3):
        value = board_axis(3 * n + i)
        assert value == add(ys[n], prefix(point, i))
        all_axes = add(all_axes, scale(Q(2) ** (-3 * n - i), value))
assert gphi == add(sub(scale(7, mom), (8, 0)), scale(Q(8) ** (1 - count), ys[count]))
assert all_axes == sub(add((2, 0), scale(Q(1, 4), gh)), scale(2 * Q(8) ** (-count), ys[count]))


# Nine actual Boolean arc guards form an invertible charge basis modulo Q.
keys = [(3, 0)] + [(r, k) for r in (1, 2, 3) for k in range(3) if (r, k) != (3, 0)]
c0 = norm_phase((Q(), Q(-1)))
c6 = norm_phase((Q(), Q(-2)))


def before(p, q):
    if p == q:
        return False
    lp, up = bounds(p)
    lq, uq = bounds(q)
    assert up < lq or uq < lp
    return up < lq


def arc(p, end):
    p = norm_phase(p)
    if before(c0, end):
        return int(not before(p, c0) and before(p, end))
    return int(not before(p, c0) or before(p, end))


ends = [c6] + [norm_phase((Q(k, 3), Q(-r, 3))) for r, k in keys[1:]]
data = cuts(2)
endpoints = [(Q(), Q())] + [p for p, _, _ in data] + [(Q(1), Q())]
labels, bv = {}, []
for left, right in zip(endpoints, endpoints[1:]):
    x = (bounds(left)[1] + bounds(right)[0]) / 2
    point = (x, Q())
    code = tuple(floor_affine((3 * x, Q(s))) % 3 for s in range(1, 7))
    values = tuple(arc(point, end) for end in ends)
    assert labels.setdefault(code, values) == values
    bv.append(values)
assert len(labels) == 18
basis = [[Q() for _ in keys] for _ in keys]
for i, (_, s, k) in enumerate(data):
    r, m = (s - 1) % 3 + 1, (s - 1) // 3
    row = keys.index((r, k))
    for column in range(9):
        basis[row][column] += 8 ** m * (bv[i + 1][column] - bv[i][column])
assert basis[0][0] == -7
for column in range(1, 9):
    assert basis[0][column] == 1 and basis[column][column] == -1
    assert all(basis[row][column] == 0 for row in range(1, 9) if row != column)
assert all(basis[row][0] == 0 for row in range(1, 9))
charges = [Q(i - 4, i + 1) for i in range(9)]
coefficients = [-sum(charges, Q()) / 7] + [-v for v in charges[1:]]
assert [sum((basis[i][j] * coefficients[j] for j in range(9)), Q()) for i in range(9)] == charges


# Each fixed-state phase slice telescopes to zero; the actual state flux does not.
def cone(z):
    return int(z[0] <= 0 and z[0] <= z[1])


gs = [int(floor_affine((Q(), Q(3 * n + 1))) % 3 == 2) for n in range(count + 1)]
hs = [cone(sub(y, (1, 0))) for y in ys]
assert gs[0] == 0 and gs[1] == 1 and gs[2] == 0
assert hs[0] == 1 and hs[1] == 0
joint = sum((Q(8) ** (-n) * hs[n] * (gs[n] - Q(gs[n + 1], 8)) for n in range(count)), Q())
flux = sum((Q(8) ** (-n - 1) * (hs[n + 1] - hs[n]) * gs[n + 1] for n in range(count)), Q())
assert joint == hs[0] * gs[0] - Q(8) ** (-count) * hs[count] * gs[count] + flux
flux_tail = Q(8) ** (-count) / 7
assert Q(-57, 448) < flux - flux_tail < flux + flux_tail < Q(-55, 448)


# A Boolean guard is nonperiodic, but b*f-f(Rx) is rational by exact telescoping.
for base in (8, 27):
    fs = []
    for n in range(41):
        lo, hi = bounds(norm_phase((Q(), Q(n))))
        assert hi < Q(1, 3) or lo >= Q(1, 3)
        fs.append(int(hi < Q(1, 3)))
    partial = sum((Q(base) ** (-n) * (base * fs[n] - fs[n + 1]) for n in range(40)), Q())
    assert partial == base * fs[0] - Q(base) ** (1 - 40) * fs[40]

print("PASS: jump reconstruction, nine-guard basis, carry coboundary, actual moments and nonzero state flux")
