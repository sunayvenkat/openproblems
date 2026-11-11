# Independent verification of the two conditional theorems (Dickson => E_1, E_2 infinite).
from math import comb
from sympy import isprime, factorint, symbols, expand

def leg(n, p):                 # nu_p(C(2n,n)) by Legendre, independent of quad4.carries_exact
    s, q = 0, p
    while q <= 2*n:
        s += 2*n//q - 2*(n//q); q *= p
    return s

def in_Ek(n, k):
    f = {}
    for i in range(k + 1):
        for p, e in factorint(n - i).items(): f[p] = f.get(p, 0) + e
    return all(leg(n, p) >= e for p, e in f.items())

def digit_carries(n, P):       # carries of n+n in base P (P need not be prime)
    c = k = 0
    while n:
        c = 1 if 2*(n % P) + c >= P else 0; k += c; n //= P
    return k

x = symbols('x')
# ---------- Theorem A: E_1 ----------
F = [14*x+3, 24*x+17, 24*x+5, 7*x+5]
assert expand(F[0]*F[1] - 2*F[2]*F[3]) == 1
bad = [t for t in range(9, 10**5, 2*1) if t % 2 == 0 and
       min(digit_carries((14*t+3)*(24*t+17), P) for P in (14*t+3, 24*t+17, 24*t+5, 7*t+5)) < 1]
print("A: even x in [9,1e5) violating a digit inequality:", bad)
hits = fails = 0; first = []
for t in range(0, 10**6, 2):
    P = [14*t+3, 24*t+17, 24*t+5, 7*t+5]
    if not all(isprime(p) for p in P): continue
    n = P[0]*P[1]
    ok = in_Ek(n, 1)
    if t >= 9:
        hits += ok; fails += (not ok)
    if ok and len(first) < 3: first.append((t, n))
print("A: x<1e6 with 4 primes (x>=9): in E_1 =", hits, " not in E_1 =", fails, " first:", first)
t, n = first[0]
print("A: direct C(2n,n) mod n(n-1) for n =", n, ":", comb(2*n, n) % (n*(n-1)))

# ---------- Theorem B: E_2, x = 42y+9 ----------
G0 = [70*x+31, 252*x+113, 84*x+37, 315*x+142, 180*x+79, 42*x+19]
Q = 52920*x**2 + 47166*x + 10509
assert expand(Q - 3*G0[0]*G0[1]) == 0 and expand(Q - 1 - 2*G0[2]*G0[3]) == 0 \
   and expand(Q - 2 - 7*G0[4]*G0[5]) == 0
G = [expand(g.subs(x, 42*x + 9)) for g in G0]
print("B: forms in y:", G)
for l in (2, 3, 5, 7, 11, 13):
    assert any(all(int(g.subs(x, r)) % l for g in G) for r in range(l)), l
lam = [ [int(c) for c in (g.coeff(x, 1), g.coeff(x, 0))] for g in G]
def vals(y): return [a*y + b for a, b in lam]
# small primes: 3 | n with base-3 digit 2 at position 1; 7 | n-2 with base-7 digit >= 4 at position 1
for y in range(0, 2000):
    v = vals(y); n = 3*v[0]*v[1]
    assert (n // 3) % 3 == 2 and ((n - 2) // 7) % 7 >= 4 and n % 2 == 1
    if y >= 1:
        assert min(digit_carries(n, P) for P in v) >= 1, y
print("B: congruence + digit conditions hold for all y in [1,2000)")
hits = fails = 0; first = []
for y in range(1, 3*10**5):
    v = vals(y)
    if not all(isprime(p) for p in v): continue
    n = 3*v[0]*v[1]
    ok = in_Ek(n, 2); hits += ok; fails += (not ok)
    if ok and len(first) < 3: first.append((y, n))
print("B: y<3e5 with 6 primes: in E_2 =", hits, " not =", fails, " first:", first)
