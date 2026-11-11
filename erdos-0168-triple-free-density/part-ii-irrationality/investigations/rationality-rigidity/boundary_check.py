"""Exact actual boundary-response coefficient; no infinite-return claim."""
from fractions import Fraction as F


ONE, ZERO = (1, 0), (0, 0)
S = (ONE, (0, -1), ZERO)
P = (ONE, (1, 1), ZERO)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0] - z[1]
    return z


def board(cutoff):
    out, power3, b = ZERO, 1, 0
    while power3 <= cutoff:
        last = (cutoff // power3).bit_length() - 1
        for a in range(last + 1):
            out = add(out, rot(ONE, a - b))
        power3 *= 3
        b += 1
    return out


def horizontal(width):
    values, power2, power3, floor_alpha = [ONE], 1, 1, 0
    for a in range(1, width):
        power2 *= 2
        while 3 * power3 <= power2:
            power3 *= 3
            floor_alpha += 1
        assert power3 <= power2 < 3 * power3
        values.append(add(values[-1], rot(S[floor_alpha % 3], -a)))
    return values


def vertical(width):
    values = [ONE]
    for b in range(1, width):
        floor_beta = (3 ** b).bit_length() - 1
        values.append(add(values[-1], rot(P[floor_beta % 3], -2 * b)))
    return values


def rho(z):
    return max(abs(z[1] - z[0]), abs(z[0]))


def low_one(z):
    return int(z[0] >= 1 and z[1] >= 0)


def check():
    aa, bb = horizontal(3200), vertical(9)
    for a in range(49):
        assert aa[a] == rot(board(2 ** a), -a)
    for b in range(9):
        assert bb[b] == rot(board(3 ** b), -2 * b)
    assert bb[1] == ZERO and bb[4] == (0, 1)
    floors = [(3 ** b).bit_length() - 1 for b in range(5)]
    assert floors[4] - floors[3] == 2
    event4 = rot(ONE, floors[4] - 8)
    assert event4 == bb[4]
    states = [(aa[3 * n][0] - 1, aa[3 * n][1]) for n in range(1067)]
    assert low_one(states[0]) == 0 and low_one(states[2]) == 1
    for radius, expected in ((0, 1), (1, 32), (2, 1065)):
        stop = next(n for n, z in enumerate(states) if rho(z) > radius)
        assert stop == expected and all(rho(z) <= radius for z in states[:stop])
        head = 0
        for z in states[:stop]:
            head = 8 * head + low_one(z)
        terminal = F(low_one(states[stop]), 7)
        value = lambda c: (head + c + terminal) / 8 ** stop
        c0, c1 = F(1, 7), F(2, 7)
        slope = F(8, 3) * (value(c1) - value(c0)) / (c1 - c0)
        assert slope == F(1, 3 * 8 ** (stop - 1))
        assert slope.denominator.bit_length() == 3 * stop - 1
        print('RADIUS', radius, 'FIRST_EXIT', stop,
              'RESPONSE_DEN_BITS', slope.denominator.bit_length())
    print('PASS: original boards, genuine low row, exact full-source response')


if __name__ == '__main__':
    check()
