"""Reconstruct and verify an exact rational invariant SOS certificate.

All coefficient checks and positive-definiteness decisions use exact integers
and fractions. NumPy/SciPy select correction coordinates during discovery only.
"""

from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import sys
import time

spec = importlib.util.spec_from_file_location("invariant", Path(__file__).with_name("marcus-invariant-sdp.py"))
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)
np, la, sp = engine.np, engine.la, engine.sp


def coefficient_matrices(data):
    m, r, degree = data["m"], data["dimension"], data.get("degree", 2)
    lookup, target, reps = engine.orbits_and_target(m, degree)
    answer = []
    for cut in data["cuts"]:
        nets, left, right = engine.networks(m, cut, degree)
        assert json.loads(json.dumps(nets)) == data["networks"][str(cut)]
        entries = [[] for _ in target]
        for i, a in enumerate(nets):
            for j in range(i, len(nets)):
                table, loops = engine.inner_diagram(a, nets[j], m, left + right, cut, degree)
                orbit, value = lookup[table], r ** loops
                entries[orbit].append((i, j, value))
                if i != j:
                    entries[orbit].append((j, i, value))
        matrices = []
        for items in entries:
            if items:
                rows, cols, values = zip(*items)
                matrices.append(sp.csc_matrix((values, (rows, cols)), shape=(len(nets), len(nets)), dtype=np.int64))
            else:
                matrices.append(sp.csc_matrix((len(nets), len(nets)), dtype=np.int64))
        for block in data["blocks"]:
            if not block["name"].startswith(f"cut{cut}/"):
                continue
            raw = np.array(block["basis"], dtype=np.int64)
            # This explicit bound guarantees no intermediate int64 overflow.
            bound = int(np.max(np.abs(raw))) ** 2 * r ** m * len(nets) ** 2
            assert bound < 2 ** 63
            answer.append([raw.T @ matrix @ raw for matrix in matrices])
    return answer, [int(x) for x in target]


def coordinates(blocks):
    return [(b, i, j) for b, block in enumerate(blocks)
            for i in range(len(block["gram"])) for j in range(i, len(block["gram"]))]


def exact_ldl(matrix):
    n = len(matrix)
    lower = [[F(i == j) for j in range(n)] for i in range(n)]
    diagonal = []
    for j in range(n):
        pivot = matrix[j][j] - sum(lower[j][k] ** 2 * diagonal[k] for k in range(j))
        assert pivot > 0, (j, float(pivot))
        diagonal.append(pivot)
        for i in range(j + 1, n):
            lower[i][j] = (matrix[i][j] - sum(lower[i][k] * lower[j][k] * diagonal[k] for k in range(j))) / pivot
    return min(float(x) for x in diagonal)


def verify(data, coefficients=None, target=None):
    if coefficients is None:
        coefficients, target = coefficient_matrices(data)
    matrices = [[[F(x) for x in row] for row in block["gram"]] for block in data["blocks"]]
    reconstructed = [F(0) for _ in target]
    minimum_pivot = float("inf")
    for b, (block, matrix, coefs) in enumerate(zip(data["blocks"], matrices, coefficients)):
        assert all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))
        pivot = exact_ldl(matrix)
        minimum_pivot = min(minimum_pivot, pivot)
        print(json.dumps({"verified_block": block["name"], "order": len(matrix), "minimum_LDL_pivot_approx": pivot}), flush=True)
        for o in range(len(target)):
            reconstructed[o] += sum(int(coefs[o][i, j]) * matrix[i][j] * (1 if i == j else 2)
                                    for i in range(len(matrix)) for j in range(i, len(matrix)))
    assert reconstructed == target, [(i, str(x-F(t))) for i, (x,t) in enumerate(zip(reconstructed, target)) if x != t]
    return {"exact_coefficient_equations": len(target), "positive_definite_gram_blocks": len(matrices),
            "minimum_LDL_pivot_approx": minimum_pivot, "exact_verified": True}


def reconstruct(path):
    import sympy as sy
    data = json.loads(Path(path).read_text())
    coefficients, target = coefficient_matrices(data)
    coords = coordinates(data["blocks"])
    system = np.array([[int(coefficients[b][o][i,j]) * (1 if i == j else 2) for b,i,j in coords] for o in range(len(target))], dtype=np.int64)
    _, qr, pivots = la.qr(system.astype(float), pivoting=True, mode="economic")
    rank = int(np.sum(np.abs(np.diag(qr)) > np.max(np.abs(qr)) * 1e-10))
    selected = [int(x) for x in pivots[:rank]]
    sub = sy.Matrix(system[:, selected].tolist())
    rows = list(sub.T.rref()[1])
    assert len(rows) == rank
    square = sub[rows, :]
    denominator = 10 ** 24
    values = [F(round(F(str(data["blocks"][b]["gram"][i][j])) * denominator), denominator) for b,i,j in coords]
    residual = [F(t) - sum(int(a) * v for a,v in zip(row, values)) for t,row in zip(target,system)]
    correction = square.inv() * sy.Matrix([sy.Rational(residual[o].numerator, residual[o].denominator) for o in rows])
    for column, delta in zip(selected, correction):
        values[column] += F(int(delta.p), int(delta.q))
    for (b,i,j), value in zip(coords, values):
        data["blocks"][b]["gram"][i][j] = str(value)
        data["blocks"][b]["gram"][j][i] = str(value)
    data["certificate_type"] = "exact rational positive-definite Gram matrices and integer tensor bases"
    data["reconstruction"] = {"linear_rank": rank, "rounding_denominator": str(denominator), "corrected_coordinates": selected}
    data["verification"] = verify(data, coefficients, target)
    for key in ("status", "seconds", "objective", "max_residual", "minimum_eigenvalue"):
        data.pop(key, None)
    for block in data["blocks"]:
        block.pop("eigenvalues", None)
    suffix = "" if data.get("degree", 2) == 2 else f"-k{data['degree']}"
    out = Path(f"marcus-invariant-exact-{data['m']}-{data['dimension']}{suffix}.json")
    out.write_text(json.dumps(data, separators=(",", ":")))
    print(json.dumps({"certificate": str(out), **data["verification"]}), flush=True)


if __name__ == "__main__":
    started = time.time()
    if sys.argv[1] == "--verify":
        print(json.dumps(verify(json.loads(Path(sys.argv[2]).read_text()))))
    else:
        reconstruct(sys.argv[1])
    print(json.dumps({"seconds": time.time()-started}), flush=True)
