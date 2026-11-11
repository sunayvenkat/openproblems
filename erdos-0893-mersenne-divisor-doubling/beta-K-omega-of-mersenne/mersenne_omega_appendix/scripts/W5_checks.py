"""Sanity checks for W5 obstruction lemmas. Run: python checks.py"""
import random, math
from math import gcd, log

# ---------- integer factoring ----------
def is_prime(n):
    if n < 2: return False
    for s in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % s == 0: return n == s
    d, r = n-1, 0
    while d % 2 == 0: d//=2; r+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def rho(n):
    if n % 2 == 0: return 2
    while True:
        y, c, m = random.randrange(1,n), random.randrange(1,n), 128
        g, r, q = 1, 1, 1
        while g == 1:
            x = y
            for _ in range(r): y = (y*y+c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r-k)):
                    y = (y*y+c) % n; q = q*abs(x-y) % n
                g = gcd(q, n); k += m
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys*ys+c) % n; g = gcd(abs(x-ys), n)
        if g != n: return g

def factor(n, out):
    if n == 1: return
    if is_prime(n): out[n] = out.get(n,0)+1; return
    d = rho(n); factor(d,out); factor(n//d,out)

DATA = {3:1,5:1,7:1,11:2,13:1,17:1,19:1,23:2,29:3,31:1,37:2,41:2,43:3,47:3,53:3,59:2,61:1,67:2,71:3,73:3,79:3,83:2,89:1,97:2,101:2,103:2,107:1,109:2,113:5,127:1}

def check_integers():
    worst = 0
    for p, w in DATA.items():
        M = 2**p-1; f = {}; factor(M, f)
        assert len(f) == w, (p, f)
        for q, v in f.items():
            assert pow(2,p,q) == 1 and (q-1) % (2*p) == 0 or p == 3
            # v_q(M_p) = v_q(2^{q-1}-1): check mod q^{v+1}
            assert pow(2,q-1,q**(v+1)) != 1 and pow(2,q-1,q**v) == 1
        S = sum(log(q)/(q-1) for q in f)
        worst = max(worst, S)
        # Lemma R: P(n,2^n) == P(n,2^r) mod q^v, random P
        for _ in range(3):
            a = [[random.randrange(-9,10) for j in range(4)] for i in range(4)]
            P = lambda x, y: sum(a[i][j]*x**i*y**j for i in range(4) for j in range(4))
            r, k = random.randrange(p), random.randrange(1,6); n = r+p*k
            for q, v in f.items():
                assert (P(n, pow(2,n)) - P(n, 2**r)) % q**v == 0
    print("integers ok; max sum log q/(q-1) =", round(worst,4), " (log2)/2 =", round(log(2)/2,4))

def check_mahler():
    # Delta^s g(0) == 0 mod M^{max(0,s-L1)}, g(k)=P(r+nk, 2^{r+nk}); n prime OR composite
    for n in (7, 11, 12, 30):
        M = 2**n-1
        for _ in range(5):
            L1, L2 = 2, 3
            a = [[random.randrange(-9,10) for j in range(L2+1)] for i in range(L1+1)]
            r = random.randrange(n)
            g = [sum(a[i][j]*(r+n*k)**i*2**(j*(r+n*k)) for i in range(L1+1) for j in range(L2+1)) for k in range(9)]
            for s in range(9):
                D = sum((-1)**(s-t)*math.comb(s,t)*g[t] for t in range(s+1))
                assert D % M**max(0, s-L1) == 0
    print("mahler ok (prime and composite n)")

# ---------- polynomials over F_l (lists, low degree first) ----------
def trim(f):
    while f and f[-1] == 0: f.pop()
    return f
def pmod(f, g, l):
    f = f[:]; inv = pow(g[-1], l-2, l)
    while len(trim(f)) >= len(g):
        c = f[-1]*inv % l; s = len(f)-len(g)
        for i, gi in enumerate(g): f[s+i] = (f[s+i]-c*gi) % l
    return f
def pmul(f, g, l):
    h = [0]*(len(f)+len(g)-1) if f and g else []
    for i, fi in enumerate(f):
        for j, gj in enumerate(g): h[i+j] = (h[i+j]+fi*gj) % l
    return trim(h)
def pgcd(f, g, l):
    f, g = trim(f[:]), trim(g[:])
    while g: f, g = g, trim(pmod(f, g, l))
    return f
def psub(f, g, l):
    n = max(len(f), len(g)); f = f+[0]*(n-len(f)); g = g+[0]*(n-len(g))
    return trim([(x-y) % l for x, y in zip(f, g)])
def ppow(f, e, m, l):
    r, b = [1], pmod(f, m, l)
    while e:
        if e & 1: r = pmod(pmul(r, b, l), m, l)
        b = pmod(pmul(b, b, l), m, l); e >>= 1
    return r
def omega_poly(F, l):
    """number of distinct monic irreducible factors of F over F_l"""
    F = trim(F[:]); N = {}; tot = 0
    x = [0,1]; X = x
    for k in range(1, len(F)):
        X = ppow(X, l, F, l)              # T^{l^k} mod F
        G = pgcd(F, psub(X, x, l), l)
        dk = len(G)-1 - sum(j*N[j] for j in N if k % j == 0)
        assert dk % k == 0
        N[k] = dk//k; tot += N[k]
    return tot
def ordmod(l, p):
    k, x = 1, l % p
    while x != 1: x = x*l % p; k += 1
    return k

def check_ff():
    random.seed(1); cnt = 0
    for l in (3, 5, 7):
        for p in (3, 5, 7, 11, 13):
            if p == l: continue
            f = ordmod(l, p)
            for d in (1, 2, 3):
                for _ in range(3):
                    a = [random.randrange(l) for _ in range(d)] + [1]
                    one = [1]
                    ap = ppow(a, p, [0]*(d*p+1)+[1], l) if False else None
                    A = [1]
                    for _ in range(p): A = pmul(A, a, l)
                    wm = omega_poly(psub(A, one, l), l)
                    wp = omega_poly(psub(A, [l-1], l), l)  # a^p + 1
                    assert wm <= d*(1+(p-1)//f), (l,p,d,a,wm,f)
                    assert wp >= (p-1)//f, (l,p,d,a,wp,f)
                    if a == [0,1]: assert wm == 1+(p-1)//f
                    cnt += 1
    print("function-field bounds ok on", cnt, "cases")

if __name__ == "__main__":
    random.seed(0)
    check_integers(); check_mahler(); check_ff()
