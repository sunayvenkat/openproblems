# Ordered stopping rationalizes the complete source

**For every nonnegative integer radius, an ordered first-exit construction now gives a rational complete source with a strictly positive error tending to zero.** The construction combines renewal stopping, factored discounted operators and positivity after occupation pairing. It retains every high block, every low row and the density coefficient. This improves the construction available in the preceding report, whose unrestricted coupled Dirichlet sources remained unknown reals. **The adequate infinite arithmetic return is still unproved:** clearing the new rational sources can overwhelm their small errors. Convex boundary tuning greatly reduces some finite denominators, but an adversarial Farey argument proves that its optimized infinite condition is equivalent to the original irrationality assertion. Three independent audits pass within these scopes; no solution or historical novelty is claimed. ([Renewal audit](<renewal_audit.md>), [convex audit](<convex_audit.md>), [symbolic audit](<symbolic_audit.md>))

## Ordered exits turn a signed interface into a positive error

Let \(F(N)\) be the largest size of a subset of \(\{1,\ldots,N\}\) containing no complete triple \(\{n,2n,3n\}\). The target is irrationality of its limiting density \(c\). The accepted finite-cover theorem and birth series give
\[
Z=9c-6=2-3Q_{\rm full}(0).
\]
Here \(Q_{\rm full}\) is the unexceptional all-row birth readout. The exceptional birth at \((0,1)\), of weight \(1/3\), is already included once in the constant two. The completed finite optimization remains an input to this investigation. ([Finite foundation](<../prefix-and-phase-audit/REPORT.md>), [complete normalization](<../numerator-and-residuals/occupation_audit.md>))

Write \(\omega^2+\omega+1=0\). The actual horizontal and vertical lifts advance three physical indices and have pullbacks \(U_A,U_B\), discounted bases eight and twenty-seven, and product adjoint
\[
\mathcal L=(8I-U_A)(27I-U_B)
=216I-27U_A-8U_B+U_AU_B.
\]
Their states retain both lattice displacement and irrational phase. For a high residue block the Boolean target is \(h=\mathcal F(\zeta)\), where \(\mathcal F(x+y\omega)=\mathbf1_{\{x\le0,\ x\le y\}}\) and \(\zeta\) includes both accumulated axes, residue and event corrections. Put
\[
\rho(x+y\omega)=\max(|y-x|,|x|),\qquad
\mathcal D_R=\{\rho(\zeta)\le R\}.
\]
The low rows have their own accepted Boolean kernels. The occupation measures used below are
\[
\Omega=\sum_{n\ge0}8^{-n}\delta_{(A_{3n},\{n\alpha\})},\qquad
\Pi_j=\sum_{m\ge m_j}27^{-m}\delta_{(B_{3m},\{m\beta\})},
\]
where \(\alpha=\log_3 2\), \(\beta=1/\alpha\), and \(m_j=(2,1,1)_j\). Thus \(\Omega\) begins at \((1,0)\), while each vertical measure retains its own actual starting state and phase. These definitions explain the line source in (3); replacing either measure by a state-only marginal would lose its phase dependence. ([Actual lifts, kernels and product transport](<../occupation-arithmetic-bridge/exact_transport.md>))

First solve horizontally, then vertically:
\[
\begin{array}{lll}
(8I-U_A)q_R=h&\text{inside }\mathcal D_R,
&q_R=(1+h)/7\text{ outside},\\
(27I-U_B)p_R=q_R&\text{inside }\mathcal D_R,
&p_R=(1+q_R)/26\text{ outside}.
\end{array}
\tag{1}
\]
Uniform finite pure-axis exits make both solutions finite rational phase-step functions on suitable common refinements. For example, at horizontal exit time \(a\),
\[
q_R(\xi)=\sum_{n<a}8^{-n-1}h(T_A^n\xi)
+8^{-a}(1+h(T_A^a\xi))/7.
\]
The analogous vertical sum has reward \(q_R\), discount \(27\), and its prescribed terminal value. Every pulled-back reward cut and endpoint is retained. No invariant phase partition or uniform exit under arbitrary alternating moves is assumed. ([Finite formulas and audit](<renewal_audit.md>))

The bounds \(0\le q_R\le2/7\), \(0\le p_R\le9/182\) give errors
\[
e_A=(8I-U_A)q_R-h,\qquad e_B=(27I-U_B)p_R-q_R,
\]
zero inside and satisfying, everywhere outside,
\[
6/7\le e_A\le9/7,\qquad
90/91\le e_B\le191/182.
\]
These include re-entry transitions. Although
\[
\mathcal Lp_R-h=e_A+(8I-U_A)e_B
\tag{2}
\]
can have signed interfaces, its complete pairing is positive. If \(\Omega\) is the horizontal occupation and \(\Pi_j\) the actual vertical occupation in block \(j\), the horizontal resolvent gives
\[
\langle(8I-U_A)e_B,\Omega\otimes\Pi_j\rangle
=8\langle e_B(1,\cdot,0,\cdot),\Pi_j\rangle\ge0.
\tag{3}
\]
The factor eight survives. This is the mechanism that avoids imposing pointwise positivity on the product residual. ([Ordered pairing proof and terminal checks](<renewal_audit.md>))

With \(b_j=(6,4,5)_j\), the complete source is
\[
S_R^{\rm ord}
=216\sum_{i,j=0}^2 2^{-i}3^{-b_j}p_{ij,R}(\xi_{ij})
+8\sum_{i=0}^2\sum_{b=0}^3 2^{-i}3^{-b}q_{i,b,R}(1,0),
\tag{4}
\]
where \(\xi_{ij}=(1,B_{3m_j},0,\{m_j\beta\})\) is the actual initial lifted point of that block. Thus all nine high and twelve low terms are rational. Their exact transport proves
\[
\boxed{Z=2-3S_R^{\rm ord}+3\Psi_R,\qquad
S_R^{\rm ord}\in\mathbb Q,\quad \Psi_R>0,\quad\Psi_R\to0.}
\tag{5}
\]
Infinite actual high support supplies strict positivity. The full height-tail theorem gives fixed \(C_\rho>0\), \(0<\kappa<1\), and \(m_R=\max(0,\lfloor(R/C_\rho)^{1/\kappa}\rfloor)\) with
\[
0<\Psi_R\le\frac{881}{91}(6\,2^{-m_R}-3\,3^{-m_R}).
\tag{6}
\]
All low rows remain horizontally infinite before pairing. Bounded potentials justify removal of the complete terminal edges and corner. ([Complete-source and tail audit](<renewal_audit.md>))

## Column discrepancy supplies the vertical exit theorem

The new construction requires vertical escape as well as the previously proved horizontal escape. This follows from original colored-column sums. Set
\[
\alpha=\log_3 2,\quad\beta=1/\alpha,\qquad
\mathcal K(t)=\sum_{2^a3^b\le t}\omega^{a-b}.
\]
The accepted vertical recurrence agrees with
\(B_b=\omega^{-2b}\mathcal K(3^b)\). For \(L_m=\lfloor3m\beta\rfloor\), exact geometric summation gives
\[
(1-\omega^{-1})B_{3m}
=\sum_{a=0}^{L_m}\omega^a
-\omega^{-1}\sum_{a=0}^{L_m}\omega^{\lceil(1+\alpha)a\rceil}.
\tag{7}
\]
The first sum is bounded. For positive \(a\), the summands of the second sum have real parts \(-1/2,-1/2,1\) on successive thirds of \(\{a(1+\alpha)/3\}\). Its real partial sum is therefore \(3/2\) times final-third discrepancy. The \(a=0\) term is retained as a constant. ([Original-column derivation and independent reconstruction](<renewal_audit.md>))

Kesten's interval criterion, in the fixed-start form stated by Kelly–Sadun, makes this discrepancy unbounded: \(1/3\notin\mathbb Z(1+\alpha)/3+\mathbb Z\). The sampling gaps \(L_{m+1}-L_m\) are four or five. Bounded increments prevent bounded sampling from hiding unbounded partial sums, so the precise actual \(B_{3m}\) is unbounded. This uses a primary published theorem at its checked scope, rather than a generic-phase or numerical substitute. ([Kelly–Sadun, Theorem 1](https://arxiv.org/html/1404.0455), [application audit](<renewal_audit.md>))

A bounded cocycle at any phase would bound all its orbit translates. Density and continuity of each finite sum at phase zero would then contradict actual unboundedness. One-sided limiting itineraries differ by only finitely many cut effects. Compactness excludes arbitrarily long surviving itineraries in a fixed finite state box. The finite lattice variable is the **combined offset \(y+w\)**, not the raw pair \((y,w)\); bounded event corrections enlarge its box by a fixed amount. This proves the uniform pure-axis exit needed in (1), without asserting joint alternating termination. ([Phase, endpoint and compactness audit](<renewal_audit.md>))

This uniformity is qualitative. No useful general upper bound for the stopping horizons is proved here. The state-height input gives a lower bound on the index of an exterior arrival and thereby controls the discounted tail. It does not bound the largest exit horizon used in a source evaluation. Consequently finite computability of the potentials supplies no affordable denominator estimate by itself. ([Exit and arithmetic limitations](<renewal_audit.md>))

## Complete denominators overwhelm the fixed-boundary returns

Rationality in (5) alone does not finish the problem. If \(z_R=2-3S_R^{\rm ord}\) and \(d_Rz_R\) is integral, the required condition is
\[
0<d_R(Z-z_R)=3d_R\Psi_R\longrightarrow0.
\tag{8}
\]
Hypothetical \(Z=A/B\) would make its multiples by \(B\) positive integers tending to zero. The current construction establishes positivity and decay before clearing; its arithmetic cost remains decisive. ([Acceptance criterion and source audit](<renewal_audit.md>))

Let \(H_R\) be the largest horizontal exit used in any source evaluation and \(T_R\) the largest vertical exit. The complete source, including every physical weight, has common clearing factor
\[
C_R=91\,8^{H_R}27^{T_R+1}.
\]
Writing \(J_R=C_RS_R^{\rm ord}\), \(g_R=\gcd(C_R,J_R)\), its reduced source denominator is \(d_R^{\rm src}=C_R/g_R\). An actual exterior witness on row \(b=4\), at horizontal first exit \(\tau_R\le H_R\), proves
\[
d_R^{\rm src}\Psi_R\ge
\frac{26\,8^{H_R-\tau_R}27^{T_R}}{g_R}.
\tag{9}
\]
Consequently the common factor itself always fails; adequate reduced clearing would require substantial whole-source gcd saving. This is a restriction on this fixed-boundary family, not a universal obstruction. ([Complete arithmetic derivation](<renewal_audit.md>))

| Radius | \((H_R,T_R,\tau_R)\) | Reduced source denominator bits | Certified \(d_R^{\rm src}\Psi_R\) |
|---|---|---:|---|
| 0 | \((3,3,1)\) | 26 | \(>2^{15}\) |
| 1 | \((200,125,32)\) | 1202 | \(>2^{1097}\) |
| 2 | \((1282,689,1065)\) | 7125 | \(>2^{3921}\) |

These exact lower bounds come from occupied witnesses, not error estimates. Independent reconstruction reproduces the complete numerators, denominators and gcds. A local CRT choice can cancel a vertical \(27^t\) when its allowed boundary interval covers every residue, but that leaves the horizontal cost and supplies no infinite full-source theorem. ([Verified data and limited CRT lemma](<renewal_audit.md>))

The local arithmetic shows why complete assembly matters. Along one stopped vertical prefix, write the horizontal rewards as \(q_m=N_m/(7\,8^{a_m})\) and \(H=\max_{m<t}a_m\). Then
\[
p_0=\frac{26\sum_{m<t}27^{t-1-m}8^{H-a_m}N_m+8^H(8+h_t)}
{182\,8^H27^t}.
\]
The terminal value \(h_t\) is Boolean. Its numerator is nonzero modulo thirteen, so thirteen survives in this individual source. It can nevertheless cancel after all block weights are summed: the radius-two denominator does cancel it. Neither an uncancelled local prime nor a small local denominator decides the arithmetic of the complete density source. The same distinction governs the local CRT lemma. ([Local numerator and whole-source checks](<renewal_audit.md>))

## Boundary tuning compresses sources but restates irrationality

Convex variation removes a needless clearing requirement: internal potential denominators need not be cleared if the aggregate source is cheap. Replace the exterior values in (1) by
\[
q=c_A+h/7,\qquad p=c_B+q/26,\qquad
c_A=(1+\theta)/7,\quad c_B=(1+\theta)/26,\quad0\le\theta\le1.
\]
For rational \(\theta\), the functions remain finite rational-step, with \(q\le3/7\), \(p\le17/182\), and positive complete paired residuals. Linearity gives
\[
S_{R,\theta}^{\rm ord}=S_{R,0}^{\rm ord}+\theta W_R,\qquad W_R>0.
\tag{10}
\]
The derivative maximum principle proves
\[
\frac34W_R\le\Psi_{R,0}\le\frac97W_R,\qquad W_R\to0.
\tag{11}
\]
In particular, varying the horizontal boundary adds a nonnegative vertical correction; no hidden signed source is discarded. The identically zero low row \(b=0\) can be represented by zero potentials, subtracting its equal contributions from the baseline source and horizontal width. ([Sensitivity proof and independent interval audit](<convex_audit.md>))

Every rational \(r\in[S_{R,0}^{\rm ord},S_{R,0}^{\rm ord}+W_R]\) is realized by the rational parameter \(\theta=(r-S_{R,0}^{\rm ord})/W_R\). Its model \(z=2-3r\) satisfies
\[
0<Z-z\le48W_R/7.
\tag{12}
\]
Only \(\operatorname{den}(z)\) enters the final integer-affine expression. Large denominators of \(\theta,q,p\) do not enter it, and their amplitudes remain uniformly bounded. At radius two, exact interval optimization yields the **13-bit model denominator** \(4303\):
\[
0<4303\left(Z-\frac{5201}{4303}\right)<2^{-10}.
\tag{13}
\]
An independent original-board \(96\times96\) head and complete tails verify the sign and bound. This certificate is weaker than the existing \(>2^{56}\) denominator exclusion; the dramatic compression does not improve that exclusion. ([Exact interval certificates](<convex_interval_results.json>), [independent checks](<convex_audit.md>))

**The optimized infinite condition is equivalent to the target irrationality.** Let \(z_R=p_R/d_R\) have smallest denominator in the model interval
\[
I_R=[2-3(S_{R,0}^{\rm ord}+W_R),\,2-3S_{R,0}^{\rm ord}].
\]
It has length \(3W_R\), lies strictly below \(Z\), and approaches \(Z\). If \(Z\) is irrational, \(d_R\to\infty\). The canonical Farey parents \(a_R/b_R<c_R/e_R\) of \(z_R\) have \(b_R+e_R=d_R\), determinant one and smaller denominators. Minimality puts both outside \(I_R\), so they surround the whole interval. Therefore
\[
d_RW_R\le\frac13(1/b_R+1/e_R).
\]
Both parent denominators diverge: a bounded one would give a fixed rational parent approaching \(Z\). Hence irrationality implies \(d_RW_R\to0\). Conversely, rational \(Z=A/B\) gives
\[
\frac1{Bd_R}\le Z-z_R\le48W_R/7,\qquad
d_RW_R\ge7/(48B).
\tag{14}
\]
Thus interval shrinkage and rational feasibility do not establish an independent supply theorem. The hoped-for shortcut has been rigorously broken. ([Farey equivalence proof and audit](<convex_audit.md>))

## Prime recurrences and duality identify the remaining obligations

The unrestricted coupled Dirichlet construction is a different family, denoted \(S_R^{\rm coupled}\). Its rationality at growing radii remains unproved. The coupled source and prime data below use the large exterior prescriptions \(p_H=1+h/182\) and \(p_L=1+h/7\); Picard iteration starts at zero inside, with these exterior values held fixed. All actual radius-zero high source grids terminate under every interior horizontal, vertical and diagonal branch; the low starts terminate separately. Exact backward substitution gives a rational complete source with an 89-bit denominator, but its cleared positive residual exceeds \(7.8\times10^{27}\). This is an actual-source certificate, **not full-phase joint termination**; an unsupported stronger cross-reference was removed during audit. ([Corrected closure and strict residual interval](<symbolic_audit.md>))

Finite-field dynamics detects cancellations in the full coupled Picard source. At depth \(m\), scale high values by \(182\,216^m\) to integers \(\widehat q_m\), and low values by \(7\,8^m\). The complete common numerator
\[
N_{R,m}=27\cdot182\cdot216^mS_{R,m}^{\rm coupled}
\]
satisfies, for \(m\ge1\),
\[
N_{R,m}\equiv F_{R,m}:=\sum_{i=0}^2 2^{3-i}\widehat q_m(i,6)\pmod3.
\]
All twelve low contributions and the high starts at \(b=4,5\) vanish at this prime after full assembly. Thus
\[
F_{R,m}\ne0\quad\Longrightarrow\quad
v_3(\operatorname{den}S_{R,m}^{\rm coupled})=3m+3.
\tag{15}
\]
Inside, from depth two, the scaled residue evolves by
\(\widehat q_m=-\widehat q_{m-1,B}-\widehat q_{m-1,AB}\pmod3\), with zero exterior residue. The 71 nonzero residues among the first 100 radius-one depths prove no infinite supply. ([Full-source scaling and killed cellular recurrence](<symbolic_audit.md>))

The certified source-error majorant is
\[
|S_R^{\rm coupled}-S_{R,m}^{\rm coupled}|
\le(61/9)6^{-m}+(640/27)8^{-m}.
\]
At nonzero-residue depths, clearing its high term costs at least \(183(9/2)^m\). This defeats that majorant as a certificate; it is no lower bound on the actual error. A Frobenius shortcut also fails: unrestricted shifts commute, but killing inserts noncommuting intermediate projections. Exact actual cells witness this failure. ([Error and commutator audit](<symbolic_audit.md>))

Convex duality separately excludes the simplest potential class. In the full lifted radius-one box, five equations at certified phase/state combinations for state-only \(P\) and arbitrary additive pure-phase forcing have integer annihilator
\[
(-8,9,-1,7,-7).
\]
It cancels every potential and forcing value while leaving the coefficient \(\lambda\) of the target \(\mathcal F\), forcing \(\lambda=0\). The result also excludes uniform error below \(1/32\) when \(\lambda=1\). It does not exclude phase-dependent potentials, identities only on actual occupied pairs, or weighted-value constructions. ([Generated five-row witness and precise scope](<convex_audit.md>))

A separate real improvement retains the Boolean current term in the interface estimate. With zero forcing, the smaller exterior prescription \((1+h)/182\) already gives a bounded coupled solution and
\[
144/182\le\mathcal Lp-h\le161/91
\]
on every exterior interface. Matching low prescriptions \((1+h)/7\) remain positive. These smaller offsets change source seeds; the offset-one prime and numerical data cannot be transferred to them. ([Small-offset proof and audit](<symbolic_audit.md>))

The three supplied and three independent exact checkers pass. They reconstruct boards, source arithmetic and complete tails; written proofs supply the infinite exit and decay statements. The next required result must use **actual numerator or phase structure** to establish affordable nonzero integer-affine returns. Generic interval rationalization merely restates the goal. The ordered construction removes unknown source rationality for its own family and exposes concrete whole-source arithmetic; it does not complete step 9 or prove Erdős #168(ii).

Skipped: Lean verification, external peer review and priority checks. Material risk: treating rational source existence, finite compression or the Farey equivalence as a proved adequate infinite return.
