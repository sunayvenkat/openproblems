# Independent audit of uniform first mediant nonvanishing

## Does the primary logarithm theorem support the claimed coefficient scale?

### Takeaway

**PASS.** Matveev's original Theorem 2.1 supports the fixed polynomial lower bound used in `fixed_logs.md`. The field, logarithms, heights and dimension remain fixed. No Kohlmeyer–Kruer seed or unknown weighted response coefficient enters this application. — [Primary theorem, journal page 1219](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3), [audited argument](fixed_logs.md).

### Cited Findings

- I independently opened the original 53-page English paper. Equations (1.1), (1.3), (2.1), (2.2), and Theorem 2.1 are present on journal pages 1217–1219. The coefficient parameter is \(B=\max\{1,\max_j |b_j|A_j/A_n\}\). The theorem assumes fixed nonzero logarithm branches independent over \(\mathbb Z\), integer coefficients, and \(b_n\ne0\). Its constants apart from \(W_0\) depend only on the fixed heights, degree and dimension; \(W_0=\log(1.5eBD\log(eD))\). — [Primary definitions and theorem](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=2).
- The note specializes to \(D=1,n=2,A_1=A_2=2\), positive real logarithms of 2 and 3, and coefficients \((m,-n)\) with positive integers \(m,n\). — [FL1 specialization](fixed_logs.md).

### Inferences

The specialization satisfies every hypothesis: \(h(2)=\log2<2\) and \(h(3)=\log3<2\); a relation between the two real logarithms would give \(2^u3^v=1\), forcing \(u=v=0\) by prime valuations. The last coefficient is nonzero. Equal height choices make \(B=\max(1,m,n)\), without hidden coefficient-dependent heights. Consequently fixed effective \(c>0,K\ge1\) satisfy
\[
|m\log2-n\log3|>c\max(1,m,n)^{-K}.
\tag{A1}
\]
There is no illicit passage from integer to arbitrary algebraic or real coefficients. — [Independent specialization of Theorem 2.1](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3).

### Gaps

- The established external theorem is an input; its complete 53-page proof is not reconstructed. No historical novelty claim is made for its elementary specialization. The huge explicit constants and eventual threshold are not optimized.

## Do all scale conversions, boundary estimates and signs survive adversarial review?

### Takeaway

**PASS, with no substantive correction.** On every sufficiently late balanced nonresonant first mediant with a nonresonant current model, the complete first-mediant jump dominates the full remainder. The uniform relative expansion is also justified. — [Accepted complete jump and variation identities](../signed-arithmetic-returns/signed_scalar.md), [accepted actual-response expansion](../response-closure-tests/response_relations.md), [new derivation](fixed_logs.md).

### Cited Findings

- For consecutive actual convergents \(p/q,P/Q\) of \(\alpha=\log2/\log3\), put \(r=p+P,s=q+Q\), \(\sigma=\operatorname{sign}(\alpha-p/q)\), and \(E=Z-\widetilde Z^\sigma_{p,q}\). The accepted complete identity is
  \[
  |E-\sigma J|\le R,\quad
  J=(2^{-s}-3^{-r})\mathcal Q_{r,s}(1/2,1/3),
  \]
  where \(R\) is the sum of both entire open-child Farey variations. On the four stated balanced nonresonant mediant states, \(|\mathcal Q|>1/20\). The origin, low rows and infinite quotient exteriors are retained. — [SS1–SS4](../signed-arithmetic-returns/signed_scalar.md).
- The actual-response error bound is
  \[
  |E-\sigma\Delta G_R|
  \le R+|\Delta|\left(\frac{45}{2}2^{-s}+\frac{63}{2}3^{-r}\right),
  \quad \Delta=2^{-s}-3^{-r},\quad |G_R|>1/20.
  \]
  — [RR7 and the four complete response enclosures](../response-closure-tests/response_relations.md).

### Inferences

**Earlier-denominator scale.** Eventually \(0<p<q\), \(Q>q\ge2\). The standard continued-fraction inequality \(|q\alpha-p|<1/Q\), combined with (A1), gives
\[
Q<C_1q^K,\qquad s<C_2q^K,
\quad C_1=\max(1,\log3/c),\quad C_2=1+C_1.
\]
Since \(0<r<s\), a second use of the *same* fixed-logarithm theorem gives
\[
|s\log2-r\log3|>c s^{-K}>c_2q^{-K^2},
\qquad c_2=cC_2^{-K}>0.
\tag{A2}
\]
These steps require neither bounded \(Q/q\) nor a condition on the next partial quotient. — [Source specialization and claimed conversion independently reconstructed](fixed_logs.md).

**Exponential conversion.** Write \(\delta=q\alpha-p\), \(\delta'=Q\alpha-P\). Both errors have absolute value less than \(1/Q\), hence \(|\Lambda|=\log3\,|\delta+\delta'|<1\) eventually. Since
\(\Delta=2^{-s}(1-e^\Lambda)\), the mean-value theorem and (A2) imply
\[
|\Delta|>e^{-1}c_2\,2^{-s}q^{-K^2}.
\tag{A3}
\]
This is a lower bound on the **old** \(q\)-scale, not merely a subexponential estimate in the possibly much larger \(s\). — [FL5–FL7](fixed_logs.md).

**Complete uniform remainder.** For a Farey pair \(a/b,c/d\), let \(A=b+d,B=a+c\). The accepted variation is
\[
\mathcal V=9\left[2^{1-A}\left(1+\frac{A+1}{bd}\right)
+3^{-B}\left(\frac32+\frac{\frac32B+\frac34}{ac}\right)\right].
\]
For positive integer endpoint coordinates, its bracket factors are bounded by 4 and \(21/4\), respectively. In the two children, \(A\alpha-B\) equals \(2\delta+\delta'\) or \(\delta+2\delta'\), whose absolute value is below \(3/Q\le1\). Therefore \(3^{-B}\le3\,2^{-A}\) and
\[
\mathcal V\le\frac{855}{4}2^{-A},\qquad
R\le\frac{855}{2}2^{-(s+q)}<432\,2^{-(s+q)}.
\tag{A4}
\]
The second child's exponent is \(s+Q\ge s+q\). Both infinite variation tails are paid. — [Accepted SS3 formula](../signed-arithmetic-returns/signed_scalar.md), [audited FL8 constant](fixed_logs.md).

**Dominance and signs.** Combining \(|J|>|\Delta|/20\), (A3), and (A4),
\[
\frac{R}{|J|}<\frac{8640e}{c_2}q^{K^2}2^{-q}\longrightarrow0.
\]
Hence a fixed effective threshold works simultaneously for all four states. Eventually
\[
E\ne0,\quad \operatorname{sign}E=\operatorname{sign}(\sigma J),\quad
|E|>\frac{c_2}{40e}2^{-s}q^{-K^2}.
\tag{A5}
\]
Successive convergent errors have opposite signs and decreasing magnitudes, so \(\delta+\delta'\) has sign \(\sigma\). Thus \(\sigma\Delta<0\). The complete quotient and its corresponding \(G_R\) have the same sign, by their certified enclosures. In particular the eventual error sign is **minus the sign of \(G_R\)**: negative for states 1 and 4, positive for states 2 and 3. This agrees with the three exact examples. — [Four-state enclosures](../response-closure-tests/response_relations.md), [independent exact endpoint checks](fixed_logs_audit_check.py).

**Floor and domain qualifications.** The parent endpoints are Farey neighbors and the first mediant is reduced. The interval between it and the actual slope is contained in the open parent interval. Every interior rational has denominator at least \(s\) and numerator at least \(r\). Thus direct floors through \(s-1\) and reciprocal floors through \(r-1\) match the actual slope, and the first 23 floors are admissible once \(r,s>24\). This does not imply the balanced mediant state; that remains an explicit hypothesis. The current model must be nonresonant for the accepted scalar clearing theorem. The successor need not be nonresonant. — [SS4 endpoint argument](../signed-arithmetic-returns/signed_scalar.md).

**Relative expansion.** Divide the complete RR7 bound by \(|\Delta G_R|\). Its variation contribution is \(O(q^{K^2}2^{-q})\), while its quotient-approximation contribution is \(O(2^{-s}+3^{-r})=O(2^{-s})\), uniformly over the four states. This proves
\[
E=\sigma\Delta G_R\left(1+O(q^{K^2}2^{-q})\right).
\tag{A6}
\]
There is no missing division by an unboundedly small \(G_R\), because the uniform lower bound is \(1/20\). — [RR7](../response-closure-tests/response_relations.md), [FL11](fixed_logs.md).

### Gaps

- The accepted combinatorial foundation, four-state complete quotient enclosures and pure-jump variation representation are theorem inputs to this audit. Their full original proofs are not rebuilt here. Their exact hypotheses were checked against the new application.
- This theorem covers balanced nonresonant first mediants, not arbitrary unbalanced states or every actual index. Its effective threshold can be extremely large.

## What is actually verified, and does this complete the infinite arithmetic return?

### Takeaway

**PASS for the new theorem; NOT COMPLETE for the original goal.** The asymptotic five-versus-eleven child-sign split is unnecessary within the balanced-first-mediant domain. The missing joint actual state/gap supply remains open. — [Audited conditional theorem](fixed_logs.md), [previous restricted two-node theorem](../response-closure-tests/general_states.md).

### Cited Findings

- The supplied `fixed_logs_check.py` passes its three exact state, short-floor, variation and jump-dominance comparisons. The independent `fixed_logs_audit_check.py` also passes. It imports no project helper, computes the actual continued-fraction prefix through integer comparisons of powers of 2 and 3, verifies that the named pairs really are consecutive actual convergents, reconstructs the mediant Eisenstein states and floor prefixes, and evaluates both full variations with `Fraction`. — [Supplied checker](fixed_logs_check.py), [independent checker](fixed_logs_audit_check.py).
- The independent actual cases are \(12/19\to41/65\), \(53/84\to306/485\), and \(306/485\to665/1054\), with mediants \(53/84,359/569,971/1539\). All satisfy the complete lower-jump-versus-remainder comparison. — [Exact reproduction](fixed_logs_audit_check.py).
- The accepted arithmetic clearing is \(D_{p,q}=27(2^{3q}-1)(3^{3p}-1)\), and its error bound is \(D_{p,q}|E|\le486(1+o(1))2^{5q-Q}\). — [Accepted scalar arithmetic](../signed-arithmetic-returns/REPORT.md).

### Inferences

The new theorem applies before considering a child response, so both same-sign and opposite-sign child cases are covered whenever their first mediant has an admissible balanced state. In that precise domain all sixteen previously classified compatible children are handled asymptotically. This does not extend the finite numerical thresholds or invalidate the useful earlier two-node finite certificates. — [General-state classification and its explicit domain](../response-closure-tests/general_states.md), [uniform one-node proof](fixed_logs.md).

If an unbounded set of actual indices satisfies all three conditions

1. the current model is nonresonant;
2. its first mediant has one of the four balanced nonresonant states;
3. \(Q-5q\to+\infty\) along those same indices,

then (A5) and the accepted scalar bound yield nonzero cleared errors tending to zero. A hypothetical \(Z=A/B\) would make \(BD_{p,q}E\) a nonzero integer tending to zero, proving irrationality of \(Z\), hence of \(c=(Z+6)/9\). This implication is correct without an extra nonvanishing or child-sign premise. — [Audited FL7 conditional theorem](fixed_logs.md).

No argument here proves the three conditions occur jointly infinitely often. In particular \(Q\le Cq^K\) is an **upper bound**, and gives neither \(Q>5q\) infinitely often nor balanced-state frequency. No unknown response constant has been rationalized and no clearing factor has been reduced. — [Explicit remaining gaps](fixed_logs.md), [remaining response arithmetic](../response-closure-tests/response_relations.md).

### Gaps

- The infinite adequate state/gap supply, alternative hierarchy boundary arithmetic, arbitrary unbalanced-state nonvanishing, Lean, external review and priority verification are not established here.
- No substantive audit erratum was found. Small Markdown parenthesis inconsistencies in the research note do not affect the formulas or proof.

Skipped: reconstructing Matveev's full proof and optimizing constants. Material risk: uniform nonvanishing on eligible indices must not be presented as a proof that infinitely many adequate eligible indices exist.
