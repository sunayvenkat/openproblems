# Baseline: fraction of random n near size N in E1 / E2.
import random, sys
from sympy import factorint
from verify import carries
def ok(n, k):
    f = {}
    for i in range(k+1):
        for p, e in factorint(n-i).items(): f[p] = f.get(p, 0)+e
    return all(carries(n, p) >= e for p, e in f.items())
random.seed(1); N = int(float(sys.argv[1])); S = int(sys.argv[2])
ns = [random.randrange(N, 2*N) for _ in range(S)]
print('N', N, 'E1', sum(ok(n,1) for n in ns)/S, 'E2', sum(ok(n,2) for n in ns)/S)
