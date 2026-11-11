# For q | P_j with log q/log x > 0.7: empirical bad rate per form vs frac_fail prediction. Also M_inf model.
import random, math
from sympy import factorint
from verify import carries
from search2 import frac_fail
def model(spec):
    m = sum(2**(1-k)*math.log(1+1/k) for k in range(4, 200))
    fs = []
    for i, (lam, F) in enumerate(spec):
        if len(F) != 2: raise ValueError
        for j in range(2):
            (a, b), (ap, bp) = F[j], F[1-j]; fs.append(frac_fail(a, b, ap, bp, lam))
    return fs, sum(fs)*(math.log(1.5)+0.5*math.log(4/3)) + len(fs)*m, m
def check(spec, X, S):
    random.seed(2); ev = [[0, 0] for _ in range(2*len(spec))]
    for _ in range(S):
        x = random.randrange(X//2, X); n = spec[0][0]
        for a, b in spec[0][1]: n *= a*x+b
        k = 0
        for i, (lam, F) in enumerate(spec):
            for (a, b) in F:
                for q, e in factorint(a*x+b).items():
                    if math.log(q)/math.log(x) > 0.7 and e == 1:
                        ev[k][0] += 1; ev[k][1] += carries(n, q) < 1
                k += 1
    return [round(b/t, 3) if t else None for t, b in ev]
E1 = [(1, [(12,-1),(22,9)]), (2, [(11,-1),(12,5)])]
E1A = [(1, [(14,3),(24,17)]), (2, [(7,5),(24,5)])]
E2 = [(1, [(14,-1),(15,-1)]), (1, [(1,0),(210,-29)]), (1, [(6,-1),(35,1)])]
for nm, s in [('E1', E1), ('E1A', E1A), ('E2', E2)]:
    fs, M, m = model(s)
    print(nm, 'pred fs', [round(f, 3) for f in fs], 'M_inf %.4f' % M, 'm %.4f' % m)
    print('   empirical bad rate (X=1e15, theta>.7):', check(s, 10**15, 3000))
