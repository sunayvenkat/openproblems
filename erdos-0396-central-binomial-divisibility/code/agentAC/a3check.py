# Theorem A3 check: large-K sign of digit D_k is sign of -a_{k+1}, where
# a_{k+1} = (-1)^k * d * [x^{delta-1}] (g^k mod f), g = (x^d+1)/Phi_{2d}.
# Predicted first negative level for large K = least k>=1 with (-1)^k [x^{delta-1}](g^k mod f) > 0 (if that
# coefficient is the dominant one).  Compare with piece_good(K*d, d) for several K.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from poly import cyclo, divmod_monic, mul
from fullgood import piece_good
for d in map(int, sys.argv[1:]):
    f = list(cyclo(2 * d)); dl = len(f) - 1
    g, r = divmod_monic([1] + [0] * (d - 1) + [1], f); assert not r
    G = [1]; signs = []
    for k in range(1, 9):
        G = divmod_monic(mul(G, g), f)[1]
        top = G[dl - 1] if len(G) == dl else 0
        signs.append((k, (-1) ** k * top))
    pred = next((k for k, v in signs if v > 0), None)
    print('d', d, 'delta', dl, '(-1)^k [x^{delta-1}](g^k mod f), k=1..8:', [v for _, v in signs])
    print('   predicted large-K first negative level:', pred)
    for K in (3, 5, 7, 9, 31, 101):
        print('   K', K, 'first negative level', piece_good(K * d, d)[0], flush=True)
