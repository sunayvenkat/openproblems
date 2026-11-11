"""Explicit increment rule for eta_d derived from formula (C); checked against exact DP taus."""
from fractions import Fraction as Fr
import sys

def v2v3(d):
    a = b = 0
    while d % 2 == 0: d //= 2; a += 1
    while d % 3 == 0: d //= 3; b += 1
    assert d == 1
    return a, b

def Q_vector(t):
    """Adjusted counts Q_j(t) = K_j - I_j - P_j (t real >= 1)."""
    t = Fr(t); K = [0, 0, 0]; a = 0
    while 2**a <= t:
        b = 0
        while 2**a * 3**b <= t: K[(a - b) % 3] += 1; b += 1
        a += 1
    A = 1
    while 2**A <= t:
        e = 2**A
        if Fr(2, 3) * t < e <= t: K[A % 3] -= 1
        if A >= 2 and 6 * e <= t < Fr(27, 4) * e: K[A % 3] -= 1   # A=1 patch window [12,27/2) never changes min, dropped
        A += 1
    return K

def increments(d):
    """Set (multiset) of colours whose Q increases by 1 at the smooth cutoff d (d >= 3)."""
    a, b = v2v3(d)
    if b == 0:                      # d = 2^a: point and isolate in same colour
        return []
    if b == 1:                      # d = 3*2^m: isolate 2^(m+1) dies
        m = a
        if m >= 3: return [(m + 1) % 3]          # patch rooted at 2^(m-1) is born, same colour as point
        return [(m + 1) % 3, (m + 2) % 3]        # m = 0,1,2: point colour m-1 and dying isolate colour m+1
    if b == 3:                      # d = 27*2^n: patch rooted at 2^(n+2) dies
        n = a
        return [n % 3, (n + 2) % 3]
    return [(a - b) % 3]

def eta_rule(d, Qprev):
    """eta_d = 1 iff every minimiser of Q(d^-) is incremented."""
    inc = set(increments(d)); m = min(Qprev)
    return int(all(j in inc for j in range(3) if Qprev[j] == m))

if __name__ == "__main__":
    lim = int(sys.argv[1])
    sm = sorted(2**a * 3**b for a in range(400) for b in range(260) if 2**a * 3**b <= lim)
    # tau from DP for verification (cheap range)
    from tau_dp import max_indep
    prevQ = Q_vector(2); prev_tau = 0; bad = 0
    for d in sm:
        if d < 3: continue
        Qd = Q_vector(d)
        # increments predicted vs actual Q change
        pred = [0, 0, 0]
        for j in increments(d): pred[j] += 1
        actual = [Qd[j] - prevQ[j] for j in range(3)]
        assert pred == actual, (d, pred, actual)
        e = eta_rule(d, prevQ)
        assert e == min(Qd) - min(prevQ)
        if d <= 10**9:
            mi, n = max_indep(d); tau = n - mi
            if tau - prev_tau != e: bad += 1; print("eta mismatch", d)
            prev_tau = tau
        prevQ = Qd
    print("increment table verified for all smooth 3<=d<=", lim, "; DP eta mismatches (d<=1e9):", bad)
