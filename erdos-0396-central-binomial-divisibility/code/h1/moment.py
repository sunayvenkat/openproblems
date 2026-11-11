# First moment: mean number of bad (prime) events per x, bucketed by theta = log q / log x.
import sys, math
from collections import Counter
from verify import carries
from ek import sieve, fac
def run(spec, X, x0, cls=None):
    L = max(abs(a)*X+abs(b) for lam, fs in spec for a, b in fs)+1
    spf = sieve(L); tot = good = 0; bad = Counter()
    for x in range(x0, X+1):
        if cls and x % cls[0] != cls[1]: continue
        n = spec[0][0]
        for a, b in spec[0][1]: n *= a*x+b
        f = {}
        for i, (lam, fs) in enumerate(spec):
            fac(lam, spf, f)
            for a, b in fs: fac(a*x+b, spf, f)
        tot += 1; nb = 0
        for q, e in f.items():
            if carries(n, q) < e:
                nb += 1; th = math.log(q)/math.log(x)
                bad['q=2' if q == 2 else 'small' if q < 50 else 'th<.5' if th < .5 else 'th<.67' if th < 2/3 else 'th>=.67'] += 1
        good += nb == 0
    return good/tot, {k: round(v/tot, 4) for k, v in bad.items()}, round(sum(bad.values())/tot, 4)
if __name__ == '__main__':
    X = int(sys.argv[1])
    E1 = [(1, [(12,-1),(22,9)]), (2, [(11,-1),(12,5)])]
    E1A = [(1, [(14,3),(24,17)]), (2, [(7,5),(24,5)])]
    E2 = [(1, [(14,-1),(15,-1)]), (1, [(1,0),(210,-29)]), (1, [(6,-1),(35,1)])]
    for name, s in [('E1best', E1), ('E1thmA', E1A), ('E2best', E2)]:
        print(name, run(s, X, X//2))
