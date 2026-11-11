from fractions import Fraction as F


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(k, x):
    return k * x[0], k * x[1]


def det(x, y):
    return x[0] * y[1] - x[1] * y[0]


def color(x):
    return (x[0] - x[1]) % 3


def power(base, n):
    return F(base**n) if n >= 0 else F(1, base**(-n))


def arrival(x, asymptotic=False):
    a, b = x
    assert a >= 0 and b >= 0
    t = F(2**a * 3**b)
    if b == 0 and (a >= 1 or asymptotic):
        t *= F(3, 2)
    if b == 1 and (a >= 2 or asymptotic):
        t *= F(9, 8)
    return t


def shapes(u, v):
    return ((0, 0), u, v), (add(u, v), mul(2, u), add(mul(2, u), v))


def owner(x, u, v):
    d = det(u, v)
    assert abs(d) == 1
    i = (v[1] * x[0] - v[0] * x[1]) // d
    j = (-u[1] * x[0] + u[0] * x[1]) // d
    n, ri = divmod(i, 3)
    m, rj = divmod(j, 2)
    typ = 0 if (ri, rj) in ((0, 0), (1, 0), (0, 1)) else 1
    anchor = add(mul(3*n, u), mul(2*m, v))
    return typ, tuple(add(anchor, z) for z in shapes(u, v)[typ])


def families(u, v):
    # Each six-period family is specified by a coordinatewise minimum.
    out = []
    cosets = {tuple(z % 6 for z in add(mul(3*n, u), mul(2*m, v)))
              for n in range(2) for m in range(3)}
    assert len(cosets) == 6
    for typ, sh in enumerate(shapes(u, v)):
        lo = tuple(min(z[k] for z in sh) for k in range(2))
        normalized = tuple((z[0]-lo[0], z[1]-lo[1]) for z in sh)
        for z in cosets:
            out.append((typ, ((z[0]+lo[0]) % 6, (z[1]+lo[1]) % 6), normalized))
    assert len(out) == 12
    return out


def bulk_cost(u, v):
    out = F(0)
    first_vertex, first_complete = None, None
    for typ, (a0, b0), sh in families(u, v):
        triple = tuple((a0+x, b0+y) for x, y in sh)
        assert owner(triple[0], u, v)[0] == typ
        assert set(owner(triple[0], u, v)[1]) == set(triple)
        times = [arrival(x) for x in triple]
        first_vertex = min(times + ([first_vertex] if first_vertex is not None else []))
        first_complete = min(max(times), first_complete) if first_complete is not None else max(times)
        # High rows have no retiming; both geometric directions are exact.
        bh = b0 if b0 >= 2 else b0 + 6
        high_max = max(power(2, a0+x) * power(3, bh+y) for x, y in sh)
        out += 1 / high_max / (1-F(1, 64)) / (1-F(1, 729))
        for k in range(3):
            assert max(arrival((a0+x+6*k, bh+y)) for x, y in sh) == high_max * 64**k
        if b0 < 2:
            actual_max = max(times)
            asym_max = max(arrival(x, True) for x in triple)
            out += 1 / actual_max + 1 / asym_max / 63
            for k in (1, 2):
                assert max(arrival((a0+x+6*k, b0+y)) for x, y in sh) == asym_max * 64**k
    return out, first_vertex, first_complete


def positive_basis(cfs, n, digits):
    cur = cfs[n]
    prev = cfs[n-1]
    x, y = (cur[1], -cur[0]), (prev[1], -prev[0])
    cx, cy = color(x), color(y)
    if cx and cy and cx != cy:
        return x, y
    if not cx:
        return y, add(x, mul(-1, y))
    if not cy:
        z = (cfs[n-2][1], -cfs[n-2][0])
        return z, add(y, mul(-1, z))
    if digits[n] >= 2:
        return y, add(x, mul(-2, y))
    res = (cfs[n-2][1], -cfs[n-2][0])
    z = (cfs[n-3][1], -cfs[n-3][0])
    assert color(res) == 0
    return z, add(res, mul(-1, z))


if __name__ == '__main__':
    digits = [0, 1, 1, 1, 2, 2, 3, 1, 5]
    cfs = []
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    for a in digits:
        p, q = a*pm1+pm2, a*qm1+qm2
        cfs.append((p, q))
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    assert cfs[4:] == [(5, 8), (12, 19), (41, 65), (53, 84), (306, 485)]
    assert 2**485 > 3**306 and 2**569 < 3**359
    checked = []
    for n in range(4, len(cfs)):
        u, v = positive_basis(cfs, n, digits)
        assert abs(det(u, v)) == 1 and {color(u), color(v)} == {1, 2}
        assert min(u[0], v[0], -u[1], -v[1]) > 0
        h, k = max(u[0], v[0]), max(-u[1], -v[1])
        assert h <= cfs[n][1] and k <= cfs[n][0]
        for a in range(-12, 13):
            for b in range(-12, 13):
                typ, triple = owner((a, b), u, v)
                assert (a, b) in triple and len(set(triple)) == 3
                assert {color(z) for z in triple} == {0, 1, 2}
                assert set(owner((a+6, b), u, v)[1]) == {add(z, (6, 0)) for z in triple}
                assert set(owner((a, b+6), u, v)[1]) == {add(z, (0, 6)) for z in triple}
                assert max(z[0] for z in triple)-min(z[0] for z in triple) == h
                assert max(z[1] for z in triple)-min(z[1] for z in triple) == k
        cost, first, complete = bulk_cost(u, v)
        clear = 2**5 * 3**3 * 63 * 728 * 2**h * 3**k
        assert (clear * cost).denominator == 1
        checked.append((cfs[n], u, v, h, k, cost, first, complete))
    for row in checked:
        print(row)
    # The all-one comparison prefix exercises the zero-color and fallback cases.
    one_digits = [0] + [1]*9
    one_cfs = []
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    for a in one_digits:
        p, q = a*pm1+pm2, a*qm1+qm2
        one_cfs.append((p, q))
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    assert [color((q, -p)) for p, q in one_cfs[6:9]] == [0, 1, 1]
    for n in (6, 7, 8):
        u, v = positive_basis(one_cfs, n, one_digits)
        assert abs(det(u, v)) == 1 and {color(u), color(v)} == {1, 2}
        assert 0 < min(u[0], v[0], -u[1], -v[1])
        assert max(u[0], v[0]) <= one_cfs[n][1]
        assert max(-u[1], -v[1]) <= one_cfs[n][0]
    print('PASS: ownership, colors, period six, spans, exact bulk resummation and clearance')
