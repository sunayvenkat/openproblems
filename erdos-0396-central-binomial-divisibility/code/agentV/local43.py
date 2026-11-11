"""§4.3: (i) image of x -> x^L on (Z/p^K)^* contains 1 + p^c Z, c = v_p(L)+1 (+1 if p=2); (ii) digit setting on a real family."""
from math import prod
from verify396 import vp, carries
from famplus import family
def image_check(p, L, K):
    c = vp(L, p) + 1 + (p == 2); mod = p ** K
    img = {pow(x, L, mod) for x in range(1, mod) if x % p}
    full = all((1 + p**c * t) % mod in img for t in range(p ** (K - c)))
    sharper = all((1 + p**(c - 1) * t) % mod in img for t in range(p ** (K - c + 1)))
    return c, full, sharper
for p, L, K in [(3, 105, 6), (3, 315, 7), (3, 35, 5), (5, 105, 5), (2, 105, 10), (2, 15, 10), (7, 105, 4)]:
    print(f"p={p} L={L}: c={image_check(p, L, K)[0]}  1+p^c Z in image: {image_check(p, L, K)[1]}   1+p^(c-1) Z in image: {image_check(p, L, K)[2]}")
# digit setting for k=2, m=(3,5,7): want digits p-1 at positions c..c+R-1 of U*B^L, R = v_p(3!) = 1
k, ms = 2, [3, 5, 7]; M0, L, cc, e = family(k, ms, extra=2)
Bres = {}
for p in (2, 3):
    c = vp(L, p) + 1 + (p == 2); R = vp(6, p); K = c + R; U = M0 // p ** e[p]
    target = next(B for B in range(1, p ** K) if B % p and all((U * pow(B, L, p**K) // p**pos) % p == p - 1 for pos in range(c, c + R)))
    Bres[p] = (target, p ** K)
from sympy.ntheory.modular import crt
b, W = crt([Bres[2][1], Bres[3][1]], [Bres[2][0], Bres[3][0]])
print("k=2 m=(3,5,7) e_p:", e, " B = %d mod %d" % (b, W))
worst = None
for B in range(int(b), int(b) + 20 * int(W), int(W)):
    n = M0 * B ** L + 3
    for p in (2, 3):
        need = sum(vp(n - i, p) for i in range(3))
        if need > carries(n, p): worst = (B, p)
print("  small primes p<=3 satisfied for 20 B in the progression:", worst is None)
