import json
import os
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

limit=10**12
points=[]
a=0
while 2**a<=limit:
    b=0
    while 2**a*3**b<=limit:
        points.append((2**a*3**b,a,b))
        b+=1
    a+=1
points.sort()
records=[]
for count,(t,_,_) in enumerate(points,1):
    if count<3: continue
    present=points[:count]
    index={v:i for i,(v,a,b) in enumerate(present)}
    triples=[(index[v],index[2*v],index[3*v]) for v,a,b in present if 3*v<=t]
    matrix=lil_matrix((len(triples),count))
    for i,triple in enumerate(triples): matrix[i,list(triple)]=1
    result=milp(np.ones(count),integrality=np.ones(count),bounds=Bounds(0,1),constraints=LinearConstraint(matrix.tocsr(),1,np.inf),options={'time_limit':20})
    if not result.success:
        print(json.dumps({'t':t,'status':result.message}),flush=True)
        break
    cover=[present[i][0] for i,x in enumerate(result.x) if x>0.5]
    assert all(any(present[i][0] in cover for i in triple) for triple in triples)
    assert len(cover)==round(result.fun)
    used={i for triple in triples for i in triple}
    classes=[sum((a+2*b)%3==c and i in used for i,(v,a,b) in enumerate(present)) for c in range(3)]
    patched=classes[:]
    for a in range(2, t.bit_length()):
        x=2**a
        if 6*x <= t and 4*t < 27*x:
            patched[a%3]-=1
    record={'t':t,'size':count,'tau':len(cover),'mod3':classes,'patched':patched,'cover':cover}
    records.append(record)
    if len(cover)<min(patched):
        print(json.dumps(record),flush=True)
        break
    if count%20==0: print(json.dumps({'t':t,'size':count,'tau':len(cover)}),flush=True)
Path(__file__).with_name('168_diagonal_results.json').write_text(json.dumps(records,indent=2))
