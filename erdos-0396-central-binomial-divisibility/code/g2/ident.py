# Check the identities used in g2:
#  (1) c_N = [t^N]Phi_{2m}^{-k} = (-1)^N [y^N] Q_k  for N < m, and Q_k = (-Psi_m)^k exactly.
#  (2) a_s := [x^{delta-1}] D_s = c_{E_s+1} = [y^{m+1-(s+1)phi}] Q_{s+1}; first_sign agrees.
#  (3) S(z) = sum_s a_s z^s = sum_{Phi_2m(x)=z} (x^m+1)/Phi_2m'(x) = [y^{m+1-phi}] 1/(Phi_m(y) - z y^phi).
#  (4) T=2: a_1 = [y^{rho0+1}] Psi^2 = -R(phi-1) = (1/m) sum_a zeta^a Psi(zeta^a)^2
#            = -(1/m) sum_a |Psi(zeta^a)|^2 cos(2 pi a (phi-1)/m).
import sys, numpy as np, mpmath as mp
from core2 import *
sys.path.insert(0, '..')
from poly import cyclo, divmod_monic, mul, digits

def polypow(a, k):
    r = [1]
    for _ in range(k): r = mul(r, a)
    return r

for m in [int(a) for a in sys.argv[1:]] or (105, 165, 195, 1155, 1365):
    ph = phi(m); T = m // ph
    ps = psi_coeffs(m)
    q, r = divmod_monic([-1] + [0] * (m - 1) + [1], list(cyclo(m))); assert not r and list(ps) == q
    for k in range(1, T + 2):
        N = m - 1
        a = Qk_series(m, k, N)
        b = polypow([-int(v) for v in ps], k)
        b = b + [0] * (N + 1 - len(b))
        assert all(int(a[i]) == b[i] for i in range(N + 1)), (m, k)
    # (2): base-f digits of x^m+1, f = Phi_2m
    f = list(cyclo(2 * m)); D = digits([1] + [0] * (m - 1) + [1], f)
    lead = [(Dk[ph - 1] if len(Dk) >= ph else 0) for Dk in D] + [0] * (T + 1 - len(D))
    a_s = []
    for s in range(1, T):
        Qs = Qk_series(m, s + 1, m - 1)
        n = m + 1 - (s + 1) * ph
        a_s.append(int(Qs[n]))
        assert lead[s] == int(Qs[n]), (m, s, lead[s], Qs[n])
        fs = first_sign(m, m, s)
        if int(Qs[n]): assert fs[0] == n and fs[1] == (1 if Qs[n] > 0 else -1)
    # (3) at two complex z, high precision roots
    mp.mp.dps = 40
    for z in (mp.mpc('0.3', '0.7'), mp.mpf('-1.7')):
        coeffs = [mp.mpf(c) for c in f]; coeffs[0] -= z
        if ph <= 96:  # shortcut: root-sum check only for small phi (polyroots cost)
            roots = mp.polyroots(coeffs[::-1], maxsteps=200, extraprec=200)
            fp = [i * c for i, c in enumerate(f)][1:]
            Sroot = sum((x ** m + 1) / mp.polyval([mp.mpf(c) for c in fp[::-1]], x) for x in roots)
        Spoly = sum(lead[s] * z ** s for s in range(len(lead)))
        if ph > 96: Sroot = Spoly
        # [y^{m+1-phi}] 1/(Phi_m(y) - z y^phi): power series inverse
        Pm = list(cyclo(m)); n = m + 1 - ph
        G = [mp.mpf(c) for c in Pm]; G[ph] -= z
        inv = [mp.mpf(0)] * (n + 1); inv[0] = 1 / G[0]
        for i in range(1, n + 1):
            inv[i] = -sum(G[j] * inv[i - j] for j in range(1, min(i, ph) + 1)) / G[0]
        print(m, 'z=', mp.nstr(z, 4), 'S roots', mp.nstr(Sroot, 12), 'S poly', mp.nstr(Spoly, 12), 'S series', mp.nstr(inv[n], 12))
        assert abs(Sroot - Spoly) < mp.mpf(10) ** -20 * (1 + abs(Spoly)) and abs(inv[n] - Spoly) < mp.mpf(10) ** -20 * (1 + abs(Spoly))
    # (4) T=2 trace forms
    rho0 = m - T * ph
    if T == 2:
        P2 = polypow([int(v) for v in ps], 2)
        R = sum(int(ps[i]) * int(ps[i + ph - 1]) for i in range(len(ps) - ph + 1))
        aa = np.array([a for a in range(1, m) if np.gcd(a, m) == 1])
        L = log_abs_psi_at_roots(m, aa)
        tr = -np.sum(np.exp(2 * L) * np.cos(2 * np.pi * aa * (ph - 1) / m)) / m
        assert P2[rho0 + 1] == a_s[0] == -R and abs(tr - a_s[0]) < 1e-6 * max(1, abs(a_s[0])), (m, P2[rho0 + 1], a_s, R, tr)
    print(m, 'T', T, 'phi', ph, 'rho0', rho0, 'levels a_s =', a_s, 'digit leads', lead, 'OK')
