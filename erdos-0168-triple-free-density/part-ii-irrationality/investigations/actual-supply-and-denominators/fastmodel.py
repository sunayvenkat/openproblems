"""Fast exact evaluation of the accepted complete nonresonant scalar model.

Same definition as `two_sided_models_check.model` (reflected return models), but the
3q x 3p high tile is summed by grouping cells by their horizontal state key
(A_a, a mod 3) and vertical key (B_b - event_b, b mod 3).  The cone test depends
only on the pair of keys, so the tile is a finite bilinear form in occupation
integers.  Low rows b<4 and the exceptional origin birth (0,1) are kept exactly.
"""
import sys
from fractions import Fraction as F
from math import gcd
sys.set_int_max_str_digits(0)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def rot(z, k):
    for _ in range(k % 3):
        z = -z[1], z[0] - z[1]
    return z


def side(n, p, q, sign):
    k, r = divmod(n * p, q)
    return k - int(n > 0 and r == 0 and sign < 0)


CORR = (((0, 0), (0, 0), (0, 0)), ((0, 0), (1, 0), (1, 1)), ((0, 0), (0, -1), (1, 0)))
HINC = ((1, 0), (0, -1), (0, 0))
VINC = ((1, 0), (1, 1), (0, 0))


def axes(p, q, sign):
    A = [(1, 0)]
    for a in range(1, 3 * q):
        A.append(add(A[-1], rot(HINC[side(a, p, q, sign) % 3], -a)))
    B = [(1, 0)]
    for b in range(1, 3 * p + 4):
        B.append(add(B[-1], rot(VINC[side(b, q, p, -sign) % 3], -2 * b)))
    return A, B


def event(b, p, q, sign):
    m = lambda k: side(k, q, p, -sign)
    iso = m(b) - m(b - 1) == 2
    pat = m(b - 1) - m(b - 3) == 4
    assert not (iso and pat)
    return rot((1, 0), m(b) - 2 * b) if iso else rot((1, 0), m(b - 1) - 1 - 2 * b) if pat else (0, 0)


def low_eta(x, y, a, b):
    if b == 0:
        return 0
    if b == 1:
        return 1 if a == 0 else int(x >= 1 and y >= 0)
    if b == 2:
        return int(x <= -1 and x - y <= 0)
    return int(min(x, 0) <= y)


def model_value(p, q, sign):
    """Return (N, D) with z = N/D unreduced, D = 27(2^{3q}-1)(3^{3p}-1)."""
    assert gcd(p, q) == 1 and (p + q) % 3 and F(3, 5) < F(p, q) < F(2, 3)
    A, B = axes(p, q, sign)
    L, Lv = 3 * q, 3 * p
    # head: rows b<4, a<3q, with exceptional (0,1) digit removed
    head = 0  # integer  sum c * 2^{L-1-a} 3^{3-b}
    for b in range(4):
        row = 0
        for a in range(L):
            x, y = add(add(A[a], B[b]), CORR[a % 3][b % 3])
            x -= 1
            e = 0 if (a, b) == (0, 1) else low_eta(x, y, a, b)
            row = 2 * row + 1 - 3 * e
        head += row * 3 ** (3 - b)
    # tile occupation integers
    hbits = {}
    for a in range(L):
        k = (A[a], a % 3)
        hbits.setdefault(k, bytearray(b'0' * L))[a] = 49
    hocc = {k: int(v.decode(), 2) for k, v in hbits.items()}  # sum 2^{L-1-a}
    vdig = {}
    for b in range(Lv):
        e = event(b + 4, p, q, sign)
        k = ((B[b + 4][0] - e[0], B[b + 4][1] - e[1]), (b + 4) % 3)
        vdig.setdefault(k, bytearray(b'0' * Lv))[b] = 49
    vocc = {k: int(v.decode(), 3) for k, v in vdig.items()}  # sum 3^{Lv-1-b}
    ones = 0
    for (za, ra), h in hocc.items():
        acc = 0
        for (zb, rb), v in vocc.items():
            c = CORR[ra][rb]
            x = za[0] + zb[0] + c[0] - 1
            y = za[1] + zb[1] + c[1]
            if x <= 0 and x - y <= 0:
                acc += v
        ones += h * acc
    tile = (2 ** L - 1) * (3 ** Lv - 1) // 2 - 3 * ones  # sum (1-3eta) 2^{L-1-a}3^{Lv-1-b}
    # value = head/(2^{L-1}27 H) + tile/(81 H V 2^{L-1}3^{Lv-1}) - 1, H=1-2^-L, V=1-3^-Lv
    # head/(2^{L-1}*27)/(1-2^{-L}) = 2 head / (27 (2^L-1))
    # tile/(81*2^{L-1}3^{Lv-1}(1-2^-L)(1-3^-Lv)) = 2*3*tile/(81 (2^L-1)(3^Lv-1)) = 2 tile/(27 (2^L-1)(3^Lv-1))
    Ah, Bv = 2 ** L - 1, 3 ** Lv - 1
    D = 27 * Ah * Bv
    N = 2 * head * Bv + 2 * tile - D
    return N, D


if __name__ == '__main__':
    import importlib.util
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location('tsm', ROOT / 'Erdos 168 reflected return models/two_sided_models_check.py')
    tsm = importlib.util.module_from_spec(spec); spec.loader.exec_module(tsm)
    for p, q in ((5, 8), (12, 19), (41, 65), (53, 84), (7, 11), (11, 17)):
        if (p + q) % 3 == 0:
            continue
        for s in (1, -1):
            N, D = model_value(p, q, s)
            assert F(N, D) == tsm.model(p, q, s)[4], (p, q, s)
    print('fastmodel agrees with accepted two_sided_models_check.model on all test slopes, both sides')
