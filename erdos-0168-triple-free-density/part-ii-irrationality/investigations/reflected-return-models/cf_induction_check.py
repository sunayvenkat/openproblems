"""Exact certificates for cf_induction.md; standard library only. Run with -B."""

from fractions import Fraction


ONE, ZERO, OMEGA = (1, 0), (0, 0), (0, 1)
UNITS = (ONE, OMEGA, (-1, -1))


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def neg(z):
    return -z[0], -z[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c - b * d


def norm(z):
    a, b = z
    return a * a - a * b + b * b


def div(z, w):
    c, d = w
    a, b = mul(z, (c - d, -d))
    return Fraction(a, norm(w)), Fraction(b, norm(w))


def unit(k):
    return UNITS[k % 3]


def word(p, q):
    return tuple(k * p // q - (k - 1) * p // q for k in range(1, q + 1))


def root_sum(w):
    z, m = ZERO, 0
    for k, h in enumerate(w, 1):
        m += h
        z = add(z, unit(-k - m))
    return z


def axis_run(w, state, readout):
    z, r, m = state
    total = Fraction(0)
    for k, h in enumerate(w, 1):
        r, m = (r + 1) % 3, (m + h) % 3
        z = add(z, mul(unit(-r), (ONE, neg(OMEGA), ZERO)[m]))
        total += Fraction(readout(z), 2**k)
    return (z, r, m), total


def axis_formula(w, r, m):
    harmonic = ZERO
    for k in range(1, len(w) + 1):
        harmonic = add(harmonic, unit(-k))
    return mul(unit(-r), div(add(harmonic, neg(mul(unit(2 * m + 2), root_sum(w)))), add(ONE, neg(unit(2)))))


def cone(z):
    x, y = z
    return int(x <= 0 and x - y <= 0)


def ray02(z):
    x, y = z
    return int(x == 0 and y >= 1)


assert mul(OMEGA, OMEGA) == (-1, -1)
assert root_sum(word(1, 2)) == neg(OMEGA)

# Independent mechanical-floor construction checks the parity-sensitive CF rule.
p0, q0, p, q = 5, 8, 18, 29
Q0, Q = root_sum(word(p0, q0)), root_sum(word(p, q))
initial_gap = None
cf_checks = 0
for n, a in enumerate((2, 1) * 6, 6):
    pp, qq = a * p + p0, a * q + q0
    W0, W = word(p0, q0), word(p, q)
    predicted_word = W * a + W0 if n % 2 == 0 else W0 + W * a
    assert predicted_word == word(pp, qq)
    rho, rho0 = unit(-p - q), unit(-p0 - q0)
    geometric = ZERO
    for j in range(a):
        geometric = add(geometric, unit(-j * (p + q)))
    predicted_Q = (
        add(mul(geometric, Q), mul(unit(-a * (p + q)), Q0))
        if n % 2 == 0
        else add(Q0, mul(mul(rho0, geometric), Q))
    )
    assert predicted_Q == root_sum(word(pp, qq))
    assert (p + q) % 3 and (p0 + q0) % 3 and (pp + qq) % 3
    gap = add(div(Q, add(ONE, neg(rho))), neg(div(Q0, add(ONE, neg(rho0)))))
    initial_gap = norm(gap) if initial_gap is None else initial_gap
    assert norm(gap) == initial_gap
    p0, q0, p, q, Q0, Q = p, q, pp, qq, Q, predicted_Q
    cf_checks += 1
    if (n + 1 - 6) % 4 == 0:
        t = (n + 1 - 6) // 4
        assert Q == (0, t - 1) and Q0 == (-t, -1)
        c_A = neg(div(mul(unit(2), Q), mul(add(ONE, neg(unit(2))), add(ONE, neg(unit(-p-q))))))
        assert c_A == (Fraction(1 - t, 3), 0)

# A bounded actual-prefix certificate, not a conjectured all-level formula.
assert (p, q) == (42258, 68039)
z, first_hits = ONE, {1: None, 2: None, 3: None}
for a, h in enumerate(word(p, q), 1):
    m = a * p // q
    z = add(z, mul(unit(-a), (ONE, neg(OMEGA), ZERO)[m % 3]))
    for level in first_hits:
        if first_hits[level] is None and ray02(add(z, (level - 1, 0))):
            first_hits[level] = a
            assert z == (1 - level, 1)
assert first_hits == {1: 209, 2: 3083, 3: 43121}

# Weighted profiles concatenate at the ACTUAL incoming state and residue.
U, V = word(5, 8), word(18, 29)
profile_checks = 0
for r in range(3):
    for m in range(3):
        state = ((2, -1), r, m)
        for h in (cone, ray02):
            middle, left = axis_run(U, state, h)
            end, right = axis_run(V, middle, h)
            direct_end, direct = axis_run(U + V, state, h)
            assert direct_end == end and direct == left + right / 2**len(U)
            assert axis_run(U * 3, state, h)[0] == state
            assert add(axis_run(U, state, h)[0][0], neg(state[0])) == axis_formula(U, r, m)
            profile_checks += 1

# Four-digit transfer and a genuinely realized sampled tie-ray obstruction.
qt, qt_previous = 29, 8
Qt, Qt_previous = neg(OMEGA), neg(OMEGA)
for t in range(25):
    assert Qt == (0, t - 1) and Qt_previous == (-t, -1)
    if t % 3 == 0:
        ell = t // 3
        A = add(div(add((2, 0), unit(-qt)), (3, 0)), neg(div(mul(unit(2), Qt), add(ONE, neg(unit(2))))))
        assert A == (1 - ell, ell)
        for level in range(1, 9):
            assert ray02(add(A, (level - 1, 0))) == int(ell == level)
    Qt, Qt_previous = (
        add(mul(neg(unit(2)), Qt), mul(unit(2), Qt_previous)),
        add(neg(Qt), mul(add(ONE, neg(OMEGA)), Qt_previous)),
    )
    qt, qt_previous = 11 * qt + 4 * qt_previous, 8 * qt + 3 * qt_previous

print(f"PASS: {cf_checks} direct CF word/root checks, {profile_checks} weighted profile checks, 25 exact unipotent iterates; first ray hits {first_hits}.")
