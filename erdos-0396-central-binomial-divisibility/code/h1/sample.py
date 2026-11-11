# Random x in [X/2, X]: good fraction and first moment (mean # bad primes), via sympy factorint.
import random, sys
from sympy import factorint
from verify import carries
def stats(spec, X, S, seed=1):
    random.seed(seed); good = nbad = 0
    for _ in range(S):
        x = random.randrange(X//2, X)
        n = spec[0][0]
        for a, b in spec[0][1]: n *= a*x+b
        f = {}
        for lam, fs in spec:
            for m in [lam]+[a*x+b for a, b in fs]:
                for p, e in factorint(m).items(): f[p] = f.get(p, 0)+e
        nb = sum(carries(n, q) < e for q, e in f.items())
        nbad += nb; good += nb == 0
    return round(good/S, 3), round(nbad/S, 3)
E1 = [(1, [(12,-1),(22,9)]), (2, [(11,-1),(12,5)])]
E2 = [(1, [(14,-1),(15,-1)]), (1, [(1,0),(210,-29)]), (1, [(6,-1),(35,1)])]
S = int(sys.argv[1])
for e in [6, 9, 12, 15]:
    print('X=1e%d' % e, 'E1', stats(E1, 10**e, S), 'E2', stats(E2, 10**e, S))
