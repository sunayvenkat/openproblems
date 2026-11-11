# Adaptive palette capacity and complete repair

## Does a genuinely enlarged palette escape the earlier finite capacity obstruction?

### Takeaway

**Yes at the tested span, and the stronger enlarged palette admits a complete rational coupling with an actual two-span optimal head.** The result below is a single exact construction at \((H,V)=(8,5)\), not an infinite feasibility theorem. — [Exact checker](adaptive_capacity_check.py), [earlier excluded two-shape class](../fractional-farey-transport/fractional_capacity.md).

### Cited Findings

- The actual token at \(z=(a,b)\) has color \(a-b\bmod3\) and arrival \(2^a3^b\), except \(b=0,a\ge1\) has factor \(3/2\), and \(b=1,a\ge2\) has factor \(9/8\). In particular \((2,1)\) arrives at \(27/2\). The accepted finite theorem gives \(\tau(t)=\min_jT_j(t)\), and the optimal coupling cost is \(M=3(1-c)\). — [Accepted arithmetic and token foundation](../fractional-farey-transport/fractional_arithmetic.md), [actual arrival implementation](adaptive_capacity_check.py).
- The first palette starts from vectors \(\mathcal C=\{(1,0),(1,-1),(2,-1),(3,-2),(8,-5)\}\). Include both reflections of \(\{0,u,v\}\) when the two vector colors are opposite nonzero residues, and the collinear progressions \(\{0,u,2u\}\) when they fit inside span \(8\times5\) and the vector color is nonzero. Normalize by coordinatewise minima, sort vertices, and remove duplicates. This produces **11 translation-distinct shapes and 396 anchored period-six types**. — [Functions `normalize` and `palette`](adaptive_capacity_check.py).
- This 11-shape class has the integer residue-cover witness with type IDs \((229,240,248,250,302,303,309,313,323,334,348,391)\). It satisfies every joint necessary-capacity inequality at every actual event through \(2^{16}\), beyond the previous two-shape failure at 6561. This is a necessary-capacity witness, not a complete repaired coupling. — [Function `check_smaller_capacity`](adaptive_capacity_check.py), [earlier threshold](../fractional-farey-transport/fractional_capacity.md).
- For the complete construction, enlarge the vector pool to every nonzero \(cu+dv\), with \(u,v\in\mathcal C\), integers \(-2\le c,d\le2\), and coordinates in \([0,8]\times[-5,0]\). There are **28 vectors**. Apply the same opposite-color-pair, reflection and collinear-progression rule; after deduplication there are **118 shapes and 4248 period-six types**. — [Function `combination_palette`](adaptive_capacity_check.py).

### Inferences

**AC1. A fixed reproducible type convention.** A normalized shape \(S\) has its coordinate minima zero, although the minimum corner need not be a vertex. At each minimum-anchor residue \((a_0,b_0)\in\{0,\ldots,5\}^2\), its plane copies are

\[
(a_0+6n,b_0+6m)+S,\qquad n,m\in\mathbb Z.
\]

Sort the shape tuples lexicographically; within each shape sort residues by \(b_0\), then \(a_0\). Thus the zero-based type ID is \(36i+6b_0+a_0\). Every triangle has one vertex of each color, hence three distinct residue nodes. The certificate’s IDs unambiguously specify whole-plane periodic families, not 32 individual finite triangles. — [Exact type generation](adaptive_capacity_check.py).

**AC2. The complete positive witness.** Give each listed type mass \(n_k/7\), with all unlisted types zero. The checker stores the 32 pairs explicitly in `NUMERATORS`; they are:

```
1619:1  1799:1  2045:2  2231:1  2273:1  2625:2  2696:1
2801:1  2806:6  2930:4  2940:4  2941:5  2944:4  3341:2
3380:5  3381:4  3454:1  3455:2  3517:3  3689:2  3742:1
3757:5  3759:3  3760:3  3765:2  3769:4  3850:2  3884:1
3910:1  4005:1  4020:6  4211:3
```

Every residue node has total incident mass one and \(\sum_kx_k=12\). Keep every wholly quadrant-contained weighted triangle. All omitted crossing mass is nonnegative and supported in \(a<8\) or \(b<5\). This supplies exact unit token marginals once the residual repair below is added. — [Coverage assertions and residual ownership](adaptive_capacity_check.py), [general fractional marginal argument](../fractional-farey-transport/fractional_arithmetic.md).

### Gaps

- Neither the 11-shape capacity witness nor the 118-shape full construction proves a favorable infinite sequence of actual Farey levels. No extrapolation from the single tested span is made. — [Finite scope of the checker](adaptive_capacity_check.py).

## Does the new witness include every boundary term and an actual optimal head?

### Takeaway

**Yes.** At buffered cuts \(A=18,B=12\), the full coupling has exact cost
\[
Q=\frac{20605867009283}{34511190884352},
\]
with all infinite geometric tails included. It agrees with the actual optimum through \(2^{16}\); its first completed-count deficit occurs at 73728 and equals one. — [Functions `check_complete_head` and `check_complete_cost`](adaptive_capacity_check.py).

### Cited Findings

- The repair corner is \(C=[0,18)\times[0,12)\); root bottom block \(R_0=[18,24)\times[0,12)\); root left block \(L_0=[0,18)\times[12,18)\). Their residual masses **per color** are respectively \(239/7,50/7,52/7\). All six balance equations are checked exactly. The cuts are the usual period-rounded cuts plus one extra period in each direction; that extra cost is retained. — [All coverage and balance equations in `actual_system`](adaptive_capacity_check.py).
- Match residual mass by actual-arrival rank intervals separately in these three finite components. Repeat bottom root groups horizontally by six and left root groups vertically by six. Rank splitting remains in \((1/7)\mathbb Z\); bottom actual times scale by 64 and left times by 729, including every low-row timing correction. — [Exact interval overlay, scaling and mass checks](adaptive_capacity_check.py), [generic rank and stream helper used read-only](../fractional-farey-transport/fractional_arithmetic_check.py).
- The safe **complete** clearing factor is
\[
D=7(63\cdot728\cdot2^6 3^6)2^{18}3^{12}
 =2086759741982823677952,
\qquad DQ\in\mathbb Z.
\]
It has 71 bits. It is an upper clearing factor, not a reduced-denominator lower bound. — [Complete cost and clearance assertions](adaptive_capacity_check.py).

### Inferences

**AC3. No edge or exceptional token is omitted.** The whole-plane residue coverage gives total token mass one before clipping. A residual point lies in the union of the two boundary strips. The buffered corner, all bottom periods and all left periods partition that union. The region above both cuts has zero residual mass. Each rank overlay uses every residual point mass exactly once. Bottom tails contribute \((64/63)q_R\), left tails contribute \((729/728)q_L\), and the corner contributes \(q_C\). Every weighted bulk stream uses the actual-first/asymptotic-horizontal/ordinary-high-row identity, so its exceptional arrivals and both infinite directions are included. Thus the displayed rational cost is the full countable coupling cost. — [Complete stream implementation](adaptive_capacity_check.py), [proved full summation identity](../fractional-farey-transport/fractional_arithmetic.md).

**AC4. Actual head verification.** For each event \(t\), let \(g_k(t)\) count completed retained type-\(k\) triangles, and \(C_{E,j}(t)\) be arrived residual mass of color \(j\) in each corner/edge component. The completed mass of this specified repair is exactly
\[
G(t)=\sum_kg_k(t)x_k+\sum_E\min_jC_{E,j}(t).
\]
The certificate directly evaluates this quantity at **all 80 actual events** through \(2^{16}\) and obtains \(G(t)=\tau(t)\). It also checks all later events through \(2^{17}\), obtaining the first loss \(\tau(73728)-G(73728)=1\). This verifies the actual constructed repair, rather than an imagined optimal repair of the residual. Simultaneous arrivals are updated together and \(27/2\) remains in the event list. — [Direct completed-mass replay](adaptive_capacity_check.py).

**AC5. Strictness and asymptotic meaning.** The accepted positive-mass dispersion argument applies to each fixed new candidate: any positive periodic bulk type supplies a quadratic family of ordinary triples with nonzero logarithmic dispersion, implying \(Q<M\). The new finite example therefore is a genuine strict rational comparison with an actual two-span agreement head. It does not supply the infinitely many levels required by the arithmetic return. Nor does its finite head alone beat the fully charged clearing factor. — [Weighted strictness theorem FA9](../fractional-farey-transport/fractional_arithmetic.md), [current finite coupling certificate](adaptive_capacity_check.py).

### Gaps

- No infinite version of these explicit weights, buffered cuts and optimal heads is known. The asymptotic target remains head \(2^{(2+\varepsilon)H}\) at infinitely many actual levels, with the complete denominator charged on the same family. — [Precise sufficient condition FA10](../fractional-farey-transport/fractional_arithmetic.md).
- This checker reuses the previously audited generic rank-overlay and stream-cost functions read-only; its own actual-head profile generation and all original-variable coverage/balance checks are independent of any discovery optimizer. A fresh audit can reconstruct the full cost separately. — [Checker dependencies](adaptive_capacity_check.py).

## What exactly prevents the same palette from reaching the next target?

### Takeaway

**There are two exact, narrowly scoped obstructions.** Minimal repair cuts cannot realize the full \(2^{16}\) head, while the 118-shape period-six class with buffered balanced components is impossible through \(2^{17}\). Neither statement excludes a larger palette, a different period, other cut phases or a different repair architecture. — [Direct obstructions](adaptive_capacity_check.py).

### Cited Findings

- All zero-surplus constraints through \(2^{16}\) leave 339 of the 4248 types. For these types, under minimal cuts \(A=12,B=6\), the first left block at \(t=729\) has unavoidable arrived residual masses \(C_{L_0,0}=1\), \(C_{L_0,1}=0\), although actual color zero is a minimum color. Thus its componentwise rank repair cannot have the entire requested head. — [Function `check_minimal_component_obstruction`](adaptive_capacity_check.py).
- All zero-surplus constraints through \(2^{17}\) leave 165 types. After restricting to them, the 36 residue coverage equations and six buffered component-balance equations have an explicit **42-row integer dual certificate** with right side 83 and every variable coefficient nonpositive. This contradicts nonnegative weights. — [Constant `HEAD17_DUAL` and function `check_head17_balance_obstruction`](adaptive_capacity_check.py).

### Inferences

**AC6. Zero-surplus bans are valid over arbitrary real weights.** At any actual event and any actual minimum color \(j\), an incomplete retained triangle containing an arrived color-\(j\) vertex reserves that mass from completed triples. Since \(T_j=\tau\), head optimality forces its type weight to zero. The checker reconstructs every partial profile from physical contained triangles and actual arrivals. Every omitted original type has a replayable positive-profile, zero-surplus witness; positive-surplus integer-only bans are never used. — [Full 4248-type profile and ban replay](adaptive_capacity_check.py), [fractional capacity conservation argument](../fractional-farey-transport/fractional_capacity.md).

**AC7. The 42-row contradiction.** Let the surviving variables be \(x_k\ge0\), and let the coverage/balance system be \(Ex=b\) in the checker’s stated row order. The hardcoded integer vector \(y\) satisfies
\[
y^Tb=83>0,\qquad (y^TE)_k\le0\quad\text{for every surviving }k.
\]
Hence \(83=y^TEx\le0\), impossible. All banned variables are already forced to zero by AC6, so this handles all 4248 original variables, not merely an unverified filtered subsystem. No simplex implementation, floating-point solver, or third-party package is retained in the final checker. — [Exact integer dual replay](adaptive_capacity_check.py).

**AC8. The earlier 729 deficit is not a first-failure theorem.** Its 339-type support restriction uses zero-surplus conditions from the *entire* \(2^{16}\) head. It therefore proves incompatibility of that requested full head with the minimal decomposition, by forcing an earlier component deficit. It does **not** assert that the first head-infeasibility threshold of the unrestricted minimal-cut class is 729. Moving the cut to \(B=12\) absorbs that early left-block token into the corner; the new explicit full witness shows this constant buffer is useful. — [Both minimal-cut and buffered checks](adaptive_capacity_check.py).

### Gaps

- The \(2^{17}\) negative certificate concerns this specified 118-shape period-six class and balanced component decomposition at \(A=18,B=12\). It does not prove a no-go theorem for every adaptive coupling or an infinite sequence of actual levels. — [Exact finite model definitions](adaptive_capacity_check.py).
- Skipped: broader scans, further palette optimization, Lean, external review, priority claims, installations and archived-file edits. Material risk: confusing the proved finite complete coupling or a finite Farkas obstruction with the still-open infinite arithmetic return. — [Final certificate scope](adaptive_capacity_check.py).
