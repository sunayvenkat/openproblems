# summarize band_*.txt: per m, any piece with no negative level at actual K; kstar histogram; kstar > kex;
# small-K failures; parity of omega(d)
import re, glob
from collections import Counter
rows = {}
for f in sorted(glob.glob('band_[0-9]*.txt')):
    m = f[5:-4]
    for L in open(f):
        if not L.startswith('d='): continue
        d = int(re.search(r'd=(\d+)', L).group(1))
        om = len(re.search(r'\[([^\]]*)\]', L).group(1).split(','))
        g = lambda k: re.search(k + r'=(\S+)', L).group(1)
        bad = re.search(r'badK\(<= 99\)=\[(.*)\]', L).group(1)
        rows[(m, d)] = dict(om=om, th=float(g('th')), K=int(g('K')), kex=int(g('kex')), ks=g('kstar'), first=g('first@K'),
                            bad=[int(x) for x in bad.split(',')] if bad.strip() else [])
for m in sorted({k[0] for k in rows}):
    R = {d: r for (mm, d), r in rows.items() if mm == m}
    print(m, 'pieces', len(R), 'no-negative-at-actual-K:', [d for d, r in R.items() if r['first'] == 'None'],
          'max first level', max((int(r['first']), d) for d, r in R.items() if r['first'] != 'None'))
U = {}
for (m, d), r in rows.items(): U[d] = r
print('distinct band pieces', len(U))
print('kstar histogram', sorted(Counter(r['ks'] for r in U.values()).items()))
print('kstar > kex (needs K-dependent levels):', sorted((d, r['ks'], r['kex']) for d, r in U.items() if r['ks'] != 'None' and int(r['ks']) > r['kex']))
print('pieces with some bad small K (K<=99, coprime, sqfree; -K = undecided):', sorted((d, r['bad']) for d, r in U.items() if r['bad']))
for par in (0, 1):
    S = [r for r in U.values() if r['om'] % 2 == par]
    print('omega(d) %s: n=%d  level-2 good (kstar=2): %d  kstar>=4: %d  some bad K: %d  mean kstar %.2f' % (
        'even' if par == 0 else 'odd', len(S), sum(r['ks'] == '2' for r in S), sum(r['ks'] == 'None' or int(r['ks']) >= 4 for r in S),
        sum(bool(r['bad']) for r in S), sum(int(r['ks']) for r in S if r['ks'] != 'None') / len(S)))
print('by omega: (omega, n, #kstar=2, #kstar>=5 or None, max kstar)')
for om in sorted({r['om'] for r in U.values()}):
    S = [r for r in U.values() if r['om'] == om]
    ks = [99 if r['ks'] == 'None' else int(r['ks']) for r in S]
    print('  ', om, len(S), sum(k == 2 for k in ks), sum(k >= 5 for k in ks), max(ks))
