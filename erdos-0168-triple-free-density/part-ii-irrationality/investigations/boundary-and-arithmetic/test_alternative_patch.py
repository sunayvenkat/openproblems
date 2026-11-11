"""Targeted test: can a winning patched class improve without removing its patch?"""
import sys
import json
from pathlib import Path
from itertools import combinations

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / '.research-tools/python'))
sys.path.insert(0, str(HERE.parent / 'Open conjecture transfer search'))
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix
from exact_168_diagonal import smooth_prefix


def certificate(points, corners, j, removed):
    color = {v: (a+2*b) % 3 for v, a, b in points}
    adj = {}
    for edge in corners:
        if any(v in removed for v in edge):
            left = next(v for v in edge if color[v] == (j+1) % 3)
            right = next(v for v in edge if color[v] == (j+2) % 3)
            adj.setdefault(left, set()).add(right)
    match = {}
    def augment(left, seen):
        for right in adj[left]:
            if right not in seen:
                seen.add(right)
                if right not in match or augment(match[right], seen):
                    match[right] = left
                    return True
        return False
    for left in adj:
        augment(left, set())
    inverse = {left: right for right, left in match.items()}
    reached_left = set(adj)-set(inverse)
    reached_right = set()
    queue = list(reached_left)
    for left in queue:
        for right in adj[left]:
            if inverse.get(left) == right or right in reached_right:
                continue
            reached_right.add(right)
            if right in match and match[right] not in reached_left:
                reached_left.add(match[right])
                queue.append(match[right])
    cover = (set(adj)-reached_left) | reached_right
    assert len(cover) == len(match)
    assert all(left in cover or right in cover for left in adj for right in adj[left])
    return {'deficiency': len(removed)-len(match), 'matching': [[l,r] for r,l in match.items()],
            'vertex_cover': sorted(cover)}


points = smooth_prefix(200)
small = [p for p in points if p[0] <= 18]
assert certificate(small, [(v,2*v,3*v) for v,_,_ in small if 3*v<=18], 2, {4,18})['deficiency'] == 0
records = []
for x in (256, 512, 4096):
    t = 6*x
    present = [p for p in points if p[0] <= t]
    j = (x.bit_length()-1) % 3
    classes = [[v for v,a,b in present if (a+2*b)%3 == k] for k in range(3)]
    candidate = [len(c)-(k==j) for k,c in enumerate(classes)]
    if candidate[j] != min(candidate):
        print(json.dumps({'t':t,'skipped':'patch class is not a winner'}), flush=True)
        continue
    corners = [(v,2*v,3*v) for v,_,_ in present if 3*v<=t]
    index = {v:i for i,(v,_,_) in enumerate(present)}
    matrix = lil_matrix((len(corners)+2,len(present)))
    for i,edge in enumerate(corners):
        matrix[i,[index[v] for v in edge]] = 1
    matrix[-2,:] = 1
    patch = {x,9*x//2,6*x}
    matrix[-1,[index[v] for v in patch]] = 1
    lower = np.array([int(a==0 and (a+2*b)%3==j) for _,a,b in present])
    result = milp(np.zeros(len(present)),integrality=np.ones(len(present)),
                  bounds=Bounds(lower,1),constraints=LinearConstraint(matrix.tocsr(),
                    np.r_[np.ones(len(corners)),0,1],
                    np.r_[np.full(len(corners),np.inf),len(classes[j])-1,np.inf]),
                  options={'time_limit':30})
    out = {'t':t,'j':j,'vertices':len(present),'status':result.message}
    if result.success:
        cover = {v for (v,_,_),z in zip(present,result.x) if z>0.5}
        assert len(cover) <= len(classes[j])-1 and cover & patch
        assert all(set(edge)&cover for edge in corners)
        removed = set(classes[j])-cover
        cert = certificate(present,corners,j,removed)
        assert cert['deficiency'] > 0 and not patch <= removed
        out.update({'removed':sorted(removed),**cert})
        # Small witnesses are minimized exhaustively, not merely by greedy deletion.
        if len(removed) <= 18:
            found = None
            for size in range(1,len(removed)+1):
                for subset in combinations(sorted(removed),size):
                    cert = certificate(present,corners,j,set(subset))
                    if cert['deficiency'] > 0:
                        found = {'removed':subset,**cert}
                        break
                if found:
                    break
            out['minimum_inside_witness'] = found
    records.append(out)
    print(json.dumps(out),flush=True)
    if result.success:
        break
(HERE/'alternative_patch_results.json').write_text(json.dumps(records,indent=2))
