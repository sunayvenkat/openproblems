# E_1 from 4 linear forms: n = Q(x) = c0*L1*L2, n-1 = c1*L3*L4, {c0,c1} = {1,2}.
# Q and Q-1 both split over Q  <=>  disc(Q) = u^2 and disc(Q)+4A = v^2.
# Large-prime carry conditions are checked at huge x (they are eventually constant in x);
# then actual prime quadruples are found and n(n-1) | C(2n,n) is verified by Kummer.
from math import gcd, isqrt
from sympy import isprime

def carries_exact(n, p):      # nu_p(C(2n,n)) = number of carries of n+n in base p
    c = k = 0
    while n:
        s = 2 * (n % p) + c
        c = 1 if s >= p else 0
        k += c
        n //= p
    return k

def split(A, B, C):
    """A x^2+Bx+C = cont*(a1 x+b1)(a2 x+b2) over Z, or None."""
    D = B * B - 4 * A * C
    r = isqrt(D)
    if r * r != D or D == 0:
        return None
    g = gcd(gcd(A, B), C)
    A1, B1, C1 = A // g, B // g, C // g
    # roots (-B1 +- r/g)/(2A1); r divisible by g? disc of primitive part = D/g^2
    D1 = B1 * B1 - 4 * A1 * C1
    r1 = isqrt(D1)
    if r1 * r1 != D1:
        return None
    out = []
    for s in (1, -1):
        num, den = -B1 + s * r1, 2 * A1     # root = num/den, form den'*x - num'
        h = gcd(num, den)
        a, b = den // h, -num // h
        if a < 0:
            a, b = -a, -b
        out.append((a, b))
    (a1, b1), (a2, b2) = out
    assert a1 * a2 == A1 and a1 * b2 + a2 * b1 == B1 and b1 * b2 == C1
    return g, (a1, b1), (a2, b2)

def val(f, x):
    return f[0] * x + f[1]

def good_large(c0, F0, c1, F1):
    """carry condition at every form-prime, tested at several huge x"""
    for x in (10**60 + 7, 10**61 + 13, 3 * 10**59 + 1):
        n = c0 * val(F0[0], x) * val(F0[1], x)
        for N, (c, F) in ((n, (c0, F0)), (n - 1, (c1, F1))):
            for f in F:
                P = val(f, x)
                if carries_exact(n, P) < 1:
                    return False
    return True

def admissible(forms):
    for l in (2, 3, 5, 7):
        if not any(all(val(f, x) % l for f in forms) for x in range(l)):
            return False
    return True

def search(Amax=120):
    found = []
    for A in range(1, Amax + 1):
        for d in range(1, isqrt(4 * A) + 1):          # (v-u)(v+u)=4A
            if (4 * A) % d:
                continue
            e = 4 * A // d
            if (d + e) % 2:
                continue
            v, u = (d + e) // 2, (e - d) // 2
            if u <= 0:
                continue
            for B in range(0, 2 * A):
                if (B * B - u * u) % (4 * A):
                    continue
                C = (B * B - u * u) // (4 * A)
                s0, s1 = split(A, B, C), split(A, B, C - 1)
                if not s0 or not s1:
                    continue
                c0, f1, f2 = s0
                c1, f3, f4 = s1
                if sorted((c0, c1)) != [1, 2]:
                    continue
                forms = [f1, f2, f3, f4]
                if not admissible(forms):
                    continue
                if good_large(c0, (f1, f2), c1, (f3, f4)):
                    found.append((A, B, C, c0, f1, f2, c1, f3, f4))
    return found

def verify(sol, X=200000, want=3):
    A, B, C, c0, f1, f2, c1, f3, f4 = sol
    ex = []
    for x in range(1, X):
        vs = [val(f, x) for f in (f1, f2, f3, f4)]
        if min(vs) < 5 or not all(isprime(v) for v in vs):
            continue
        n = A * x * x + B * x + C
        assert n == c0 * vs[0] * vs[1] and n - 1 == c1 * vs[2] * vs[3]
        # full Kummer check: every prime power of n(n-1) divides C(2n,n)
        ok = carries_exact(n, 2) >= 1  # nu_2(n(n-1)) = 1
        ok &= all(carries_exact(n, p) >= 1 for p in vs)
        if ok:
            ex.append((x, n))
            if len(ex) >= want:
                break
        else:
            return ("FAIL", x, n)
    return ex

if __name__ == "__main__":
    sols = search()
    print(len(sols), "families with A <= 120")
    for s in sols[:12]:
        print(s, verify(s))
