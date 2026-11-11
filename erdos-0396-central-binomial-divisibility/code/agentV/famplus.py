"""Family '+' machinery: n = M0*B^L + (k+1),  n-i = j'(A_{j'}^{m_{j'}} + 1),  j' = k+1-i.
Used by stress.py (task 3) and search.py (task 5)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from functools import lru_cache
from math import prod
from poly import cyclo
from lemC import piece_report, divisors
from verify396 import is_prime, factor, carries, vp


def ev(coeffs, x):
    r = 0
    for c in reversed(coeffs):
        r = r * x + c
    return r


def phi_poly(n2, x):
    return ev(cyclo(n2), x)


@lru_cache(None)
def predicted_levels(m, d):
    "asymptotic carry levels t=s+1 of piece Phi_{2d}(x) in j'(x^m+1) (Laurent-sign rule of NOTES/lemC)"
    good, res = piece_report(m, d)
    return frozenset(s + 1 for s, sg in res if sg and sg[1] < 0)


def actual_levels(n, q):
    out, t, pt = set(), 1, q
    while pt <= 2 * n:
        if 2 * (n % pt) >= pt: out.add(t)
        t += 1; pt *= q
    return frozenset(out)


def family(k, ms, extra=0):
    """ms[j'-1] = m_{j'} (odd, pairwise coprime).  Returns (M0, L, c) with M/j' = (c[j'] B^(L/m_{j'}))^{m_{j'}}.
    e_p = least exponent >= max v_p(j') (+extra) solving e_p = v_p(j) mod m_j for all j."""
    L = prod(ms); M0 = 1; e = {}
    for p in [p for p in range(2, k + 2) if is_prime(p)]:
        lo = max(vp(j, p) for j in range(1, k + 2)) + extra
        ep = next(x for x in range(lo, lo + L + 1) if all((x - vp(j, p)) % ms[j - 1] == 0 for j in range(1, k + 2)))
        e[p] = ep; M0 *= p ** ep
    c = {j: prod(p ** ((e[p] - vp(j, p)) // ms[j - 1]) for p in e) for j in range(1, k + 2)}
    for j in c:
        assert c[j] ** ms[j - 1] * j == M0, (j, c[j])
    return M0, L, c, e


def pieces(k, ms, c, L, B):
    "list over i of (j', A, [(d, Phi_{2d}(A))])"
    out = []
    for i in range(k + 1):
        j = k + 1 - i; m = ms[j - 1]; A = c[j] * B ** (L // m)
        out.append((j, A, [(d, phi_poly(2 * d, A)) for d in divisors(m)]))
    return out
