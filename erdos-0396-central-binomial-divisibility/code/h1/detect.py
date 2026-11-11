# Rigorous-side first moment: mean # of "detectable bad" events per x (top: rule fails & coin3 tails; medium: coins s=2..L-1 tails).
# Also checks rule == coin2 in top regime.
import random, math, sys
from sympy import factorint
from search2 import frac_fail
def coins(n, q):  # list of parities of floor(2n/q^s), s=1.. while >0
    out = []; t = 2*n
    while True:
        t //= q
        if t == 0: break
        out.append(t & 1)
    return out
def rule_ok(a, b, lam, kappa, q):
    u = pow(q, -2, a) if a > 1 else 0
    r = (-lam*kappa*b*u) % a; lk = lam*kappa
    return 2*r > a or (2*r == a and lk > 0) or (r == 0 and lk < 0)
def stats(spec, X, S, z0=50, seed=5):
    random.seed(seed); det = act = 0; agree = tot_top = 0; perform = [0]*sum(len(F) for _, F in spec)
    for _ in range(S):
        x = random.randrange(X//2, X); n = spec[0][0]
        for a, b in spec[0][1]: n *= a*x+b
        allf = [(lam, a, b, a*x+b) for lam, F in spec for a, b in F]
        j = 0
        for lam, F in spec:
            for idx, (a, b) in enumerate(F):
                (ap, bp) = F[1-idx]; kappa = a*bp - ap*b; P = a*x+b
                for q, e in factorint(P).items():
                    if q <= z0 or e > 1 or any(v % q == 0 for l_, a_, b_, v in allf if v != P): continue
                    c = P//q; cs = coins(n, q); L = len(cs)
                    assert cs[0] == 0
                    if L == 1:  # q^2 > 2n: no carry possible, always bad
                        act += 1; det += 1; perform[j] += 1; continue
                    if 2*abs(kappa)*c < q:  # top regime
                        tot_top += 1; ok = rule_ok(a, b, lam, kappa, q); agree += (ok == bool(cs[1]))
                        bad = not any(cs[1:]); act += bad; det += bad; perform[j] += bad
                    else:
                        bad_act = not any(cs[1:]); bad_det = not any(cs[1:L-1]) if L >= 4 else bad_act
                        act += bad_act; det += bad_det; perform[j] += bad_det
                j += 1
    return dict(X=X, det=round(det/S, 3), act=round(act/S, 3), rule_agree='%d/%d' % (agree, tot_top), perform=[round(p/S, 3) for p in perform])
E1 = [(1, [(12,-1),(22,9)]), (2, [(11,-1),(12,5)])]
E2 = [(1, [(14,-1),(15,-1)]), (1, [(1,0),(210,-29)]), (1, [(6,-1),(35,1)])]
S = int(sys.argv[1])
for e in [9, 12, 15]:
    print('E1', stats(E1, 10**e, S)); print('E2', stats(E2, 10**e, S))
