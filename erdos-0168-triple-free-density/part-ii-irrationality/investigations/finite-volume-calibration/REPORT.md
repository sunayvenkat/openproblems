# Real calibrations expose the arithmetic bottleneck

**Erdős #168(ii) remains unproved: the finite combinatorial foundation is complete in our written argument, but the decisive infinite arithmetic return is missing.** The latest work constructs a full bounded real calibration with exact interior cancellation and a strictly positive exterior, including every interface and all low rows. It also classifies the rational relations among the actual pure-phase guards, reducing their horizontal numerical values to exactly ten rational dimensions. Neither theorem makes the calibration's source values rational or controls their denominators. The earlier eleven-step roadmap therefore has steps 1–7 established, step 8 available as a rational-model framework, step 9 open, step 10 proved for specified families but not matched to an adequate arithmetic family, and step 11 ready as a conditional deduction. These are written proofs with internal independent audits and exact certificates; they are not an externally accepted solution or a percentage-complete proof. ([Finite foundation](<../prefix-and-phase-audit/REPORT.md>), [current exterior audit](<exterior_audit.md>), [current guard audit](<coboundary_audit.md>))

## The roadmap separates completed reductions from the remaining theorem

Let \(F(N)\) be the largest size of a subset of \(\{1,\ldots,N\}\) containing no complete triple \(\{n,2n,3n\}\), and let \(c=\lim_{N\to\infty}F(N)/N\). The problem asks for the value of \(c\) and whether it is irrational. Existence of the limit and a smooth-number series were already established by Graham, Spencer and Witsenhausen. The official formal-conjectures source distinguishes the open value question, **part (i)**, from the open irrationality question, **part (ii)**, and labels existence separately as solved. Our continuing target is part (ii); a closed-form evaluation solving part (i) is not claimed. The Conjectures.io page currently records no published contribution against part (ii). These published labels do not assess our unpublished arguments. ([Problem statement and background](https://www.erdosproblems.com/168), [official distinctions](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/168.lean), [current part ii page](https://conjectures.io/problems/erdos168-erdos-168-parts-ii))

The numbering below preserves the earlier roadmap. “Proved” means that the written argument has the stated internal audit support. Step 8 is a framework rather than a claim that its approximations already meet the final infinite-sequence requirement. Step 10 now has stronger results than when the original roadmap was written. ([Original numbered roadmap](<../reflected-return-models/REPORT.md>), [subsequent scalar results](<../signed-arithmetic-returns/REPORT.md>))

| Step | Required result | Current progress and remaining work |
|---|---|---|
| 1 | Establish the limit and split integers into components \(m2^a3^b\), \((m,6)=1\). | **Established background.** Every forbidden triple stays in one component. |
| 2 | Express density by the finite-component birth increments. | **Complete.** An absolutely convergent weighted series gives the target \(Z=9c-6\). |
| 3 | Construct corrected three-color covers. | **Proved.** Isolated dyadic points and the valid three-to-two patch supply the corrected upper bound. |
| 4 | Classify positive matching deficiency away from the vertical axis. | **Proved.** The classification handles arbitrary relevant owner sets, including multiple roots. |
| 5 | Control vertical-axis deficiencies and obtain the required common optimum. | **Proved.** Restricted maximizers, one excluded owner and prefix repairs resolve the compatibility problem. |
| 6 | Prove the exact finite optimum for every cutoff. | **Proved for every real \(t\ge3\).** The full formula below has two final independent internal audits. |
| 7 | Derive the corrected birth dynamics. | **Complete.** Both accumulated axis states, residue and event corrections, the exceptional birth and all four low rows are retained. |
| 8 | Construct rational models with denominators, heights and matching windows. | **Framework proved.** Explicit integer clearing and complete error bounds are available. Infinite adequacy belongs to step 9. |
| 9 | Obtain an adequate infinite arithmetic-return family for the actual logarithmic slope. | **Decisive open step.** Positive small real returns exist infinitely, even at every state radius. An affordable integer-affine relation to \(Z\), or sufficient actual scalar supply, is still missing. |
| 10 | Prove the errors nonzero along the family used in step 9. | **Proved for specified eligible scalar cases and positive real occupation/calibration families.** No single family yet combines this with every arithmetic requirement of step 9. |
| 11 | Use discreteness to conclude \(c\notin\mathbb Q\). | **Conditional deduction complete.** It applies once steps 9 and 10 hold together for the same sequence. |

For the substantive finite theorem, put \(D_t=\{2^a3^b\le t\}\), let \(\tau(D_t)\) be its minimum corner-cover size, and color a point by \(a-b\pmod3\). The color counts \(K_j\), isolated-root correction \(I_j\), and patch correction \(P_j\) satisfy
\[
\boxed{\tau(D_t)=\min_j\bigl(K_j(t)-I_j(t)-P_j(t)\bigr),\qquad t\ge3.}
\]
This is the completed **step 6**. Its proof eliminates the unbounded boundary configurations symbolically; exact bounded certificates handle the remaining endpoint intervals. It does not rely on extrapolating numerical agreement. The density normalization is
\[
M=\sum_{a,b\ge0}\eta_{a,b}2^{-a}3^{-b},\qquad
Z=3-3M=9c-6=2-3Q_{\rm full}(0).
\]
Here \(Q_{\rm full}\) uses unexceptional births, with the sole exceptional birth contributing \(1/3\) to \(M\). All low rows are part of this identity. ([Complete finite proof](<../prefix-and-phase-audit/REPORT.md>), [normalization audit](<../numerator-and-residuals/occupation_audit.md>))

The final deduction has a short exact acceptance test. It is sufficient to construct integers \(u_n,v_n\) with
\[
0<|u_nZ+v_n|\longrightarrow0.
\tag{1}
\]
If \(Z=A/B\), then \(B(u_nZ+v_n)=u_nA+Bv_n\) would be a nonzero integer tending to zero, a contradiction. Obtaining a real error tending to zero is therefore only part of the task: it must become a nonzero integer-affine expression **after every denominator and auxiliary readout is paid**. This explains why a numerical completion percentage would misrepresent the present position. ([Established arithmetic framework](<../infinite-return-construction/REPORT.md>), [complete bridge requirements](<../occupation-arithmetic-bridge/REPORT.md>))

## Full real calibration now cancels the interior and controls every interface

The actual high occupation is a positive measure \(\nu^H\) on the lattice \(\mathbb Z[\omega]\), where \(\omega^2+\omega+1=0\), with total mass \(1/27\) and infinite support. Write \(z=x+y\omega=s\omega+t\omega^2\), so \(s=y-x\), \(t=-x\), and take \(\rho(z)=\max(|s|,|t|)\). Four complete cone values telescope to the mass \(\mathcal B_R=\nu^H\{\rho\le R\}\). Hence
\[
\mathcal E_R^{\rm out}=1/27-\mathcal B_R>0
\]
for every radius. The actual unbounded fixed-row path has step at most three in this norm, so every shell \(R<\rho\le R+3\) also has positive mass. The accepted state-height theorem gives fixed effective \(C_\rho>0\), \(0<\kappa<1\), and
\[
0<\mathcal E_R^{\rm out}\le6\,2^{-m_R},\qquad
m_R=\left\lfloor(R/C_\rho)^{1/\kappa}\right\rfloor.
\tag{2}
\]
These are actual infinite-family positivity and complete-tail results. The four translated cone values, including their infinite low-row corrections, remain arithmetically unevaluated. ([Exterior formulas and audit](<exterior_audit.md>))

The stronger current theorem uses the full guarded discounted operator
\[
\mathcal L=216I-27U_A-8U_B+U_AU_B.
\]
The pullbacks \(U_A,U_B\) follow the actual horizontal and vertical lifted dynamics, including phase and event information. For Boolean target \(h\), bounded forcing \(|g|\le G\), and state domain \(D_R=\{\rho\le R\}\), put \(c_0=G+1\), prescribe \(p=c_0+h/182\) outside, and solve \(\mathcal Lp=h+g\) inside. The interior fixed-point equation is
\[
p=\frac{27p_A+8p_B-p_{AB}+h+g}{216}.
\]
Its supremum-norm contraction factor is \(36/216=1/6\), proving a unique bounded real solution. With \(C_0=c_0+1/182\), its global norm is at most \(C_0\). The complete residual satisfies
\[
K_R=0\quad(\rho\le R),\qquad
179c_0-18/91\le K_R\le252C_0+c_0\quad(\rho>R).
\tag{3}
\]
The lower bound is strictly positive and includes all outside-to-inside interfaces. This closes unrestricted bounded-real feasibility, rather than just far-exterior positivity. ([Independent contraction proof](<exterior_audit.md>))

Each low row has its separate operator \(8I-U_A\). Prescribing \(p=c_0+h/7\) outside gives contraction factor \(1/8\), zero interior residual and exterior lower bound \(6c_0-1/7>0\). Thus the high and low calibrations assemble with the same target coefficient and no omitted signed low term. For \(g=0\), the amplitudes are independent of \(R\), and the combined residual integral \(\Psi_R\) is strictly positive and tends to zero by the complete height-tail estimate. The exact transport pairing gives
\[
S_R=Q_{\rm full}(0)+\Gamma+\Psi_R,\qquad
\boxed{Z=2-3S_R+3\Gamma+3\Psi_R.}
\tag{4}
\]
Here \(\Gamma\) is the full forcing readout; it vanishes for \(g=0\). The source \(S_R\) is a finite rational-coefficient combination of nine high and twelve low initial lifted values of \(p\). ([Full source pairing and low-row proof](<exterior_audit.md>))

**Those finitely many initial values are unknown reals.** The interior domain contains infinitely many phase contexts, even though the lattice state box is finite. Contraction does not make it a finite rational linear system. For \(g=0\), proving integers \(T_R>0\) with \(T_RS_R\in\mathbb Z\) and \(T_R\Psi_R\to0\) would turn (4) into (1). A sufficient growth budget is \(\log T_R=o(R^{1/\kappa})\); growing residual amplitudes must also be charged. Neither rationality nor such a clearing estimate is established. This calibration works for arbitrary bounded target data, so its real existence alone cannot distinguish an irrational target from a rational one. ([Arithmetic limitation and budget](<exterior_audit.md>))

## Pure-phase arithmetic is classified but does not remove state flux

There is now a complete scalar test. For irrational rotation \(R_\theta\), integer \(b\ge2\), and a finite rational-valued right-continuous step function \(h\), its discounted readout
\[
G_h(x)=\sum_{n\ge0}b^{-n}h(R_\theta^nx)
\]
is rational at one starting point if and only if
\[
h=f-b^{-1}f\circ R_\theta
\]
for a finite rational step transfer \(f\). Rationality propagates along the dense orbit into a bounded rational lattice; uniform approximation then forces the readout itself to be finite step. On each cut orbit \(c_j=c_0+j\theta\), the equivalent finite test is
\[
\sum_j b^{-j}\Delta h(c_j)=0.
\tag{5}
\]
The reconstructed rational constant must also vanish when testing an exact zero relation. Arbitrary rational endpoint overrides need a separate finite rational orbit correction; the functional converse applies to the canonical right-continuous function. These qualifications prevent false claims caused by endpoint spikes or integer digit carries. ([Complete converse and independent audit](<coboundary_audit.md>))

For the actual horizontal guards, cuts \((k-s\alpha)/3\), \(\alpha=\log2/\log3\), occupy exactly nine rotation orbits. Nine explicit Boolean guards have charge determinant \(-7\), proving that their numerical readouts together with 1 form an **exactly ten-dimensional rational space**. Reconstruction has bit height linear in context span and input height. The vertical analogue gives an at-most-100-dimensional product span, restricted to the actual horizontal and vertical cut-orbit modules. It does not include arbitrary new cuts or assert independence of the products. The same charges prove rational independence of 1 and both lattice coordinates of the actual horizontal affine moment. These are genuine arithmetic theorems, but their observables differ from the target cone density. ([Basis, heights and moments](<coboundary_audit.md>))

A previous result already gives adequate arithmetic returns on an actual infinite subsequence for nonconstant Boolean horizontal phase codes. Their common clearer is \(8^q-1\), with cleared error at most \((8/7)2^{s_*+2q-Q}\). A proved unrestricted subsequence satisfies \(Q-2q>q/3\), so fixed contexts work without a large-partial-quotient conjecture. This direct periodic-code argument invokes no growing-dimensional Kohlmeyer–Kruer seed estimate. It still does not prove the stronger joint supply needed by the original scalar density models. ([Pure-guard theorem and scope](<../occupation-arithmetic-bridge/REPORT.md>))

The obstacle to using these results state by state is explicit. Along \(T(y,x)=(y+\Phi(x),Rx)\), a phase transfer acquires a changing-state flux. One actual cone/guard example has zero scalar coboundary readout at every fixed state, yet its full joint readout lies in
\[
[-57/448,-55/448]<0.
\]
The entire infinite tail is included. A pure-phase cancellation therefore cannot erase a state-conditioned term without paying this flux. Nor can the ten-dimensional numerical closure be treated as a finite invariant partition or a rational representation of the coupled Dirichlet source. ([Actual flux identity and certificate](<coboundary_audit.md>))

## The remaining routes require different arithmetic theorems

The alternatives below are routes through steps 9–10, rather than requirements that must all be solved. Each has its own matching obligation.

| Route | What is proved | What remains necessary |
|---|---|---|
| Signed scalar models | Exact integer clearing, complete error bound and uniform nonvanishing on six eligible state classes. | An actual infinite eligible subsequence with \(Q-5q\to\infty\); infinitely many eligible next digits at least five would suffice. |
| Positive occupation/calibration | Actual infinite support, positive decaying returns, full transport, and now bounded real calibration including every low row and interface. | A target-dependent exact or positivity-preserving approximate arithmetic bridge with affordable clearing. For (4), source arithmetic remains open. |
| Corrected fan models | Full expansion, actual numerator congruences, and nonvanishing on specified subfamilies. | Arithmetic of the actual response constants, sufficient whole-model denominator cancellation, and infinite applicability together. |
| Hierarchical models | An actual infinite sequence with small real residual and full boundary identity. | Affordable arithmetic for the entire boundary and nonvanishing of that same residual. |

These statuses are established in the accepted scalar, numerator/residual and hierarchy reports; the current work changes the real-feasibility and guard-arithmetic components, rather than resolving their remaining arithmetic conjunctions. ([Scalar status](<../signed-arithmetic-returns/REPORT.md>), [fan and occupation status](<../numerator-and-residuals/REPORT.md>), [hierarchy status](<../hybrid-arithmetic-closure/REPORT.md>))

The scalar route makes the missing supply especially concrete. For actual consecutive convergents \(p/q,P/Q\) in the permitted current-model class, its rational value \(z\) satisfies
\[
D z\in\mathbb Z,\qquad D=27(2^{3q}-1)(3^{3p}-1),\qquad
D|Z-z|\le486(1+o(1))2^{5q-Q}.
\]
Here \(Q\) is the immediate successor denominator, not the next member of a chosen sparse sequence. The nonvanishing theorem handles the specified six eligible first-mediant states. What is not supplied is infinitely many actual visits satisfying both eligibility and the adequate gap \(Q-5q\to\infty\). Unrestricted infinite visits adequate for pure horizontal guards use the weaker threshold \(Q-2q\); changing that threshold or discarding the state condition would change the theorem. Thus this route needs a genuine actual-slope supply result, rather than additional finite precision at an already verified convergent. ([Scalar denominator, eligibility and full error](<../signed-arithmetic-returns/REPORT.md>), [guard threshold](<../occupation-arithmetic-bridge/REPORT.md>))

The current finite-volume tests also prove failures that constrain future attempts. Every phase exits a fixed finite one-axis state box within a uniform finite time; hence a killed Poisson solution is a finite rational step function on a sufficiently large common refinement. For a positive odd reward, the cleared head \(8p_0\) has reduced denominator exactly \(8^{\tau-1}\), while \(p_0\) itself has denominator \(8^\tau\), and the cleared positive residual is at least \(1/8\). This ansatz cannot meet (1). A binary noncompact boundary prescription permits denominator cancellation instead. Its exact source numerator is
\[
N_\tau=1+h_\tau+7\sum_{n<\tau}8^{\tau-1-n}h_n,
\quad p_0=\frac{N_\tau}{7\,8^\tau}.
\]
Seven never cancels. Adequacy for this particular one-axis construction is equivalent to unbounded terminal-one runs ending at an exit zero. **No theorem supplies those runs at actual exits**, and its one-axis target still needs a complete relation to \(Z\). ([Finite-volume and carry audit](<calibration_audit.md>))

A fully priced density rectangle also fails: the unexceptional reward \(1+6\bar\eta\) sums to \(7-2Z\), and its odd-by-odd head has exact denominator \(2^{A-1}3^{B-1}\). Its cleared positive complement diverges. Pure compact mixed-Green clipping has a separate row/column-marginal obstruction to a one-signed exterior. These are scoped counterarguments, not a universal prohibition on signed, noncompact or joint-state constructions. ([Rectangle audit](<calibration_audit.md>), [compact obstruction audit](<exterior_audit.md>))

Three current independent audits report PASS with the stated scope clarifications, supported by supplied and standalone exact standard-library checkers. They reconstruct original boards, phase cuts and complete tails rather than treating finite patterns as infinite theorems. The density's finite rational-denominator exclusion remains **greater than \(2^{56}\)**; the new real and guard results do not improve it. ([Current calibration audit](<calibration_audit.md>), [finite exclusion](<../signed-arithmetic-returns/REPORT.md>))

Overall, the structural reduction and exact finite optimization are established, and analytic positivity is available for complete actual families. The next decisive theorem must control the arithmetic of one such family while preserving its nonzero error. For the latest calibration, the concrete target is the source \(S_R\) in (4): prove an affordable clearing relation, or replace it with a target-dependent approximation whose error preserves positivity. Until that is done, the infinite-return objective remains open.

Skipped: Lean verification, external peer review and novelty/priority checks. Material risk: treating finite collections of unknown real source values, or pure-phase numerical closure, as the missing arithmetic bridge to \(Z\).
