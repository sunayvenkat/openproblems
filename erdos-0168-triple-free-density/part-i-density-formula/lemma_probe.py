"""Max deficiency over pools: D*(P) = |P| - min{|F| : F meets every corner whose colour-j point lies in P}.
Used to probe (4) axis-avoiding bound and the mandatory-owner lemma (8)."""
import numpy as np, sys
from tau_dp import heights
from eta_rule import Q_vector

def min_cover_required(t, req):
    """req(a,b) -> bool : corner rooted at (a,b) must be hit. Column DP on independent sets of hypergraph of required corners."""
    hs = heights(t)
    G = np.zeros(1, dtype=np.int32); hn = 0
    for a in range(len(hs) - 1, -1, -1):
        h = hs[a]
        S = np.arange(1 << h, dtype=np.int64)
        rm = sum(1 << b for b in range(min(hn, h - 1)) if req(a, b))
        P = (S & (S >> 1)) & rm
        pc = np.zeros(1 << h, dtype=np.int32)
        for i in range(h): pc += ((S >> i) & 1).astype(np.int32)
        W = pc + G[P]
        for i in range(h):
            W = W.reshape(-1, 2, 1 << i); np.maximum(W[:, 1, :], W[:, 0, :], out=W[:, 1, :]); W = W.reshape(-1)
        G = W[((1 << h) - 1) ^ np.arange(1 << h)]; hn = h
    return sum(hs) - int(G[0])

def colour_point(a, b, j):
    for p in ((a, b), (a + 1, b), (a, b + 1)):
        if (p[0] - p[1]) % 3 == j: return p

def Dstar(t, j, pool):
    P = [p for p in pool]
    Ps = set(P)
    return len(P) - min_cover_required(t, lambda a, b: colour_point(a, b, j) in Ps)

def board(t):
    return [(a, b) for a in range(200) if 2**a <= t for b in range(200) if 2**a * 3**b <= t]

def exceptional(t):
    from fractions import Fraction as Fr
    A = 1
    while 2**A <= t:
        e = 2**A
        if Fr(2, 3) * t < e <= t or (A >= 2 and 6 * e <= t < Fr(27, 4) * e): return (A, 0)
        A += 1
    return None

if __name__ == "__main__":
    lim = int(sys.argv[1])
    sm = sorted(2**a * 3**b for a in range(60) for b in range(40) if 18 <= 2**a * 3**b <= lim)
    pt = {6: (1, 1), 12: (2, 1), 18: (1, 2)}
    m_of = {0: (1, 1), 1: (2, 1), 2: (1, 2)}
    viol4 = viol8 = 0; cnt8 = 0
    for t in sm:
        B = board(t); e = exceptional(t)
        Bmax = max(b for a, b in B); jtop = (-Bmax) % 3
        for j in range(3):
            pool = [p for p in B if (p[0] - p[1]) % 3 == j and p != e]
            # (4): axis-avoiding part of allowed pool has max deficiency <= 0
            if Dstar(t, j, [p for p in pool if p[0] >= 1]) > 0: viol4 += 1; print("(4) fails", t, j)
            if j != jtop:
                D = Dstar(t, j, pool)
                if D > 0:
                    cnt8 += 1
                    if Dstar(t, j, [p for p in pool if p != m_of[j]]) >= D: viol8 += 1; print("(8) fails", t, j)
    print("t in [18,%d]: (4) violations %d; mandatory-owner cases tested %d, violations %d" % (lim, viol4, cnt8, viol8))
