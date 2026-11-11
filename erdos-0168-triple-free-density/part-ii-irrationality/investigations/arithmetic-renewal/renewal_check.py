"""Exact ordered one-axis calibration; no adequate-return claim."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import importlib.util


source = Path(__file__).parents[1] / 'Erdos 168 occupation arithmetic bridge' / 'exact_transport_check.py'
spec = importlib.util.spec_from_file_location('accepted_transport', source)
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
aa, bb = t.axes(6000)


@lru_cache(None)
def state(a, b):
    z = t.add(t.sub(t.add(aa[a], bb[b]), t.ONE), t.C[a % 3][b % 3])
    if b >= 4:
        z = t.sub(z, t.event(t.phase(b // 3, t.BETA), b % 3))
    return z


def rho(z):
    return max(abs(z[1] - z[0]), abs(z[0]))


def h(a, b):
    return t.cone(state(a, b)) if b >= 4 else t.low(state(a, b), b)


@lru_cache(None)
def q(a, b, radius):
    stop = 0
    while rho(state(a + 3 * stop, b)) <= radius:
        stop += 1
    num = 1 + h(a + 3 * stop, b)
    num += 7 * sum(8 ** (stop - 1 - n) * h(a + 3 * n, b) for n in range(stop))
    value = F(num, 7 * 8 ** stop)
    assert 0 <= value <= F(2, 7)
    return value, stop, num


@lru_cache(None)
def p(a, b, radius):
    assert b >= 4
    stop = 0
    while rho(state(a, b + 3 * stop)) <= radius:
        stop += 1
    rows = [q(a, b + 3 * m, radius) for m in range(stop)]
    height = max((row[1] for row in rows), default=0)
    terminal = h(a, b + 3 * stop)
    num = 26 * sum(27 ** (stop - 1 - m) * 8 ** (height - row[1]) * row[2]
                   for m, row in enumerate(rows)) + 8 ** height * (8 + terminal)
    value = F(num, 182 * 8 ** height * 27 ** stop)
    direct = sum((row[0] / 27 ** (m + 1) for m, row in enumerate(rows)), F())
    direct += F(8 + terminal, 182 * 27 ** stop)
    assert value == direct and 0 <= value <= F(9, 182)
    assert num % 13 != 0
    return value, stop, height


def ea(a, b, radius):
    value = 8 * q(a, b, radius)[0] - q(a + 3, b, radius)[0] - h(a, b)
    assert value == 0 if rho(state(a, b)) <= radius else F(6, 7) <= value <= F(9, 7)
    return value


def eb(a, b, radius):
    value = 27 * p(a, b, radius)[0] - p(a, b + 3, radius)[0] - q(a, b, radius)[0]
    assert value == 0 if rho(state(a, b)) <= radius else F(90, 91) <= value <= F(191, 182)
    return value


def valuation(n, prime):
    out = 0
    while n % prime == 0:
        n //= prime
        out += 1
    return out


def check():
    # Original boards and exact column sums certify the vertical-axis reduction.
    mul = lambda z, w: (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]-z[1]*w[1])
    for m in range(13):
        cutoff = 3 ** (3*m)
        board = t.ZERO
        for b in range(3*m+1):
            last = (cutoff // 3 ** b).bit_length()-1
            for a in range(last+1):
                board = t.add(board, t.rot(t.ONE, a-b))
        assert board == bb[3*m]
        last = t.floor_lin(0, 3*m, t.BETA)
        col1 = col2 = t.ZERO
        for a in range(last+1):
            col1 = t.add(col1, t.rot(t.ONE, a))
            ceiling = a - t.floor_lin(0, -a)
            col2 = t.add(col2, t.rot(t.ONE, ceiling))
        assert mul((2, 1), board) == t.sub(col1, t.rot(col2, -1))
    for radius in (0, 1, 2):
        high = 216 * sum((F(1, 2 ** i * 3 ** b) * p(i, b, radius)[0]
                          for i in range(3) for b in (6, 4, 5)), F())
        low = 8 * sum((F(1, 2 ** i * 3 ** b) * q(i, b, radius)[0]
                       for i in range(3) for b in range(4)), F())
        total = high + low
        den = total.denominator
        height = max([p(i, b, radius)[2] for i in range(3) for b in (6, 4, 5)]
                     + [q(i, b, radius)[1] for i in range(3) for b in range(4)])
        vertical = max(p(i, b, radius)[1] for i in range(3) for b in (6, 4, 5))
        common = 91 * 8 ** height * 27 ** (vertical+1)
        assert (common * total).denominator == 1 and common % den == 0
        e2, e3 = valuation(den, 2), valuation(den, 3)
        print('SOURCE', radius, 'DEN_BITS', den.bit_length(), 'V2', e2, 'V3', e3,
              'OTHER', den // (2 ** e2 * 3 ** e3),
              'H_T_GCD', (height, vertical, common // den),
              'HIGH_EXIT_HORIZONS', [(i, b, *p(i, b, radius)[1:])
                                     for i in range(3) for b in (6, 4, 5)])
        # An actual occupied exterior point gives a complete positive lower bound.
        first = next(n for n in range(1800) if rho(state(3 * n, 4)) > radius)
        witness = F(6, 7 * 8 ** first * 3 ** 4)
        cleared = den * witness
        assert common * witness == 26 * 8 ** (height-first) * 27 ** vertical
        print('CLEARED_WITNESS', radius, 'FIRST_N', first,
              'GREATER_THAN_ONE', cleared > 1,
              'FLOOR_LOG2', cleared.numerator.bit_length() - cleared.denominator.bit_length() - 1)
        assert cleared > 1
        # Four-by-four exact product pairing, retaining every terminal term.
        nmax, mmax, a0, b0 = 4, 4, 0, 4
        weighted = lambda f: sum((F(1, 8 ** n * 27 ** m) * f(a0 + 3*n, b0 + 3*m)
                                 for n in range(nmax) for m in range(mmax)), F())
        target = weighted(h)
        apos = weighted(lambda a, b: ea(a, b, radius))
        bpos = 8 * sum((eb(a0, b0 + 3*m, radius) / 27 ** m for m in range(mmax)), F())
        bterm = F(8, 8 ** nmax) * sum((eb(a0 + 3*nmax, b0 + 3*m, radius) / 27 ** m
                                      for m in range(mmax)), F())
        terminal = 216 * p(a0, b0, radius)[0]
        terminal -= F(216, 8 ** nmax) * p(a0 + 3*nmax, b0, radius)[0]
        terminal -= F(216, 27 ** mmax) * p(a0, b0 + 3*mmax, radius)[0]
        terminal += F(216, 8 ** nmax * 27 ** mmax) * p(a0 + 3*nmax, b0 + 3*mmax, radius)[0]
        assert target + apos + bpos - bterm == terminal
        for a in range(3):
            for b in range(4):
                ea(a, b, radius)
    print('PASS: nested sources, uncancelled13, residual bounds and complete product terminals')


if __name__ == '__main__':
    check()
