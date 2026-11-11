# Self-check of Lemma X: for f=Phi_{2d}(x) | x^m+1, N=j'(x^m+1), any integer c with j' c^(s+1) |R_s(x)| < 1/2
# has frac(N c^(s+1) / f^(s+1)) > 1/2 (so a prime q=f/c with q||N gets a carry at level s+1).
import sys, random
from fractions import Fraction
sys.path.insert(0, '..')
from poly import cyclo
def ev(p, x): return sum(a * x**i for i, a in enumerate(p))
random.seed(1)
for (m, d, s, nu0, a) in [(165, 55, 2, 10, -3), (165, 11, 2, 8, -105), (195, 65, 2, 14, -3), (165, 165, 1, 1, -1)]:
    f = cyclo(2*d)
    for trial in range(20):
        x = random.randint(10**6, 10**7); jp = random.randint(1, 15)
        fx = ev(f, x); N = jp * (x**m + 1); assert N % fx == 0
        cmax = int((Fraction(x**nu0, 2*jp*abs(a))) ** Fraction(1, s+1) * 0.9) if False else int((x**nu0 / (2*jp*abs(a))) ** (1/(s+1)) * 0.9)
        for c in [1, 2, max(1, cmax // 2), max(1, cmax)]:
            r = Fraction(N * c**(s+1), fx**(s+1)); fr = r - (r.numerator // r.denominator)
            assert fr > Fraction(1, 2), (m, d, x, jp, c, float(fr))
    print('ok', m, d, 'cmax at x=1e6 ~', cmax)
