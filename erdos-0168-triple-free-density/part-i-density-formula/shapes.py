"""tau for general down-set shapes given by row widths w_0>=w_1>=..., via column DP."""
import numpy as np
import itertools, random

def tau_rows(w):
    w = [x for x in w if x > 0]
    if not w: return 0
    hs = [sum(1 for x in w if x > a) for a in range(w[0])]
    G = np.zeros(1, dtype=np.int32); hn = 0
    for a in range(len(hs) - 1, -1, -1):
        h = hs[a]
        S = np.arange(1 << h, dtype=np.int64)
        P = (S & (S >> 1)) & ((1 << hn) - 1)
        pc = np.zeros(1 << h, dtype=np.int32)
        for i in range(h): pc += ((S >> i) & 1).astype(np.int32)
        W = (pc + G[P]).copy()
        for i in range(h):
            W = W.reshape(-1, 2, 1 << i)
            np.maximum(W[:, 1, :], W[:, 0, :], out=W[:, 1, :]); W = W.reshape(-1)
        G = W[((1 << h) - 1) ^ np.arange(1 << h)]; hn = h
    return sum(w) - int(G[0])

def Kcounts(w):
    K = [0, 0, 0]
    for b, x in enumerate(w):
        for a in range(x): K[(a - b) % 3] += 1
    return K

def formula_rows(w):
    w = [x for x in w if x > 0] + [0, 0, 0, 0]
    K = Kcounts(w)
    d = [0, 0, 0]
    if w[0] - w[1] == 2 and w[0] >= 2: d[(w[0] - 1) % 3] += 1          # isolate at (w0-1,0)
    if (w[0]-w[1], w[1]-w[2], w[2]-w[3]) == (1, 2, 2) and w[3] >= 1: d[w[0] % 3] += 1  # patch
    return min(K[j] - d[j] for j in range(3))

def sturm_rows(t):
    w = []; b = 0
    while 3**b <= t:
        a = 0
        while 2**a * 3**b <= t: a += 1
        w.append(a); b += 1
    return w
