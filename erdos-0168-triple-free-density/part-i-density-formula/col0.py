"""U_t(X) = min cover of D_t containing X, X subset of column 0. Test closed forms."""
import numpy as np, sys
from tau_dp import heights
def col0_values(t):
    hs = heights(t)
    G = np.zeros(1, dtype=np.int32); hn = 0
    for a in range(len(hs) - 1, -1, -1):
        h = hs[a]
        S = np.arange(1 << h, dtype=np.int64)
        P = (S & (S >> 1)) & ((1 << hn) - 1)
        pc = np.zeros(1 << h, dtype=np.int32)
        for i in range(h): pc += ((S >> i) & 1).astype(np.int32)
        V = pc + G[P]; W = V.copy()
        for i in range(h):
            W = W.reshape(-1, 2, 1 << i); np.maximum(W[:, 1, :], W[:, 0, :], out=W[:, 1, :]); W = W.reshape(-1)
        if a == 0:
            full = (1 << h) - 1
            U = sum(hs) - W[full ^ np.arange(1 << h)]
            return U, h
        G = W[((1 << h) - 1) ^ np.arange(1 << h)]; hn = h
def popcount_arr(n, h):
    S = np.arange(1 << h, dtype=np.int64); pc = np.zeros(1 << h, dtype=np.int32)
    for i in range(h): pc += ((S >> i) & 1).astype(np.int32)
    return S, pc
if __name__ == "__main__":
    for t in [int(x) for x in sys.argv[1:]]:
        U, h = col0_values(t)
        S, pc = popcount_arr(None, h)
        # column 0 point (0,b) has color -b mod 3
        Xj = [sum(1 << b for b in range(h) if (-b) % 3 == j) for j in range(3)]
        A = [int(U[x]) for x in Xj]
        cand = np.full(1 << h, 10**9)
        for j in range(3): cand = np.minimum(cand, A[j] + pc[S & ~Xj[j]])
        d = cand - U
        bad = np.nonzero(d)[0]
        print(t, "h0", h, "tau", int(U[0]), "A", A, "mismatch", len(bad), "max", int(d.max()), "min", int(d.min()),
              "examples", [(format(int(x), '0%db' % h)[::-1], int(U[x]), int(cand[x])) for x in bad[:4]])
