"""Task 2: numeric checks of Lemma 1 (local reduction) and the CRT small-prime claim."""
import random
from verify396 import carries, vp, factor, is_prime

random.seed(396)
# Lemma 1: q > 2i, q | n-i  =>  carries(n,q) == carries(n-i,q)
bad = 0; tested = 0; counter = None
for _ in range(20000):
    i = random.randrange(0, 12); n = random.randrange(i + 2, 10**12)
    for q in factor(n - i):
        if q > 2 * i:
            tested += 1; bad += carries(n, q) != carries(n - i, q)
        elif q > i and counter is None and carries(n, q) != carries(n - i, q):
            counter = (n, i, q, carries(n, q), carries(n - i, q))
print(f"Lemma 1: {tested} (n,i,q) with q>2i, mismatches = {bad}")
print("  q in (i,2i] can differ, e.g. (n,i,q,carries(n),carries(n-i)) =", counter)
# for i < q <= 2i the carry from i+i only adds: carries(n,q) >= carries(n-i,q)+1
viol = 0
for _ in range(20000):
    i = random.randrange(1, 12); n = random.randrange(i + 2, 10**12)
    for q in factor(n - i):
        if i < q <= 2 * i:
            viol += carries(n, q) < carries(n - i, q) + 1
print(f"  i<q<=2i: violations of carries(n) >= carries(n-i)+1 : {viol}")

# CRT claim: n = -1 mod p^e, e > v_p((k+1)!)  =>  carries >= e  and  sum v_p(n-i) = v_p((k+1)!)
def vfact(m, p):
    s, pp = 0, p
    while pp <= m:
        s += m // pp; pp *= p
    return s
viol = 0; cnt = 0
for _ in range(20000):
    k = random.randrange(0, 30); ps = [p for p in range(2, k + 2) if is_prime(p)]
    if not ps: continue
    p = random.choice(ps); e = vfact(k + 1, p) + 1 + random.randrange(3)
    n = random.randrange(1, 10**15) * p**e - 1
    if n <= k: continue
    cnt += 1
    s = sum(vp(n - i, p) for i in range(k + 1))
    viol += not (carries(n, p) >= e and s == vfact(k + 1, p))
print(f"CRT claim: {cnt} random cases, violations = {viol}")
# sharpness: e = v_p((k+1)!) is NOT enough when p^e <= k+1  (p = k+1 prime)
k, p = 2, 3; n = 3**5 + 2   # e=1 = v_3(3!), n = -1 mod 3, but 3^5 | n-2
print(f"  e=v_p((k+1)!) counterexample k={k} p={p} n={n}: sum v_p={sum(vp(n-i,p) for i in range(k+1))}, carries={carries(n,p)}")

# family '+' small primes: n = (k+1) + p^e * Y with e > max v_p(j'):  sum v_p(n-i) = v_p((k+1)!)  and each
# base-p digit p-1 of Y gives a carry
viol = 0
for _ in range(20000):
    k = random.randrange(1, 30); ps = [p for p in range(2, k + 2) if is_prime(p)]
    p = random.choice(ps); e = max(vp(j, p) for j in range(1, k + 2)) + 1 + random.randrange(2)
    R = random.randrange(0, 6); pos = random.randrange(0, 5)
    Y = random.randrange(0, p**pos) + p**pos * (p**R - 1) + p**(pos + R) * random.randrange(0, 1000)
    n = k + 1 + p**e * Y
    s = sum(vp(n - i, p) for i in range(k + 1))
    viol += not (s == vfact(k + 1, p) and carries(n, p) >= R)
print(f"family '+' small-prime digits: violations = {viol}")
