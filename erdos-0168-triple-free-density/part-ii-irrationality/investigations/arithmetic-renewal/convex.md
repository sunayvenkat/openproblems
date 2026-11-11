# Convex source intervals and an exact dual obstruction

## Can boundary slack compress the complete source without clearing every internal coefficient?

### Takeaway

**Yes.** Two common rational boundary constants let the complete source range over an explicit rational interval. Every rational point of that interval is realized by a finite rational-phase calibration with uniformly bounded potentials and a strictly positive complete paired error. The denominator to clear is only the final model denominator, even if the internal boundary constants have enormous denominators. However, the optimized infinite criterion is equivalent to the original irrationality assertion, as proved in the next section; it is not an established arithmetic supply theorem. — [Exact checker](convex_check.py), [ordered construction and exact data](renewal.md), [source data](renewal_source_data.json).

### Cited Findings

- The accepted target is \(Z=2-3Q_{\rm full}(0)=9c-6\), including all infinite low rows and the exceptional birth normalization. The product adjoint is \(\mathcal L=(8I-U_A)(27I-U_B)\); a full finite source comprises nine high initial values and twelve low initial values. — [Exact transport ET1–ET8](../occupation-arithmetic-bridge/exact_transport.md), [normalization audit](../numerator-and-residuals/occupation_audit.md).
- The ordered construction supplies finite rational-phase first-exit solutions in each axis. In each high block, \((8I-U_A)q=h+e_A\), \((27I-U_B)p=q+e_B\); the complete pairing is \(S-Q_{\rm full}=\Psi=\langle e_A\rangle+8\langle e_B\text{ at the horizontal source}\rangle\), summed with every block weight and the low rows. Pointwise signs of \((8I-U_A)e_B\) need not be positive; this complete paired expression is positive. — [Ordered construction](renewal.md), [source checker](renewal_check.py).
- At the baseline boundaries \(q=(1+h)/7\), \(p=1/26+q/26\), one has \(0\le q\le2/7\), \(e_A\in[6/7,9/7]\) outside and zero inside, and \(e_B\in[90/91,191/182]\) outside and zero inside. Uniform one-axis exit is an accepted infinite theorem here, not extrapolated from the source data. — [Ordered proof](renewal.md), [one-axis audit](../finite-volume-calibration/calibration_audit.md).

### Inferences

**C1 — a rational interval of complete calibrations.** In each high block prescribe
\[
q=c_A+h/7\quad\text{outside }D_R,\qquad (8I-U_A)q=h\quad\text{inside},
\]
\[
p=c_B+q/26\quad\text{outside }D_R,\qquad (27I-U_B)p=q\quad\text{inside}.
\]
Use the same \(c_A\) in the low-row horizontal solutions, and take
\[
c_A=(1+\theta)/7,\qquad c_B=(1+\theta)/26,\qquad 0\le\theta\le1.
\tag{C1}
\]
For rational \(\theta\), all functions are finite rational phase-step functions by uniform axis exit. Their global bounds are \(0\le q\le3/7\), \(0\le p\le17/182\). Outside, direct substitution gives
\[
e_A=8c_A+h/7-q_A\in[6/7,17/7],
\]
\[
e_B=27c_B+q/26-p_B\in[179/182,381/182].
\tag{C2}
\]
Thus all paired residuals stay nonnegative and an actual occupied high exterior point makes the complete \(\Psi_\theta\) strictly positive. These estimates are global, including re-entry interfaces. The source is affine in \(\theta\), not merely bounded between numerical samples. — [First-exit construction supplying the operators and pairing](renewal.md), [source data and finite algebra checks](renewal_source_data.json), [convex certificate](convex_check.py).

Here are the useful exact sensitivities. Put
\[
r_A=\partial q/\partial c_A,\quad s_A=\partial p/\partial c_A,
\quad s_B=\partial p/\partial c_B.
\]
The first-exit formulas give \(0\le r_A\le1\), \(0\le s_A\le1/26\), \(0\le s_B\le1\). All corresponding residual derivatives vanish inside. Outside,
\[
\partial_{c_A}e_A=8-r_A\circ T_A\in[7,8],
\]
\[
\partial_{c_A}e_B=1/26-s_A\circ T_B\in[0,1/26],
\quad
\partial_{c_B}e_B=27-s_B\circ T_B\in[26,27].
\tag{C3}
\]
In particular, raising \(c_A\) cannot create a negative paired vertical correction. To justify the bound on \(s_A\), its interior forcing is \(r_A\le1\) and its exterior boundary is \(r_A/26\le1/26\); the constant \(1/26\) is a supersolution of the vertical equation. The first-exit formula proves the comparison directly. — [Ordered finite-exit formulas](renewal.md); the derivative calculation above is a proof from those formulas.

Let \(S_0\) be the baseline complete source, and define
\[
W_A=\tfrac17\partial_{c_A}S,\qquad
W_B=\tfrac1{26}\partial_{c_B}S,
\quad W=W_A+W_B.
\tag{C4}
\]
They are explicit positive rational numbers. Write \(t_{ij}\) for a source's first vertical exit and \(a_{ij,m}\) for the horizontal exit at its \(m\)-th vertical iterate. With \(b_j=(6,4,5)_j\),
\[
W_A=\frac17\left[
216\sum_{i,j}2^{-i}3^{-b_j}
\left(\sum_{m<t_{ij}}\frac{8^{-a_{ij,m}}}{27^{m+1}}
+\frac{27^{-t_{ij}}}{26}\right)
+8\sum_{i,b<4}2^{-i}3^{-b}8^{-a_{ib}}
\right],
\]
\[
W_B=\frac{216}{26}\sum_{i,j}2^{-i}3^{-b_j}27^{-t_{ij}}.
\tag{C5}
\]
Consequently
\[
S_\theta=S_0+\theta W,\qquad \Psi_\theta=\Psi_0+\theta W.
\tag{C6}
\]
The source data file computes these exact finite expressions, reusing the ordered source traversal. No second traversal or floating solver was used. — [Exact data](renewal_source_data.json), [ordered source checker](renewal_check.py).

**C2 — the complete error is comparable to interval width.** The baseline bounds and C3 give, pointwise outside for horizontal terms,
\[
\tfrac17\partial_{c_A}e_A\in[1,8/7],\qquad
e_{A,0}\in[6/7,9/7].
\]
For vertical terms,
\[
\tfrac17\partial_{c_A}e_B+\tfrac1{26}\partial_{c_B}e_B
\in[1,95/91],\qquad
e_{B,0}\in[90/91,191/182].
\]
Thus the whole positive pairing proves
\[
\boxed{\tfrac34W\le\Psi_0\le
\tfrac97W_A+\tfrac{191}{182}W_B\le\tfrac97W.}
\tag{C7}
\]
For the lower inequality, the horizontal derivative-to-baseline ratio is at most \(4/3\); the vertical ratio is at most \(19/18<4/3\). For the upper inequality, baseline horizontal terms are at most \(9/7\) times their \(c_A\)-variation, and baseline vertical terms at most \(191/182\) times their \(c_B\)-variation. Extra \(c_A\)-vertical variation is nonnegative. This pays every low-row and source term. In particular \(W_R\to0\) follows from the already proved \(\Psi_{0,R}\to0\). — [Positive complete pairing and decay input](renewal.md); C3–C7 give the full comparison proof.

**C3 — aggregate rationalization.** For every rational \(r\in[S_0,S_0+W]\), choose the rational
\[
\theta=(r-S_0)/W.
\]
The resulting complete source is exactly \(r\), and
\[
0<Z-(2-3r)=3\Psi_\theta
\le3\left(\tfrac97W_A+\tfrac{191}{182}W_B+r-S_0\right)
\le\tfrac{48}{7}W.
\tag{C8}
\]
Let \(D=\operatorname{den}(2-3r)\). Only \(D\), rather than the denominators of \(q,p,\theta,c_A,c_B\), is needed in the final integer-affine identity. Indeed \(D(2-3r)\) is integral, so under hypothetical \(Z=A/B\), the positive number \(BD[Z-(2-3r)]\) is an integer. Internal denominators affect neither this identity nor the uniform amplitude bounds in C2. This distinction is the constructive convex gain over clearing the displayed enormous common source denominator. — [Integer-lattice acceptance condition](../finite-volume-calibration/REPORT.md), [exact interval checker](convex_check.py).

The low row \(b=0\) has identically zero target. One may take its three potentials identically zero. In the baseline data its dummy source contribution equals its contribution to \(W_A\); subtracting both preserves C1–C8. The checker performs both versions. — [Exact low rule ET8](../occupation-arithmetic-bridge/exact_transport.md), [data](renewal_source_data.json), [certificate](convex_check.py).

### Gaps

- The condition \(D_RW_R\to0\) is not proved for the actual target. It is equivalent to the target's irrationality, as shown next. Real convex feasibility and rational density do not settle it. — [Equivalence proof below](convex.md).
- Exact smallest-denominator models for the tested radii are \(-7,0,5201/4303\) at \(R=0,1,2\), respectively; omitting the dummy zero row changes these to \(-1,9/8,5201/4303\). The strongest tested certificate is
  \[
  0<4303\left(Z-\frac{5201}{4303}\right)<2^{-10}.
  \]
  It does **not** improve the already established exclusion \(>2^{56}\). The exact integer inequality is stored as numerator times \(2^{10}\) strictly less than denominator in the JSON certificate and rechecked. An independent original-colored-board \(96\times96\) target head plus complete geometric tails verifies its orientation and bound. — [Computed certificates](convex_interval_results.json), [checker](convex_check.py), [earlier stronger exclusion](../signed-arithmetic-returns/REPORT.md).

## Does the optimized interval condition genuinely weaken the missing arithmetic theorem?

### Takeaway

**No.** For these shrinking one-sided intervals, the least model denominator satisfies \(D_RW_R\to0\) if and only if \(Z\) is irrational. This is an exact elementary equivalence, not an independent supply theorem. — [C7–C8 above](convex.md), [Farey-parent algebra checked here](convex_check.py).

### Cited Findings

- Every model interval
  \[
  I_R=[2-3(S_{0,R}+W_R),2-3S_{0,R}]
  \]
  has length \(3W_R\), lies strictly below \(Z\), and all its points are within \(48W_R/7\) of \(Z\), with \(W_R\to0\). — [C7–C8 and the accepted decay input](convex.md).
- A minimum-denominator rational in a closed rational interval is computable by exact Euclidean recursion: if an integer lies in the interval, take one; otherwise subtract the common floor and invert the endpoints in reverse order, recurse, and invert back. The checker verifies its output against every smaller denominator for several independent small positive and negative intervals, and verifies the parent containment for the actual models. — [Exact recursion and tests](convex_check.py).

### Inferences

**C4 — elementary equivalence theorem.** Choose \(z_R=p_R/D_R\in I_R\) of least positive denominator. Suppose first \(Z\) irrational. Necessarily \(D_R\to\infty\). For a reduced \(p/q\) with \(q>1\), take the unique \(b\in\{1,\ldots,q-1\}\) with \(pb\equiv1\pmod q\), and put
\[
a=(pb-1)/q,\quad d=q-b,\quad c=p-a.
\]
Then \(bc-ad=1\), \(b+d=q\), and
\[
\frac ab<\frac pq<\frac cd,\qquad
\frac cd-\frac ab=\frac1{bd}.
\]
Both parents have denominator strictly below \(q\), so neither belongs to the closed interval \(I_R\). Since they lie on opposite sides of its chosen rational, they surround the whole interval. Hence
\[
3W_R\le\frac1{b_Rd_R},\qquad
D_RW_R\le\tfrac13\left(\frac1{b_R}+\frac1{d_R}\right).
\tag{C9}
\]
Both parent denominators tend to infinity. Otherwise, along a subsequence one parent has bounded denominator; its distance to \(p_R/D_R\) is \(1/(b_RD_R)\) or \(1/(d_RD_R)\), tending to zero. Its numerators are bounded because the models approach finite \(Z\); a further subsequence fixes that parent, forcing \(Z\) rational. This contradiction proves \(D_RW_R\to0\). Every step is elementary integer algebra; no unquoted Diophantine theorem is used. — [Parent algebra and actual-interval containment checks](convex_check.py).

Conversely, if \(Z=A/B\) is rational in lowest terms, it lies outside every \(I_R\). For every rational \(z_R=p_R/D_R\in I_R\),
\[
\frac1{BD_R}\le Z-z_R\le\frac{48}{7}W_R,
\quad\text{hence}\quad
\boxed{D_RW_R\ge\frac7{48B}.}
\tag{C10}
\]
Thus the proposed cheap-denominator supply is exactly equivalent to the goal. A transparent counterexample to deriving it from width decay alone is a rational target \(x=A/B\) and intervals \([x-2w_n,x-w_n]\), \(w_n\downarrow0\); every contained rational has denominator at least \(1/(2Bw_n)\). — [Explicit arithmetic deduction C10](convex.md).

### Gaps

- No property of the actual source numerators has yet been proved that forces C9's cheap-denominator conclusion without assuming irrationality of \(Z\). The convex construction removes irrelevant internal clearing costs, but does not prove a breakthrough on the infinite arithmetic return. — [Full source data and conditional criterion](renewal_source_data.json), [C4 proof](convex.md).

## Can a state-only potential be repaired by an arbitrary additive phase forcing?

### Takeaway

**No, already on the radius-one state box.** Five exact constraints have a signed integer dual witness annihilating every state-potential value and both arbitrary phase-forcing values, while leaving the target coefficient equal to one. This is a full discounted-operator obstruction, with a precise scope different from the earlier pure compact Green obstruction. — [Dual certificate and exact phase checks](convex_check.py), [earlier compact obstruction](../finite-volume-calibration/exterior_audit.md).

### Cited Findings

- In the high block \(i=j=0\), the full corrected state has horizontal increment \(\Phi(x)\) and vertical increment \(\Xi_3(v)+e_0(v)-e_0(v+\beta)\). Exact all-cell and right-endpoint enumeration gives horizontal alphabet \(\{0,\pm1,\pm\omega,\pm\omega^2\}\) and corrected vertical alphabet \(\{0,1,\omega,\omega^2\}\). At rational phases \(x_0=1/16,x_1=1/6,v_0=1/100\), the increments are respectively \(0,\omega,0\), each inside a positive-length phase cell. Rational logarithm enclosures, rather than floating samples, certify the cell ordering and floors. Original colored boards also reconstruct both actual drift formulas through the finite axis range used by the independent target-head test. — [Standalone checker](convex_check.py), [exact lifted state definitions](../occupation-arithmetic-bridge/exact_transport.md).

### Inferences

**C5 — five-row dual obstruction.** Suppose a state-only real function \(P(z)\), an arbitrary pure-phase real forcing \(g(x,v)\), and a scalar \(\lambda\) satisfy
\[
\mathcal LP(z)=\lambda F(z)+g(x,v)
\]
for every lifted phase and every state of Green radius at most one. All three states \(-\omega,0,\omega\) lie in this box. At the phase pair \((x_0,v_0)\), both increments vanish, yielding
\[
182P(-\omega)-g_0=0,\quad
182P(0)-g_0=\lambda,\quad
182P(\omega)-g_0=\lambda.
\]
At \((x_1,v_0)\), the horizontal increment is \(\omega\) and vertical increment zero, yielding
\[
208P(-\omega)-26P(0)-g_1=0,
\]
\[
208P(0)-26P(\omega)-g_1=\lambda.
\]
Multiply these five equations, in that order, by
\[
\boxed{(-8,9,-1,7,-7).}
\]
Every unknown on the left cancels. The right side is \(\lambda\), proving \(\lambda=0\). The coefficient vector has absolute sum 32; if an ansatz only approximates the equations with residuals of absolute value at most \(\varepsilon\) on those five rows, then \(|\lambda|\le32\varepsilon\). In particular \(\lambda=1\) cannot have uniform interior error below \(1/32\) in this state-only class. — [Exact matrix/right-hand-side verification](convex_check.py).

Adding an arbitrary pure-phase function to \(P\) does not escape this obstruction: its image under \(\mathcal L\) is itself pure phase and can be absorbed into \(g\). A useful finite correction therefore needs genuine state-and-phase interaction. The ordered killed solutions provide that interaction, which is why the new interval construction is not excluded. — [Dual cancellation above](convex.md), [ordered state-phase construction](renewal.md).

### Gaps

- This excludes state-only potentials, even with additive phase corrections, on the **full lifted state/phase box**. It does not exclude phase-dependent potentials, identities restricted only to actual occupied state/phase pairs, different domains, weighted-value identities, or the constructive ordered family. The five phase/state combinations are not asserted to occur together on the actual orbit. — [Exact scope of C5](convex.md).
- No Lean, external review, novelty search, or new dependency installation was performed. Main remaining risk is promoting the explicit convex interval rationalization to an unconditional cheap-denominator infinite family; C4 proves that the latter remains equivalent to the original irrationality task. — [Equivalence theorem C4](convex.md).
