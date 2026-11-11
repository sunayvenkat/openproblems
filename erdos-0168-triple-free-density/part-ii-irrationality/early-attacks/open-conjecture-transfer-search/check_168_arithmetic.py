"""Compare descending greedy to exact finite no-{n,2n,3n} optima."""
import heapq
import json
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

heap = [1]
seen = {1}
points = []
for _ in range(250):
    v = heapq.heappop(heap)
    points.append(v)
    for w in (2*v, 3*v):
        if w not in seen:
            seen.add(w)
            heapq.heappush(heap, w)

records = []
for count in range(1, len(points)+1):
    present = points[:count]
    selected = set()
    for v in reversed(present):
        if 2*v not in selected or 3*v not in selected:
            selected.add(v)
    triples = [(v,2*v,3*v) for v in present if 3*v <= present[-1]]
    assert all(not all(v in selected for v in t) for t in triples)
    index = {v:i for i,v in enumerate(present)}
    matrix = lil_matrix((len(triples),count))
    for row,t in enumerate(triples):
        for v in t:
            matrix[row,index[v]] = 1
    result = milp(-np.ones(count),integrality=np.ones(count),
                  bounds=Bounds(0,1),
                  constraints=LinearConstraint(matrix.tocsr(),-np.inf,2),
                  options={'time_limit':30})
    if not result.success:
        print(json.dumps({'count':count,'error':result.message}),flush=True)
        break
    opt = {v for i,v in enumerate(present) if result.x[i] > .5}
    assert all(not all(v in opt for v in t) for t in triples)
    assert len(opt) == round(-result.fun)
    record = {'k':count,'t':present[-1],'greedy':len(selected),'F':len(opt)}
    records.append(record)
    if len(selected) < len(opt):
        record['greedyRemoved'] = sorted(set(present)-selected)
        record['optRemoved'] = sorted(set(present)-opt)
        print(json.dumps(record),flush=True)
        break
    if count % 25 == 0:
        print(json.dumps(record),flush=True)

Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2))
