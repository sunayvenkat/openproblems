# Fresh audit of the four actual responses

## Are the canonical arrays and their complete approximation bounds correct?

### Takeaway

**PASS; no substantive erratum found.** The four constants are well-defined actual-axis series without any infinite state-frequency assumption. Their stated rational-model approximation and the complete nonzero enclosures reconstruct, with all low rows and both infinite sides retained. The supplied checker and an independent checker both pass. — [Response proof](response_relations.md), [supplied checker](response_relations_check.py), [independent checker](response_audit_check.py).

### Cited Findings

- The accepted scalar input is the complete toric quotient, with coefficients bounded by \(3(1+b/p)\), and the low-coefficient equality \(Q^{p,q}_{a,b}=c^+_{q+a,b}-c^-_{q+a,b}\) when \(b<p\). Its low-row and origin conventions are part of the input, not reconstructed from an uncorrected high-row rule. — [SS1–SS6](../signed-arithmetic-returns/signed_scalar.md).
- The canonical endpoint table is
  \[
  (p_0,q_0,e_R,\gamma_R)=
  (0,1,-\omega,\omega^2),\quad
  (1,1,0,\omega),\quad
  (2,0,1,\omega),\quad
  (2,2,1,\omega^2).
  \]
  The independent checker reconstructs these endpoints from direct rational-floor sums, and reconstructs actual \(A_a,B_b\) from the original smooth board rather than the companion axis-increment tables. — [RR1](response_relations.md), [independent endpoint and board calculations](response_audit_check.py).
- The independent rational-model calculation enumerates original colored tokens, applies their exact effective exponents, groups duplicate arrivals, and processes rational grades with the two opposite tie orders. It imports no companion or archived code. It recovers the claimed local quotient coefficients at \(5/8,12/19,41/65,53/84\), and checks complete quotient enclosures with explicit coefficient tails. — [Independent rational-grade certificate](response_audit_check.py).

### Inferences

**A1. The shifted-axis formula is exact on the stated rectangle.** For \(0\le a<q\), coprimality ensures that the positive indices \(1,\ldots,a\) contain no additional rational tie. The shifted horizontal increment is therefore
\[
A^+_{q+a}-A^+_q
=\sum_{k=1}^a\omega^{-q-k}S\!\left(p+\lfloor kp/q\rfloor\right).
\]
The elementary root-sum identity
\[
S(p+m)=S(p-1)+\omega^{2p}S(m)
\]
gives
\[
A^+_{q+a}
=e_R+\omega^{2p-q}(A_a-1)
 +\omega^{-q}S(p-1)\sum_{k=1}^a\omega^{-k}.
\]
It uses only \(p,q\bmod3\), the exact endpoint \(e_R\), and the actual short floors. The negative endpoint subtracts \(\gamma_R\), while every subsequent increment is common to the two sides. For \(b<B\le p\), the reciprocal floors have no positive-index rational ties, so the vertical axis and all \(b,b-1,b-3\) correction tests agree with the actual ones. The residue term depends only on \(a+q_0,b\bmod3\). — [RR1–RR2](response_relations.md), [accepted endpoint formula SS6](../signed-arithmetic-returns/signed_scalar.md).

The model horizontal index is \(q+a>0\). Hence the exceptional original birth at \((0,1)\) must not be inserted into the new response even at its reindexed \(a=0\). The original target \(c\) retains that exception. The four separate low-row functions, and the high-row correction only for \(b\ge4\), are used consistently. — [Canonical definitions](response_relations.md), [minimum-difference birth reconstruction](response_audit_check.py).

**A2. The actual constants exist before any supply theorem.** The explicit formula defines \(g_R(a,b)\) at every actual index, and each coefficient lies in \(\{-3,0,3\}\). Thus
\[
G_R=\sum_{a,b\ge0}g_R(a,b)2^{-a}3^{-b}
\]
is absolutely convergent. This definition needs neither an actual subsequence of state \(R\) nor a rationality assumption on \(Z\). If a sequence of reduced rationals approaches the actual irrational slope in that fixed state, every fixed finite direct/reciprocal floor prefix eventually agrees and \(p,q\) tend to infinity. The convergence statement is conditional on such a sequence, while the definition of \(G_R\) is unconditional. — [RR1–RR4](response_relations.md).

**A3. Both omitted exteriors are paid.** The model quotient coefficient bound gives, for \(B\le p\), an exterior of at most
\[
\frac{27}{2}2^{-A}+\frac{45}{2}3^{-B}.
\]
For the actual canonical array, the bound \(|g_R|\le3\) gives an exterior no larger than \(9(2^{-A}+3^{-B})\); overcounting the intersection is harmless. The coefficients agree inside \(a<A,b<B\). Consequently
\[
\left|\mathcal Q_{p,q}(1/2,1/3)-G_R\right|
\le \frac{45}{2}2^{-A}+\frac{63}{2}3^{-B}.
\]
No boundary or negative-coordinate term is removed in this comparison. For a state-fixed approaching sequence, one first fixes a rectangle and then increases it; this proves convergence without a rate or state-frequency assumption. — [RR4 and the complete quotient input](response_relations.md), [independent weighted bounds](response_audit_check.py).

The independent \(24\times24\) canonical calculation uses the exact tail \(9(2^{-24}+3^{-24})\) and verifies
\[
G_1\in(9/20,1/2),\quad
G_2\in(-3/50,-1/20),\quad
G_3\in(-11/10,-1),\quad
G_4\in(7/5,3/2).
\]
These are enclosures for the complete actual constants. They prove nonzero real values, not rationality or algebraicity. — [Independent enclosure certificate](response_audit_check.py).

### Gaps

- No actual infinite frequency of any balanced rational state is proved by this audit. — [Supply scope](response_relations.md).
- No implication \(Z\in\mathbb Q\Rightarrow G_R\in\mathbb Q\), or \(G_R\in\mathbb Q+\mathbb QZ\), is established. Four fixed real coefficients do not meet a fixed-rational-coefficient seed hypothesis merely by being fixed. — [Remaining response arithmetic](response_relations.md), [seed hypotheses](../signed-arithmetic-returns/seed_arithmetic.md).

## Are the ray dictionary and the coefficient obstruction valid in their stated scope?

### Takeaway

**PASS.** Every ray formula follows by subtracting the two integer-state tests, including all equality cases. The high-row contributions are genuinely nonzero, and the six actual coefficient vectors have determinant magnitude \(243\). The determinant excludes only the stated same-index constant-coefficient identity. — [RR3–RR6](response_relations.md), [independent ray and determinant certificate](response_audit_check.py).

### Cited Findings

- The independent checker encodes births by minimum differences, separately from the supplied inequality implementation. For example, the high-row birth is \(\min(x,y,0)-\min(x-1,y,0)\), row two is \(\min(x+1,y+1,0)-\min(x,y+1,0)\), and row three is \(1+\min(x,y,0)-\min(x,y+1,0)\). — [Independent minimum representation](response_audit_check.py).
- The six original target coefficients are independently reconstructed by the original smooth board and its isolate/patch corrections, with the original integer insertion cutoffs. The response coefficients are obtained through actual board axes. — [Independent original-board calculation](response_audit_check.py).

### Inferences

**A4. The high-row rays and all low-row signs are exact.** With \(z=x+y\omega\), subtraction by \(\omega\) changes \(y\) to \(y-1\). In high rows, this removes exactly the boundary \(x=y\le0\); in low rows one, two and three it removes respectively \(x\ge1,y=0\), \(x=y\le-1\), and \(y=\min(x,0)\). Multiplication by \(-3\) gives the negative entries in the dictionary. These are elementary integer inequalities, not an inference from finitely many orbit points. — [Exact ray table](response_relations.md).

Subtraction by \(\omega^2=-1-\omega\) changes \((x,y)\) to \((x+1,y+1)\). In high rows the difference is the boundary \(x=0,y\ge0\); in row two it is \(x=-1,y\ge-1\), both with coefficient \(-3\). Row three gains the boundary \(x\ge0,y=-1\), with coefficient \(+3\). Row one gains the disjoint sets \(x=0,y\ge-1\) and \(x\ge1,y=-1\), each with coefficient \(+3\). Row zero is identically zero in both directions. Thus no low-row term is included in a high-row approximation. — [Exact ray table and independent minimum checks](response_relations.md), [certificate](response_audit_check.py).

For each state the high-row response is \(-3\) times a nonnegative indicator. Actual witnesses are \((4,23),(5,11),(5,4),(4,16)\), respectively. Hence each corresponding high-ray weighted profile is strictly positive, and deleting it changes the complete response. In particular the exact expression \(G_R=L_R-3T_R\) contains both the one-dimensional low-row rays and a two-dimensional high-row ray; the current proof evaluates neither arithmetically. — [RR5](response_relations.md), [independent witness checks](response_audit_check.py).

**A5. The determinant has only a coefficientwise consequence.** The independent original-board reconstruction gives the six rows
\[
\begin{pmatrix}
1&1&0&0&0&0\\
1&1&0&0&0&-3\\
1&1&-3&0&0&-3\\
1&1&0&0&-3&0\\
1&-2&0&0&0&0\\
1&1&0&-3&0&0
\end{pmatrix}
\]
at the six stated actual points. Its determinant has absolute value \(243\). Therefore a constant-coefficient pointwise identity among \(1,c,g_1,g_2,g_3,g_4\) on the whole high-row actual array must be trivial. This proves the narrow obstruction as stated. — [RR6](response_relations.md), [independent determinant](response_audit_check.py).

Summing coefficients with weights can introduce exact cancellations or boundary identities invisible to this matrix. Thus it does not exclude a weighted value relation, a shifted-array identity, an evaluation-specific coboundary, or a further implication of target rationality. It supplies no numerical rational independence or irrationality statement about \(G_R,L_R,T_R\). — [Stated rank-test scope](response_relations.md).

### Gaps

- The weighted boundary-ray values are still present; coefficient rank does not evaluate them. — [RR5–RR6](response_relations.md).
- Any claimed rational closure would need an additional actual weighted identity, with its shifted sides and all low rows charged. No such identity is provided here. — [Remaining closure gap](response_relations.md).

## Does the fixed-response error expansion retain the full Farey remainder?

### Takeaway

**PASS as an absolute-error reduction.** The same four actual constants give the leading term at every applicable mediant, with both child variations and the quotient approximation explicitly retained. The result supplies no relative leading-term estimate when the physical gap is exceptionally small, and no infinite arithmetic return by itself. — [RR7–RR8](response_relations.md), [prior complete Farey criterion](../signed-arithmetic-returns/signed_scalar.md).

### Cited Findings

- The previously audited cluster theorem starts on the correct side of the current actual convergent, crosses the first mediant, excludes the successor endpoint, and charges all other jumps in both open children. It gives \(\left|(Z-\widetilde Z)-\sigma J\right|\le R_{\rm child}\). — [SS3–SS4](../signed-arithmetic-returns/signed_scalar.md).
- Any rational strictly inside the parent Farey interval has denominator at least \(s=q+Q\) and numerator at least \(r=p+P\). Hence the mediant and actual slope agree on direct floors through \(s-1\) and reciprocal floors through \(r-1\). This remains valid for a semiconvergent. — [Accepted domain proof](../signed-arithmetic-returns/signed_scalar.md).

### Inferences

**A6. The triangle inequality gives the exact charged form.** Apply the quotient approximation with \(A=s,B=r\), and write \(\Delta=2^{-s}-3^{-r}\). Since \(J=\Delta\mathcal Q_{r,s}(1/2,1/3)\),
\[
\left|(Z-\widetilde Z)-\sigma\Delta G_R\right|
\le R_{\rm child}
+|\Delta|\left(\frac{45}{2}2^{-s}+\frac{63}{2}3^{-r}\right).
\]
The extra term is not omitted and is not asserted rational. The independent checks of actual rational-grade coefficients and complete tails support its inputs; the infinite implication follows from the exact identities above. — [RR7](response_relations.md), [independent certificate](response_audit_check.py).

Along consecutive actual convergents, \(3^{-p}\asymp2^{-q}\) and \(3^{-r}\asymp2^{-s}\), uniformly eventually. The two child variation bounds therefore give \(R_{\rm child}=O(2^{-(s+q)})\), even if \(Q/q\) is unbounded. The new response error is \(O(2^{-2s})\), which is within that absolute remainder since \(s>q\). Thus
\[
Z-\widetilde Z
=\sigma(2^{-s}-3^{-r})G_R+O(2^{-(s+q)}).
\]
The constants can be taken uniformly over the four states. This does not assert that the remainder is small relative to the leading term: such a statement still needs a physical-gap estimate on the old-\(q\) scale. — [RR8 and its stated limits](response_relations.md).

### Gaps

- No cheap same-family clearing of the \(G_R\) terms has been proved, and no actual infinite adequate state/gap supply follows from the expansion. — [Arithmetic gap](response_relations.md).
- The full goal remains open. Skipped: Lean, external review, installations and broader relation searches. Material risk: treating fixed real response coefficients as fixed rational arithmetic coefficients, or turning the pointwise rank certificate into a statement about weighted numerical values.
