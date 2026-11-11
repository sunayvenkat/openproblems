# Brute-force: for x <= X, n = P1 P2, n-1 = 2 P3 P4; test n in E_1 via Kummer. Report fraction and failure breakdown.
import sys
from collections import Counter
def carries(n, q):
    c = 0; m = n; s = 0
    # count s>=1 with n mod q^s >= q^s/2  <=> floor(2n/q^s) odd
    t = 2*n
    while t:
        t //= q
        if t & 1: c += 1
    return c
def factor_small(m, spf):
    f = {}
    m = abs(m)
    while m > 1:
        p = spf[m]
        while m % p == 0: f[p] = f.get(p, 0)+1; m //= p
    return f
def run(forms, X, cls=None):
    (a1,b1),(a2,b2),(a3,b3),(a4,b4) = forms
    LIM = max(a*X+abs(b) for a,b in forms)+1
    spf = list(range(LIM+1))
    for i in range(2, int(LIM**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, LIM+1, i):
                if spf[j] == j: spf[j] = i
    good = tot = 0; fails = Counter(); failx = []
    for x in range(1, X+1):
        if cls and x % cls[0] != cls[1]: continue
        P = [a*x+b for a,b in forms]
        if min(P) <= 0: continue
        n = P[0]*P[1]
        assert n - 1 == 2*P[2]*P[3]
        tot += 1
        ok = True; why = []
        # prime 2
        v2 = 1 + factor_small(P[2],spf).get(2,0) + factor_small(P[3],spf).get(2,0)
        if bin(n).count('1') < v2: ok = False; why.append('2')
        for j,(val,i) in enumerate([(P[0],0),(P[1],0),(P[2],1),(P[3],1)]):
            for q,v in factor_small(val, spf).items():
                if q == 2: continue
                vq = v + (factor_small(P[1-j] if j<2 else P[5-j], spf).get(q,0))
                if carries(n, q) < vq:
                    ok = False; why.append((j, q, 'c<q' if val//q < q else 'c>=q'))
        if ok: good += 1
        else:
            for w in why: fails[w if isinstance(w,str) else (w[0], w[2])] += 1
            failx.append((x, why))
    return good, tot, fails, failx
if __name__ == '__main__':
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    for forms in [[(12,-1),(22,9),(11,-1),(12,5)], [(14,3),(24,17),(7,5),(24,5)], [(4,-1),(6,1),(3,-1),(4,1)]]:
        good, tot, fails, failx = run(forms, X)
        print(forms, 'good', good, 'of', tot, 'frac %.4f' % (good/tot))
        print('  failures by (form, c<q?):', dict(fails))
        print('  sample failing x:', failx[:5])
