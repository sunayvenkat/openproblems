"""Top-down row transfer: U_b(Z) = min cost of rows >= b with Z forced into row b."""
import numpy as np
def popc(n, w):
    S = np.arange(1 << w, dtype=np.int64); pc = np.zeros(1 << w, dtype=np.int32)
    for i in range(w): pc += ((S >> i) & 1).astype(np.int32)
    return S, pc
def supmin(V, w):
    U = V.copy()
    for i in range(w):
        U = U.reshape(-1, 2, 1 << i)
        np.minimum(U[:, 0, :], U[:, 1, :], out=U[:, 0, :]); U = U.reshape(-1)
    return U
def row_dp(w):
    """w: row widths bottom->top. returns list U[b] arrays (index by bitmask of row b)."""
    B = len(w) - 1
    Us = [None] * (B + 1)
    S, pc = popc(None, w[B]); Us[B] = pc.copy()
    for b in range(B - 1, -1, -1):
        S, pc = popc(None, w[b]); m = (1 << w[b + 1]) - 1
        Z = (~S) & (~(S >> 1)) & m
        V = pc + Us[b + 1][Z]
        Us[b] = supmin(V, w[b])
    return Us
def phase_mask(wb, b, j):
    return sum(1 << a for a in range(wb) if (a - b) % 3 == j)
