# Trace data of a piece d (f = Phi_{2d}, zeta = e^{i pi a/d}, a odd, gcd(a,d)=1):
#   H = (x^{2d}-1)/Phi_{2d},  logH(zeta),  h1 = zeta H'(zeta)/H(zeta),  tau = Im(h1)/d.
#   a_n = Tr(zeta (H/2)^n)  (large-K level k negative iff a_{k+1} > 0)
#   corrected predictor  M_k(K) = sum zeta (H/2)^{k+1} (K + beta)^k,  beta = 1/d + (k+1)(-theta/2 + i tau),
#   theta = phi(d)/d;  S_k(K) ~ -M_k(K)/(d k!).
import sys, os, numpy as np
from math import gcd
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'agentV'))
from fastgood import sqfree_divs, phi, pf

def data(d, chunk=1 << 18):
    n2 = 2 * d
    a = np.arange(1, n2, 2, dtype=np.int64)
    a = a[np.gcd(a, d) == 1]
    logH = np.zeros(len(a), np.complex128); h1 = np.zeros(len(a), np.complex128)
    for e, mu in sqfree_divs(n2):
        if e == n2: continue
        c = np.exp(1j * np.pi * ((a * e) % n2) / d)
        logH -= mu * np.log(c - 1)
        h1 -= mu * e * c / (c - 1)
    z = np.exp(1j * np.pi * a / d)
    return a, z, logH, h1

def a_n(z, logH, ns):
    "a_n / (|H_max|/2)^n  for n in ns, and log scale"
    L0 = logH.real.max() - np.log(2)
    return [float(np.sum(z * np.exp(n * (logH - np.log(2)) - n * L0)).real) for n in ns], L0

def Mk(z, logH, h1, d, K, k):
    th = phi(d) / d
    beta = 1 / d + (k + 1) * (-th / 2 + 1j * h1.imag / d)
    L0 = logH.real.max() - np.log(2)
    return float(np.sum(z * np.exp((k + 1) * (logH - np.log(2)) - (k + 1) * L0) * ((K + beta) / K) ** k).real)

def summary(d, nmax=40):
    a, z, logH, h1 = data(d)
    th = phi(d) / d
    o = np.argsort(-logH.real)
    top = [(int(a[j]), float(np.exp(logH[j].real)), float(np.angle(np.exp(1j * logH[j].imag)) / np.pi), float(h1[j].imag / d)) for j in o[:4]]
    gap = float(logH[o[2]].real - logH[o[0]].real) if len(o) > 2 else None  # log(|H_3|/|H_1|): pairs o[0],o[1] conj
    v, _ = a_n(z, logH, range(1, nmax + 1))
    return dict(d=d, theta=th, top=top, gap=gap, signs=''.join('+' if x > 1e-9 else ('-' if x < -1e-9 else '0') for x in v),
                tau_max=float(np.abs(h1.imag).max() / d), n=len(a))

if __name__ == '__main__':
    for d in map(int, sys.argv[1:]):
        s = summary(d)
        print(d, pf(d), 'theta=%.4f' % s['theta'], 'gap=%.4f' % s['gap'], 'tau_max=%.2f' % s['tau_max'])
        print('   top (a,|H|,argH/pi,tau):', [(x[0], round(x[1], 2), round(x[2], 4), round(x[3], 3)) for x in s['top']])
        print('   signs a_1..a_40:', s['signs'])
