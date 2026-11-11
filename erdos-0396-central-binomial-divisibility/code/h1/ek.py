# Generic: n-i = lam_i * prod(a x + b). Count x<=X with prod_{i<=k}(n-i) | C(2n,n) (Kummer).
import sys
from verify import carries
def sieve(L):
    spf = list(range(L+1))
    for i in range(2, int(L**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, L+1, i):
                if spf[j] == j: spf[j] = i
    return spf
def fac(m, spf, f):
    m = abs(m)
    while m > 1:
        p = spf[m]; m //= p; f[p] = f.get(p, 0)+1
def run(spec, X, x0=1):
    L = max(abs(a)*X+abs(b) for lam, fs in spec for a, b in fs)+1
    spf = sieve(L); good = tot = 0
    for x in range(x0, X+1):
        vals = [[a*x+b for a, b in fs] for lam, fs in spec]
        if min(v for vs in vals for v in vs) <= 0: continue
        n = spec[0][0]
        for v in vals[0]: n *= v
        f = {}
        for i, ((lam, fs), vs) in enumerate(zip(spec, vals)):
            m = lam
            for v in vs: m *= v
            assert m == n-i, (x, i)
            fac(lam, spf, f)
            for v in vs: fac(v, spf, f)
        tot += 1
        good += all(carries(n, q) >= e for q, e in f.items())
    return good, tot
if __name__ == '__main__':
    X = int(sys.argv[1])
    E2 = [(1, [(14,-1),(15,-1)]), (1, [(1,0),(210,-29)]), (1, [(6,-1),(35,1)])]
    for X_ in [X//10, X]:
        g, t = run(E2, X_); print('E2 best', X_, g, t, '%.4f' % (g/t))
