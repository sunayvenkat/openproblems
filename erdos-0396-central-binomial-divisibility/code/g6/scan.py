# Scan quartic families (route a) -> integer models -> refinement search.  Prints families needing few augmentations.
import sys, itertools
from quartic import family
from qint import integer_models
from refine import search
S, maxaug = int(sys.argv[1]), int(sys.argv[2])
for s in itertools.permutations(range(1, S + 1), 4):
    if s[0] > s[3]: continue
    fam = family(s)
    if not fam or fam[1] == 0: continue
    for sub, n0 in integer_models(*fam[:4], maxopts=3):
        res = search(n0)
        if not res or not res[0]: continue
        (combo, aug), st = res
        if len(aug) <= maxaug:
            print(s, sub, "aug", aug, "e-vectors", [e for e, _ in combo], flush=True)
