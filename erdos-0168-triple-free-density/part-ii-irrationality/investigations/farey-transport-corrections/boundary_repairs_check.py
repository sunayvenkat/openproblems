from fractions import Fraction as F
from collections import Counter


def arrival(z, asym=False):
    a, b = z
    t = F(2) ** a * F(3) ** b
    if b == 0 and (asym or a >= 1):
        t *= F(3, 2)
    if b == 1 and (asym or a >= 2):
        t *= F(9, 8)
    return t


def colour(z):
    return (z[0] - z[1]) % 3


class Repair:
    def __init__(self, u, v):
        self.u, self.v = u, v
        self.det = u[0] * v[1] - u[1] * v[0]
        assert abs(self.det) == 1
        assert sorted((colour(u), colour(v))) == [1, 2]
        self.h = max(0, u[0], v[0]) - min(0, u[0], v[0])
        self.k = max(0, u[1], v[1]) - min(0, u[1], v[1])
        self.A = (self.h + 5) // 6 * 6
        self.B = (self.k + 5) // 6 * 6
        assert self.B >= 6
        corner = [(a, b) for a in range(self.A) for b in range(self.B)
                  if self.residual((a, b))]
        self.left = [[(a, b) for a in range(self.A)
                      for b in range(self.B, self.B + 6)
                      if self.residual((a, b)) and colour((a, b)) == j]
                     for j in range(3)]
        bottom = [(a, b) for a in range(self.A, self.A + 6)
                  for b in range(self.B) if self.residual((a, b))]
        assert len(set(map(len, self.left))) == 1
        assert len({sum(colour(z) == j for z in bottom) for j in range(3)}) == 1
        self.n = len(self.left[0])
        assert self.n > 0 and abs(self.n - self.h) <= 10
        counts = Counter(map(colour, corner))
        self.d = [max(counts.values()) - counts[j] for j in range(3)]
        self.J = (max(self.d) + self.n - 1) // self.n
        assert max(self.d) <= 36 * (self.h + self.k + 6)
        if self.h >= 20 and self.k <= self.h:
            assert self.J <= 180
        head = corner + [self.left_token(j, i) for j in range(3)
                         for i in range(self.d[j])]
        self.head_groups = self.rank_groups(head)
        self.bottom_groups = self.rank_groups(bottom)
        self.head_owner = {z: g for g in self.head_groups for z in g}
        self.bottom_owner = {z: g for g in self.bottom_groups for z in g}
        self.left_slot = [{z: i for i, z in enumerate(lst)} for lst in self.left]

    def ij(self, z):
        a, b = z
        u, v, d = self.u, self.v, self.det
        return ((v[1] * a - v[0] * b) // d,
                (-u[1] * a + u[0] * b) // d)

    def xy(self, i, j):
        return (i * self.u[0] + j * self.v[0],
                i * self.u[1] + j * self.v[1])

    def tile(self, z):
        i, j = self.ij(z)
        n, ri = divmod(i, 3)
        m, rj = divmod(j, 2)
        offsets = ((0, 0), (1, 0), (0, 1)) if (ri, rj) in (
            (0, 0), (1, 0), (0, 1)) else ((1, 1), (2, 0), (2, 1))
        return tuple(self.xy(3 * n + a, 2 * m + b) for a, b in offsets)

    def residual(self, z):
        return any(a < 0 or b < 0 for a, b in self.tile(z))

    def left_token(self, j, i):
        m, t = divmod(i, self.n)
        a, b = self.left[j][t]
        return a, b + 6 * m

    @staticmethod
    def rank_groups(tokens):
        lists = [sorted((z for z in tokens if colour(z) == j),
                        key=lambda z: (arrival(z), z)) for j in range(3)]
        assert len(set(map(len, lists))) == 1
        return list(zip(*lists))

    def group(self, z):
        if not self.residual(z):
            g = self.tile(z)
        elif z in self.head_owner:
            g = self.head_owner[z]
        elif z[0] >= self.A:
            m, r = divmod(z[0] - self.A, 6)
            g = tuple((a + 6 * m, b) for a, b in
                      self.bottom_owner[(self.A + r, z[1])])
        else:
            j = colour(z)
            m, r = divmod(z[1] - self.B, 6)
            idx = m * self.n + self.left_slot[j][(z[0], self.B + r)]
            assert idx >= self.d[j]
            t = idx - self.d[j]
            g = tuple(self.left_token(c, self.d[c] + t) for c in range(3))
        return tuple(sorted(g))

    @staticmethod
    def cost(groups):
        return sum((1 / max(map(arrival, g)) for g in groups), F(0))

    def bulk_cost(self):
        total = F(0)
        for residues, offsets in [((0, 0), ((0, 0), self.u, self.v)),
                                  ((1, 1), ((0, 0),
                                            (self.u[0] - self.v[0], self.u[1] - self.v[1]),
                                            self.u))]:
            xmin = -min(a for a, b in offsets)
            ymin = -min(b for a, b in offsets)
            for ra in range(6):
                for rb in range(6):
                    i, j = self.ij((ra, rb))
                    if (i % 3, j % 2) != residues:
                        continue
                    a = ra + 6 * ((xmin - ra + 5) // 6)
                    b = rb + 6 * ((ymin - rb + 5) // 6)
                    g = [(a + x, b + y) for x, y in offsets]
                    assert all(x >= 0 and y >= 0 for x, y in g)
                    assert len({colour(z) for z in g}) == 3
                    actual = max(map(arrival, g))
                    asym = max(arrival(z, True) for z in g)
                    raw = max(F(2) ** x * F(3) ** y for x, y in g)
                    total += 1 / actual + 1 / (63 * asym) + F(64, 63 * 728) / raw
        return total

    def full_cost(self):
        phase = [tuple(self.left_token(j, self.d[j] + t) for j in range(3))
                 for t in range(self.n)]
        return (self.bulk_cost() + self.cost(self.head_groups)
                + F(64, 63) * self.cost(self.bottom_groups)
                + F(729, 728) * self.cost(phase))

    def events(self, cap):
        records = []
        b = 0
        while 3 ** b <= cap:
            a = 0
            while 2 ** a * 3 ** b <= cap:
                z = a, b
                if arrival(z) <= cap:
                    records.append((arrival(z), z))
                a += 1
            b += 1
        return sorted(records)

    def first_deficit(self, cap):
        records = self.events(cap)
        groups = {self.group(z) for _, z in records}
        completed = Counter()
        for g in groups:
            assert len({colour(z) for z in g}) == 3
            assert all(self.group(z) == g for z in g)
            t = max(map(arrival, g))
            if t <= cap:
                completed[t] += 1
        counts = [0, 0, 0]
        done = 0
        index = 0
        for t in sorted({t for t, z in records}):
            while index < len(records) and records[index][0] == t:
                counts[colour(records[index][1])] += 1
                index += 1
            done += completed[t]
            assert done <= min(counts)
            if done < min(counts):
                return t, min(counts), done

    def first_forced_deficit(self, cap):
        records = self.events(cap)
        bulk = {tuple(sorted(self.tile(z))) for _, z in records
                if not self.residual(z)}
        completed = Counter(max(map(arrival, g)) for g in bulk)
        counts, leftovers = [0, 0, 0], [0, 0, 0]
        done = index = 0
        times = sorted({t for t, z in records})
        for pos, t in enumerate(times):
            while index < len(records) and records[index][0] == t:
                z = records[index][1]
                counts[colour(z)] += 1
                if self.residual(z):
                    leftovers[colour(z)] += 1
                index += 1
            done += completed[t]
            gap = min(counts) - done - min(leftovers)
            assert gap >= 0
            if gap:
                assert pos + 1 < len(times)
                lower = gap * (1 / t - 1 / times[pos + 1])
                return t, gap, times[pos + 1], lower


if __name__ == '__main__':
    cases = [((8, -5), (3, -2), 243, 243, F(5, 7776)),
             ((19, -12), (27, -17), 382205952, 382205952,
              F(7153, 203119913336832)),
             ((84, -53), (65, -41), 34856377305871210027941888,
              61966892988215484494118912,
              F(7153, 32931747576550225295039048712192))]
    for u, v, expected_first, expected_forced, expected_lower in cases:
        r = Repair(u, v)
        for a in range(-6, r.h + 7):
            for b in range(-6, r.k + 7):
                g = r.tile((a, b))
                assert (a, b) in g and len({colour(z) for z in g}) == 3
                assert all(r.tile(z) == g for z in g)
        q = r.full_cost()
        clearing = (63 * 728 * 2 ** 6 * 3 ** 6
                    * 2 ** r.A * 3 ** (r.B + 6 * r.J))
        assert (q * clearing).denominator == 1
        cap = 2 ** (r.h + 5)
        deficit = r.first_deficit(cap)
        assert deficit is not None
        forced = r.first_forced_deficit(cap)
        assert deficit[0] == expected_first
        assert forced is not None and forced[0] == expected_forced
        assert forced[3] == expected_lower
        if r.h in (8, 27):
            assert forced is not None and forced[0] == deficit[0]
        print({'u': u, 'v': v, 'span': (r.h, r.k), 'cuts': (r.A, r.B),
               'left_capacity': r.n, 'deficits': r.d, 'periods': r.J,
               'bulk_cost': str(r.bulk_cost()), 'cost': str(q),
               'denominator_bits': q.denominator.bit_length(),
               'first_deficit': (str(deficit[0]), *deficit[1:]),
               'forced_all_repairs': None if forced is None else tuple(map(str, forced))})
    print('PASS')
