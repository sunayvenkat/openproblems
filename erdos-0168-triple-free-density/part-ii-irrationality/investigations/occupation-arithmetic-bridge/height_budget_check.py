"""Exact finite certificates for the actual state/first-arrival budget."""
from fractions import Fraction as F
from bisect import bisect_right


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def sub(z, w):
    return z[0] - w[0], z[1] - w[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0] - z[1]
    return z


ROOTS = ((1, 0), (0, 1), (-1, -1))
C = (((0, 0), (0, 0), (0, 0)),
     ((0, 0), (1, 0), (1, 1)),
     ((0, 0), (0, -1), (1, 0)))


def log_interval(z, count=120):
    partial = 2 * sum((z**(2*k+1) / (2*k+1) for k in range(count)), F(0))
    tail = 2*z**(2*count+1) / ((2*count+1)*(1-z*z))
    return partial, partial + tail


def beta_convergent_denominators():
    l2, u2 = log_interval(F(1, 3))
    l3, u3 = log_interval(F(1, 2))
    low, high = l3/u2, u3/l2
    p0, p1, q0, q1 = 0, 1, 1, 0
    out = set()
    for _ in range(20):
        a, b = low.numerator//low.denominator, high.numerator//high.denominator
        assert a == b
        p0, p1, q0, q1 = p1, a*p1+p0, q1, a*q1+q0
        if q1 > 306:
            break
        out.add(q1)
        low, high = 1/(high-a), 1/(low-a)
    assert 12 in out and 53 in out and 306 in out
    return sorted(out)


def floor_three_beta(d):
    if d == 0:
        return 0
    value = (3**(3*abs(d))).bit_length()-1
    return value if d > 0 else -value-1


def check_all_block_phases(q):
    # At x=r/3-k0*beta every other orbit term avoids a third endpoint.
    floors = {d: floor_three_beta(d) for d in range(1-q, q)}
    largest = 0
    for k0 in range(q):
        for r in range(3):
            counts = [0, 0, 0]
            for k in range(q):
                counts[(r+floors[k-k0]) % 3] += 1
            for side in range(2):
                if side:
                    counts[r] -= 1
                    counts[(r-1) % 3] += 1
                assert all(abs(3*n-q) <= 30 for n in counts)
                x, y = counts[0]-counts[2], counts[1]-counts[2]
                norm2 = x*x-x*y+y*y
                assert norm2 <= 30**2
                largest = max(largest, norm2)
    return largest


def axes(width):
    powers = [1]
    while powers[-1] <= 2**width:
        powers.append(3*powers[-1])
    aa, bb = [(1, 0)], [(1, 0)]
    for n in range(1, width):
        f = bisect_right(powers, 2**n)-1
        aa.append(add(aa[-1], rot(((1, 0), (0, -1), (0, 0))[f % 3], -n)))
        g = (3**n).bit_length()-1
        bb.append(add(bb[-1], rot(((1, 0), (1, 1), (0, 0))[g % 3], -2*n)))
    return aa, bb


def board(clock):
    counts = [0, 0, 0]
    power3, b = 1, 0
    while power3 <= clock:
        value, a = power3, 0
        while value <= clock:
            counts[(a-b) % 3] += 1
            value, a = 2*value, a+1
        power3, b = 3*power3, b+1
    return counts[0]-counts[2], counts[1]-counts[2]


def event(b):
    floor = lambda n: (3**n).bit_length()-1
    isolated = floor(b)-floor(b-1) == 2
    patch = floor(b-1)-floor(b-3) == 4
    assert not (isolated and patch)
    return (rot((1, 0), floor(b)-2*b) if isolated else
            rot((1, 0), floor(b-1)-1-2*b) if patch else (0, 0))


def check():
    blocks = {q: check_all_block_phases(q) for q in beta_convergent_denominators()}
    aa, bb = axes(600)
    for n in (0, 1, 2, 3, 6, 12, 36, 72, 120):
        assert aa[n] == rot(board(2**n), -n)
        assert bb[n] == rot(board(3**n), n)
    seen, witness = {}, None
    for n in range(199):
        state, increment = aa[3*n], sub(aa[3*n+3], aa[3*n])
        if state in seen and seen[state][1] != increment:
            witness = state, seen[state], (n, increment)
            break
        seen[state] = n, increment
    assert witness is not None
    first = {}
    for total in range(4, 80):
        for b in range(4, total+1):
            a = total-b
            state = sub(add(sub(add(aa[a], bb[b]), (1, 0)), C[a % 3][b % 3]), event(b))
            first.setdefault(state, (total, a, b))
    for total, a, b in first.values():
        assert F(1, 2**a*3**b) >= F(1, 3**total)
    for n in range(20):
        triangle_tail = sum((F(2, 2**(n-b)*3**b) for b in range(n)), F(3, 3**n))
        assert triangle_tail == F(6, 2**n)-F(3, 3**n)
    print('PASS: all circle phases at convergent block denominators', blocks)
    print('PASS: direct original-board axes and first-arrival witness weights')
    print('Nonautonomous state witness:', witness)
    print('Finite occupied states:', len(first))


if __name__ == '__main__':
    check()
