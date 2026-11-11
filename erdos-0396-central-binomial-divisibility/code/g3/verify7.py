# independent check of the exact s=7 value for (m,d) = (50115065, 10023013): residues at two primes not used by deep.level
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'aur'))
from deep import coeffs_mod, PR
V = -3299327387824433105301865655986924920323754547685215817308920
P = PR[int(sys.argv[1])]
r = int(coeffs_mod(50115065, 10023013, 7, 4, P)[0])
print('prime', P, 'residue', r, 'expected', V % P, 'OK' if r == V % P else 'MISMATCH', flush=True)
