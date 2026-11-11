"""Exhaustive stress test of the structural lemmas of PROOF.md on actual boards (independent code).

For every 3-smooth t in [3, N] and every colour j:
  * Lemma 2.1 owner lists vs corners enumerated directly;
  * Lemma 2.2: tau = K_j - D_j  (tau from audit_formula.tau_dp);
  * all tight sets U (d(U)=D>0, all proper subsets < D): Lemma 4.1(i),(ii) for every minimum vertex cover W,
    Lemma 5.1 predecessor property;
  * all critical sets with a>=1 everywhere: Lemma 5.2 classification;
  * Corollary 5.3;
  * all inclusion-minimal maximisers U of D*_j over A_j: Lemmas 6.1, (6.1), 6.2, 6.4, 6.5, 6.6(a-e) (6.6(e) for
    every minimum vertex cover), 6.8, 6.9, 6.10.
Usage: python audit_struct.py N [full41_limit]
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations
from audit_formula import tau_dp, Q, smooth_upto

val = lambda p: 2 ** p[0] * 3 ** p[1]
col = lambda p: (p[0] - p[1]) % 3


def board(t):
    return [(a, b) for a in range(64) for b in range(41) if 2 ** a * 3 ** b <= t]


def exceptional(t):
    t = Fr(t)
    for A in range(1, 64):
        e = 2 ** A
        if e > t:
            break
        if Fr(2, 3) * t < e <= t:
            return (A, 0), "isolate"
        if A >= 2 and 6 * e <= t < Fr(27, 4) * e:
            return (A, 0), "patch"
    return None, None


def edges_for(t, j):
    """owner -> list of (left, right, kind), built from corners directly."""
    B = set(board(t))
    own = {p: [] for p in B if col(p) == j}
    for (a, b) in B:
        if val((a, b)) * 3 <= t:
            T = [(a, b), (a + 1, b), (a, b + 1)]
            u = [p for p in T if col(p) == j][0]
            l = [p for p in T if col(p) == (j + 1) % 3][0]
            r = [p for p in T if col(p) == (j + 2) % 3][0]
            kind = {(a, b): "R", (a + 1, b): "E", (a, b + 1): "N"}[u]
            own[u].append((l, r, kind))
    return own


def lemma21_check(t, j, own):
    B = set(board(t))
    for (a, b), es in own.items():
        exp = []
        u = (a, b)
        if b >= 1:
            exp.append(((a, b - 1), (a + 1, b - 1), "N"))
        if a >= 1 and (a - 1, b + 1) in B:
            exp.append(((a - 1, b + 1), (a - 1, b), "E"))
        if (a, b + 1) in B:
            exp.append(((a + 1, b), (a, b + 1), "R"))
        assert sorted(es) == sorted(exp), (t, j, u, es, exp)


def matching(Ulist, own):
    adj = {}
    for u in Ulist:
        for (l, r, _) in own[u]:
            adj.setdefault(l, []).append(r)
    mate = {}

    def aug(l, seen):
        for r in adj[l]:
            if r in seen:
                continue
            seen.add(r)
            if r not in mate or aug(mate[r], seen):
                mate[r] = l
                return True
        return False

    return sum(1 for l in adj if aug(l, set()))


def edge_list(Ulist, own):
    return [(l, r, u) for u in Ulist for (l, r, _) in own[u]]


def min_vertex_covers(E, nu):
    """all vertex covers of size nu (they are exactly the minimum ones)."""
    out = []

    def rec(i, W, forb):
        if len(W) > nu:
            return
        while i < len(E) and (E[i][0] in W or E[i][1] in W):
            i += 1
        if i == len(E):
            if len(W) == nu:
                out.append(frozenset(W))
            return
        l, r, _ = E[i]
        if l not in forb:
            rec(i + 1, W | {l}, forb)
        if r not in forb:
            rec(i + 1, W | {r}, forb | {l})

    rec(0, frozenset(), frozenset())
    return list(set(out))


def check41(U, own, D, full):
    E = edge_list(U, own)
    nu = len(U) - D
    Ws = min_vertex_covers(E, nu)
    assert Ws, "no min cover?"
    for W in Ws:
        for w in W:
            uniq = {u for (l, r, u) in E if (l == w and r not in W) or (r == w and l not in W)}
            assert len(uniq) >= 2, ("4.1(i) fails", U, W, w)
        if full and len(W) <= 12:
            Wl = sorted(W)
            for k in range(1, len(Wl) + 1):
                for S in combinations(Wl, k):
                    S = set(S)
                    T = {u for (l, r, u) in E if l in S or r in S}
                    assert len(T) >= len(S) + 1, ("4.1(ii) fails", U, W, S)
    return Ws


def cone_coords(p, base):
    da, db = p[0] - base[0], p[1] - base[1]
    if (2 * da + db) % 3 or (da + 2 * db) % 3:
        return None
    return ((2 * da + db) // 3, (da + 2 * db) // 3)


def in_cone(p, base):
    c = cone_coords(p, base)
    return c is not None and c[0] >= 0 and c[1] >= 0


WINDOWS = [(54, 72), (216, 243), (576, 648), (5184, 5832)]


def analyse(N, full41):
    stats = dict(tight=0, covers=0, critical_a1=0, minmax=0, caseO=0, D1=0, D2=0, I=0)
    seenI = []
    for t in [t for t in smooth_upto(N) if t >= 3]:
        tau = tau_dp(t)
        e, ekind = exceptional(t)
        Bd = board(t)
        jtop = (-max(b for (a, b) in Bd)) % 3
        for j in range(3):
            own = edges_for(t, j)
            lemma21_check(t, j, own)
            C = sorted(own, key=val)
            n = len(C)
            d = [0] * (1 << n)
            for m in range(1 << n):
                U = [C[i] for i in range(n) if m >> i & 1]
                d[m] = len(U) - matching(U, own)
            Dj = max(d)
            assert tau == len(C) - Dj, ("2.2", t, j)
            # tight sets
            Msub = [0] * (1 << n)
            for m in range(1 << n):
                best = d[m]
                for i in range(n):
                    if m >> i & 1:
                        best = max(best, Msub[m ^ (1 << i)])
                Msub[m] = best
            for m in range(1, 1 << n):
                if d[m] > 0 and all(Msub[m ^ (1 << i)] < d[m] for i in range(n) if m >> i & 1):
                    U = [C[i] for i in range(n) if m >> i & 1]
                    stats["tight"] += 1
                    Ws = check41(U, own, d[m], full41 and t <= full41)
                    stats["covers"] += len(Ws)
                    Us = set(U)
                    for u in U:  # Lemma 5.1
                        if u[0] >= 1 and u[1] >= 1:
                            pred = [(u[0] - 1, u[1] - 1), (u[0] + 1, u[1] - 2), (u[0] - 2, u[1] + 1)]
                            assert any(p in Us for p in pred), ("5.1", t, j, U, u)
                    # Lemma 5.2: critical with all a>=1
                    if d[m] == 1 and Msub[m] == 1 and all(u[0] >= 1 for u in U):
                        stats["critical_a1"] += 1
                        x = min(U, key=val)
                        A = x[0]
                        ok = (x[1] == 0 and len(U) == 1 and Fr(2, 3) * t < val(x)) or \
                             (x[1] == 0 and A >= 2 and set(U) == {x, (A - 1, 2), (A + 1, 1)}
                              and 6 * val(x) <= t < Fr(27, 4) * val(x))
                        assert ok, ("5.2", t, j, U)
            # Corollary 5.3 and section 6
            Aj = [i for i in range(n) if C[i] != e]
            Amask = sum(1 << i for i in Aj)
            a1mask = sum(1 << i for i in Aj if C[i][0] >= 1)
            for m in range(1 << n):
                if m & a1mask == m:
                    assert d[m] <= 0, ("5.3", t, j)
            Dstar = max(d[m] for m in range(1 << n) if m & Amask == m)
            assert Dstar >= Dj - (1 if (e is not None and col(e) == j) else 0)
            if Dstar <= 0:
                continue
            has = [False] * (1 << n)
            for m in range(1 << n):
                if m & Amask != m:
                    continue
                has[m] = d[m] == Dstar or any(has[m ^ (1 << i)] for i in range(n) if m >> i & 1)
            for m in range(1 << n):
                if m & Amask != m or d[m] != Dstar:
                    continue
                if any(has[m ^ (1 << i)] for i in range(n) if m >> i & 1):
                    continue
                stats["minmax"] += 1
                U = [C[i] for i in range(n) if m >> i & 1]
                Us = set(U)
                bz = [u for u in U if u[1] == 0]
                az = [u for u in U if u[0] == 0]
                assert bz and az, ("6.1", t, j, U)
                x = min(bz, key=val)
                y = min(az, key=val)
                E = edge_list(U, own)
                Ws = min_vertex_covers(E, len(U) - Dstar)
                if x == (0, 0):
                    stats["caseO"] += 1
                    assert j == 0
                    if t >= 18:
                        assert (1, 1) in Us, ("6.10 O", t, U)
                    continue
                A, B = x[0], y[1]
                assert (2 * A - B) % 3 == 0
                r, s = (2 * A - B) // 3, (2 * B - A) // 3
                assert r >= 0 and s >= 0, ("6.2", t, j, U)
                assert all(in_cone(u, x) or in_cone(u, y) for u in U), ("(6.1)", t, j, U)
                mj = {0: (1, 1), 1: (2, 1), 2: (1, 2)}[j]
                if s == 0:
                    stats["D1"] += 1
                    assert B <= 2, ("6.4", t, j, U)
                    if t >= 18:
                        assert mj in Us, ("6.10 D1", t, j, U)
                elif r == 0:
                    stats["D2"] += 1
                    assert A <= 2, ("6.5", t, j, U)
                    if t >= 18:
                        assert mj in Us, ("6.10 D2", t, j, U)
                else:
                    stats["I"] += 1
                    seenI.append((t, j, r, s, sorted(U, key=val)))
                    assert 3 * val(y) > t, ("6.6a", t, U)
                    assert r in (1, 2), ("6.6b", t, U)
                    assert az == [y] and j == jtop, ("6.6c", t, U)
                    assert Dstar == 1, ("6.6d", t, U)
                    assert any(lo <= t < hi for lo, hi in WINDOWS), ("6.8", t, U)
                    if r == 1:
                        assert s <= 3, ("6.9", t, U)
                    z = (A - s, 2 * s)
                    assert 3 * val(z) <= 2 * t, ("6.6e z", t, U)
                    for W in Ws:
                        for k in range(s):
                            u = (A - k, 2 * k)
                            gu1 = (A - k - 1 + 2, 2 * (k + 1) - 1)
                            assert u in Us and gu1 in Us, ("6.6e U", t, U)
                            assert (u[0] - 1, u[1] + 1) in W and (u[0] + 1, u[1]) in W, ("6.6e W", t, U, W)
                            assert (u[0], u[1] + 1) not in W, ("6.6e notW", t, U, W)
    return stats, seenI


if __name__ == "__main__":
    N = int(sys.argv[1])
    full41 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    st, I = analyse(N, full41)
    print("all assertions passed for 3-smooth t in [3,%d]" % N, st)
    for row in I:
        print("case (I) maximiser:", row)
