"""Test substitutions of a known bad boundary that remove 11 and 222."""
from cover_words import *

old = '122112211222'
for one, two in [('12', '122'), ('21', '221'), ('122', '12'), ('221', '21')]:
    word = ''.join(one if d == '1' else two for d in old)
    assert '11' not in word and '222' not in word
    for last in (1, 2):
        rows = [last]
        for d in reversed(word):
            rows.append(rows[-1]+int(d))
        rows.reverse()
        points, corners = instance(rows)
        pairs = [pair_matching(points, corners, *p) for p in ((0, 1), (0, 2), (1, 2))]
        matrix = lil_matrix((len(corners)+1, len(points)))
        for i, edge in enumerate(corners):
            matrix[i, list(edge)] = 1
        matrix[-1, :] = 1
        result = milp(np.zeros(len(points)), integrality=np.ones(len(points)),
                      bounds=Bounds(0, 1), constraints=LinearConstraint(matrix.tocsr(),
                          np.r_[np.ones(len(corners)), 0],
                          np.r_[np.full(len(corners), np.inf), min(pairs)-1]),
                      options={'time_limit': 45})
        out = {'one': one, 'two': two, 'rows': rows, 'drops': word,
               'vertices': len(points), 'pairs': pairs, 'status': result.message}
        if result.success:
            cover = [i for i, x in enumerate(result.x) if x > 0.5]
            assert len(cover) < min(pairs)
            assert all(any(i in cover for i in edge) for edge in corners)
            out['cover'] = [[points[i][1], points[i][2]] for i in cover]
            Path(__file__).with_name('cover_word_counterexample.json').write_text(json.dumps(out, indent=2))
            print(json.dumps(out), flush=True)
            break
        print(json.dumps(out), flush=True)
    else:
        continue
    break
