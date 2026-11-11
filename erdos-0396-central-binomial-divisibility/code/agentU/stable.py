# Is the governor set D0={m: m | C(2m,m)} Hildebrand-stable? Measure density of {N<=X: 1_D0(N) != 1_D0(pN)}.
import numpy as np
X = 200000; Y = 7 * X + 1
spf = np.zeros(Y, dtype=np.int64)
for i in range(2, Y):
    if spf[i] == 0:
        spf[i::i][spf[i::i] == 0] = i
def carries(m, q):
    c = 0; s = q
    while s <= 2 * m:
        if (2 * m // s) % 2: c += 1
        s *= q
    return c
def gov(m):
    t = m
    while t > 1:
        q = int(spf[t]); v = 0
        while t % q == 0: t //= q; v += 1
        if carries(m, q) < v: return False
    return True
D = np.array([False] + [gov(m) for m in range(1, Y)])
assert [m for m in range(1, 100) if D[m]] == [1, 2, 6, 15, 20, 28, 42, 45, 66, 77, 88, 91]  # Pomerance's list
print('density D0 up to X:', D[1:X+1].mean())
for p in (2, 3, 5, 7):
    N = np.arange(1, X + 1)
    print(p, 'd{N: D0(N) xor D0(pN)} =', (D[N] != D[p * N]).mean(), ' P(pN in D0 | N in D0) =', D[p * N][D[N]].mean())
