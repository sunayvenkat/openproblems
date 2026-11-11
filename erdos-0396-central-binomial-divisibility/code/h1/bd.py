# Breakdown of bad large-prime events (q > x^(2/3)) by form j, cofactor c, q mod a.
import sys, math
from collections import Counter
from verify import carries
from ek import sieve, fac
forms = [(12,-1),(22,9),(11,-1),(12,5)]; lam = [1,1,2,2]
X = int(sys.argv[1]); x0 = X//2
spf = sieve(24*X+10); C = Counter(); tot = 0; ex = []
for x in range(x0, X+1):
    P = [a*x+b for a,b in forms]; n = P[0]*P[1]; tot += 1
    for j,(a,b) in enumerate(forms):
        f = {}; fac(P[j], spf, f)
        for q, e in f.items():
            if q > x**(2/3):
                fo = {}; fac(n*(n-1), spf, fo) if False else None
                other = P[1-j] if j<2 else P[5-j]
                e2 = e + (other % q == 0)
                if carries(n, q) < e2:
                    c = P[j]//q; C[(j, q % a, 'c=1' if c==1 else 'c>1')] += 1
                    if len(ex) < 6: ex.append((x, j, q, c))
for k in sorted(C): print(k, round(C[k]/tot, 4))
print(ex)
