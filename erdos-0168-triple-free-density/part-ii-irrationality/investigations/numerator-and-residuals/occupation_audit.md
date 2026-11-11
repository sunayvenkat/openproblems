# Independent audit of occupation potentials and positive returns

## Are the complete occupation formulas and Green kernels correctly normalized?

### Takeaway

**PASS; no substantive erratum.** The occupation identities are exact convolutions of positive measures, with the low rows and the exceptional origin paid separately. The high-row point-source identity is archival; the complete row formulation and its use below do not rationalize any translated value. — [Audited note](response_arithmetic.md), [archival H12–H13](../hybrid-arithmetic-closure/hybrid_compression.md), [independent checker](occupation_audit_check.py).

### Cited Findings

- The accepted state separates as \(A_a+B_b-1+C_{a,b}-\mathbf1_{b\ge4}E_b\). Canonical responses multiply \(A_a\) by a cube root \(\gamma\), then add the specified residue-dependent endpoint displacement. — [Accepted actual definitions](../response-closure-tests/response_relations.md), [RA1–RA3](response_arithmetic.md).
- The supplied checker passes. The independent checker imports no project module and rebuilds actual axes directly from original colored boards, row tests from differences of minima, and the eight canonical endpoint states from their published specification. — [Supplied checker](response_arithmetic_check.py), [independent checker](occupation_audit_check.py).

### Inferences

For \(i,j\in\{0,1,2\}\), the measures
\[
\mathsf A_i=\sum_{a\equiv i(3)}2^{-a}\delta_{A_a},\qquad
\mathsf B_j=\sum_{\substack{b\ge4\\b\equiv j(3)}}3^{-b}\delta_{B_b-1-E_b}
\]
have the claimed rational total masses. Their nine shifted convolutions put precisely one original weight \(2^{-a}3^{-b}\) at every high-row plus state. Their combined mass is \(2\sum_{b\ge4}3^{-b}=1/27\). For each low row, the vertical measure is a single atom with its original weight, while the horizontal sum remains infinite. Absolute convergence justifies convolution, regrouping and every bounded-kernel pairing. This is a product-measure identity, not a claim that the cone readout factors into two scalar readouts or known rational totals. — [RA1–RA3](response_arithmetic.md), [independent eight-response product tests](occupation_audit_check.py).

Writing \(m(x,y)=\min(0,x,y)\), the integer-state identity
\(F(z)=m(z)-m(z-1)\) agrees with \(F(x+y\omega)=\mathbf1_{x\le0,\ x\le y}\). Thus the high response is the stated second difference of a common minimum potential. Axis increments are bounded, so the potential grows at most linearly in \(a+b\); its weighted absolute sum converges. No divergent potential is being differentiated. — [RA2 and accepted axis increments](response_arithmetic.md), [minimum-difference implementation](occupation_audit_check.py).

Let \(Q_{\mathrm{full}}\) denote the **unexceptional** complete cone/row readout used in the note. Its value at zero omits the sole birth override at \((0,1)\), of weight \(1/3\). Hence the true birth series is \(M=Q_{\mathrm{full}}(0)+1/3\), and
\[
Z=3-3M=2-3Q_{\mathrm{full}}(0),\qquad
Q_H(t)=Q_{\mathrm{full}}(t)-L(t).
\]
The constant two is correct. The independent checker confirms the target coefficients against direct finite-optimum differences, including \((0,1)\), and reproduces the complete rational models exactly at \(12/19\) and \(53/84\). It reconstructs each model axis as its own rational colored triangle and uses full geometric occupation periods, rather than a truncated model or a companion import. — [RA4 and RA3 model specialization](response_arithmetic.md), [independent complete normalization](occupation_audit_check.py).

For \(D_v f(z)=f(z)-f(z-v)\), direct calculation gives
\[
D_\omega F=\mathbf1_{x=y\le0},\qquad
D_\omega D_{\omega^2}F=\delta_0.
\]
The first difference is a diagonal ray; subtracting its translate by \(-\omega^2=1+\omega\) removes only its endpoint. The old H12 is an equivalent translated, signed form, so this basic high-row stencil is not a new discovery. — [Archival stencil](../hybrid-arithmetic-closure/hybrid_compression.md), [RA6](response_arithmetic.md).

The complete low-row rules are also correct. The identities
\[
\Phi_1(z)=F(\omega(z-1)),\quad
\Phi_2(z)=F(z-\omega^2),\quad
\Phi_3(z)=1-F(\omega^2(z+\omega))
\]
prove, by rotating and translating the high-row stencil,
\[
D_1D_\omega\Phi_1=\delta_1,\quad
D_\omega D_{\omega^2}\Phi_2=\delta_{\omega^2},\quad
D_1D_{\omega^2}\Phi_3=-\delta_{-\omega}.
\]
Row zero is zero. In particular the row-three sign cannot be replaced by positivity. The independent checker verifies all four kernels and their weighted translated versions, retaining each row measure. — [RA4 complete row proof](response_arithmetic.md), [independent kernel tests](occupation_audit_check.py).

For target high-row occupation \(\nu^H\), boundedness of \(F\) and finite mass give
\[
D_\omega D_{\omega^2}Q_H(t)=\nu^H(-t).
\]
Replacing \(Q_H\) by the full target readout requires subtracting the same differences of \(L\). Those four low rows have infinite horizontal extent and are not automatically rational. Any comparison of actual and model products likewise retains both one-axis defects: bilinearity gives \(\mu*\nu-\widetilde\mu*\widetilde\nu=(\mu-\widetilde\mu)*\nu+\widetilde\mu*(\nu-\widetilde\nu)\); expanding about both model factors also retains the mixed defect. No such defect is silently set to zero here. — [Complete product definitions and explicit gaps](response_arithmetic.md), [earlier boundary limitations](../weighted-response-identities/weighted_audit.md).

### Gaps

- No identity equates these distinct cone, ray, vertex or translated readouts arithmetically. Rationality of \(Z\) has not rationalized the canonical responses, occupation coefficients or complete low rows. — [RA1 and RA7 limitations](response_arithmetic.md).
- The accepted finite optimum and canonical endpoint definitions are inputs; their full global proofs are not reconstructed by the present finite checks. — [Accepted finite foundation](../prefix-and-phase-audit/REPORT.md).

## Does the precise actual horizontal orbit force an infinite positive family?

### Takeaway

**PASS.** The cited unboundedness really concerns \(A_{3m}\) of the actual logarithm ratio. I independently reconstructed the saved row-sum reduction and checked the primary bounded-remainder theorem. It is sufficient for infinite high-state support at one fixed row; no generic-phase or abstract-slope substitution is involved. — [Original reduction](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md), [R3](../infinite-return-construction/ray_return_attack.md), [Kelly–Sadun, Theorem 1](https://arxiv.org/html/1404.0455).

### Cited Findings

- Direct original-board summation gives \(A_a=\omega^{-a}\mathcal K(2^a)\), so \(A_{3m}=\mathcal K(2^{3m})=W(3m\log2)\). The independent checker reconstructs these board counts and the exact row-sum identity at the sampled cutoffs. — [Original-board identity](../correlated-return-arithmetic/fan_audit.md), [independent exact reconstruction](occupation_audit_check.py).
- Kelly–Sadun's primary proof states that the discrepancy of an interval under an irrational rotation is bounded precisely when its length is congruent modulo one to an integer multiple of the rotation angle. The stated discrepancy fixes a starting point; changing endpoint conventions here changes only a bounded number of terms. — [Primary Theorem 1](https://arxiv.org/html/1404.0455).

### Inferences

Here is the actual-support argument reconstructed independently. Put \(\beta=\log_2 3\), \(B_m=\lfloor3m/\beta\rfloor\) and \(W_m=\mathcal K(2^{3m})\). The last dyadic exponent in row \(b\) is \(3m-\lceil\beta b\rceil\). Its geometric color sum gives exactly
\[
(1-\omega)W_m=
\sum_{b=0}^{B_m}\omega^{-b}
-\omega\sum_{b=0}^{B_m}\omega^{-\lceil(\beta+1)b\rceil}.
\tag{A1}
\]
The first sum is uniformly bounded. Let \(\theta=(\beta+1)/3\). For positive \(b\), the summand in the second sum is \(\omega^2,\omega,1\) on the successive thirds of \(\{b\theta\}\). No positive iterate hits a third endpoint, because \(\theta\) is irrational. Therefore the discrepancy of the last third through index \(B\) equals \((2/3)\operatorname{Re}\sum_{b=1}^B\omega^{-\lceil(\beta+1)b\rceil}\). It is unbounded: \(1/3\notin\mathbb Z\theta+\mathbb Z\), so the primary criterion applies. — [Original derivation, independently reconstructed here](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md), [primary criterion](https://arxiv.org/html/1404.0455).

The sampling does not lose that unboundedness. From \(2^3<3^2<2^4\), one has \(3/2<\beta<2\), hence \(1<3/\beta<2\). Consecutive \(B_m\) differ by one or two. If the second sums in A1 were bounded only at these sampled indices, every intermediate prefix would also be bounded, since each omitted increment is a unit. Thus \(W_m\), and therefore the precise actual \(A_{3m}\), is unbounded. This establishes the needed phase-zero input directly; the stronger all-phase escape portion of R3 is unnecessary for this deduction. — [Actual sampled reduction](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md), [R3 sampling audit](../infinite-return-construction/final_return_audit.md).

At fixed \(b=4,a=3m\), every residue and patch term is constant:
\[
\zeta_{3m,4}=A_{3m}+B_4-1+C_{0,1}-E_4.
\]
Unboundedness gives infinitely many distinct occupied states. Each has positive mass because it is attained at an actual cell with positive weight. The same conclusion holds for canonical plus-state measures, since their fixed-row states are \(\gamma A_{3m}\) plus a constant, with \(\gamma\ne0\). This proof uses actual support, not finite arrival examples. — [RA8](response_arithmetic.md), [independent fixed-row consistency checks](occupation_audit_check.py).

For an occupied state \(z\), the first total-index arrival \(N(z)=\min\{a+b:b\ge4,\ \zeta_{a,b}=z\}\) exists. Finitely many cells have total index at most any fixed bound. Hence infinitely many distinct states have a subsequence \(z_n\) with \(N_n=N(z_n)\to\infty\). Every mass contributing to that state is outside the smaller total-index triangle, so
\[
0<\nu^H(z_n)\le\sum_{\substack{a,b\ge0\\a+b\ge N_n}}2^{-a}3^{-b}
=6\,2^{-N_n}-3\,3^{-N_n}\to0.
\tag{A2}
\]
Summing first over \(a\ge\max(N-b,0)\), then separating \(b<N\) and \(b\ge N\), proves the displayed full-quadrant tail. It safely overbounds the high-row domain. The Green identity gives the actual four-cone return exactly, with last argument \(1-z_n\) because \(\omega+\omega^2=-1\). — [RA9–RA10](response_arithmetic.md), [independent finite arrival/tail/Green checks](occupation_audit_check.py).

The suggested exact selection search also terminates: the states reached at \(a+b<M\) form a finite set, and the unbounded fixed-row states eventually leave it. No quantitative escape-time estimate has been asserted. — [RA5 selection argument](response_arithmetic.md).

### Gaps

- The external bounded-remainder theorem is used as a primary theorem input, not reproved in full. Its irrational-angle and interval-length hypotheses were checked. — [Kelly–Sadun](https://arxiv.org/html/1404.0455).
- Neither the support proof nor A2 provides a rational lattice for the atoms or translated potentials. These are positive **real** returns. — [Explicit RA5 gaps](response_arithmetic.md).

## Does the proposed arithmetic bridge finish the problem, and what has actually been checked?

### Takeaway

**PASS for the conditional bridge; the original objective remains incomplete.** A proved cheap integer-affine identity would finish irrationality because the new family already has actual infinitude, positivity and decay. Such identities have not been constructed. — [RA11 and its explicit hypothesis](response_arithmetic.md).

### Cited Findings

- Both supplied and independent checkers finish successfully. The standalone checker has no project imports, no floating arithmetic and no solver. It verifies all eight finite response products, low/high kernels, the origin, complete rational models, actual board sampling and first-arrival examples. — [Supplied certificate](response_arithmetic_check.py), [independent certificate](occupation_audit_check.py).
- The independently reproduced first arrivals are \(4,5,7,7,12,26\). These are finite certificates for the exact definitions, not a substitute for the unboundedness argument. The model values agree exactly with the accepted complete values at \(12/19\) and \(53/84\), not merely in denominator lengths. — [Independent checker](occupation_audit_check.py).

### Inferences

Suppose identities \(T_n\nu^H(z_n)=u_nZ+v_n\), with positive integer \(T_n\) and integer \(u_n,v_n\), were proved with \(\log_2T_n\le(1-\varepsilon)N_n\) eventually for a fixed \(\varepsilon>0\). If \(Z=A/B\) were rational, \(BT_n\nu^H(z_n)=u_nA+Bv_n\) would be a positive integer, yet A2 bounds it by \(6B2^{-\varepsilon N_n}\to0\). This contradiction is valid. In particular \(\log T_n=o(N_n)\) is sufficient, and no separate height bound on \(u_n,v_n\) is needed. — [RA11, independently checked](response_arithmetic.md).

The warning against free arithmetic is also correct. If one integer \(T\) cleared every occupied atom, their infinitely many positive integer masses would contradict finite total mass \(T/27\). If a particular atom is rational, its reduced denominator is at least the reciprocal of its mass, and hence exceeds \(2^{N(z)}/6\). Thus small positive masses do not have cheap denominators merely because their coefficients are integer digits. This neither proves any specified atom irrational nor excludes the target-dependent bridge when \(Z\) is irrational. — [RA12](response_arithmetic.md).

The sole known target relation supplies one complete unexceptional cone value at zero. The four state translations in the return and their low-row corrections remain separate arithmetic readouts. State translation is not a physical index shift. No connection equating the digit-one corrected-fan defect with one positive atom is established by these identities alone. — [RA4 and explicit gaps](response_arithmetic.md), [archived warning](../hybrid-arithmetic-closure/hybrid_compression.md).

### Gaps

- **Final disposition: PASS; no substantive audit erratum.** The actual positive family is valid, but the integer-affine bridge, response rationality and adequate infinite arithmetic return remain unproved. — [Audited scope](response_arithmetic.md).
- Skipped: Lean, external review, a full reproof of the bounded-remainder theorem and a global reproof of the archived finite optimum. Material risk: promoting the positive real atoms or rational total measure masses into a cheap target-dependent arithmetic identity.
