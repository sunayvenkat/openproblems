# Top-piece checks for a few large m (only feasible levels). Usage: python bigm.py m [levels...]
import sys, time
from core import phi, factor, mu
from topscan import top_levels
from fastser import cyclo_pow_series_fast
m = int(sys.argv[1]); ph = phi(m); T = m // ph
levels = [int(a) for a in sys.argv[2:]] or list(range(1, T))
print('m', m, sorted(factor(m)), 'mu', mu(m), 'phi/m=%.4f' % (ph / m), 'T', T, 'rho0', m - T * ph, flush=True)
for s in levels:
    t0 = time.time(); E = m - (s + 1) * ph
    e = cyclo_pow_series_fast(m, -(s + 1), E + 40)
    vals = [(N - E, e[N] if N % 2 == 0 else -e[N]) for N in range(E + 1, E + 41)]
    first = next(((i, v) for i, v in vals if v), None)
    print(' level', s, 'window start E+1 =', E + 1, 'first nonzero (offset, c_N) =', first,
          '-> carry' if first and first[1] < 0 else '-> no carry', '(%.0fs)' % (time.time() - t0), flush=True)
