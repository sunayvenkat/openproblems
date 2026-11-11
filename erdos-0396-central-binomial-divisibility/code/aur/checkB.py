# Non-top pieces of x^m+1, d | m, d < m, via the binomial digit formula (agentAC Thm A1):
#   phi(d)/d > 2/3            -> good at level 2 (A1b);  d = 1 -> good (A1a)
#   1/2 < phi(d)/d <= 2/3     -> D_2 = -C(K,2) (g^2 mod f): good iff lc(g^2 mod f) > 0,
#       lc(g^2 mod f) = first nonzero [t^N](1+t^d)^2 Phi_{2d}(t)^{-3}, N > 2d - 3 phi(d)   (exact ints)
# Pieces failing level 2 are listed for a deeper check.
import sys
sys.path.insert(0, '../agentV')
from fastgood import series, pf, phi
from itertools import combinations

def divisors_sqfree(m):
    ps = pf(m); out = []
    for r in range(len(ps) + 1):
        for c in combinations(ps, r):
            d = 1
            for p in c: d *= p
            out.append(d)
    return sorted(out)

def lc_g2_mod_f(d):
    delta = phi(d); E = 2 * d - 3 * delta; W = 256
    while True:
        N = E + W
        c = series(2 * d, -3, N)
        for t in range(E + 1, N + 1):
            v = c[t] + (2 * c[t - d] if t >= d else 0) + (c[t - 2 * d] if t >= 2 * d else 0)
            if v: return t - E, v
        W *= 4

def check(m):
    todo = []
    for d in divisors_sqfree(m):
        if d == m: continue
        r = phi(d) / d
        if d == 1 or r > 2 / 3:
            continue
        if 2 * phi(d) <= d:   # formula D_2 = -C(K,2)(g^2 mod f) needs deg g < phi(d)
            print(f'  d={d} phi/d={r:.4f} <= 1/2: deeper check', flush=True); todo.append(d); continue
        off, v = lc_g2_mod_f(d)
        tag = 'good-L2' if v > 0 else 'L2-BAD'
        print(f'  d={d} {pf(d)} phi/d={r:.4f} K={m//d} offset={off} lc(g^2 mod f)~{v:.3e} {tag}', flush=True)
        if v < 0: todo.append(d)
    return todo

if __name__ == '__main__':
    for m in map(int, sys.argv[1:]):
        print('m =', m, pf(m), flush=True)
        print('  needs deeper check:', check(m), flush=True)
