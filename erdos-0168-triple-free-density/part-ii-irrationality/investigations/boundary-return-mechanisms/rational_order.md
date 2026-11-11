# Rational-order couplings and their max correction

## Does rational token order give a genuine long actual head?

### Takeaway

Yes. A nonresonant actual convergent \(p/q\), with next denominator \(Q\), defines a complete equal-rank coupling which is optimal through \(X=2^{q+Q-1}\). This is an actual-token coupling statement, not a claim that its full actual cost equals the old scalar model; that distinction is essential. — [Token construction](../hybrid-arithmetic-closure/global_carries.md), [exact new certificate](rational_order_check.py).

### Cited Findings

- The old one-sided scalar coefficient model already has first axis floor disagreements at \(q+Q,p+P\). The smaller \(Q-q\) rectangle occurs after applying the \(2q\) skew annihilator. Thus the window proved here must not be advertised as a new improvement of the scalar floor window. — [Old supply and window theorem](../infinite-return-construction/diophantine_supply.md), [retained-side identity](../infinite-return-construction/weighted_returns.md).
- Delayed tokens have effective exponents
  \[
  (A,B)=
  \begin{cases}(a-1,1)&b=0,\ a\ge1,\\
  (a-3,3)&b=1,\ a\ge2,\\
  (a,b)&\text{otherwise}.
  \end{cases}
  \]
  Their actual time is \(2^A3^B\), their color remains \(a-b\bmod3\), and \(A\ge-1,B\ge0\). The sole negative exponent is token \((2,1)\), arriving at \(27/2\). — [Audited positive representation](../hybrid-arithmetic-closure/global_carries.md).
- Direct exact replay checks the complete token prefixes through \(2^{26}\) at \(5/8\) and \(2^{83}\) at \(12/19\), not merely the relative order of a preselected finite subset. It also checks an exact row frontier excluding omitted tokens. — [Certificate, prefix_order and frontier_min2](rational_order_check.py).

### Inferences

**RO1. Definition.** Assume \(\gcd(p,q)=1\), \(3/5<p/q<2/3\), and \(p+q\not\equiv0\pmod3\). Put \(\sigma=\operatorname{sign}(q\log2-p\log3)\). Order every token lexicographically by
\[
(pA+qB,\ \sigma A).
\]
Identical effective exponents have identical actual times; their order is immaterial. Restricting this order to each color gives an infinite locally finite list. Couple the \(k\)-th token of each color for every \(k\). This is a complete genuine bijective coupling, denoted \(\mathcal C_{p,q}\).

**RO2. Prefix proof including outside tokens.** Now let \(p/q\) be an actual convergent and \(P/Q\) its immediate successor. Let \(N=q+Q-1\). Consecutive convergents are Farey neighbors, so no rational strictly between \(p/q\) and the actual \(\alpha=\log_3 2\) has denominator less than \(q+Q\). Consequently any two nonexceptional tokens with \(0\le A\le N\) have the same actual and model order: a wrong sign would exhibit just such a rational with denominator \(|\Delta A|\le N\). Rational ties are resolved by the specified \(\sigma\).

It remains to exclude outside tokens preceding the actual head in model order. Write \(\epsilon=\alpha-p/q\). If an actual token has \(t\le2^N\), then \(A\le N\), and
\[
pA+qB=q\log_3t-q\epsilon A
 \le pN+q\epsilon(N-A).
\]
For \(\epsilon<0\), this is at most \(pN\). For \(\epsilon>0\), use \(A\ge-1\) and \(\epsilon<1/(qQ)\) to obtain
\[
pA+qB<pN+(N+1)/Q<pN+2.
\]
The integer grade is therefore at most \(pN+1\). Since \(p\ge2\), every model predecessor has \(A\le N\), because \(B\ge0\). The Farey comparison applies to all nonexceptional predecessors, not just tokens already known to lie in the actual head.

The negative-exponent token is harmless separately: for \(A\ge4\), actual time exceeds \(27/2\), and model grade is at least \(4p>3q-p\) because \(p/q>3/5\). Comparisons with \(A\le3\) use denominator at most four, covered by the same Farey exclusion. Thus the *entire* token prefix through \(2^N\) agrees, including simultaneous and retimed arrivals.

**RO3. Consequences.** Every cutoff \(t\le X=2^{q+Q-1}\) has \(G_{\mathcal C}(t)=\tau(t)\). Therefore
\[
0\le M-Q(\mathcal C)=O(\log X/X).
\]
The standard smooth-token tail gives this bound after head equality; it does not discard a large raw \(\tau\)-tail. The coupling has a quadratic-density interior family of fixed-offset ordinary triples, proved below, so the accepted dispersion theorem makes the inequality strict. — [Strictness theorem](../rational-coupling-construction/coupling_strictness.md).

### Gaps

- The long head supplies no cheap bound on the full rational denominator.
- The argument uses the original immediate successor \(Q\), not a retained or more distant convergent.

## Is the full actual maximum cost rational, and what must be charged?

### Takeaway

The full actual cost is rational for every admissible nonresonant \(p/q\). Its computation requires explicit cross-grade max corrections, with finite crossover powers fully retained. The old degree-six scalar denominator cannot be assigned to this different cost. — [Scalar model input](../reflected-return-models/two_sided_models.md), [new full-cost certificate](rational_order_check.py).

### Cited Findings

- The old corrected scalar min-birth sum \(M^\sigma_{p,q}\) is rational and clears by \(27(2^{3q}-1)(3^{3p}-1)\). It attributes each completed rank to its *model-latest* token, not necessarily its actual latest token. — [Audited scalar definition and resummation](../reflected-return-models/two_sided_models_check.py), [model definitions](../reflected-return-models/two_sided_models.md).
- The present checker imports that exact audited scalar value, and independently constructs model-ordered token lists, finite actual maximum costs, endpoint stream roots, geometric corrections and exact enclosing tails. — [Certificate, full_cost](rational_order_check.py).

### Inferences

**RO4. Periodic grade discrepancies.** Let \(\omega^2+\omega+1=0\). The weighted arrival generating function in rational grade \(n=pA+qB\) is exactly
\[
F_\omega(z)=\frac1{(1-\omega z^p)(1-\omega^2z^q)}
 +\frac{\omega(z^q-z^p+z^{3q-p}-z^{2p+q})}{1-\omega z^p}.
\]
This is the positive-token generating function with its two delays, not an assumed synthetic cover theorem.

Put \(L=3pq\). The two denominator factors have no common root: a common root would imply \(p+q\equiv0\pmod3\). Their product, and also its product with \(1-z\), divide \(1-z^L\). Therefore both weighted grade arrivals and weighted cumulative counts are eventually \(L\)-periodic. The numerator degree is at most \(\max(4q-p,2p+2q)\); periodicity holds by grade \(L\) in the stated range.

Uncolored grade arrivals increase by exactly three under \(n\mapsto n+L\): the ordinary Diophantine line gains three points, and the delayed-row corrections are periodic. Hence each color's grade count increases by one. If \(B_j(g)\) counts color-\(j\) tokens with grade less than \(g\), then for \(g\ge L\)
\[
B_j(g+L)-B_j(g)=g+\kappa,\qquad
B_j(g+mL)=B_j(g)+m(g+\kappa)+L\,m(m-1)/2,
\]
where the same integer \(\kappa\) works for all three colors. Equality of the three increments follows from periodic cumulative color differences.

Let \(D=\max_{L\le g<2L}(\max_jB_j(g)-\min_jB_j(g))\). This bounds every later pre-grade spread. Each ordinary grade has at least \(\lfloor n/L\rfloor\) tokens per color, since its solution chain cycles through all three colors. Retiming removes at most two per color at any grade. Thus for
\[
G=(2D+4)L
\]
every grade \(n\ge G-1\) has more than \(D\) tokens of each color.

**RO5. All future cross-grade triples have finite affine templates.** A rank triple whose maximum grade is \(g\ge G\) can use only grades \(g-1,g\). Otherwise one intervening grade, containing more than \(D\) of every color, contradicts the bound on pre-grade rank differences. Cross-grade ranks are exactly
\[
\min_jB_j(g)<k\le\max_jB_j(g).
\]
There are therefore at most \(D\) such triples per grade, a periodic number.

Within grade \(g\), ordinary solutions run along \((q,-p)\). Under \(g\mapsto g+L\), a bounded leading end translates by \((0,3p)\) when \(\sigma>0\), and by \((3q,0)\) when \(\sigma<0\); the trailing end uses the opposite translation. All low-row corrections at the trailing end repeat under the horizontal shift. Leading and trailing windows are disjoint because every color has more than \(D\) arrivals.

This is an all-\(m\) rank identity, not finite pattern extrapolation. A leading-end position has unchanged within-color index; a trailing-end position increases that index by \(m\). For a token of root grade \(g_z\), write this increment as \(h_zm\), with \(h_z=0\) leading and \(1\) trailing. Its full rank polynomial has common quadratic part above and linear coefficient \(g_z+\kappa+h_z\). In a cross-grade triple, old suffix tokens have \(g_z=g-1,h_z=1\), while new prefix tokens have \(g_z=g,h_z=0\). The three rank polynomials are identical for every \(m\). One finite set of roots for \(G\le g<G+L\) consequently generates **all** subsequent cross-grade triples. Their count matches the pre-grade spread, proving completeness.

The checker verifies root rank matching, correct leading/trailing shifts, the \(g_z+h_z=g\) identity, completeness counts, and two additional periods. The infinite implication comes from the rank-polynomial proof, not from those additional samples.

**RO6. Complete max correction.** Set \(U=2^{3q}\), \(V=3^{3p}\). A same-grade triple is already in actual order, so its model-latest token is its actual latest token. Only cross-grade triples contribute to
\[
M^\sigma_{p,q}-Q(\mathcal C_{p,q})
 =\sum_{\text{cross-grade triples}}
 \left(\frac1{t_{\rm model-last}}-\frac1{\max_jt_j}\right)\ge0.
\]
The finite head before \(G\) is evaluated directly. In each infinite template, the model-last endpoint grows with the slower of \(U,V\), while at least one old trailing endpoint grows with the faster. Let their largest root times be \(c_s,c_f\), bases \(R_s<R_f\), and define the exact integer crossover
\[
k=\min\{m\ge0:c_fR_f^m\ge c_sR_s^m\}.
\]
Its complete correction is
\[
\frac{1}{c_sR_s^k(1-R_s^{-1})}
-\frac{1}{c_fR_f^k(1-R_f^{-1})}.
\]
There is no omitted pre-crossover correction: the model-last token is then the actual maximum. All roots, bases and crossover powers are rational, so the full sum and \(Q\) are rational.

**RO7. Explicit safe arithmetic.** Let \(A_*,B_*\) bound effective exponents in the finite correction head and at every template's crossover, with \(A_*\ge0,B_*\ge3\). Then
\[
(U-1)(V-1)\,2^{A_*}3^{B_*}\,Q\in\mathbb Z.
\]
This retains every crossover power. Its logarithm contains \(A_*\log2+B_*\log3\) in addition to the old six-\(q\) period cost. No \(O(q)\) bound with a useful constant is proved. A denominator for a model-birth series is not a denominator for the actual-max coupling.

**RO8. Strictness.** Beyond the finite boundary windows, same-grade ordinary rank triples have finitely many fixed offsets and form a quadratic-density family. Cross-grade templates and low-row endpoints have only linear count at logarithmic height. Distinct ordinary points in a rational grade have physical log differences that are nonzero integer multiples of \(q\log2-p\log3\). The accepted dispersion theorem therefore gives \(Q<M\) for each fixed candidate. No uniform positive dispersion as \(q\to\infty\) is assumed.

### Gaps

- Rationality is established, but no adequate uniform reduced-denominator bound is established.
- Late max corrections can introduce large smooth denominators; geometric resummation must retain their starting powers.
- A universal valuation lower bound for this new coupling family is not proved.

## Do the two exact complete examples give adequate returns?

### Takeaway

No. Their long actual heads coexist with **actual reduced** denominators of 137 and 439 bits. Exact first-deficit intervals show denominator times error is much larger than one in both cases; this is stronger than failure of a nominal upper estimate. It remains a two-example statement. — [Complete exact certificate](rational_order_check.py).

### Cited Findings

- At \(5/8\), the exact full actual cost is
  \[
  Q=\frac{84385048996040971880909606545935202648457}
  {141324170955093527314663887572476341780480}.
  \]
  Its reduced denominator is
  \(b=2^{54}3^{27}\cdot1028780687935\), with 137 bits. The first deficit is one on
  \([2^{27}3^7,\ 2^8 3^{19})\). Consequently
  \[
  b(M-Q)\ge
  6480237886298005471431229440>1.
  \]
  — [Exact full sum, factorization and first interval](rational_order_check.py).
- At \(12/19\), the reduced denominator is
  \(b=2^{137}3^{121}\cdot1351932287187751456719735745864595\), with 439 bits. The first deficit is one on
  \([2^{103}3^2,\ 2^{19}3^{55})\). The exact product
  \(b(1/t-1/t')\), printed by the checker, exceeds one by many orders of magnitude. The full reduced fraction is also printed rather than approximated numerically. — [Exact full sum and interval](rational_order_check.py).
- The new checker uses integer doubled times, exact grade frontiers, Fraction arithmetic, complete geometric tails and the all-\(m\) rank conditions. Independent finite-head/one-color-tail enclosures contain both full rational costs. It imports only the previously audited scalar model value, not the new coupling geometry or cost. — [Certificate](rational_order_check.py), [audited scalar source](../reflected-return-models/two_sided_models_check.py).

### Inferences

The direct rational-order family closes genuine construction obligations: it is complete, rational, strictly below the target, and has the actual \(q+Q\)-scale optimal head. It simultaneously exposes the missing arithmetic: replacing model-latest weights by actual maxima changes the denominator drastically. Neither the old scalar denominator nor the unusually long observed first-deficit scale may be retained while discarding that correction.

The sufficient infinite target is unchanged: on the same actual infinite family one needs affordable integer clearing and \(0<D(M-Q)\to0\). The two computed reduced denominators and exact gap products refute adequacy of these named examples; they do not exclude an exceptional infinite subsequence or a zero-cost geometric compression with a separately proved height bound.

### Gaps

- Infinite adequate returns and irrationality remain unproved.
- Generic transcendence of the slope cannot be substituted for a missing approximation-supply theorem; the existing sharp supply and comparison countermodels remain relevant. — [Sharp supply scope](../infinite-return-construction/diophantine_supply.md).
- Skipped Lean, external review, installations, broad scans and historical priority. Material risk: conflating the scalar model, its actual-max rank coupling and their different complete denominators.
