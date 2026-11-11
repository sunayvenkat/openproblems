# Independent check of the Lemma A counterexample (m,d)=(1365,455): base-f digits of x^m+1, f=Phi_910,
# computed by exact polynomial division (poly.py), and an integer check of w mod q^s < q^s/2 at a sample x.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from poly import cyclo, digits
m, d = int(sys.argv[1]) if len(sys.argv) > 1 else 1365, int(sys.argv[2]) if len(sys.argv) > 2 else 455
f = list(cyclo(2 * d)); delta = len(f) - 1
ds = digits([1] + [0] * (m - 1) + [1], f)          # D_0, D_1, ..., D_T
print('m', m, 'd', d, 'delta', delta, 'T', len(ds) - 1)
for k, D in enumerate(ds):
    print('  D_%d: deg %s lead %s' % (k, len(D) - 1 if D else None, D[-1] if D else 0))
# integer check at x = 10 (q need not be prime for the digit statement)
x = 10
ev = lambda P: sum(c * x**i for i, c in enumerate(P))
q = ev(f); n_i = x**m + 1; assert n_i % q == 0; w = n_i // q
carries = [s for s in range(1, len(ds) + 2) if 2 * (w % q**s) >= q**s]
print('x=10: levels s with w mod q^s >= q^s/2:', carries)
