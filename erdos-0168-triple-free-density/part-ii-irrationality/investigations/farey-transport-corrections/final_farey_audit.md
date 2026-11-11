# Independent final audit of Farey transport corrections

## Are the positive imbalance tails and doubling counterterm valid for the actual target?

### Takeaway

**Pass.** The exact scalar identity, the uniform positive tail lower bound, the actual continued-fraction upper bound, the eventual exact reduced ternary valuation on every lower actual convergent, and the strict doubling counterterm all reconstruct correctly. They do not produce an adequate infinite integer-cleared error sequence. The independent certificate integrates actual constant intervals and reconstructs token geometry without importing any companion checker. — [Imbalance note](imbalance_tails.md), [independent certificate](final_farey_audit_check.py), [accepted arithmetic target](../rational-coupling-construction/REPORT.md).

### Cited Findings

- The accepted input is the finite minimum theorem with positive tokens of color `a-b mod3`. Their arrivals are `2^a3^b`, except `b=0,a>=1` has factor `3/2`, and `b=1,a>=2` has factor `9/8`. In particular `(2,1)` arrives at `27/2`; no rounding or deletion of this endpoint is allowed. The rank cost is `M`, and `Z=3-3M=9c-6`. This audit accepts the earlier finite theorem and rank optimum rather than re-proving them. — [Accepted input](../rational-coupling-construction/REPORT.md), [token construction](../hybrid-arithmetic-closure/global_carries.md).
- All three original checkers pass under Python 3.14 with `-B`. The imbalance checker treats actual arrival endpoints and intervening intervals, both lower examples `5/8,41/65`, the upper example `12/19`, and the rational forcing formula. Finite checking supplements the infinite proofs below. — [Imbalance certificate](imbalance_tails_check.py), [bulk certificate](farey_bulk_check.py), [repair certificate](boundary_repairs_check.py).
- The independent checker obtains `L_8=119/108`, `L_64=2065/1728`, and reduced ternary exponents `15,34,123` at `5/8,12/19,41/65`. The principal valuation theorem retains its proved **sufficiently late lower-convergent** scope; the zero convergent `0/1` is not an exception to be silently included. — [Independent exact values](final_farey_audit_check.py), [scope of IT10–IT12](imbalance_tails.md).

### Inferences

**A1. Normalization and every real endpoint.** Write `Q_j(t)` for the actual right-continuous arrived counts, `N=sum Q_j`, `tau=min Q_j`, and `e=N-3tau`. The raw reciprocal token mass is `3`. The dyadic retiming subtracts `1/3`; the row-one retiming subtracts `1/54`. Therefore the full positive mass is `143/54`. Tonelli applies to `N` and `tau` separately, and gives

```
Z=19/54+integral_1^infinity e(t)t^-2 dt
 =19/54+integral_0^infinity E(T)e^-T dT,
E(T)=e(exp T).
```

For rational `X>=1`, the rational lower comparison is

```
L_X=19/54+sum_(s<=X) Delta e(s)/s-e(X)/X,
Z-L_X=R(X)=integral_X^infinity e(t)t^-2dt.
```

At an actual arrival exactly at `X`, its newly inserted reciprocal jump cancels the change in `e(X)/X`. Simultaneous arrivals are processed together. Thus neither right-continuity nor the fractional endpoint `27/2` creates a missing term. For a rational coupling optimal through `X`, adding one third of its entire partial-token tail to its cost and transforming by `3-3(cost)` gives exactly `L_X`; this correction is independent of the chosen coupling. Rationality of this one complete scalar integral does not imply rationality of individual translated profiles. — [IT1–IT4](imbalance_tails.md), [independent interval/jump equality](final_farey_audit_check.py).

**A2. Uniform tail floor.** Let `omega^2+omega+1=0`, `V=sum_j Q_j omega^j`, and `m=floor(log_3(2t))`. For all real `t>=7`, retiming doubles covariantly and

```
V(2t)=omega V(t)+s(m),
s(m)=1,-omega,0 for m=0,1,2 mod3.
```

The only inverse low-patch failure occurs below `27/4`, so `7` is a valid uniform threshold. Since `e=0` if and only if `V=0`, nonzero forcing implies `e(t)+e(2t)>=1`. For every `X>=7` there is `[u,3u)` inside `[X,27X]`, with `u<=9X`, on which the forcing is nonzero. Hence

```
2/(3u) <= integral_u^(3u) (e(t)+e(2t))t^-2dt
        <=3 integral_X^(54X) e(t)t^-2dt,
R(X)>=integral_X^(54X)e(t)t^-2dt>=2/(81X)>0.
```

This argument is uniform in the actual real cutoff and includes intervals straddling simultaneous or retimed events. — [IT5–IT7 and endpoint certificate](imbalance_tails.md), [original exact checks](imbalance_tails_check.py).

**A3. Actual CF-grid upper bound.** For a sufficiently late actual convergent `p/q` of `alpha=log_3 2`, the reciprocal `q/p` is a convergent of `beta=log_2 3`. At `X=2^(3q)` the row endpoint is `3p-1` or `3p`. In each of the three row residues, remove exactly `p` iterates of the zero-mean step function `g(u)=omega^floor(3u)`. A rational `p`-grid has a bounded interval-count error; displacement by less than `1/p` can affect only a bounded number near the endpoints. Ten per third and thirty in modulus per block are safe, uniformly in initial phase. At logarithmic future displacement `s>=0`, the remaining number of terms is at most `s/log3+2`. Thus

```
|W(log X+s)|<=93+s/log3,
e(X exp(s))<=188+2s/log3,
2/(81X)<=R(X)<=(188+2/log3)/X<200/X.
```

Using the complete future block estimate, rather than merely a small imbalance at `X`, is essential. Both parities of actual convergents are covered. — [IT8–IT9](imbalance_tails.md), [uniform moving-phase grid proof](../rational-coupling-construction/coupling_strictness.md).

**A4. A genuine reduced denominator obstruction on the stated sequence.** For every sufficiently late lower actual convergent, put `B=3p` and `X=2^(3q)`. Then `3^B<X<2*3^B` and `B>3`. Exactly one head arrival has ternary exponent `B`: the ordinary token `(0,B)`. Its imbalance jump is `1-3 Delta tau`, a 3-adic unit. Every other reciprocal term has ternary denominator exponent below `B`; the endpoint term is dyadic and `19/54` has ternary exponent only three. Therefore

```
v_3(L_X)=-3p.
```

This proof applies to every member in the eventual lower sequence, not only the two checked examples. If `b_X` is the actual reduced denominator, then `b_X>=3^(3p)`, and `3^(3p)/X->1`. Consequently

```
liminf b_X*(Z-L_X)>=2/81.
```

Every integer clearing factor of `L_X` is at least `b_X`. Thus this specific lower-CF truncation family cannot have shrinking integer-cleared errors, even with all possible cancellations allowed. This is stronger than its nominal upper clearance `2^(3q)3^max(floor(log_3 X),3)`, and has a narrower scope: it is not a valuation theorem for the Richardson counterterm, arbitrary upper convergents, or independently built couplings. — [IT10–IT12](imbalance_tails.md), [independent exact valuations](final_farey_audit_check.py).

**A5. The rational doubling counterterm.** Remove the balanced cycles of the vertical strip in the count-vector doubling identity. If `r=(floor(log_3(2t))+1) mod3`, its residual minimum increment `h(t)` is binary, and

```
e(2t)-e(t)=r(t)-3h(t),   h in {0,1},   t>=7.
```

For rational `X`, with `m=floor(log_3(2X))` and `r_j=(m+j+1) mod3`, direct three-interval geometric summation gives

```
F_r(X)=integral_X^infinity r(t)t^-2dt
      =r_0/X+(-8r_0+6r_1+2r_2)/(13*3^m).
J_X=2L_(2X)-L_X,
U_X=J_X+F_r(X),
U_X-Z=3H(X),   H(X)=integral_X^infinity h(t)t^-2dt.
```

Three doublings give a zero-mean finite-step forcing for `V(8t)-V(t)`. Uniform irrational-rotation averaging makes its accumulated value `o(n)`, uniformly in starting phase. The norm `e(V)=-2 min_j Re(omega^-j V)` is 2-Lipschitz and rotation invariant. The forcing `r(2^j t)` has uniform mean one, so telescoping the last recurrence gives the uniform dyadic-orbit mean

```
sup_(t>=7) |(1/(3n))*sum_(j<3n) h(2^j t)-1/3| ->0.
```

A fixed `M` therefore forces at least one positive `h` among every `M` doublings. Integrating over `[X,2X]` yields `2^-M/X<=H(X)<=1/X`, hence

```
0<3*2^-M/X<=U_X-Z<=3/X,   X>=7.
```

The counterterm is rational and strictly above `Z`, with error of exact order `1/X`; its available dyadic-cutoff clearance is `13*2^(n+1)*3^max(floor(log_3(2X)),3)=O(X^2)`. Qualitative uniform averaging supplies existence of `M`, not a claimed effective discrepancy rate or finite-state closure. — [IT13–IT19](imbalance_tails.md), [independent forcing and clearance checks](final_farey_audit_check.py).

### Gaps

- None of these scalar comparisons has the required proved nonzero integer-cleared errors tending to zero. The exact lower-CF obstruction is sequence-specific; the nominal counterterm clearance is an upper bound, not a reduced-denominator lower bound. — [Arithmetic scopes](imbalance_tails.md).
- No statement about these positive scalar errors proves nonvanishing of the earlier signed hierarchy residual or cheap arithmetic for its entire boundary. — [Accepted remaining obligations](../rational-coupling-construction/REPORT.md).

## Do the Farey tiling and boundary repair define complete cheap rational couplings?

### Takeaway

**Pass in the stated eventual positive-basis regime, including every infinite edge and donor preperiod.** The basis selection is congruence-complete, the whole plane has an index-six three-color partition, and the repaired quadrant cost clears by a fixed constant times `2^A3^(B+6J)` with uniformly bounded `J`. Strictness and convergence hold, but the guaranteed actual head has only scale `2^(H+o(1))`, below the presently charged degree-two arithmetic scale. — [Bulk proof](farey_bulk.md), [complete repair](boundary_repairs.md), [independent incidence/cost reconstruction](final_farey_audit_check.py).

### Cited Findings

- For `u=(q,-p),v=(s,-r)` with determinant magnitude one and opposite nonzero colors, the two basis-coordinate triominoes are `{(0,0),(1,0),(0,1)}` and `{(1,1),(2,0),(2,1)}` in a `3x2` block. Their original-coordinate shapes are `{0,u,v}` and `{u+v,2u,2u+v}`. — [FB1–FB2](farey_bulk.md).
- The five basis-reduction cases cover opposite colors, a zero current color, a zero preceding color, equal nonzero colors with current digit at least two, and the equal-color digit-one fallback. They give positive bases of spans `H<=q_n,V<=p_n`, with both errors tending to zero and spans tending to infinity. No infinitude of a favorable residue type is assumed. — [Complete case table and checks](farey_bulk.md), [comparison-prefix residue checks](farey_bulk_check.py).
- The independent checker reconstructs ownership from a `6x6` incidence cell, using no basis-inversion owner or imported repair code. It recovers the three unshifted costs, donor bijections, reduced denominator bit lengths `27,60,179`, actual first losses, and every named fixed-bulk capacity interval. — [Independent certificate](final_farey_audit_check.py), [original exact outputs](boundary_repairs_check.py).

### Inferences

**A6. Exhaustive positive-basis supply and constant index.** Consecutive convergent colors cannot both vanish because the determinant is a unit modulo three. Each row of the published reduction table preserves determinant magnitude one. Its subtraction vectors are positive by the continued-fraction recurrence; in the digit-one fallback, the two preceding equal colors force the intervening color to zero. Selected errors are combinations with coefficients at most two of errors at a fixed finite lag. Their signs remain opposite. These facts prove supply for every sufficiently late actual convergent, including noncomplementary and zero residue cases. — [FB2 and its complete case table](farey_bulk.md).

In each `3x2` basis block, the two triominoes use exactly its six distinct cells and each contains all three colors. The basis map is a bijection of `Z^2`. The period lattice `Lambda=<3u,2v>` has index six, contains `6Z^2`, and has a color-cycling translation `2v`. The two shapes are reflections, have the same spans `H=max(q,s),V=max(p,r)`, and have logarithmic dispersion bounded by twice the sum of the two basis errors. Small dispersion alone supplies no long optimality window. — [FB1–FB2](farey_bulk.md).

**A7. The bulk summation includes the actual low rows.** Normalize each shape by its coordinatewise minimum. It has six anchor residue classes modulo six, giving twelve streams. Every wholly contained triangle is uniquely one of these anchors plus `(6n,6m)`, `n,m>=0`; containment is exactly nonnegativity of the minimum anchor. For any stream, let `M_act`, `M_asym`, and `M_raw` be its first actual, asymptotically retimed, and ordinary maxima. The exact complete contribution is

```
1/M_act + 1/(63 M_asym) + 64/(63*728 M_raw).
```

The middle term sums all later horizontal translates in the first six-row block. The last term sums all positive vertical translates, which are ordinary, and all horizontal translates. This is equivalent to FB4–FB5; it remains valid when the first block is already ordinary. The invalid asymptotic low roots affect only `M_act`, never an omitted infinite tail. All maxima scale together, so no unresolved comparison of independent geometric bases is present. A safe full bulk clearance is

```
(2^5*3^3*63*728)*2^H3^V.
```

This is a complete bulk upper clearing factor, not a reduced-denominator theorem. — [FB3–FB6](farey_bulk.md), [independent twelve-stream sum](final_farey_audit_check.py).

**A8. Balanced edge flux and the finite charge.** Keep exactly the triangles wholly in the quadrant. A residual point lies in `a<H` or `b<V`. With `A=6 ceil(H/6), B=6 ceil(V/6)`, split residual points into the finite corner, the bottom strip, and the left strip. On a horizontal cylinder modulo six, moving a horizontal cut by one removes two raw tokens of each color and an equal number of complete triples for each color. Hence color differences in crossing residual counts are independent of the cut. Translating by `2v` also cycles the colors. The difference vector must equal its cyclic rotations and have zero total, so all three counts agree. The vertical cylinder gives the other edge. This proves the far-edge balance and does not presume corner balance. — [BR1–BR2](boundary_repairs.md).

Each point type is a coset of the index-six lattice and has six points in a `6x6` cell, two of each color. If `ell_t,k_t` are its displacements from the triple minimum, reflection gives `sum ell_t=3H`, `sum k_t=3V`. Its count in an `ell_t` by six rectangle differs from `ell_t` by at most five. Thus the number `n` of each color in a left period satisfies `|n-H|<=10`; the bottom capacity similarly differs from `V` by at most ten. For the corner, inclusion-exclusion cancels the balanced wide vertical and horizontal terms. Only six rectangles of dimensions `ell_t,k_t` remain. Removing complete `6x6` cells leaves at most `6(H+V)+36` points per type, proving

```
d_max=max c_j-min c_j <=36(H+V+6).
```

For `H>=20,V<=H`, `n>=H/2>0` and `J=ceil(d_max/n)<=180`. The actual Farey regime eventually satisfies these hypotheses. Positivity in the finite named small case is checked directly. — [BR3](boundary_repairs.md), [capacity and corner assertions](final_farey_audit_check.py).

**A9. Donors, all preperiods, and the full denominator.** Take `d_j=max c-c_j` initial tokens from color `j` of the left strip in period order. The enlarged corner is finite and balanced; couple it by actual ranks. Couple each bottom period by actual ranks. After the donors, couple the three left lists by equal residual indices. For a fixed residue `t<n`, the left triple's color-`j` index is `d_j+t`, and its vertical shift is `6 floor((d_j+t)/n)` before the common later shift. Therefore the entire remaining left cost is exactly

```
(729/728)*sum_(t<n) 1/max_j arrival(left_j[(d_j+t) mod n]
                                      +(0,6 floor((d_j+t)/n))).
```

This explicitly includes the possible donor preperiod; it is not an assertion that an infinite actual-time sorted list starts in its eventual period. The four pieces are disjoint and cover every quadrant label once, including labels whose retimed arrivals coincide. The finite donor head has `a<A,b<B+6J`. Bottom geometric summation supplies numerator `64`, canceling its six extra horizontal exponents; left summation supplies numerator `729`, canceling its six extra vertical exponents. With the already charged bulk and low exceptions, the safe full clearing factor is

```
D=(63*728*2^6*3^6)*2^A3^(B+6J),   D Q in Z.
```

Since `J` is uniformly bounded and `A=H+O(1),B=V+O(1)`, this gives `log D=H log2+V log3+O(1)=(2+o(1))H log2` on the actual selected bases. It is an upper bound on the full rational cost, not a lower bound on its reduced denominator. — [BR4–BR5](boundary_repairs.md), [independent group and integrality tests](final_farey_audit_check.py).

**A10. Actual head, convergence, and strictness.** Let `X` be the minimum of `2^A,3^B` and the ordinary arrival times in the two normalized shapes. Every kept bulk point and every residual point outside the corner arrives at least `X`; forward retiming preserves this inequality. Thus every token arriving strictly before `X` lies in the optimally ranked head, proving true completed-count equality for every `t<X`. The normalized logarithmic times are `V log3+{0,e_u,e_v}` and `H log2-{0,e_u,e_v}`, so `X=2^(H+o(1))`.

The optimal rank tail after this head is bounded by the smooth reciprocal tail, `O(log X/X)`. Hence `M-Q=O(H*2^(-H+o(1)))` and `Q->M`. The retained interior bulk has a full-index fixed-offset dispersed subfamily, so the accepted dispersion theorem gives `Q<M` for every constructed member. This strictness applies after the complete repair, and gives no uniform rate by itself. — [BR6](boundary_repairs.md), [accepted strictness theorem](../rational-coupling-construction/coupling_strictness.md).

### Gaps

- The degree-two full denominator and single-span head do not give `D(M-Q)->0`. An inadequate bound is not a universal impossibility theorem for all selected subsequences or other couplings. — [BR5–BR6 and limitations](boundary_repairs.md).
- The original bulk note deliberately leaves its boundary obligation open; the companion repair discharges that obligation. Its bulk-only warnings must not be mistaken for a defect in the combined construction. — [Bulk scope](farey_bulk.md), [complete companion repair](boundary_repairs.md).

## What do fixed-bulk, translation, and torus capacity tests actually exclude?

### Takeaway

The fixed-bulk lower bound is valid for **every repair of that bulk**. The six translated two-triomino partitions and the larger 72-type torus class have complete finite obstructions for the two named bases. These finite obstructions do not exclude all Farey bases or an adequate infinite family, and the full arithmetic objective remains **STILL OPEN**. — [Fixed-bulk capacity theorem](boundary_repairs.md), [translation classification](translation_phases.md), [torus classification](torus_bulk.md), [independent finite certificate](final_farey_audit_check.py).

### Cited Findings

- For the unshifted bases of spans `(8,5),(27,17),(84,53)`, the independently recovered first forced cutoffs are `243`, `382205952`, and `61966892988215484494118912`. The respective unavoidable full cost gaps are `5/7776`, `7153/203119913336832`, and `7153/32931747576550225295039048712192`. Each forced completed-count deficit is one. — [BR7 exact intervals](boundary_repairs.md), [independent replay](final_farey_audit_check.py).
- All six translation phases are distinct. At spans `(8,5)` their first forced cutoffs, in small horizontal-shift order `0,1,2,3,4,5`, are `243,243,486,1458,2187,4608`. At spans `(27,17)`, shifts `(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)` give `382205952,129140163,429981696,129140163,805306368,258280326`. Every listed cutoff is below `2^(2H)`. — [TP1–TP4](translation_phases.md), [independent complete phase replay](final_farey_audit_check.py).
- Both prescribed best-capacity-phase costs are independently recovered: `13501693/22643712` at shift `(5,0)` and `11301677504582126401/18927526004379353088` at `(2,0)`. Their own repair first losses are earlier, at `1458` and `429981696`. Multiplying each actual reduced denominator by its unavoidable later gap gives a value greater than one; the same assertion holds for the actual reduced denominator of `3-3Q` times three times that gap. — [TP5–TP6](translation_phases.md), [independent denominator/gap products](final_farey_audit_check.py).

### Inferences

**A11. The obstruction quantifier is exactly fixed bulk.** Let `G_B(t)` count completed retained bulk triples, `R_j(t)` count arrived residual tokens, and `P_j(t)` count arrived color-`j` tokens in incomplete bulk triples. Every residual repair, including a fractional repair using each token to total mass one, has

```
G(t)<=G_B(t)+min_j R_j(t),
tau(t)-G(t)>=F_B(t)=tau(t)-G_B(t)-min_j R_j(t)>=0.
```

Writing `Q_j=G_B+P_j+R_j` also gives the useful exact identity

```
F_B(t)=max_j(P_j(t)-(Q_j(t)-tau(t))).
```

If `F_B=g` on `[t,t')`, integrate the nonnegative completed-count loss to obtain the unavoidable cost gap `g(1/t-1/t')`. No sorting or alternative donor order can defeat this bound while retaining that bulk. Moving the bulk phase changes `G_B,P_j,R_j`; the old witness does not automatically apply to the moved partition. — [BR7](boundary_repairs.md), [independent all-event calculation](final_farey_audit_check.py).

**A12. Exhaustive translations retain the complete arithmetic proof.** The full period group is `Lambda`: a translation cannot exchange the two shapes, since a noncollinear three-point set cannot be a translate of its reflection. Hence there are precisely six integer-translation classes. Representatives in `[0,5]^2` exhaust them. Translation preserves the normalized shapes, spans, color-cycling period, type-cell balance, corner bound, and uniform donor bound. Only the six bulk residue cosets and finite lists change. The full rational cost formula, low-row terms, and complete denominator charge therefore persist uniformly across phases. The independent checker generates these representatives by cosets in the original-coordinate `6x6` cell and checks all twelve named phases. — [TP1–TP2](translation_phases.md), [independent phase-aware incidence and cost](final_farey_audit_check.py).

The phase `(5,0)` at `H=8` has unavoidable later gap `1/41472`, so its actual reduced denominator gives the exact lower product `22643712/41472=546`. This is a genuine statement about that prescribed rational value. It is neither a universal denominator lower bound nor a lower bound for every alternative repair of the same bulk; an alternative repair can change its rational denominator. — [TP5–TP6](translation_phases.md), [independent exact product](final_farey_audit_check.py).

**A13. The finite torus class and its necessary constraints.** For each named basis, consider the 72 triangle types `z+{0,u,v}` and `z+{0,-u,-v}`, with all 36 anchor residues modulo six. A 36-node exact cover chooses twelve disjoint residue triples. Each chosen type is repeated under `6Z^2`; together they give a genuine full-plane six-period partition. After retaining its quadrant-contained triples, let `P_(k,j)(t)` be the partial-token profile of type `k`. Exact zero fixed-bulk capacity through a cutoff requires the joint inequalities

```
sum_(selected k) P_(k,j)(t)<=Q_j(t)-tau(t)
```

at every actual event and every color. Since each summand is nonnegative, a type violating an inequality by itself can be banned. If the surviving types admit no exact cover, no partition in this class has zero capacity throughout that prefix. This relaxation is sound without any balanced-edge-flux assumption. — [TB1–TB4 and exact capacity construction](torus_bulk.md), [independent direct-anchor profiles and cover search](final_farey_audit_check.py).

For `(8,-5),(3,-2)`, the first individual-filter unsatisfiability occurs at `6561`, with 50 surviving types and an exhaustive 20-state replay in the supplied checker. For `(19,-12),(27,-17)`, it occurs at `3057647616`, with 53 surviving types and a four-state replay. The independent checker separately reconstructs all 72 profiles, repeats an exact-cover search, and verifies UNSAT at both cutoffs. — [Torus search certificate](torus_bulk_check.py), [independent certificate](final_farey_audit_check.py).

There is also a twelve-type cover satisfying the **joint** inequalities at every earlier event in each case; the last prior events are `6144` and `2902376448`. Therefore these are the exact first prefix-capacity infeasibility cutoffs for this 72-type class, not merely upper bounds from the individual-filter relaxation. This is a statement about capacity feasibility. The witness covers have not thereby acquired the color-cycling symmetry, balanced infinite edges, cheap global repair, or full arithmetic of A8–A10. — [Explicit previous covers and joint replay](torus_bulk_check.py), [independent previous-witness checks](final_farey_audit_check.py).

### Gaps

- The named fixed-bulk and torus results are finite classifications for two bases. They do not exclude other actual convergent levels, selected infinite subsequences, larger periods, additional triangle shapes, or state-dependent bulk choices. The torus search excludes integer exact covers of the stated 72 types; it makes no claim about fractional hypermatchings of those types. — [Translation scope](translation_phases.md), [torus class and fractional limitation](torus_bulk.md).
- A zero capacity profile is necessary for an optimal fixed-bulk head; it does not itself prove a cheap rational boundary repair. The earlier hierarchy still needs its own complete boundary arithmetic and signed nonvanishing, and the new couplings still need an adequate accuracy-to-clearing ratio for one infinite family. — [Full objective](../rational-coupling-construction/REPORT.md).
- Audit verification: the three original checkers, both focused followup checkers, and `final_farey_audit_check.py` run with the designated Python 3.14 interpreter and `-B`. The independent checker imports no previous implementation and writes no files. No source edits outside this new folder, external theorem searches, broad scans, Lean, installs, or external posts were used. The material risk is promoting a nominal denominator bound, a finite capacity obstruction, or new-family strictness into the missing adequate infinite nonzero integer-cleared errors tending to zero. — [All independent assertions](final_farey_audit_check.py), [accepted open endpoint](../rational-coupling-construction/REPORT.md).
