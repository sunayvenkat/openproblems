# Independent audit of rational-order couplings

## Does the actual optimal-head theorem include all predecessors and exceptional tokens?

### Takeaway

**PASS.** The complete rational-order coupling is well defined, and the actual head through \(2^{q+Q-1}\) follows from Farey exclusion together with an explicit model-predecessor bound. The argument is stronger than merely comparing a selected finite collection of tokens. — [Audited construction, RO1–RO3](rational_order.md), [independent certificate](rational_order_audit_check.py).

### Cited Findings

- Both the supplied checker and the new standalone checker pass under Python 3.14 with `-B`. The latter imports no companion code and independently recovers complete prefix sizes 234 and 2241 for \(5/8\) and \(12/19\), respectively. — [Supplied checker](rational_order_check.py), [independent modular-line and actual-time enumeration](rational_order_audit_check.py).
- The positive token representation retains original colors and has effective coordinates \((a-1,1)\) on the delayed dyadic row and \((a-3,3)\) on the delayed row one. The only negative effective first coordinate is \((-1,3)\), namely arrival \(27/2\). — [Token definition and prefix proof](rational_order.md).

### Inferences

**A1. A complete coupling, not a model birth assignment.** Positive rational grade and the lower bound \(A\ge-1\) make each grade sublevel finite. Each color has infinitely many tokens. Its rank list therefore defines a complete bijective three-color coupling. The actual completion time is always the maximum of the three actual arrivals, independently of their model order. — [RO1 and RO6](rational_order.md).

**A2. The Farey window is valid.** Consecutive convergents \(p/q,P/Q\) are Farey neighbors, and the actual slope lies between them. Any rational strictly between \(p/q\) and the slope consequently has denominator at least \(q+Q\). For \(0\le A\le N=q+Q-1\), an ordering reversal of two different effective exponent pairs would give such a rational with denominator at most \(N\). Rational-grade ties are resolved by the sign of \(q\log2-p\log3\), exactly their physical order. Identical effective exponents are genuine simultaneous arrivals. — [RO2](rational_order.md).

**A3. The predecessor argument closes the window.** Every actual-head token has integer grade at most \(pN+1\): the positive approximation error contributes less than \((N+1)/Q<2\), and the negative-error case is even smaller. Since \(p\ge2\) and \(B\ge0\), every model predecessor also has \(A\le N\). The exceptional token \((-1,3)\) is earlier than every token with \(A\ge4\) both physically and in the model, because \(4p>3q-p\). Its remaining comparisons have denominator at most four. Thus no omitted large-coordinate token can precede an actual-head token in model order. — [RO2](rational_order.md), [independent prefix closure](rational_order_audit_check.py).

The standalone replay enumerates the entire actual head by physical row thresholds, then separately enumerates model grades by modular inversion. It checks that the former is the initial segment of the latter, including \(27/2\). This uses different enumeration logic from the supplied frontier checker. — [check_prefix and modular_lists](rational_order_audit_check.py).

### Gaps

- The successor \(Q\) must be the original immediate continued-fraction successor. The proof supplies no analogous window using an arbitrarily selected later denominator. — [RO2 and stated scope](rational_order.md).
- The token-order theorem does not enlarge the previously proved scalar raw coefficient window; the post-annihilator \(Q-q\) window is a separate statement. — [Window distinction](rational_order.md).

## Does the full infinite maximum cost have a proved rational sum and charged denominator?

### Takeaway

**PASS, with no substantive erratum.** The all-future rank templates are proved by exact periodic grade discrepancies and identical rank polynomials. The rational full cost includes every actual maximum correction and crossover power. No useful uniform small-height bound follows. — [RO4–RO8](rational_order.md), [independent direct full-cost sum](rational_order_audit_check.py).

### Cited Findings

- The weighted generating function in RO4 is the raw two-dimensional geometric series plus exactly the two retiming differences. In the nonresonant case its two denominator factors have disjoint roots, and their product with \(1-z\) divides \(1-z^{3pq}\). This proves eventual periodicity of both grade discrepancies and cumulative color discrepancies. — [RO4](rational_order.md).
- The independent checker verifies the resulting common cumulative increment \(g+\kappa\) and the increase of exactly one grade arrival per color. It then computes the actual full cost without importing the scalar model value. — [cumulative and direct_cost](rational_order_audit_check.py).

### Inferences

**A4. The infinite implication does not rest on three sampled periods.** Write \(L=3pq\) and let \(D\) bound the periodic pre-grade color spread. For \(G=(2D+4)L\), the written lower bound in fact gives **more than \(2D\)** arrivals of each color at every grade \(g\ge G-1\). This stronger consequence justifies disjoint leading and trailing windows. A cross-grade rank at maximum grade \(g\ge G\) can therefore use only grades \(g-1,g\), with exactly the ranks between the minimum and maximum pre-grade cumulative counts. — [RO4–RO5](rational_order.md).

Under grade translation by \(L\), new-grade leading positions retain their within-color indices; old-grade trailing positions gain one. Their full ranks have the same common quadratic term and linear coefficient \(g_z+\kappa+h_z\). Since \(g_z+h_z=g\) for all three vertices, a root triple remains a rank triple for **every** later period. The number of roots equals the periodic spread, proving exhaustiveness. Ordinary leading and trailing translations also preserve all delayed-row rules at the only end where those rules occur. — [RO5](rational_order.md).

**A5. The maximum correction is exact.** Within one rational grade, the chosen orientation is the actual physical order. Only cross-grade triples can have a model-latest token which is not physically latest. Their future endpoints scale with \(U=2^{3q}\) and \(V=3^{3p}\). A maximum of a slower and faster geometric stream has one integer crossover; before it the correction is zero, and after it both reciprocal tails are ordinary geometric sums. The finite grade head is evaluated directly. Thus every infinite correction is rational, with its starting power retained. — [RO6](rational_order.md).

The stated safe factor \((U-1)(V-1)2^{A_*}3^{B_*}\) clears the scalar input and every correction when \(A_*,B_*\) bound the finite-head and crossover exponents and \(B_*\ge3\). Resummation does not remove those powers. — [RO7](rational_order.md).

**A6. A second full-cost derivation agrees exactly.** For a fixed grade residue, the ordinary within-grade color word expands by one three-color block per period. Such a block adds one completed rank and shifts every subsequent relative count equally. Its reciprocal birth contribution is a finite geometric run; the endpoint terms scale by \(U^{-m}\) or \(V^{-m}\). The finitely many low-row endpoint modifications have the same endpoint scaling. Cross-grade credited leading tokens also scale with one of those bases. Consequently the actual *same-grade* period sum \(S_m\) is a linear combination of \(U^{-m}\) and \(V^{-m}\). Its complete sum is
\[
\sum_{m\ge0}S_m=
\frac{S_1+(1-U^{-1}-V^{-1})S_0}
{(1-U^{-1})(1-V^{-1})}.
\]
This is the word-insertion/endpoints argument behind the independent direct-cost calculation; the additional period recurrence is a check of that proof, not its replacement. Adding the actual cross-grade maximum tails and finite head reproduces both complete fractions exactly, without the old scalar helper. — [Independent direct_cost](rational_order_audit_check.py), [all-period rank structure](rational_order.md).

**A7. Strictness has its required scope.** There are only linearly many cross-grade or low-row endpoint triples below logarithmic height \(T\). The ordinary same-grade triples form a quadratic-density family with finitely many fixed offsets. Their physical dispersion is at least a positive multiple of \(|q\log2-p\log3|\) for each fixed candidate. The accepted dispersion theorem therefore gives \(Q<M\); no positive constant uniform in \(q\) is used. — [RO8](rational_order.md), [accepted strictness theorem](../rational-coupling-construction/coupling_strictness.md).

### Gaps

- Neither the safe arithmetic nor this audit proves a useful uniform bound on the largest finite-head/crossover powers. The degree-six scalar denominator cannot be transferred to the actual-max cost. — [RO7 and gaps](rational_order.md).
- Rationality, strictness and the long actual head are established together; shrinking denominator-weighted errors on an infinite family remain unproved. — [Remaining target](rational_order.md).

## Are the reduced denominators and named failure certificates genuine?

### Takeaway

**PASS.** Independent direct summation recovers the actual reduced denominators of 137 and 439 bits. Complete physical-event replay proves the first deficit intervals, and the reduced-denominator-weighted lower bounds exceed one in both cases. These are two named failures, not a universal valuation theorem. — [Independent checker output](rational_order_audit_check.py), [supplied exact fractions](rational_order_check.py).

### Cited Findings

- For \(5/8\), the independent full sum is
\[
\frac{84385048996040971880909606545935202648457}
{141324170955093527314663887572476341780480}.
\]
The reduced denominator is \(2^{54}3^{27}\cdot1028780687935\). Its first unit deficit is on \([2^{27}3^7,2^8 3^{19})\), and denominator times this interval's contribution equals \(6480237886298005471431229440\). — [Exact direct sum and deficit replay](rational_order_audit_check.py).
- For \(12/19\), the reduced denominator is \(2^{137}3^{121}\cdot1351932287187751456719735745864595\). The first unit deficit is on \([2^{103}3^2,2^{19}3^{55})\). Its denominator-weighted contribution is the exact integer
\[
29020759742318750102918346738692832886934796342980007386666132244204992059268251568465927146045440>1.
\]
— [Exact direct sum and deficit replay](rational_order_audit_check.py).

### Inferences

The independent replay generates **every actual token** up to the second endpoint of each interval, checks that all belong to the complete enumerated model rank prefixes, and only then counts finished rank triples. A future omitted partner cannot complete a new triple before that endpoint. Thus firstness and the interval lower bounds do not come from a truncated-list assumption. — [actual_head and check_deficit](rational_order_audit_check.py).

All supplied and independent checks pass. There is no substantive erratum; the only presentation clarification is that the chosen grade threshold gives the stronger \(>2D\) multiplicity needed for the disjoint-window assertion. — [RO4–RO5](rational_order.md), [independent checks](rational_order_audit_check.py).

### Gaps

- No all-level reduced-denominator obstruction, no infinite adequate return and no irrationality proof is established by these two examples. — [Scope of RO7 and final gaps](rational_order.md).
- Skipped Lean, external review, installations and broader experiments. Material risk: using the scalar-model denominator for the different actual-max coupling, or treating an exact infinite-tail computation as an adequate arithmetic estimate.
