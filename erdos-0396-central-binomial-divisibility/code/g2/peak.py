# Mechanism test: primes in a residue class making an even real character chi mod q equal -1
# on every prime create a huge peak of |Psi_m| at a primitive q-th root of unity:
#   log|Psi_m(zeta_q^b)| = -sum_{e|m,e<m} mu(m/e) log|1 - zeta_q^{be}|  ~  |B| 2^r,  B = (lam_even-lam_odd)/2.
# For each m: global max of log|Psi| on the circle (dense FFT grid) vs the q-th-root values,
# and how much of [y^n] Q^2 (n in the bulk, and n = rho0+1 when T >= 2) comes from windows around zeta_q^b.
import sys, time, numpy as np
from math import gcd
from core2 import pf, phi, sqfree_divs, logQ

def run(m, q, M=None, nsample=2000, win=None):
    ph = phi(m); D = m - ph; r = len(pf(m)); T = m // ph
    if M is None:
        M = 1 << int(np.ceil(np.log2(2 * D + 2)))
    t0 = time.time()
    th = np.arange(M) / M                              # turns
    L = np.zeros(M, dtype=complex)
    for e, mu in sqfree_divs(m):
        if e == m: continue
        ang = ((e % M) * np.arange(M, dtype=np.int64) % M) / M   # exact e*j mod M
        L -= mu * np.log(1 - np.exp(2j * np.pi * ang))
    L[0] = 0  # y = 1 is a root of Q (factor 1-y); value irrelevant
    L[~np.isfinite(L)] = -np.inf
    lab = L.real
    jmax = np.nanargmax(np.where(np.isfinite(lab), lab, -1e300))
    bs = [b for b in range(1, q) if gcd(b, q) == 1]
    peaks = {}
    for b in bs:
        v = logQ(m, np.array(0.0), np.array(b / q)).real
        peaks[b] = float(v)
    # FFT coefficients of Q^2 (shift by max to avoid overflow)
    shift = 2 * lab[jmax]
    F = np.exp(2 * L - shift)
    c = np.fft.fft(F) / M                       # c[n] = (1/M) sum F_j e^{-2 pi i n j/M} ~ [y^n] Q^2 * e^{-shift}
    # local windows around b/q
    if win is None: win = 0.02
    loc = np.zeros(M, dtype=complex)
    for b in bs:
        mask = np.abs(((th - b / q + 0.5) % 1.0) - 0.5) < win
        Fl = np.where(mask, F, 0)
        loc += np.fft.fft(Fl) / M
    n_bulk = np.linspace(1, 2 * D - 1, nsample).astype(int)
    big = np.abs(c[n_bulk].real) > 1e-6 * np.max(np.abs(c.real))
    agree = np.mean(np.sign(c[n_bulk].real[big]) == np.sign(loc[n_bulk].real[big])) if big.any() else np.nan
    relerr = np.median(np.abs(c[n_bulk] - loc[n_bulk])[big] / np.abs(c[n_bulk].real[big])) if big.any() else np.nan
    print(f"m={m} r={r} q={q} T={T} phi/m={ph/m:.4f} M={M} ({time.time()-t0:.0f}s)")
    print(f"  global max log|Psi| on grid = {lab[jmax]:.3f} at turns {th[jmax]:.6f} (nearest b/q: {min(bs, key=lambda b: abs(((th[jmax]-b/q+0.5)%1)-0.5))}/{q})")
    print("  log|Psi(zeta_q^b)|: " + ", ".join(f"{b}:{v:.3f}" for b, v in peaks.items()))
    # second-highest local max away from all b/q windows
    far = np.ones(M, bool)
    for b in bs: far &= np.abs(((th - b / q + 0.5) % 1.0) - 0.5) > win
    jf = np.argmax(np.where(far & np.isfinite(lab), lab, -1e300))
    print(f"  max log|Psi| outside windows (+-{win} turns) = {lab[jf]:.3f} at turns {th[jf]:.6f}")
    print(f"  bulk coeffs of Q^2: sign(total)==sign(window part) for {agree*100:.1f}% of {big.sum()} sampled n; median rel. err {relerr:.2e}")
    if T >= 2:
        for k in range(2, T + 1):
            n = m + 1 - k * ph
            if k == 2:
                print(f"  level 1: n=rho0+1={n}: FFT total {c[n].real:+.4e}, window part {loc[n].real:+.4e} (scaled by e^-{shift:.1f})")
    return c, loc, shift

if __name__ == '__main__':
    q = int(sys.argv[1]); ms = [int(a) for a in sys.argv[2:]]
    for m in ms: run(m, q)
