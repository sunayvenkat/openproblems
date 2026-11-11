import random, math
from sympy import factorint
from verify import carries
random.seed(3); X = 10**15; k = 0
while k < 4:
    x = random.randrange(X//2, X); P0, P1 = 12*x-1, 22*x+9; n = P0*P1
    for q, e in factorint(P0).items():
        th = math.log(q)/math.log(x)
        if .55 < th < .65 and carries(n, q) < 1:
            c = P0//q; bits = [(2*n//q**s) & 1 for s in range(1, 6)]
            print('x', x, 'q', q, 'c', c, 'c^2/q %.3g' % (c*c/q), 'f', (22*c*c) % 12, 'bits s=1..5', bits, 'n/q^3 %.3g' % (n/q**3), 'other factors of P0', factorint(c))
            k += 1
