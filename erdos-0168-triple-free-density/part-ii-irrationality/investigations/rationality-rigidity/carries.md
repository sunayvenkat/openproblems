# Mixed tails expose the missing carry arithmetic

## What carry constraint actually follows from rationality of the full target?

### Takeaway

The bounded mixed-tail field has an exact integer-coefficient recurrence, but rationality at its corner does not propagate to its boundary axes. A common rational lattice on **both** boundary axes would propagate everywhere; obtaining that lattice from rationality of the actual target remains unproved. The proposed bounded-integer-carry argument therefore has a missing boundary-arithmetic premise. — [Exact certificate](carries_check.py), [accepted complete normalization](../numerator-and-residuals/occupation_audit.md).

### Cited Findings

- Write the actual unexceptional births as \(h_{ab}\in\{0,1\}\). The target is \(Q=\sum h_{ab}2^{-a}3^{-b}=Q_{\rm full}(0)\), with \(Z=2-3Q=9c-6\). The original birth at \((0,1)\) is handled by the existing constant two; no override is added to translated tails. All low rows remain in these sums. — [Normalization and actual kernels](../numerator-and-residuals/occupation_audit.md), [complete transport](../occupation-arithmetic-bridge/exact_transport.md).
- The checker independently evaluates a finite actual birth rectangle using the accepted finite-cover formula, including the isolated-root and patch corrections. It checks the true birth at three and its unexceptional removal, Boolean values, exact mixed-tail recurrence and a direct weighted sum. This is a finite formula check, not a proof of infinite rationality or irrationality. — [Checker](carries_check.py), [accepted global finite theorem](../prefix-and-phase-audit/REPORT.md).

### Inferences

**Carry lemma.** For any bounded Boolean array, define
\[
R_{ab}=\sum_{i,j\ge0}2^{-i}3^{-j}h_{a+i,b+j}.
\]
Absolute convergence gives \(0\le R_{ab}\le3\), and inclusion-exclusion gives
\[
6R_{ab}-3R_{a+1,b}-2R_{a,b+1}+R_{a+1,b+1}=6h_{ab}. \tag{1}
\]
Consequently, if a fixed positive integer \(B\) clears **every** \(R_{a0}\) and \(R_{0b}\), induction using (1) clears every \(R_{ab}\). The scaled values then lie in the finite integer alphabet \(\{0,\ldots,3B\}\). Rationality of \(R_{00}\) alone supplies only one value of those two infinite boundaries. More explicitly,
\[
R_{10}=2\left(Q-\sum_{b\ge0}3^{-b}h_{0b}\right).
\]
The removed column is an infinite weighted readout, not an integer digit. — [Recurrence and finite-lattice checks](carries_check.py); the infinite equalities follow directly by absolutely convergent reindexing above.

One can always round the bounded real field, but this does not create an exact integer carry. For \(k_{ab}=\lfloor BR_{ab}\rfloor\), define
\[
\epsilon_{ab}=6k_{ab}-3k_{a+1,b}-2k_{a,b+1}+k_{a+1,b+1}-6Bh_{ab}.
\]
Writing \(e_{ab}=BR_{ab}-k_{ab}\in[0,1)\) in (1) gives
\[
\epsilon_{ab}=-6e_{ab}+3e_{a+1,b}+2e_{a,b+1}-e_{a+1,b+1}\in\{-6,\ldots,4\}.
\]
The complete discounted pairing telescopes to
\[
\sum_{a,b\ge0}2^{-a}3^{-b}\epsilon_{ab}
=6k_{00}-6BQ=-6\{BQ\}. \tag{2}
\]
Thus hypothetical rationality \(Q=A/B\) gives a bounded integer **defect array of total weight zero**, not pointwise zero defect. The proof uses boundedness of \(k\) to remove all terminal strips. It supplies no affordable return by itself. — [Exact recurrence](carries_check.py), [accepted form of complete terminal pairing](../occupation-arithmetic-bridge/exact_transport.md); equations (1)–(2) are proved here.

### Gaps

- No special property of the actual floor/cocycle births has been proved that makes their boundary axes lie in one rational lattice under rationality of \(Q\), or makes the rounded defect vanish. Without that theorem, a finite carry alphabet or a finite automaton cannot be inferred. — [Existing joint-readout limitations](../occupation-arithmetic-bridge/exact_transport.md).

## Can a rational total coexist with an irrational boundary and a nonzero carry defect?

### Takeaway

Yes, even for a Boolean array avoiding the actual forbidden motif \(1001\). The explicit irrational boundary calculation below breaks the proposed generic propagation implication. **This array is not the actual Erdős birth array:** it does not obey the actual global floor/cocycle conditions, and it is no counterexample to the conjecture. — [Certificate](carries_check.py), [earlier motif limitation](../reflected-return-models/actual_carries.md).

### Cited Findings

- The actual high array excludes \(1001\), but that local restriction alone already has rational aperiodic countermodels. The present calculation uses an elementary equal-mass block to identify a particular irrational missing boundary, rather than claiming a new language criterion. — [Prior actual-carry analysis](../reflected-return-models/actual_carries.md).
- For each \(k\ge0\), choose one of two two-row, two-column blocks, with all columns \(a\ge2\) zero:
  \[
  A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
  B=\begin{pmatrix}0&0\\1&1\end{pmatrix}.
  \]
  Rows are \(b=2k,2k+1\), columns are \(a=0,1\). Each block has weighted mass \(\tfrac12 9^{-k}\), since \(1/2=1/3+1/6\). Every internal and adjacent-block square avoids \(1001\). The checker exhausts all four adjacent block choices. — [Exact block and boundary checks](carries_check.py).

### Inferences

Take block \(B\) precisely when \(k\) is a positive square, and otherwise take \(A\). Put
\[
G=\sum_{k\ge0}9^{-k}\mathbf1_{\{k\text{ is a positive square}\}}.
\]
Its base-nine digits are zero or one, with infinitely many ones and unbounded zero runs. They cannot be eventually periodic. A rational base-nine expansion is eventually periodic by finite remainder states in long division; digits zero and one exclude the alternate terminating/all-eight representation. Hence \(G\) is irrational. Direct summation gives
\[
Q=\frac9{16},\qquad R_{10}=\frac98-\frac23G\notin\mathbb Q,
\qquad R_{01}=\frac3{16},\qquad R_{11}=3R_{10}-3.
\tag{3}
\]
All statements concern this explicitly defined countermodel. — [Block identities and rational enclosures](carries_check.py); irrationality follows by the full digit argument just given.

Even canonical rounding fails locally. For \(B=16\), exact bounds using the first two square positions and the entire remaining geometric tail prove
\[
\lfloor16R_{00}\rfloor=9,\quad \lfloor16R_{10}\rfloor=16,
\quad\lfloor16R_{01}\rfloor=3,\quad\lfloor16R_{11}\rfloor=2.
\]
Since \(h_{00}=0\), its origin defect is \(54-48-6+2=2\ne0\), although (2) has total zero. This distinguishes zero weighted defect from a pointwise integer recurrence. — [Exact strict interval and defect checks](carries_check.py).

### Gaps

- No necessary carry condition contradicting the **actual** Erdős array has been established. The outstanding issue is actual joint boundary arithmetic under rationality of the single target value, followed by affordable clearing on a nonzero infinite family. The ordered rational-source construction and generic Farey equivalence do not supply that premise. — [Latest accepted status](../arithmetic-renewal/REPORT.md).
- Skipped Lean, external theorem searches, novelty checks and further directions after the user's stop-after-this-round instruction. Material risk: treating this generic Boolean-array countermodel as the actual dynamics, or treating rationality at one corner as rationality of an infinite boundary.
