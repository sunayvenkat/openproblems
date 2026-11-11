"""Bounded integration checks; largest stored model values remain working inputs."""
from fractions import Fraction as F
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path
import pickle

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent


class DataOnlyUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        raise ValueError(f"Unexpected object in data cache: {module}.{name}")


def cached(name):
    with (HERE / name).open("rb") as handle:
        return DataOnlyUnpickler(handle).load()


def log_interval(d, bits=8192):
    # log((d+1)/(d-1)) = 2 sum 1/((2k+1)d^(2k+1)).
    scale, count, power, total = 1 << bits, bits // 2 + 2, d, 0
    for k in range(count):
        total += (2 * scale) // ((2 * k + 1) * power)
        power *= d * d
    assert 2 * scale * d * d < power * (2 * count + 1) * (d * d - 1)
    return F(total, scale), F(total + count + 1, scale)


def common_cf(lo, hi, limit=None):
    n1, d1, n2, d2 = lo.numerator, lo.denominator, hi.numerator, hi.denominator
    out = []
    while d1 and d2 and (limit is None or len(out) < limit):
        a, r1 = divmod(n1, d1)
        b, r2 = divmod(n2, d2)
        if a != b:
            break
        out.append(a)
        n1, d1, n2, d2 = d1, r1, d2, r2
    return out


l2, u2 = log_interval(3)
l3, u3 = log_interval(2)
alpha_lo, alpha_hi = l2 / u3, u2 / l3
digits = common_cf(alpha_lo, alpha_hi, 600)
assert len(digits) == 600
ps, qs = [0, 1], [1, 0]
for a in digits:
    ps.append(a * ps[-1] + ps[-2])
    qs.append(a * qs[-1] + qs[-2])
convs = list(zip(ps[2:], qs[2:]))


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    x, y = z
    u, v = w
    return x * u - y * v, x * v + y * u - y * v


def wp(k):
    return ((1, 0), (0, 1), (-1, -1))[k % 3]


lower, upper = (0, 1, (1, 0)), (1, 1, (1, 0))
states = {(0, 1): (1, 0), (1, 1): (1, 0)}
for k, a in enumerate(digits[1:], 1):
    for _ in range(a - 1 if k == 1 else a):
        m = (lower[0] + upper[0], lower[1] + upper[1],
             add(lower[2], mul(wp(lower[0] + lower[1]), upper[2])))
        states[m[:2]] = m[2]
        if k % 2:
            upper = m
        else:
            lower = m

balanced = {(0, 1, (1, 0)), (1, 1, (1, 0)), (2, 0, (2, 1)), (2, 2, (2, 0))}
resonant = {(1, 2, (1, 1)), (2, 1, (1, 0))}
eligible_count = large_count = joint_res = joint_bal = 0
for n in range(3, 592):
    p, q = convs[n]
    pp, qq = convs[n + 1]
    r, s = p + pp, q + qq
    state = (r % 3, s % 3, states[(r, s)])
    nonres = (p + q) % 3 != 0
    eligible = nonres and state in balanced | resonant
    prediction = nonres and (p + q + pp + qq) % 3 == 0
    assert prediction == (nonres and state in resonant)
    eligible_count += eligible
    large_count += digits[n + 1] >= 5
    if eligible and digits[n + 1] >= 5:
        joint_res += state in resonant
        joint_bal += state in balanced
assert (eligible_count, large_count, joint_res, joint_bal) == (159, 168, 38, 1)
print("Exact log intervals certify 600 alpha digits; 589 indices reproduce 159 eligible, 168 large, 39 joint (38 resonant, 1 balanced)", flush=True)

from fastmodel import model_value
from resmodel import model_value as resonant_value

models = {k: F(*v) for k, v in cached("models.pkl").items()}
assert all(k in convs for k in models)
spec = spec_from_file_location("archived_model", NOTES / "Erdos 168 reflected return models/two_sided_models_check.py")
archived = module_from_spec(spec)
spec.loader.exec_module(archived)
for p, q in [(5, 8), (12, 19), (41, 65), (53, 84)]:
    for sign in (-1, 1):
        value = F(*model_value(p, q, sign))
        assert value == archived.model(p, q, sign)[4]
    correct = 1 if 2**q > 3**p else -1
    assert F(*model_value(p, q, correct)) == models[(p, q)]
assert F(*model_value(15601, 24727, 1)) == models[(15601, 24727)]
rz, _, _ = resonant_value(665, 1054)
assert rz == models[(665, 1054)] == F(*cached("res1054.pkl"))
print("Fast evaluator matches archived small models on both sides; q=24727 and resonant q=1054 caches reproduced", flush=True)


@lru_cache(None)
def phi(n, base):
    value = base**n - 1
    for d in range(1, n):
        if n % d == 0:
            factor = phi(d, base)
            assert value % factor == 0
            value //= factor
    return value


for (p, q), value in models.items():
    if (p + q) % 3 == 0:
        continue
    D = 27 * (2**(3 * q) - 1) * (3**(3 * p) - 1)
    assert D % value.denominator == 0
    N = value.numerator * (D // value.denominator)
    for factor in (phi(3 * q, 2), phi(3 * p, 3)):
        assert value.denominator % factor == 0 and gcd(N, factor) == 1
print("Eight cached actual nonresonant models retain both full tested cyclotomic factors; q=176251 value not cached/recomputed", flush=True)


def error(p, q):
    n = convs.index((p, q))
    pp, qq = convs[n + 1]
    return 9 * (F(1, 2**(q + qq)) + F(1, 3**(p + pp)) - F(1, 2**(q + qq) * 3**(p + pp)))


best = (79335, 125743)
zb, eb = models[best], error(*best)
assert F(1, 2**301990) < eb < F(1, 2**301989)
assert abs(rz - zb) + eb < F(1, 2**63973)
print("Full best-model radius is between 2^-301990 and 2^-301989; resonant-model error is below 2^-63973", flush=True)
for key, value in models.items():
    if key != best:
        assert abs(value - zb) > eb
print("Later-model interval excludes equality Z=z_n at n=4,...,11 (use |z_n-z_best|>eps_best, without eps_n)", flush=True)

# The first mediant at n=12 is resonant. Use the archived |jump| > gap/2,
# and the complete two-child Farey variation, rather than recomputing n=13.
p, q = best
pp, qq = convs[13]
r, s = p + pp, q + qq
assert (r + s) % 3 == 0
assert abs(3**r - 2**s) * 2**60 > 2 * 3**r


def variation(a, b, c, d):
    A, B = b + d, a + c
    return 9 * (F(2, 2**A) * (1 + F(A + 1, b * d))
                + F(1, 3**B) * (F(3, 2) + F(6 * B + 3, 4 * a * c)))


assert variation(p, q, r, s) + variation(r, s, pp, qq) < F(1, 2**(s + 60))
print("n=12 nonvanishing also certified by resonant-mediant jump exceeding both complete child variations", flush=True)

prefix = common_cf(zb - eb, zb + eb)
assert prefix == cached("zcf_best.pkl") and len(prefix) == 71933
assert max(prefix).bit_length() == 27607 and prefix.index(max(prefix)) == 10707
pm2, pm1, qm2, qm1 = 0, 1, 1, 0
for k, a in enumerate(prefix):
    pm2, pm1, qm2, qm1 = pm1, a * pm1 + pm2, qm1, a * qm1 + qm2
    if k == 10706:
        assert F(pm1, qm1) == rz
assert qm1.bit_length() == 150991
print("Stored best-model enclosure reproduces 71933 common Z CF terms, 27607-bit a_10707, final convergent denominator 150991 bits", flush=True)
print("Conditional rational-denominator exclusion: den(Z)>=2^150990 and den(c)>=den(Z)", flush=True)

# Exact necessary denominator bounds at the one finite test index; not a minimum
# construction and not a refutation of an eventual asymptotic hypothesis.
for slack in (0, 20, 60):
    E = 569 - slack
    target = 1 << E
    qm2, qm1 = 1, 0
    for k, a in enumerate(prefix[:-1]):
        qm2, qm1 = qm1, a * qm1 + qm2
        if qm1 * qm1 * (prefix[k + 1] + 2) >= target:
            break
    assert qm1 > 2**252 and 2**504 < (1 << (E - 1))
print("At q=84 and slacks 0,20,60, Legendre/CF necessary bounds exclude denominator <=2^(3q); this is a finite obstruction only", flush=True)
print("PASS: selected exact checks complete; no infinite supply established and no largest-model rerun", flush=True)
