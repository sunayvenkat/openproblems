# Lemma S' test: n - i = A*B with B = -1 mod A, q^e || A, cofactor c' = A/q^e < q/2  =>  carries(n,q) >= e.
import random, sys
sys.path.insert(0, r'../h1')
from verify import carries
random.seed(7); tot = ok = 0; viol = []
for _ in range(20000):
    q = random.choice([3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127])
    e = random.randint(1, 4); c = random.randint(1, (q-1)//2)
    A = q**e * c
    B = A*random.randint(1, 10**6) - 1          # B = -1 mod A
    i = random.randint(0, min(5, (q-1)//2))
    n = A*B + i
    tot += 1
    if carries(n, q) >= e: ok += 1
    else: viol.append((q, e, c, i))
print('cases', tot, 'ok', ok, 'violations', viol[:5])
