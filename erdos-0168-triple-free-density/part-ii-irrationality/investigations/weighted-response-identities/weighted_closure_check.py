"""Exact finite certificates for actual response shift identities."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util

SOURCE = Path(__file__).resolve().parents[1] / 'Erdos 168 response closure tests/response_relations_check.py'
spec = importlib.util.spec_from_file_location('accepted_responses', SOURCE)
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def arrays(width):
    aa, bb = r.axes(width)
    result = {}
    for a in range(width):
        for b in range(4, width):
            z = r.sub(r.add(r.add(aa[a], bb[b]), r.CORRECTION[a % 3][b % 3]), (1, 0))
            z = r.sub(z, r.event(b))
            target = 1 - 3 * int(z[0] <= 0 and z[0] - z[1] <= 0)
            result[a, b] = (target,) + tuple(r.response(state, a, b, aa, bb)[0] for state in r.STATES)
    return result


def shift_rank(data, shifts, width, prime=1000003):
    columns = [('constant', 0, 0)] + [(j, u, v) for j in range(5) for u, v in shifts]
    basis, witnesses = {}, []
    for a in range(width):
        for b in range(4, width):
            raw = [1] + [data[a + u, b + v][j] for j, u, v in columns[1:]]
            row = [x % prime for x in raw]
            for pivot, known in sorted(basis.items()):
                factor = row[pivot]
                if factor:
                    row = [(x - factor * y) % prime for x, y in zip(row, known)]
            pivot = next((j for j, value in enumerate(row) if value), None)
            if pivot is not None:
                inverse = pow(row[pivot], -1, prime)
                basis[pivot] = [x * inverse % prime for x in row]
                witnesses.append((a, b))
                if len(basis) == len(columns):
                    return len(basis), columns, witnesses
    return len(basis), columns, witnesses


def determinant(matrix):
    matrix = [row[:] for row in matrix]
    previous, sign = 1, 1
    for k in range(len(matrix) - 1):
        pivot = next(i for i in range(k, len(matrix)) if matrix[i][k])
        if pivot != k:
            matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
            sign = -sign
        value = matrix[k][k]
        for i in range(k + 1, len(matrix)):
            for j in range(k + 1, len(matrix)):
                numerator = matrix[i][j] * value - matrix[i][k] * matrix[k][j]
                assert numerator % previous == 0
                matrix[i][j] = numerator // previous
            matrix[i][k] = 0
        previous = value
    return sign * matrix[-1][-1]


if __name__ == '__main__':
    width = 100
    data = arrays(width + 7)
    for label, indices, expected in (
            ('unit and full color period', range(4), 8649772697327523432457189461277550575610520),
            ('color preserving blocks', (0, 3, 6), -259979518176473365480584)):
        shifts = [(u, v) for u in indices for v in indices]
        rank, columns, witnesses = shift_rank(data, shifts, width)
        assert rank == len(columns)
        matrix = [[1] + [data[a + u, b + v][j] for j, u, v in columns[1:]] for a, b in witnesses]
        det = determinant(matrix)
        assert det == expected and det % 1000003
        # The original colored-board formula independently checks every target entry.
        points = {(a + u, b + v) for a, b in witnesses for u, v in shifts}
        for point in points:
            assert data[point][0] == r.original_c(*point)
        print('PASS:', label, 'rank', rank, 'integer determinant', det)
        print('Witnesses:', witnesses)
    # Finite support makes every omitted boundary visible without a tail estimate.
    for j in range(5):
        finite = {(a, b): data[a, b][j] for a in range(7) for b in range(4, 11)}
        total = sum((F(value, 2 ** a * 3 ** b) for (a, b), value in finite.items()), F(0))
        for u in (0, 1, 3, 6):
            for v in (0, 1, 3, 6):
                shifted = sum((F(finite.get((a + u, b + v), 0), 2 ** a * 3 ** b)
                               for a in range(7) for b in range(4, 11)), F(0))
                col = sum((F(value, 2 ** a * 3 ** b) for (a, b), value in finite.items() if a < u), F(0))
                row = sum((F(value, 2 ** a * 3 ** b) for (a, b), value in finite.items() if b < 4 + v), F(0))
                corner = sum((F(value, 2 ** a * 3 ** b) for (a, b), value in finite.items()
                              if a < u and b < 4 + v), F(0))
                assert shifted == 2 ** u * 3 ** v * (total - col - row + corner)
    print('PASS: complete weighted shift identity on five finite-supported actual arrays')
