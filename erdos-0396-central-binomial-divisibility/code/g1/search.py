# Search P-rough odd squarefree m <= Y with T = 2 (2 <= m/phi(m) < 3) and small rho = m - 2 phi(m).
# DFS over body primes in increasing order; the last prime q is solved for: rho = 2 phi(n) - q (2 phi(n) - n).
#   python search.py P log10Y X [mode]   mode 'all' (every m with rho <= X) or 'best' (record min rho)
import sys, bisect
from math import log
from sympy import primerange, isprime

def run(P, Y, X, mode='all', pmax=10 ** 5):
    pr = list(primerange(P + 1, pmax))
    Lp = [0.0]; Lr = [0.0]
    for p in pr: Lp.append(Lp[-1] + log(p)); Lr.append(Lr[-1] + log(p / (p - 1)))
    found, best, nodes = [], [None], [0]

    def reach(j, logB):        # upper bound for log of the ratio gain from primes pr[j:] with product <= B
        k = bisect.bisect_right(Lp, Lp[j] + logB) - 1
        return Lr[min(k + 1, len(pr))] - Lr[j]

    def finals(n, f, lastp, ps):
        d = 2 * f - n
        qhi = min((2 * f - 1) // d, Y // n)
        qlo = max(lastp + 1, -(-(2 * f - X) // d)) if mode == 'all' else lastp + 1
        q = qhi if qhi % 2 else qhi - 1
        tries = 0
        while q >= qlo and tries < 10 ** 5:
            if isprime(q):
                m = n * q; rho = 2 * f - q * d
                if mode == 'all': found.append((m, rho, ps + [q]))
                else:
                    if best[0] is None or rho / (f * (q - 1)) < best[0][0]: best[0] = (rho / (f * (q - 1)), m, rho, ps + [q])
                    return
            q -= 2; tries += 1

    def dfs(j, n, f, ps):
        nodes[0] += 1
        lr = log(n / f)
        d = 2 * f - n
        if ps and d > 0: finals(n, f, ps[-1], ps)
        for k in range(j, len(pr)):
            q = pr[k]
            if n * q > Y: break
            n2, f2 = n * q, f * (q - 1)
            if 2 * f2 - n2 <= 0:          # ratio >= 2 at q: handled by finals (q <= q*); larger q keep ratio < 2
                continue
            # still below 2: need to reach 2 with primes > q within budget
            if log(n2 / f2) + reach(k + 1, log(Y / n2)) < log(2): break
            dfs(k + 1, n2, f2, ps + [q])

    dfs(0, 1, 1, [])
    return found, best[0], nodes[0]

if __name__ == '__main__':
    P, ly, X = int(sys.argv[1]), float(sys.argv[2]), int(float(sys.argv[3]))
    mode = sys.argv[4] if len(sys.argv) > 4 else 'all'
    found, best, nodes = run(P, int(10 ** ly), X, mode)
    print(f'P={P} Y=1e{ly} X={X} mode={mode}: nodes {nodes}')
    if mode == 'all':
        found.sort(key=lambda t: t[1])
        print(f'  {len(found)} m with 1 <= rho <= X; omega odd: {sum(len(t[2]) % 2 for t in found)}')
        for m, rho, ps in found[:40]: print(f'  rho={rho} m={m} omega={len(ps)} primes={ps}')
    else:
        print('  best (rho/phi, m, rho, primes):', best)
