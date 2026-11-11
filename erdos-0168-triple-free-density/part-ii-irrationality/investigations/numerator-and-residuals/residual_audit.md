# Independent audit of corrected fan nonvanishing

## Does the complete successor-child decomposition prove the claimed uniform theorem?

### Takeaway

**PASS; no substantive erratum found.** On the stated balanced-parent domain and following-digit-\(\ge2\) subfamily, the complete corrected-fan residual has the claimed leading successor-child jump, remainder below \(1400\,2^{-2q-2Q}\), and uniform eventual nonvanishing. This is a theorem about the corrected residual, rather than a transfer of ordinary scalar nonvanishing. — [Audited proof](<corrected_residual.md>), [independent checker](<residual_audit_check.py>).

### Cited Findings

- The accepted complete fan theorem starts with consecutive actual convergents \(p/q,P/Q\) of \(\alpha=\log2/\log3\), a nonresonant current model, and a balanced nonresonant first mediant \((r,s)=(p+P,q+Q)\). Its canonical actual responses repeat with period three, while the complete rational quotients generally do not. Their discrepancy is bounded using the common rectangle \(a<s,b<r\), with \(\varepsilon=(45/2)2^{-s}+(63/2)3^{-r}\). — [Complete fan audit](<../correlated-return-arithmetic/fan_audit.md>).
- The accepted pure-jump representation, complete paired quotient factorization, and full open-Farey variation formula include the low rows and both infinite exteriors. Resonant jumps are valid analytic inputs without an assumed cheap resonant scalar clearing factor. — [Complete scalar jump theorem](<../signed-arithmetic-returns/signed_scalar.md>), [resonant grade extension](<../response-closure-tests/general_states.md>).
- The previously audited primary Matveev specialization gives fixed effective \(c>0,K\ge1\) with \(|m\log2-n\log3|>c\max(m,n)^{-K}\), and \(Q\le Cq^K\) at actual convergents. This audit checks the new scale conversion, accepting that external theorem and its established specialization. — [Primary Matveev, Theorem 2.1](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3), [prior primary-source audit](<../weighted-response-identities/fixed_logs_audit.md>).

### Inferences

**Crossing and indexing.** Put \(\delta=q\alpha-p\), \(\delta'=Q\alpha-P\), and \(a=a_{n+2}\), where \(p/q=p_n/q_n\). The next error satisfies \(\delta''=\delta+a\delta'\). Alternation and decreasing error magnitudes give
\[
\frac{|\delta|}{|\delta'|}=a+\frac{|\delta''|}{|\delta'|}\in(a,a+1).
\]
Consequently \(\delta+2\delta'\) has the current error's sign exactly when \(a\ge2\). The point
\[
W=w/t=(p+2P)/(q+2Q)
\]
lies between the first mediant and successor. It is crossed from the correct-side current endpoint to \(\alpha\) exactly in this digit case. At digit one the point is on the other side of \(\alpha\). This is an exact criterion, not a finite numerical heuristic. — [CR1](<corrected_residual.md>), [independent actual CF and power checks](<residual_audit_check.py>).

**Complete residual identity.** With \(\sigma=\operatorname{sign}\delta\), write
\[
\mathcal R_{\rm fan}=Z-z-\sigma\sum_{j=1}^3 C_j\Gamma_j.
\]
Subtracting the actual-response fan rather than the rational jump fan leaves the term
\[
\sigma\sum_{k\ge1}(2^{-Q-kq}-3^{-P-kp})(\mathcal Q_k-\Gamma_k).
\]
Its sign is not prescribed. Its full absolute bound is retained as \(\varepsilon\) times the sum of the two geometric masses. The other omitted jumps belong to the two open children of \((F_1,P/Q)\) at \(W\), or to an open gap between consecutive current-side fan points. Absolute convergence justifies this infinite decomposition and the current one-sided limit; no current-endpoint jump is inserted. — [CR2–CR3](<corrected_residual.md>), [accepted infinite coverage](<../correlated-return-arithmetic/fan_audit.md>).

Thus, precisely in the crossed case,
\[
|\mathcal R_{\rm fan}-\sigma J_W|\le B_*,
\]
where \(B_*\) is the sum of both complete \(W\)-child variations, the two separately summed fan-gap series, and the complete quotient-comparison product in CR3. Both child endpoint determinants are one. Their threshold pairs are \((2q+3Q,2p+3P)\) and \((q+3Q,p+3P)\); their logarithmic offsets are bounded by \(5/Q\) and \(4/Q\). For sufficiently late indices each child variation is at most \((855/4)2^{-A}\), and both exponents \(A\) are at least \(2q+2Q\). The other fan gaps contribute less than \(215\,2^{-(3q+2Q)}\), and the complete quotient comparison at most \(936\,2^{-2s}\). Consequently, for the elementary thresholds in the note,
\[
B_*<\left(\frac{855}{2}+\frac{215}{16}+936\right)2^{-2s}
=\frac{22031}{16}2^{-2s}<1400\,2^{-2s}.
\]
This reconstructs the constant independently. The infinite fan is summed separately in bases two and three, so no estimate assumes \(k\delta\) remains small for arbitrary \(k\). The additional fixed response-word matching thresholds are satisfied eventually, as required by the theorem. — [Accepted fan constants](<../correlated-return-arithmetic/fan_audit.md>), [new exact bound implementation](<residual_audit_check.py>).

**Uniform logarithmic scale.** Since \(t=q+2Q\le(1+2C)q^K\) and eventually \(0<w<t\), Matveev at \((t,w)\) gives
\[
|t\log2-w\log3|\ge c_1q^{-K^2}.
\]
Its absolute value is eventually below one, because it is \(\log3\,|\delta+2\delta'|<3\log3/Q\). Hence the mean-value bound gives fixed \(\eta>0\) with
\[
|\Delta_W|=|2^{-t}-3^{-w}|\ge\eta2^{-t}q^{-K^2}.
\]
The independently checked sixteen classes all have complete quotient magnitude exceeding \(1/20000\). Therefore
\[
\frac{B_*}{|J_W|}<\frac{28000000}{\eta}q^{K^2}2^{-q}\longrightarrow0.
\]
This proves eventual nonvanishing uniformly over the finite class list, with the source's lower bound \(\eta2^{-t}q^{-K^2}/40000\). All constants depend only on fixed theorem data and the finite family, not on a varying response coefficient. — [CR4–CR5 and source inputs](<corrected_residual.md>), [independent response certificates](<residual_audit_check.py>).

The Farey interval \((F_1,P/Q)\) gives matching direct and reciprocal floors through \(t-1,w-1\) for \(W\) and the actual slope. The accepted actual-response comparison therefore replaces \(\mathcal Q_W\) by its canonical actual value \(\Lambda_S\) with error \(O(2^{-t})\). Dividing the complete residual identity by \(|\Delta_W\Lambda_S|\) proves
\[
\mathcal R_{\rm fan}=\sigma\Delta_W\Lambda_S
\left(1+O(q^{K^2}2^{-q})\right).
\]
In the crossed case \(\sigma\Delta_W<0\); the eventual sign is minus the sign of \(\Lambda_S\). Resonant \(W\) presents no arithmetic issue for this analytic statement. — [CR6 and accepted actual-response comparison](<corrected_residual.md>).

### Gaps

- The complete prior finite optimum, canonical endpoint formula, pure-jump representation and Matveev specialization are explicit accepted inputs. This audit checks their new use; it does not reconstruct their full historical proofs. — [Accepted framework](<../correlated-return-arithmetic/REPORT.md>).
- No actual infinite supply of balanced parents with the required following digit is proved. Neither rationality of the response values under rational \(Z\) nor adequate full-model gcd saving follows from the analytic theorem. — [Stated remaining interfaces](<corrected_residual.md>).

## Do all sixteen classes and the actual certificates reconstruct independently?

### Takeaway

**PASS.** A standalone exact checker reproduces all ten response intervals, both positive corrected-residual certificates, and a separate full model/actual-target enclosure for the digit-one example. It imports no companion or archived project module. — [Independent checker](<residual_audit_check.py>).

### Cited Findings

- The supplied `corrected_residual_check.py` completes successfully and reproduces the advertised response intervals, ratios and digit-one enclosure. — [Supplied checker, rerun](<corrected_residual_check.py>).
- The new checker constructs actual axes directly from original colored-board counts, implements the row birth tests as differences of minima, and checks target coefficients against the accepted exact finite-cover formula at six cells, including the origin exception. Its numerical work is entirely integer or `Fraction` arithmetic. — [Standalone reconstruction](<residual_audit_check.py>).
- The checker closes the residue/commutator graph on 24 states, independently inverts the four balanced mediant equations, selects sixteen current-parent orientations, and derives the successor children using the two Christoffel concatenation formulas. Exactly ten canonical child states result. — [Independent graph and endpoint construction](<residual_audit_check.py>).

### Inferences

All ten six-decimal enclosures in the source reproduce with a complete quotient exterior \((27/2)2^{-48}+(45/2)3^{-48}\). The smallest new magnitude is in \((.000055,.000056)\), so the uniform \(1/20000\) lower bound is valid and \(1/10000\) would be invalid. The two added states are \((0,2,-\omega)\) and \((1,0,3)\); there is no claim of their infinite occurrence. Low-row minimum differences and the canonical positive-index origin convention are retained. — [Exact state checks](<residual_audit_check.py>).

For actual inputs the checker first constructs rigorous logarithm intervals from the positive atanh series with explicit tails. Shared continued-fraction floors certify the current/successor pairs and their following digits. Integer powers separately check the side of each rational point. The finite certificates independently yield:

| Current / successor | Successor child | Complete leading/remainder ratio | Corrected sign |
|---|---|---:|---|
| \(53/84,306/485\) | \(665/1054\), resonant | \(>4288019834875106187\) | positive |
| \(306/485,665/1054\) | \(1636/2593\) | \(>2^{400}\) | positive |

These are certified by the full residual identity and exact complete-tail inequalities; a direct huge target rectangle is unnecessary for these two cases. The separate complete target/model evaluation is performed for the digit-one case below. — [Independent actual prefix, common floors, variations and inequalities](<residual_audit_check.py>).

### Gaps

- Finite checks certify the state list and named inputs. The infinite theorem rests on the written complete decomposition, convergence, uniform tails and Matveev comparison; it is not extrapolated from finite values. — [Audited CR1–CR6](<corrected_residual.md>).
- No new original-token enumeration for the large resonant child was run. The resonance-independent quotient theorem is an accepted input; the independent current audit uses original-board axes and minimum-difference response tests. — [Earlier resonant theorem audit](<../correlated-return-arithmetic/supply_audit.md>).

## Precisely what does digit one disprove, and is the original goal complete?

### Takeaway

**The finite all-digit retained-jump estimate fails on the stated actual input; general corrected-residual nonvanishing is not disproved.** The main following-digit theorem passes. The original infinite arithmetic-return goal remains incomplete. — [Independent finite enclosure](<residual_audit_check.py>), [source scope](<corrected_residual.md>).

### Cited Findings

- The exact actual pair \(12/19\to41/65\) has following digit one. Its current rational is above \(\alpha\), but \(94/149\) is below it. Thus that successor child is not part of the current-to-actual jump path. — [Independent actual CF and integer-power comparisons](<residual_audit_check.py>).
- The standalone checker evaluates the full periodic rational current model independently, with its exceptional origin contribution removed exactly once. It encloses the actual target using a column-major \(260\times180\) integer Horner sum plus both exterior strips. Each \(192\times192\) actual response uncertainty is multiplied by its exact rational fan coefficient before forming the corrected interval. — [Independent complete model/target/response enclosure](<residual_audit_check.py>).

### Inferences

The complete exact intervals reproduce
\[
-2^{-175}<\mathcal R_{\rm fan}<-2^{-176}.
\]
The incorrectly inserted term has \(\sigma J_{94/149}>0\), with its complete lower bound greater than the same proposed \(B_*\). Since the actual residual is negative,
\[
|\mathcal R_{\rm fan}-\sigma J_{94/149}|>B_*.
\]
This refutes the all-digit version of the finite CR2 estimate at this input. **The example itself has a nonzero residual.** It therefore does not refute a possible all-digit nonvanishing theorem. A single finite example also cannot refute a statement with an unspecified sufficiently-late threshold. The proof's structural crossing condition remains essential, and a universal eventual extension would need a separate argument. The source's wording about an unconditional extension should be read in this precise finite-estimate sense. — [Independent exact false-estimate certificate](<residual_audit_check.py>).

The audit's final disposition is PASS with no substantive mathematical correction. The new result removes corrected-residual nonvanishing on the explicit following-digit subfamily, while leaving actual infinite applicability and the full response/denominator arithmetic open. It establishes no unrestricted digit-one theorem, hierarchy residual theorem, algebraic independence or solution of Erdős #168(ii). — [Audited theorem and remaining obligations](<corrected_residual.md>), [previous arithmetic interface](<../correlated-return-arithmetic/arithmetic_audit.md>).

### Gaps

- Skipped Lean, external review, historical priority, optimized constants and full reproofs of accepted foundation/Matveev theorems. Both supplied and standalone independent checkers pass; the latter runs in approximately half a second. Material risk: extending the crossed-jump formula beyond its digit condition or presenting a conditional nonzero real residual as an adequate infinite arithmetic return.
