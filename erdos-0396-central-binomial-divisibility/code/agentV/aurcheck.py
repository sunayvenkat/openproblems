"""Claim (1): Aurifeuillean pieces q = F(+-y) of N = x^123 + 1, x = 123 y^2.
(a) exact Z[x] decomposition N/F(+-y)^t = P1(x) -+ 123 y P2(x) + T_t, T_t = (R1(x) -+ 123 y R2(x))/Phi_246(x)^t,
    using 1/F(+-y) = F(-+y)/Phi_246(x) and F(+-y) = C(x) +- 123 y D(x);  sign of T_t as y -> +inf;
(b) direct carry test 2*(N mod q^t) >= q^t at random y (any residue mod 123, odd and even)."""
import sys, os, pickle, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from poly import cyclo, mul, add, sub, divmod_monic
F, C, D = pickle.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aur123.pkl'), 'rb'))
m = 123
Phi = list(cyclo(2 * m))
N = [1] + [0] * (m - 1) + [1]                      # x^123 + 1 in x
ev = lambda a, z: sum(c * z**i for i, c in enumerate(a))
# identity checks
assert all(F[2*i] == C[i] * 123**i for i in range(len(C))) and all(F[2*i+1] == D[i] * 123**(i+1) for i in range(len(D)))
def mulpair(a, b):
    "(U1 + w V1)(U2 + w V2), w = 123 y, w^2 = 123^2 y^2 = 123 x"
    U = add(mul(a[0], b[0]), [123 * v for v in mul([0, 1], mul(a[1], b[1]))] if a[1] and b[1] else [])
    V = add(mul(a[0], b[1]) if b[1] else [], mul(a[1], b[0]) if a[1] else [])
    return U, V
Fp = (C, D); Fm = (C, [-v for v in D])
res = {}
for sgn, name, conj in ((1, 'F(+y)', Fm), (-1, 'F(-y)', Fp)):
    for t in (2, 3):
        W = ([1], [])
        for _ in range(t): W = mulpair(W, conj)
        Pht = [1]
        for _ in range(t): Pht = mul(Pht, Phi)
        P1, R1 = divmod_monic(mul(N, W[0]), Pht)
        P2, R2 = divmod_monic(mul(N, W[1]), Pht) if W[1] else ([], [])
        # T = (R1(x) + 123 y R2(x)) / Phi^t ; degrees in y: 2*deg R1, 2*deg R2 + 1 ; denominator 160 t
        d1 = 2 * (len(R1) - 1) if R1 else -1; d2 = 2 * (len(R2) - 1) + 1 if R2 else -1
        lead = (R1[-1] if d1 > d2 else 123 * R2[-1])
        sign = 1 if lead > 0 else -1
        res[(name, t)] = sign
        print(f"{name} t={t}: tail ~ y^{max(d1, d2) - 160 * t} (-> 0: {max(d1, d2) < 160 * t}), sign {'NEG => carry' if sign < 0 else 'POS => no carry'}")
# (b) direct check at random y
random.seed(123)
bad = 0; tot = 0
for _ in range(60):
    y = random.randrange(10**40, 10**41) if _ % 2 else random.randrange(10**80, 10**81)
    if _ % 3 == 0: y = y - y % 123 + random.randrange(1, 123)      # force y not divisible by 123
    x = 123 * y * y; Nn = x**m + 1
    for sgn, name in ((1, 'F(+y)'), (-1, 'F(-y)')):
        q = ev(F, sgn * y)
        assert Nn % q == 0
        for t in (2, 3):
            carry = 2 * (Nn % q**t) >= q**t
            tot += 1; bad += carry != (res[(name, t)] < 0)
print(f"direct test at {tot} (y, piece, t) with y ~ 1e40..1e81 (1/3 of them y mod 123 != 0): mismatches = {bad}")
