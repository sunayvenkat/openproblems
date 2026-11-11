import sys
from verify import run
forms = [(12,-1),(22,9),(11,-1),(12,5)]
for X in (20000, 100000, 300000):
    good, tot, fails, failx = run(forms, X, cls=(6,4))
    print('X', X, 'class x=4 mod 6: good', good, 'of', tot, 'frac %.4f' % (good/tot))
    print('   fails', dict(sorted(fails.items(), key=str)))
