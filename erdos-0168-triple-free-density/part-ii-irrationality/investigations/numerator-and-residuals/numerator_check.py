"""Whole-model period residues and exact smooth/off-S normalization."""
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = spec_from_file_location(name, ROOT / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


models = load("numerator_models", "Erdos 168 reflected return models/two_sided_models_check.py")
fast = load("numerator_integer", "Erdos 168 correlated return arithmetic/arithmetic_audit_check.py")


def valuation(n, prime):
    assert n
    result = 0
    while n % prime == 0:
        n //= prime
        result += 1
    return result


def split_periods(a, b):
    A, B = a**3-1, b**3-1
    s2, s3 = valuation(B, 2), valuation(A, 3)
    A0, B0 = A//3**s3, B//2**s2
    A1 = (a-1)//3**valuation(a-1, 3)
    A2 = (a*a+a+1)//3**valuation(a*a+a+1, 3)
    B1, B2 = (b-1)//2**valuation(b-1, 2), b*b+b+1
    assert A1*A2 == A0 and B1*B2 == B0
    assert gcd(A1, A2) == gcd(B1, B2) == 1
    return A, B, s2, s3, A0, B0, A1, A2, B1, B2


def blocks(p, q, sigma):
    model = models.model(p, q, sigma)
    eta, z = model[3], model[4]
    a, b = 2**q, 3**p
    A, B = a**3-1, b**3-1

    def row(i, k):
        value = 0
        for r in range(q):
            digit = eta(r+i*q, k) if (r+i*q, k) != (0, 1) else 0
            value = 2*value+1-3*digit
        return value

    head, tile = [], []
    for i in range(3):
        h = 0
        for k in range(4):
            h = 3*h+row(i, k)
        head.append(h)
        line = []
        for j in range(3):
            t = 0
            for k in range(p):
                t = 3*t+row(i, k+j*p+4)
            line.append(t)
        tile.append(line)
    W = [B*head[i]+sum(b**(2-j)*tile[i][j] for j in range(3)) for i in range(3)]
    V = [sum(a**(2-i)*tile[i][j] for i in range(3)) for j in range(3)]
    N = 2*sum(a**(2-i)*W[i] for i in range(3))-27*A*B
    assert F(N, 27*A*B) == z
    assert N == fast.exact_model_numerator(p, q, sigma)
    return N, W, V


def verify(p, q, P, Q, sigma, decompose=True):
    a, b, U, V = 2**q, 3**p, 2**Q, 3**P
    A, B, s2, s3, A0, B0, A1, A2, B1, B2 = split_periods(a, b)
    if decompose:
        N, W, Y = blocks(p, q, sigma)
        residues = (2*sum(W), 2*((W[1]-W[0])*a+W[2]-W[0]),
                    2*sum(Y), 2*((Y[1]-Y[0])*b+Y[2]-Y[0]))
        assert all((N-r) % m == 0 for r, m in zip(residues, (A1, A2, B1, B2)))
    else:
        N = fast.exact_model_numerator(p, q, sigma)
    z = F(N, 27*A*B)
    for h, T in (((1, 2, -3), 7), ((3, -5, 6), 14), ((-7, 4, 9), 10),
                 ((1, 1, 1), 1), ((0, 0, 12), 35)):
        poly = lambda x: h[0]*x*x+h[1]*x+h[2]
        L = 27*T*U*V*A*B
        J = T*U*V*N+27*sigma*(V*B*poly(a)-U*A*poly(b))
        assert Q > s2+valuation(h[2], 2)
        assert P > 3+s3+valuation(h[2], 3)
        assert valuation(J, 2) == s2+valuation(h[2], 2)
        assert valuation(J, 3) == 3+s3+valuation(h[2], 3)
        smooth_h = 2**valuation(h[2], 2)*3**valuation(h[2], 3)
        smooth_T = 2**valuation(T, 2)*3**valuation(T, 3)
        T0 = T//smooth_T
        axis = gcd(abs(J), A0*B0)
        e = gcd(abs(J), T0*A0*B0)//axis
        assert T0 % e == 0
        whole_gcd = 27*2**s2*3**s3*smooth_h*e*axis
        assert whole_gcd == gcd(abs(J), L)
        den = L//whole_gcd
        predicted_smooth = F(U*V*smooth_T, smooth_h)
        assert predicted_smooth.denominator == 1
        predicted_off = T0*A0*B0//(e*axis)
        assert gcd(predicted_off, 6) == 1
        assert den == predicted_smooth.numerator*predicted_off
        corrected = z+sigma*(F(poly(a), T*U*A)-F(poly(b), T*V*B))
        assert corrected == F(J, L) and corrected.denominator == den
        rA = T*U*N+27*sigma*B*poly(a)
        rB = T*V*N-27*sigma*A*poly(b)
        gA, gB = gcd(abs(rA), A0), gcd(abs(rB), B0)
        assert gA == gcd(abs(J), A0) and gB == gcd(abs(J), B0)
        cross_ratio = (gA*gB)//axis
        assert gA*gB == axis*cross_ratio and gcd(A0, B0) % cross_ratio == 0
        assert gA == gcd(abs(rA), A1)*gcd(abs(rA), A2)
        assert gB == gcd(abs(rB), B1)*gcd(abs(rB), B2)
        if decompose:
            reduced_poly = lambda x: (h[1]-h[0])*x+h[2]-h[0]
            corrected_residues = (T*U*residues[0]+27*sigma*B*sum(h),
                                  T*U*residues[1]+27*sigma*B*reduced_poly(a),
                                  T*V*residues[2]-27*sigma*A*sum(h),
                                  T*V*residues[3]-27*sigma*A*reduced_poly(b))
            assert all((r-r0) % m == 0 for r, r0, m in
                       zip(corrected_residues, (rA, rA, rB, rB), (A1, A2, B1, B2)))
        if gcd(T, A0*B0) == 1:
            offset = 27*sigma*(V*B*poly(a)-U*A*poly(b))
            synthetic_N = -offset*pow(T*U*V, -1, A0*B0) % (A0*B0)
            synthetic_J = T*U*V*synthetic_N+offset
            assert synthetic_J % (A0*B0) == 0
    print("WHOLE_NUMERATOR_PASS", (p, q), "current_den_bits", z.denominator.bit_length())


if __name__ == "__main__":
    for case in ((5, 8, 12, 19, 1), (12, 19, 41, 65, -1), (53, 84, 306, 485, -1)):
        verify(*case)
    verify(306, 485, 665, 1054, 1, decompose=False)
    print("PASS: full period blocks, four cyclotomic residues, exact whole-model smooth/off-S gcd")
