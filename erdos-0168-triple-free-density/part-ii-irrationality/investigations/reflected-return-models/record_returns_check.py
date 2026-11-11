"""Exact record-prefix and actual-array corner certificates. Run with -B."""

from fractions import Fraction


ZERO, ONE = (0, 0), (1, 0)
UNIT = (ONE, (0, 1), (-1, -1))


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c - b * d


def rot(z, k):
    return mul(UNIT[k % 3], z)


def base(p, q):
    roots = [ZERO]
    for k in range(1, q + 1):
        roots.append(add(roots[-1], UNIT[(-k - k * p // q) % 3]))
    return (q, p, roots[-1], UNIT[(-q-p) % 3], None, roots)


def concat(children):
    length, ones, Q, rho = 0, 0, ZERO, ONE
    for child in children:
        length += child[0]
        ones += child[1]
        Q = add(Q, mul(rho, child[2]))
        rho = mul(rho, child[3])
    assert rho == UNIT[(-length-ones) % 3]
    return (length, ones, Q, rho, children, None)


def prefix(node, k):
    assert 0 <= k <= node[0]
    if k == node[0]:
        return node[2]
    if node[5] is not None:
        return node[5][k]
    Q, rho = ZERO, ONE
    for child in node[4]:
        if k <= child[0]:
            return add(Q, mul(rho, prefix(child, k)))
        k -= child[0]
        Q = add(Q, mul(rho, child[2]))
        rho = mul(rho, child[3])
    raise AssertionError("prefix exhausted")


# Independent floor sum checks the nontrivial seed used by the all-level proof.
assert base(218, 351)[5][114] == (-3, -3)
assert base(218, 351)[5][209] == (0, 2)
W, V = base(18, 29), base(5, 8)
for t in range(25):
    q, v = W[0], V[0]
    assert W[2] == (0, t-1) and V[2] == (-t, -1)
    if t >= 1:
        assert v % 2 == 0
        g, f = v//2 - 14, q-v//2-14
        assert 0 <= g < q and 0 <= f < q and f % 3 == 2
        assert prefix(W, g) == (-t-2, -t-2)
        Qf = prefix(W, f)
        assert Qf == (1-t, t+1)
        numerator = add(add((2, 0), UNIT[-f % 3]), mul((2, 1), Qf))
        assert numerator == (3*(1-t), 3)
    common = (W, W, W, V)
    next_W = concat(common*3 + (W, W, V))
    next_V = concat(common*2 + (W, W, V))
    assert (next_W[0], next_V[0]) == (11*q+4*v, 8*q+3*v)
    # Exact lower/upper convergent brackets certify ACTUAL floor values.
    f = q-v//2-14
    d = W[1]-(V[1]+19)//2
    assert d % 3 == 0 and f % 3 == 2
    assert f*next_W[1]//next_W[0] == d
    quotient, remainder = divmod(f*next_V[1], next_V[0])
    assert quotient-int(remainder == 0) == d
    for b, expected in ((d, f-2), (d-1, f-3), (d-2, f-5)):
        assert b*next_V[0]//next_V[1] == expected
        quotient, remainder = divmod(b*next_W[0], next_W[1])
        assert quotient-int(remainder == 0) == expected
    Qf = prefix(W, f)
    QB = add((-1, 0), (-Qf[0], -Qf[1]))
    conjugate_QB = (QB[0]-QB[1], -QB[1])
    three_Bd = add(add((2, 0), UNIT[d % 3]), mul((1, -1), conjugate_QB))
    assert three_Bd == (3*(t+1), 3)
    B_row, E_row, C_row = (t, 1), (0, 1), (1, 0)
    row_offset = add(add(add(B_row, (-1, 0)), C_row), (0, -1))
    assert row_offset == (t, 0)
    next_f = next_W[0]-next_V[0]//2-14
    next_Qf = prefix(next_W, next_f)
    three_A = add(add((2, 0), UNIT[-next_f % 3]), mul((2, 1), next_Qf))
    assert three_A == (-3*t, 3)
    assert add((-t, 1), row_offset) == (0, 1)
    W, V = next_W, next_V


def exact_floor(n, from_base, to_base):
    value, exponent = from_base**n, 0
    while to_base**(exponent+1) <= value:
        exponent += 1
    return exponent


def model_floor(n, p, q, sign):
    quotient, remainder = divmod(n*p, q)
    return quotient - int(n > 0 and remainder == 0 and sign < 0)


def axis(limit, floor_function, vertical=False):
    states = [ONE]
    table = (ONE, (1, 1), ZERO) if vertical else (ONE, (0, -1), ZERO)
    for k in range(1, limit+1):
        states.append(add(states[-1], rot(table[floor_function(k) % 3], -2*k if vertical else -k)))
    return states


# Independent bounded reciprocal-floor checks of the first three coupled rows.
for b in range(1, 1915):
    assert b*68039//42258 == b*49808//30935
Bstar = axis(1914, lambda b: b*68039//42258, True)
for level, d in ((0, 6), (1, 129), (2, 1914)):
    assert Bstar[d] == (level+1, 1)
    assert Bstar[d-1] == (level, 1)


correction = (((0, 0), (0, 0), (0, 0)),
              ((0, 0), (1, 0), (1, 1)),
              ((0, 0), (0, -1), (1, 0)))
R, S, max_a, max_b = 27, 17, 36, 26
true_a = lambda a: exact_floor(a, 2, 3)
true_b = lambda b: exact_floor(b, 3, 2)
model_a = lambda a: model_floor(a, 5, 8, 1)
model_b = lambda b: model_floor(b, 8, 5, -1)
AT, AM = axis(max_a, true_a), axis(max_a, model_a)
BT, BM = axis(max_b, true_b, True), axis(max_b, model_b, True)
assert AT[:R] == AM[:R] and BT[:S] == BM[:S]


def coefficient(A, B, reciprocal_floor, a, b):
    x, y = add(add(A[a], B[b]), correction[a % 3][b % 3])
    x -= 1
    if b == 0:
        eta = 0
    elif b == 1:
        eta = 1 if a == 0 else int(x >= 1 and y >= 0)
    elif b == 2:
        eta = int(x <= -1 and x-y <= 0)
    elif b == 3:
        eta = int(min(x, 0) <= y)
    else:
        isolated = reciprocal_floor(b)-reciprocal_floor(b-1) == 2
        patch = reciprocal_floor(b-1)-reciprocal_floor(b-3) == 4
        assert not (isolated and patch)
        E = ZERO
        if isolated:
            E = UNIT[(reciprocal_floor(b)-2*b) % 3]
        if patch:
            E = UNIT[(reciprocal_floor(b-1)-1-2*b) % 3]
        eta = int(x <= E[0] and x-y <= E[0]-E[1])
    return 1-3*eta


corner_sum, nonzero = Fraction(0), []
for a in range(max_a+1):
    for b in range(max_b+1):
        TT = coefficient(AT, BT, true_b, a, b)
        MT = coefficient(AM, BT, true_b, a, b)
        TM = coefficient(AT, BM, model_b, a, b)
        MM = coefficient(AM, BM, model_b, a, b)
        mixed = TT-MT-TM+MM
        assert abs(mixed) <= 6
        if a < R or b < S:
            assert mixed == 0
        if mixed:
            nonzero.append((a, b, mixed))
        corner_sum += Fraction(mixed, 2**a*3**b)
assert nonzero and abs(corner_sum) <= Fraction(18, 2**R*3**S)

print(f"PASS: 25 induced record-hit levels; {len(nonzero)} nonzero actual mixed corners in the targeted rectangle; first {nonzero[0]}.")
