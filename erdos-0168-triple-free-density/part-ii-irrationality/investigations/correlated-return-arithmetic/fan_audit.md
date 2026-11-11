# Independent audit of the complete Farey fan

## Does the infinite resummation retain every jump and boundary?

### Takeaway

**PASS; no substantive erratum.** The complete fan expansion and the bound \(300\,2^{-(q+2Q)}\) follow from the accepted jump, variation and actual-response theorems. The proof correctly distinguishes the three-periodic canonical actual responses from the generally nonperiodic full rational quotients. — [Audited theorem FF1–FF6](<farey_fan.md>), [accepted complete scalar identities](<../signed-arithmetic-returns/signed_scalar.md>).

### Cited Findings

- The current model is the prescribed correct-side model at an actual nonresonant convergent \(p/q\), with immediate successor \(P/Q\). The first mediant \(r/s=(p+P)/(q+Q)\) must have one of the four balanced nonresonant states. The accepted comparison retains the complete jump and both open Farey variation intervals, including low rows and the exceptional origin convention. — [Accepted scalar theorem](<../signed-arithmetic-returns/signed_scalar.md>), [accepted response theorem](<../response-closure-tests/response_relations.md>).
- Complete rational-grade conservation supplies the paired quotient factorization even when a fan member is resonant. The established bound is \(|Q_{a,b}|\le3(1+b/r_k)\); no cheap scalar denominator for a resonant member is needed here. — [Resonant grade extension](<../response-closure-tests/general_states.md>).
- Both the supplied checker and the new independent checker pass. The latter imports no project module. — [Supplied checker](<farey_fan_check.py>), [independent checker](<fan_audit_check.py>).

### Inferences

Write \(\delta=q\alpha-p\), \(\delta'=Q\alpha-P\), and \(\sigma=\operatorname{sign}\delta\). Consecutive errors have opposite signs and \(|\delta'|<|\delta|\). Therefore \(k\delta+\delta'\) has sign \(\sigma\) for every \(k\ge1\). Every
\[
F_k=(kp+P)/(kq+Q)
\]
lies on the current side of the actual slope and is crossed when travelling from the current correct-side endpoint to \(\alpha\). Consecutive fan members are Farey neighbors. Their open intervals, the fan points, and the open interval \((F_1,P/Q)\) cover the required path; the last interval may overcover beyond \(\alpha\), which is harmless for a variation bound. The current endpoint jump is excluded by the one-sided convention. These conclusions use ordinary continued-fraction inequalities and the accepted pure-jump representation, not numerical observations. — [Accepted endpoint conventions](<../signed-arithmetic-returns/signed_scalar.md>), [audited FF1–FF2](<farey_fan.md>).

The quotient bound gives \(|\mathcal Q_{r_k,s_k}|\le9+9/(2r_k)\le27/2\). Hence the jump series is absolutely convergent, dominated by a constant times
\(\sum_k(2^{-Q-kq}+3^{-P-kp})\). At the current endpoint, each fixed coefficient has the prescribed side limit; uniform absolute convergence of the weighted coefficient series justifies dominated convergence to the correct-side model. No additional endpoint jump or continuous variation term is lost. — [Complete quotient and pure-jump inputs](<../signed-arithmetic-returns/signed_scalar.md>).

For a Farey pair with coordinate sums \(A,B\), the exact variation formula implies
\[
\mathcal V\le72\,2^{-A}+\frac{189}{4}3^{-B}.
\]
The two fan-gap thresholds are \(A=(2k+1)q+2Q\) and \(B=(2k+1)p+2P\). Summing the two geometric series separately yields precisely the stated \(B_{\rm off}\). This is valid for arbitrarily large \(k\): it never assumes that \(k\delta+\delta'\) stays small. — [FF1 and the accepted variation formula](<farey_fan.md>).

For every fan member, the original parent Farey interval contains both it and \(\alpha\), and no interior rational has denominator below \(s=q+Q\) or numerator below \(r=p+P\). A disagreement at direct index \(a<s\) or reciprocal index \(b<r\) would produce such an interior rational. Thus the common rectangle is exactly the justified one:
\[
|\mathcal Q_{r_k,s_k}(1/2,1/3)-G_k|
\le \varepsilon=\frac{45}{2}2^{-s}+\frac{63}{2}3^{-r}.
\]
The range conditions \(s\le s_k,r\le r_k\) hold. Using \(s_k,r_k\) as the matching rectangle for \(k\ge2\) would generally be wrong; the audited proof does not do so. Its accepted exterior comparison includes the low rows and resonant grade boundary. — [RR4 complete exterior estimate](<../response-closure-tests/response_relations.md>), [resonant extension](<../response-closure-tests/general_states.md>).

The parent commutator and balanced first-mediant transform pin the parent transforms. Since the current multiplier is a nontrivial cube root of unity, the exact repeated-word recurrence has period three. The residue pair has the same period. The canonical endpoint and actual-axis definition therefore give \(G_{k+3}=G_k\). **It is only the canonical actual response that is periodic:** the quotient error is retained separately and uniformly. With \(x=2^{-q},y=3^{-p},u=2^{-Q},v=3^{-P}\), absolute summation gives
\[
Z-\widehat Z^\sigma_{p,q}
=\sigma\sum_{j=1}^3\left(\frac{ux^j}{1-x^3}
-\frac{vy^j}{1-y^3}\right)G_j+\mathcal R,
\]
\[
|\mathcal R|\le B_{\rm off}
+\varepsilon\left(\frac{ux}{1-x}+\frac{vy}{1-y}\right).
\]
All terms in this bound have explicit provenance. — [Parent commutator and canonical endpoints](<../response-closure-tests/general_states.md>), [FF2–FF5](<farey_fan.md>).

I independently checked the loose constant. For \(q\ge4,Q\ge5,p\ge3\), the first off-fan variation is at most \((855/4)2^{-(q+2Q)}\). The fan-gap geometric sum is below \(215\,2^{-(3q+2Q)}\); here only the first exponent comparison uses \(|3\delta+2\delta'|<5/Q\le1\), and the later terms are summed in their respective bases. Also \(\varepsilon\le117\,2^{-s}\) and the gap-sum bound is at most \(8\,2^{-s}\). Consequently
\[
|\mathcal R|<
\left(\frac{855}{4}+215\,2^{-2q}+936\,2^{-q}\right)2^{-(q+2Q)}
<300\,2^{-(q+2Q)}.
\]
These threshold inequalities are comfortably satisfied by the named actual example. — [FF6, reconstructed here](<farey_fan.md>), [independent exact numerical verification](<fan_audit_check.py>).

### Gaps

- The accepted global finite optimum, complete birth formulas, quotient factorization, response exterior theorem and pure-jump representation are inputs; their complete earlier proofs are not rebuilt in this audit. Their domain and boundary hypotheses were checked for the new application. — [Accepted foundation](<../weighted-response-identities/REPORT.md>).
- The corrected residual \(\mathcal R\) has not been proved nonzero. Existing scalar nonvanishing concerns \(Z-\widehat Z\), not this residual. Nor has rationality of the \(G_j\) been deduced from rationality of \(Z\). — [Explicit arithmetic gaps](<farey_fan.md>).

## Do the state classification, weighted cycles and actual example reconstruct independently?

### Takeaway

**PASS.** An independent exact implementation reproduces all sixteen oriented classes, eight canonical responses, five nonzero weighted cycle sums, sixteen rank-five certificates, the resonant \(65/103\) local grade calculation, and the complete \(12/19\) fan interval. The “46-bit” statement compares two different explicit remainder bounds; it is not a gain for the same rational approximant. — [Independent certificate](<fan_audit_check.py>).

### Cited Findings

- The checker derives actual axes from original colored-board counts: the imbalance at \(2^a\) is rotated by \(\omega^{-a}\), and that at \(3^b\) by \(\omega^b\). The response births are calculated using differences of minima, rather than importing the companion inequality/ray implementation. Direct finite-optimum differences verify target coefficients at eight cells, including the exceptional origin digit. — [Independent construction](<fan_audit_check.py>), [accepted finite theorem](<../prefix-and-phase-audit/REPORT.md>).
- The independent reachable-state graph starts at the actual \(5/8<12/19\) bracket, reconstructs all 24 residue/commutator states, then solves the balanced-mediant equations and advances the fan one word at a time. Exactly 16 oriented classes and 8 response states result; the period-three check is exact. — [Independent recurrence and enumeration](<fan_audit_check.py>), [accepted graph proof](<../response-closure-tests/general_states.md>).
- Complete response values are independently summed over a \(96\times96\) rectangle with exterior \(9(2^{-96}+3^{-96})\). All eight stated six-decimal rational enclosures reproduce. The five cycle sums lie in \((-.124,-.123),(.188,.189),(1.113,1.114),(.718,.719),(-.163,-.162)\), with the full three-response exterior paid. Every triple has both signs. — [Independent exact enclosures](<fan_audit_check.py>).

### Inferences

Every cycle sum is genuinely nonzero at the actual weighted values; the simple \(G_1+G_2+G_3=0\) cancellation is unavailable in all five classes. This numerical-value exclusion follows from full interval certificates, not from pointwise rank. Separately, all sixteen exact matrices for \((1,c,g_1,g_2,g_3)\) have rank five. The displayed five-row witness at current \(12/19\) has determinant exactly \(-81\), independently recomputed by a permutation determinant. These facts exclude the specified everywhere pointwise affine relations. They say nothing about other weighted numerical relations or eventual identities. — [Independent checker](<fan_audit_check.py>).

The resonant \(65/103\) test enumerates original tokens, applies the established retiming to their arrival exponents, groups simultaneous arrivals, and sorts ties in the two rational slope directions. It reproduces the canonical \(8\times8\) quotient rectangle, including the nonsmooth \((-1,3)\) arrival whose jump is zero. It uses no companion grade routine. The common direct/reciprocal floors are independently checked for fan members \(1\le k\le6\) at each of the three named actual parent pairs. — [Independent retimed-token and floor tests](<fan_audit_check.py>).

For current \(12/19\), successor \(41/65\), the independent evaluator computes the entire periodic rational current model with a separately implemented summation and the exceptional origin contribution removed exactly once. A \(200\times140\) actual-target rectangle retains both exterior strips; its coefficient formula is the accepted one, with the independent original-board axis construction. The uncertainty of each \(96\times96\) actual response is multiplied by its exact rational fan coefficient before the final interval comparison. The actual target enclosure lies strictly inside the resulting complete fan interval. — [Independent full model/target/fan enclosure](<fan_audit_check.py>).

Precisely, define
\[
R_{\rm old}=\mathcal V(p,q;r,s)+\mathcal V(r,s;P,Q),
\quad
R_{\rm new}=B_{\rm off}+\varepsilon\left(\frac{ux}{1-x}+\frac{vy}{1-y}\right).
\]
The checker proves
\[
2^{46}<R_{\rm old}/R_{\rm new}<2^{47}.
\]
\(R_{\rm old}\) bounds the remainder after retaining one complete mediant jump; \(R_{\rm new}\) bounds the remainder after retaining the full three-real-response fan correction. They are the exact displayed bounds, not merely the universal constants 432 and 300. **The correction and the approximation have changed.** The new correction contains unknown actual real series, so this is neither a 46-bit improvement to the same rational model nor a 46-bit gain after arithmetic clearing. — [Exact comparison](<fan_audit_check.py>), [old single-jump identity](<../signed-arithmetic-returns/signed_scalar.md>).

### Gaps

- Finite certificates verify the stated examples and the finite state classification. The infinite resummation rests on the written recurrence, common-floor, absolute-convergence and variation arguments above. — [FF1–FF6](<farey_fan.md>).
- No algebraic independence, arbitrary weighted-value independence, or exclusion of all possible state-dependent/correlated cancellations follows. — [Explicit scope](<farey_fan.md>).

## Does the analytic gain establish an adequate arithmetic return?

### Takeaway

**No.** The fan theorem is valid, but the rational prefactors retain successor powers and period factors. The quoted coefficient-price theorem has the stated scope; it does not price the full actual corrected approximation. No adequate infinite arithmetic return is established by this component. — [FF7–FF8 and gaps](<farey_fan.md>).

### Cited Findings

- Substituting \(a=2^q,b=3^p,U=2^Q,V=3^P\) gives \(C_j=a^{3-j}/(U(a^3-1))-b^{3-j}/(V(b^3-1))\). The common nominal factor \(27UV(a^3-1)(b^3-1)\) clears the current model and every coefficient. Its exponent is \(2Q+6q+o(q)\). — [Exact algebra FF7](<farey_fan.md>).
- The previously audited primary S-unit gcd input gives \(\gcd(a^3-1,b^3-1)=\exp(o(q))\). This audit accepts that external theorem and its prior application as an input; it does not reprove the Subspace Theorem. — [Primary Corvaja–Zannier paper](https://arxiv.org/pdf/math/0311030v2), [accepted application audit](<../response-closure-tests/cheaper_audit.md>).

### Inferences

For \(C_3\), let \(A=a^3-1,B=b^3-1,N=VB-UA\). At sufficiently late parents, \(Q>v_2(B)\), \(P>v_3(A)\), so \(v_2(N)=v_2(B)\) and \(v_3(N)=v_3(A)\). Since the raw denominator is \(UVAB\), its reduced factors at two and three are exactly \(2^Q3^P\). Off those primes, \(\gcd(N,AB)\le\gcd(A,B)^2\). The accepted gcd bound therefore yields
\[
\log_2\operatorname{den}(C_3)=2Q+6q+o(q).
\]
The elementary valuations and the direction of every denominator bound are correct. This concerns one rational coefficient itself. It neither bounds the denominator after unknown weighted values are combined nor controls the full-model numerator gcd. — [FF8](<farey_fan.md>), [accepted S-unit application](<../response-closure-tests/cheaper_audit.md>).

At \(12/19\to41/65\), the supplied exact checker finds a 241-bit separate-coefficient clearer and verifies that this clearer times the explicit new remainder bound exceeds one. This is a failure of that particular certification bound, not a lower bound on the true corrected residual. — [Supplied exact arithmetic check, rerun successfully](<farey_fan_check.py>).

### Gaps

- The arithmetic of the actual response values under rationality of \(Z\), adequate cancellation in the complete model numerator, and nonvanishing of the corrected residual remain open. Infinite eligible actual state/gap supply is also not established. — [Parallel complete arithmetic interface](<same_scale.md>).
- No substantive audit erratum was found. Skipped: independent reproof of the archived finite foundation and S-unit theorem, Lean, external review, and additional branches. Material risk: presenting the improved real fan remainder as a cheaper rational return, or the coefficient-price result as a universal obstruction.
