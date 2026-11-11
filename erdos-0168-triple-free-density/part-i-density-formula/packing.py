"""Max number of pairwise disjoint corners (same-orientation L-trominoes) in a down-set given by row widths."""
from functools import lru_cache
def pack_rows(w):
    w = [x for x in w if x > 0]
    if not w: return 0
    hs = [sum(1 for x in w if x > a) for a in range(w[0])] + [0]
    n = len(hs) - 1
    # state: bitmask of cells in column a occupied by trominoes rooted in column a-1
    @lru_cache(maxsize=None)
    def best(a, occ):
        if a >= n: return 0
        h, hn = hs[a], hs[a + 1]
        res = 0
        # enumerate root sets R: roots b need b,b+1 free in column a, b < hn, b+1 < h; disjoint pairs
        def rec(b, R, cnt, used):
            nonlocal res
            if b >= h:
                v = cnt + best(a + 1, R)
                if v > res: res = v
                return
            rec(b + 1, R, cnt, used)
            if b < hn and b + 1 < h and not (occ >> b) & 1 and not (occ >> (b + 1)) & 1 and not (used >> b) & 1:
                rec(b + 2, R | (1 << b), cnt + 1, used | (1 << b) | (1 << (b + 1)))
        rec(0, 0, 0, 0)
        return res
    return best(0, 0)
