# explicit K_1 of the effective A3 (Thm E + Prop F of the report) for a piece d at level k:
#   rho_k = a_{k+1} / sum|H/2|^{k+1},  B = (k+1)(theta/2 + tau*) + 1/d,  K_1 = 40 k B / rho_k scaled (rho/12 normalisation)
import sys, numpy as np
from tr import data, phi
for arg in sys.argv[1:]:
    d, k = map(int, arg.split(':'))
    a, z, logH, h1 = data(d)
    w = z * np.exp((k + 1) * (logH - logH.real.max()))
    rho = w.sum().real / np.abs(w).sum()
    th = phi(d) / d; tau = np.abs(h1.imag).max() / d; B = (k + 1) * (th / 2 + tau) + 1 / d
    K1 = max(3 * k * B / rho, 6.4 * k ** 1.75 / rho ** 0.5) if rho > 0 else None
    o = np.argsort(-logH.real)
    eta = 1 - np.exp(logH[o[2]].real - logH[o[0]].real)
    print(f'd={d} k={k} rho={rho:.3f} tau*={tau:.3f} B={B:.2f} K1~{K1 and round(K1)}  eta={eta:.3f} argH0/pi={abs(logH[o[0]].imag/np.pi)%2:.4f}')
