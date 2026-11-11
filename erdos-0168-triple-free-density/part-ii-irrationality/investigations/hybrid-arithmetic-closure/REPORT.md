# Hierarchical returns isolate Erdős’s arithmetic gap

**An actual infinite sequence of exponentially small real residuals is now proved, with cumulative factor cost at most \(5q/2\). The adequate arithmetic infinite-return construction remains unproved, and the goal remains active.** The new identity includes the complete boundary and all four low rows; its boundary value has not been placed in a fixed rational lattice or given sufficiently cheap denominator control. Nonvanishing of the residual is also open. Exact actual-model certificates disprove the simplest hybrid-integrality and ordered-bracketing shortcuts. A positive colored-token representation supplies a second exact formulation through common-rank matching, while adversarial checks delimit the sign and resonance arguments. The final fresh audit passes the auxiliary claims and all five exact certificates, and rejects completion of the infinite-return objective. ([Hierarchy proof](<hierarchy_absorption.md>), [final audit](<final_hybrid_audit.md>))

The target is irrationality of \(c=\lim F(N)/N\), where \(F(N)\) is the largest size of a subset of \([1,N]\) containing no complete triple \(\{n,2n,3n\}\). The accepted finite input is the complete ordinary proof
\[
\tau(D_t)=\min_j(K_j(t)-I_j(t)-P_j(t)),\qquad
D_t=\{2^a3^b\le t\},\quad t\ge3.
\]
Here \(K_j\) counts color \(a-b\bmod3\), and \(I_j,P_j\) are the isolated-root and patch indicators. If \(\eta_{a,b}\) is the increment of \(\tau\) at insertion of \(2^a3^b\), put \(c_{a,b}=1-3\eta_{a,b}\in\{1,-2\}\). The absolutely convergent target series is
\[
Z=\sum_{a,b\ge0}c_{a,b}2^{-a}3^{-b}=9c-6.
\]
The finite proof and density normalization are inputs to this report; the present audit does not independently reprove them. ([Finite proof and two audits](<../prefix-and-phase-audit/REPORT.md>), [established arithmetic framework](<../infinite-return-construction/REPORT.md>))

The new hierarchy uses \(\alpha=\log_3 2\) and actual nonresonant convergents \(p_i/q_i\), meaning \(p_i+q_i\not\equiv0\bmod3\). The proved supply contains infinitely many with immediate-successor ratio
\[
r_i=q_{\mathrm{next}}/q_i>C_*=\frac{15+\sqrt5}{10}.
\]
Retain indices separated by at least four continued-fraction steps. Their denominators satisfy \(q_{i+1}\ge5q_i\), hence
\[
\sum_{i\le m}q_i\le\frac54q_m.
\]
Every matching window continues to use the original immediate successor, not the next retained denominator. This distinction prevents an unjustified enlargement of the agreement rectangle. ([Supply theorem](<../infinite-return-construction/diophantine_supply.md>), [thinning and cost proof](<adaptive_induction.md>))

Shift past the exceptional low rows by defining \(d(a,b)=c_{a,b+4}\), and write \(W(d)=\sum d(a,b)2^{-a}3^{-b}\). With \(S_a,S_b\) denoting positive index shifts, set
\[
L_i=S_a^{2q_i}+S_a^{q_i}S_b^{p_i}+S_b^{2p_i},\qquad
F_i=2^{2q_i}+2^{q_i}3^{p_i}+3^{2p_i},
\]
\[
P_m=\prod_{i\le m}L_i,\qquad \Pi_m=\prod_{i\le m}F_i.
\]
The earlier high-row skew identity makes the latest \(L_m d\) vanish for \(a<q_{\mathrm{next}}-q_m\), \(b<p_{\mathrm{next}}-p_m-4\). All older shifts are charged: if \(Q_-=\sum_{i<m}q_i\) and \(P_-=\sum_{i<m}p_i\), the product vanishes on the smaller rectangle with widths
\[
A_m=q_{\mathrm{next}}-q_m-2Q_-,\qquad
H_m=p_{\mathrm{next}}-p_m-4-2P_-.
\]
The older operators have coefficient sum \(3^{m-1}\), giving the full exterior bound
\[
|W(P_m d)|\le18\,3^{m-1}
\bigl(2^{-A_m}+3^{-H_m}-2^{-A_m}3^{-H_m}\bigr).
\]
This includes both infinite exterior strips. ([Exact hierarchy, HA1–HA7](<hierarchy_absorption.md>))

Thinning gives \(Q_-\le q_m/4\) and \(m=O(\log q_m)\). Summable convergent errors give \(P_-=\alpha Q_-+O(1)\). Thus \(A_m\ge(r_m-3/2)q_m\) and \(H_m\log3=A_m\log2+O(1)\); the coefficient growth is subexponential in \(q_m\). Summing the individual factor costs likewise pays every retained scale. Consequently the **actual infinite sequence**, without any additional large-partial-quotient hypothesis, satisfies
\[
\boxed{\log\Pi_m\le\left(\frac52+o(1)\right)q_m\log2,\qquad
|\mathcal R_m|\le
\exp\!\left[-\left(\frac{\sqrt5}{10}+o(1)\right)q_m\log2\right],}
\qquad \mathcal R_m=W(P_m d).
\]
The margin is \(C_*-3/2=\sqrt5/10>0\). These are established real estimates, beyond the first-round conditional cost calculation. ([HA8–HA9 and reconstruction](<final_hybrid_audit.md>))

Reindexing identifies the exact comparison value. For \(P=\sum c_{AB}S_a^AS_b^B\), its boundary kernel is
\[
\mathcal K_P(a,b)=2^{-a}3^{-b}
\sum_{A,B:\ a<A\ \mathrm{or}\ b<B}c_{AB}2^A3^B,
\qquad
\mathcal B_P(d)=\sum_{a,b\ge0}\mathcal K_P(a,b)d(a,b).
\]
The union condition subtracts the corner intersection once. Define the complete low-row value \(L_0=\sum_{a\ge0,\,b<4}c_{a,b}2^{-a}3^{-b}\). Then
\[
\boxed{81\Pi_m Z=B_m+\mathcal R_m,\qquad
B_m=81\Pi_mL_0+\mathcal B_{P_m}(d).}
\]
The notes call \(B_m\) by \(N_m^*\); **no integrality is implied by that notation**. Weighted finite corners clear to integers, but the semi-infinite sides and low-row profiles remain in this explicit real boundary value. ([HA2–HA3 and HA10](<hierarchy_absorption.md>))

A fixed rational lattice for \(B_m\) would suffice. More generally, a proved integer factor \(S_m\) with \(\log S_m=o(q_m)\) and \(S_mB_m\in\mathbb Z\) would preserve the exponential residual decay. Under \(Z=A/B\), the resulting cleared errors would lie in \(B^{-1}\mathbb Z\) and eventually vanish. A theorem showing nonzero residuals infinitely often on that same sequence would then contradict rationality. Neither the required boundary arithmetic nor nonvanishing is proved. Growing intermediate term count is permissible here only after genuine integer clearing; this argument does not extend a fixed-dimensional S-unit theorem to arbitrary dimension. ([Conditional arithmetic budget](<adaptive_induction.md>), [final arithmetic audit](<final_hybrid_audit.md>))

Direct multiplication does not remove the boundary. Put \(A_{\max}=2\sum q_i\), \(H_{\max}=2\sum p_i\). The unique all-horizontal monomial yields
\[
\mathcal K_{P_m}(A_{\max}-1,b)=2\,3^{-b}\qquad(b\ge H_{\max}),
\]
an explicit surviving infinite column. At \(a=0\), the kernel is \(3^{-b}M_b\), with \(M_b\) a unit modulo three. Every actual \(d(0,b)\) is also a unit modulo three. The last term therefore gives the head through \(b=T-1\) reduced denominator **exactly \(3^{T-1}\)**. Clearing this column separately incurs a growing cost that cancels its elementary tail decay. This is an individual-head result and a formal multiplication obstruction; cross-column identities or signed actual-state corrections remain possible. The specific repair \(27F_{5,8}F_{53,84}\) also fails to clear the unchanged \(53/84\) scalar model. ([Boundary and head proofs](<hierarchy_absorption.md>))

The previous hybrid shortcut has a stronger negative verdict. With \(D=27(2^{3q}-1)(3^{3p}-1)\) and \(J=Z_{MT}+Z_{TM}-Z_{MM}\), the product-tail estimate for \(Z-J\) survives, but **unconditional \(DJ\)-integrality is false**. Exact one-axis periodic resummation reduces each hybrid to an infinite integer-alphabet series, in base three or two. The alphabet heights grow exponentially with \(q\), and the actual-axis series remains. Rigorous complete-tail intervals at \(5/8\) place the fractional part of \(DJ\) strictly between \(788789/1048576\) and \(788790/1048576\). At \(53/84\), writing \(N=DZ_{MM}\), they give
\[
-2^{-60}<DJ-N<-2^{-100}.
\]
If \(DJ\) is rational there, its reduced denominator exceeds \(2^{60}\). The certificates exclude the universal shortcut, not a conditional implication under \(Z\in\mathbb Q\) or a selected subsequence. ([Normal forms and exact enclosures](<hybrid_compression.md>))

Those bounds also certify complete-target nonvanishing: \(Z>Z_{MM}(5/8,+)\) and \(Z<Z_{MM}(53/84,-)\). A separate direct actual rectangle with its entire exterior tail proves
\[
Z_-(12/19)<Z<Z_+(12/19).
\]
Exact power comparisons verify that \(12/19\) is an actual upper convergent. Thus a fixed ordered convention \(Z_+\le Z\le Z_-\) fails, and the matched minus-side errors already have opposite signs at \(12/19\) and \(53/84\). These are three named nonvanishing results. The unordered bracket and infinite nonstabilization remain open. ([Actual signs](<hybrid_compression.md>), [12/19 certificate and scope](<hybrid_bracketing.md>))

The full correction also has a new positive-process formulation. Start with one colored token at every \(2^a3^b\), retaining its color \(a-b\bmod3\). Delay
\[
2^a\longmapsto3\,2^{a-1}\quad(a\ge1),\qquad
3\,2^a\longmapsto27\,2^{a-3}\quad(a\ge2).
\]
The color counts of arrived tokens are exactly \(T_j(t)=K_j(t)-I_j(t)-P_j(t)\). The sole nonsmooth arrival \(12\mapsto27/2\) has zero minimum increment; simultaneous arrivals have equal reciprocal weights. Hence \(\tau(t)=\min_jT_j(t)\) is globally a positive token-count process. Its three marginal reciprocal sums are rational, with total \(143/54\). ([Retiming proof, endpoints and generating function](<global_carries.md>))

If \(t_j(k)\) is the \(k\)-th arrival of color \(j\), counting multiplicities, then exactly
\[
\sum_{a,b\ge0}\frac{\eta_{a,b}}{2^a3^b}
=\sum_{k\ge1}\frac1{\max(t_0(k),t_1(k),t_2(k))}.
\]
Equal-rank matching maximizes reciprocal triple cost among all bijective three-color couplings. Indeed, at any threshold the number of triples having all three reciprocal entries above that threshold is bounded by the smallest marginal count; equal-rank matching attains that bound simultaneously at every threshold. Integration proves the assertion, including the infinite summable lists. A genuine rational coupling would therefore give a one-sided comparison, with strictness requiring a deficit on an interval of thresholds. **No sufficiently accurate low-cost rational coupling is constructed.** Rational marginals alone do not determine the optimum: the note gives finite smooth-arrival examples with identical marginal masses but costs \(1/4\) and \(5/18\). ([Rank identity](<global_carries.md>), [matching proof and counterexample](<hierarchy_absorption.md>))

Two further positive identities clarify the remaining cancellation. Complete reversal of any balanced color block has a nonnegative weighted minimum-birth response when weights stay attached to physical tokens. Every pure cyclic-color grade has the same sign, with an explicit zero-or-one tie-ray table. Actual attached low events break the extension: at \(5/8\), complete grades \(48\) and \(88\) have weighted forward-minus-reverse differences \(13/186624\) and \(-13/45349632\). The pure-grade theorem cannot determine the signed sum of all exceptional grades. ([Complete reversal proof and actual counterexamples](<global_carries.md>))

The actual axis states also satisfy exact Beatty reciprocity. At merged boundary pairs \(b=\lfloor a\alpha\rfloor\) or \(a=\lfloor b/\alpha\rfloor\),
\[
B_b^{\mathrm{axis}}+\overline{A_a}
=\Lambda_{a\bmod3,b\bmod3},\qquad
\Lambda=\begin{pmatrix}
2&2+\omega&1\\2+\omega&1+\omega&1\\1&1&1
\end{pmatrix},\quad \omega^2+\omega+1=0.
\]
Both hybrid profiles thus follow one origin-anchored accumulated walk, with a finite residue controller. Their unequal discounts persist. The bare minimum potential fails the \(1/2,1/3,1/6\) discounted harmonic identity on the actual square based at \(81\), with defect \(-1/2\). An exact cone-difference stencil localizes curvature to weighted point occupation, but rationality of the translated cone sums is unproved. ([Reciprocity, actual counterexample and point-source identity](<hybrid_compression.md>))

The complementary-resonance analysis closes another generic shortcut. Four-digit blocks \((k,1,1,1)\) preserve resonant root magnitude while two blocks add an explicit nonzero unipotent drift to the preceding register. On the fixed **golden comparison slope**, the analysis proves all-level corrected birth defects at \(a=\Theta(\sqrt q)\), \(b=S+1\), and an unbounded individual low-row dyadic denominator. This refutes bounded-preperiod and late-absolute-support inferences from bounded resonant drift. It supplies no target-logarithm trajectory, full scalar denominator lower bound, signed-error lower bound or first-defect theorem. ([Both-parity induction and all-level comparison proof](<adaptive_induction.md>))

The updated dependency status is precise:

| Obligation for this route | Current evidence |
|---|---|
| Complete finite optimum and corrected birth rules | Established written proofs; accepted inputs. |
| Actual infinite retained supply and cumulative factor cost | Proved, with cost at most \(5q/2+o(q)\). |
| Exponentially small actual multiscale real residual | Proved with margin \(\sqrt5/10\). |
| Fixed-lattice or sufficiently cheap rational denominator control of the full \(B_m\) | Unproved; boundary strips and low rows remain. |
| Nonzero residuals infinitely often on that same family | Unproved. |
| Irrationality conclusion and adequate arithmetic infinite return | Not established; goal active. |

The final audit independently reconstructed the main proofs and ran all five exact certificates successfully. They use integer/Fraction arithmetic, exact logarithmic floors and exact infinite-tail bounds; the two periodic-axis evaluations share an explicit previously audited model helper. Finite checks support the written infinite proofs and do not replace them. The next arithmetic theorem must control the complete \(B_m\), including its low rows, or construct a different rational comparison with the same useful cost and error. The token matching formulation provides an exact alternative object for that task; its variational bound does not supply the missing construction. ([Final audit and validation scope](<final_hybrid_audit.md>))

Skipped: Lean, external review and priority verification; this synthesis adds no experiments. The material risk is treating the proved real residual decay as an arithmetic return before its full boundary value has controlled denominators and the required nonvanishing.
