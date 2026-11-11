"""Exact integer ordering and color discrepancies of 3-smooth prefixes."""
import heapq
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

limit = 10**100
points = []
a, p2 = 0, 1
while p2 <= limit:
    b, v = 0, p2
    while v <= limit:
        points.append((v,a,b))
        b += 1
        v *= 3
    a += 1
    p2 *= 2
points.sort()
colors = [0,0,0]
records = []
spread = -1
previous_f = 0
density = Fraction(0)
bad_increments = []
for k,(v,a,b) in enumerate(points,1):
    colors[(a+2*b)%3] += 1
    cur = max(colors)-min(colors)
    if cur > spread:
        spread = cur
        record = {'k':k,'t':str(v),'a':a,'b':b,'colors':colors.copy(),'spread':spread}
        records.append(record)
        print(json.dumps(record),flush=True)
    adjusted = colors.copy()
    two_exp = v.bit_length()-1
    two = 1 << two_exp
    if 3*two > 2*v:
        adjusted[two_exp%3] -= 1
    patch_exp = (v//6).bit_length()-1
    if patch_exp >= 0:
        patch_two = 1 << patch_exp
        if 6*patch_two <= v and 4*v < 27*patch_two:
            adjusted[patch_exp%3] -= 1
    candidate_f = k-min(adjusted)
    # Small domains have additional isolated vertices, handled directly.
    if v < 3:
        candidate_f = k
    delta = candidate_f-previous_f
    if delta not in (0,1):
        bad_increments.append({'k':k,'t':str(v),'delta':delta})
    density += Fraction(delta,3*v)
    previous_f = candidate_f
print(json.dumps({'last':{'k':len(points),'t':str(points[-1][0]),'colors':colors},'maxSpread':spread}),flush=True)
tail = Fraction(0)
a, p2 = 0, 1
while p2 <= limit:
    p3 = 1
    while p2*p3 <= limit:
        p3 *= 3
    tail += Fraction(3,2*p2*p3)
    a += 1
    p2 *= 2
tail += Fraction(3,p2)
with localcontext() as ctx:
    ctx.prec = 110
    print(json.dumps({'candidateDensity':str(Decimal(density.numerator)/Decimal(density.denominator)),
                      'tailBound':str(Decimal(tail.numerator)/Decimal(3*tail.denominator)),
                      'badIncrements':bad_increments}),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2))
