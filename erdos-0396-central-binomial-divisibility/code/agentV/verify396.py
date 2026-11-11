"""Exact verifier for Erdos #396:  prod_{i=0}^{k} (n-i) | C(2n,n) ?

For every prime p dividing some n-i, checks  sum_i v_p(n-i) <= v_p(C(2n,n)),
where v_p(C(2n,n)) = #carries of n+n in base p (Kummer).  Each prime is
cross-checked with Legendre: v_p((2n)!(n-k-1)!/(n!)^3) = (3s(n)-s(2n)-s(n-k-1)-(k+1))/(p-1).

usage:  python verify396.py n k            (factors each n-i itself: trial div + Pollard-Brent)
        python verify396.py n k --facs JSON  (JSON: list over i=0..k of {"p": e}; fast path)
"""
import sys, json, random
from math import gcd, isqrt

SMALL = [p for p in range(2, 10000) if all(p % q for q in range(2, isqrt(p) + 1))]
MR_BASES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]  # deterministic below 3.3e24


def is_prime(n):
    if n < 2:
        return False
    for p in SMALL[:50]:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    # shortcut: above 3.3e24 the fixed bases + 8 random ones make this a probable-prime test
    bases = MR_BASES if n < 3317044064679887385961981 else MR_BASES + [random.randrange(2, n - 1) for _ in range(8)]
    for a in bases:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def brent(n):
    "a nontrivial factor of composite odd n (Pollard rho, Brent's cycle + batched gcd)"
    while True:
        y, c, m = random.randrange(1, n), random.randrange(1, n), 128
        g = r = q = 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = (y * y + c) % n
                    q = q * abs(x - y) % n
                g = gcd(q, n); k += m
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n
                g = gcd(abs(x - ys), n)
        if g != n:
            return g


def factor(n, out=None):
    "dict prime->exponent of n >= 1"
    out = {} if out is None else out
    for p in SMALL:
        if p * p > n:
            break
        while n % p == 0:
            out[p] = out.get(p, 0) + 1; n //= p
    stack = [n] if n > 1 else []
    while stack:
        m = stack.pop()
        if is_prime(m):
            out[m] = out.get(m, 0) + 1
        else:
            r = isqrt(m)
            if r * r == m:
                stack += [r, r]
            else:
                d = brent(m); stack += [d, m // d]
    return out


def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p; v += 1
    return v


def carries(n, p):
    "v_p(C(2n,n)) = #{t>=1 : n mod p^t >= p^t/2}"
    c, pt = 0, p
    while pt <= 2 * n:
        c += 2 * (n % pt) >= pt
        pt *= p
    return c


def digsum(n, p):
    s = 0
    while n:
        s += n % p; n //= p
    return s


def verify(n, k, facs=None):
    """returns (ok, rows) ; rows = [(p, need, have)] for every prime dividing prod(n-i).
    facs: optional list (i=0..k) of {prime: exp}; validated (product + primality)."""
    assert n > k >= 0
    if facs is None:
        facs = [factor(n - i) for i in range(k + 1)]
    else:
        facs = [{int(p): int(e) for p, e in f.items()} for f in facs]
        for i, f in enumerate(facs):
            prod = 1
            for p, e in f.items():
                assert is_prime(p), f"supplied factor {p} of n-{i} is not prime"
                prod *= p ** e
            assert prod == n - i, f"supplied factorisation of n-{i} has product {prod}"
    rows = []
    for p in sorted(set().union(*facs)):
        need = sum(vp(n - i, p) for i in range(k + 1))
        have = carries(n, p)
        leg = (3 * digsum(n, p) - digsum(2 * n, p) - digsum(n - k - 1, p) - (k + 1))
        assert leg % (p - 1) == 0 and leg // (p - 1) == have - need, ("Legendre cross-check failed", p)
        rows.append((p, need, have))
    return all(nd <= hv for _, nd, hv in rows), rows


def _selftest():
    from math import comb
    random.seed(1)
    for n in range(2, 400):
        for k in range(0, 4):
            if n > k:
                P = 1
                for i in range(k + 1):
                    P *= n - i
                assert verify(n, k)[0] == (comb(2 * n, n) % P == 0), (n, k)
    for a in range(2, 200000):
        assert is_prime(a) == all(a % d for d in range(2, isqrt(a) + 1)), a
    for a in (561, 41041, 3215031751, 3825123056546413051, 318665857834031151167461):
        assert not is_prime(a), a  # strong pseudoprimes to several small bases
    for _ in range(300):
        a = random.randrange(2, 10**18)
        f = factor(a); P = 1
        for p, e in f.items():
            assert is_prime(p); P *= p ** e
        assert P == a
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        _selftest(); sys.exit()
    n, k = int(sys.argv[1]), int(sys.argv[2])
    facs = json.loads(sys.argv[sys.argv.index("--facs") + 1]) if "--facs" in sys.argv else None
    ok, rows = verify(n, k, facs)
    for p, nd, hv in rows:
        print(f"  p={p}: sum v_p(n-i)={nd}  carries={hv}  {'ok' if nd <= hv else 'FAIL'}")
    print(f"n={n} k={k}: {'IN E_k' if ok else 'NOT in E_k'}")
