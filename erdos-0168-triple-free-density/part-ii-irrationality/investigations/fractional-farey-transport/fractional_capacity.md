# Exact fractional Farey capacity thresholds

## Can positive fractional weights evade the two integer torus obstructions?

### Takeaway

**No: the first fractional necessary-capacity obstructions are exactly the same cutoffs, 6561 and 3057647616.** Explicit integer node potentials prove infeasibility for arbitrary nonnegative real weights, not only rational or integer weights. The previous twelve-type integer covers are valid fractional witnesses at every earlier actual arrival event. This is an exact finite theorem about the prescribed 72-type, period-six Farey bulk class; it does not establish an obstruction for all couplings or all convergent levels. — [Direct integer certificate replay](fractional_capacity_check.py), [type and profile definitions](../farey-transport-corrections/torus_bulk.md).

### Cited Findings

- The tested bases are `u=(8,-5),v=(3,-2)` with horizontal span `H=8`, and `u=(19,-12),v=(27,-17)` with span `H=27`. Both are unimodular, and their two vector colors are the two nonzero residues modulo three. The two orientations of `{0,u,v}`, each at all36 anchor residues modulo six, give72 types. — [Reference geometry](../farey-transport-corrections/torus_bulk.md).
- Type numbering is `k=36*s+a+6*b`, for `s=0,1` the positive/negative orientation and `0<=a,b<6`. A type contains three distinct residue nodes, one of each color. Node numbering is `j=a+6*b`. — [Enumeration](../farey-transport-corrections/torus_bulk_check.py).
- Actual arrival times are `2^a3^b`, except dyadic tokens with `a>=1` have factor `3/2`, and row-one tokens with `a>=2` have factor `9/8`. Thus token `(2,1)` arrives at `27/2`, which the checker retains exactly. — [Exact arrival/profile implementation](../farey-transport-corrections/torus_bulk_check.py), [current replay](fractional_capacity_check.py).
- The new certificate checker uses only the standard library and integer/Fraction arithmetic. It reuses the archived geometric profile constructor read-only, then checks fixed integer Farkas rows on all72 variables, with no optimizer invocation. — [Current checker](fractional_capacity_check.py).

### Inferences

Let `x_k>=0` be the weight of type k. A whole-plane fractional coupling with token marginal one requires

```
sum_(k containing residue j) x_k = 1,   j=0,...,35.        (FC1)
```

Lift the types by `6Z^2` and retain only triples lying wholly in the quadrant. At an actual cutoff t, let `T_j(t)` be the three arrived-token counts, `tau(t)=min_j T_j(t)`, and `L_j=T_j-tau`. Let `P_k,j(t)>=0` count arrived color-j vertices in incomplete retained triples of type k. Attaining the optimal completed mass through that cutoff requires

```
sum_k P_k,j(t) x_k <= L_j(t).                            (FC2)
```

This is the original capacity proof with completed masses in place of integer completed counts: subtract the weighted completed bulk from each residual color count. It is valid even if the residual repair is allowed arbitrary fractional, nonlocal and nonrational matching. The reference profile constructor enumerates every retained triple with an arrived member, including those completed after the target, and aggregates simultaneous arrivals before comparisons. — [Capacity derivation and exact profile semantics](../farey-transport-corrections/torus_bulk.md).

The essential fractional distinction is that `P_k,j>L_j>0` does **not** force `x_k=0`; it can merely bound the weight. This work uses only rows with `L_j=0`. Nonnegativity then rigorously forces `x_k=0` whenever `P_k,j>0`. No positive-lag integer ban is transferred. — [Zero-lag construction and Farkas checks](fractional_capacity_check.py).

Let `A(t*)` be the types surviving all zero-lag rows up to `t*`. There are50 survivors at `t*=6561` and53 at `t*=3057647616`. Every residue remains incident to some surviving type, so an uncovered-node argument alone would miss the obstruction. Nevertheless each survivor has nonnegative total node potential under the explicit potentials below, while the total node potential is negative. Multiplying (FC1) by those potentials yields the contradiction. — [Survivor assertions and node potentials](fractional_capacity_check.py).

### Gaps

- No fractional or integral global repair is supplied by a necessary-capacity witness alone. In particular, the earlier feasible integer covers are not claimed to have balanced strip flux, balanced finite corners, cheap rational repairs, or any specified arithmetic clearance. — [Scope of prior witnesses](../farey-transport-corrections/torus_bulk.md).
- No assertion about the existence of an adequate infinite return follows from these two finite negative cases. — [Full arithmetic target](../farey-transport-corrections/REPORT.md).

## What are the explicit fractional infeasibility certificates?

### Takeaway

Two six-by-six integer potential arrays supply direct, human-readable separation certificates. Each can also be extended to all72 original variables using a short positive combination of actual zero-lag capacity rows, so the proof need not trust a support-reduction routine. — [Arrays and full Farkas replay](fractional_capacity_check.py).

### Cited Findings

- For the first basis, row b of the following array lists potentials at nodes `a+6*b`, with a increasing across the row. Its total is `-2`. Every surviving triangle has nonnegative potential sum. — [First fixed certificate](fractional_capacity_check.py).

```
 -2 -1 -2 -2 -1 -2
 -1  0 -2 -1  1  2
 -2 -1 -1  2  1  1
  0  1  0  2  3  0
 -1  2  2  1  1  0
  0  1 -1 -1 -2  1
```

- For the second basis the following array has total `-3`, and every surviving triangle again has nonnegative potential sum. — [Second fixed certificate](fractional_capacity_check.py).

```
 -2 -2 -2 -2 -2  1
  1  1  1 -2  1  1
  1 -2  1  1 -2  1
  1  1 -2  1  1 -2
 -2  1  1 -2  4  1
 -2 -2  1  1 -2  4
```

- The first full72-variable certificate uses the following `(cutoff,color,multiplier)` zero-lag rows. Every listed multiplier is positive and every listed actual lag is zero. — [Full replay assertions](fractional_capacity_check.py).

```
(729,0,4), (1458,1,2), (2916,1,1), (6561,2,1),
(2187,1,3), (6561,1,4), (864,2,2), (3456,1,3),
(4608,1,2), (243,1,1), (486,2,3), (1458,2,3), (2187,2,2).
```

- The second uses these rows, again with strictly positive multipliers and zero right-hand sides. — [Full replay assertions](fractional_capacity_check.py).

```
(382205952,1,6), (764411904,2,3), (1528823808,0,3),
(3057647616,1,3), (129140163,1,6), (258280326,0,3),
(1019215872,2,3), (2293235712,0,6), (258280326,2,6),
(429981696,0,3), (805306368,1,3).
```

### Inferences

For a node potential `w_j`, write `h_k=sum_(j in type k) w_j`. Suppose `(FC1)` and `(FC2)` were satisfied. On the zero-lag support, `h_k>=0`, hence

```
0 <= sum_k h_k x_k
   = sum_j w_j sum_(k containing j) x_k
   = sum_j w_j < 0,                                      (FC3)
```

a contradiction. This proof works over the reals, so allowing arbitrary rational denominators cannot evade it. — [Checked node potentials](fractional_capacity_check.py).

For a second direct replay that does not remove types, let `mu_(t,j)` be the listed multipliers. The checker verifies for every original `k=0,...,71` that

```
h_k + sum_(t,j) mu_(t,j) P_k,j(t) >= 0.                  (FC4)
```

The right-hand side after applying the constraints is

```
sum_j w_j + sum_(t,j) mu_(t,j) L_j(t) = -2 or -3.        (FC5)
```

Thus the same contradiction holds in the unreduced variables. All72 coefficients are nonnegative, while the implied scalar upper bound is negative. No floating-point status, assumed integer integrality, or algorithmic search result enters (FC4)–(FC5). — [Fixed full-column replay](fractional_capacity_check.py).

The second potential has a short Hall-style description. Put

```
S={0,1,2,3,4,9,13,16,20,23,24,27,30,31,34},
T={28,35}.
```

Its potential is `w=1-3*1_S+3*1_T`. Every surviving triangle has `#S-#T<=1`. Summing all36 marginal-one equations shows total triangle mass is12, but coverage requires `|S|-|T|=13`. Therefore `13<=12`, a contradiction. This is an interpretation of the already checked second node-potential certificate, not a general Hall theorem for arbitrary three-uniform hypergraphs. — [Set inequality replay](fractional_capacity_check.py); interpretation supplied independently by the companion obstruction researcher.

### Gaps

- The potential matrices are explicit finite certificates, not an infinite-level formula. No argument proves that such a potential exists for every large actual Farey basis. — [Prescribed cases](fractional_capacity_check.py).
- The direct checker reuses the archived exact profile constructor. Its Farkas arithmetic is independent of a solver, but a separate reconstruction of geometry is still desirable as an adversarial audit. — [Reference dependency](fractional_capacity_check.py).

## Are the cutoffs exact, and what does this change for the infinite return?

### Takeaway

The exact first fractional infeasibility thresholds equal the earlier integer ones. This rules out a fractional rescue of these two period-six examples before the accuracy scale needed to beat their degree-two denominator cost, but it neither excludes other bases nor solves the main arithmetic return. — [All-event witness and dual replay](fractional_capacity_check.py), [current arithmetic frontier](../farey-transport-corrections/REPORT.md).

### Cited Findings

| Basis | First fractional infeasibility | Previous actual arrival | Zero-lag survivors | Negative Farkas RHS |
|---|---:|---:|---:|---:|
| `(8,-5),(3,-2)` | 6561 | 6144 | 50 | -2 |
| `(19,-12),(27,-17)` | 3057647616 | 2902376448 | 53 | -3 |

The following earlier covers use fixed type numbering and satisfy all36 marginal equations and **every joint capacity inequality at every earlier actual event**. They therefore supply exact fractional feasibility witnesses before the displayed obstructions. — [Replay over all earlier events](fractional_capacity_check.py).

```
8/3:   (15,17,70,14,66,13,69,16,71,67,12,68),
19/27: (5,38,3,52,9,50,56,23,27,68,21,70).
```

The checker was run successfully under Python3.14 with `-B`; its final line is `PASS: integer Farkas rows over all72 types and all earlier joint-capacity witnesses`. — [Current exact checker](fractional_capacity_check.py).

### Inferences

The real-time constraints are constant between arrival events. Prior feasible covers therefore prove feasibility for every earlier real cutoff; the dual proves infeasibility at the next actual event. Later head requirements contain the same constraints, so infeasibility persists for every later target. In particular, these negative thresholds lie below `2^(2H)` for `H=8,27`; the prescribed family cannot achieve an optimal head through that scale, even before imposing rational-repair constraints. — [Exact firstness replay](fractional_capacity_check.py).

This result changes the next research action: fractional weights at the **same fixed period and the same two shapes/bases** do not supply the desired escape. New bases, a larger period, additional shapes or a different decomposition require their own feasibility and arithmetic arguments. The companion arithmetic research may still give a useful conditional theorem for such future families. — [Finite scope of current certificates](fractional_capacity_check.py), [full return requirements](../farey-transport-corrections/REPORT.md).

### Gaps

- No claim that the first infeasible cutoffs concern all global couplings: only the retained periodic bulk class and its necessary optimal-head capacity problem are classified. — [Definition of tested class](../farey-transport-corrections/torus_bulk.md).
- No Lean, external review, package installations, broad basis/period scans, density decimals, prior-file edits, or historical-priority checks were performed. The main risk is treating these exact finite fractional obstructions as a universal impossibility theorem or as a proof of irrationality.
