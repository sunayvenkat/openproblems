# Top piece d=m scan over odd squarefree m with phi(m)/m < 1/2.
# Level s (1<=s<=T-1, T=m//phi): first nonzero c_N, N in (m-(s+1)phi, m-phi], c_N=(-1)^N [u^N]Phi_m(u)^{-(s+1)}.
# Output per m: T, rho0=m-T*phi, mu(m), per-level (offset i=N-E, sign of c_N).
import sys
from core import factor, phi, mu
from fastser import cyclo_pow_series_fast

def top_levels(m, only_last=False):
    ph = phi(m); T = m // ph; out = []
    levels = [T - 1] if only_last else range(1, T)
    for s in levels:
        E = m - (s + 1) * ph; hi = m - ph
        width = 64; res = None
        while res is None and E + 1 <= hi:
            Nmax = min(E + width, hi)
            e = cyclo_pow_series_fast(m, -(s + 1), Nmax)
            for N in range(E + 1, Nmax + 1):
                if e[N]:
                    v = e[N] if N % 2 == 0 else -e[N]
                    res = (N - E, 1 if v > 0 else -1, v); break
            if Nmax == hi: break
            width *= 4
        out.append((s, res))
    return T, out

def odd_sqfree_candidates(Mmax):
    for m in range(105, Mmax + 1, 2):
        f = factor(m)
        if any(e > 1 for e in f.values()): continue
        if 2 * phi(m) < m: yield m, sorted(f)

if __name__ == '__main__':
    Mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    tot = good = 0
    for m, ps in odd_sqfree_candidates(Mmax):
        T, lv = top_levels(m)
        g = any(r and r[1] < 0 for _, r in lv)
        tot += 1; good += g
        ph = phi(m)
        print(m, ps, 'mu', mu(m), 'T', T, 'rho0', m - T * ph, 'top', 'good' if g else 'BAD', lv, flush=True)
    print('total', tot, 'good', good)
