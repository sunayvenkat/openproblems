# Independent audit of the convex source intervals

## Does the five-row obstruction have its claimed scope?

### Takeaway

**PASS.** The witness excludes state-only potentials with arbitrary additive pure-phase forcing on the **full lifted radius-one box**, when the target coefficient is nonzero. It does not exclude genuinely phase-dependent potentials or equality required only on actual occupied state/phase pairs. — [C5][convex], [independent checker][check].

### Cited Findings

- Exact phase-cut enumeration, including right-continuous endpoint values, gives horizontal alphabet \(\{0,\pm1,\pm\omega,\pm\omega^2\}\) and corrected vertical alphabet \(\{0,1,\omega,\omega^2\}\) in block \(i=j=0\). Rational logarithm enclosures certify every ordering and floor. The phases \(1/16,1/6,1/100\) lie off all cuts and give the required drifts \(0,\omega,0\). — [Actual lifted definitions][transport], [independent enumeration][check].
- The checker generates the five operator rows from \(216I-27U_A-8U_B+U_AU_B\), rather than merely checking a copied matrix. For columns \(P(-\omega),P(0),P(\omega),g_0,g_1\), their coefficients are
  \[
  (182,0,0,-1,0),\ (0,182,0,-1,0),\ (0,0,182,-1,0),
  \]
  \[
  (208,-26,0,0,-1),\ (0,208,-26,0,-1).
  \]
  The weights \((-8,9,-1,7,-7)\) annihilate every column and pair to one with target \((0,1,1,0,1)\). Hence \(\lambda=0\); approximate equality requires \(|\lambda|\le32\varepsilon\). — [C5][convex], [generated witness][check].

### Inferences

An added pure-phase potential is absorbed into the arbitrary forcing, because its operator image is pure phase. The ordered construction escapes this obstruction by genuine interaction between state and phase. The witness does not assert that its five combinations occur on the actual orbit. — [C5 limitations][convex], [ordered construction][renewal].

### Gaps

At audit start, the symbolic note attributed a full-phase radius-zero joint-termination theorem to the convex researcher. No such theorem appears in the finalized convex note or checker. The coordinator confirmed it was an interim idea; the symbolic auditor corrected the current note and recorded the correction. No joint-path theorem is accepted here. — [Symbolic audit][symbolicaudit], [finalized convex note][convex].

## Do the boundary constants give the complete rational interval?

### Takeaway

**PASS.** Bounded rational boundary constants give the stated affine source interval and positive complete paired residual. Only the final model denominator needs clearing. — [C1–C8][convex], [independent source reconstruction][check].

### Cited Findings

- With \(c_A\in[1/7,2/7]\), \(c_B\in[1/26,2/26]\), the ordered first-exit formulas give finite rational phase-step functions, \(q\le3/7\), \(p\le17/182\), and exterior residual bounds
  \[
  e_A\in[6/7,17/7],\qquad e_B\in[179/182,381/182].
  \]
  Re-entry is included. For the first lower bound, retain the correlated bound \(q_A\le c_A+1/7\). — [C1–C2][convex], [exit formulas][renewal].
- The derivative bounds are valid: \(0\le r_A\le1\), \(0\le s_A\le1/26\), \(0\le s_B\le1\). The constant \(1/26\) is a supersolution for \(s_A\), including its exterior boundary. Outside, the residual derivatives lie in \([7,8]\), \([0,1/26]\), and \([26,27]\), respectively. Thus varying \(c_A\) adds a nonnegative vertical correction. — [C3][convex].
- For common \(\theta\), \(S_\theta=S_0+\theta W\), \(W=W_A+W_B\). The horizontal baseline-to-variation lower ratio is \(3/4\); the vertical ratio is \(18/19\). Summing the **complete positive pairing**, retaining its factor eight, gives
  \[
  \frac34W\le\Psi_0\le\frac97W_A+\frac{191}{182}W_B\le\frac97W.
  \]
  This does not assume pointwise positivity of the product residual. Consequently every rational \(r\in[S_0,S_0+W]\) is realized and satisfies \(0<r-Q_{\rm full}(0)\le16W/7\). Accepted residual decay gives \(W_R\to0\). — [C4–C8][convex], [complete pairing][renewal].
- The independent checker reads both JSON files as fixtures but independently reconstructs every source total at \(R=0,1,2\), using integer-floor axis recurrences and original isolate/patch inequalities. It checks all nine high and twelve low entries, their recorded horizons and numerators, and \(S_0,W_A,W_B\). It verifies both zero-row versions. The identically zero row contributes equally to \(S_0\) and \(W_A\); deleting both contributions preserves normalization and every comparison. — [Source fixture][data], [certificates][results], [independent reconstruction][check].

### Inferences

For \(z=2-3r\) and \(D=\operatorname{den}(z)\), hypothetical \(Z=A/B\) makes \(BD(Z-z)\) a positive integer. Internal denominators of the parameters and potentials need not be cleared; their amplitudes stay bounded. The local CRT lemma cancels a vertical factor under its stated width condition, but supplies neither cheap aggregate denominators nor a requirement to clear every internal coefficient. — [C8][convex], [local R18][renewal].

### Gaps

Uniform one-axis exit, complete normalization, infinite support and decay remain accepted foundation inputs, separately audited by the renewal auditor. Finite reconstruction checks their application and source arithmetic, not their infinite proofs. — [Renewal foundations][renewal].

## Are the finite certificate and irrationality equivalence valid?

### Takeaway

**PASS.** The finite certificate is correct. The infinite optimized criterion remains exactly the original irrationality problem. — [C4][convex], [independent checker][check].

### Cited Findings

- Independent iterative Euclid plus exhaustive exclusion of every smaller denominator gives models \(-7,0,5201/4303\); deleting row zero gives \(-1,9/8,5201/4303\). Optimality at radius two excludes every denominator through 4302. — [Results][results], [independent optimality checks][check].
- An independently reconstructed original-board \(96\times96\) target head, with complete Boolean tail \(3(2^{-96}+3^{-96}-6^{-96})\), confirms
  \[
  0<4303\left(Z-\frac{5201}{4303}\right)<2^{-10}.
  \]
  The sensitivity bound independently verifies the same inequality. This excludes target denominators at most \(2^{10}\), weaker than the accepted prior \(2^{56}\) exclusion. — [Exact enclosure][check], [prior exclusion and normalization][calibration].

### Inferences

Every interval has length \(3W_R\), lies below \(Z\), and satisfies \(9W_R/4\le Z-z\le48W_R/7\). If \(Z\) is irrational, minimum denominators \(q\) tend to infinity. Farey parents \(a/b,c/d\) obey \(bc-ad=1\), \(b+d=q\), and surround the whole closed interval by minimality. Hence \(qW_R\le(1/b+1/d)/3\). Each parent approaches \(Z\); a bounded parent denominator would force a fixed rational subsequence approaching \(Z\). Thus both parent denominators diverge and \(D_RW_R\to0\). The parent algebra and actual interval containment are independently checked. — [C9][convex], [Farey checks][check].

Conversely, rational \(Z=A/B\) gives \(1/(BD_R)\le Z-z_R\le48W_R/7\), so \(D_RW_R\ge7/(48B)\). This proves the claimed equivalence, with no independent arithmetic supply or completion of Erdős #168(ii). — [C10][convex].

### Gaps

The supplied checker passed once and left the saved certificate unchanged. The standalone checker imports no project code, writes nothing, and passes all stated checks. Reproduce with Python 3.14, the -B flag, and the linked checker. No archived file was edited. — [Supplied checker][supplied], [independent checker][check].

Skipped Lean, installations, external posts, novelty checks and new research. Material risk: treating aggregate rationalization or this generic equivalence as the missing arithmetic supply.

[convex]: <convex.md>
[renewal]: <renewal.md>
[data]: <renewal_source_data.json>
[results]: <convex_interval_results.json>
[supplied]: <convex_check.py>
[check]: <convex_audit_check.py>
[symbolicaudit]: <symbolic_audit.md>
[transport]: <../occupation-arithmetic-bridge/exact_transport.md>
[calibration]: <../finite-volume-calibration/REPORT.md>
