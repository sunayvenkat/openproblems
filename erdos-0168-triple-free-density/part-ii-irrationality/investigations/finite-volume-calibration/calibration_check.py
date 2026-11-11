"""Exact finite-volume baselines; no adequate density-return claim."""
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import product
from pathlib import Path
import importlib.util


source = Path(__file__).parents[1] / 'Erdos 168 occupation arithmetic bridge' / 'exact_transport_check.py'
spec = importlib.util.spec_from_file_location('accepted_transport', source)
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)


def norm(y):
    return max(abs(y[0]), abs(y[1]))


def cells(length):
    cuts = [(F(0), F(0)), (F(1), F(0))]
    for s in range(1, 3*length+1):
        k = t.floor_lin(0, s)
        cuts += [(F(j, 3), F(-s, 3)) for j in range(k+1, k+4)]
    def compare(a, b):
        if a == b:
            return 0
        lo, hi = t.interval(a[0]-b[0], a[1]-b[1])
        assert lo > 0 or hi < 0
        return 1 if lo > 0 else -1
    cuts.sort(key=cmp_to_key(compare))
    return [((a[0]+b[0])/2, (a[1]+b[1])/2) for a, b in zip(cuts, cuts[1:])]


def exit_time(y, x, radius, limit):
    for n in range(limit+1):
        if norm(y) > radius:
            return n
        if n < limit:
            y = t.add(y, t.displacement((x[0], x[1]+n), 3, t.ALPHA))
    return None


def eta(a, b, aa, bb):
    z = t.add(t.sub(t.add(aa[a], bb[b]), t.ONE), t.C[a % 3][b % 3])
    if b >= 4:
        z = t.sub(z, t.event(t.phase(b//3, t.BETA), b % 3))
        return t.cone(z)
    return t.low(z, b)


def v2(n):
    assert n
    n = abs(n)
    return (n & -n).bit_length()-1


def check():
    # A larger common phase refinement is used; no invariant partition is assumed.
    radius = 1
    for horizon in (4, 8, 16, 32, 64, 128, 256, 512, 1024):
        latest = 0
        valid = True
        for x in cells(horizon):
            for y in product(range(-radius, radius+1), repeat=2):
                n = exit_time(y, x, radius, horizon)
                if n is None:
                    valid = False
                    break
                latest = max(latest, n)
            if not valid:
                break
        if valid:
            print('ALL_PHASE_RADIUS1_EXIT_BOUND', latest, 'REFINEMENT', horizon)
            break
    assert valid

    aa, bb = t.axes(1500)
    yy = aa[::3]
    # Positive odd reward: the exact source head has full binary denominator.
    for radius in (1, 2):
        tau = next(n for n, y in enumerate(yy) if norm(y) > radius)
        h = [1+6*t.cone(t.sub(y, t.ONE)) for y in yy]
        head = sum((F(h[n], 8**n) for n in range(tau)), F())
        assert head.denominator == 8**(tau-1)
        def killed(n):
            if norm(yy[n]) > radius:
                return F()
            stop = next(k for k in range(n+1, len(yy)) if norm(yy[k]) > radius)
            return sum((F(h[k], 8**(k-n+1)) for k in range(n, stop)), F())
        terms = 30
        ps = [killed(n) for n in range(terms+1)]
        assert ps[0] == head/8
        assert ps[0].denominator == 8**tau
        residual = [h[n]-8*ps[n]+ps[n+1] for n in range(terms)]
        for n, e in enumerate(residual):
            assert e == 0 if norm(yy[n]) <= radius else 1 <= e <= 8
        lhs = sum((F(h[n], 8**n) for n in range(terms)), F())-head
        rhs = sum((residual[n]/8**n for n in range(terms)), F())-F(8, 8**terms)*ps[-1]
        assert lhs == rhs
        print('ODD_REWARD_EXIT', radius, tau, 'DEN_BITS', head.denominator.bit_length(), 'CLEARED_LOWER', F(1, 8))

    # Actual 0/1 target, with rational noncompact outer potential (1+h)/7.
    bits = [t.cone(t.sub(y, t.ONE)) for y in yy]
    for radius in (1, 2):
        tau = next(n for n, y in enumerate(yy) if norm(y) > radius)
        numer = 1+bits[tau]+7*sum(8**(tau-1-n)*bits[n] for n in range(tau))
        q = F(numer, 8**(tau-1))
        def p(n):
            if norm(yy[n]) > radius:
                return F(1+bits[n], 7)
            stop = next(k for k in range(n+1, len(yy)) if norm(yy[k]) > radius)
            return sum((F(bits[k], 8**(k-n+1)) for k in range(n, stop)), F())+F(1+bits[stop], 7*8**(stop-n))
        assert 56*p(0) == q
        assert numer % 7 in (1, 2)
        assert (8*p(0)).denominator == 7*q.denominator
        assert p(0).denominator == 7*2**max(3*tau-v2(numer), 0)
        for n in range(30):
            e = 8*p(n)-p(n+1)-bits[n]
            assert e == 0 if norm(yy[n]) <= radius else F(6, 7) <= e <= F(9, 7)
        print('BINARY_REWARD_EXIT', radius, tau, 'LAST_BIT', bits[tau], 'DEN_56P0', q.denominator, 'DEN_8P0', (8*p(0)).denominator)

    # Exhaustive short words independently check the exact base8 carry formula.
    for tau in range(1, 9):
        for word in product((0, 1), repeat=tau+1):
            numer = 1+word[tau]+7*sum(8**(tau-1-n)*word[n] for n in range(tau))
            if word[tau] == 0 and word[tau-1] == 1:
                run = 0
                for bit in reversed(word[:tau]):
                    if not bit:
                        break
                    run += 1
                expected = 3*run
            else:
                expected = int(word[tau] == 1 and word[tau-1] == 0)
            assert v2(numer) == expected
            source = F(numer, 7*8**(tau-1))
            scaled = 7*source
            assert numer % 7 in (1, 2)
            assert source.denominator == 7*scaled.denominator
            assert scaled.denominator == 2**max(3*(tau-1)-expected, 0)

    # A complete density calibration with an ACTUAL nonzero Z coefficient.
    for a in (1, 3, 5, 9):
        for b in (1, 3, 5, 7):
            head = sum((F(1+6*eta(i, j, aa, bb), 2**i*3**j) for i in range(a) for j in range(b)), F())
            den = 2**(a-1)*3**(b-1)
            assert head.denominator == den
            mass = 3*(F(1, 2**a)+F(1, 3**b)-F(1, 2**a*3**b))
            assert den*mass >= F(3**b, 2)
            assert den*mass >= 2**(a-1)
    print('PASS: complete odd rectangle head denominators and divergent positive cleared exterior')
    print('PASS: finite-volume killed/Dirichlet identities and 0/1 carry exceptions')


if __name__ == '__main__':
    check()
