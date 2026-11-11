"""General exact resonant (p+q = 0 mod 3) complete model, grouped by states.

Definitions copied from `Erdos 168 infinite return construction/resonant_models_check.py`
(exact_model), generalized to all four drift-table cases by the i<->j swap stated in
resonant_models.md, and summed by grouping cells by horizontal/vertical state keys.
"""
import sys
from fractions import Fraction as F
from math import gcd
from fastmodel import add, rot, side, CORR
sys.set_int_max_str_digits(0)


def ceildiv(a, b):
    return -((-a) // b)


def cone(z):
    return int(z[0] <= 0 and z[0] - z[1] <= 0)


def cone_sum(x, y, X, Y, lower):
    d = x - y
    if lower:
        stop = max(0, ceildiv(-x, 2), ceildiv(d - 2 * x, 3))
        head = sum((X ** i * Y ** max(0, 2 * i + x, ceildiv(i + d, 2)) for i in range(stop)), F(0)) / (1 - Y)
        return head + X ** stop * Y ** (2 * stop + x) / ((1 - Y) * (1 - X * Y ** 2))
    stop = max(0, d, ceildiv(x, 2), ceildiv(2 * x - d, 3))
    head = sum((X ** i * (1 - Y ** (min(2 * i - x, (i - d) // 2) + 1)) / (1 - Y)
                for i in range(stop) if min(2 * i - x, (i - d) // 2) >= 0), F(0))
    tail = X ** stop / ((1 - X) * (1 - Y))
    tail -= (X ** stop * Y ** ((stop - d) // 2 + 1) + X ** (stop + 1) * Y ** ((stop + 1 - d) // 2 + 1)) / ((1 - Y) * (1 - X ** 2 * Y))
    return head + tail


def build(p, q):
    assert gcd(p, q) == 1 and (p + q) % 3 == 0 and F(3, 5) < F(p, q) < F(2, 3)
    sigma = 1 if 2 ** q > 3 ** p else -1
    P, Q = 3 * q, 3 * p
    A, B = [(1, 0)], [(1, 0)]
    for a in range(1, 2 * P + 1):
        A.append(add(A[-1], rot(((1, 0), (0, -1), (0, 0))[side(a, p, q, sigma) % 3], -a)))
    for b in range(1, 2 * Q + 5):
        B.append(add(B[-1], rot(((1, 0), (1, 1), (0, 0))[side(b, q, p, -sigma) % 3], -2 * b)))
    da = (A[P][0] - 1, A[P][1]); db = (B[Q][0] - 1, B[Q][1])
    assert all(A[a + P] == add(A[a], da) for a in range(P + 1))
    assert all(B[b + Q] == add(B[b], db) for b in range(Q + 4))
    case = {((2, 1), (-1, 1)): ('lower', False), ((-2, -1), (1, -1)): ('upper', False),
            ((-1, 1), (2, 1)): ('lower', True), ((1, -1), (-2, -1)): ('upper', True)}[(da, db)]

    def state(a, b):
        i, r = divmod(a, P); j, s = divmod(b, Q)
        z = add(add(A[r], (i * da[0], i * da[1])), add(B[s], (j * db[0], j * db[1])))
        z = add(z, CORR[a % 3][b % 3])
        return z[0] - 1, z[1]

    def epsilon(b):
        m = lambda k: side(k, q, p, -sigma)
        iso, pat = m(b) - m(b - 1) == 2, m(b - 1) - m(b - 3) == 4
        assert not (iso and pat)
        color = (m(b) - 2 * b) % 3 if iso else (m(b - 1) - 1 - 2 * b) % 3
        return rot((1, 0), color) if iso or pat else (0, 0)

    def eta(a, b):
        x, y = state(a, b)
        if b == 0: return 0
        if b == 1: return 1 if a == 0 else int(x >= 1 and y >= 0)
        if b == 2: return int(x <= -1 and x - y <= 0)
        if b == 3: return int(min(x, 0) <= y)
        e = epsilon(b)
        return cone((x - e[0], y - e[1]))
    return dict(p=p, q=q, sigma=sigma, P=P, Q=Q, A=A, B=B, da=da, db=db, case=case,
                state=state, epsilon=epsilon, eta=eta)


def value(m):
    p, q, P, Q, A, B, da = m['p'], m['q'], m['P'], m['Q'], m['A'], m['B'], m['da']
    X, Y = F(1, 2 ** P), F(1, 3 ** Q)
    kind, swap = m['case']
    total = F(0)
    stats = dict(max_low_stop=0, max_state=0)
    # low rows: group by (b, state(a,b), a==0)
    for b in range(4):
        groups = {}
        for a in range(P):
            k = (m['state'](a, b), a == 0)
            groups[k] = groups.get(k, 0) + (1 << (P - 1 - a))
        for ((x, y), zero), h in groups.items():
            def dig(i):
                xx, yy = x + i * da[0], y + i * da[1]
                if b == 0: return 0
                if b == 1: return 1 if (zero and i == 0) else int(xx >= 1 and yy >= 0)
                if b == 2: return int(xx <= -1 and xx - yy <= 0)
                return int(min(xx, 0) <= yy)
            stop = abs(x) + abs(y) + 4
            assert all(dig(stop) == dig(stop + t) for t in range(1, 8))
            stats['max_low_stop'] = max(stats['max_low_stop'], stop)
            L = sum((dig(i) * X ** i for i in range(stop)), F(0)) + dig(stop) * X ** stop / (1 - X)
            total += L * F(h, 2 ** (P - 1)) / 3 ** b
    # tile b in [4, 4+Q)
    hg, vg = {}, {}
    for a in range(P):
        k = (A[a], a % 3); hg[k] = hg.get(k, 0) + (1 << (P - 1 - a))
    vdig = {}
    for b in range(4, 4 + Q):
        e = m['epsilon'](b)
        k = ((B[b][0] - e[0], B[b][1] - e[1]), b % 3)
        vdig.setdefault(k, bytearray(b'0' * Q))[b - 4] = 49
    vg = {k: int(v.decode(), 3) for k, v in vdig.items()}  # sum 3^{Q-1-(b-4)}
    cache = {}
    tile = F(0)
    for (za, ra), h in hg.items():
        acc = F(0)
        for (zb, rb), v in vg.items():
            c = CORR[ra][rb]
            x, y = za[0] + zb[0] + c[0] - 1, za[1] + zb[1] + c[1]
            stats['max_state'] = max(stats['max_state'], abs(x), abs(x - y))
            if (x, y) not in cache:
                cache[(x, y)] = cone_sum(x, y, Y, X, kind == 'lower') if swap else cone_sum(x, y, X, Y, kind == 'lower')
            acc += cache[(x, y)] * v
        tile += acc * h
    total += tile / (2 ** (P - 1) * 3 ** (Q - 1) * 81)
    return total, stats


def model_value(p, q):
    """Return (Ztilde, stats, model) with Ztilde = 3 - 3 * sum eta 2^-a 3^-b (complete model)."""
    m = build(p, q)
    tot, stats = value(m)
    return 3 - 3 * tot, stats, m


def brute_check(p, q):
    m = build(p, q)
    tot, _ = value(m)
    P, Q = m['P'], m['Q']
    part = sum((F(m['eta'](a, b), 2 ** a * 3 ** b) for a in range(2 * P) for b in range(2 * Q + 4)), F(0))
    tail = 3 * (F(1, 2 ** (2 * P)) + F(1, 3 ** (2 * Q + 4)) - F(1, 2 ** (2 * P) * 3 ** (2 * Q + 4)))
    assert 0 <= tot - part <= tail, (p, q)
    return True


def smooth(n):
    t = h = 0
    while n % 2 == 0: n //= 2; t += 1
    while n % 3 == 0: n //= 3; h += 1
    return t, h, n


if __name__ == '__main__':
    for p, q in ((7, 11), (8, 13), (22, 35), (29, 46)):
        brute_check(p, q)
        z, st, m = model_value(p, q)
        t, h, rest = smooth(z.denominator)
        print((p, q), m['case'], 'den bits', z.denominator.bit_length(), 'v2', t, 'v3', h, 'nonS', rest, st)
    # archived: 7/11 -> 2^13*3^5*(2^22*3^7-1); 8/13 -> 2^29*3^24*(2^13*3^16-1)/7
    z, _, _ = model_value(7, 11); assert z.denominator == 2**13*3**5*(2**22*3**7-1)
    z, _, _ = model_value(8, 13); assert z.denominator == 2**29*3**24*(2**13*3**16-1)//7
    print('PASS: matches archived 7/11, 8/13 reduced denominators; brute tail checks pass')
