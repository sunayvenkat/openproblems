"""Exact guarded occupation transport; no arithmetic-bridge claim."""
from fractions import Fraction as F
from functools import cmp_to_key


def log_interval(t, terms=160):
    x = F(t-1, t+1)
    total = 2*sum((x**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    tail = 2*x**(2*terms+1)/F(2*terms+1)/(1-x*x)
    return total, total+tail


l2, l3 = log_interval(2), log_interval(3)
ALPHA = l2[0]/l3[1], l2[1]/l3[0]
BETA = 1/ALPHA[1], 1/ALPHA[0]
ONE, OM, OM2, ZERO = (1, 0), (0, 1), (-1, -1), (0, 0)
S, P = (ONE, (0, -1), ZERO), (ONE, (1, 1), ZERO)
C = ((ZERO, ZERO, ZERO), (ZERO, ONE, (1, 1)), (ZERO, (0, -1), ONE))


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def sub(x, y):
    return x[0]-y[0], x[1]-y[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0]-z[1]
    return z


def interval(r, s, bounds=ALPHA):
    ends = r+s*bounds[0], r+s*bounds[1]
    return min(ends), max(ends)


def floor_lin(r, s, bounds=ALPHA):
    lo, hi = interval(r, s, bounds)
    a, b = lo.numerator//lo.denominator, hi.numerator//hi.denominator
    assert a == b
    return a


def phase(n, bounds):
    return F(-floor_lin(0, n, bounds)), F(n)


def displacement(x, length, bounds, vertical=False):
    r, s = x
    out = ZERO
    for k in range(1, length+1):
        digit = floor_lin(3*r, 3*s+k, bounds)
        out = add(out, rot((P if vertical else S)[digit % 3], -2*k if vertical else -k))
    return out


def event(x, j):
    r, s = x
    m = lambda k: floor_lin(3*r, 3*s+k, BETA)
    isolated = m(j)-m(j-1) == 2
    patch = m(j-1)-m(j-3) == 4
    assert not (isolated and patch)
    return rot(ONE, m(j)-2*j) if isolated else rot(ONE, m(j-1)-1-2*j) if patch else ZERO


def cone(z):
    return int(z[0] <= 0 and z[0] <= z[1])


def low(z, b):
    x, y = z
    return 0 if b == 0 else int(x >= 1 and y >= 0) if b == 1 else int(x <= -1 and x <= y) if b == 2 else int(min(x, 0) <= y)


def axes(width):
    aa, bb = [ONE], [ONE]
    for n in range(1, width):
        aa.append(add(aa[-1], rot(S[floor_lin(0, n) % 3], -n)))
        bb.append(add(bb[-1], rot(P[floor_lin(0, n, BETA) % 3], -2*n)))
    return aa, bb


def check():
    width = 100
    aa, bb = axes(width)
    for n in range(25):
        x, y = phase(n, ALPHA), phase(n, BETA)
        for i in range(4):
            assert aa[3*n+i] == add(aa[3*n], displacement(x, i, ALPHA))
            assert bb[3*n+i] == add(bb[3*n], displacement(y, i, BETA, True))
        for j in range(3):
            b = 3*n+j
            if b >= 4:
                m = lambda k: floor_lin(0, k, BETA)
                expected = rot(ONE, m(b)-2*b) if m(b)-m(b-1) == 2 else rot(ONE, m(b-1)-1-2*b) if m(b-1)-m(b-3) == 4 else ZERO
                assert event(y, j) == expected

    # Every cut is exact affine data (k-s*alpha)/3; no floating sort.
    for length in range(1, 7):
        cuts = [(F(0), F(0)), (F(1), F(0))]
        for s in range(1, 3*length+1):
            f = floor_lin(0, s)
            cuts += [(F(k, 3), F(-s, 3)) for k in range(f+1, f+4)]
        def compare(a, b):
            if a == b:
                return 0
            lo, hi = interval(a[0]-b[0], a[1]-b[1])
            assert lo > 0 or hi < 0
            return 1 if lo > 0 else -1
        cuts.sort(key=cmp_to_key(compare))
        values = []
        for left, right in zip(cuts, cuts[1:]):
            mid = (left[0]+right[0])/2, (left[1]+right[1])/2
            values.append(displacement(mid, 3*length, ALPHA))
        assert len(cuts) == 9*length+2
        assert all(a != b for a, b in zip(values, values[1:]))
        assert values[0] == values[-1]
        for n in range(10):
            assert sub(aa[3*(n+length)], aa[3*n]) == displacement(phase(n, ALPHA), 3*length, ALPHA)

    # Finite lifted resolvent includes its exact terminal atom.
    values = [cone(add(aa[3*n], (1, -1))) for n in range(17)]
    lhs = sum((F(values[n], 8**n)-F(values[n+1], 8**(n+1)) for n in range(16)), F(0))
    assert lhs == values[0]-F(values[16], 8**16)

    # Full high-row product kernel, including j-specific first block and E.
    starts = (2, 1, 1)
    nmax, mmax = 5, 5
    for i in range(3):
        for j in range(3):
            first = starts[j]
            def h(n, m, t=ZERO):
                x, y = phase(n, ALPHA), phase(m, BETA)
                z = add(add(add(aa[3*n], displacement(x, i, ALPHA)),
                            add(bb[3*m], displacement(y, j, BETA, True))), C[i][j])
                z = sub(sub(z, ONE), event(y, j))
                return cone(add(z, t))
            for t in (ZERO, OM, OM2, (2, -1)):
                def pair(da, db):
                    return sum((F(h(n+da, m+db, t), 8**n*27**m)
                                for n in range(nmax) for m in range(first, first+mmax)), F(0))
                combined = 216*pair(0, 0)-27*pair(1, 0)-8*pair(0, 1)+pair(1, 1)
                boundary = 216*F(h(0, first, t), 27**first)
                boundary -= 216*F(h(nmax, first, t), 8**nmax*27**first)
                boundary -= 216*F(h(0, first+mmax, t), 27**(first+mmax))
                boundary += 216*F(h(nmax, first+mmax, t), 8**nmax*27**(first+mmax))
                assert combined == boundary

    # All complete low-row horizontal flows have their own terminal correction.
    for i in range(3):
        for b in range(4):
            f = lambda n: low(add(sub(add(aa[3*n+i], bb[b]), ONE), C[i][b % 3]), b)
            lhs = sum((F(f(n), 8**n)-F(f(n+1), 8**(n+1)) for n in range(10)), F(0))
            assert lhs == f(0)-F(f(10), 8**10)
    assert sub(aa[3], aa[0]) != sub(aa[6], aa[3])
    assert aa[0] == aa[9] == ONE
    assert sub(aa[3], aa[0]) == (0, -1)
    assert sub(aa[12], aa[9]) == OM2
    print('PASS: actual horizontal/vertical guarded lifts, high E and all low rows, finite resolvent terminals')
    print('PASS: exact integer two-axis transport and9L nonzero phase cuts forL=1..6')
    print('ACTUAL_STRIDE3_INCREMENTS', sub(aa[3], aa[0]), sub(aa[6], aa[3]))
    print('SAME_ACTUAL_STATE_DIFFERENT_NEXT_STEP', aa[0], sub(aa[3], aa[0]), sub(aa[12], aa[9]))


if __name__ == '__main__':
    check()
