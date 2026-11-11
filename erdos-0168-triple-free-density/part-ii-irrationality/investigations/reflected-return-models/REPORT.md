# Exact return identities expose Erdős’s remaining gaps

**The finite optimization in our approach to Erdős #168(ii) has a complete ordinary proof and two internal adversarial audits. The irrationality proof remains incomplete, and the infinite-return goal remains active.** The completed formula determines every finite smooth-component optimum and removes the former combinatorial hypothesis from the arithmetic construction. The remaining work is to produce an adequate infinite family of weighted arithmetic approximations and prove that its errors are nonzero infinitely often. The latest positive result gives exact mixed corner support and a product-of-two-tail error; its comparison value still contains two infinite hybrid sums with no proved arithmetic compression. Other new lemmas explain why reflection, order-three endpoint returns and local carry restrictions do not automatically supply that compression. These are audited auxiliary results, with no claim of Lean verification, external acceptance or historical priority. ([Finite proof](<../prefix-and-phase-audit/REPORT.md>), [final return audit](<final_reflected_audit.md>))

Here the target is part (ii): if \(F(N)\) is the largest size of a subset of \(\{1,\ldots,N\}\) containing no complete triple \(\{n,2n,3n\}\), prove that \(c=\lim F(N)/N\) is irrational. Existence of this limit and the smooth-component reduction are established background, not new results of this investigation. A closed-form evaluation for part (i) is not claimed. ([Target](https://conjectures.io/problems/erdos168-erdos-168-parts-ii), [density reduction and background](https://arxiv.org/html/2604.15515v1))

The table is a dependency map for the present strategy. “Proved” means a written ordinary argument with the stated internal checks; it does not mean a formally verified or externally reviewed theorem. The rows have very different difficulty, so their number is not a completion percentage.

| Step | Required result | Current progress |
|---|---|---|
| 1 | Establish the limiting density and reduce integers to components \(m2^a3^b\), \((m,6)=1\). | **Known background; complete.** Each forbidden triple lies in one component. |
| 2 | Express the density through finite-component birth increments. | **Complete.** The absolutely convergent series below gives \(Z=9c-6\), making irrationality of \(Z\) equivalent to the target. |
| 3 | Construct the corrected three-color covers. | **Proved.** Isolated dyadic points and the valid three-to-two patch give the proposed upper bound for the finite minimum. |
| 4 | Classify positive matching deficiency away from the vertical axis. | **Proved.** The unrestricted axis-avoiding classification leaves only the permitted isolate or patch, including for multiple-root sets. |
| 5 | Control vertical-axis deficiencies and put the required omissions inside one common optimum. | **Proved.** Restricted maximizers, the single-exclusion argument and prefix augmentations close the compatibility gap. |
| 6 | Prove the exact finite optimum at every cutoff. | **Proved:** formula (C) below holds for every real \(t\ge3\). Both final finite audits pass. |
| 7 | Derive the exact corrected birth dynamics. | **Complete.** Both accumulated axis states, the residue term, active exception and four low-column rules are retained. |
| 8 | Construct rational models with proved denominators, height and matching windows. | **Complete as a framework.** Nonresonant convergents give the explicit integer-cleared model and error bound below. Its adequacy infinitely often remains unproved. |
| 9 | Obtain an adequate infinite weighted-return family for the actual logarithmic slope. | **Open, with partial results.** The real product-tail estimate is proved. The scalar route lacks sufficient actual convergent supply; the hybrid route also lacks arithmetic compression. |
| 10 | Prove nonvanishing or nonstabilization along that family. | **Open.** Nonzero individual digits or mixed cells do not establish a nonzero infinite weighted remainder. |
| 11 | Apply the arithmetic contradiction to conclude \(c\notin\mathbb Q\). | **Conditional implication ready.** It becomes a proof after steps 9 and 10 hold for the same family. |

The finite dependency chain and its two final audits support steps 3–6; the earlier return report supplies steps 2, 7 and 8. The latest audit explicitly leaves steps 9 and 10 open. ([Finite assembly](<../prefix-and-phase-audit/REPORT.md>), [established arithmetic framework](<../infinite-return-construction/REPORT.md>), [current audit](<final_reflected_audit.md>))

For the completed finite result, let \(D_t=\{2^a3^b\le t:a,b\ge0\}\), and let \(\tau(D_t)\) be its minimum corner-cover size. Color each point by \(a-b\bmod3\), and write \(K_j(t)\) for the color counts. The indicator \(I_j\) records a dyadic root \(e=2^A\), \(A\ge1\), of color \(j\) with \(2t/3<e\le t\); \(P_j\) records one with \(6e\le t<27e/4\). At most one exceptional root is active across all colors. The proved formula is

\[
\boxed{\tau(D_t)=\min_j\bigl(K_j(t)-I_j(t)-P_j(t)\bigr)\qquad(t\ge3).} \tag{C}
\]

The lower bound is the substantive completed advance. It controls arbitrary positive deficiency over allowed owner pools, uses a common global optimum for the color comparison, and eliminates the unbounded boundary family by prefix repairs. Exact bounded certificates handle the remaining endpoint intervals. Older reports describing (C) as conjectural are superseded by this proof and its final audits. ([Complete proof and validation](<../prefix-and-phase-audit/REPORT.md>))

Let \(\eta_{a,b}\in\{0,1\}\) be the increment of \(\tau\) at insertion of \(2^a3^b\). Then

\[
Z=\sum_{a,b\ge0}\frac{1-3\eta_{a,b}}{2^a3^b}=9c-6.
\]

For \(b\ge4\), the exact digit is the closed-cone readout of \(A_a+B_b-1+C_{a,b}-E_b\): \(A,B\) are accumulated floor cocycles, \(C\) is the residue correction and \(E\) retains the active isolate or patch. The four low columns have separate proved rules. This gives an explicit arithmetic object without assuming a bounded actual state or a finite register. ([Birth dynamics and normalization](<../infinite-return-construction/REPORT.md>))

The scalar route states a precise sufficient theorem for step 9. Put \(\alpha=\log_3 2\), take consecutive convergents \(p/q,p'/q'\), and require \(p+q\not\equiv0\bmod3\). The correct one-sided model agrees with the true array for \(a<q+q'\), \(b<p+p'\). Its weighted value \(\widetilde Z\) satisfies

\[
D=27(2^{3q}-1)(3^{3p}-1),\qquad N=D\widetilde Z\in\mathbb Z,
\]
\[
|DZ-N|\le486(1+o(1))\,2^{5q-q'}.
\]

If \(Z=A/B\) were rational, \(DZ-N\) would lie in the fixed lattice \(B^{-1}\mathbb Z\). Therefore **an infinite eligible sequence with \(q'-5q\to+\infty\)** would force eventual equality. Infinitely many eligible next partial quotients at least five would suffice for this upper approximation. Neither that actual supply nor the nonstabilization needed to contradict equality is proved. The established universal supply gives infinitely many eligible ratios above \((15+\sqrt5)/10\), which does not meet the scalar threshold. ([Scalar estimate and supply](<../infinite-return-construction/REPORT.md>))

The newest positive identity improves the real error by combining four arrays. Use true or model horizontal data in the first position, and true or model vertical data in the second, retaining the exception and low rules. Their weighted sums are \(Z_{TT}=Z,Z_{MT},Z_{TM},Z_{MM}\), with \(Z_{MM}\) rational. For \(R=q+q'\), \(S=p+p'\), the mixed coefficient \(\Delta=c_{TT}-c_{MT}-c_{TM}+c_{MM}\) vanishes whenever \(a<R\) **or** \(b<S\). Its magnitude is at most six. Absolute convergence proves

\[
M=Z_{TT}-Z_{MT}-Z_{TM}+Z_{MM},\qquad
|M|\le18\,2^{-R}3^{-S}.
\]

This is a complete theorem about the actual array and its models. The narrow actual-logarithm check finds 38 nonzero mixed cells in its specified rectangle, including \(\Delta(27,19)=3\). Those cells do not prove \(M\ne0\), because further weighted terms can cancel. ([Product-tail proof and certificate](<record_returns.md>))

The missing arithmetic theorem concerns \(J=Z_{MT}+Z_{TM}-Z_{MM}\). The identity gives a small real error \(Z-J\), but **no proof makes \(DJ\) integral or expresses \(J\) in an adequate fixed arithmetic form**. Each hybrid still contains one true unbounded axis process. If \(DJ\in\mathbb Z\) were established at the existing clearing cost along an infinite sequence, the product bound would give a cleared error at most \(486(1+o(1))2^{4q-2q'}\). The sufficient supply threshold would improve to \(q'-2q\to+\infty\). This remains conditional: hybrid compression, appropriate actual supply and nonvanishing are unresolved. ([Exact interface](<record_returns.md>), [independent audit](<final_reflected_audit.md>))

The other new arguments sharpen those requirements. Opposite-side reflection is exact for the uncorrected state, including axes and rational ties. The corrected high coefficients fail that palindrome in all three named models; exact ray and low-row terms remain in the numerator. Reversal evaluates the opposite polynomial at \((2,3)\), not at the original reciprocal weights. No growing 2-adic or 3-adic divisibility follows from the proved reflection. Separately, the full paired numerator has the genuine factor \(x^q-y^p\), whose scalar consequence does not supply an adequate exponential saving. The formal vertical cancellation obstruction applies to two named models and the specified readout architecture; it does not cover every scalar approximation or infinite subsequence. ([Reflection analysis](<numerator_reflection.md>), [paired-model proof](<two_sided_models.md>))

Continued-fraction induction reaches the origin-anchored endpoints and weighted profiles exactly. A nonresonant block returns its complete endpoint state after three copies, while the weighted evaluation retains its cubic period denominator. The all-level early-hit theorem is specifically for the comparison slope \(\alpha_*=[0;1,1,1,1,1,3,\overline{2,1}]\). Including reciprocal rows and their prescribed correction, it exhibits coupled ties at indices of order \(q_L\) while the current scale is \(q_{3L}=\Theta(q_L^3)\). It disproves a universal inference that large recentering forces exponentially late positive tie support. It proves hits, not firstness; it establishes no such trajectory for \(\log_3 2\), no synthetic-board optimality and no prohibition of coherent signed cancellation. ([Exact induction](<cf_induction.md>), [comparison theorem](<record_returns.md>))

There is also a genuine new target-array constraint: for \(b\ge4\), the digits at \(d,2d,3d,6d\) never form \(1001\). Every other four-cell binary motif occurs. The theorem follows from the exact state curl and horizontal increment alphabet. However, a rational nonperiodic countermodel obeys the same forbidden motif, can preserve any finite actual head, and can retain the full fifteen-pattern language. It need not satisfy the actual floor and residue constraints. Consequently that local language alone cannot establish irrationality or the required canonical carry control. ([Actual carry theorem and countermodel](<actual_carries.md>))

For an alternative nonintegral S-unit architecture, the lower-bound interface still requires fixed term count, controlled rational coefficients and height, a nonzero error and the essential scale restriction \(0<t\le\min(1,u_1,\ldots,u_m)\). Endpoint recurrence or small spatial support does not verify these weighted arithmetic hypotheses. The integer-cleared scalar model instead needs only an error tending to zero under rationality; imposing a stronger Subspace Theorem margin would unnecessarily strengthen that task. ([Arithmetic acceptance audit](<final_reflected_audit.md>), [KK primary manuscript, Proposition 7.4](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf))

The finite/combinatorial foundation is complete in the current written proof, and the arithmetic framework and product-tail identity are established. The next decisive theorem must control an actual infinite weighted family together with its full denominator or coefficient cost. A separate nonvanishing theorem must apply to that same family. **The final audit gives a qualified PASS to the auxiliary results and rejects completion of the infinite-return objective.** No meaningful numerical percentage follows from the completed preparatory steps. ([Final audit](<final_reflected_audit.md>))

Skipped: Lean, external review and priority verification. The material risk is treating the proved small real hybrid error as an arithmetic approximation before its comparison value has controlled arithmetic.
