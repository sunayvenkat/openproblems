# Vectorized trace formula c(m) = -(2/m^2) sum_{a<=m/2,(a,m)=1} R_a^2 [(m+phi-1) cos th_a + S_a sin th_a]
# (verified against the series in trace_top.py). Measures concentration on the peak a = c*8^{-1} mod m
# for m with every prime = +-3 mod 8 (Peak lemma), via the reparametrization c = 8a mod m.
import sys, math, numpy as np
from sympy import divisors, totient, factorint
from sympy.functions.combinatorial.numbers import mobius
def terms(m):
    phi = int(totient(m)); a = np.arange(1, m // 2 + 1, dtype=np.int64)
    a = a[np.gcd(a, m) == 1]
    logR = np.zeros(len(a)); S = np.zeros(len(a))
    for d in divisors(m)[1:]:
        mu = int(mobius(d))
        if not mu: continue
        x = np.pi * (a % d) / d
        logR -= mu * np.log(2 * np.abs(np.sin(x))); S += mu * (m / d) / np.tan(x)
    th = 2 * np.pi * ((a * ((1 - phi) % m)) % m) / m
    return a, phi, logR, S, th
if __name__ == "__main__":
  for m in map(int, sys.argv[1:]):
      a, phi, logR, S, th = terms(m); L = logR.max()
      v = -2 * np.exp(2 * (logR - L)) * ((m + phi - 1) * np.cos(th) + S * np.sin(th))   # scaled by e^{2L}/m^2
      tot = v.sum(); mag = np.abs(v); o = np.argsort(-mag)
      c8 = (8 * a[o[:6]]) % m; c8 = np.where(c8 > m // 2, c8 - m, c8)
      cum = np.cumsum(v[o]); first = next((j + 1 for j in range(len(cum)) if np.sign(cum[j:]).min() == np.sign(cum[j:]).max() == np.sign(tot)), None)
      print('m', m, factorint(m), 'r', len(factorint(m)), 'sign', '+' if tot > 0 else '-', '| top1 %.3f top4 %.3f of sum|.|' % (mag[o[0]] / mag.sum(), mag[o[:4]].sum() / mag.sum()),
            '| 8a mod m of top terms', list(c8), '| partial sums fix sign after', first, 'terms', flush=True)
