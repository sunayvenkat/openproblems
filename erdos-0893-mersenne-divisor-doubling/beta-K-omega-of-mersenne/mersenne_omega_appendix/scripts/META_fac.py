"""Factoring toolkit: BPSW primality, Pollard-Brent rho, ECM (Montgomery, Suyama), stage 2."""
import math, random

SMALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def sieve(n):
    b = bytearray([1]) * (n + 1); b[0:2] = b'\x00\x00'
    for i in range(2, int(n ** .5) + 1):
        if b[i]: b[i*i::i] = bytearray(len(range(i*i, n+1, i)))
    return [i for i in range(n + 1) if b[i]]

PR = sieve(1 << 20)

def mr(n, a):
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    x = pow(a, d, n)
    if x in (1, n - 1): return True
    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1: return True
    return False

def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def strong_lucas(n):
    D = 5
    while True:
        j = jacobi(D, n)
        if j == -1: break
        if j == 0 and abs(D) != n: return False
        D = -D - 2 if D > 0 else -D + 2
    P, Q = 1, (1 - D) // 4
    d, s = n + 1, 0
    while d % 2 == 0: d //= 2; s += 1
    # compute U_d, V_d via binary method
    U, V, Qk = 0, 2, 1  # U_0, V_0, Q^0
    inv2 = (n + 1) // 2
    for bit in bin(d)[2:]:
        U, V = U * V % n, (V * V - 2 * Qk) % n
        Qk = Qk * Qk % n
        if bit == '1':
            U, V = (P * U + V) * inv2 % n, (D * U + P * V) * inv2 % n
            Qk = Qk * Q % n
    if U == 0 or V == 0: return True
    for _ in range(s - 1):
        V = (V * V - 2 * Qk) % n; Qk = Qk * Qk % n
        if V == 0: return True
    return False

def is_prime(n):
    """Deterministic for n < 3.3e24 (MR first 12 prime bases); BPSW otherwise (PRP)."""
    if n < 2: return False
    for p in SMALL:
        if n % p == 0: return n == p
    if not all(mr(n, a) for a in SMALL): return False
    if n < 3317044064679887385961981: return True
    return strong_lucas(n)

def rho(n, iters=200000):
    if n % 2 == 0: return 2
    for c in range(1, 6):
        y, r, q, g = random.randrange(n), 1, 1, 1
        f = lambda x: (x * x + c) % n
        x = ys = y; done = 0
        while g == 1 and done < iters:
            x = y
            for _ in range(r): y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(128, r - k)):
                    y = f(y); q = q * abs(x - y) % n
                g = math.gcd(q, n); k += 128
            r *= 2; done += r
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys); g = math.gcd(abs(x - ys), n)
        if 1 < g < n: return g
    return None

# ---------- ECM (Montgomery XZ) ----------
def xdbl(X, Z, a24, n):
    s = (X + Z); s = s * s; d = (X - Z); d = d * d
    t = s - d
    return s * d % n, t * (d + a24 * t) % n

def xadd(X1, Z1, X2, Z2, Xd, Zd, n):
    u = (X1 - Z1) * (X2 + Z2); v = (X1 + Z1) * (X2 - Z2)
    a = u + v; b = u - v
    return Zd * a * a % n, Xd * b * b % n

def ladder(k, X, Z, a24, n):
    R0, R1 = (X, Z), xdbl(X, Z, a24, n)
    for bit in bin(k)[3:]:
        if bit == '1':
            R0 = xadd(*R0, *R1, X, Z, n); R1 = xdbl(*R1, a24, n)
        else:
            R1 = xadd(*R0, *R1, X, Z, n); R0 = xdbl(*R0, a24, n)
    return R0

def ecm_curve(n, B1, B2, sigma):
    u = (sigma * sigma - 5) % n; v = 4 * sigma % n
    X = pow(u, 3, n); Z = pow(v, 3, n)
    den = 16 * X * v % n  # 4 u^3 v * 4
    g = math.gcd(den, n)
    if g != 1: return g if g < n else None
    a24 = pow(v - u, 3, n) * (3 * u + v) % n * pow(den, -1, n) % n
    # stage 1: multiply by product of prime powers <= B1 in chunks
    k = 1
    for p in PR:
        if p > B1: break
        pp = p
        while pp * p <= B1: pp *= p
        k *= pp
        if k.bit_length() > 4000:
            X, Z = ladder(k, X, Z, a24, n); k = 1
    if k > 1: X, Z = ladder(k, X, Z, a24, n)
    g = math.gcd(Z, n)
    if 1 < g < n: return g
    if g == n: return None
    # stage 2: standard continuation with differences of consecutive primes
    D = 2310
    # precompute multiples j*Q for even j up to max gap (use table of 2..2*maxgap)
    Q = (X, Z)
    Q2 = xdbl(X, Z, a24, n)
    table = {1: Q, 2: Q2}
    # baby steps: odd j < D coprime to D: j*Q
    baby = {}
    prev, cur = Q, ladder(3, X, Z, a24, n) if True else None
    baby[1] = Q
    Pj = {1: Q, 3: cur}
    j = 3
    while j + 2 < D // 2 + 2:
        nxt = xadd(*Pj[j], *Q2, *Pj[j - 2], n)
        Pj[j + 2] = nxt; j += 2
    babyj = [j for j in range(1, D // 2, 2) if math.gcd(j, D) == 1]
    bx = {j: (Pj[j][0], Pj[j][1]) for j in babyj}
    # normalize baby x-coords: store X*Zinv not needed; use cross-product trick
    DQ = ladder(D, X, Z, a24, n)
    m = (B1 // D) | 0
    if m < 1: m = 1
    R = ladder(m * D, X, Z, a24, n)
    Rprev = ladder((m - 1) * D, X, Z, a24, n) if m > 1 else Q  # placeholder
    if m == 1:
        Rprev = Q  # unused difference fix below
        # (m-1)*D = 0 -> handle by computing 2D directly next
    acc = 1
    primes_set = None
    while m * D - D // 2 <= B2:
        for j in babyj:
            Xb, Zb = bx[j]
            acc = acc * ((R[0] * Zb - Xb * R[1]) % n) % n
        g = math.gcd(acc, n)
        if 1 < g < n: return g
        if g == n: return None
        # next R = R + DQ with difference Rprev
        if m == 1:
            Rn = xdbl(*DQ, a24, n)
        else:
            Rn = xadd(*R, *DQ, *Rprev, n)
        Rprev, R = R, Rn; m += 1
    g = math.gcd(acc, n)
    return g if 1 < g < n else None

def ecm(n, B1=2000, B2=None, curves=50, seed=None):
    if B2 is None: B2 = 100 * B1
    rnd = random.Random(seed)
    for _ in range(curves):
        g = ecm_curve(n, B1, B2, rnd.randrange(6, 1 << 62))
        if g: return g
    return None

SCHED = [(2000, 25), (11000, 90), (50000, 300), (250000, 700), (1000000, 1800)]

def factor(n, trial=None, sched=SCHED, budget_level=5, log=None):
    """Return (dict prime->exp, list of unfactored composites)."""
    fs, left = {}, []
    for p in (trial or PR[:2000]):
        if p * p > n: break
        while n % p == 0: fs[p] = fs.get(p, 0) + 1; n //= p
    stack = [n] if n > 1 else []
    while stack:
        m = stack.pop()
        if m == 1: continue
        if is_prime(m): fs[m] = fs.get(m, 0) + 1; continue
        r = math.isqrt(m)
        if r * r == m: stack += [r, r]; continue
        g = rho(m, 100000) if m.bit_length() < 140 else None
        if not g:
            for lvl, (B1, c) in enumerate(sched[:budget_level]):
                g = ecm(m, B1, 100 * B1, c)
                if g: break
        if g: stack += [g, m // g]
        else: left.append(m)
    return fs, left

if __name__ == '__main__':
    # self-check
    assert [x for x in range(200) if is_prime(x)] == [x for x in PR if x < 200]
    assert is_prime(2**127 - 1) and not is_prime(2**128 + 1)
    assert not is_prime(3215031751) and not is_prime(3825123056546413051)
    n = (2**67 - 1)
    f, l = factor(n); assert f == {193707721: 1, 761838257287: 1}, f
    p1, p2 = 1000000000000000003, 1000000000000000009
    g = ecm(p1 * 1000003, 2000, 200000, 50); assert g in (1000003, p1), g
    print('ok')
