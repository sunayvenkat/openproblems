"""Exact actual-board Picard sources and joint-path survival; no infinity inference."""
from collections import deque
from fractions import Fraction as Q
from functools import cache

ONE = (1, 0)
C = (((0, 0), (0, 0), (0, 0)),
     ((0, 0), ONE, (1, 1)), ((0, 0), (0, -1), ONE))


def add(z, w):
    return z[0]+w[0], z[1]+w[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0]-z[1]
    return z


def board(t):
    counts, p3, b = [0, 0, 0], 1, 0
    while p3 <= t:
        last = (t//p3).bit_length()-1
        for j in range(3):
            first = (j+b) % 3
            if first <= last:
                counts[j] += (last-first)//3+1
        p3, b = 3*p3, b+1
    return counts[0]-counts[2], counts[1]-counts[2]


def event(b):
    t, e, k, hits = 3**b, 2, 1, []
    while e <= t:
        if 3*e > 2*t or (6*e <= t and 4*t < 27*e):
            hits.append(rot(ONE, k+b))
        e, k = 2*e, k+1
    assert len(hits) <= 1
    return hits[0] if hits else (0, 0)


def rho(z):
    return max(abs(z[1]-z[0]), abs(z[0]))


def cone(z):
    return int(z[0] <= 0 and z[0] <= z[1])


WIDTH = 930
AA = [rot(board(2**a), -a) for a in range(WIDTH)]
BB = [rot(board(3**b), b) for b in range(WIDTH)]
EE = [(0, 0)]*4+[event(b) for b in range(4, WIDTH)]


def state(a, b):
    z = add(add(AA[a], BB[b]), C[a % 3][b % 3])
    return z[0]-1-EE[b][0], z[1]-EE[b][1]


def low_state(a, b):
    z = add(add(AA[a], BB[b]), C[a % 3][b % 3])
    return z[0]-1, z[1]


def low(z, b):
    x, y = z
    return (0 if b == 0 else int(x >= 1 and y >= 0) if b == 1
            else int(x <= -1 and x <= y) if b == 2
            else int(min(x, 0) <= y))


def source(radius, depth, high_offset=Q(1)):
    @cache
    def high(a, b, d):
        z, h = state(a, b), cone(state(a, b))
        if rho(z) > radius:
            return high_offset+Q(h, 182)
        if d == 0:
            return Q(0)
        return (27*high(a+3, b, d-1)+8*high(a, b+3, d-1)
                -high(a+3, b+3, d-1)+h)/216

    @cache
    def low_value(a, b, d):
        z, h = low_state(a, b), low(low_state(a, b), b)
        if rho(z) > radius:
            return 1+Q(h, 7)
        return Q(0) if d == 0 else (low_value(a+3, b, d-1)+h)/8

    high_total = sum((216*Q(1, 2**i*3**b)*high(i, b, depth)
                      for i in range(3) for b in (6, 4, 5)), Q(0))
    low_total = sum((8*Q(1, 2**i*3**b)*low_value(i, b, depth)
                     for i in range(3) for b in range(4)), Q(0))
    out = high_total+low_total
    assert (4914*high_offset.denominator*216**depth*out).denominator == 1
    return out, high_total, low_total


def valuation(n, prime):
    out = 0
    while n % prime == 0:
        n, out = n//prime, out+1
    return out


def joint_path(radius, i, b, limit=300):
    start = (0, 0)
    if rho(state(i, b)) > radius:
        return 'outside', 0, 0, None
    queue, seen, parents = deque([start]), {start}, {}
    maximum = 0
    while queue:
        n, m = queue.popleft()
        maximum = max(maximum, n+m)
        if max(n, m) == limit:
            path, cell = [], (n, m)
            while cell != start:
                prev = parents[cell]
                path.append((cell[0]-prev[0], cell[1]-prev[1]))
                cell = prev
            return 'frontier', len(seen), maximum, ''.join(
                'A' if s == (1, 0) else 'B' if s == (0, 1) else 'D'
                for s in reversed(path))
        for nxt in ((n+1, m), (n, m+1), (n+1, m+1)):
            if nxt not in seen and rho(state(i+3*nxt[0], b+3*nxt[1])) <= radius:
                seen.add(nxt)
                parents[nxt] = (n, m)
                queue.append(nxt)
    return 'terminated', len(seen), maximum, None


def prime3_source(radius, maximum):
    """Full-source numerator mod3, by killed B/AB path propagation."""
    def inside(a, b):
        return rho(state(a, b)) <= radius

    def q0(a, b):
        return 0 if inside(a, b) else 182+cone(state(a, b))

    def q1(a, b):
        return (2*cone(state(a, b))-q0(a, b+3)-q0(a+3, b+3)) % 3

    weights = {(i, 6): 2**(3-i) % 3 for i in range(3) if inside(i, 6)}
    values = []
    for depth in range(1, maximum+1):
        values.append(sum(w*q1(a, b) for (a, b), w in weights.items()) % 3)
        nxt = {}
        for (a, b), w in weights.items():
            for cell in ((a, b+3), (a+3, b+3)):
                if inside(*cell):
                    nxt[cell] = (nxt.get(cell, 0)-w) % 3
        weights = {cell: w for cell, w in nxt.items() if w}
    return values


def check():
    assert AA[0] == AA[9] == ONE
    assert state(12, 8) == (-2, -2) and state(22, 35) == (-1, 1)
    for i in range(3):
        for b in range(4):
            steps = 0
            while rho(low_state(i+3*steps, b)) == 0:
                steps += 1
            assert steps <= 3
    for r in range(4):
        residues = prime3_source(r, 100)
        for i in range(3):
            for b in (6, 4, 5):
                status, size, total, path = joint_path(r, i, b)
                if r == 0:
                    assert status != 'frontier' and total < 20
                print('JOINT', r, i, b, status, size, total,
                      'path_prefix='+path[:60] if path else '')
        for d in (0, 1, 2, 4, 8, 12, 20, 32):
            out, h, l = source(r, d)
            den = out.denominator
            if d:
                numerator = 4914*216**d*out
                assert numerator.denominator == 1
                assert numerator.numerator % 3 == residues[d-1]
                if residues[d-1]:
                    assert valuation(den, 3) == 3*d+3
            print('SOURCE', r, d, 'v2', valuation(den, 2),
                  'v3', valuation(den, 3), 'bits', den.bit_length(),
                  'high_bits', h.denominator.bit_length(),
                  'low_bits', l.denominator.bit_length())
        nonzero = [d for d, value in enumerate(residues, 1) if value]
        print('PRIME3_NONZERO', r, len(nonzero), 'of100', nonzero)
    s0 = source(0, 20)[0]
    assert s0 == source(0, 32)[0]
    assert s0 == Q(7949385124218080419452346025,
                   372885909329585286602293248)
    cutoff = 100
    head = sum((Q(cone(state(a, b)) if b >= 4 else low(low_state(a, b), b),
                  2**a*3**b)
                for a in range(cutoff) for b in range(cutoff-a)), Q(0))
    tail = 6*Q(1, 2**cutoff)-3*Q(1, 3**cutoff)
    bounds = ((s0-head-tail)*s0.denominator, (s0-head)*s0.denominator)
    floors = [v.numerator//v.denominator for v in bounds]
    assert floors == [7851029231031622054440914924]*2
    print('R0_FULL_SOURCE', s0, 'CLEARED_PSI0_FLOOR', floors[0])
    for h in (0, 1):
        # The original small offset is already sufficient when g=0.
        assert (36*Q(1, 91)+1)/216 <= Q(1, 91)
        assert Q(216, 182)+Q(34*h, 182)-36*Q(1, 91) >= Q(144, 182)
    print('PASS: exact board witnesses, all source normalizations and denominator divisibility')
    print('PASS: independent mod3 path recurrence matches full rational sources')


if __name__ == '__main__':
    check()
