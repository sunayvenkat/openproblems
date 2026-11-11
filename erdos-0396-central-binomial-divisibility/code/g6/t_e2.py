# sanity: checker on g5's E_2 family (x = 42y+9) should report all good
import sympy as sp
from check import w, analyze, crt_class
x = 42*w + 9
n = sp.expand(52920*x**2 + 47166*x + 10509)
r = analyze(n, 2)
print(r is not None and crt_class(*r[1:]))
n1 = sp.expand((14*w+3)*(24*w+17))
r = analyze(n1, 1); print(r is not None and crt_class(*r[1:]))
