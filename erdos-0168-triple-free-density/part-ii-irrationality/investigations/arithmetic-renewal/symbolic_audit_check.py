"""Independent SY1--SY5 audit: exact stdlib arithmetic, no project imports.

Finite calculations certify only the displayed finite claims.  Infinite
contraction, numerator and tail arguments are given in symbolic_audit.md.
"""
from bisect import bisect_right
from fractions import Fraction as Q
from functools import cache
from itertools import product

ZERO, ONE = (0, 0), (1, 0)
WIDTH = 930
POW3 = [3**n for n in range(WIDTH)]
AFLOOR = [bisect_right(POW3, 2**n)-1 for n in range(WIDTH)]
BFLOOR = [(3**n).bit_length()-1 for n in range(WIDTH)]


def add(z, w):
    return z[0]+w[0], z[1]+w[1]


def sub(z, w):
    return z[0]-w[0], z[1]-w[1]


def rotate(z, n):
    for _ in range(n % 3):
        z = -z[1], z[0]-z[1]
    return z


def correction(a, b):
    x, y = sub(ONE, rotate(ONE, -a))
    u, v = sub(ONE, rotate(ONE, -2*b))
    x, y = x*u-y*v, x*v+y*u-y*v
    assert x % 3 == y % 3 == 0
    return x//3, y//3


AA, BB, EE = [ONE], [ONE], [ZERO]*4
for n in range(1, WIDTH):
    AA.append(add(AA[-1], rotate((ONE, (0, -1), ZERO)[AFLOOR[n] % 3], -n)))
    BB.append(add(BB[-1], rotate((ONE, (1, 1), ZERO)[BFLOOR[n] % 3], -2*n)))
for b in range(4, WIDTH):
    isolate = BFLOOR[b]-BFLOOR[b-1] == 2
    patch = BFLOOR[b-1]-BFLOOR[b-3] == 4
    assert not (isolate and patch)
    EE.append(rotate(ONE, BFLOOR[b]-2*b) if isolate else
              rotate(ONE, BFLOOR[b-1]-1-2*b) if patch else ZERO)


@cache
def state(a, b):
    z = add(sub(add(AA[a], BB[b]), ONE), correction(a, b))
    return sub(z, EE[b]) if b >= 4 else z


def rho(z):
    return max(abs(z[0]), abs(z[1]-z[0]))


def target(a, b):
    x, y = state(a, b)
    if b >= 4:
        return int(x <= min(0, y))
    return (0 if b == 0 else int(x >= 1 and y >= 0) if b == 1 else
            int(x <= min(-1, y)) if b == 2 else int(y >= min(0, x)))


def board_counts(t):
    """Enumerate individual original smooth-board cells; no floor formula."""
    counts, p3, b = [0, 0, 0], 1, 0
    while p3 <= t:
        p2, a = 1, 0
        while p2*p3 <= t:
            counts[(a-b) % 3] += 1
            p2, a = 2*p2, a+1
        p3, b = 3*p3, b+1
    return counts


def original_tau(clock):
    counts = board_counts(clock//2)
    root, k = 2, 1
    while 2*root <= clock:
        if 3*root > clock or (12*root <= clock and 2*clock < 27*root):
            counts[k % 3] -= 1
        root, k = 2*root, k+1
    return min(counts)


HIGH = [(i, b) for i in range(3) for b in (6, 4, 5)]
LOW = [(i, b) for i in range(3) for b in range(4)]
STEPS = ((3, 0), (0, 3), (3, 3))


def picard(radius):
    @cache
    def value(a, b, d):
        h = target(a, b)
        if rho(state(a, b)) > radius:
            return 1+Q(h, 182 if b >= 4 else 7)
        if d == 0:
            return Q(0)
        if b < 4:
            return (value(a+3, b, d-1)+h)/8
        return (27*value(a+3, b, d-1)+8*value(a, b+3, d-1)
                -value(a+3, b+3, d-1)+h)/216
    return value


def full_source(value, d):
    return (sum((Q(216, 2**a*3**b)*value(a, b, d) for a, b in HIGH), Q(0))
            + sum((Q(8, 2**a*3**b)*value(a, b, d) for a, b in LOW), Q(0)))


def prime_residues(radius):
    @cache
    def modq(a, b, d):
        if rho(state(a, b)) > radius:
            return (182+target(a, b)) % 3 if d == 0 else 0
        if d == 0:
            return 0
        return ((2*target(a, b) if d == 1 else 0)
                -modq(a, b+3, d-1)-modq(a+3, b+3, d-1)) % 3
    return [sum(2**(3-i)*modq(i, 6, d) for i in range(3)) % 3
            for d in range(1, 101)]


def valuation(n, prime):
    assert n > 0
    v = 0
    while n % prime == 0:
        n, v = n//prime, v+1
    return v


def main():
    for n in range(80):
        for base, axis, exponent in ((2, AA, -n), (3, BB, n)):
            counts = board_counts(base**n)
            assert axis[n] == rotate((counts[0]-counts[2], counts[1]-counts[2]), exponent)
    for b in range(4, 128):
        hits = [rotate(ONE, k+b) for k in range(1, BFLOOR[b]+1)
                if 3*2**k > 2*3**b or (6*2**k <= 3**b and 4*3**b < 27*2**k)]
        assert len(hits) <= 1 and EE[b] == (hits[0] if hits else ZERO)
    assert AA[0] == AA[9] == ONE
    assert state(12, 8) == (-2, -2) and state(22, 35) == (-1, 1)

    graphs, exact, low_steps = {}, {}, {}
    for start in HIGH:
        todo, seen = [start], set()
        while todo:
            a, b = todo.pop()
            if (a, b) in seen or state(a, b) != ZERO:
                continue
            assert a < 200 and b < 200, 'R0 closure did not finish within audit guard'
            seen.add((a, b))
            todo.extend((a+da, b+db) for da, db in STEPS)
        graphs[start] = (len(seen), max(((a-start[0]+b-start[1])//3 for a, b in seen), default=0))
        values = {}
        for a, b in sorted(seen, key=lambda cell: sum(cell), reverse=True):
            successors = [(a+da, b+db) for da, db in STEPS]
            p = [values[cell] if cell in seen else 1+Q(target(*cell), 182) for cell in successors]
            assert all(cell in values or state(*cell) != ZERO for cell in successors)
            values[(a, b)] = (27*p[0]+8*p[1]-p[2]+target(a, b))/216
        exact[start] = values[start] if start in seen else 1+Q(target(*start), 182)
    assert {k: v for k, v in graphs.items() if v[0]} == {
        (0, 6): (1, 0), (0, 4): (3, 2), (0, 5): (1, 0),
        (1, 5): (1, 0), (2, 6): (15, 17)}
    for a, b in LOW:
        n = 0
        while state(a+3*n, b) == ZERO:
            n += 1
            assert n <= 3
        low_steps[(a, b)] = n
        p = 1+Q(target(a+3*n, b), 7)
        for k in range(n-1, -1, -1):
            p = (p+target(a+3*k, b))/8
        exact[(a, b)] = p
    s0 = sum((Q(216, 2**a*3**b)*exact[(a, b)] for a, b in HIGH), Q(0))
    s0 += sum((Q(8, 2**a*3**b)*exact[(a, b)] for a, b in LOW), Q(0))
    assert s0 == Q(7949385124218080419452346025, 372885909329585286602293248)
    assert s0.denominator.bit_length() == 89

    samples = {(a, b) for a in range(16) for b in range(16-a)}
    samples.update(HIGH+LOW+[(12, 8), (22, 35), (96, 4)])
    for a, b in samples:
        t = 2**(a+1)*3**b
        assert original_tau(t)-original_tau(t-1) == target(a, b)+int((a, b) == (0, 1))

    depth_list = (0, 1, 2, 4, 8, 12, 20, 32)
    for radius in range(4):
        p, residues = picard(radius), prime_residues(radius)
        for d in depth_list:
            source = full_source(p, d)
            q = {cell: 182*216**d*p(*cell, d) for cell in HIGH}
            r = {cell: 7*8**d*p(*cell, d) for cell in LOW}
            assert all(x.denominator == 1 for x in list(q.values())+list(r.values()))
            formula = sum(2**(3-a)*3**(6-b)*q[(a, b)] for a, b in HIGH)
            formula += 26*27**d*sum(2**(3-a)*3**(3-b)*r[(a, b)] for a, b in LOW)
            assert formula == 27*182*216**d*source
            if d:
                assert formula.numerator % 3 == residues[d-1]
                if residues[d-1]:
                    assert valuation(source.denominator, 3) == 3*d+3
            if radius == 0 and d >= 20:
                assert source == s0
            if radius == 1 and d == 32:
                assert (valuation(source.denominator, 2), valuation(source.denominator, 3),
                        source.denominator.bit_length()) == (94, 99, 258)
        if radius == 1:
            assert sum(bool(x) for x in residues) == 71
            assert all(residues[d-1] for d in (1, 4, 12, 20, 32))
        print('MOD3_NONZERO_FIRST100', radius, sum(bool(x) for x in residues))

    witnesses = []
    for radius in range(4):
        for a in range(60):
            for b in range(4, 60):
                inside = lambda x, y: rho(state(x, y)) <= radius
                if inside(a, b) and inside(a+3, b+6) and inside(a, b+3) != inside(a+3, b+3):
                    witnesses.append((radius, a, b))
                    break
            if witnesses and witnesses[-1][0] == radius:
                break
    assert witnesses, 'Need an actual killed B/AB commutator witness'

    cutoff = 100
    head = sum((Q(target(a, b), 2**a*3**b) for a in range(cutoff)
                for b in range(cutoff-a)), Q(0))
    tail = 6*Q(1, 2**cutoff)-3*Q(1, 3**cutoff)
    k = 7851029231031622054440914924
    assert k < s0.denominator*(s0-head-tail) < s0.denominator*(s0-head) < k+1
    for m in range(40):
        split_tail = sum((Q(2, 2**(m-b)*3**b) for b in range(m)), Q(0))+Q(3, 3**m)
        assert split_tail == 6*Q(1, 2**m)-3*Q(1, 3**m)

    high_mass = sum((Q(216, 2**a*3**b) for a, b in HIGH), Q(0))
    low_mass = sum((Q(8, 2**a*3**b) for a, b in LOW), Q(0))
    assert (high_mass, low_mass) == (Q(182, 27), Q(560, 27))
    assert high_mass*Q(183, 182) == Q(61, 9)
    assert low_mass*Q(8, 7) == Q(640, 27)
    for m in range(40):
        assert 27**(m+1)*Q(61, 9)*Q(1, 6**m) == 183*Q(9, 2)**m
    c, bound = Q(1, 182), Q(1, 91)
    assert Q(36, 216) == Q(1, 6) and (36*bound+1)/216 <= bound
    extrema = [216*c+Q(34*h, 182)-27*a-8*b+ab
               for h, a, b, ab in product((0, 1), (-bound, bound), (-bound, bound), (-bound, bound))]
    assert (min(extrema), max(extrema)) == (Q(144, 182), Q(161, 91))
    assert 180*Q(1, 910)-Q(36, 182) == 0
    assert Q(1, 910)+Q(1, 182) >= Q(1, 180)
    low_bound = Q(2, 7)
    assert (low_bound+1)/8 <= low_bound
    assert min(8*Q(1+h, 7)-h-a for h, a in product((0, 1), (-low_bound, low_bound))) == Q(6, 7)
    print('R0_GRAPHS', graphs, 'LOW_EXIT_STEPS', low_steps)
    print('R0_FULL_SOURCE', s0, 'CLEARED_PSI0_FLOOR', k)
    print('KILLED_B_AB_NONCOMMUTATION', witnesses)
    print('PASS: full-source SY1--SY5 exact finite assertions; no infinite-supply claim')


if __name__ == '__main__':
    main()
