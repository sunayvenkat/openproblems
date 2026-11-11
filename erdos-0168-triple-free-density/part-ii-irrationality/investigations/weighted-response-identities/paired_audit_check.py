"""Independent exact evaluator for the named two-response cancellation."""
from fractions import Fraction as F
from math import gcd, lcm


ROOT = ((1, 0), (0, 1), (-1, -1))
COR = (((0, 0), (0, 0), (0, 0)),
       ((0, 0), (1, 0), (1, 1)),
       ((0, 0), (0, -1), (1, 0)))


def rotate(z, k):
    x, y = z
    return ((x, y), (-y, x - y), (y - x, -x))[k % 3]


def axes(na, nb, horizontal_floor, vertical_floor):
    out = []
    for size, floor, increments, multiplier in (
        (na, horizontal_floor, ((1, 0), (0, -1), (0, 0)), -1),
        (nb, vertical_floor, ((1, 0), (1, 1), (0, 0)), -2),
    ):
        row = [(1, 0)]
        for k in range(1, size):
            dx, dy = rotate(increments[floor(k) % 3], multiplier * k)
            x, y = row[-1]
            row.append((x + dx, y + dy))
        out.append(row)
    return out


def coefficient(a, b, aa, bb, floor):
    dx, dy = COR[a % 3][b % 3]
    x, y = aa[a][0] + bb[b][0] + dx - 1, aa[a][1] + bb[b][1] + dy
    if b >= 4:
        isolate, patch = floor(b) - floor(b - 1) == 2, floor(b - 1) - floor(b - 3) == 4
        assert not (isolate and patch)
        if isolate or patch:
            exponent = floor(b) - 2 * b if isolate else floor(b - 1) - 1 - 2 * b
            dx, dy = ROOT[exponent % 3]
            x, y = x - dx, y - dy
        born = x <= 0 and x - y <= 0
    elif b == 0:
        born = False
    elif b == 1:
        born = x >= 1 and y >= 0
    elif b == 2:
        born = x <= -1 and x - y <= 0
    else:
        born = min(x, 0) <= y
    return 1 - 3 * born


def rectangle(width, start, height, aa, bb, floor):
    # Column-major Horner summation, independently of the companion row-major code.
    numerator = 0
    for a in range(width):
        column = 0
        for b in range(start, start + height):
            column = 3 * column + coefficient(a, b, aa, bb, floor)
        numerator = 2 * numerator + column
    return F(numerator, 2 ** (width - 1) * 3 ** (start + height - 1))


def model(p, q, sign):
    def side(k, p, q, sign):
        quotient, remainder = divmod(k * p, q)
        return quotient - (k > 0 and remainder == 0 and sign < 0)
    aperiod, bperiod = 3 * q, 3 * p
    fa = lambda k: side(k, p, q, sign)
    fb = lambda k: side(k, q, p, -sign)
    aa, bb = axes(aperiod, bperiod + 4, fa, fb)
    head = rectangle(aperiod, 0, 4, aa, bb, fb)
    tile = rectangle(aperiod, 4, bperiod, aa, bb, fb)
    return (head + tile / (1 - F(1, 3 ** bperiod))) / (1 - F(1, 2 ** aperiod)) - 1


def tau(t):
    counts, b, p3 = [0, 0, 0], 0, 1
    while p3 <= t:
        top = (t // p3).bit_length() - 1
        for r in range(3):
            if top >= r:
                counts[(r - b) % 3] += (top - r) // 3 + 1
        b, p3 = b + 1, p3 * 3
    a, e = 1, 2
    while e <= t:
        if 3 * e > 2 * t or (6 * e <= t and 4 * t < 27 * e):
            counts[a % 3] -= 1
        a, e = a + 1, e * 2
    return min(counts)


def ln_interval(t, terms=48):
    partial = sum((2 * t ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), F(0))
    tail = 2 * t ** (2 * terms + 1) / ((2 * terms + 1) * (1 - t * t))
    return partial, partial + tail


def run():
    l2, u2 = ln_interval(F(1, 3))
    l3, u3 = ln_interval(F(1, 2))
    lo, hi = l2 / u3, u2 / l3
    p0, p1, q0, q1, convergents = 0, 1, 1, 0, []
    while True:
        digit = lo.numerator // lo.denominator
        assert digit == hi.numerator // hi.denominator
        p, q = digit * p1 + p0, digit * q1 + q0
        convergents.append((p, q))
        if q > 2000:
            break
        p0, p1, q0, q1 = p1, p, q1, q
        lo, hi = 1 / (hi - digit), 1 / (lo - digit)
    for current, successor, sign in (((12, 19), (41, 65), -1), ((306, 485), (665, 1054), 1)):
        i = convergents.index(current)
        assert convergents[i + 1] == successor
        p, q = current
        assert ((2 ** q > 3 ** p) - (2 ** q < 3 ** p)) == sign
    for r, s in ((53, 84), (971, 1539)):
        h = [0, 0]
        for a in range(s):
            x, y = ROOT[(a + a * r // s) % 3]
            h[0], h[1] = h[0] + x, h[1] + y
        assert (r % 3, s % 3, tuple(h)) == (2, 0, (2, 1))

    a1, a2 = -(3 ** 53 - 2 ** 84), 3 ** 971 - 2 ** 1539
    k1, k2 = 2 ** 84 * 3 ** 53, 2 ** 1539 * 3 ** 971
    assert abs(84 * 971 - 1539 * 53) == 3
    assert gcd(abs(a1), abs(a2)) == gcd(2 ** 3 - 1, 3 ** 3 - 1) == 1
    lam, mu = a2, -a1 * (k2 // k1)
    assert lam * F(a1, k1) + mu * F(a2, k2) == 0
    assert gcd(abs(lam), abs(mu)) == 1
    assert (abs(lam).bit_length(), abs(mu).bit_length()) == (1530, 2986)
    z1, z2 = model(12, 19, -1), model(306, 485, 1)
    assert (z1.denominator.bit_length(), z2.denominator.bit_length()) == (108, 2908)
    ell, k = lcm(z1.denominator, z2.denominator), lam + mu
    m1, m2 = int(ell * z1), int(ell * z2)
    j = lam * m1 + mu * m2
    prediction = F(j, k * ell)
    assert prediction.denominator == abs(k) * ell // gcd(abs(j), abs(k) * ell)
    assert prediction.denominator.bit_length() == 5975
    assert gcd(abs(k), abs(j)) == gcd(abs(k), abs(m1 - m2))

    width, height = 1800, 1200
    floors_a, power2, power3, exponent = [0], 1, 1, 0
    for a in range(1, width):
        power2 *= 2
        while power3 * 3 <= power2:
            power3, exponent = 3 * power3, exponent + 1
        floors_a.append(exponent)
    floor_b = lambda b: (3 ** b).bit_length() - 1
    aa, bb = axes(width, height, floors_a.__getitem__, floor_b)
    for a, b in ((0, 0), (0, 1), (0, 2), (1, 1), (6, 0), (5, 4), (4, 11),
                 (19, 12), (28, 31), (53, 36), (71, 12), (2, 93)):
        t = 2 ** a * 3 ** b
        direct = 1 - 3 * (tau(t) - tau(t - 1))
        value = coefficient(a, b, aa, bb, floor_b) - (3 if (a, b) == (0, 1) else 0)
        assert value == direct, (a, b, value, direct)
    center = rectangle(width, 0, height, aa, bb, floor_b) - 1
    radius = 6 * (F(1, 2 ** width) + F(1, 3 ** height) - F(1, 2 ** width * 3 ** height))
    rcenter, rradius = k * center - F(j, ell), abs(k) * radius
    low, high = abs(rcenter) - rradius, abs(rcenter) + rradius
    assert F(2) ** 1419 < low < high < F(2) ** 1420
    low, high = prediction.denominator * low / abs(k), prediction.denominator * high / abs(k)
    assert F(2) ** 4408 < low < high < F(2) ** 4409
    print('PASS: independent model sums, actual CF/state/board inputs, affine gcd, and complete 4408/4409 return enclosure')


if __name__ == '__main__':
    run()
