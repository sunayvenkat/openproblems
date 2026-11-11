# Exact analysis of a polynomial family n(w) in Z[w] for E_k.
# Kummer: nu_P C(2n,n) = #{s>=1 : frac(n/P^s) >= 1/2}.  For a piece f | N = n-i, n = i + f*C, and for large w
# frac(n/f^(s+1)) -> frac(Q_s(w)) +- 0 where C = Q_s f^s + Rem_s (division in Q[w]); the sign of the
# infinitesimal is sign(lc Rem_s) (or + from i/f^(s+1) when Rem_s = 0).  Q_s(w) mod 1 is periodic in w.
import sympy as sp
from fractions import Fraction as Fr
from math import lcm, prod
from sympy import isprime, factorint, primerange
w = sp.Symbol('w')

def fr(c): c = sp.Rational(c); return Fr(int(c.p), int(c.q))

def shifts(n, k):
    """[(j_i, [(piece Poly, exponent)])] with pieces primitive, lc > 0."""
    out = []
    for i in range(k + 1):
        c, fl = sp.factor_list(sp.Poly(n - i, w))
        ps = []
        for f, e in fl:
            if f.LC() < 0: f = -f; c *= (-1) ** e
            ps.append((f, e))
        out.append((int(c), ps))
    return out

def carry_levels(f, C):
    """(L, list over r mod L of #levels s with an eventual carry) for base f, cofactor C."""
    d, levels = f.degree(), []
    for s in range(1, C.degree() // d + 1):
        Q, Rm = sp.div(C, f ** s)
        qc = [fr(c) for c in Q.all_coeffs()]
        sig = 1 if Rm.is_zero else (1 if Rm.LC() > 0 else -1)
        levels.append((qc, sig, lcm(*[c.denominator for c in qc])))
    L = lcm(1, *[l for _, _, l in levels])
    cnt = []
    for r in range(L):
        k = 0
        for qc, sig, _ in levels:
            th = sum(c * r ** e for e, c in enumerate(reversed(qc))) % 1
            k += th > Fr(1, 2) or (th == Fr(1, 2) and sig > 0) or (th == 0 and sig < 0)
        cnt.append(k)
    return L, cnt

def low_carries(m, p, R):
    return sum(2 * (m % p ** s) >= p ** s for s in range(1, R + 1))

def analyze(n, k, verbose=True):
    sh = shifts(n, k)
    D = sp.Poly(n, w).degree()
    pieces = [f for _, ps in sh for f, _ in ps]
    report, L, good = [], 1, None
    for i, (j, ps) in enumerate(sh):
        for f, e in ps:
            C, rem = sp.div(sp.Poly(n - i, w), f); assert rem.is_zero
            Lf, cnt = carry_levels(f, C)
            ok = [r for r in range(Lf) if cnt[r] >= e]
            report.append((i, j, f.as_expr(), e, Lf, len(ok)))
            if 2 * f.degree() > D or not ok: good = False
            L2 = lcm(L, Lf)
            prev = set(range(L)) if good is None else good
            good = {r for r in range(L2) if r % L in prev and r % Lf in ok} if good is not False else False
            L = L2
    global LAST; LAST = report
    if verbose:
        for row in report: print("  shift %d j=%d piece %s ^%d  classes mod %d good: %d" % row)
    if not good: return None
    # local primes
    js = [j for j, _ in sh]
    S = set(primerange(2, 2 * k + 1)) | {p for j in js for p in factorint(j)} | set(primerange(2, sum(f.degree() for f in pieces) + 1))
    loc, nP = {}, sp.Poly(n, w)
    for p in sorted(S):
        need = sum(factorint(j).get(p, 0) for j in js)
        R = need + (2 if p <= 5 else 1) if need else 1
        rs = [r for r in range(p ** R)
              if all(f.eval(r) % p for f in pieces) and low_carries(int(nP.eval(r)), p, R) >= need]
        loc[p] = (R, need, rs)
        if verbose: print("  p=%d need %d carries, mod p^%d: %d good residues" % (p, need, R, len(rs)))
        if not rs: LAST = ('local', p); return None
    return sh, L, sorted(good), loc

def crt_class(L, good, loc, pick=0):
    """one residue r mod M satisfying everything (L assumed coprime to the local moduli, else filtered)."""
    from sympy.ntheory.modular import crt
    mods, res = [], []
    for p, (R, need, rs) in loc.items():
        mods.append(p ** R); res.append(rs[pick % len(rs)])
    M0 = prod(mods); r0 = int(crt(mods, res)[0]) if mods else 0
    M = lcm(M0, L)
    for r in range(r0, M, M0):
        if r % L in good: return M, r
    return None

def legendre(n, p):
    s, q = 0, p
    while q <= 2 * n: s += 2 * n // q - 2 * (n // q); q *= p
    return s

def in_Ek_given(n, k, fac):
    """fac: dict prime->exponent claimed for prod(n-i); checks the product then Legendre for each prime."""
    assert prod(p ** e for p, e in fac.items()) == prod(n - i for i in range(k + 1))
    assert all(isprime(p) for p in fac)
    return all(legendre(n, p) >= e for p, e in fac.items())
