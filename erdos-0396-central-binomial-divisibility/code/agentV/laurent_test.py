"""Test the Laurent-sign rule on ALL x (the level test 2*(N mod q^t) >= q^t is defined for any integer q,
prime or not), N = j'(x^m+1), q = Phi_{2d}(x).  Reports last x where actual != predicted
(i) for the whole level set, (ii) for the binary 'has a carry' status that the construction needs."""
import sys
from famplus import phi_poly, predicted_levels, actual_levels
from lemC import divisors

def scan(m, js, X):
    for d in divisors(m):
        pr = predicted_levels(m, d)
        for j in js:
            last_set = last_bin = None
            for x in range(2, X + 1):
                N = j * (x ** m + 1); q = phi_poly(2 * d, x)
                ac = actual_levels(N, q)
                if ac != pr: last_set = x
                if bool(ac) != bool(pr): last_bin = x
            print(f"m={m:4d} d={d:4d} j'={j} pred={'GOOD' if pr else 'BAD '} levels={sorted(pr)[:8]}{'...' if len(pr)>8 else ''}"
                  f"  last x<= {X} with set-mismatch={last_set}  binary-mismatch={last_bin}", flush=True)

if __name__ == "__main__":
    for spec in sys.argv[1:]:
        m, X = map(int, spec.split(':'))
        scan(m, (1, 2, 3), X)
