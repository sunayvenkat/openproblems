# End-window rule: for prime r = e*phi0 + 1 - i in the one-term range ((e phi0+2)/2, e phi0+1] and w_{m0}(0) != 0,
#   sign(level e-1 of m0*r) = sign(w_{m0}(0)) * sign(first nonzero of beta_i, beta_{i+1}, ...),  beta = Phi_{m0}^e.
# Check against rscan output (which was itself checked against exact series).
import sys
from toppiece_rscan import cyclo_power, window, phi_of
for m0 in (105, 165, 195, 1365, 1155, 3003):
    e = 2; phi0 = phi_of(m0); D = e*phi0
    if m0 - e*phi0 < 0: continue
    beta = [int(x) for x in cyclo_power(m0, e, D + 1)]
    w0 = window(m0, e, 0)[0]
    ok = bad = 0
    from sympy import isprime
    for r in range((D + 2)//2 + 1, D + 2):
        if not isprime(r) or m0 % r == 0: continue
        i = D + 1 - r
        b = next(x for x in beta[i:] if x)
        pred = (w0 * b) < 0
        ex = window(m0 * r, e, 3)
        t = next(u for u in range(4) if ex[u]); actual = ex[t] < 0
        ok += pred == actual; bad += pred != actual
    print(m0, 'w0', w0, 'one-term primes', ok + bad, 'rule agrees', ok, 'disagrees', bad, flush=True)
