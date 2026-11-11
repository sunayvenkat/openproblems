# Actual occupation potentials and positive returns

## Can the complete actual responses be represented by one weighted state construction?

### Takeaway

**Yes.** Nine products of one-dimensional discounted occupation measures, together with the explicitly retained low rows, represent the target and every canonical response. This is an exact common state-potential interface, not an arithmetic evaluation. The basic high-row point-source stencil is already present in the archived hybrid work; the new statements below are its complete low-row/product formulation and its application to an actual infinite positive-return family. — [Accepted actual arrays](../response-closure-tests/response_relations.md), [archived point-source identity H12–H13](../hybrid-arithmetic-closure/hybrid_compression.md), [new exact checker](response_arithmetic_check.py).

### Cited Findings

- The actual unexceptional state is \(\zeta_{a,b}=A_a+B_b-1+C_{a,b}-\mathbf1_{b\ge4}E_b\). The arrays \(A,B\), periodic color correction \(C\), indicator correction \(E\), four low-row tests, and the original target's sole exceptional birth at \((0,1)\) are accepted proved inputs. — [Canonical definitions RR1–RR3](../response-closure-tests/response_relations.md), [independent original-board reconstruction](../response-closure-tests/response_audit.md).
- A canonical state \(R=(p_0,q_0,e)\) has \(\gamma=\omega^{2p_0-q_0}\), \(\kappa=\omega^{-q_0}S(p_0-1)\), and plus-state \(z_R(a,b)=\gamma A_a+B_b-1-\mathbf1_{b\ge4}E_b+\xi_{ij}^R\), where \(i=a\bmod3,j=b\bmod3\) and
  \[
  \xi_{ij}^R=e-\gamma+\kappa P_i^-+C_{i+q_0,j},\qquad
  P_i^-=\sum_{k=1}^{i}\omega^{-k}.
  \]
  Its response is \(-3[\Phi_b(z_R)-\Phi_b(z_R-\gamma)]\), with no exceptional origin insertion. — [Exact shifted endpoint formula RR1–RR2](../response-closure-tests/response_relations.md).
- The new checker uses those accepted axis definitions but independently constructs the state occupation products and all four Green kernels. It reproduces the finite rectangles of all eight fan responses and the complete rational scalar models at \(12/19\) and \(53/84\). — [Checker](response_arithmetic_check.py), [complete scalar definition](../reflected-return-models/two_sided_models_check.py).

### Inferences

**RA1. Positive occupation products.** Work in the group algebra of \(\mathbb Z[\omega]\), identifying \(x+y\omega\) with \((x,y)\), and let \(\delta_z\) denote unit mass at state \(z\). Define
\[
\mathsf A_i=\sum_{a\equiv i\ (3)}2^{-a}\delta_{A_a},\qquad
\mathsf B_j=\sum_{\substack{b\ge4\\b\equiv j\ (3)}}3^{-b}\delta_{B_b-1-E_b}.
\tag{RA1}
\]
These are positive \(\ell^1\) measures. Their masses are exactly
\[
\|\mathsf A_i\|_1=\frac{2^{-i}}{1-2^{-3}},\qquad
\|\mathsf B_j\|_1=\frac{3^{-b_j}}{1-3^{-3}},\quad(b_0,b_1,b_2)=(6,4,5).
\]
Let \(\rho_\gamma\) push a state forward by multiplication by \(\gamma\). The complete high-row plus-state measure of response \(R\) is
\[
\boxed{\nu_R^H=\sum_{i,j=0}^2\delta_{\xi_{ij}^R}*
      (\rho_\gamma\mathsf A_i)*\mathsf B_j.}
\tag{RA2}
\]
Its mass is \(2\sum_{b\ge4}3^{-b}=1/27\). For a fixed low row \(b<4\), the exact measure is instead
\[
\nu_R^{(b)}=3^{-b}\sum_{i=0}^2
\delta_{B_b-1+\xi_{i,b\bmod3}^R}*(\rho_\gamma\mathsf A_i).
\tag{RA3}
\]
Expanding the convolution gives exactly one original weight \(2^{-a}3^{-b}\) at each corresponding state. All exchanges are justified by absolute convergence. This factorization is a Fubini identity for the Cartesian index sum; it does **not** assert statistical independence of the deterministically linked axes. — [Accepted state separation](../boundary-and-arithmetic/arithmetic.md), [all-eight-response product checks](response_arithmetic_check.py).

For the target take \(\gamma=1,\xi_{ij}=C_{ij}\) in RA2–RA3. Write the resulting measures as \(\nu^H,\nu^{(b)}\), and let
\[
F(x+y\omega)=\mathbf1_{x\le0,\ x-y\le0},\qquad
Q_H(t)=\langle F(\cdot+t),\nu^H\rangle,
\]
\[
L(t)=\sum_{b=0}^3\langle\Phi_b(\cdot+t),\nu^{(b)}\rangle,
\qquad Q_{\rm full}(t)=Q_H(t)+L(t).
\]
The target's exceptional birth has weight \(1/3\), so its complete relation is
\[
\boxed{Z=2-3Q_{\rm full}(0),\qquad Q_H(t)=Q_{\rm full}(t)-L(t).}
\tag{RA4}
\]
The constant is **two**, not three: total geometric coefficient mass is three and the sole origin override subtracts one from the scalar value. Low rows are infinite horizontal series. Neither \(Q_H(0)\) nor any translated value has been evaluated by RA4. — [Origin correction in the complete scalar model](../reflected-return-models/two_sided_models_check.py), [independent target coefficient spot checks](response_arithmetic_check.py).

**RA2. A common minimum potential.** Put \(m(x,y)=\min(0,x,y)\) and \(D_vf(z)=f(z)-f(z-v)\). Then \(F=D_1m\). Hence a high-row response is exactly
\[
\Gamma_R^H=-3\langle D_\gamma D_1m,\nu_R^H\rangle.
\tag{RA5}
\]
All potentials are summable: the axis increments have bounded size, so \(|z_R(a,b)|=O(a+b+1)\), and the binary/ternary weights have finite first moments. Thus these are legitimate weighted derivatives of one minimum potential applied to the products RA2, not a formal substitution into a divergent series. — [Accepted bounded axis increments](../response-closure-tests/response_relations_check.py), [exact Green checks](response_arithmetic_check.py).

**RA3. The very same construction reproduces complete rational models.** For a nonresonant rational model, replace the horizontal occupations by one full \(3q\)-period divided by \(1-2^{-3q}\), and the high vertical occupations by the rows \(4\le b<4+3p\) divided by \(1-3^{-3p}\). Keep the four low rows separately. RA4 then gives its full value \(z\), including the unique origin override exactly once. The checker verifies exact equality, not just denominator sizes, for two actual current models. The whole period numerator is therefore a cone functional of these finite occupation numerators; the actual responses are boundary derivatives of the corresponding actual products. No identity equating those two different readouts has been proved. — [Complete periodic model](../reflected-return-models/two_sided_models_check.py), [exact equality certificates](response_arithmetic_check.py).

### Gaps

- The common construction has not implied \(Z\in\mathbb Q\Rightarrow\Gamma_R\in\mathbb Q\), nor a sufficient congruence for the whole corrected model numerator. Cone values, ray values and individual vertex coefficients remain different linear functionals of the products.
- This is not another short-filter rank assertion. It retains the full infinite occupation measures and every low row; those objects still require arithmetic control. — [Earlier shift-boundary limitations](../weighted-response-identities/weighted_audit.md).

## Does the state Green identity produce infinitely many actual nonzero small returns?

### Takeaway

**Yes for an explicitly defined family of positive real four-cone differences.** Actual horizontal-axis unboundedness, already proved for the precise phase-zero cocycle, guarantees infinitely many positive vertex masses. Their decay has an elementary explicit bound. No claim makes these real returns arithmetic yet. — [Precise actual-cocycle theorem R3](../infinite-return-construction/ray_return_attack.md), [audit confirming the phase-zero sampling](../infinite-return-construction/final_return_audit.md), [new finite first-arrival checks](response_arithmetic_check.py).

### Cited Findings

- The accepted actual board identity is \(A_a=\omega^{-a}\mathcal K(2^a)\), where \(\mathcal K(t)=\sum_j\omega^jK_j(t)\). In particular \(A_{3n}=\mathcal K(2^{3n})\). — [Original-board reconstruction](../correlated-return-arithmetic/fan_audit.md), [new direct board-count checks](response_arithmetic_check.py).
- With \(W(T)=\mathcal K(e^T)\), the saved actual-cocycle theorem proves unbounded phase-zero sums in
  \[
  W(T+3n\log2)-W(T)=\sum_{k=0}^{n-1}\Phi(x+k\alpha),\quad
  x=T/(3\log3)\bmod1.
  \]
  Thus \(A_{3n}=W(3n\log2)\) is unbounded. This is the actual logarithmic orbit at its fixed origin, not an abstract-slope example or a claim about color imbalance at arbitrary unrelated cutoffs. — [R3 and its exact sampling argument](../infinite-return-construction/ray_return_attack.md), [final audit, actual cocycle section](../infinite-return-construction/final_return_audit.md).
- The archived high-row localization already proves an equivalent shifted point-source identity. It is not claimed as newly discovered here. — [H12–H13](../hybrid-arithmetic-closure/hybrid_compression.md).

### Inferences

**RA4. Complete row Green kernels.** On every integer state,
\[
D_\omega D_{\omega^2}F=\delta_0.
\tag{RA6}
\]
Indeed \(D_\omega F=\mathbf1_{x=y\le0}\); shifting by \(-\omega^2=(1,1)\) removes exactly its endpoint. The low rows satisfy the following complete list:

| Row | Localizing directions | Result |
|---|---|---|
| 0 | any | zero |
| 1 | \(1,\omega\) | \(D_1D_\omega\Phi_1=\delta_1\) |
| 2 | \(\omega,\omega^2\) | \(D_\omega D_{\omega^2}\Phi_2=\delta_{\omega^2}\) |
| 3 | \(1,\omega^2\) | \(D_1D_{\omega^2}\Phi_3=-\delta_{-\omega}\) |
| at least 4 | \(\omega,\omega^2\) | \(\delta_0\) |

For a direct proof of the low rules,
\[
\Phi_1(z)=F(\omega(z-1)),\qquad
\Phi_2(z)=F(z-\omega^2),\qquad
\Phi_3(z)=1-F(\omega^2(z+\omega)).
\]
Conjugating RA6 by these rotations/translations gives the table, including the negative row-three sign. Applying the operators to RA2–RA3 is justified because the kernels are bounded and the measures are in \(\ell^1\). In particular
\[
\boxed{D_\omega D_{\omega^2}Q_H(t)=\nu^H(-t).}
\tag{RA7}
\]
The same statement, with the appropriate row vertex and sign, holds for every canonical response plus-state occupation. — [Exact all-integer kernel proofs above; checker](response_arithmetic_check.py), [archival high-row counterpart](../hybrid-arithmetic-closure/hybrid_compression.md).

**RA5. Infinite actual positive support.** Fix \(b=4\) and \(a=3n\). All color and isolate/patch terms are fixed, so
\[
\zeta_{3n,4}=A_{3n}+B_4-1+C_{0,1}-E_4.
\tag{RA8}
\]
The accepted unboundedness of \(A_{3n}\) makes these states unbounded and hence distinct infinitely often. Every such state has positive \(\nu^H\)-mass. More generally each canonical plus state at these indices is \(\gamma A_{3n}\) plus a fixed vector, so all canonical high-row measures have infinite positive support too. This implication does not infer infinite behavior from the finite checker. — [Exact actual-axis input cited above](../infinite-return-construction/ray_return_attack.md), [finite board/fixed-row consistency checks](response_arithmetic_check.py).

For a positive atom \(z\), define its first total-index arrival
\[
N(z)=\min\{a+b:\ b\ge4,\ \zeta_{a,b}=z\}.
\]
Only finitely many cells have \(a+b\le M\), so an infinite sequence of distinct occupied states has a subsequence with \(N(z_n)\to\infty\). Its mass obeys the exact complete tail estimate
\[
\boxed{0<\nu^H(z_n)\le
\sum_{a+b\ge N(z_n)}2^{-a}3^{-b}
=6\,2^{-N(z_n)}-3\,3^{-N(z_n)}\longrightarrow0.}
\tag{RA9}
\]
The displayed full-quadrant tail overbounds the high-row domain. Split its sum at \(b=N\): the first part is \(6\,2^{-N}-6\,3^{-N}\), and the remaining part is \(3\,3^{-N}\). No cancellation or nonvanishing hypothesis is needed, because all masses are positive.

Combining RA7 and RA9 gives the actual infinite real returns
\[
\boxed{\begin{aligned}
\mathcal E_n={}&Q_H(-z_n)-Q_H(-z_n-\omega)
 -Q_H(-z_n-\omega^2)+Q_H(1-z_n)\\
={}&\nu^H(z_n)>0,\qquad
\mathcal E_n\le6\,2^{-N(z_n)}-3\,3^{-N(z_n)}.
\end{aligned}}
\tag{RA10}
\]
Every low-row term is retained through \(Q_H=Q_{\rm full}-L\); the operator applied to \(Q_{\rm full}\) must have the same operator applied to \(L\) subtracted. These are state translations, not physical shifts in \(a,b\), and the translated readouts are not asserted to be new extremal densities. — [RA4–RA9; exact finite Green/arrival certificates](response_arithmetic_check.py).

The family can be selected by an exact search: for a prescribed integer \(M\), enumerate the finite state set attained at cells \(a+b<M\), then follow the fixed row \((3n,4)\) until it leaves that set. RA8 guarantees termination; the chosen atom has first arrival at least \(M\). There is no claimed effective bound on the needed row index from the non-effective unboundedness theorem. — [Actual unboundedness input](../infinite-return-construction/ray_return_attack.md).

### Gaps

- RA10 proves infinitude, positivity and decay for these **real state-cone returns**. It proves no rational-lattice statement for them and no adequate infinite arithmetic return.
- No general identification of the full fan's digit-one quotient-comparison defect with one RA10 atom is proved. The Green formula is relevant only after an actual state-displacement/transport identity has been established; matching scales or signs is not such a proof.
- The precise existing actual-axis unboundedness theorem is reused; this note does not reconstruct Kesten's full theorem or reprove the entire earlier cocycle reduction.

## What arithmetic bridge would make the positive returns prove irrationality?

### Takeaway

A cheap integer-affine bridge from the positive vertex masses to the single target would finish irrationality, with no continued-fraction digit-supply or further nonvanishing assumption. **That bridge remains unproved.** The occupation factorization and Green identities alone do not provide it. — [Positive family RA10](response_arithmetic_check.py), [accepted target relation](../correlated-return-arithmetic/REPORT.md).

### Cited Findings

- Rationality of \(Z\) has not rationalized translated cone values, complete low-row profiles, or the canonical response values in the accepted work. — [H13 arithmetic limitation](../hybrid-arithmetic-closure/hybrid_compression.md), [complete shift dictionary](../weighted-response-identities/weighted_audit.md).
- The finite occupation checker uses standard-library exact arithmetic. It verifies all eight response product representations, all four Green kernels, the unique origin normalization, two complete rational model values, the original-board identity along the first sixteen three-doubling samples, and finite first-arrival atoms. It does not use those samples as an infinitude proof. — [Checker](response_arithmetic_check.py).

### Inferences

**RA6. A sufficient integer-affine bridge.** Suppose the RA10 atoms admit identities
\[
T_n\nu^H(z_n)=u_nZ+v_n,\qquad
T_n\in\mathbb Z_{>0},\quad u_n,v_n\in\mathbb Z,
\tag{RA11}
\]
with \(\log_2 T_n\le(1-\varepsilon)N(z_n)\) eventually for some fixed \(\varepsilon>0\). The stronger condition \(\log T_n=o(N(z_n))\) is sufficient. Under a hypothetical \(Z=A/B\),
\[
BT_n\nu^H(z_n)=u_nA+Bv_n
\]
is a positive integer, while RA9 bounds it by \(6B\,2^{-\varepsilon N(z_n)}\to0\), a contradiction. No height restriction on \(u_n,v_n\) is needed for this elementary fixed-denominator argument. Thus a proved bridge RA11 would establish irrationality of \(Z\), hence of the density. The statement is a conditional criterion, not a construction of its identities.

**RA7. Why vertex occupation is not free arithmetic.** Infinite positive support and finite total mass imply that no integer \(T>0\) makes \(T\nu^H(z)\) an integer for every occupied \(z\): infinitely many nonzero integer masses would sum to more than \(T/27\). Quantitatively, if an atom of first arrival \(N\) is rational, its reduced denominator satisfies
\[
\operatorname{den}\nu^H(z)\ge\frac1{\nu^H(z)}
\ge\frac1{6\,2^{-N}-3\,3^{-N}}>2^N/6.
\tag{RA12}
\]
Accordingly a uniformly bounded denominator for all translated high-cone values is impossible too, because RA7 would transfer it to all atoms. This does not imply that any specified atom is irrational: rational atoms with unbounded denominators remain possible. Nor does RA12 rule out the target-dependent bridge RA11 when \(Z\) is irrational. Rather, RA11 would force rationality of \(Z\) to imply an arithmetic property contradicted by RA9/RA12.

The target relation RA4 determines only one full cone readout at zero. Even its high-row part has the separate low-row profile \(L(0)\). The four translated values in RA10 do not follow arithmetically from that one number. The positive convolution factorization therefore supplies a common exact object on which to seek an arithmetic identity, not a deduction that rationality passes to its individual coefficients or derivatives. — [Earlier translated-readout warning](../hybrid-arithmetic-closure/hybrid_compression.md), [new complete product normalization](response_arithmetic_check.py).

### Gaps

- No RA11 bridge, no sufficient whole-model numerator congruence and no rationality transfer for actual response values is proved. The original infinite arithmetic-return objective remains open.
- This positive family has its own proved actual infinitude and nonvanishing. Those facts do not transfer to every corrected fan residual or to the separate hierarchy, and its arithmetic interface must not be exchanged with theirs.
- Skipped: new external theorem searches, a full reproof of the accepted unboundedness/cocycle inputs, Lean, external review and priority verification. Material risk: presenting state translation as a physical-index shift, or the positive real returns as already lying in the required rational lattice.
