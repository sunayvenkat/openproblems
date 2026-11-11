from fractions import Fraction as F
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import sys

sys.dont_write_bytecode = True
spec = spec_from_file_location('boundary_repair_input', Path(__file__).with_name('boundary_repairs_check.py'))
base = module_from_spec(spec)
spec.loader.exec_module(base)


class PhaseRepair(base.Repair):
    def __init__(self, u, v, shift):
        self.shift = shift
        super().__init__(u, v)

    def tile(self, z):
        x, y = self.shift
        return tuple((a + x, b + y) for a, b in super().tile((z[0] - x, z[1] - y)))

    def bulk_cost(self):
        total = F(0)
        for residues, offsets in [((0, 0), ((0, 0), self.u, self.v)),
                                  ((1, 1), ((0, 0),
                                            (self.u[0] - self.v[0], self.u[1] - self.v[1]), self.u))]:
            xmin = -min(a for a, b in offsets)
            ymin = -min(b for a, b in offsets)
            found = 0
            for ra in range(6):
                for rb in range(6):
                    i, j = self.ij((ra - self.shift[0], rb - self.shift[1]))
                    if (i % 3, j % 2) != residues:
                        continue
                    found += 1
                    a = ra + 6 * ((xmin - ra + 5) // 6)
                    b = rb + 6 * ((ymin - rb + 5) // 6)
                    g = [(a + x, b + y) for x, y in offsets]
                    assert all(x >= 0 and y >= 0 for x, y in g)
                    assert tuple(sorted(g)) == tuple(sorted(self.tile(g[0])))
                    actual = max(map(base.arrival, g))
                    asym = max(base.arrival(z, True) for z in g)
                    raw = max(F(2) ** x * F(3) ** y for x, y in g)
                    total += 1 / actual + 1 / (63 * asym) + F(64, 63 * 728) / raw
            assert found == 6
        return total


def representatives(u, v):
    det = u[0] * v[1] - u[1] * v[0]
    reps = {}
    for a in range(6):
        for b in range(6):
            i = (v[1] * a - v[0] * b) // det
            j = (-u[1] * a + u[0] * b) // det
            reps.setdefault((i % 3, j % 2), (a, b))
    assert len(reps) == 6
    return sorted(reps.items())


def main():
    cases = [((8, -5), (3, -2), [243, 1458, 486, 4608, 2187, 243], 1458),
             ((19, -12), (27, -17),
              [382205952, 129140163, 429981696, 129140163, 805306368, 258280326],
              429981696)]
    for u, v, expected, repair_first in cases:
        results = []
        origin_tiles = set()
        for phase_index, (coset, shift) in enumerate(representatives(u, v)):
            r = PhaseRepair(u, v, shift)
            origin_tiles.add(tuple(sorted(r.tile((0, 0)))))
            cap = 2 ** ((5 * r.h + 1) // 2)
            forced = r.first_forced_deficit(cap)
            assert forced is not None
            assert forced[0] == expected[phase_index]
            assert forced[0] < 2 ** (2 * r.h)
            for a in range(-6, r.h + 6):
                for b in range(-6, r.k + 6):
                    g = r.tile((a, b))
                    assert (a, b) in g and len({base.colour(z) for z in g}) == 3
                    assert all(r.tile(z) == g for z in g)
            q = r.full_cost()
            clearing = 63 * 728 * 2 ** 6 * 3 ** 6 * 2 ** r.A * 3 ** (r.B + 6 * r.J)
            assert (q * clearing).denominator == 1
            results.append((forced[0], coset, shift, r, forced, q))
            print({'basis': (u, v), 'coset': coset, 'shift': shift,
                   'capacity_first': str(forced[0]), 'gap': forced[1],
                   'next_arrival': str(forced[2]), 'cost_gap_lower': str(forced[3]),
                   'below_2H': forced[0] < 2 ** (2 * r.h),
                   'edge_capacity': r.n, 'periods': r.J,
                   'cost': str(q), 'reduced_denominator_bits': q.denominator.bit_length()})
        assert len(origin_tiles) == 6
        _, coset, shift, r, forced, q = max(results, key=lambda row: row[0])
        actual = r.first_deficit(2 ** ((5 * r.h + 1) // 2))
        assert actual is not None and actual[0] == repair_first <= forced[0]
        clearing = 63 * 728 * 2 ** 6 * 3 ** 6 * 2 ** r.A * 3 ** (r.B + 6 * r.J)
        assert q.denominator * forced[3] > 1
        zhat = 3 - 3 * q
        assert 3 * zhat.denominator * forced[3] > 1
        print({'best_capacity_phase': shift, 'coset': coset,
               'capacity_first': str(forced[0]), 'actual_repair_first': tuple(map(str, actual)),
               'cost': str(q), 'clearing_bits': clearing.bit_length()})
    print('PASS')


if __name__ == '__main__':
    main()
