# Saddle-point predictor for a_s = [y^n] Q^k (k=s+1, n=m+1-k*phi) from the peaks of |Psi_m| at
# primitive q-th roots eta (primes chosen with chi(p) = -1 for an even real character chi mod q).
#   G(w) = log Q(eta e^w) = -sum_{e|m,e<m} mu(m/e) log(1 - eta^e e^{e w}),   k G'(w0) = n,
#   I_eta ~ eta^{-n} exp(k G(w0) - n w0) / sqrt(2 pi k G''(w0)),   prediction = sum over eta.
# Only eta^e = zeta_q^{b e mod q} and e*w (small) enter, so it runs for m far beyond exact reach.
# Usage: python saddle.py q b1,b2,.. m [m ...]   (check vs exact series when m < 3e6)
import sys, cmath, math
from core2 import pf, phi, sqfree_divs, first_sign, Qk_series

def Gder(divs, q, b, w, nder=3):
    "G, G', G'', G''' at w (complex), divisor list [(e, mu(m/e))] without e=m"
    out = [0j] * (nder + 1)
    for e, mu in divs:
        z = cmath.exp(2j * math.pi * ((b * e) % q) / q + e * w)
        u = z / (1 - z)                 # derivatives of -log(1-z) in w: e*u, e^2 u(1+u), e^3 u(1+u)(1+2u)
        out[0] -= mu * cmath.log(1 - z)
        out[1] += mu * e * u
        out[2] += mu * e * e * u * (1 + u)
        out[3] += mu * e ** 3 * u * (1 + u) * (1 + 2 * u)
    return out

def predict(m, q, bs, k, n):
    divs = [(e, mu) for e, mu in sqfree_divs(m) if e != m]
    tot = 0j; info = []
    for b in bs:
        w = 0j
        for _ in range(60):             # Newton on k G'(w) = n
            G = Gder(divs, q, b, w)
            step = (k * G[1] - n) / (k * G[2])
            w -= step
            if abs(step) < 1e-15 * (abs(w) + 1e-300): break
        G = Gder(divs, q, b, w)
        lgI = k * G[0] - n * w - 2j * math.pi * ((b * n) % q) / q - 0.5 * cmath.log(2 * math.pi * k * G[2])
        tot += cmath.exp(lgI - 0)       # caller rescales if huge
        eps = abs(k * G[3]) / abs(k * G[2]) ** 1.5   # Gaussian-validity parameter
        info.append((b, w, lgI, eps))
    return info

def report(m, q, bs, exact=True):
    ph = phi(m); T = m // ph; r = len(pf(m))
    print(f"m={m} r={r} primes mod {q}: {sorted(set(p % q for p in pf(m)))} T={T} phi/m={ph/m:.5f}")
    for s in range(1, T):
        k = s + 1; n = m + 1 - k * ph
        info = predict(m, q, bs, k, n)
        L = max(i[2].real for i in info)
        val = sum(cmath.exp(i[2] - L) for i in info)
        line = f"  level {s} n={n}: predicted sign {'+' if val.real > 0 else '-'} (|pred| ~ e^{L:.2f}, cos-phase {val.real/abs(val):+.3f}); " \
               + "; ".join(f"b={b} |w0|m={abs(w)*m:.3g} eps={eps:.3f}" for b, w, _, eps in info)
        if exact and n < 3 * 10**6:
            c = int(Qk_series(m, k, n)[n])
            line += f"; exact {'+' if c > 0 else '-' if c else '0'} log|c|={math.log(abs(c)) if c else float('nan'):.2f}"
        print(line, flush=True)

if __name__ == '__main__':
    q = int(sys.argv[1]); bs = [int(x) for x in sys.argv[2].split(',')]
    for m in [int(a) for a in sys.argv[3:]]: report(m, q, bs)
