"""Independent integer-period and whole-numerator audit; no project imports."""
from fractions import Fraction
from math import gcd


ROOTS = ((1, 0), (0, 1), (-1, -1))


def plus(z, w):
    return z[0] + w[0], z[1] + w[1]


def turn(z, k):
    x, y = z
    return ((x, y), (-y, x-y), (y-x, -x))[k % 3]


def product(z, w):
    x, y = z
    u, v = w
    return x*u-y*v, x*v+y*u-y*v


def cutoff(k, p, q, side):
    n, r = divmod(k*p, q)
    return n - int(k > 0 and not r and side < 0)


def independent_digits(p, q, side):
    def axis(length, numerator, denominator, tie, vertical):
        states = [(1, 0)]
        partial = ((1, 0), (1, 1), (0, 0)) if vertical else ((1, 0), (0, -1), (0, 0))
        for k in range(1, 2*length+1):
            states.append(plus(states[-1], turn(partial[cutoff(k, numerator, denominator, tie) % 3], k if vertical else -k)))
        assert states[:length+1] == states[length:]
        return states[:length]

    aa = axis(3*q, p, q, side, False)
    bb = axis(3*p, q, p, -side, True)

    def birth(a, b):
        first = plus((1, 0), tuple(-v for v in ROOTS[-a % 3]))
        second = plus((1, 0), tuple(-v for v in ROOTS[-2*b % 3]))
        correction = product(first, second)
        assert not correction[0] % 3 and not correction[1] % 3
        z = plus(plus(aa[a % (3*q)], bb[b % (3*p)]), (correction[0]//3-1, correction[1]//3))
        if b >= 4:
            m = lambda k: cutoff(k, q, p, -side)
            isolate = m(b)-m(b-1) == 2
            patch = m(b-1)-m(b-3) == 4
            assert not (isolate and patch)
            if isolate or patch:
                e = ROOTS[(m(b)-2*b if isolate else m(b-1)-1-2*b) % 3]
                z = z[0]-e[0], z[1]-e[1]
        x, y = z
        if b == 0:
            return 0
        if b == 1:
            return int(x >= 1 and y >= 0)
        if b == 2:
            return int(x <= -1 and x <= y)
        if b == 3:
            return min(x, y, 0)-min(x-1, y, -1)
        return min(x, y, 0)-min(x-1, y, 0)

    return birth


def token_birth(p, q, side, a, b):
    grade = p*a+q*b
    before, arriving = [0]*3, [0]*3
    for original_b in range(grade//q+2):
        for original_a in range(grade//p+4):
            if original_b == 0 and original_a >= 1:
                i, j = original_a-1, 1
            elif original_b == 1 and original_a >= 2:
                i, j = original_a-3, 3
            else:
                i, j = original_a, original_b
            key = p*i+q*j, side*i
            target = grade, side*a
            if key < target:
                before[(original_a-original_b) % 3] += 1
            elif key == target:
                arriving[(original_a-original_b) % 3] += 1
    return min(before[i]+arriving[i] for i in range(3))-min(before)


def complete_blocks(p, q, side):
    birth = independent_digits(p, q, side)
    for a, b in ((0, 0), (0, 1), (1, 1), (2, 1), (0, 4), (q, 1), (q+1, 2), (q+2, 3), (q+3, p+4)):
        expected = 1 if (a, b) == (0, 1) else birth(a, b)
        assert token_birth(p, q, side, a, b) == expected
    assert token_birth(p, q, side, -1, 3) == 0
    a, b = 2**q, 3**p
    A, B = a**3-1, b**3-1
    twos = [2**k for k in range(3*q)]
    threes = [3**k for k in range(3*p+4)]
    heads, tiles = [0]*3, [[0]*3 for _ in range(3)]
    whole_head = whole_tile = 0
    for column in range(3*q):
        i, r = divmod(column, q)
        low = sum((1-3*birth(column, row))*threes[3-row] for row in range(4))
        heads[i] += twos[q-1-r]*low
        whole_head += twos[3*q-1-column]*low
        subtiles, full = [0]*3, 0
        for k in range(3*p):
            j, t = divmod(k, p)
            c = 1-3*birth(column, k+4)
            subtiles[j] += c*threes[p-1-t]
            full += c*threes[3*p-1-k]
        for j in range(3):
            tiles[i][j] += twos[q-1-r]*subtiles[j]
        whole_tile += twos[3*q-1-column]*full
    W = [B*heads[i]+sum(b**(2-j)*tiles[i][j] for j in range(3)) for i in range(3)]
    Y = [sum(a**(2-i)*tiles[i][j] for i in range(3)) for j in range(3)]
    N = 2*sum(a**(2-i)*W[i] for i in range(3))-27*A*B
    horizontal = 1-Fraction(1, a**3)
    vertical = 1-Fraction(1, b**3)
    direct = Fraction(whole_head, 27*twos[-1])/horizontal + Fraction(whole_tile, twos[-1]*threes[3*p+3])/(horizontal*vertical)-1
    assert direct == Fraction(N, 27*A*B)
    residues = (2*sum(W), 2*((W[1]-W[0])*a+W[2]-W[0]), 2*sum(Y), 2*((Y[1]-Y[0])*b+Y[2]-Y[0]))
    moduli = a-1, a*a+a+1, b-1, b*b+b+1
    assert all((N-residue) % modulus == 0 for residue, modulus in zip(residues, moduli))
    return N, residues, direct


def val(n, prime):
    assert n
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent


def check(case):
    p, q, P, Q, side, bits = case
    a, b, U, V = 2**q, 3**p, 2**Q, 3**P
    A, B = a**3-1, b**3-1
    N, residues, z = complete_blocks(p, q, side)
    assert z.denominator.bit_length() == bits
    s2, s3 = val(B, 2), val(A, 3)
    A0, B0 = A//3**s3, B//2**s2
    A1 = (a-1)//3**val(a-1, 3)
    A2 = (a*a+a+1)//3**val(a*a+a+1, 3)
    B1 = (b-1)//2**val(b-1, 2)
    B2 = b*b+b+1
    assert A1*A2 == A0 and B1*B2 == B0
    assert gcd(A1, A2) == gcd(B1, B2) == 1
    for h, T in (((1, 2, -3), 7), ((3, -5, 6), 14), ((-7, 4, 9), 10), ((1, 1, 1), 1), ((0, 0, 12), 35)):
        poly = lambda t: (h[0]*t+h[1])*t+h[2]
        L = 27*T*U*V*A*B
        offset = 27*side*(V*B*poly(a)-U*A*poly(b))
        test_N = [N, 0, 1, -1]
        if gcd(T, A0*B0) == 1:
            artificial = (-offset*pow(T*U*V, -1, A0*B0)) % (A0*B0)
            test_N.append(artificial)
            assert (T*U*V*artificial+offset) % (A0*B0) == 0
        for n in test_N:
            J = T*U*V*n+offset
            assert Q > s2+val(h[2], 2) and P > 3+s3+val(h[2], 3)
            assert val(J, 2) == s2+val(h[2], 2)
            assert val(J, 3) == 3+s3+val(h[2], 3)
            hS = 2**val(h[2], 2)*3**val(h[2], 3)
            TS = 2**val(T, 2)*3**val(T, 3)
            T0 = T//TS
            g = gcd(abs(J), A0*B0)
            e = gcd(abs(J), T0*A0*B0)//g
            assert T0 % e == 0
            assert gcd(abs(J), L) == 27*2**s2*3**s3*hS*e*g
            den = Fraction(J, L).denominator
            assert den == (U*V*TS//hS)*(T0*A0*B0//(e*g))
            rA, rB = T*U*n+27*side*B*poly(a), T*V*n-27*side*A*poly(b)
            gA, gB = gcd(abs(rA), A0), gcd(abs(rB), B0)
            assert gA == gcd(abs(J), A0) and gB == gcd(abs(J), B0)
            assert gA*gB % g == 0 and gcd(A0, B0) % (gA*gB//g) == 0
            assert gA == gcd(abs(rA), A1)*gcd(abs(rA), A2)
            assert gB == gcd(abs(rB), B1)*gcd(abs(rB), B2)
            if n == N:
                reduced = lambda t: (h[1]-h[0])*t+h[2]-h[0]
                corrected_residues = (T*U*residues[0]+27*side*B*sum(h), T*U*residues[1]+27*side*B*reduced(a), T*V*residues[2]-27*side*A*sum(h), T*V*residues[3]-27*side*A*reduced(b))
                assert all((r-residue) % modulus == 0 for r, residue, modulus in zip((rA, rA, rB, rB), corrected_residues, (A1, A2, B1, B2)))
                assert z+side*(Fraction(poly(a), T*U*A)-Fraction(poly(b), T*V*B)) == Fraction(J, L)
                assert Fraction(den, 2**(q+2*Q)) == Fraction(U*V, 2**(2*Q))*Fraction(T, hS*e)*Fraction(A0*B0, 2**q*g)
    print('INDEPENDENT_WHOLE_NUMERATOR', (p, q), 'model_bits', bits)
    return N


if __name__ == '__main__':
    for case in ((5, 8, 12, 19, 1, 44), (12, 19, 41, 65, -1, 108), (53, 84, 306, 485, -1, 507), (306, 485, 665, 1054, 1, 2908)):
        check(case)
    print('PASS: independent full periods, original-token spots, four true residues and whole-J gcd factorization')
