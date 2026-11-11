# Bounded integration review of Claude's colour-tripling work

Reviewed 2026-11-08. Source: [Claude's report](<REPORT.md>) and its eight accompanying scripts. These are the additional files found in ErdosGPT. The original 29-file external part (i) folder still matches the saved snapshot. Claude's source files have been preserved unchanged.

Part (ii) remains unproved in these files. This review incorporates the useful arguments and corrects their scope; it does not replace the final comprehensive rigor and novelty review requested for later. W1–W5 below refer to the working inputs in Claude's report.

## What the new arguments establish

### 1. An affine return formula for the actual horizontal state

Write alpha=log_3(2), omega^2+omega+1=0, and S=(1,-omega,0). The elementary identity

\[
S(n+p)=\omega^{2p}S(n)+c_p,\qquad c_p=\sum_{k=0}^{p-1}\omega^{2k}
\]

combined with the accepted axis recurrence gives

\[
A_{a+q}=A_q+u(A_a-1)+c_p\omega^{-q}g(a),\qquad
u=\omega^{2p-q},\quad g(a)=\sum_{i=1}^a\omega^{-i}.
\]

For sufficiently late actual consecutive convergents p/q, P/Q, best approximation gives the required floor agreement for 1<=i<Q, so this formula holds for 0<=a<Q. It is a finite agreement statement for the irrational orbit. In the rational periodic extension, the corresponding relation continues globally with the chosen endpoint convention.

The linear part u is trivial exactly when p+q=0 modulo three. Otherwise it has order three. This explains the 3q and 3p periods used by the existing nonresonant scalar construction. On the actual orbit, applying the displayed formula three times requires a+2q<Q. In the nonresonant case its forcing also cancels, giving A_(a+3q)=A_a on that guaranteed window. The check for 41/65 has an empty guaranteed window: its separately observed nonzero drift is not a consequence of three valid applications of L1. In the resonant case the q-step forcing depends on a modulo three, so a claim of a single constant q-step drift needs that residue dependence retained.

**Scope correction:** an order-three linear part does not prove a lower bound on the reduced denominator of the complete scalar value, nor on denominators obtainable by other constructions. Even a minimal binary period six permits 7/(2^6-1)=1/9, with reduced denominator 9 rather than 63. Periodic numerators, readouts, and complete source sums can cancel. Thus the report explains the nominal cost of this construction; it has not proved that every method must pay that cost or that tripling is the whole obstruction.

### 2. A conditional irrationality criterion using model denominators

Let K be an infinite family of actual nonresonant convergents for which the chosen, correctly oriented complete scalar models z_k satisfy W3–W4:

\[
D_kz_k\in\mathbb Z,\quad
D_k=27(2^{3q_k}-1)(3^{3p_k}-1),\quad
D_k|Z-z_k|\le486(1+o(1))2^{5q_k-Q_k}.
\]

Assume, on this same family,

\[
\text{G1: }Q_k-5q_k\longrightarrow+\infty,
\qquad
\text{G2: }\operatorname{den}(z_k)\text{ is unbounded.}
\]

Then Z and hence c are irrational. Indeed, if Z=A/B, then B*D_k*(Z-z_k) is an integer tending to zero, so z_k=Z eventually. Its reduced denominator would then be bounded by B, contradicting G2.

This correct argument replaces a separate state-eligibility/nonvanishing proof **if G2 is established**. It gives an alternative to the earlier six-state scalar route; it does not prove the missing arithmetic. G2 concerns an infinite sequence, despite each individual model being finite periodic data. With G1 fixed, convergence makes G2 equivalent to irrationality, so its reformulation alone is not a solution.

For actual convergents, Q_k=a_(k+1)q_k+q_(k-1). Infinitely many applicable next digits at least five give G1 on a subsequence. The report does not establish that supply at nonresonant indices. A primitive prime of 2^(3q_k)-1 or 3^(3p_k)-1 surviving in the reduced denominator on an infinite applicable subfamily would establish G2: its multiplicative order forces the prime to grow. That survival is also unproved.

### 3. A useful cost target, with qualifications

The working estimates imply an absolute error upper bound O(2^(-q-Q)). If a complete model with that same error could be cleared by C=O(2^(c*q)), then

\[
C|Z-z|=O(2^{(c-1)q-Q}).
\]

The present nominal exponent c=6 gives 5q-Q. An exact O(2^(2q)) cost would give q-Q<=-q_previous, tending to minus infinity along the convergents. This is a worthwhile alternative target, not a constructed family. It still requires nonvanishing or an equivalent denominator argument. A cost 2^((2+o(1))q) additionally requires its positive overhead to be dominated by Q-q on the selected family. W4 supplies upper bounds, so the report's two-sided asymptotic signs for errors should be read as O bounds.

## Selected computations and their limits

The accompanying [exact checker](<codex_review_check.py>) ran successfully with Python 3.14 using standard-library arithmetic. It checked:

- L1 at every index in the claimed windows for 12/19, 41/65, 53/84, and 306/485, including the first failure at a=Q. The guaranteed triple-return window lengths are 27, 0, 317, and 84.
- The two reported cyclotomic losses using the supplied model-value routine: 11/17 with the minus convention loses 103; 33/52 with minus loses 1249. The plus convention retains both tested full cyclotomic factors in both examples.
- Exact integer inequalities showing those two slopes are upper approximants and are not actual convergents of alpha. For an upper approximant the correctly oriented tie convention in model.py is plus. Consequently these examples disprove unrestricted two-sided divisibility; they do **not** disprove divisibility on the actual correctly oriented convergent family. That stronger restricted claim is still unproved here.
- The existing density enclosure gives 127 common continued-fraction terms for Z, with maximum partial quotient 283. This is certified finite information, not an irrationality argument.
- For the toy T=sum_(b>=0) 3^(-b)*2^(-floor(b*log_2(3))), the b<400 rational truncation has tail less than (9/4)*9^(-400). Comparing the continued fractions of both interval endpoints certifies eight common terms, with largest partial-quotient bit length 92. The raw truncation has a quotient of bit length 802, but that quotient lies beyond this certified prefix. It cannot be used as an established property of the infinite toy from the present computation.

The report's 110-case cyclotomic survey is evidence from near slopes and both signs, not 110 actual convergents. It was not rerun in full. The finite period assertions inside modelval.py use the pre-existing rational-model periodicity theorem as a working input; sampling more entries alone would not prove an infinite period. The near-period script per2.py also requires eta700.pkl, which is not supplied in this folder and was not regenerated.

## Updated remaining obligations

The scalar route can close in either of two ways: prove an infinite eligible supply for the earlier direct nonvanishing theorem, or prove G1 and G2 together for the new denominator criterion. Alternatively construct a cheaper complete approximant family, with a proved clearing/error budget and nonvanishing. The ordered renewal route still needs its own affordable-denominator theorem for the full rational source; positivity and real tail decay are already available in that route.

In every route the arithmetic estimate must concern the same actual complete models as the error and nonvanishing estimates, retaining all low rows and corrections. After that bridge, the integer-lattice contradiction is elementary. Final comprehensive verification of all working inputs and historical novelty remains deferred; no Lean work or autonomous proof search was started by this integration.
