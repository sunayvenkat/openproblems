# Independent fractional capacity audit

## Are the sharp fractional torus thresholds rigorously certified?

### Takeaway

**PASS.** The two prescribed period-six fractional classes first fail their necessary optimal-head capacity constraints at exactly `6561` and `3057647616`. Both node-potential certificates and all unreduced72-column Farkas inequalities reconstruct independently. The earlier witnesses prove firstness only for this necessary-capacity problem, not for complete rational repairs. — [Independent checker](fractional_capacity_audit_check.py), [capacity theorem under audit](fractional_capacity.md).

### Cited Findings

- Both supplied scripts pass under the verified Python3.14 executable with `-B`. The independent checker also passes and imports no geometric/count/profile helper from any supplied checker. It rebuilds the physical triangles from their coordinatewise minima and evaluates every partial profile directly. — [Independent source](fractional_capacity_audit_check.py), [supplied fractional replay](fractional_capacity_check.py), [supplied local replay](obstruction_check.py).
- The audit reproduces exactly50 and53 surviving types after all actual zero-surplus constraints, negative potential totals `-2,-3`, nonnegative potential sums on every survivor, and nonnegative full Farkas coefficients on all72 original variables. Every listed multiplier is positive and its actual surplus is zero. — [Independent periodic replay](fractional_capacity_audit_check.py).
- The first head contains51 distinct actual arrival events through6561; the second contains309 through3057647616. Their preceding events are6144 and2902376448. The specified twelve-type covers have node coverage one and satisfy every joint capacity constraint at all50 and308 respectively earlier events. The retimed `27/2` event is included. — [Independent event and witness assertions](fractional_capacity_audit_check.py).
- For the second case, the displayed sets `S,T` have cardinalities15 and2, and every surviving triangle obeys `|e intersect S|-|e intersect T|<=1`. This is checked using independently reconstructed type masks and zero-surplus support. — [Independent signed Hall replay](fractional_capacity_audit_check.py), [explicit sets](fractional_capacity.md).

### Inferences

**Geometry completeness.** A wholly quadrant-contained triple has a nonnegative coordinatewise minimum. If some member has arrived by a head cutoff `X`, both coordinates of that member are bounded by `floor(log_2 X),floor(log_3 X)`, since every retiming is forward. The triple's coordinatewise minimum satisfies the same bounds. For each anchor residue and orientation the audit enumerates exactly the corresponding minimum residues modulo six inside this finite rectangle, adds the normalized shape, and retains every triple with an arrived member. Its maximum uses all three actual arrivals, including members beyond `X`. Thus it does not omit partial triples or inherit the original token-to-anchor enumeration. — [Independent construction](fractional_capacity_audit_check.py).

**Necessary capacity with fractional mass.** Let `G_B` be completed retained bulk mass, `P_j` its arrived incomplete mass in color j, and `R_j` arrived residual mass. Marginal conservation gives `T_j=G_B+P_j+R_j`; any complete repair satisfies `G<=G_B+R_j`. Hence

```
tau-G >= P_j-(T_j-tau).
```

If `T_j=tau`, exact optimality forces `P_j=0`. Every term in `P_j=sum_k P_k,j x_k` is nonnegative, so an actually incomplete type has weight zero at such a cutoff. This inference is valid for arbitrary nonnegative real weights. The audited certificates never infer zero weight from a strictly positive surplus. — [Capacity derivation](fractional_capacity.md), [independent profile replay](fractional_capacity_audit_check.py).

**Farkas direction and all original variables.** If `h_k` is the sum of node potentials on type k and the listed zero-surplus rows have multipliers `mu>=0`, the audit checks `h_k+sum mu P_k,j>=0` for every original k. Coverage one would make the scalar value of this expression at most the negative potential total, because all added capacity right-hand sides vanish. Nonnegative weights make its scalar value nonnegative. This is a contradiction without integer assumptions, rationality assumptions, an optimizer, or omitted banned variables. — [Full-column assertions](fractional_capacity_audit_check.py).

**Firstness.** The fixed earlier covers satisfy all joint capacity constraints at every preceding actual event, not just individual filters. Counts and profiles are constant between events. They therefore prove fractional feasibility for every earlier real head, while the dual excludes the threshold and every later head. In the second case the same dual reads `13=|S|-|T|<=sum_e x_e=12`, since each of36 nodes has coverage one and each triangle has three vertices. — [Independent witness and Hall checks](fractional_capacity_audit_check.py).

### Gaps

- Necessary-capacity feasibility does not establish balanced strip flux, balanced finite corners, a complete coupling, rational costs, or cheap denominators. No such conclusion is attributed to the preceding witnesses. — [Scope retained from the source](fractional_capacity.md).
- The period-six negative results concern exactly the two bases and their72 specified types. They do not exclude other bases, extra shapes, or larger periods. — [Audited geometry](fractional_capacity_audit_check.py).

## Does the two-event obstruction really remove the period assumption?

### Takeaway

**PASS in the stated retained-bulk class.** For basis `(8,-5),(3,-2)`, arbitrary nonnegative spatial weights on the two prescribed shapes cannot match the actual optimum at both839808 and995328. Every completed valid repair retaining all wholly contained weighted triangles has `M-Q>=13/214990848`. No periodicity or rationality is used. — [Independent local certificate](fractional_capacity_audit_check.py), [local theorem](obstruction.md).

### Cited Findings

- All six physical triangles incident to `z=(12,5)` are distinct and wholly quadrant-contained. The two groups are exactly `{1,5}` and `{0,2,3,4}` in the source's numbering. — [Independent incidence enumeration](fractional_capacity_audit_check.py), [displayed six triangles](obstruction.md).
- The arrived counts at839808 and995328 are exactly `(46,46,46)` and `(48,47,47)`. The next actual events are884736 and1062882. Color2 has zero surplus on the first interval; color1 has zero surplus on the second. — [Independent exact counts](fractional_capacity_audit_check.py).
- Edges1 and5 contain an arrived color2 vertex at839808 and remain incomplete throughout `[839808,884736)`. Edges0,2,3,4 contain an arrived color1 vertex at995328 and remain incomplete throughout `[995328,1062882)`. The independent assertions check incompleteness through each entire interval, not merely at its left endpoint. — [Independent interval checks](fractional_capacity_audit_check.py).

### Inferences

Let the six incident weights be `w_0,...,w_5`, with sum one by whole-plane token marginal coverage. The capacity inequality above gives deficits at least `w_1+w_5` on the first interval and at least `w_0+w_2+w_3+w_4` on the second. The intervals are disjoint, so integrating does not double count a deficit. Their two reciprocal lengths are

```
1/839808-1/884736 =13/214990848,
1/995328-1/1062882=139/2176782336.
```

The first is smaller. Integrating `tau-G` and using the incident weights' sum one proves the stated bound. The positive integrands justify the comparison even for arbitrary infinite fractional repairs. Exact agreement at both left endpoints would instead force both groups' weights to zero, immediately contradicting coverage one. — [Exact reciprocal differences and incidence partition](fractional_capacity_audit_check.py), [general integrated support lemma](obstruction.md).

### Gaps

- Coverage one on the whole plane and retaining every wholly contained weighted triangle are indispensable. A method allowed to discard contained triangles and give their mass directly to a free residual repair falls outside the theorem. — [Explicit audited hypotheses](obstruction.md).
- The statement excludes an optimal head **through**995328 inclusively; a convention requiring equality only for `t<X` is excluded when `X>995328`. This endpoint distinction does not alter the positive integrated cost bound. — [Audited cutoff and interval assertions](fractional_capacity_audit_check.py).
- This fixed-basis real gap gives no reduced-denominator lower bound or infinite-family impossibility. No analogous period-free theorem for the second basis is supplied. — [Source limitations](obstruction.md).

## What remains open after the audit?

### Takeaway

No substantive erratum was found in these two obstruction packages. They close the proposed fractional escape for the two named period-six examples and establish a broader same-shape obstruction for the first basis. They do not supply the adequate infinite arithmetic return needed for irrationality. — [Audited periodic theorem](fractional_capacity.md), [audited local theorem](obstruction.md), [existing arithmetic target](../farey-transport-corrections/REPORT.md).

### Cited Findings

- The validation consists of both supplied checkers plus the separate normalized-geometry checker, and the written conservation, duality, firstness and integration arguments above. All pass in their stated finite/model scopes. — [Independent exact certificate](fractional_capacity_audit_check.py).

### Inferences

- A next attempt must change some unexcluded structure or prove an actual infinite feasibility theorem; neither an optimizer's status nor a feasible capacity profile alone completes the arithmetic argument. — [Scope of the two source results](fractional_capacity.md), [remaining arithmetic requirement](../farey-transport-corrections/REPORT.md).

### Gaps

- Not checked: Lean, external acceptance, priority, broader basis/shape/period classes, or new infinite feasibility. No prior folder was modified. Material risk: promoting the exact finite or retained-bulk obstruction into a universal impossibility or an irrationality proof.
