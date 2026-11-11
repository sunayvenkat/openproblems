# Independent check of agent g5's Theorems A and B: n(n-1)...(n-k) | C(2n, n), tested prime by prime
# with Kummer (nu_q C(2n,n) = number of carries of n+n in base q) on sympy factorizations.
from sympy import isprime, factorint
from sympy.abc import x
from sympy import expand

def carries(n, q):
    c = k = 0
    while n:
        d = n % q; k = (2 * d + k) // q; c += k; n //= q
    return c

def in_E(n, k):
    need = {}
    for i in range(k + 1):
        for q, e in factorint(n - i).items(): need[q] = need.get(q, 0) + e
    return all(carries(n, q) >= e for q, e in need.items())

# identities
A = [14*x+3, 24*x+17, 24*x+5, 7*x+5]
assert expand(A[0]*A[1] - 2*A[2]*A[3]) == 1
X = 42*x + 9
B = [3*(70*X+31)*(252*X+113), 2*(84*X+37)*(315*X+142), 7*(180*X+79)*(42*X+19)]
assert expand(B[0] - B[1]) == 1 and expand(B[0] - B[2]) == 2

hits = bad = 0
for t in range(9, 20000):
    P = [f.subs(x, t) for f in A]
    if all(isprime(int(p)) for p in P):
        n = int(P[0] * P[1]); hits += 1
        if not in_E(n, 1): bad += 1; print('A FAIL', t, n)
print('Theorem A: x in [9, 20000): four-prime x =', hits, ' failures =', bad)

hits = bad = 0
lin = [70*X+31, 252*X+113, 84*X+37, 315*X+142, 180*X+79, 42*X+19]
for t in range(1, 300000):
    if all(isprime(int(f.subs(x, t))) for f in lin):
        n = int(B[0].subs(x, t)); hits += 1
        ok = in_E(n, 2); bad += not ok
        print('B y =', t, 'n =', n, 'E_2' if ok else 'FAIL')
        if hits == 3: break
print('Theorem B: six-prime y found =', hits, ' failures =', bad)
