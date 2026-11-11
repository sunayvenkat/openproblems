# Independent audit of the signed scalar return

## Is the complete paired-jump lower bound valid?

### Takeaway

**PASS in the stated rational-state and short-floor domain.** The infinite quotient, including its boundary coefficients and entire exterior, reconstructs correctly. No substantive erratum was found. The theorem is not a claim about every rational slope or an arbitrary unbounded Christoffel state. — [Audited proof, SS1–SS2](signed_scalar.md), [independent exact certificate](signed_scalar_audit_check.py).

### Cited Findings

- The accepted scalar coefficients lie in \(\{1,-2\}\), retain every low-row exception, and use opposite direct/reciprocal tie conventions. The scalar value credits a model birth and need not equal an actual maximum-arrival coupling cost. — [Accepted two-sided definitions](../reflected-return-models/two_sided_models.md), [actual-maximum distinction](../boundary-return-mechanisms/rational_order.md).
- Both the supplied checker and the independent checker pass under Python3.14 with the no-bytecode option. The independent certificate imports no companion code; it uses exact Eisenstein-ring products and direct rational/raw-board counts instead of the supplied endpoint/model helpers. — [Supplied certificate](signed_scalar_check.py), [independent certificate](signed_scalar_audit_check.py).
- The four complete quotient intervals reproduce as \((9/20,1/2)\), \((-3/50,-1/20)\), \((-11/10,-1)\), and \((7/5,3/2)\), in the source's state order. — [Independent four-response checks](signed_scalar_audit_check.py).

### Inferences

**A1. The toric boundary is accounted for.** Let \(d_{a,b}=c^+_{a,b}-c^-_{a,b}\). At each rational grade the total difference is zero: the two tie orders have the same adjusted counts before and after the complete grade, including the attached indicator events. The fractional endpoint has zero birth in the stated domain. For
\[
Q_{a,b}=\sum_{j=1}^{\lfloor b/p\rfloor+1}
d_{a+jq,b-(j-1)p},
\]
the coefficient of \((X^q-Y^p)\mathcal Q\) is \(d_{a,b}\) when \(a\ge q\), by direct cancellation. When \(a<q\), the missing horizontal term is replaced precisely by the zero total of the complete nonnegative grade chain. When also \(b<p\), that chain is a singleton and \(d_{a,b}=0\). Thus no negative-coordinate remainder is omitted. — [SS1](signed_scalar.md), [prior grade-conservation proof](../reflected-return-models/two_sided_models.md).

There are at most \(1+b/p\) summands, so \(|Q_{a,b}|\le3(1+b/p)\). Both weighted exterior strips converge absolutely. For \(B\le p\), overcounting their intersection gives
\[
\left|\mathcal Q(1/2,1/3)-
\sum_{a<A,b<B}d_{q+a,b}2^{-a}3^{-b}\right|
\le\frac{27}{2}2^{-A}+\frac{45}{2}3^{-B}.
\]
The first constant uses
\(\sum_b(1+b/p)3^{-b}=3/2+3/(4p)\); the second uses the exact tail
\(3^{-B}[\,3(1+B/p)/2+3/(4p)\,]\).
The condition \(B\le p\) is essential when replacing low quotient coefficients by \(d_{q+a,b}\). — [SS1–SS4](signed_scalar.md).

**A2. The low response is genuinely finite-state.** Summing the direct-axis increments yields the displayed endpoint formula in SS6, because
\[
\sum_{a=1}^{q}\omega^{a+\lfloor pa/q\rfloor}
=H(p,q)-1+\omega^{p+q}.
\]
Complex conjugation and the geometric expression for \(S(m)\) give exactly its factor \(1-\omega^2\). The opposite endpoint differs by \(\omega^{2p-q}\). At \(q+r\), \(0<r<24<q\), there are no additional horizontal ties; the extra increment uses only the prescribed short direct floor. The vertical axis and correction tests up to row23 use only the corresponding short reciprocal floors. The origin exception never becomes a spurious exception at the large index \(q+r\). — [SS2 and SS6](signed_scalar.md), [independent ring reconstruction](signed_scalar_audit_check.py).

The coefficient-corner term was independently computed as
\((1-\omega^{-a})(1-\omega^{-2b})/3\), without the source's lookup table. The short vertical axis was reconstructed from raw colored boards at \(3^b\). This reproduces all four enclosures after adding the full24-by24 exterior bound, giving
\[
|\widetilde Z^+_{p,q}-\widetilde Z^-_{p,q}|
>\frac1{20}|2^{-q}-3^{-p}|.
\]
The proof needs the four balanced **rational** states, nonresonance, \(p,q>24\), and the first23 direct/reciprocal floors. Its use at a semiconvergent is valid only after these conditions are checked. — [Independent certificate](signed_scalar_audit_check.py), [domain in SS5](signed_scalar.md).

### Gaps

- A nonzero paired jump does not alone prove correct-side error nonvanishing. The cluster argument below is a separate essential step. — [SS4](signed_scalar.md).
- The full quotient varies with \(p,q\). Its finite response description does not turn it into a fixed rational coefficient for a seed S-unit theorem. — [SS2 scope](signed_scalar.md).

## Does the Farey-cluster argument prove the correct-side error?

### Takeaway

**PASS.** The source bounds the complete variation in both Farey children, so its criterion proves the actual correct-side error rather than only a difference between adjacent models. Its two asymptotic regimes keep the older and mediant denominator scales separate. — [SS3–SS5](signed_scalar.md).

### Cited Findings

- A scalar coefficient depends only on direct floors of indices at most \(a\) and reciprocal floors of indices at most \(b\). The isolated/patch tests use \(b,b-1,b-3\), which do not introduce larger indices. — [Accepted scalar construction](../infinite-return-construction/REPORT.md).
- The independent certificate recovers all three mediant transforms by literal finite sums, verifies their first23 floors with exact powers, and independently computes the child-variation bounds. The leading/remainder ratios agree with the supplied certificate: greater than34 for \(12/19\), and greater than \(938164839467516912276\) for \(53/84\). — [Independent cluster checks](signed_scalar_audit_check.py).

### Inferences

**A3. No continuous variation is hidden.** A direct floor event of index \(n\) affects only \(a\ge n\), and its entire possible weighted effect is at most \(9\,2^{-n}\). A reciprocal event costs at most \(9\,3^{-n}\). On a compact slope interval there are \(O(n)\) events of either kind at index \(n\); the sums of these variation bounds converge. Thus the scalar series converges in bounded-variation norm, not merely uniformly. Its derivative measure is supported on the countable union of rational floor breakpoints, so there is no leftover continuous part. Simultaneous events may be overcounted, which is safe. — [SS3](signed_scalar.md).

For an open Farey interval \((a/b,c/d)\), no direct event has index below \(b+d\), and no reciprocal event has index below \(a+c\). Event counts at index \(n\) are at most \(1+n/(bd)\) and \(1+n/(ac)\). Summing the two geometric series and their first moments gives exactly SS7, including its factors9, \(3/2\), and \(3/4\). Positivity of the endpoint numerators is used for the reciprocal count. — [SS7](signed_scalar.md).

**A4. The endpoint orientation is correct.** Consecutive actual convergents admit
\(\alpha=(p+tP)/(q+tQ)\) with \(t>1\). Hence the actual slope lies beyond the first mediant as viewed from the current endpoint. Starting on the correct side excludes the current endpoint jump. Crossing the mediant contributes its complete oriented jump \(\sigma J\). Every remaining event before or after it is charged to one of the two open child intervals; the successor endpoint is not crossed. Therefore
\[
\left|(Z-\widetilde Z^\sigma_{p,q})-\sigma J\right|\le R
\]
has no omitted endpoint contribution. The first mediant and \(\alpha\) lie in the same parent Farey interior, so any direct floor of index less than \(s=q+Q\), and reciprocal floor of index less than \(r=p+P\), has the same value at both. This proves the short-floor condition for sufficiently large mediants without pretending they are actual convergents or actual critical resets. — [SS4](signed_scalar.md).

**A5. The asymptotic scale hypotheses are necessary and correctly stated.** Along actual consecutive convergents, the two child bounds are \(R=O(2^{-(s+q)})\), with uniform constants: their ternary exponents differ from the corresponding binary exponents by combinations of convergent logarithmic errors tending to zero. The paired lower bound is
\[
|J|\ge\frac1{20}2^{-s}|2^s/3^r-1|.
\]
Thus the explicit condition \(-\log|2^s/3^r-1|=o(q)\) makes the leading jump dominate. The seed input is the fixed one-unit bound at **any close rational gap**, not just at a convergent; that input is named separately in the source audit. — [SS5](signed_scalar.md), [seed normalization](seed_arithmetic.md).

If \(Q/q\) is bounded, the seed's \(o(s)\) separation is indeed \(o(q)\). If \(Q/q\) is unbounded this inference is unavailable. The alternative \(a_{n+2}\ge2\) correctly repairs it: the error recurrence implies
\[
|\delta_n+\delta_{n+1}|\ge\tfrac12|\delta_n|>
\frac1{2(q+Q)}.
\]
Then \(\log Q=o(q)\) gives the required lower scale on the **old** \(q\). Conversion from logarithmic gap to \(2^s/3^r-1\) uses only bounded factors because the mediants approach \(\alpha\). — [SS5 and seed corollary](signed_scalar.md).

### Gaps

- No theorem here supplies infinitely many actual balanced nonresonant mediants satisfying a dominance regime and the adequate gap condition. — [SS5 gaps](signed_scalar.md).
- This scalar argument does not establish nonvanishing of the separate product-hierarchy residual. — [Separate hierarchy boundary](hierarchy_boundary.md).

## What do the exact certificates establish about irrationality?

### Takeaway

**The finite exclusion through \(2^{56}\) is valid; the unconditional irrationality conclusion remains open.** The complete conditional theorem has no additional nonvanishing premise, but retains its actual infinite-supply premise. — [SS5–SS6](signed_scalar.md).

### Cited Findings

- The independent checker reconstructs the correct \(12/19\) model by direct rational-grade board counts and the established periodic summation. Its true160-by110 enclosure is independently reconstructed from the finite minimum-cover formula at \(t\) and \(t-1/2\), without the source's separated-axis implementation. This enclosure lies in the predicted positive cluster-error interval. — [Independent exact checker](signed_scalar_audit_check.py), [accepted finite formula](../prefix-and-phase-audit/REPORT.md).
- At \(53/84\), the independent exact computation verifies
\[
0<D(L-R)<9D\left(2^{-569}+3^{-359}-2^{-569}3^{-359}\right)<2^{-56},
\quad D=27(2^{252}-1)(3^{159}-1).
\]
The outer factor9 is retained. — [Independent finite exclusion](signed_scalar_audit_check.py).

### Inferences

The accepted model integrality \(D\widetilde Z\in\mathbb Z\), the cluster lower bound and the full scalar rectangle upper bound establish
\[
0<|D(Z-\widetilde Z)|<2^{-56}.
\]
If \(Z=A/B\) is rational, its numerator after subtracting \(D\widetilde Z\) is a nonzero integer divided by \(B\). Thus the absolute value is at least \(1/B\), and \(B>2^{56}\). For rational \(c\), the denominator of \(Z=9c-6\) divides that of \(c\), so the same exclusion holds for \(c\). The cleared error itself need not be an integer without multiplying by the unknown target denominator. — [SS12](signed_scalar.md).

On the **same infinite sequence**, a balanced nonresonant mediant, either sufficient dominance regime, and \(Q-5q\to+\infty\) imply nonzero errors and the existing bound \(D|Z-\widetilde Z|\le486(1+o(1))2^{5q-Q}\to0\). Multiplication by a hypothetical fixed denominator of rational \(Z\) would then contradict integer discreteness. None of the three finite certificates supplies that sequence. — [Conditional finish, SS5](signed_scalar.md).

### Gaps

- The actual infinite balanced-mediant and adequate-gap supply remains unproved. The finite exclusion is not a proof of irrationality or a claimed strongest numerical bound.
- Skipped: Lean, installations, external review, priority checks, broader scans and new construction research. Material risk: conflating a complete finite/nonvanishing criterion with its still-missing actual infinite supply.
