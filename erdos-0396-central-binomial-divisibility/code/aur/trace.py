# Large-K prediction of the level-k digit sign of piece Phi_{2d} (agent AC, Thm A3):
#   lc(D_k) ~ -K^k/(d k!) * a_{k+1},  a_n = Tr(zeta * (H(zeta)/2)^n),  H = (x^{2d}-1)/Phi_{2d}
# (gamma = g(zeta) = -H(zeta)/2, 1/f'(zeta) = zeta H(zeta)/(2d)).  Level k is negative iff a_{k+1} > 0.
import sys, numpy as np
from math import gcd
sys.path.insert(0, '../agentV')
from fastgood import sqfree_divs

def trace_signs(d, nmax):
    n2 = 2 * d
    a = np.array([a for a in range(1, n2) if gcd(a, n2) == 1], dtype=np.float64)
    th = 2 * np.pi * a / n2
    logH = np.zeros(len(a), dtype=np.complex128)
    for e, mu in sqfree_divs(n2):          # e | 2d with mu = mobius(2d/e) != 0
        if e == n2: continue
        logH -= mu * np.log(np.exp(1j * th * e) - 1)
    z = np.exp(1j * th)
    out = []
    for n in range(1, nmax + 1):
        L = n * logH; sh = L.real.max()
        v = np.sum(z * np.exp(L - sh)).real
        out.append((n, v, sh))
    i = np.argsort(-logH.real)[:6]
    return out, [(float(np.exp(logH[j].real)), float(np.angle(np.exp(logH[j])) / np.pi)) for j in i]

if __name__ == '__main__':
    d, nmax = int(sys.argv[1]), int(sys.argv[2])
    out, top = trace_signs(d, nmax)
    print('top |H|, arg/pi:', top)
    first = [n for n, v, _ in out if n >= 2 and v > 0]
    print('signs a_n (n=2..):', ''.join('+' if v > 0 else '-' for n, v, _ in out[1:]))
    print('first n>=2 with a_n>0 (level k=n-1 negative):', first[:3])
