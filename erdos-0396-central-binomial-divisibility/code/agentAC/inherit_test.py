# Test the inheritance theorem: if the top piece of m is good at level s and p is a prime, p not | m,
# p > (s+1)phi(m), then the top piece of m*p is good at level s with the SAME first coefficient
# (located at N' = p*N, value equal).  Also test full goodness (all pieces) of m*p.
import sys
from sympy import primerange
from core import phi
from fullgood import piece_level, full_good

def top1(m):  # level-1 data of the top piece
    return piece_level(m, m, 1)

if __name__ == '__main__':
    seeds = [int(a) for a in sys.argv[1:]] or [105, 165, 195]
    for S in seeds:
        b = 2 * phi(S)
        base = top1(S)
        print('seed', S, '2phi', b, 'level-1 (offset,sign)', base, flush=True)
        agree = dis = 0; below = []
        for p in primerange(7, 2 * b + 60):
            if S % p == 0: continue
            r = top1(S * p)
            if p > b:
                if r and base and r[1] == base[1]: agree += 1
                else: dis += 1; print('   DISAGREE above bound p=', p, r)
            else:
                below.append((p, '+' if r and r[1] > 0 else '-' if r else '0'))
        print('   p<=2phi:', ' '.join(f'{p}{s}' for p, s in below))
        print('   p>2phi : agree', agree, 'disagree', dis, flush=True)
