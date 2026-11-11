# Exact capacity obstruction for the six-period Farey torus

**The richer prescribed torus class still does not supply the required head.** All 72 translated positive/negative Farey triangle types were tested on the original six-by-six residue torus. Exact integer capacity profiles and an exhaustive exact-cover replay prove obstruction by cutoff6561 for the8/3 basis and3057647616 for the19/27 basis, far before their prescribed targets. Preceding covers satisfy every full joint capacity inequality, so these are the exact first infeasible cutoffs of this finite necessary-capacity problem. No balanced edge flux, rational repair, infinite theorem or general impossibility is inferred. — [Exact replay certificate](torus_bulk_check.py).

## What richer periodic bulk class was actually tested?

### Takeaway

The class includes every original-residue translate of both point-reflected unit Farey triangles, not only translations of the earlier two-triangle partition. An exact cover of its36 residue nodes lifts to a genuine whole-plane three-color coupling. Only wholly quadrant-contained triples are retained for the capacity test. — [Type enumeration and masks](torus_bulk_check.py), [first-round bulk geometry](farey_bulk.md).

### Cited Findings

- The two prescribed bases are `u=(8,-5),v=(3,-2)` and `u=(19,-12),v=(27,-17)`. Each is unimodular and has opposite nonzero color increments. The full-plane index-six construction and actual low-row timing have already been derived. — [Bulk note and certificate](farey_bulk.md).
- The actual token universe keeps color `a-b mod3` and delays dyadic tokens by `3/2`, row-one tokens by `9/8`, with the exact small admissibility exceptions. Its minimum color count is the actual finite optimum. — [Accepted token/minimum input](../hybrid-arithmetic-closure/global_carries.md).
- The new checker is standalone: all actual arrival comparisons are integer/Fraction operations. It imports no prior checker, numerical solver or optimizer. — [Source](torus_bulk_check.py).

### Inferences

For each sign `sigma` in `{+1,-1}` and anchor residue `(a0,b0)` in `{0,...,5}^2`, define a type consisting of all translates by `6Z^2` of

```
{(a0,b0), (a0,b0)+sigma*u, (a0,b0)+sigma*v}.       (TB1)
```

The three residue nodes are distinct, since u,v are unimodular. Their colors are distinct. There are72 types, each a three-node mask on the36-node residue torus. Select12 types whose masks are pairwise disjoint and cover all nodes. Then each original lattice token belongs to exactly one lifted triple. No additional orbit-count or color-supply hypothesis is used. — [Exact type assertions](torus_bulk_check.py).

Type numbering is fixed and reproducible:

```
id =36*s+a0+6*b0,
s=0 for sigma=+1,       s=1 for sigma=-1.         (TB2)
```

For a selected type, keep only triples whose three original coordinates lie in the quadrant. The rest leave uncovered tokens to any proposed boundary repair. This is a larger class than the original six pure translations, but it does not include larger periods, new Farey offsets, arbitrary mixtures, or state-dependent bulk rules. — [Enumeration and clipping implementation](torus_bulk_check.py).

### Gaps

- An exact torus cover by itself gives no balanced edge flux or cheap rational quadrant repair. The original color-cycling proof is not assumed for these arbitrary covers. — [Boundary warning and previous scope](farey_bulk.md).
- No claim about all rational or all near-isotime couplings follows from this finite class. — [Current actual arithmetic requirement](../rational-coupling-construction/REPORT.md).

## Which exact capacity conditions are necessary, and how is infeasibility certified?

### Takeaway

Reserved incomplete bulk triples consume the color surplus available at a cutoff. Every retained type has a nonnegative partial-token profile; if one type alone exceeds a surplus it is forbidden in every admissible selected cover. The resulting integer exact-cover problem is small enough for exhaustive replay, with no reliance on solver status. — [Profile and exact-cover routines](torus_bulk_check.py).

### Cited Findings

- For any complete coupling, its completed count is bounded by the actual minimum color count. The earlier repair work already isolates this rank-capacity issue. — [Actual matching principle](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- The checker enumerates all actual tokens arriving by `2^ceil(5H/2)`, with `H=max(q,s)`, and all distinct actual arrival times up to that bound. This includes simultaneous delayed tokens and the `27/2` arrival. — [Exact token enumeration](torus_bulk_check.py).

### Inferences

Let `T_j(t)` be actual arrived-token counts and `tau(t)=min_j T_j(t)`. For type k, let `K_k,j(t)` count its arrived color-j vertices among retained triples, and let `G_k(t)` count its completed retained triples. Define

```
P_k,j(t)=K_k,j(t)-G_k(t)>=0,
L_j(t)=T_j(t)-tau(t)>=0.                          (TB3)
```

For a selected cover B, the residual color count is `T_j-sum_B K_k,j`. Any residual completion compatible with attaining tau must satisfy

```
sum_(k in B) P_k,j(t) <= L_j(t)
for every cutoff t and color j.                   (TB4)
```

Indeed the bulk already completes `sum_B G_k` triples, so the residual must complete at least `tau-sum_B G_k`. Comparing this requirement with each residual color count gives(TB4). These are necessary even if one allows an ideal residual repair with no rationality or locality restrictions. — [Exact profile construction](torus_bulk_check.py).

All profiles are constant between actual token-arrival times. For a given type, the checker discovers every retained triple having an arrived member by taking each head token's unique compatible anchor; it then includes all three actual arrival times, even if the last lies beyond the target. Thus an incomplete group is not omitted merely because its other members have not arrived. At its last arrival the profile subtracts one in every color, and simultaneous arrivals are aggregated before comparisons. — [Source and nonnegativity assertions](torus_bulk_check.py).

If `P_k,j(t)>L_j(t)` at any tested cutoff, k is individually forbidden. Since every profile is nonnegative, adding other types cannot repair that violation. For each head the checker removes all individually forbidden types, chooses an uncovered residue with fewest compatible masks, and recursively tests every disjoint option. Memoization is sound here because the relaxed remaining problem depends only on the covered-node mask. A returned `None` is a complete finite exhaustive proof that no selected cover can satisfy(TB4). — [Exact recursion `cover_at`](torus_bulk_check.py).

This filter is ordinarily only a relaxation: sums of individually admissible profiles might still exceed a surplus. The final certificates additionally replay the preceding12-type covers against **all joint sums** in(TB4). That extra verification is what permits the exact first-capacity-infeasibility statement below. — [Headline and joint-capacity assertions](torus_bulk_check.py).

### Gaps

- Feasible(TB4) profiles do not establish rationality, balanced strip flux, a finite corner charge or a cheap complete repair. The witnesses below retain that limited status. — [Global repair still required](farey_bulk.md).
- The proof searches integer exact covers of72 types. No untested assertion about fractional hypermatchings is made. — [Explicit search class](torus_bulk_check.py).

## Where does the prescribed torus class first become capacity-infeasible?

### Takeaway

The two exact first thresholds are `6561=3^8` and `3057647616=2^22*3^6`. The preceding witnesses pass every joint inequality, while the next cutoff has no exact cover even under the weaker individual filter. Hence no boundary repair preserving this bulk class can attain the target head in either prescribed example. This is a finite actual-model obstruction, not an infinite family lower bound. — [Complete replay](torus_bulk_check.py).

### Cited Findings

- The prescribed heads are `2^20` and `2^68`. There are respectively124 and1448 distinct actual arrival events below them; the counts remain constant from the last event to the target. — [Exact output](torus_bulk_check.py).
- At the first obstructions the relaxed exact-cover replays visit only20 and4 distinct covered-node states respectively. The script retains every forbidden type's exact cutoff/color/profile/surplus witness. — [Printed finite certificate and assertions](torus_bulk_check.py).

### Inferences

|Basis|First capacity-infeasible cutoff|Previous actual event|Types surviving individual filter|Exhaustive states at obstruction|
|---|---:|---:|---:|---:|
|`(8,-5),(3,-2)`|`6561`|`6144`|50|20|
|`(19,-12),(27,-17)`|`3057647616`|`2902376448`|53|4|

The preceding exact covers, in numbering(TB2), are

```
8/3:   (15,17,70,14,66,13,69,16,71,67,12,68),
19/27: (5,38,3,52,9,50,56,23,27,68,21,70).           (TB5)
```

Each has12 disjoint masks covering all36 residues. The checker verifies every earlier arrival event and every color, with no joint-capacity failure. Between those events the counts are constant. Therefore this necessary-capacity problem is feasible for every earlier real cutoff and infeasible at the displayed next event. The stronger terminology is justified by the full witnesses, not by the individual-filter search alone. — [Exact witness verification](torus_bulk_check.py).

At the prescribed target, the8/3 relaxation leaves only14 types and entirely uncovers residues `{2,3,8,9,30}`; the19/27 relaxation leaves no type. No edge-flux condition was imposed to obtain these negative conclusions. Imposing a valid rational-repair condition can only narrow the class. — [Final target assertions/output](torus_bulk_check.py).

The new thresholds improve on the particular original partition's intrinsic first obstructions, but they remain well before the desired heads. They do not prove that every larger-period or different-offset coupling has an early defect, that every comparison has a large reduced denominator, or that actual irrationality is impossible. The adequate infinite arithmetic return remains unproved. — [Earlier partition repair scope](farey_bulk.md), [actual acceptance conditions](../hybrid-arithmetic-closure/REPORT.md).

### Gaps

- No selected witness in(TB5) is claimed to admit the earlier same-axis rational repair, because its color-cycling period and corner charge were not checked. — [Witness scope](torus_bulk_check.py).
- No additional period sizes or models were searched. Skipped: Lean, external review, installs, broad scans, density decimals and old-file edits. Main risk: promoting the finite72-type necessary-capacity obstruction into a universal impossibility theorem or a rational-repair claim.
