"""Independent check of formula (C): tau(t) = min_j (K_j - I_j - P_j), and of the tables in PROOF.md sections 8, 9.

tau is computed by an exact column DP (no code from the parent directory is used).
Column a holds positions b with 2^a 3^b <= t. Corner rooted at (a,b) uses (a,b),(a,b+1),(a+1,b)
and exists iff 3*2^a*3^b <= t.  Usage: python audit_formula.py [N]
"""
import sys
from fractions import Fraction as Fr
import numpy as np


def heights(t):
    h, a = [], 0
    while 2 ** a <= t:
        b = 0
        while 2 ** a * 3 ** (b + 1) <= t:
            b += 1
        h.append(b + 1)
        a += 1
    return h


def tau_dp(t):
    h = heights(t)
    INF = 10 ** 9
    pc = lambda n: np.array([bin(i).count("1") for i in range(1 << n)], dtype=np.int64)
    f = pc(h[0])
    for a in range(len(h) - 1):
        ha, hb = h[a], h[a + 1]
        S = np.arange(1 << ha, dtype=np.int64)
        lowmask = (1 << (ha - 1)) - 1 if ha >= 2 else 0   # corners rooted at b = 0..ha-2
        req = (~S) & (~(S >> 1)) & lowmask
        assert int(req.max(initial=0)) < (1 << hb)
        g = np.full(1 << hb, INF, dtype=np.int64)
        np.minimum.at(g, req, f)
        for bit in range(hb):                 # subset-min transform
            idx = np.arange(1 << hb)
            m = (idx >> bit) & 1 == 1
            g[m] = np.minimum(g[m], g[idx[m] ^ (1 << bit)])
        f = pc(hb) + g
    assert h[-1] == 1 or len(h) == 1
    # last column: corners rooted there need 3r<=t; height 1 means none
    return int(f.min())


def Q(t, patchA1=False):
    t = Fr(t)
    K = [0, 0, 0]
    a = 0
    while 2 ** a <= t:
        b = 0
        while 2 ** a * 3 ** b <= t:
            K[(a - b) % 3] += 1
            b += 1
        a += 1
    I, P = [0, 0, 0], [0, 0, 0]
    A = 1
    while 2 ** A <= t:
        e = 2 ** A
        if Fr(2, 3) * t < e <= t:
            I[A % 3] += 1
        if A >= (1 if patchA1 else 2) and 6 * e <= t < Fr(27, 4) * e:
            P[A % 3] += 1
        A += 1
    return K, I, P, [K[j] - I[j] - P[j] for j in range(3)]


def smooth_upto(N):
    return sorted(2 ** a * 3 ** b for a in range(70) for b in range(45) if 2 ** a * 3 ** b <= N)


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
    # breakpoints of tau and of Q are 3-smooth or (A=1 patch) 27/2; check all 3-smooth t and t=27/2-eps region
    pts = [t for t in smooth_upto(N) if t >= 3]
    bad = 0
    for t in pts:
        tau = tau_dp(t)
        M = min(Q(t)[3])
        M1 = min(Q(t, True)[3])
        if not (tau == M == M1):
            bad += 1
            print("MISMATCH", t, tau, M, M1)
    # t = 13 lies in [12, 27/2) (A=1 patch window); t=13.5 is a breakpoint of P only
    for t in (Fr(13), Fr(27, 2)):
        print("t=%s tau(floor)=%d Q=%s Q(A=1 patch)=%s" % (t, tau_dp(int(t)), Q(t)[3], Q(t, True)[3]))
    print("checked %d 3-smooth t in [3,%d]; mismatches: %d" % (len(pts), N, bad))

    print("\nSection 8 windows:")
    sm = smooth_upto(10 ** 5)
    for lo, hi in [(54, 64), (64, 72), (216, 243), (576, 648), (5184, 5832)]:
        inside = [u for u in sm if lo < u < hi]
        K, I, P, q = Q(lo)
        h = heights(lo)
        # row widths: row b = number of a with 2^a 3^b <= t
        rows = [sum(1 for a in range(len(h)) if h[a] > b) for b in range(h[0])]
        jtop = (-(len(rows) - 1)) % 3   # floor(log3 t) = h[0]-1
        # constancy of Q on window: check at lo and at hi - tiny
        q_hi = Q(Fr(hi) - Fr(1, 10 ** 6))[3]
        print(f"[{lo},{hi}) smooth inside={inside} rows={rows} K={K} I={I} P={P} Q={q} Q(hi-)={q_hi} "
              f"jtop={jtop} Qtop={q[jtop]} M={min(q)} tau={tau_dp(lo)} Qtop>M={q[jtop] > min(q)}")

    print("\nSection 9:")
    for t in [3, 4, 6, 8, 9, 12, 16]:
        print(t, "tau", tau_dp(t), "Q", Q(t)[3], "Q(A=1)", Q(t, True)[3])
