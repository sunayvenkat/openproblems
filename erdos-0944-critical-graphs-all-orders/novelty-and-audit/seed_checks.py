"""Independent exact checks of the displayed Kohlmeyer--Kruer seed construction.

Run with Python 3. No external packages. This checks finite instances and the
winding lemma for t <= 3; it is not a proof of the universal seed theorem.
"""
from itertools import product
from math import gcd, prod
from pathlib import Path
import json


def crt(congruences):
    x, modulus = 0, 1
    for residue, new_modulus in congruences:
        assert gcd(modulus, new_modulus) == 1
        x += modulus * ((residue - x) * pow(modulus, -1, new_modulus) % new_modulus)
        modulus *= new_modulus
        assert 0 <= x < modulus
    assert all(x % m == a % m for a, m in congruences)
    return x, modulus


def parameters(r):
    t = r + (int((3 * r + 1) % 5 == 0))
    q, d, kappa, a = 3 * t + 1, [], [], [1]
    D = 30 * q
    for j in range(1, q):
        congruences = [(0, 3), (1, 5 * D - 5)]
        congruences += [(pow(D, -1, di) * (pow(ki, -1, di) + D - 1), di)
                        for di, ki in zip(d, kappa)]
        kj, step = crt(congruences)
        lower = max(6, (2 * q * a[-1] - 1) // D + 2)
        kj += max(0, (lower - kj + step - 1) // step) * step
        dj = D * (kj - 1) + 1
        assert 5 * dj > 10 * q * a[-1]
        assert kj % 15 == 6 and dj % 15 == 1 and gcd(kj, 5 * dj) == 1
        assert all(dj % di == pow(ki, -1, di) for di, ki in zip(d, kappa))
        d.append(dj)
        kappa.append(kj)
        a.append(5 * dj)
    L = 15 * prod(d)
    n, step = crt([(1, 3), (0, q), (4, 5)] +
                  [(-pow(ki, -1, di), di) for ki, di in zip(kappa, d)])
    assert step == q * L
    bound = 1000 * (r + 1) * q * L * L
    n += ((bound - n) // step + 1) * step
    assert bound < n <= bound + step
    assert n % q == 0 and n % 3 == 1 and all(gcd(ai, n) == 1 for ai in a)
    ratios = []
    for i, ai in enumerate(a):
        for j, aj in enumerate(a):
            if i == j:
                continue
            ratio = ai * pow(aj, -1, n) % n
            assert 0 < q * ratio < n and ratio % 3 == 2
            assert ai != aj and ai + aj != n
            for ell in range(4, q + 1, 3):
                assert (ell * ratio % n) % 3 == 2
            ratios.append([i, j, str(ratio)])
    for j, (kj, aj) in enumerate(zip(kappa, a[1:]), 1):
        assert (1 + kj * n) % aj == 0
        assert pow(aj, -1, n) == (1 + kj * n) // aj
    return {"r": r, "t": t, "q": q, "d": d, "kappa": kappa,
            "a": a, "L": L, "n": n, "ratios": ratios}


def generic_class(p, coordinates):
    congruences = [(2, 3), (coordinates[0], 5)]
    congruences += [(e * pow(k, -1, d), d)
                    for e, k, d in zip(coordinates, p["kappa"], p["d"])]
    residue, modulus = crt(congruences)
    assert modulus == p["L"]
    assert all(k * residue % a == e for k, a, e in
               zip(p["kappa"], p["a"][1:], coordinates))
    return residue


def check_words(p):
    r, n, L, a = (p[key] for key in ("r", "n", "L", "a"))
    targets = set(a)
    for h in range(5):
        for end in (False, True):
            es = [2 + 3 * h + 15 * (((d - 1) // 3 - (h > 0)) if end else 0)
                  for d in p["d"]]
            z = generic_class(p, es)
            if z == 0:
                z += L
            assert 0 < 2 * z < n
            targets.add(z)
    certificates = []
    for z in sorted(targets):
        c = 2 if z == 1 else 1
        W = z + c * n
        totals = [aj + k - 2 if z == 1 else 2 * aj - 1 if z == aj
                  else aj + k * z % aj - 1 for k, aj in zip(p["kappa"], a[1:])]
        assert W % 3 == 0
        assert all(M % 3 == 0 and aj < M < 2 * aj and
                   (M - k * W) % aj == 0 for M, k, aj in zip(totals, p["kappa"], a[1:]))
        es = [2 + 15 * ((M // 3 - 2) // 15) for M in totals]
        coords = [es, es, [M - 2 * e for M, e in zip(totals, es)]]
        residues = [generic_class(p, row) for row in coords]
        assert sum(residues) % L == W % L
        low, high = -(-(8 * W - n) // 24), (8 * W + n) // 24
        banned = {z, n - z}
        if n % 2 == 0:
            banned.add(n // 2)
        words = []
        for _ in range(r):
            s1 = residues[0] + ((low - residues[0] + L - 1) // L) * L
            while s1 in banned:
                s1 += L
            s2 = residues[1] + ((low - residues[1] + L - 1) // L) * L
            while s2 in banned or W - s1 - s2 in banned:
                s2 += L
            s3 = W - s1 - s2
            assert low <= s1 <= high and low <= s2 <= high
            word = [s1, s2, s3]
            assert sum(word) % n == z
            for s in word:
                assert 0 < s < n and s not in banned and 2 * s != n
                assert s % 3 == 2
                assert all((k * s % aj) % 3 == 2 for k, aj in zip(p["kappa"], a[1:]))
                for aj in a:
                    normalized = s * pow(aj, -1, n) % n
                    assert normalized in (1, n - 1) or normalized % 3 == 2
            banned.update(word)
            banned.update(n - s for s in word)
            words.append([str(s) for s in word])
        certificates.append({"target": str(z), "words": words})
    return certificates


def winding_checks():
    results = []
    for t in range(4):
        length = 3 * t + 2
        edges = [(i, j) for i in range(length) for j in range(i + 1, length)
                 if (j - i) % 3 == 1]
        checked = qualifying = 0
        for tail in product(range(3), repeat=length - 1):
            colors = (0,) + tail
            checked += 1
            if sum(colors[i] == colors[j] for i, j in edges) > t:
                continue
            qualifying += 1
            increments = [3 if colors[i] == colors[(i + 1) % length] else
                          1 if (colors[(i + 1) % length] - colors[i]) % 3 == 1 else -1
                          for i in range(length)]
            assert sum(increments) <= 3 * t
            assert sum(increments[:-1]) <= 3 * t + 1
        results.append({"t": t, "colorings_up_to_global_color_shift": checked,
                        "colorings_with_at_most_t_bad_edges": qualifying})
    return results


if __name__ == "__main__":
    assert crt([(2, 3), (3, 5)]) == (8, 15)
    results = {"winding": winding_checks(), "instances": []}
    for r in (1, 2):
        p = parameters(r)
        words = check_words(p)
        results["instances"].append({**{k: str(v) if isinstance(v, int) else
                                       [str(x) for x in v] for k, v in p.items()
                                       if k != "ratios"},
                                     "n_digits": len(str(p["n"])),
                                     "L_digits": len(str(p["L"])),
                                     "ratios": p["ratios"], "word_certificates": words})
    out = Path(__file__).with_name("seed-check-results.json")
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"winding": results["winding"],
                      "instances": [{k: v for k, v in x.items() if k in
                                     ("r", "q", "n_digits", "L_digits")}
                                    | {"word_targets": len(x["word_certificates"])}
                                    for x in results["instances"]]}, indent=2))
