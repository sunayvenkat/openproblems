# Structural obstructions to fractional Farey heads

## Can a short local witness exclude arbitrary periods and spatial weights?

### Takeaway

**Yes for the named basis `(8,-5),(3,-2)`.** Two exact actual-count events exclude any full-plane fractional covering by the two reflected Farey triangle shapes, followed by keeping every wholly quadrant-contained triangle and repairing the residual arbitrarily, from matching the optimum through cutoff995328. The argument uses no period, rationality, finite-dimensional LP or integer restriction. It is a finite named-basis obstruction, not an infinite family impossibility theorem. — [Independent exact certificate](obstruction_check.py).

### Cited Findings

- The accepted positive token universe has color `a-b mod3`, ordinary arrival `2^a3^b`, dyadic delay factor `3/2` for `b=0,a>=1`, and row-one delay factor `9/8` for `b=1,a>=2`. In particular `(2,1)` arrives at `27/2`. Actual optimum completed count is `tau(t)=min_j T_j(t)` and `M=integral tau(t)t^-2dt`. — [Accepted complete construction](../farey-transport-corrections/REPORT.md), [independent arrival reconstruction](obstruction_check.py).
- At actual cutoff839808 the three arrived counts are `(46,46,46)`. The next event is884736. At995328 they are `(48,47,47)`; the next event is1062882. The checker rebuilds counts from all original exponent pairs and exact retimed arrivals, processing simultaneous arrivals together. — [Standalone exact reconstruction](obstruction_check.py).
- The six possible reflected Farey triangles through `z=(12,5)` are entirely quadrant-contained. Two contain `(7,8)`, which arrives at839808, but both finish only at995328. The other four contain z, which arrives at995328, but have a later member. — [Six-triangle exhaustive incidence assertion](obstruction_check.py).

### Inferences

**General local support lemma.** Fix positive `u=(q,-p),v=(s,-r)` with unimodular determinant and distinct nonzero colors. Assign arbitrary nonnegative real weights to all physical translates of `{0,u,v}` and `{0,-u,-v}`, with total incident weight1 at every original lattice point. Keep every wholly quadrant-contained triangle at its assigned weight, and complete any remaining mass by an arbitrary valid three-color fractional coupling. Suppose an interior point z has all six incident triangles contained. Partition these six edges into groups `A_1,...,A_l`. For each group choose an actual interval `[t_i,t'_i)` and a color `j_i` with zero surplus `T_ji=tau` throughout it, and require every edge in the group to have at least one arrived color-j_i vertex but remain incomplete throughout the interval. If the intervals are pairwise disjoint, then

```
M-Q >= sum_i (1/t_i-1/t'_i) * sum_(e in A_i) w_e
    >= min_i(1/t_i-1/t'_i)>0.                         (O1)
```

Indeed, if `G(t)` is the weighted number of completed triples, retained incomplete mass of a minimum color is unusable by every residual repair. Thus `tau-G>=sum_(e in A_i)w_e`. Integrate over the disjoint intervals and use `sum_(e incident z)w_e=1`. For exact head agreement the weaker pointwise claim suffices: every weight in every group is forced0. This contradicts coverage1 at z. The lemma also holds for more general finite prescribed edge supports, provided the stated incidence, coverage and group conditions hold. — [Proof implementation and exact groups](obstruction_check.py).

For the named example, the six edges, in the checker's order, are

```
0: {(12,5),(20,0),(15,3)}
1: {(4,10),(12,5),(7,8)}
2: {(9,7),(17,2),(12,5)}
3: {(12,5),(4,10),(9,7)}
4: {(20,0),(12,5),(17,2)}
5: {(15,3),(7,8),(12,5)}.
```

Use `A_1={1,5}`, minimum color2 and `[839808,884736)`. Use `A_2={0,2,3,4}`, minimum color1 and `[995328,1062882)`. The two intervals are disjoint and their groups partition the six incident edges. Consequently every complete repaired coupling in this class obeys

```
M-Q >= min(13/214990848,139/2176782336)
     = 13/214990848.                                  (O2)
```

This is stronger in scope than an obstruction limited to period-six coefficients: weights may vary with every physical triangle and may be irrational. It is weaker quantitatively than the sharp period-six threshold6561 supplied by the companion capacity certificate. — [Independent local proof](obstruction_check.py), [sharp periodic certificate](fractional_capacity_check.py).

### Gaps

- Coverage1 at every full-plane point and keeping **all** wholly contained weighted triangles are essential hypotheses. If an arbitrary algorithm may delete otherwise-contained bulk triangles and assign their tokens directly to the free residual repair, the incident-weight equation used here no longer holds. — [Definition and check of the six-edge support](obstruction_check.py).
- This fixed-basis positive real gap is not a lower bound for reduced denominators along an infinite continued-fraction family. It does not exclude changing triangle shapes or selecting other convergent levels. — [Actual arithmetic objective](../farey-transport-corrections/REPORT.md).
- No analogous period-free local witness for `(19,-12),(27,-17)` has been proved here. — [Limited current output](obstruction_check.py).

## Does the second sharp period-six dual have a simple combinatorial meaning?

### Takeaway

**Yes: it is a signed Hall inequality.** After actual zero-surplus events remove forbidden types,15 specified torus nodes require13 units of triangle mass after allowing two compensating nodes, but coverage of all36 nodes allows only12 units. This proves fractional infeasibility at3057647616 without a numerical optimization assumption. — [Companion full certificate](fractional_capacity_check.py), [independent signed Hall reconstruction](obstruction_check.py).

### Cited Findings

- The torus has36 nodes numbered `a+6b`, with `a,b=0,...,5`, and72 anchored reflected triangle types. A fractional cover assigns nonnegative type weights and coverage1 at every torus node. Summing all36 coverage equations gives total triangle mass12. — [Original exact torus model](../farey-transport-corrections/torus_bulk.md).
- At cutoff3057647616 for basis `(19,-12),(27,-17)`, exactly53 types survive all zero-surplus bans. Define

```
S={0,1,2,3,4,9,13,16,20,23,24,27,30,31,34},
T={28,35}.
```

Every surviving triangle e has `|e intersect S|-|e intersect T|<=1`. The standalone checker reconstructs actual zero-surplus bans directly from physical triangles and actual counts, without importing the LP code or the prior torus checker. It exhibits actual zero-surplus witnesses for every type violating this signed bound. — [Independent exact support test](obstruction_check.py).

### Inferences

Multiply `|e intersect S|-|e intersect T|<=1` by the nonnegative type weight and sum. Coverage1 would give

```
13=|S|-|T| <= sum_e x_e =12,                         (O3)
```

a contradiction. Equivalently the node potential `y_j=1/2-(3/2)1_S(j)+(3/2)1_T(j)` has nonnegative sum on every surviving triangle, while its total over all36 nodes is `-3/2`. This is the human-readable meaning of the companion rational Farkas certificate. Types outside the surviving set have weight0 because some actual minimum color is already present in an incomplete retained triangle. No positive-surplus constraint is needed. — [Independent support and charge assertions](obstruction_check.py), [full72-column rational replay](fractional_capacity_check.py).

### Gaps

- The signed Hall sets are basis-specific torus data; they do not automatically persist for arbitrary original-coordinate periods or other continued-fraction bases. The period-free theorem above uses a different physical-point argument. — [Stated scopes](obstruction_check.py).
- Neither finite obstruction proves that all rational approximants fail, nor does either prove Erdős168 irrationality. Skipped: Lean, installs, external posting and priority research. Material risk: dropping the complete-bulk coverage hypothesis or treating these two named bases as an infinite universal theorem.
