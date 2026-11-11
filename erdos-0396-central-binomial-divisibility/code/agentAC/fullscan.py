# Full goodness (all pieces) for every odd squarefree m <= Mmax whose top piece is good (from topscan output).
import sys, re
from fullgood import full_good
src = sys.argv[1]
tot = ok = 0
for line in open(src):
    if ' top good ' not in line: continue
    m = int(line.split()[0]); tot += 1
    bad = full_good(m)
    ok += not bad
    print(m, re.search(r'\[.*?\]', line).group(0), 'FULLY GOOD' if not bad else 'bad non-top pieces %s' % bad, flush=True)
print('top-good', tot, 'fully good', ok)
