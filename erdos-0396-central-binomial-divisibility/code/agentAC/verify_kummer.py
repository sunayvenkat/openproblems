# Task 3: check the Laurent-sign carry criterion against Kummer directly.
# For (m,d,k,j'): find x >= x0 with q = Phi_{2d}(x) prime, set n = j'(x^m+1) + i (i = k+1-j'),
# so n - i = j'(x^m+1).  Compute nu_q(C(2n,n)) = #carries of n+n in base q (Kummer) and compare with
# the prediction #{s in [1,T-1] : level s negative} from core.level_sign.
import sys
from sympy import isprime
from core import phi, level_sign

def poly_eval(m_d):
    pass

def cyclo_coeffs(n):
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    from poly import cyclo
    return list(cyclo(n))

def kummer_nu(n, q):
    "number of carries in n+n base q = nu_q(C(2n,n))"
    c = 0; carry = 0
    while n:
        dgt = n % q; n //= q
        carry = 1 if 2 * dgt + carry >= q else 0
        c += carry
    return c

def predicted(m, d):
    T = m // phi(d)
    neg = 0; last = None
    for s in range(1, T):
        r = level_sign(m, d, s)
        if r and r[1] < 0: neg += 1
    return neg

def run(m, d, k, jp, x0):
    f = cyclo_coeffs(2 * d)
    x = x0
    while True:
        q = sum(c * x**e for e, c in enumerate(f))
        if isprime(q): break
        x += 1
    i = k + 1 - jp
    n = jp * (x**m + 1) + i
    v = 0; t = n - i
    while t % q == 0: t //= q; v += 1
    nu = kummer_nu(n, q)
    pr = predicted(m, d)
    print(f'm={m} d={d} k={k} j\'={jp} x={x} digits(q)={len(str(q))} nu_q(n-i)={v} '
          f'Kummer nu_q(C(2n,n))={nu} predicted={pr} {"OK" if nu == pr else "MISMATCH"}', flush=True)
    return nu == pr

if __name__ == '__main__':
    cases = [(15, 1, 3, 2, 10**6), (15, 3, 3, 1, 10**5), (15, 5, 2, 3, 10**4), (21, 3, 4, 2, 10**5),
             (21, 7, 1, 1, 10**4), (45, 9, 2, 2, 10**4), (45, 15, 3, 1, 10**4),
             (105, 105, 1, 1, 10**4), (105, 35, 2, 1, 10**4), (165, 165, 1, 2, 10**4),
             (195, 195, 2, 3, 10**4), (195, 65, 1, 1, 10**4)]
    ok = all(run(*c) for c in cases)
    print('ALL OK' if ok else 'SOME MISMATCH')
