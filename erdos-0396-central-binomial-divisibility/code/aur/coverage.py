# Coverage audit for m2 = 59814755: every divisor d must be (top) or (A1b: phi/d > 2/3, T >= 3)
# or appear in checkB_out.txt as good-L2, or be L2-BAD with a negative level in the deep outputs.
import re, sys
from itertools import combinations
from math import prod
sys.path.insert(0, '../agentV')
from fastgood import phi
m = 59814755; P = [5, 7, 11, 13, 17, 19, 37]
divs = sorted(prod(c) for r in range(len(P) + 1) for c in combinations(P, r))
txt = open('checkB_out.txt', encoding='utf-16').read() if open('checkB_out.txt', 'rb').read(2) in (b'\xff\xfe', b'\xfe\xff') else open('checkB_out.txt').read()
sec = txt.split('m = 50115065')[0]
gl2 = set(map(int, re.findall(r'd=(\d+) .*good-L2', sec))); bad = set(map(int, re.findall(r'd=(\d+) .*L2-BAD', sec)))
deep = {}
for f in ('deep_out1.txt', 'deep_out2.txt', 'deep_out3.txt', 'lev319865.txt'):
    raw = open(f, 'rb').read(); s = raw.decode('utf-16') if raw[:2] in (b'\xff\xfe', b'\xfe\xff') else raw.decode()
    for d, lv in re.findall(r'd=(\d+) .*first negative level (\d+)', s): deep[int(d)] = int(lv)
    if f.startswith('lev'):
        for lv, c in re.findall(r's=(\d+) offset \d+ coeff (-\S+)', s): deep[319865] = int(lv)
cls = {}
for d in divs:
    T = m // phi(d)
    if d == m: cls[d] = 'top'
    elif 3 * phi(d) > 2 * d: cls[d] = 'A1b' if T >= 3 else 'A1b-NO-LEVEL2'
    elif d in gl2: cls[d] = 'good-L2'
    elif d in bad: cls[d] = f'deep L{deep[d]}' if d in deep else 'BAD-UNRESOLVED'
    else: cls[d] = 'MISSING'
from collections import Counter
print(len(divs), Counter(v.split()[0] if v.startswith('deep') else v for v in cls.values()))
print('problems:', [(d, v) for d, v in cls.items() if v in ('MISSING', 'BAD-UNRESOLVED', 'A1b-NO-LEVEL2')])
