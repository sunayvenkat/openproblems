"""Symbolic audit of the exponent identities, owner lists, cone-coordinate claims and availability ratios used in PROOF.md.
Points are exponent vectors (a,b) with symbolic integer entries, so each identity is checked for all parameter values.
Ratio bounds are exact rational constants."""
import sympy as sp
from fractions import Fraction as Fr

A, B, n, i, k, r, s = sp.symbols('A B n i k r s', integer=True)
a_, b_ = sp.symbols('a b', integer=True)
checks = []

def V(a, b): return (sp.expand(a), sp.expand(b))
def mul(p, f): return V(p[0] + f[0], p[1] + f[1])
def inv(f): return (-f[0], -f[1])
def pw(f, e): return (f[0] * e, f[1] * e)
def comb(*fs): return (sum(f[0] for f in fs), sum(f[1] for f in fs))
two, three, g, q = (1, 0), (0, 1), (2, -1), (-1, 2)
half, third = inv(two), inv(three)

def eq(p, p2, msg):
    assert all(sp.simplify(p[t] - p2[t]) == 0 for t in range(2)), (msg, p, p2)
    checks.append(msg)

def colour(p): return sp.Mod(p[0] - p[1], 3)

def coords(base, p):
    """(m, n) with p = base * g^m q^n."""
    da, db = sp.expand(p[0] - base[0]), sp.expand(p[1] - base[1])
    return (sp.simplify((2 * da + db) / 3), sp.simplify((da + 2 * db) / 3))

def val(f): return Fr(2) ** f[0] * Fr(3) ** f[1]

# ---- Lemma 2.1 ----
u = (A, B)
N_l, N_r = mul(u, third), mul(u, comb(two, third))
E_l, E_r = mul(u, comb(three, half)), mul(u, half)
R_l, R_r = mul(u, two), mul(u, three)
for p in (N_l, E_l, R_l): assert sp.simplify(colour(p) - sp.Mod(A - B + 1, 3)) == 0
for p in (N_r, E_r, R_r): assert sp.simplify(colour(p) - sp.Mod(A - B + 2, 3)) == 0
checks.append("2.1 left endpoints have colour j+1, right endpoints colour j+2")
eq(mul(u, comb(half, three)), E_l, "2.1 T(u/2) minus u = E(u)")
eq(mul(u, comb(third, two)), N_r, "2.1 T(u/3) minus u = N(u)")
eq(mul(mul(u, half), two), u, "2.1 left owner l/2 via R")
eq(mul(mul(u, comb(two, third)), comb(three, half)), u, "2.1 left owner 2l/3 via E")
eq(mul(mul(u, three), third), u, "2.1 left owner 3l via N")
eq(mul(mul(u, third), three), u, "2.1 right owner v/3 via R")
eq(mul(mul(u, comb(three, half)), comb(two, third)), u, "2.1 right owner 3v/2 via N")
eq(mul(mul(u, two), half), u, "2.1 right owner 2v via E")
# ---- multiplier relations ----
eq(comb(two, three), comb(g, q), "6 = gq"); eq(comb(g, g, q), (3, 0), "8 = g^2 q"); eq(comb(g, q, q), (0, 3), "27 = g q^2")
M = sp.Matrix([[2, -1], [-1, 2]]); assert M.det() == 3; checks.append("(U) exponent map determinant 3")
# ---- Lemma 5.1 ----
eq(mul(N_l, half), mul(u, inv(comb(g, q))), "5.1 R-owner of u/3 is u/6")
eq(mul(N_l, comb(two, third)), mul(u, inv(q)), "5.1 E-owner of u/3 is 2u/9")
eq(mul(N_r, two), mul(u, g), "5.1 E-owner of 2u/3 is 4u/3")
eq(mul(mul(u, g), comb(three, half)), R_l, "5.1 E(4u/3) left endpoint = 2u")
eq(mul(E_r, third), mul(u, inv(comb(g, q))), "5.1 R-owner of u/2 is u/6")
eq(mul(E_r, comb(three, half)), mul(u, inv(g)), "5.1 N-owner of u/2 is 3u/4")
eq(mul(E_l, half), mul(u, inv(g)), "5.1 R-owner of 3u/2 is 3u/4")
eq(mul(E_l, three), mul(u, q), "5.1 N-owner of 3u/2 is 9u/2")
eq(mul(mul(u, q), comb(two, third)), R_r, "5.1 N(9u/2) right endpoint = 3u")
# ---- Lemma 5.2 (x = (A,0)) ----
x = (A, 0)
def X(m_, n_): return mul(x, comb(pw(g, m_), pw(q, n_)))
un = X(0, n)
eq(mul(un, inv(comb(two, three))), X(-1, n - 1), "5.2 u_n/6 = x g^-1 q^(n-1)")
eq(mul(un, comb(three, half, half)), X(-1, n), "5.2 3u_n/4 = x g^-1 q^n")
eq(mul(mul(un, comb(three, half)), three), X(0, n + 1), "5.2 N-owner of L_n is u_{n+1}")
eq(mul(X(0, n + 1), comb(two, third)), mul(un, three), "5.2 N(u_{n+1}) right endpoint = 3u_n")
An = mul(un, two)
eq(mul(An, comb(two, third)), X(1, n), "5.2 E-owner of A_n is g u_n")
eq(mul(An, three), X(1, n + 1), "5.2 N-owner of A_n is g u_{n+1}")
assert sp.simplify(X(1, 0)[1] + 1) == 0; checks.append("5.2 g u_0 has b = -1")
eq(mul(X(1, n), third), mul(X(0, n - 1), two), "5.2 g u_n / 3 = 2 u_{n-1}")
beta = mul(X(1, n), comb(two, third))
eq(mul(beta, third), X(1, n - 1), "5.2 R-owner of beta_n is g u_{n-1}")
eq(mul(beta, comb(three, half)), X(1, n), "5.2 N-owner of beta_n is g u_n")
eq(mul(beta, two), X(2, n), "5.2 E-owner of beta_n is g^2 u_n")
eq(mul(X(2, n), comb(three, half)), mul(X(1, n), two), "5.2 E(g^2 u_n) left endpoint = 2 g u_n")
eq(mul(X(1, n), three), mul(X(1, n + 1), comb(two, third)), "5.2 3 g u_n = beta_{n+1}")
Bn = mul(X(1, n), two)
eq(mul(Bn, comb(two, third)), X(2, n), "5.2 E-owner of B_n is g^2 u_n"); eq(mul(Bn, three), X(2, n + 1), "5.2 N-owner of B_n is g^2 u_{n+1}")
eq(mul(X(2, k), comb(two, third)), mul(X(2, k - 1), three), "5.2 gamma_k = 2w_k/3 = 3w_{k-1}")
gk = mul(X(2, k - 1), three)
eq(mul(gk, comb(three, half)), X(2, k), "5.2 N-owner of gamma_k is w_k"); eq(mul(gk, two), X(3, k), "5.2 E-owner of gamma_k is g w_k")
eq(mul(X(2, n), third), mul(X(1, n - 1), two), "5.2 w_n/3 = B_{n-1}")
gam = mul(X(2, n), comb(two, third))
eq(mul(gam, third), X(2, n - 1), "5.2 R-owner of gamma_n is w_{n-1}"); eq(mul(gam, two), X(3, n), "5.2 E-owner of gamma_n is g^3 u_n")
eq(mul(X(3, n), comb(three, half)), mul(X(2, n), two), "5.2 E(g^3 u_n) left endpoint = 2w_n")
eq(mul(X(2, n), three), mul(X(2, n + 1), comb(two, third)), "5.2 3w_n = gamma_{n+1}")
Cn = mul(X(2, n), two)
eq(mul(Cn, comb(two, third)), X(3, n), "5.2 E-owner of C_n is g^3 u_n"); eq(mul(Cn, three), X(3, n + 1), "5.2 N-owner of C_n is g^3 u_{n+1}")
assert sp.simplify(X(3, 1)[1] + 1) == 0; checks.append("5.2 g^3 u_1 has b = -1")
eq(X(2, 1), (A + 3, 0), "5.2 w_1 = 8x is horizontal")
for nm, p, e in [("L", mul(un, comb(three, half)), -1), ("A", An, 0), ("B", Bn, 1), ("C", Cn, 2)]:
    assert coords(mul(x, two), p) == (e, n), nm
checks.append("5.2 selected L,A,B,C = 2x g^e q^n with e = -1,0,1,2 (distinct)")
assert val(pw(g, 2)) * Fr(2, 3) == Fr(32, 27) > 1; checks.append("5.2 g^2 u_k > 32t/27 > t")
assert 1 / val(q) == Fr(2, 9) and 1 / val(g) == Fr(3, 4); checks.append("5.2 u_n <= u_k/q <= 2t/9; u_k <= 3t/4")
assert val(comb(g, g, inv(q))) == Fr(32, 81) and Fr(32, 81) * Fr(3, 4) == Fr(8, 27) < Fr(1, 3); checks.append("5.2 w_{k-1} <= 8t/27 < t/3")
# ---- Lemma 3.2 patch ----
e0 = (A, 0)
eq(mul(e0, q), (A - 1, 2), "3.2 9e/2 = (A-1,2)"); eq(mul(e0, comb(g, q)), (A + 1, 1), "3.2 6e = (A+1,1)")
p2, p3 = mul(e0, q), mul(e0, comb(g, q))
eq(mul(p2, third), mul(e0, comb(three, half)), "3.2 N(9e/2) left = 3e/2"); eq(mul(p2, comb(two, third)), mul(e0, three), "3.2 N(9e/2) right = 3e")
eq(mul(p3, third), mul(e0, two), "3.2 N(6e) left = 2e"); eq(mul(p3, comb(two, third)), mul(e0, (2, 0)), "3.2 N(6e) right = 4e")
assert val(comb(q, three, half)) == Fr(27, 4) and val(comb(q, three)) == Fr(27, 2) and val(comb(g, q, three, half)) == 9 and val(comb(g, q, three)) == 18
checks.append("3.2 absent edges of 9e/2, 6e need 27e/4, 27e/2, 9e, 18e <= t")
assert Fr(27, 4) < 8 and 4 * Fr(1, 6) == Fr(2, 3); checks.append("3.1 patch => largest dyadic 4e <= 2t/3")
# ---- Case (I) ----
xI, yI = (2 * r + s, 0), (0, r + 2 * s)
def XI(m_, n_): return mul(xI, comb(pw(g, m_), pw(q, n_)))
eq(XI(-r, s), yI, "6.1 y = x g^-r q^s")
vi = mul(yI, pw(g, i)); eq(vi, XI(i - r, s), "6.6 v_i = x g^(i-r) q^s")
assert coords(xI, mul(vi, inv(comb(g, q)))) == (i - r - 1, s - 1) and coords(xI, mul(vi, inv(q))) == (i - r, s - 1)
checks.append("6.6 other owners of v_i/3 have m < 0 and n < s for i < r")
uI = XI(0, n)
assert coords(xI, mul(uI, inv(comb(g, q)))) == (-1, n - 1) and coords(xI, mul(uI, inv(g))) == (-1, n)
checks.append("6.6 other owners of u_n/2 have m = -1 and n' <= n < s")
z = XI(0, s); eq(z, mul(yI, pw(g, r)), "6.6 z = u_s = y g^r"); eq(z, (2 * r, 2 * s), "6.6 z = 2^(2r) 3^(2s)")
eq(mul(yI, q), (-1, r + 2 * s + 2), "6.6 q v_0 = 9y/2 has a = -1")
eq(mul(mul(vi, comb(two, third)), two), mul(yI, pw(g, i + 1)), "6.6 E-owner of 2v_i/3 is v_{i+1}")
eq(mul(mul(vi, comb(two, third)), third), mul(vi, inv(q)), "6.6 R-owner of 2v_i/3 is v_i/q")
eq(mul(mul(vi, three), comb(three, half)), mul(vi, q), "6.6 N-owner of 3v_i is q v_i")
eq(mul(mul(vi, three), two), mul(mul(yI, pw(g, i + 1)), q), "6.6 E-owner of 3v_i is q v_{i+1}")
assert val(comb(q, two, third)) == 3; checks.append("6.6 q v <= t gives 3v <= 2t/3")
eq(mul(mul(z, g), comb(three, half)), mul(z, two), "6.6 E(gz) left endpoint = 2z")
eq(mul(mul(z, g), half), mul(XI(0, s - 1), three), "6.6 E(gz) right endpoint = 3u_{s-1}")
eq(mul(mul(z, q), third), mul(mul(yI, pw(g, r - 1)), two), "6.6 N(qz) left endpoint = 2v_{r-1}")
eq(mul(mul(z, q), comb(two, third)), mul(z, three), "6.6 N(qz) right endpoint = 3z")
eq(mul(mul(z, two), comb(two, third)), mul(z, g), "6.6 E-owner of 2z is gz"); eq(mul(mul(z, two), three), mul(z, comb(g, q)), "6.6 N-owner of 2z is 6z")
eq(mul(mul(z, three), comb(three, half)), mul(z, q), "6.6 N-owner of 3z is qz"); eq(mul(mul(z, three), two), mul(z, comb(g, q)), "6.6 E-owner of 3z is 6z")
assert coords(xI, mul(mul(yI, pw(g, i)), q)) == (i - r, s + 1); checks.append("6.6 q v_i has q-coordinate s+1, so H and V meet only in z")
assert val(pw(g, 2)) < 2 < val(pw(g, 3)); checks.append("6.6 g^r < 2 implies r <= 2")
assert val(g) * Fr(2, 9) * Fr(2, 3) == Fr(16, 81) and val(pw(g, 2)) * Fr(2, 9) * Fr(2, 3) == Fr(64, 243) < Fr(1, 3)
checks.append("6.7 g u_n <= 16t/81, g^2 u_n <= 64t/243 < t/3")
eq(mul(X(2, s - 1), three), mul(X(2, s), comb(two, third)), "6.7 gamma_s = 3 g^2 u_{s-1}")
assert val(pw(g, 2)) / 3 == Fr(16, 27) and val(pw(g, 4)) / 3 > 1; checks.append("6.8 r=2: z > 16t/27 and g^2 z > t")
assert val(g) / 3 == Fr(4, 9) > Fr(1, 3); checks.append("6.8 r=1: z = gy > 4t/9 > t/3")
for S_ in range(1, 8):
    zz = 4 * 9 ** S_
    assert zz == 2 ** 2 * 3 ** (2 * S_) and Fr(16, 9) * zz == 64 * 9 ** (S_ - 1)
checks.append("6.8 r=1: z = 4*9^s and g^2 z = 64*9^(s-1)")
assert (2 ** 5, 3 ** 4, 2 ** 4 * 3 ** 2) == (32, 81, 144) and Fr(3, 2) * 144 == 216 and Fr(3, 2) * 36 == 54 and 2 * 36 == 72
checks.append("6.8 window endpoints 54, 72, 216")
# ---- augmentations ----
for name, kf, edges in [("P1: right endpoints on a+2b", lambda p: p[0] + 2 * p[1], [comb(two, third), half, three]),
                        ("P2/P4: left endpoints on 2a+b", lambda p: 2 * p[0] + p[1], [third, comb(three, half), two])]:
    p = (a_, b_)
    assert [sp.expand(kf(mul(p, f)) - kf(p)) for f in edges] == [-1, -1, 2], name
    checks.append(name + " lie on k-1, k-1, k+2 (N, E, R)")
assert sp.simplify(sp.Mod((a_ - b_) - (a_ + 2 * b_), 3)) == 0 and sp.simplify(sp.Mod((a_ - b_) + (2 * a_ + b_), 3)) == 0
checks.append("colour = (a+2b) = -(2a+b) mod 3")
yB = (0, B); vB = mul(yB, pw(g, i))
eq(mul(vB, comb(two, third)), (2 * i + 1, B - i - 1), "P1 frontier 2v_i/3 = (2i+1, B-i-1)")
assert sp.expand((2 * i + 1) + 2 * (B - i - 1)) == 2 * B - 1; checks.append("P1 frontier lies on a+2b = 2B-1")
assert coords(yB, mul(vB, inv(comb(g, q))))[1] == -1 and coords(yB, mul(vB, inv(q)))[1] == -1; checks.append("P1 other owners of v_i/3 have y-q-coordinate -1")
eq(mul(XI(0, n), comb(three, half)), (2 * r + s - n - 1, 2 * n + 1), "P2/P4 frontier 3u_n/2 = (A-n-1, 2n+1)")
assert sp.expand(2 * (2 * r + s - n - 1) + 2 * n + 1) == 2 * (2 * r + s) - 1; checks.append("P2/P4 frontier lies on 2a+b = 2A-1")
f = lambda kk: kk // 2 + 1 if kk >= 0 else 0
for AA in range(0, 500):
    assert sum(f(2 * AA - 3 * m) - f(2 * AA - 3 * m - 1) for m in range(1, AA + 2)) == AA // 3
checks.append("(6.2) diagonal count = floor(A/3) for A < 500 (text gives the general proof)")
# P4 with r = 1: k0 = 2(s+2), y = 3^(2s+1) on k0-3, second point 2y/9 = z/6
assert sp.expand(2 * 0 + (2 * s + 1) - (2 * (s + 2) - 3)) == 0; checks.append("6.9 y lies on k0-3")
assert Fr(2, 9) == Fr(4, 3) / 6; checks.append("6.9 2y/9 = z/6 (z = 4y/3)")
assert Fr(2, 3) / 6 == Fr(1, 9) < Fr(4, 27); checks.append("6.9 added owners <= t/9 < 4t/27")
print(len(checks), "symbolic/exact checks passed")
for c in checks: print(" -", c)
