# Positive finite-volume exteriors and compact-cutoff signs

## Can exterior positivity and decay be made uniform in state radius?

### Takeaway

**Yes, at the level of actual real returns.** Green-coordinate boxes have exact four-corner cone formulas; their outside masses are positive for every radius and decay faster than any coefficient growth allowed by the audited state-height budget. A shell version also has an actual fixed-row witness. None of these formulas supplies a target-affine arithmetic relation. — [Accepted positive occupation construction](<../numerator-and-residuals/occupation_audit.md>), [audited quantitative height bound](<../occupation-arithmetic-bridge/height_audit.md>).

### Cited Findings

- The actual high-state occupation is a positive measure \(\nu^H\) on \(\mathbb Z[\omega]\), of total mass \(1/27\), and
  \[
  D_\omega D_{\omega^2}Q_H(t)=\nu^H(-t),\qquad
  Q_H=Q_{\rm full}-L,\qquad Z=2-3Q_{\rm full}(0).
  \]
  The low rows in \(L\) are infinite horizontally. The basic high-row Green stencil is archival. — [Complete occupation/normalization audit](<../numerator-and-residuals/occupation_audit.md>), [archival H12–H13](<../hybrid-arithmetic-closure/hybrid_compression.md>).
- For the actual high state \(\zeta_{a,b}\), the accepted fixed effective constants \(C>0\), \(0<\kappa=K/(K+1)<1\) give
  \[
  \max(|x|,|y|)\le C(a+b+1)^\kappa,\qquad \zeta_{a,b}=x+y\omega .
  \]
  Actual \(\zeta_{3n,4}\) is unbounded. — [Height theorem](<../occupation-arithmetic-bridge/height_audit.md>), [precise actual-support proof](<../numerator-and-residuals/occupation_audit.md>).
- The exact checker verifies the finite formulas, complete-tail algebra, actual step bounds, and occupied sign witnesses below. It reuses the accepted actual-axis definitions rather than claiming to reprove the global finite optimum. — [Exact checker](<exterior_check.py>).

### Inferences

**EX1: choose the Green-coordinate geometry.** Write
\[
z=s\omega+t\omega^2,\qquad s=y-x,\quad t=-x,
\qquad \rho(z)=\max(|s|,|t|).
\]
Then \(F(z)=\mathbf1_{\{s\ge0,t\ge0\}}\). The norms satisfy
\[
\rho(z)\le2\max(|x|,|y|),\qquad
\max(|x|,|y|)\le2\rho(z).
\]
In particular, for \(C_\rho=2C\),
\[
\rho(\zeta_{a,b})\le C_\rho(a+b+1)^\kappa.
\tag{EX1}
\]
This changes the shape of the region, not the accepted arithmetic budget.

**EX2: four complete cone values give a box mass.** Define
\[
\mathcal B_R=\nu^H\{z:\rho(z)\le R\},\qquad R\in\mathbb Z_{\ge0}.
\]
Summing the Green identity over \(-R\le s,t\le R\) telescopes twice:
\[
\boxed{\begin{aligned}
\mathcal B_R={}&Q_H(-R)
-Q_H(-(R+1)\omega+R\omega^2)\\
&-Q_H(R\omega-(R+1)\omega^2)+Q_H(R+1).
\end{aligned}}
\tag{EX2}
\]
Indeed, if \(q(s,t)=Q_H(-s\omega-t\omega^2)\), then the atom at \(s\omega+t\omega^2\) is
\(q(s,t)-q(s+1,t)-q(s,t+1)+q(s+1,t+1)\).
Only the four displayed corners remain. Absolute convergence of the positive finite-mass occupation permits this finite summation without an omitted side.

Consequently
\[
\boxed{\mathcal E_R^{\rm out}=\frac1{27}-\mathcal B_R
=\nu^H\{\rho>R\}>0}
\tag{EX3}
\]
for every \(R\): the actual support is infinite, whereas a lattice box is finite. These are positive actual real returns formed from four translated cone values and one rational constant. Their positivity does not require a sparse state selection or a conjectural continued-fraction visit. It does not make the four values rational or target-affine.

**EX3: the complete exterior tail includes the arithmetic growth.** Set
\[
m_R=\max\!\left(0,\left\lfloor(R/C_\rho)^{1/\kappa}\right\rfloor\right).
\]
If \(\rho(\zeta_{a,b})>R\), EX1 forces \(a+b\ge m_R\). Thus
\[
0<\mathcal E_R^{\rm out}
\le6\,2^{-m_R}-3\,3^{-m_R}
\le6\,2^{-m_R}.
\tag{EX4}
\]
The equality used for the full-quadrant tail is
\[
\sum_{\substack{a,b\ge0\\a+b\ge m}}2^{-a}3^{-b}
=6\,2^{-m}-3\,3^{-m}.
\]
For example, split at \(b=m\), sum \(2^{1-m+b}3^{-b}\) below the split, and sum the complete dyadic mass above it. This safely overbounds the actual high domain \(b\ge4\).

Hence \(\mathcal E_R^{\rm out}\le\exp[-cR^{1/\kappa}+O(1)]\) for a fixed \(c>0\). No upper escape-time estimate is asserted. The radius estimate supplies a lower bound on the total index of every exterior arrival.

More generally, let a **whole corrected** kernel \(\psi_R\) satisfy
\[
\psi_R=0\quad(\rho\le R),\qquad
0\le\psi_R\le B_R .
\]
Then
\[
0\le\langle\psi_R,\nu^H\rangle
\le B_R(6\,2^{-m_R}-3\,3^{-m_R}).
\tag{EX5}
\]
If the kernel is strictly positive on all states with \(\rho>R+D\), for a fixed \(D\), its integral is strictly positive by actual infinite support. A sufficient alternative is strict positivity on the full shell below. If a complete identity
\[
T_R\langle\psi_R,\nu^H\rangle=u_R Z+v_R,
\quad T_R\in\mathbb Z_{>0},\quad u_R,v_R\in\mathbb Z
\tag{EX6}
\]
were proved, then
\[
\log(T_RB_R)=o(R^{1/\kappa})
\tag{EX7}
\]
would make its cleared positive value tend to zero. A hypothetical rational \(Z=A/B\) would then produce positive integers \(BT_R\langle\psi_R,\nu^H\rangle\to0\). Both the denominator and kernel-amplification cost must be charged; bounding \(T_R\) alone is insufficient. In particular, a bound \(O(R^d)\) for this combined logarithm is affordable whenever \(d<1/\kappa=1+1/K\).

**EX4: a local shell has an actual witness.** The root-unit horizontal increments have Green-coordinate norm at most one. At fixed \(b=4,a=3n\), residue and patch terms are constant, so
\[
\rho(\zeta_{3(n+1),4}-\zeta_{3n,4})\le3 .
\]
Here \(\zeta_{0,4}=0\): original board counts give \(A_0=1,B_4=\omega,E_4=\omega,C_{0,1}=0\). The path is unbounded. At its first crossing of radius \(R\), therefore,
\[
R<\rho(\zeta_{3n,4})\le R+3 .
\]
The full shell return
\[
\mathcal E_R^{\rm sh}=\mathcal B_{R+3}-\mathcal B_R
=\nu^H\{R<\rho\le R+3\}
\tag{EX8}
\]
is positive for every nonnegative integer \(R\), has the same upper bound EX4, and is an exact combination of eight complete cone values. Its first-crossing witness contributes \(3^{-4}8^{-n}>0\). A sparse proper subset of that shell has no automatic witness. The checker reproduces the first sampled crossings \(R=0,a=3,z=(0,-1)\) and \(R=1,a=96,z=(1,-1)\); the infinite statement rests on bounded steps and actual unboundedness. — [Accepted actual-axis increment and support formulas](<../numerator-and-residuals/occupation_audit.md>), [exact finite shell check](<exterior_check.py>).

### Gaps

- EX6 is a conditional arithmetic interface, not a constructed bridge. Four- or eight-term state translation does not imply an integer physical-index identity.
- Replacing \(Q_H\) by \(Q_{\rm full}\) requires every translated low-row term \(L\). The target normalization alone supplies only \(Q_{\rm full}(0)\).
- A signed exterior bound does not imply positivity of its integral. EX5–EX8 require the stated whole-kernel sign or actual witness.

## Can a noncompact outer potential reduce positivity to finitely many interface checks?

### Takeaway

**Yes, conditionally on an interior calibration.** A fixed rational outer prescription makes the far exterior uniformly positive, independently of the guard action. The unresolved work is exact interior cancellation, the finite interface inequalities, complete low-row matching and an affordable rational source; the lemma does not supply those.

### Cited Findings

- The complete high adjoint is
  \[
  \mathcal L=216I-27U_A-8U_B+U_AU_B,
  \qquad \mathcal L1=182,
  \]
  with \(U_A,U_B\) the actual three-step pullbacks. Its pairing has the exact finite sources stated in ET5–ET8. The displayed zero-bulk resolvent is not already a nonzero-target calibration. — [Complete transport audit](<../occupation-arithmetic-bridge/transport_audit.md>).
- Physical high-state displacements obey Green-radius bounds \(3\) horizontally, \(5\) vertically, and \(8\) jointly. The vertical bound includes the difference of the two bounded isolate/patch corrections. — [Actual increment and high correction formulas](<../occupation-arithmetic-bridge/exact_transport.md>), [exact sampled checks](<exterior_check.py>).

### Inferences

**EX5: the far-exterior prescription.** Let \(h\) be the target Boolean kernel (for high rows, \(h=F(\zeta)\)). Let \(g(x,v)\) be a **global pure-phase** forcing with \(\|g\|_\infty\le G\), \(G\ge0\). Prescribe outside \(\rho>R\)
\[
p_\infty=\frac{h+G+1}{182}.
\tag{EX9}
\]
Whenever all four current/successor states lie in that exterior,
\[
\begin{aligned}
\mathcal Lp_\infty-h-g
&=G+1-g\\
&\quad+\frac{34h-27h_A-8h_B+h_{AB}}{182}.
\end{aligned}
\tag{EX10}
\]
The last numerator has absolute value at most \(35\), since its positive coefficients total \(35\), as do its negative coefficients. Therefore
\[
\boxed{\frac{147}{182}
\le \mathcal Lp_\infty-h-g
\le 2G+\frac{217}{182}.}
\tag{EX11}
\]
For \(g=0\), the outer potential takes only the two values \(1/182,2/182\). This conclusion is an exact algebraic bound for all sixteen Boolean quadruples; it is not a typical-phase estimate.

If \(p_R\) equals EX9 outside \(\rho>R\), all four arguments use that prescription whenever the current \(\rho>R+8\). Thus the far exterior already has a fixed positive margin. A finite-volume candidate only needs:

1. the exact interior equation \(\mathcal Lp_R-h-g=0\) for \(\rho\le R\);
2. nonnegativity on \(R<\rho\le R+8\);
3. its complete rational source and multiplier-height proof.

If the ansatz depends on a finite interval phase partition, every image must be evaluated on the larger common refinement. No invariant partition is assumed. The interior and interface assertions remain unproved for a useful actual candidate. Infeasibility of a robust all-state/all-phase ansatz would not exclude an actual-support calibration.

**EX6: low rows have a separate positive outer prescription.** Their horizontal adjoint is \(\mathcal L_A=8I-U_A\), with \(\mathcal L_A1=7\). For each Boolean low rule \(h_b=\Phi_b\), choose
\[
p_{\infty,b}=\frac{h_b+G_b+1}{7}.
\]
Then
\[
\frac67\le\mathcal L_Ap_{\infty,b}-h_b-g_b
\le2G_b+\frac87
\]
whenever \(|g_b|\le G_b\). Only a width-three interface is needed horizontally. This uses the low Boolean rules themselves; it does not turn the negative row-three Green kernel into a positive source.

For the complete target, high and low calibrations must use the same coefficient of their target readouts. Only after their actual low-row residuals are cancelled or given proved signs can the full positivity argument be used. The finite source and any global pure-phase forcing must be shown rational and cleared. A phase forcing multiplied by a state-region indicator is not a pure-phase term; applying marginal guard arithmetic to it would be invalid.

Thus EX9–EX11 provide a concrete bounded noncompact boundary condition, not a solution of the finite-volume Poisson/adjoint problem. The complete identity would pair \(\mathcal Lp_R=h+g+\psi_R\) against the actual occupation product. A proved rational readout of \(g\) and a proved rational finite source would leave the target plus \(\langle\psi_R\rangle\); the factor \(Z=2-3Q_{\rm full}(0)\) and a fixed clearing factor three must then be paid. No such complete candidate is asserted here.

### Gaps

- Far positivity alone gives neither interior feasibility nor a small rational multiplier. The bound on \(p_\infty\) is not a bound on unknown interior coefficients.
- The global forcing may be handled only by a proved complete arithmetic relation. Irrational guard values are not automatically rational; the present lemma assumes no scalar independence factorization.
- The separate high and low kernels must assemble into one whole target identity. An uncancelled signed low term can destroy positivity.

## Why does compact Green clipping fail as a one-signed exterior scheme?

### Takeaway

**A compact pure-state Green potential cannot leave a one-signed exterior balancing a point source.** Row and column marginals prove the general scoped obstruction, and a natural square cutoff has both signs on actual occupied states. Noncompact potentials and the full discounted guarded adjoint remain outside this obstruction.

### Cited Findings

- The state Green operator is \(D_\omega D_{\omega^2}\), and the actual measure is positive. Its high/low distinction and normalization are accepted inputs. — [Occupation audit](<../numerator-and-residuals/occupation_audit.md>).
- The checker uses exact original accepted axes and phase corrections. It verifies compact row/column cancellation, actual occupied sign witnesses, four-corner box telescoping, eight-corner shells, and all high/low outer Boolean bounds. — [Reproducible checker](<exterior_check.py>).

### Inferences

**EX7: mixed-difference marginals.** In coordinates \(z=s\omega+t\omega^2\), write \(D_s,D_t\) for the backward unit differences. If \(f\) has finite support, every fixed-row and fixed-column sum of \(D_sD_t f\) is zero, by telescoping.

Suppose \(D_sD_t f=\delta_0+e\), where \(e(0)=0\) and \(e\) is an exterior kernel. If \(e\ge0\), total summation gives \(0=1+\sum e\), impossible. If \(e\le0\), put \(r=-e\ge0\). Row marginals of \(\delta_0-r\) force \(r\) onto the zero-th row, and column marginals force it onto the zero-th column. Thus \(r\) must be supported only at the origin, contradicting \(r(0)=0\) and its total mass one. Consequently \(e\) has both signs.

In particular a compact potential agreeing with the fundamental cone near the source cannot prove a globally nonnegative balancing exterior in either orientation. This is a theorem about that compact pure-state mixed-difference construction, not about \(\mathcal L\), noncompact outer conditions, or numerical weighted-value cancellations.

For the compact Green-coordinate rectangle
\[
f_R(z)=\mathbf1_{\{0\le s,t\le R\}},
\]
the obstruction is visible explicitly:
\[
D_\omega D_{\omega^2}f_R
=\delta_0-\delta_{(R+1)\omega}
-\delta_{(R+1)\omega^2}+\delta_{-(R+1)}.
\tag{EX12}
\]
The three exterior vertices already have mixed signs. This formula and the row/column proof hold for every \(R\), independent of the actual occupation support.

**EX8: an actual occupied sign failure.** As a separate concrete test, clip the cone by the original coefficient square,
\[
\widetilde f_1(z)=F(z)\mathbf1_{\{\max(|x|,|y|)\le1\}},
\qquad e_1=D_\omega D_{\omega^2}\widetilde f_1-\delta_0 .
\]
Exact actual states give

| Actual cell | State | \(e_1\) |
|---|---|---:|
| \((a,b)=(12,8)\) | \(-2-2\omega\) | \(-1\) |
| \((a,b)=(22,35)\) | \(-1+\omega\) | \(+1\) |

Both states have positive occupation, at least their displayed original weights. Thus this particular exterior is neither pointwise nonnegative nor pointwise nonpositive even on the **actual** support. The first actual Green-radius exit from radius one has total index eight; the fixed-row path has a different first crossing, as expected. — [Exact witness and geometry checker](<exterior_check.py>).

This does not determine the sign of the integrated \(e_1\), prove both signs on actual support for every radius, or refute a corrected full-state/phase scheme. The role of the example is to break the unproved pointwise-positivity shortcut.

### Gaps

- No finite-volume test potential with nonzero target coefficient, complete rational source and affordable denominator has been produced.
- No exact or approximate occupation arithmetic bridge is established; no proof of Erdős #168(ii) follows.
- Skipped Lean, external review, new proofs of the accepted global finite theorem/Matveev input, and optimization of the height constants. Material risk: treating EX6 as an achieved identity, or far-exterior positivity as proof of interior calibration feasibility.
