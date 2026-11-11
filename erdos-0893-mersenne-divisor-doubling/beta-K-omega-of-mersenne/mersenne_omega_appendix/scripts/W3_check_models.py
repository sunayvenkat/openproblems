# Sanity checks for barrier.md: (1) the axiom system Sigma_{D,J} holds for TRUE factorizations
# (small p), (2) explicit fake models (single-prime and many-prime) satisfy Sigma_{D,J} for a range of p.
# Illustrative finite computation only; the theorems are proved in barrier.md.
import math, random, sys
random.seed(1)
SMALLP = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def is_prime(n):
    if n < 2: return False
    for q in SMALLP:
        if n % q == 0: return n == q
    d, s = n-1, 0
    while d % 2 == 0: d //= 2; s += 1
    # bases 2..41 deterministic below 3.3e24; above that probabilistic (sanity check only)
    for a in [2,3,5,7,11,13,17,19,23,29,31,37,41] + [random.randrange(2, n-1) for _ in range(8)]:
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def rho(n):
    if n % 2 == 0: return 2
    while True:
        y, c, m = random.randrange(1, n), random.randrange(1, n), 128
        g, r, q = 1, 1, 1
        while g == 1:
            x = y
            for _ in range(r): y = (y*y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r-k)):
                    y = (y*y + c) % n; q = q*abs(x-y) % n
                g = math.gcd(q, n); k += m
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys*ys + c) % n; g = math.gcd(abs(x-ys), n)
        if g != n: return g

def factor(n, out):
    if n == 1: return
    if is_prime(n): out.append(n); return
    d = rho(n); factor(d, out); factor(n//d, out)

def primes_upto(n):
    s = bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]

def prod(L):
    r = 1
    for x in L: r *= x
    return r

def depth_ok(q, n, D):
    # for d<=D with d | q-1:  [2^{(q-1)/d} == 1 mod q]  <=>  [d | (q-1)/n]
    for d in range(1, D+1):
        if (q-1) % d == 0:
            if (pow(2, (q-1)//d, q) == 1) != (((q-1)//n) % d == 0): return False
    return True

def check(p, F, G, D, J):
    """Return list of violated axiom labels for (F(p),G(p))."""
    bad = []
    M = 2**p - 1; Phi = (2**p + 1)//3; W = 8*p**J
    if prod(F).bit_length() != M.bit_length(): bad.append('A1F')
    if prod(G).bit_length() != Phi.bit_length(): bad.append('A1G')
    if any(not is_prime(q) for q in F+G): bad.append('prime')
    if any(q % (2*p) != 1 for q in F+G): bad.append('A2')
    if any(q % 8 not in (1, 7) for q in F): bad.append('A3F')
    for q in G:
        m = (q-1)//(2*p)
        if q % 8 != (1 if m % 2 == 0 else 3): bad.append('A3G')
    if prod(F) % W != M % W: bad.append('A4F')
    if prod(G) % W != Phi % W: bad.append('A4G')
    if any(not depth_ok(q, p, D) for q in F): bad.append('A5F')
    if any(not depth_ok(q, 2*p, D) for q in G): bad.append('A5G')
    if set(F) & set(G) or not F or not G: bad.append('A6')
    return bad

D, J = 12, 3
print("== Part 1: Sigma_{D,J} on TRUE factorizations (D=%d, J=%d) ==" % (D, J))
for p in primes_upto(89)[2:]:
    F, G = [], []
    factor(2**p - 1, F); factor((2**p + 1)//3, G)
    b = check(p, sorted(F), sorted(G), D, J)
    # Mod-24 obstruction check: some q|M_p has q = 1 mod 3 or q = 1 mod 8
    obs = any(q % 3 == 1 or q % 8 == 1 for q in F)
    print(p, "omega(M_p)=%d tau(Phi)=%d" % (len(set(F)), 2**len(G) if len(set(G)) == len(G) else -1),
          "violations:", b, "mod24-witness:", obs)
    assert not b and obs

# ---- fake models ----
used = set()
P_D = prod([l for l in primes_upto(D) if l >= 3])

def admissible_prime_in(lo, hi, residue_mod_W, W, rng_tries=200000):
    """Prime q in [lo,hi) with q = residue mod W, q = 2 mod l for odd l<=D, avoiding used."""
    # CRT: modulus W*P_D (W = 8 p^J coprime to P_D for p > D)
    a, m = residue_mod_W % W, W
    for l in primes_upto(D):
        if l < 3: continue
        t = ((2 - a) * pow(m, -1, l)) % l
        a, m = a + m*t, m*l
    start = lo + ((a - lo) % m)
    q = start
    while q < hi:
        if q not in used and is_prime(q): return q
        q += m
    return None

def fake_model(p, r):
    """r small F-primes (r even) in class 7 mod 8, 1 mod 2p, 2 mod l (3<=l<=D) + filler; G single prime."""
    M = 2**p - 1; Phi = (2**p + 1)//3; W = 8*p**J
    small = []
    # small class: q = 1 mod 2p, 7 mod 8, 2 mod l; modulus 8p*P_D
    # CRT for q=1 mod p, q=7 mod 8
    a = next(x for x in range(1, 8*p) if x % p == 1 and x % 8 == 7); m = 8*p
    for l in primes_upto(D):
        if l < 3: continue
        t = ((2 - a) * pow(m, -1, l)) % l
        a, m = a + m*t, m*l
    q = a
    while len(small) < r:
        if q not in used and is_prime(q): small.append(q)
        q += m
    R = prod(small)
    lo, hi = -(-2**(p-1)//R), -(-2**p//R)
    filler = admissible_prime_in(lo, hi, (M * pow(R, -1, W)) % W, W)
    F = small + [filler]
    Q = admissible_prime_in(2**(p-2), 2**(p-1), Phi % W, W)
    used.update(F); used.add(Q)
    return F, [Q]

D, J = 6, 2
P_D = prod([l for l in primes_upto(D) if l >= 3])
print("== Part 2: fake models (r=0: beta=0 type; r>0: many primes) ==")
for p in [q for q in primes_upto(260) if q > 40]:
    for r in (0, 2*(p//60)):
        F, G = fake_model(p, r)
        b = check(p, F, G, D, J)
        print(p, "r=%d omega(F)=%d |G|=1 smallest F=%d violations:%s" % (r, len(set(F)), min(F), b))
        assert not b
print("all checks passed")
