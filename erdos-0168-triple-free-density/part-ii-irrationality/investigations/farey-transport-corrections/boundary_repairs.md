# Exact periodic edge repair for Farey couplings

**A complete rational quadrant coupling is constructed with clearing cost asymptotically (2H\log2), where (H) is the Farey tile's horizontal span.** Both infinite edge strips and an unbalanced finite corner are repaired. The construction has strictly nonzero actual error and converges as the Farey vectors grow. Its guaranteed optimal prefix is only of scale (2^H), so the proved approximation rate remains inadequate. More importantly, exact named examples show a forced bulk deficit that no alternative repair of the same kept bulk can remove. A better long-window construction must alter that bulk or its phase, rather than only sort the residual strips differently. — [Exact complete-coupling certificate](boundary_repairs_check.py), [bulk construction](farey_bulk.md), [accepted strictness](../rational-coupling-construction/coupling_strictness.md).

## Can all infinite boundary strips be repaired without cross-axis maxima?

### Takeaway

Yes. The index-six Farey tiling has a color-cycling period, which forces each far-edge residual to contain equal numbers of the three colors in every six-wide period. An unbalanced finite corner can consume finitely many tokens from one periodic strip; the remaining strip is matched using shifted period indices. Every infinite cost then has one geometric base, avoiding cross-axis crossover series. — [Certificate](boundary_repairs_check.py).

### Cited Findings

- The accepted target is the optimum (M=\sum\eta(d)/d) of genuine three-color token couplings, with (Z=3-3M=9c-6). Tokens preserve original color (a-b\bmod3); their actual arrivals are (2^a3^b), except dyadic (a\ge1) is delayed by (3/2), and row-one (a\ge2) by (9/8). The token (12\to27/2) is retained. — [Retiming and matching inputs](../hybrid-arithmetic-closure/global_carries.md), [rank optimum](../hybrid-arithmetic-closure/hierarchy_absorption.md).
- For a unimodular basis (u,v\in\mathbb Z^2) having opposite nonzero color steps, the bulk construction partitions the whole plane by the two triominoes (\{0,u,v\}) and (\{u+v,2u,2u+v\}), repeated by (3u,2v). The period lattice has index six and contains (6\mathbb Z^2); translation by (2v) cycles colors. Each individual triple has horizontal span (H=\max(0,u_x,v_x)-\min(0,u_x,v_x)) and vertical span (V=\max(0,u_y,v_y)-\min(0,u_y,v_y)). — [Bulk proof](farey_bulk.md), [independent ownership routine](boundary_repairs_check.py).
- The present checker independently reconstructs each point's unique plane triple by inverting the basis and reducing coordinates modulo (3,2). It verifies ownership, color multiplicities, rational costs and actual first deficits for three named bases. It imports no earlier checker. — [Source and assertions](boundary_repairs_check.py).

### Inferences

**BR1. Clip complete triples, not individual vertices.** Keep every plane triple wholly inside the quadrant. A residual token is a quadrant point whose plane triple crosses an axis. Since the two triple shapes have spans (H,V), all residual tokens lie in (a<H\) or (b<V). Put

\[
A=6\lceil H/6\rceil,\qquad B=6\lceil V/6\rceil.
\]

The residual set is the disjoint union of a finite corner (a<A,b<B), a bottom strip (a\ge A,b<B), and a left strip (a<A,b\ge B). The bottom pattern repeats under (a\mapsto a+6); the left one repeats under (b\mapsto b+6). — [Exact ownership and residual tests](boundary_repairs_check.py).

**BR2. Exact zero color flux.** Work first on the horizontal cylinder modulo (6e_a). At cut (b\ge c), let (R_j(c)) count color-(j) tokens in crossing triples. For a triple with color-(j) height (b_j) and minimum height (b_\min), its contribution is

\[
\mathbf1_{b_j\ge c}-\mathbf1_{b_\min\ge c}.
\]

Only finitely many triples contribute. Moving the cut by one removes exactly two raw tokens of each color, while the number of formerly complete triples lost is the same for every color. Consequently (R_j(c)-R_\ell(c)) is independent of (c). Translation by the period (2v) shifts the cut and cycles all three colors. The same invariant difference must therefore equal its two cyclic permutations; their sum is zero. Hence (R_0(c)=R_1(c)=R_2(c)). The vertical-cylinder argument is identical. This proves balance of each six-period edge residual; it does not assume balance of the finite corner. — [Period/color structure](farey_bulk.md), [exact strip counts](boundary_repairs_check.py).

**BR3. Capacity and corner charge are controlled.** Each of the six point types is a coset of the index-six period lattice. It contains six points in a (6\times6) cell, two of each color, because the lattice has a color-cycling translation. For type (t), write \(\ell_t,k_t\) for the horizontal and vertical distances from a point of that type to its triple's coordinatewise minimum. Its residual condition is (a<\ell_t\) or (b<k_t\). Reflection of the two triominoes gives

\[
\sum_t\ell_t=3H,\qquad\sum_tk_t=3V.
\]

The number of type-(t) points in ([0,\ell_t)\times[0,6)) differs from \(\ell_t\) by at most five. Thus, if (n) is the number of each color in a six-row left period and (m) the analogous bottom capacity,

\[
|n-H|\le10,\qquad |m-V|\le10.
\]

To bound the finite corner's color differences, apply inclusion-exclusion to its typewise union (a<\ell_t\) or (b<k_t\). The wide vertical and horizontal terms have equal color counts by BR2. Only the six rectangles (a<\ell_t,b<k_t) remain. Complete (6\times6) cells of each type are balanced; the remaining boundary cells have at most (6(H+V)+36) points per type. If (c_j) are the corner counts, then the safe uniform bound is

\[
\max_jc_j-\min_jc_j\le36(H+V+6).
\]

In particular, when (H\ge20) and (V\le H), the left capacity is at least (H/2), and all deficits can be supplied within at most 180 left periods. The constants are deliberately unoptimized. These estimates prove bounded extra height in the eventual positive Farey regime, rather than infer it from a finite table. — [Type-count and named charge checks](boundary_repairs_check.py).

**BR4. A complete bijection.** Let (K=\max_jc_j), and (d_j=K-c_j). Enumerate each color's left strip first by successive six-row periods and then by a fixed ordering of its (n) tokens in one period. Move the first (d_j) tokens of color (j) into the corner. The resulting finite head has (K) tokens of each color; couple it by actual equal ranks. Couple every bottom period by actual equal ranks. On the remaining left lists, couple the three entries with the same residual enumeration index. The retained bulk, finite head, bottom periods and remaining left triples are disjoint and cover every quadrant token exactly once. Every group has one token of each color. — [Constructive `Repair.group` and completeness checks](boundary_repairs_check.py).

Let (\ell_j(t)), (0\le t<n), list the original left-period tokens. For residual rank (nm+t), the color-(j) token is

\[
\ell_j((d_j+t)\bmod n)+(0,6m+6\lfloor(d_j+t)/n\rfloor).
\]

Its actual arrival scales by (3^{6m}). The maximum of each triple therefore scales by the same base, and the entire remaining left cost is

\[
Q_L=\frac{729}{728}\sum_{t<n}
\frac1{\max_j\operatorname{arr}(\ell_j((d_j+t)\bmod n)+(0,6\lfloor(d_j+t)/n\rfloor))}.
\]

There is no variable cross-axis comparison. This period-index coupling is not claimed to be the actual sorted-rank optimum of the infinite strip. — [Exact left-tail formula](boundary_repairs_check.py).

### Gaps

- Equal edge periods do not imply a balanced corner. The construction explicitly supplies its deficits; the named corners below include genuine imbalance. — [Corner counts](boundary_repairs_check.py).
- Sorting an entire strip by actual time is a different repair and may introduce a warmup preperiod from its spread of root weights. No cheap bound for that alternative is assumed. — [Enumeration in BR4](boundary_repairs_check.py).
- A complete rational coupling does not by itself establish a long optimal prefix or an adequate arithmetic return. — [Accepted accuracy requirement](../rational-coupling-construction/REPORT.md).

## What is the complete arithmetic and guaranteed actual accuracy of this repair?

### Takeaway

The repaired coupling has a full clearing factor (D=C2^A3^{B+6J}), with one fixed constant (C) and (J=O(1)) in the actual bounded-slope regime. Hence its logarithmic cost is (H\log2+V\log3+O(1)), asymptotically (2H\log2). The proved optimal prefix is only of order (2^H), yielding an upper error (O(H2^{-H})). — [Full rational cost and clearing assertion](boundary_repairs_check.py).

### Cited Findings

- All low delays and the exceptional (27/2) arrival are included in `arrival`. The bottom shift (a\mapsto a+6) scales actual arrivals by (64) once (a\ge A\ge6); the left shift (b\mapsto b+6) scales them by (729) when (b\ge B\ge6). — [Arrival and tail implementations](boundary_repairs_check.py).
- The kept bulk has twelve residue-coset streams. At a valid minimal anchor, its corner cost is (1/M_{\rm act}), its (n\ge1,m=0) cost is (1/(63M_{\rm asym})), and its (m\ge1,n\ge0) cost is (64/(63\cdot728M_{\rm high})). This is independently the same whole bulk as the companion construction. — [Independent bulk summation](boundary_repairs_check.py), [bulk formula](farey_bulk.md).
- A genuine coupling with a positive-density fixed-offset bulk has strictly positive actual cost gap by the proved dispersion theorem. It applies separately to every repaired Farey coupling; it does not supply a uniform error rate. — [Strictness theorem](../rational-coupling-construction/coupling_strictness.md).

### Inferences

**BR5. Every denominator is charged.** Put (J=\lceil\max_jd_j/n\rceil). The finite head's largest exponent is bounded by (a<A), (b<B+6J), after retaining the actual delays. It clears by (2^{A-1}3^{B+6J-1}). The bottom-period cost acquires factor (64/63); its numerator cancels the extra six horizontal exponents. The left cost acquires (729/728), canceling its extra six vertical exponents. The twelve bulk streams have coordinate exponents at most (H+5,V+5), including all low-row cases. The safe explicit common clearing factor

\[
D=(63\cdot728\cdot2^6\cdot3^6)\,2^A3^{B+6J}
\]

satisfies (DQ\in\mathbb Z). No coefficient or finite head is discarded. When (H,V\to\infty), (V\le H), and the basis is near the actual logarithmic direction, BR3 gives (J\le180), (A=H+O(1)), (B=V+O(1)) and (V\log3=H\log2+o(1)). Therefore

\[
\log D=H\log2+V\log3+O(1)=(2+o(1))H\log2.
\]

This is an actual bound on a complete rational comparison, not only the bulk. It is not a reduced-denominator lower bound. — [Clearing proof and exact assertions](boundary_repairs_check.py).

**BR6. Prefix and convergence.** Normalize each triple shape by its coordinatewise minimum. Let (X\) be the minimum of (2^A,3^B) and all ordinary arrival times of vertices in the two normalized shapes. Every token of a kept bulk triple arrives at least (X); every residual token outside the corner does too. Thus all actual tokens arriving strictly before (X) are in the optimally rematched finite head. The coupling has completed count exactly \(\tau(t)\) for every (t<X). If the two basis vectors' logarithmic errors tend to zero, normalized triple times are all (2^{H+o(1)}), so (X=2^{H+o(1)}). The accepted smooth tail bound yields

\[
0<M-Q\le O(\log X/X)=O(H2^{-H+o(1)}).
\]

The positive inequality follows from the retained dispersed bulk. This supplies another infinite one-sided rational family as the chosen Farey bases grow. Its available error and degree-two clearance do not imply (D(M-Q)\to0). — [Actual finite-head optimum and strictness inputs](../hybrid-arithmetic-closure/hierarchy_absorption.md), [coupling proof and tests](boundary_repairs_check.py).

The exact named repair data are:

|Basis (u,v)|Spans (H,V)|Corner counts|Left tokens/color|Extra periods (J)|Complete cost (Q)|
|---|---|---|---:|---:|---|
|((8,-5),(3,-2))|(8,5)|(17,17,18)|8|1|(40448827/67931136)|
|((19,-12),(27,-17))|(27,17)|(159,159,159)|27|0|(538175119414808197/901310762113302528)|
|((84,-53),(65,-41))|(84,53)|(1412,1406,1412)|84|1|reduced denominator has179 bits|

The checker proves bijectivity on all relevant direct ownership tests, sums every infinite geometric stream exactly, and verifies the displayed common clearing. No decimal density is calculated. — [Exact named outputs](boundary_repairs_check.py).

### Gaps

- Degree-two arithmetic is improved over the earlier degree-five skew construction, but its guaranteed matching window also shrinks to the single-span scale. No adequate error-to-height ratio is proved. — [Earlier skew comparison](../rational-coupling-construction/rational_templates.md).
- The finite optimal corner does not make all retained bulk triples optimal. Improving the first-deficit window requires an actual argument, not near equality of their three arrival times. — [Forced deficits below](boundary_repairs_check.py).

## Can an ideal boundary repair rescue this fixed bulk's long matching window?

### Takeaway

No for the named early events: a capacity calculation gives a strict deficit even if every residual token could be globally rematched optimally. This is a limitation of the specified kept bulk and phase, not of all Farey tilings or every selected infinite subsequence. — [All-repair capacity certificate](boundary_repairs_check.py).

### Cited Findings

- For the fixed kept bulk let (G_B(t)) count its completed triples and (R_j(t)) count arrived residual tokens of color (j). Any repair completes at most \(\min_jR_j(t)\) residual triples at (t). — [Direct token/group counts](boundary_repairs_check.py).
- The checker uses the positive retimed counts \(\tau(t)=\min_jT_j(t)\), enumerates every relevant simultaneous arrival, and directly reconstructs all kept triples and the repaired group containing each token. It does not import the old cone-state checker. — [Event and owner routines](boundary_repairs_check.py).

### Inferences

**BR7. Fixed-bulk capacity obstruction.** Every repair has completed count bounded by

\[
G(t)\le G_B(t)+\min_jR_j(t).
\]

Consequently its loss is at least

\[
F_B(t)=\tau(t)-G_B(t)-\min_jR_j(t)\ge0.
\]

The nonnegativity follows also by writing the arrived color counts as completed bulk triples, partial bulk tokens and residual tokens. If (F_B(t)=g>0) on an interval ([t,t')), every possible residual repair has full cost gap at least (g(1/t-1/t')). This includes fractional repairs with each token used to total mass one. — [Capacity routine and exact intervals](boundary_repairs_check.py).

For the three prescribed phases, exact first forced deficits are:

|Basis spans|First (t) with (F_B(t)>0)|Next arrival (t')|Forced cost gap|
|---|---:|---:|---|
|(8,5)|243|288|(5/7776)|
|(27,17)|382205952|387420489|(7153/203119913336832)|
|(84,53)|61966892988215484494118912|62812323716259432401731584|(7153/32931747576550225295039048712192)|

Each forced deficit equals one. The explicit repair's first losses are at the first two same cutoffs, but for the (84,53) basis its first loss is earlier, at34856377305871210027941888. Better strip sorting might repair that earlier loss, but it cannot remove the later capacity obstruction while keeping this bulk unchanged. For the first (8,5) basis, the forced loss already occurs well before the old (2^{27}) Farey threshold. — [Complete exact event certificates](boundary_repairs_check.py).

### Gaps

- These named capacity obstructions do not prove an all-level early-defect theorem or exclude another integer translation phase. The index-six tiling has six global translation classes with small original-coordinate representatives; changing phase costs only a bounded coordinate shift and preserves the edge-flux theorem. That is a separate sharply defined candidate for testing. — [Period lattice](farey_bulk.md).
- Neither the improved rationality nor the existing strictness theorem proves a sufficiently accurate integer-cleared return. No old signed hierarchy residual is identified with this matching loss. — [Current goal and open arithmetic obligations](../rational-coupling-construction/REPORT.md).
- Skipped: Lean, installations, broad scans, density decimals, old-folder edits, external posts and priority verification. Main risk: treating balanced strip flux or small geometric dispersion as a proof of a long actual optimality window, or calling a nominal denominator bound a reduced-denominator impossibility theorem.
