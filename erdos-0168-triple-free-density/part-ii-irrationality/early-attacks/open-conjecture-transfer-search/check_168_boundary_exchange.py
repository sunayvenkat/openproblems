"""Find checked exchanges improving a color cover near the sloped boundary.

Coordinates i may be negative; multiply all weights by a sufficiently large
power of 2 to obtain an ordinary finite 3-smooth domain. Outside the mutable
band the cover is fixed to one color. Only witnesses, not floating MIP bounds,
are used to certify improvements.
"""
import argparse
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

parser = argparse.ArgumentParser()
parser.add_argument('--height',type=int,default=40)
parser.add_argument('--width',type=int,default=5)
args = parser.parse_args()
B,H = args.height,args.width

def weight(p):
    i,b = p
    return Fraction(3**b * 2**max(0,i),2**max(0,-i))

all_points = []
thresholds = {Fraction(1)}
for b in range(B+2):
    exponent = (3**b).bit_length()-1
    thresholds.add(Fraction(3**b,2**exponent))
    if b <= B:
        all_points += [(i,b) for i in range(-exponent-H,-exponent+1)]

records=[]
nonoptimal=[]
solves=0
for step,r in enumerate(sorted(thresholds)):
    points = [p for p in all_points if weight(p)<=r]
    index = {p:i for i,p in enumerate(points)}
    anchors=set()
    for i,b in points:
        anchors.update([(i,b),(i-1,b)])
        if b: anchors.add((i,b-1))
    triples=[]
    for i,b in anchors:
        if 3*weight((i,b))<=r:
            triples.append(((i,b),(i+1,b),(i,b+1)))
    for color in range(3):
        baseline={p for p in points if (p[0]+2*p[1])%3==color}
        needed=[triple for triple in triples if not any(p not in index and (p[0]+2*p[1])%3==color for p in triple)]
        matrix=lil_matrix((len(needed),len(points)))
        for row,triple in enumerate(needed):
            for p in triple:
                if p in index: matrix[row,index[p]]=1
        result=milp(np.ones(len(points)),integrality=np.ones(len(points)),
                    bounds=Bounds(0,1),constraints=LinearConstraint(matrix.tocsr(),1,np.inf),
                    options={'time_limit':15})
        solves += 1
        if not result.success:
            nonoptimal.append({'r':str(r),'color':color,'status':result.message})
        if result.x is None:
            print(json.dumps({'r':str(r),'color':color,'status':result.message}),flush=True)
            continue
        cover={p for p,x in zip(points,result.x) if x>.5}
        assert all(any((p in cover if p in index else (p[0]+2*p[1])%3==color) for p in triple) for triple in triples)
        gain=len(baseline)-len(cover)
        # Known reductions in relative coordinates: isolated top power1;
        # the 3-to-2 exchange has r in [3/2,27/16), x=1/4, color1.
        known=int((r<Fraction(3,2) and color==0) or (Fraction(3,2)<=r<Fraction(27,16) and color==1))
        if gain>known:
            rec={'height':B,'width':H,'r':str(r),'color':color,'gain':gain,'known':known,
                 'removed':sorted(baseline-cover),'added':sorted(cover-baseline),'status':result.message}
            records.append(rec)
            print(json.dumps(rec),flush=True)
            Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2))
    if step%20==0:
        print(json.dumps({'step':step,'thresholds':len(thresholds),'done_r':str(r)}),flush=True)
summary={'height':B,'widthParameter':H,'thresholds':len(thresholds),'solves':solves,
         'unexpectedExchanges':len(records),'nonoptimal':nonoptimal}
print(json.dumps(summary),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2))
Path(__file__).with_name('168_boundary_exchange_summary.json').write_text(json.dumps(summary,indent=2))
