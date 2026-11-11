# Bulk test: saddle-point predictor (saddle.py) vs FFT coefficients of Q^2 (peak.py) for many n.
# Usage: python bulk_saddle.py q b1,b2,.. m
import sys, cmath, numpy as np
from peak import run
from saddle import predict
q = int(sys.argv[1]); bs = [int(x) for x in sys.argv[2].split(',')]; m = int(sys.argv[3])
c, loc, shift = run(m, q, nsample=500)
D = len(c) and None
from core2 import phi
D = m - phi(m)
ns = np.unique(np.linspace(D // 50, 2 * D - D // 50, 400).astype(int))
cmax = np.max(np.abs(c.real))
agree = tot = 0; errs = []
for n in ns:
    if abs(c[n].real) < 1e-8 * cmax: continue
    val = sum(cmath.exp(i[2] - shift) for i in predict(m, q, bs, 2, int(n)))
    tot += 1; agree += (val.real > 0) == (c[n].real > 0)
    errs.append(abs(val.real - c[n].real) / abs(c[n].real))
print(f"saddle vs FFT over {tot} bulk n: sign agreement {agree}/{tot}, median rel err {np.median(errs):.2e}, 90% {np.quantile(errs, 0.9):.2e}")
