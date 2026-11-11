"""Search row-drop words avoiding 11 and 222 for a two-color gap."""
import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / '.research-tools/python'))
sys.path.insert(0, str(ROOT / 'research_notes/Open conjecture transfer search'))
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix
from exact_168_diagonal import exact_tau


def pair_matching(points, corners, c1, c2):
    colors = [(a+2*b) % 3 for _, a, b in points]
    adj = [[] for _ in points]
    for edge in corners:
        left = next(i for i in edge if colors[i] == c1)
        right = next(i for i in edge if colors[i] == c2)
        adj[left].append(right)
    matched = {}
    def augment(left, seen):
        for right in adj[left]:
            if right not in seen:
                seen.add(right)
                if right not in matched or augment(matched[right], seen):
                    matched[right] = left
                    return True
        return False
    return sum(augment(i, set()) for i, c in enumerate(colors) if c == c1)


def shapes(width, rows=(), word=''):
    rows += (width,)
    if width <= 2:
        yield rows, word
    for d in (1, 2):
        newword = word+str(d)
        if width > d and not newword.endswith(('11', '222')):
            yield from shapes(width-d, rows, newword)


def instance(rows):
    points = [(0, a, b) for b, w in enumerate(rows) for a in range(w)]
    index = {(a, b): i for i, (_, a, b) in enumerate(points)}
    corners = [(index[a, b], index[a+1, b], index[a, b+1])
               for b in range(len(rows)-1) for a in range(rows[b+1])]
    return points, corners


if __name__ == '__main__':
    checked = 0
    for width in range(int(sys.argv[1]), int(sys.argv[2])+1):
        for rows, word in shapes(width):
            points, corners = instance(rows)
            pairs = [pair_matching(points, corners, *p) for p in ((0, 1), (0, 2), (1, 2))]
            bound = min(pairs)-1
            matrix = lil_matrix((len(corners)+1, len(points)))
            for i, edge in enumerate(corners):
                matrix[i, list(edge)] = 1
            matrix[-1, :] = 1
            result = milp(np.zeros(len(points)), integrality=np.ones(len(points)),
                          bounds=Bounds(0, 1),
                          constraints=LinearConstraint(matrix.tocsr(),
                              np.r_[np.ones(len(corners)), 0],
                              np.r_[np.full(len(corners), np.inf), bound]),
                          options={'time_limit': 20})
            checked += 1
            if result.success:
                cover = [i for i, x in enumerate(result.x) if x > 0.5]
                assert len(cover) <= bound
                assert all(any(i in cover for i in edge) for edge in corners)
                assert '11' not in word and '222' not in word
                out = {'rows': rows, 'drops': word, 'vertices': len(points),
                       'pair_optima': pairs, 'cover_size': len(cover),
                       'cover': [[points[i][1], points[i][2]] for i in cover],
                       'checked': checked}
                Path(__file__).with_name('cover_word_counterexample.json').write_text(json.dumps(out, indent=2))
                print(json.dumps(out), flush=True)
                sys.exit(0)
            assert result.status == 2, result.message
        print(json.dumps({'width': width, 'checked': checked}), flush=True)
