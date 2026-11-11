# Independent audit of fractional Farey arithmetic

## Does the weighted construction include every token and every arithmetic factor?

### Takeaway

**PASS.** FA1–FA4 define an exhaustive positive fractional coupling under the explicitly imposed corner and edge balance equations. The complete rational cost clears with one common weight denominator, including low retimings and both infinite edges. No substantive erratum was found. — [Construction and FA1–FA7](fractional_arithmetic.md), [supplied exact checker](fractional_arithmetic_check.py), [independent audit checker](fractional_arithmetic_audit_check.py).

### Cited Findings

- The supplied checker passes both nonintegral examples, recovering complete costs `60728105/101896704` and `22603355036644932679/37855052008758706176`. Their common weight denominators are respectively3 and2. — [Supplied checker](fractional_arithmetic_check.py), [independent reconstruction](fractional_arithmetic_audit_check.py).
- The audit checker imports no companion or archived checker. It reconstructs a phase's owner by testing the six possible signed physical incidences and their basis-lattice congruences, rather than reusing the supplied tile-residue branch. It constructs weighted finite rank triples by the union of cumulative mass endpoints. It independently obtains both exact complete costs and the displayed one-S clearing. — [Audit checker, physical_owner, overlay and run](fractional_arithmetic_audit_check.py).
- Independent global replay covers every actual event through `2^24` for basis `(8,-5),(3,-2)` and through `2^48` for `(19,-12),(27,-17)`:179 and720 distinct events. It checks the completed mass of explicitly scaled triples against the sum of componentwise color minima, including later bottom and left blocks, and checks that this mass never exceeds the actual minimum color count. These are stronger finite scopes than testing only the initial corner. — [Audit checker](fractional_arithmetic_audit_check.py).

### Inferences

**AA1. Coverage and residual positivity.** Determinant magnitude one ensures that the three offsets have distinct residues modulo6, and the nonzero opposite color increments ensure one point of each color. Each point therefore belongs to at most one physical triple of a particular anchored type. The36 coverage equations make its total marginal mass exactly one, so the residual after removing crossing triples is nonnegative. A point with `a>=H,b>=V` cannot belong to a crossing owner; hence all residual mass lies in the two asserted strips. With `A>=H,B>=V`, the corner and edge blocks are disjoint and exhaustive. Six-coordinate shifts preserve owner residues and cannot create a horizontal crossing on the bottom or a vertical crossing on the left. This proves exact repetition of the residual blocks. The six balance equations are genuine restrictions; arbitrary weights are not silently assumed to satisfy them. — [FA1–FA3](fractional_arithmetic.md).

**AA2. One denominator, not several.** If `Sx` is integral, each residual point mass is a multiple of `1/S`. Every cumulative color mass and every difference between adjacent overlay endpoints is also a multiple of `1/S`. Overlaying the three finite partitions takes minima and differences of those endpoints; it never multiplies their denominators. Thus oneS clears all finite repaired triple masses. Zero balanced component mass gives the empty coupling and causes no division. — [FA2 and supplied rank_groups](fractional_arithmetic.md), [independent endpoint overlay](fractional_arithmetic_audit_check.py).

**AA3. Both infinite tails and actual low rows.** Bottom-root points have `a>=A>=6`, so horizontal shifts multiply their actual arrivals by64 even for `b=0,1`. Left-root points have `b>=B>=6`, so vertical shifts multiply ordinary arrivals by729. Their full costs are consequently `(64/63)q_R` and `(729/728)q_L`. For any bulk stream, a first positive horizontal shift has passed all exceptional low-a roots; a positive vertical shift has passed all low-b roots. Summing first member, horizontal tail and ordinary double tail gives exactly FA5. The retimed `27/2` token is preserved by both implementations. — [FA2–FA3](fractional_arithmetic.md), [independent exact cost and scaled-time replay](fractional_arithmetic_audit_check.py).

**AA4. Safe complete clearance.** A normalized bulk root has coordinates at most `H+5,V+5`; finite edge roots have coordinates at most `A+5,B+5`, and corner roots have smaller coordinates. The possible actual/asymptotic retimings add only bounded prime exponents. Since `A,B>=6`, the safe factor `2^6 3^6` covers all those exponents. Multiplication by63 and728 clears the geometric sums, and multiplication byS clears all weights. Therefore the asserted full factor

```
D=S*(63*728*2^6*3^6)*2^A3^B
```

is sufficient. It is a clearing upper bound; nothing in this audit turns it into a reduced-denominator lower bound. — [FA3 and FA6](fractional_arithmetic.md), [both exact clearances reconstructed](fractional_arithmetic_audit_check.py).

### Gaps

- The finite checker exercises the two stated phase mixtures and period6. It supports the construction but does not replace the general written geometric and mass-interval proofs. — [Checker scope](fractional_arithmetic_audit_check.py).
- Balanced repairs and complete rationality do not establish a super-two-span optimal head. The two displayed examples only claim their small verified optimal heads. — [FA4 and construction scope](fractional_arithmetic.md).

## Is the projected polytope and polynomial common-denominator theorem sound?

### Takeaway

**PASS.** Actual componentwise rank optimality is exactly expressible in the original72 variables. The potentially many head inequalities do not enlarge the ambient dimension, and one determinant bounds a common denominator for a feasible vertex. — [FA5–FA8](fractional_arithmetic.md), [global functional replay](fractional_arithmetic_audit_check.py).

### Cited Findings

- For a finite balanced component, the arrived color mass is an initial interval of its cumulative rank coordinate. Intersecting its three initial intervals has length the minimum of the three masses. Repeated edge repairs have the same property at their scaled actual times. — [FA5 derivation](fractional_arithmetic.md), [independent all-event identities](fractional_arithmetic_audit_check.py).
- The inequality that the sum of component minima exceeds a threshold is equivalent to imposing the corresponding linear inequality for every choice of one color in every component. It is not equivalent to imposing a single fixed color choice or merely the ideal residual-global-rank capacity condition. — [FA8–FA9](fractional_arithmetic.md), [necessary-only capacity distinction](../farey-transport-corrections/torus_bulk.md).

### Inferences

**AA5. No head component is omitted.** At a fixed actual cutoff there are only finitely many arrived points and hence finitely many relevant corner/edge components. Include all of them, not just the three finite roots. Their completed-mass functional is the retained bulk mass plus the sum of their three-color minima. Because every positive repaired triple finishes at an actual token arrival, checking all actual events up toX also checks every intervening real cutoff. These event locations are independent ofx. The audit's global replay explicitly includes later periods and verifies this identity. — [FA5](fractional_arithmetic.md), [independent global event loop](fractional_arithmetic_audit_check.py).

**AA6. Coefficients stay polynomial across the entire inequality.** In any chosen color sum, the disjoint components use each arrived point at most once. Each such point has coefficient0 or−1 for a specified kept type; each type has at most one owner at that point. Thus the combined residual coefficient is bounded by the total number `N_X` of arrived points, rather than a per-component bound multiplied by the number of components. The bulk coefficient is likewise bounded by `N_X`. Forward retiming gives `N_X<=(KH+1)^2` at `X<=2^(KH)`. Corner and edge-root balance coefficients are bounded by their finite region areas. The stated `L=4(K+1)^2(H+V+12)^2` safely bounds all coefficients and right sides. This verifies the essential height claim and its uniformity over every projected inequality. — [FA6 and FA10–FA11](fractional_arithmetic.md).

**AA7. One active determinant suffices.** Coverage implies every variable lies in `[0,1]`; hence the finite polyhedron is bounded. A nonempty bounded polyhedron has an extreme point. The active equality and inequality normals at an extreme point span all72 ambient directions, even if the feasible polytope itself lies in a lower-dimensional affine space: otherwise a small positive and negative movement perpendicular to every active normal would preserve all finitely many inactive strict inequalities. Select72 independent integer rows. Cramer's rule clears every coordinate by the single integer `S=|det A|`, and the row-volume bound gives `S<=(sqrt72 L)^72`. No separate product of coordinate denominators or auxiliary-variable denominators is needed. With fixedK and bounded slopes, `log S=O(log H)`. — [FA7](fractional_arithmetic.md).

**AA8. Variable period has the stated arithmetic scope.** For a periodm divisible by6, anchored offsets remain distinct modulo m. The root-coordinate overhead is at mostm−1 in each direction, and the geometric factors become `2^m-1,3^m-1`; `m>=6` still isolates every low exception. There are `d=2m^2` variables and polynomial coefficient height in `H+V+m`. The same determinant proof gives `log S=O(m^2 log(H+V+m))`. Thus the full overhead is `O(m+m^2 log(H+V+m))`, which is sublinear inH under the displayed hypothesis. This is a written parameterized implication, not a tested larger-period feasibility claim. — [FA8 and FA13–FA14](fractional_arithmetic.md).

### Gaps

- The polytope can be empty. Its bounded dimension and vertex arithmetic prove neither feasibility nor an efficient exact search method. — [FA7 gaps](fractional_arithmetic.md), [companion fractional infeasibility certificates](fractional_capacity.md).
- No additional general-period example is claimed or needed for the algebraic implication; the independent finite tests are period6 only. — [Independent checker](fractional_arithmetic_audit_check.py).

## Does the package really reduce irrationality to infinite long-head feasibility?

### Takeaway

**PASS as a conditional reduction, not as a solution of Erdős #168(ii).** Candidatewise strictness extends to fractional mass. If infinitely many actual Farey levels have the specified feasible head beyond the degree-two scale, their complete rational errors would contradict rationality. Actual infinite feasibility remains unproved. — [FA9–FA10](fractional_arithmetic.md), [accepted actual dispersion theorem](../rational-coupling-construction/coupling_strictness.md).

### Cited Findings

- The accepted actual-token discrepancy satisfies `E(T)=N(expT)-3tau(expT)=o(T)`, proved with uniform rotation averaging. The ordinary finite optimum and density identities are earlier accepted dependencies, not re-proved by this audit. — [Actual discrepancy and integrated dispersion proof](../rational-coupling-construction/coupling_strictness.md), [finite theorem and audits](../prefix-and-phase-audit/REPORT.md).
- The new fractional coverage has total type mass12, so at least one type has positive fixed weight for each candidate. Its deep ordinary lattice translates have positive logarithmic dispersion and quadratic completed count. — [FA1 and FA9](fractional_arithmetic.md).

### Inferences

**AA9. Positivity survives overlaps.** For a unit-marginal fractional coupling, partial-token mass is still `U(T)=N(expT)-3G(T)>=0`, and `3(tau-G)=U-E`. A fixed positive-weight ordinary type contributes its positive dispersion times a quadratic lattice count to the integratedU. Every other weighted triple contributes nonnegatively; overlapping supports are counted by their weights, which already sum to unit marginal mass. Since integratedE is `o(T^2)`, the nonnegative completed-count deficit has a positive integral. Its exponentially weighted cost integral is therefore strictly positive. All constants may depend on the candidate; no uniform positive dispersion inH is used. — [FA9](fractional_arithmetic.md), [accepted dispersion mechanism](../rational-coupling-construction/coupling_strictness.md).

**AA10. The correct tail estimate uses the matched head.** Once `G(X)=tau(X)`, monotonicity of completed mass gives, for `t>=X`,

```
0<=tau(t)-G(t)<=tau(t)-tau(X).
```

Integrating this bound against `t^-2 dt` bounds `M-Q` by the optimum rank tail born strictly afterX. Each such birth is bounded by the arrival mass, so the smooth reciprocal tail gives `O(log X/X)` with an absolute constant. A raw integral of `tau(t)` would only give the weaker `O((log X)^2/X)`; the actual head equality supplies the subtraction needed for the displayed sharper estimate. This audit confirms the sharper estimate is valid. — [FA10](fractional_arithmetic.md), [exact actual optimum and rank input](../hybrid-arithmetic-closure/global_carries.md).

Restrict an assumed feasible head to exactly `X=2^((2+epsilon)H)` before invoking the fixedK coefficient bound. The rational vertex then has polynomialS and full clearance `2^(2H+o(1))H^O(1)` on the accepted near-isotime bases. Strictness and the tail estimate give positive cleared errors tending to zero. If `M=A/B` were rational, `BD(M-Q)` would be positive integers tending to zero, impossible. Growing m satisfying the sublinear-overhead hypothesis also works, with `exp(o(H))` overhead; that total overhead need not be polynomial. — [FA10 and precise restriction](fractional_arithmetic.md).

### Gaps

- **OPEN:** infinitely many actual levels with nonempty balanced actual-head polytopes through `2^((2+epsilon)H)`. Neither an exact finite feasible example nor the conditional determinant theorem supplies this infinite theorem. — [FA17 and explicit remaining gap](fractional_arithmetic.md), [named finite obstructions](fractional_capacity.md).
- Skipped Lean, external review, novelty checks and new model exploration. Material risk: treating the audited conditional arithmetic package as proof of actual infinite feasibility or of irrationality. — [Complete audit scope](fractional_arithmetic_audit_check.py).
