# Full goodness of an odd m: every piece Phi_{2d}, d | m, has a level s in [1, T_d-1] with negative
# first window coefficient. Uses the period-d quasi-polynomial structure of [u^N]Phi_d(u)^{-(s+1)}
# (for fixed r, n -> e_{r+nd} is a polynomial of degree <= s, valid for all N >= 0) to reach N ~ m cheaply.
import sys
from math import comb
from core import divisors, phi
from fastser import cyclo_pow_series_fast

class PieceSeries:
    def __init__(self, d, s, Nneed):
        self.d, self.s = d, s
        B = (s + 1) * d + d          # enough base values for interpolation
        self.direct = Nneed <= B
        self.c = cyclo_pow_series_fast(d, -(s + 1), Nneed if self.direct else B)
        self.cache = {}
    def e(self, N):
        if self.direct: return self.c[N]
        d, s = self.d, self.s
        r, n = N % d, N // d
        if r not in self.cache:
            y = [self.c[r + j * d] for j in range(s + 1)]
            diffs = []
            while y:
                diffs.append(y[0]); y = [y[i + 1] - y[i] for i in range(len(y) - 1)]
            self.cache[r] = diffs
        return sum(comb(n, j) * dj for j, dj in enumerate(self.cache[r]))

def piece_level(m, d, s):
    "(offset, sign) of first nonzero window coefficient c_N (t-variable), or None"
    delta = phi(d); E = m - (s + 1) * delta; hi = m - delta
    if d == 1:   # [t^N](1+t)^{-(s+1)} = (-1)^N C(N+s,s); first N = E+1
        return (1, -1 if (E + 1) % 2 else 1)
    ps = PieceSeries(d, s, hi)
    for N in range(E + 1, hi + 1):
        v = ps.e(N)
        if v:
            v = v if N % 2 == 0 else -v      # c_N = (-1)^N e_N  (Phi_{2d}(t) = Phi_d(-t), d odd > 1)
            return (N - E, 1 if v > 0 else -1)
    return None

def piece_good(m, d):
    T = m // phi(d)
    pat = []
    for s in range(1, T):
        r = piece_level(m, d, s)
        pat.append(0 if r is None else r[1])
        if r and r[1] < 0: return s, pat
    return None, pat

def full_good(m, verbose=False):
    bad = []
    for d in sorted(divisors(m), reverse=True):
        s, pat = piece_good(m, d)
        if verbose: print('   d', d, 'first neg level', s, pat if s is None else '')
        if s is None: bad.append(d)
    return bad

if __name__ == '__main__':
    # self-check vs core.level_sign on small cases
    from core import level_sign
    for m in (105, 165, 195, 315, 1155, 1365, 3003):
        for d in divisors(m):
            for s in range(1, min(4, m // phi(d))):
                a = level_sign(m, d, s); b = piece_level(m, d, s)
                assert (a is None and b is None) or (a[1] == b[1] and a[0] - (m - (s + 1) * phi(d)) == b[0]), (m, d, s, a, b)
    print('fullgood agrees with core on small cases')
    for m in map(int, sys.argv[1:]):
        print(m, 'bad pieces:', full_good(m, verbose=True))
