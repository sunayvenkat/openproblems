# Identity: m = X^4+pX^2+qX+r, y^2 = m(c), G = X^3 + c X^2 + (c^2+p+y) X + (q - 2c^3 - 2cy)/2.
# Then G^2 mod m is linear: u + vX.  So x(w) with disc(x - theta) = (const * gamma)^2 splits m(x(w)) into 2 quartics.
import sympy as sp
X, p, q, c, y = sp.symbols('X p q c y')
r = y**2 - (c**4 + p*c**2 + q*c)                 # forces y^2 = m(c)
m = sp.Poly(X**4 + p*X**2 + q*X + r, X)
G = X**3 + c*X**2 + (c**2 + p + y)*X + (q - 2*c**3 - 2*c*y)/2
rem = sp.rem(sp.Poly(sp.expand(G**2), X), m)
print("deg of G^2 mod m:", rem.degree(), " coeff X^2, X^3:", [sp.simplify(rem.coeff_monomial(X**k)) for k in (2, 3)])
print("v =", sp.factor(rem.coeff_monomial(X)), "\nu =", sp.factor(rem.coeff_monomial(1)))
