"""Exact cone sums for the requested resonant models 7/11 and 8/13."""
import sys
sys.dont_write_bytecode = True

from fractions import Fraction as F
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("skew", Path(__file__).with_name("skew_denominator_check.py"))
skew = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skew)
old, add = skew.old, skew.add


def ceildiv(a, b):
    return -((-a)//b)


def cone_sum(x, y, X, Y, lower):
    """Sum X^i Y^j for F((x,y)+i*dA+j*dB)=1."""
    d = x-y
    if lower:
        stop = max(0, ceildiv(-x, 2), ceildiv(d-2*x, 3))
        head = sum((X**i * Y**max(0, 2*i+x, ceildiv(i+d, 2))
                    for i in range(stop)), F(0))/(1-Y)
        return head + X**stop * Y**(2*stop+x)/((1-Y)*(1-X*Y**2))
    stop = max(0, d, ceildiv(x, 2), ceildiv(2*x-d, 3))
    head = sum((X**i * (1-Y**(min(2*i-x, (i-d)//2)+1))/(1-Y)
                for i in range(stop) if min(2*i-x, (i-d)//2) >= 0), F(0))
    tail = X**stop/((1-X)*(1-Y))
    tail -= (X**stop * Y**((stop-d)//2+1)
             + X**(stop+1)*Y**((stop+1-d)//2+1))/((1-Y)*(1-X**2*Y))
    return head+tail


def exact_model(p, q):
    assert (p, q) in ((7, 11), (8, 13))
    sigma = 1 if 2**q > 3**p else -1
    P, Q = 3*q, 3*p
    A, B = [(1, 0)], [(1, 0)]
    for a in range(1, 2*P+1):
        inc = ((1, 0), (0, -1), (0, 0))[old.floor_side(a, p, q, sigma) % 3]
        A.append(add(A[-1], old.rot(inc, -a)))
    for b in range(1, 2*Q+4):
        inc = ((1, 0), (1, 1), (0, 0))[old.floor_side(b, q, p, -sigma) % 3]
        B.append(add(B[-1], old.rot(inc, -2*b)))
    da = A[P][0]-1, A[P][1]
    db = B[Q][0]-1, B[Q][1]
    assert da == (2*sigma, sigma) and db == (-sigma, sigma)
    assert all(A[a+P] == add(A[a], da) for a in range(P+1))
    assert all(B[b+Q] == add(B[b], db) for b in range(Q+4))

    def state(a, b):
        i, r = divmod(a, P)
        j, s = divmod(b, Q)
        z = add(add(A[r], (i*da[0], i*da[1])), add(B[s], (j*db[0], j*db[1])))
        z = add(z, old.CORRECTION[a % 3][b % 3])
        return z[0]-1, z[1]

    def epsilon(b):
        m = lambda k: old.floor_side(k, q, p, -sigma)
        isolated, patch = m(b)-m(b-1) == 2, m(b-1)-m(b-3) == 4
        assert not (isolated and patch)
        color = (m(b)-2*b) % 3 if isolated else (m(b-1)-1-2*b) % 3
        return old.rot((1, 0), color) if isolated or patch else (0, 0)

    def eta(a, b):
        x, y = state(a, b)
        if b == 0:
            return 0
        if b == 1:
            return 1 if a == 0 else int(x >= 1 and y >= 0)
        if b == 2:
            return int(x <= -1 and x-y <= 0)
        if b == 3:
            return int(min(x, 0) <= y)
        e = epsilon(b)
        return skew.cone((x-e[0], y-e[1]))

    X, Y = F(1, 2**P), F(1, 3**Q)
    total = F(0)
    max_stop = 0
    max_low = 0
    max_state = 1
    for a in range(P):
        for b in range(4):
            x, y = state(a, b)
            max_state = max(max_state, abs(x), abs(x-y))
            stop = abs(x)+abs(y)+4
            max_low = max(max_low, stop)
            tail = eta(a+stop*P, b)
            assert tail == eta(a+(stop+1)*P, b)
            term = sum((F(eta(a+i*P, b))*X**i for i in range(stop)), F(0))
            total += (term+tail*X**stop/(1-X))/2**a/3**b
        for b in range(4, 4+Q):
            e = epsilon(b)
            assert e == epsilon(b+p)
            z = state(a, b)
            x, y = z[0]-e[0], z[1]-e[1]
            max_state = max(max_state, abs(x), abs(x-y))
            ta, tb = (q, 2*p) if sigma > 0 else (2*q, p)
            shifted = state(a+ta, b+tb)
            assert epsilon(b+tb) == e
            assert (shifted[0]-z[0], shifted[1]-z[1]) == old.rot((1, 0), q)
            stop = (max(0, ceildiv(-x, 2), ceildiv(-x-y, 3)) if sigma > 0
                    else max(0, x-y, ceildiv(x, 2), ceildiv(x+y, 3)))
            max_stop = max(max_stop, stop)
            total += cone_sum(x, y, X, Y, sigma > 0)/2**a/3**b
    partial = sum((F(eta(a, b), 2**a*3**b)
                   for a in range(2*P) for b in range(2*Q+4)), F(0))
    tail_bound = 3*(F(1, 2**(2*P))+F(1, 3**(2*Q+4))-F(1, 2**(2*P)*3**(2*Q+4)))
    assert 0 <= total-partial <= tail_bound
    value = 3-3*total
    denominator = value.denominator
    two = three = 0
    while denominator % 2 == 0:
        denominator //= 2
        two += 1
    while denominator % 3 == 0:
        denominator //= 3
        three += 1
    diagonal = 2**q*3**(2*p)-1 if sigma > 0 else 2**(2*q)*3**p-1
    assert diagonal % denominator == 0
    first_a = next(n for n in range(1, 4*q+1)
                   if old.exact_power_floor(n, 2, 3) != old.floor_side(n, p, q, sigma))
    first_b = next(n for n in range(1, 4*p+1)
                   if old.exact_power_floor(n, 3, 2) != old.floor_side(n, q, p, -sigma))
    assert (first_a, first_b) == ((19, 12) if p == 7 else (8, 5))
    print({"p": p, "q": q, "sigma": sigma, "dA": da, "dB": db,
           "denominator_v2": two, "denominator_v3": three,
           "nonS_denominator": denominator, "diagonal": diagonal,
           "diagonal_cancel": diagonal//denominator,
           "max_base_state": max_state,
           "first_floor_disagreements": [first_a, first_b],
           "max_block_cone_stop": max_stop, "safe_low_stop": max_low,
           "reduced_denominator_bits": value.denominator.bit_length()})


if __name__ == "__main__":
    # Independent finite sums check both rational cone formulas and their tails.
    X, Y = F(1, 4), F(1, 9)
    for x, y in ((0, 0), (-2, 1), (3, -1)):
        for lower in (False, True):
            da, db = ((2, 1), (-1, 1)) if lower else ((-2, -1), (1, -1))
            finite = sum((X**i*Y**j for i in range(12) for j in range(12)
                          if skew.cone((x+i*da[0]+j*db[0], y+i*da[1]+j*db[1]))), F(0))
            remainder = cone_sum(x, y, X, Y, lower)-finite
            assert 0 <= remainder <= (X**12+Y**12-X**12*Y**12)/((1-X)*(1-Y))
    exact_model(7, 11)
    exact_model(8, 13)
