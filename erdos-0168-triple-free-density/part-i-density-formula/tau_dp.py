"""Exact tau(t) for D_t = {2^a 3^b <= t} via column transfer DP, compared with formula (C)."""
import numpy as np
from fractions import Fraction as Fr

def heights(t):
    hs = []
    a = 0
    while 2**a <= t:
        h = 0
        while 2**a * 3**h <= t:
            h += 1
        hs.append(h); a += 1
    return hs

def max_indep(t):
    hs = heights(t)
    G = np.zeros(1, dtype=np.int32)  # G for column beyond last: h=0
    hn = 0
    for a in range(len(hs) - 1, -1, -1):
        h = hs[a]
        S = np.arange(1 << h, dtype=np.int64)
        P = (S & (S >> 1)) & ((1 << hn) - 1)
        pc = np.zeros(1 << h, dtype=np.int32)
        for i in range(h):
            pc += ((S >> i) & 1).astype(np.int32)
        V = pc + G[P]
        W = V.copy()
        for i in range(h):
            W = W.reshape(-1, 2, 1 << i)
            np.maximum(W[:, 1, :], W[:, 0, :], out=W[:, 1, :])
            W = W.reshape(-1)
        full = (1 << h) - 1
        G = W[full ^ np.arange(1 << h)]
        hn = h
    return int(G[0]), sum(hs)

def formula(t):
    t = Fr(t)
    if t < 3:
        return 0
    K = [0, 0, 0]
    a = 0
    while 2**a <= t:
        b = 0
        while 2**a * 3**b <= t:
            K[(a - b) % 3] += 1; b += 1
        a += 1
    I = [0, 0, 0]; P = [0, 0, 0]
    A = 1
    while 2**A <= t:
        e = 2**A
        if Fr(2, 3) * t < e <= t: I[A % 3] = 1
        if 6 * e <= t < Fr(27, 4) * e: P[A % 3] = 1
        A += 1
    return min(K[j] - I[j] - P[j] for j in range(3))

if __name__ == "__main__":
    import sys
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
    sm = sorted(2**a * 3**b for a in range(64) for b in range(41) if 2**a * 3**b <= lim)
    bad = 0; prev = 0; etas = []
    for d in sm:
        mi, n = max_indep(d)
        tau = n - mi
        f = formula(d)
        if tau != f:
            bad += 1; print("MISMATCH", d, tau, f)
        etas.append((d, tau - prev)); prev = tau
    # also check the non-smooth breakpoint 27/2
    print("t=13.5 formula", formula(Fr(27, 2)), "tau", max_indep(13)[1] - max_indep(13)[0])
    print("checked", len(sm), "smooth cutoffs up to", lim, "mismatches", bad)
    print("last tau", prev)
