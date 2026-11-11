"""Independent exact fan arithmetic and original-board response interface."""
from fractions import Fraction as F
from math import gcd, lcm


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def neg(z):
    return -z[0], -z[1]


def mul(z, w):
    return z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0] - z[1]*w[1]


def rot(z, k):
    return mul(z, ((1, 0), (0, 1), (-1, -1))[k % 3])


def floor_side(n, p, q, side):
    quotient, remainder = divmod(n*p, q)
    return quotient - int(n > 0 and remainder == 0 and side < 0)


def exact_model_numerator(p, q, side):
    """Integer Horner evaluation of the accepted complete scalar period."""
    height, width = 3*p, 3*q
    aa, bb = [(1, 0)], [(1, 0)]
    for a in range(1, width):
        step = ((1, 0), (0, -1), (0, 0))[floor_side(a, p, q, side) % 3]
        aa.append(add(aa[-1], rot(step, -a)))
    for b in range(1, height):
        step = ((1, 0), (1, 1), (0, 0))[floor_side(b, q, p, -side) % 3]
        bb.append(add(bb[-1], rot(step, -2*b)))
    correction = (((0, 0), (0, 0), (0, 0)),
                  ((0, 0), (1, 0), (1, 1)),
                  ((0, 0), (0, -1), (1, 0)))

    def row(b):
        event = (0, 0)
        if b >= 4:
            m = lambda k: floor_side(k, q, p, -side)
            isolate = m(b)-m(b-1) == 2
            patch = m(b-1)-m(b-3) == 4
            assert not (isolate and patch)
            if isolate:
                event = rot((1, 0), m(b)-2*b)
            if patch:
                event = rot((1, 0), m(b-1)-1-2*b)
        result = 0
        for a in range(width):
            z = add(add(aa[a], bb[b % height]), correction[a % 3][b % 3])
            x, y = add(z, neg(add((1, 0), event)))
            if b >= 4:
                eta = min(x, y, 0)-min(x-1, y, 0)
            elif b == 0:
                eta = 0
            elif b == 1:
                eta = int(x >= 1 and y >= 0)
            elif b == 2:
                eta = int(x <= -1 and x-y <= 0)
            else:
                eta = int(min(x, 0) <= y)
            if (a, b) == (0, 1):
                eta = 0
            result = 2*result + 1-3*eta
        return result

    head = 0
    for b in range(4):
        head = 3*head + row(b)
    tile = 0
    for b in range(4, height+4):
        tile = 3*tile + row(b)
    A, B = 2**width-1, 3**height-1
    return 2*B*head+2*tile-27*A*B


def valuation(n, prime):
    assert n
    count = 0
    while n % prime == 0:
        count += 1
        n //= prime
    return count


def arithmetic():
    cases = ((12, 19, 41, 65, -1, 238),
             (53, 84, 306, 485, -1, 1465),
             (306, 485, 665, 1054, 1, 5013))
    for p, q, P, Q, sigma, bits in cases:
        a, b, U, V = 2**q, 3**p, 2**Q, 3**P
        A, B = a**3-1, b**3-1
        x, y = F(1, a), F(1, b)
        C = tuple(F(1, U)*x**j/(1-x**3)-F(1, V)*y**j/(1-y**3)
                  for j in (1, 2, 3))
        assert C == tuple(F(a**(3-j), U*A)-F(b**(3-j), V*B) for j in (1, 2, 3))
        den = C[2].denominator
        common = lcm(*(c.denominator for c in C))
        assert den == common and den.bit_length() == bits
        assert valuation(den, 2) == Q and valuation(den, 3) == P
        A0, B0 = A // 3**valuation(A, 3), B // 2**valuation(B, 2)
        cross = gcd(A0, B0)
        assert den % (U*V*(A0//cross)*(B0//cross)) == 0
        assert (U*V*A0*B0) % den == 0
        assert F(common, 2**(q+2*Q)) > 2**(4*q)
        N = exact_model_numerator(p, q, sigma)
        z = F(N, 27*A*B)
        for h, T in (((1, 1, 1), 1), ((1, -1, 0), 7), ((1, 0, 0), 11),
                     ((0, 0, 1), 3), ((1, 2, -3), 13)):
            poly = lambda t: h[0]*t*t+h[1]*t+h[2]
            correction = sum((F(h[j], T)*C[j] for j in range(3)), F(0))
            left, right = F(poly(a), T*U*A), F(poly(b), T*V*B)
            assert correction == left-right
            common_divisor = gcd(left.denominator, right.denominator)
            lower_divisor = left.denominator*right.denominator//common_divisor**2
            assert correction.denominator % lower_divisor == 0
            L = 27*T*U*V*A*B
            J = T*U*V*N+27*sigma*(V*B*poly(a)-U*A*poly(b))
            prediction = z+sigma*correction
            assert prediction == F(J, L)
            reduced = L//gcd(abs(J), L)
            assert prediction.denominator == reduced
            unit_majorant = F(reduced, 2**(q+2*Q))
            assert unit_majorant == F(L, gcd(abs(J), L)*2**(q+2*Q))
        print('EXACT_FAN', (p, q), 'bits', bits, 'model_bits', z.denominator.bit_length())


def board_counts(t):
    counts = [0, 0, 0]
    b, power3 = 0, 1
    while power3 <= t:
        a, value = 0, power3
        while value <= t:
            counts[(a-b) % 3] += 1
            a, value = a+1, 2*value
        b, power3 = b+1, 3*power3
    return counts


def tau(t):
    counts = board_counts(t)
    exponent, root = 1, 2
    while root <= t:
        if 3*root > 2*t or (6*root <= t and 4*t < 27*root):
            counts[exponent % 3] -= 1
        exponent, root = exponent+1, 2*root
    return min(counts)


def direct_axis(n, vertical=False):
    counts = board_counts((3 if vertical else 2)**n)
    return rot((counts[0]-counts[2], counts[1]-counts[2]), n if vertical else -n)


def actual_response(pr, qr, endpoint, a, b):
    aa, bb = direct_axis(a), direct_axis(b, True)
    gamma = (2*pr-qr) % 3
    cumulative = ((0, 0), (-1, -1), (-1, 0))[a % 3]
    residue = rot(mul(((0, 0), (1, 0), (0, -1))[pr], cumulative), -qr)
    shifted = add(add(endpoint, rot(add(aa, (-1, 0)), gamma)), residue)
    correction = (((0, 0), (0, 0), (0, 0)),
                  ((0, 0), (1, 0), (1, 1)),
                  ((0, 0), (0, -1), (1, 0)))
    def beta(k):
        return (3**k).bit_length()-1
    event = (0, 0)
    if beta(b)-beta(b-1) == 2:
        event = rot((1, 0), beta(b)-2*b)
    elif beta(b-1)-beta(b-3) == 4:
        event = rot((1, 0), beta(b-1)-1-2*b)
    plus = add(add(add(shifted, bb), correction[(a+qr) % 3][b % 3]),
               neg(add((1, 0), event)))
    minus = add(plus, neg(rot((1, 0), gamma)))
    def birth(z):
        x, y = z
        return min(x, y, 0)-min(x-1, y, 0)
    return -3*(birth(plus)-birth(minus))


def determinant(rows):
    matrix = [list(map(F, row)) for row in rows]
    value = F(1)
    for j in range(len(rows)):
        pivot = next(i for i in range(j, len(rows)) if matrix[i][j])
        if pivot != j:
            matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
            value = -value
        p = matrix[j][j]
        value *= p
        for i in range(j+1, len(rows)):
            ratio = matrix[i][j]/p
            for k in range(j+1, len(rows)):
                matrix[i][k] -= ratio*matrix[j][k]
            matrix[i][j] = 0
    return value


def rank_interface():
    states = ((0, 1, (0, -1)), (1, 1, (0, 0)), (2, 0, (1, 0)),
              (2, 2, (1, 0)), (1, 2, (1, 0)), (2, 1, (1, 0)))
    cells = ((0, 4), (0, 5), (0, 6), (0, 8), (0, 9), (0, 11), (0, 28), (2, 4))
    rows = []
    for a, b in cells:
        t = 2**a*3**b
        rows.append([1, 1-3*(tau(t)-tau(t-1))]
                    + [actual_response(*state, a, b) for state in states])
    assert determinant(rows) == -2187
    print('ORIGINAL_BOARD_RANK8_DETERMINANT', determinant(rows))


if __name__ == '__main__':
    arithmetic()
    rank_interface()
    print('PASS: independent exact fan/model normalization and rank8 reconstruction')
