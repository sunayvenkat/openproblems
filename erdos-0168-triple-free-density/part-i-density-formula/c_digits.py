"""Rigorous enclosure of c = 1 - (1/3) sum_d eta_d/d using the explicit increment rule (exact integer arithmetic)."""
import sys
from fractions import Fraction as Fr
from eta_rule import increments, Q_vector
from decimal import Decimal, getcontext

def enclosure(N):
    sm = sorted(2**a * 3**b for a in range(N.bit_length() + 1) for b in range(N.bit_length()) if 2**a * 3**b <= N)
    amax = max(v for v in range(N.bit_length() + 1) if 2**v <= N); bmax = 0
    while 3**(bmax + 1) <= N: bmax += 1
    den = 2**amax * 3**bmax
    Q = Q_vector(2); num = 0; ones = 0
    for d in sm:
        if d < 3: continue
        inc = increments(d); m = min(Q)
        eta = all(j in inc for j in range(3) if Q[j] == m)
        for j in inc: Q[j] += 1
        if eta: num += den // d; ones += 1
    S = Fr(num, den)
    # tail: sum_{d>N} 1/d <= sum_{b>=0} 3^-b * 2 * 2^-a_b,  a_b = least a with 2^a 3^b > N
    tail = Fr(0); b = 0
    while True:
        a = 0
        while 2**a * 3**b <= N: a += 1
        tail += Fr(2, 2**a * 3**b)
        if a == 0: break
        b += 1
    tail += Fr(1, 3**b)   # remaining b' > b all have a=0: sum 2*3^-b' = 3^-b
    hi = 1 - S / 3
    lo = hi - tail / 3
    return lo, hi, len(sm), ones, min(Q)

if __name__ == "__main__":
    N = 10**int(sys.argv[1])
    lo, hi, n, ones, tau = enclosure(N)
    getcontext().prec = 140
    L = Decimal(lo.numerator) / Decimal(lo.denominator); H = Decimal(hi.numerator) / Decimal(hi.denominator)
    print("N = 10^%s, smooth terms %d, eta=1 count %d, tau(N) = %d" % (sys.argv[1], n, ones, tau))
    print("lower", L); print("upper", H); print("width", H - L)
