"""Exact complementary-resonance induction and narrow comparison-mask checks."""

from math import isqrt

ZERO, ONE = (0, 0), (1, 0)
UNIT = (ONE, (0, 1), (-1, -1))


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def scale(k, z):
    return k*z[0], k*z[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c-b*d


def rot(z, k):
    return mul(z, UNIT[k % 3])


def root(p, q):
    z = ZERO
    for a in range(1, q+1):
        z = add(z, UNIT[(-a-a*p//q) % 3])
    return z


def step(Q, P, rho, previous_rho, digit, parity):
    geometric = ZERO
    for j in range(digit):
        geometric = add(geometric, UNIT[(j*rho) % 3])
    next_Q = (add(mul(geometric, Q), rot(P, digit*rho))
              if parity == 0 else add(P, rot(mul(geometric, Q), previous_rho)))
    return next_Q, Q, (digit*rho+previous_rho) % 3, rho


# Both parity formulas are checked directly against all four one-step transfers.
for parity in (0, 1):
    for r in (1, 2):
        for k in (1, 2, 5):
            Q, P = (2, -1), (-3, 4)
            predicted_Q = rot(scale(-1, Q), 2*r if parity == 0 else r)
            predicted_P = (add(add(Q, rot(scale(-k, Q), 2*r)), rot(scale(-1, P), 2*r))
                           if parity == 0 else add(add(rot(Q, 2*r), scale(-k, Q)), rot(scale(-1, P), 2*r)))
            state = (Q, P, 0, r)
            for offset, digit in enumerate((k, 1, 1, 1)):
                state = step(*state, digit, (parity+offset) % 2)
            assert state == (predicted_Q, predicted_P, 0, 2*r % 3)
            second = state
            for offset, digit in enumerate((2, 1, 1, 1)):
                second = step(*second, digit, (parity+offset) % 2)
            shift = scale(k+3, Q) if parity == 0 else rot(scale(k+3, Q), r)
            assert second == (Q, add(P, shift), 0, r)


def side_floor(n, p, q, sign):
    value, rem = divmod(n*p, q)
    return value-int(n > 0 and rem == 0 and sign < 0)


def axis(limit, floor, vertical=False):
    states = [ONE]
    table = (ONE, (1, 1), ZERO) if vertical else (ONE, (0, -1), ZERO)
    for k in range(1, limit+1):
        states.append(add(states[-1], rot(table[floor(k) % 3], -2*k if vertical else -k)))
    return states


CORRECTION = ((ZERO, ZERO, ZERO),
              (ZERO, ONE, (1, 1)),
              (ZERO, (0, -1), ONE))


def mask(A, B, reciprocal, a, b):
    x, y = add(add(A[a], B[b]), CORRECTION[a % 3][b % 3])
    x -= 1
    if b == 0:
        return 0
    if b == 1:
        return 1 if a == 0 else int(x >= 1 and y >= 0)
    if b == 2:
        return int(x <= -1 and x-y <= 0)
    if b == 3:
        return int(min(x, 0) <= y)
    isolated = reciprocal(b)-reciprocal(b-1) == 2
    patch = reciprocal(b-1)-reciprocal(b-3) == 4
    assert not (isolated and patch)
    color = reciprocal(b)-2*b if isolated else reciprocal(b-1)-1-2*b
    e = UNIT[color % 3] if isolated or patch else ZERO
    return int(x-e[0] <= 0 and x-y-e[0]+e[1] <= 0)


# alpha_g=(sqrt(5)-1)/2 has the all-one complementary resonance pattern.
# Adjacent convergents bracket every used floor exactly; no float is used.
low_p, low_q, high_p, high_q = 6765, 10946, 10946, 17711


def true_a(a):
    return (isqrt(5*a*a)-a)//2


def true_b(b):
    return (isqrt(5*b*b)+b)//2


for k in range(1000):
    assert true_a(k) == k*low_p//low_q == side_floor(k, high_p, high_q, -1)
    assert true_b(k) == k*high_q//high_p == side_floor(k, low_q, low_p, -1)


for p, q, pp, qq in ((8, 13, 13, 21), (55, 89, 89, 144), (377, 610, 610, 987)):
    R, S = q+qq, p+pp
    max_a, max_b = 4*R, 4*S
    ma = lambda a: side_floor(a, p, q, 1)
    mb = lambda b: side_floor(b, q, p, -1)
    AT, AM = axis(max_a, true_a), axis(max_a, ma)
    BT, BM = axis(max_b, true_b, True), axis(max_b, mb, True)
    assert AT[:R] == AM[:R] and BT[:S] == BM[:S]
    first_horizontal = None
    for a in range(R, max_a+1):
        for b in range(min(S, 3*p+4)):
            if mask(AT, BT, true_b, a, b) != mask(AM, BM, mb, a, b):
                first_horizontal = (a, b)
                break
        if first_horizontal:
            break
    first_vertical = None
    for b in range(S, max_b+1):
        for a in range(min(R, 3*q)):
            if mask(AT, BT, true_b, a, b) != mask(AM, BM, mb, a, b):
                first_vertical = (a, b)
                break
        if first_vertical:
            break
    assert first_horizontal and first_vertical
    print({"comparison": "golden", "p/q": (p, q), "floor_window": (R, S),
           "first_horizontal_band_defect": first_horizontal,
           "first_vertical_band_defect": first_vertical,
           "B_T_at_S_plus_1": BT[S+1], "B_M_at_S_plus_1": BM[S+1],
           "root_Q": root(p, q), "previous_root": root(pp-p, qq-q)})

p, q, u, v = 8, 13, 5, 8
history = []
for j in range(3):
    history.append((p, q, u, v))
    h = (j+1)//2
    R, S = 2*q+v, 2*p+u
    a = history[h][3] - (1 if j % 2 == 0 else 3)
    b = S+1
    base_a, last_i = q-v, j+1
    ma = lambda a: side_floor(a, p, q, 1)
    mb = lambda b: side_floor(b, q, p, -1)
    AM = axis(base_a+3*q*last_i, ma)
    AT = axis(max(a, v), true_a)
    BM, BT = axis(b, mb, True), axis(b, true_b, True)
    assert p % 3 == u % 3 == v % 3 == 2 and q % 3 == 1
    assert root(p, q) == ONE and root(u, v) == (3*j, -1)
    assert AM[base_a] == (j+1, -j)
    assert AT[v] == (2*j+2, j+1)
    assert AT[v-1] == AT[v-3] == (2*j+1, j)
    for i in range(last_i+1):
        aa = base_a+3*q*i
        assert AM[aa] == (j+1+2*i, -j+i)
        assert mask(AM, BM, mb, aa, 1) == int(i >= j+1)
    assert BM[b] == (-j, j+2) and BT[b] == (-j, j+1)
    assert a < R and AT[a] == AM[a] == (2*h+1, h)
    assert mask(AT, BT, true_b, a, b) == 1
    assert mask(AM, BM, mb, a, b) == 0
    print({"all_level_formula_check_j": j, "p/q": (p, q),
           "proved_defect_witness": (a, b),
           "last_zero_on_low_residue": base_a+3*q*j})
    p, u = 34*p+21*u, 21*p+13*u
    q, v = 34*q+21*v, 21*q+13*v

print("PASS: both parity resonance transfers; narrow bands; three direct all-level-formula checks.")
