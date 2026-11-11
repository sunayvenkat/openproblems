# Fixed logarithms close the nonvanishing gap

**Correct-side nonvanishing is now proved uniformly for every sufficiently late eligible balanced first mediant.** A primary-source application of Matveev's theorem to the two fixed logarithms of 2 and 3 removes the previous successor-ratio, following-digit and child-sign restrictions within that domain. It also upgrades the four-response approximation from an absolute expansion to a relative one. This scalar nonvanishing argument needs no Kohlmeyer–Kruer seed. Three independent audits pass, including separate exact reconstructions of the finite certificates. **The adequate infinite arithmetic return is still unproved:** no theorem supplies infinitely many actual indices with the necessary states and denominator gaps, and neither arithmetic investigation below constructs a cheaper replacement. ([Logarithm audit](<fixed_logs_audit.md>), [boundary audit](<weighted_audit.md>), [elimination audit](<paired_audit.md>))

Let \(c=\lim F(N)/N\), where \(F(N)\) is the largest size of a subset of \([1,N]\) avoiding every complete triple \(\{n,2n,3n\}\). The completed finite theorem determines the minimum corner-cover size on \(D_t=\{2^a3^b\le t:a,b\in\mathbb Z_{\ge0}\}\):
\[
\tau(D_t)=\min_j\bigl(K_j(t)-I_j(t)-P_j(t)\bigr),\qquad t\ge3.
\]
Here \(K_j\) counts color \(a-b\bmod3\), and \(I_j,P_j\) retain the isolated-root and exceptional-patch corrections. This is an ordinary proof for every real cutoff, with the vertical-axis case and common-optimum issue resolved in the earlier audits. Its birth increments \(\eta_{a,b}\in\{0,1\}\) give the absolutely convergent target
\[
Z=\sum_{a,b\ge0}(1-3\eta_{a,b})2^{-a}3^{-b}=9c-6.
\]
Thus irrationality of \(Z\) is equivalent to irrationality of the density. These completed reductions remain inputs here. ([Finite proof and audits](<../prefix-and-phase-audit/REPORT.md>), [density and scalar framework](<../signed-arithmetic-returns/REPORT.md>))

**The new estimate controls the mediant on the current denominator's scale.** Matveev's original Theorem 2.1, on journal page 1219, gives fixed effective constants \(\kappa>0,K\ge1\) such that
\[
|m\log2-n\log3|>\kappa\max(1,m,n)^{-K}
\tag{1}
\]
for positive integers \(m,n\). The application uses the field \(\mathbb Q\), its positive real logarithms, integer coefficients \((m,-n)\), and fixed height choices \(A_1=A_2=2\). The source's coefficient parameter is consequently \(B=\max(1,m,n)\). Prime valuations prove integer independence of the two logarithms and nonvanishing of the form. No unknown response constant enters its coefficients, and neither the dimension nor the algebraic numbers vary. Both researchers checked the primary statement and definitions; the full proof of Matveev's theorem is an established external input. ([Matveev, Theorem 2.1, pp. 1218–1219](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3), [specialization and independent review](<fixed_logs_audit.md>))

Write \(\alpha=\log2/\log3\), take consecutive actual convergents \(p/q,P/Q\), and put
\[
r=p+P,\qquad s=q+Q,\qquad
\sigma=\operatorname{sign}(\alpha-p/q),\qquad
\Delta=2^{-s}-3^{-r}.
\]
The convergent inequality and (1) imply
\[
\kappa q^{-K}<|q\log2-p\log3|<\frac{\log3}{Q},
\qquad Q<C_1q^K,\qquad s<C_2q^K.
\]
Applying the same theorem again, with integer coefficients \(s,-r\), gives
\[
|s\log2-r\log3|>\kappa_2q^{-K^2},\qquad
|\Delta|>e^{-1}\kappa_2\,2^{-s}q^{-K^2},
\tag{2}
\]
where \(\kappa_2=\kappa C_2^{-K}>0\). The exponential conversion follows from \(\Delta=2^{-s}(1-e^{s\log2-r\log3})\); its exponent has absolute value below one eventually. This double application is essential: a weak bound expressed only in the potentially much larger \(s\) would not supply the needed old-\(q\) scale. All constants are fixed and effective, though enormous and unoptimized. ([Derivation FL1–FL7](<fixed_logs.md>), [independent scale audit](<fixed_logs_audit.md>))

The required balanced nonresonant mediant states are explicit. With \(\omega^2+\omega+1=0\) and \(H(r,s)=\sum_{a=0}^{s-1}\omega^{a+\lfloor ra/s\rfloor}\), set
\[
\mathcal B=\{(0,1,1),(1,1,1),(2,0,2+\omega),(2,2,2)\}.
\]
Eligibility means \(p+q\not\equiv0\pmod3\) for the current model and \((r\bmod3,s\bmod3,H(r,s))\in\mathcal B\) for its first mediant. Eventually all slopes lie in \((3/5,2/3)\). The necessary short direct and reciprocal floors agree automatically by Farey exclusion once \(r,s>24\); this fact does not prove the balance condition. The successor itself need not be nonresonant. ([Accepted complete jump domain](<../signed-arithmetic-returns/signed_scalar.md>), [new domain audit](<fixed_logs_audit.md>))

For \(E=Z-\widetilde Z^\sigma_{p,q}\), the accepted complete first-mediant comparison is
\[
|E-\sigma J|\le R,\qquad
|J|>\frac1{20}|\Delta|,
\]
where \(R\) includes the entire variation in both open Farey child intervals. Independent reconstruction bounds each child's variation by \((855/4)2^{-A}\), with \(A=q+s\) or \(s+Q\), so
\[
R\le\frac{855}{2}2^{-(s+q)}<432\,2^{-(s+q)}.
\]
Together with (2), this yields
\[
\frac R{|J|}<\frac{8640e}{\kappa_2}q^{K^2}2^{-q}\longrightarrow0.
\tag{3}
\]
Hence a fixed effective threshold works for every eligible index and all four states. The correct-side error is nonzero and, eventually,
\[
|E|>\frac{\kappa_2}{40e}2^{-s}q^{-K^2}.
\]
Both infinite variation tails and the complete jump quotient are retained; no isolated disagreement is substituted for the full weighted error. ([Full comparison and constants](<fixed_logs_audit.md>))

The four actual response constants \(G_R\), defined directly from the actual axis sequences, already satisfy complete nonzero enclosures. Their earlier absolute expansion now becomes
\[
Z-\widetilde Z^\sigma_{p,q}
=\sigma\Delta G_R\left(1+O(q^{K^2}2^{-q})\right).
\tag{4}
\]
Uniformity follows from \(|G_R|>1/20\) and the charged quotient-approximation error. Since consecutive convergent errors alternate and decrease in magnitude, \(\sigma\Delta<0\); the eventual error sign is therefore **minus the sign of \(G_R\)**. This covers all sixteen previously classified compatible children, including the eleven opposite-sign cases, without adding their jumps. It supersedes the old asymptotic case split within the balanced-first-mediant domain, while preserving the usefulness of the earlier finite certificates. It establishes no assertion for arbitrary unbalanced mediants and no rationality of \(G_R\) under rationality of \(Z\). ([Actual responses and complete expansion](<../response-closure-tests/response_relations.md>), [relative-expansion and sign audit](<fixed_logs_audit.md>))

**The scalar criterion now has one remaining joint supply premise.** Its complete rational model satisfies
\[
D_{p,q}\widetilde Z^\sigma_{p,q}\in\mathbb Z,\qquad
D_{p,q}=27(2^{3q}-1)(3^{3p}-1),
\]
\[
D_{p,q}|E|\le486(1+o(1))2^{5q-Q}.
\tag{5}
\]
Suppose an unbounded set of actual indices has a nonresonant current model, first-mediant state in \(\mathcal B\), and \(Q-5q\to+\infty\) along those same indices. Equation (3) supplies eventual nonvanishing, and (5) makes the cleared errors tend to zero. If \(Z=A/B\) were rational, \(BD_{p,q}E\) would be a nonzero integer tending to zero, a contradiction. **The joint infinite state/gap premise is not proved.** The polynomial upper bound on \(Q\) supplies neither a lower bound \(Q>5q\) infinitely often nor balanced-state frequency. The finite certificate at current \(53/84\), proving that any rational \(Z\) or \(c\) has reduced denominator exceeding \(2^{56}\), remains unchanged. ([Scalar arithmetic and finite certificate](<../signed-arithmetic-returns/REPORT.md>), [audited conditional theorem](<fixed_logs_audit.md>))

**Shifting responses exposes the arithmetic still needed at the boundary.** For a bounded integer array \(f\), let \(W(f)=\sum_{a\ge0,b\ge4}f(a,b)2^{-a}3^{-b}\) and \(S_a^uS_b^vf(a,b)=f(a+u,b+v)\). If \(C_u\) is its weighted sum over the complete strip \(a<u\), \(R_v\) the weighted sum over \(4\le b<4+v\), and \(K_{u,v}\) the weighted sum over their finite intersection, absolute convergence and reindexing give
\[
W(S_a^uS_b^vf)=2^u3^v\bigl(W(f)-C_u(f)-R_v(f)+K_{u,v}(f)\bigr).
\tag{6}
\]
For a finite rational polynomial \(P=\sum\lambda_{u,v}X^uY^v\), the complete dictionary has bulk term \(P(2,3)W(f)\), vertical-profile coefficients \(-2^{-i}\sum_{u>i,v}\lambda_{u,v}2^u3^v\), horizontal-profile coefficients \(-3^{-(4+j)}\sum_{u,v>j}\lambda_{u,v}2^u3^v\), and a finite rational corner sum. Thus \(P(2,3)=0\) removes the bulk without evaluating the surviving profiles. Returning to the full \(Z\) or \(G_R\) also retains their four low rows, each infinite horizontally. Only the corner is automatically rational. ([Complete formulas WC1–WC3](<weighted_closure.md>), [independent boundary reconstruction](<weighted_audit.md>))

Two exact determinants exclude short everywhere-pointwise identities involving the target array and the four response arrays. The constant plus all shifts \(0\le u,v\le3\) has rank **81**; the constant plus color-preserving shifts \(u,v\in\{0,3,6\}\) has rank **46**. An independent implementation rebuilt the actual entries from colored boards and minimum differences and reproduced both determinants. These certificates exclude precisely those finite classes of constant-coefficient identities on the entire high-row domain. They do not prove independence of weighted values, exclude eventual identities, or prohibit a value-specific cancellation of the infinite profiles. No arithmetic closure was found. ([Rank certificates and scope](<weighted_audit.md>))

**Two same-state returns can eliminate \(G_R\), but their integer price is explicit.** Write their expansions as \(Z-z_i=d_iG_R+\rho_i\), where
\[
d_i=\sigma_i\Delta_i=\frac{A_i}{K_i},\qquad
A_i=\sigma_i(3^{r_i}-2^{s_i}),\qquad K_i=2^{s_i}3^{r_i}.
\]
The side signs are essential: \(\Delta_i\) alone is not the shared-response coefficient. For later indices \(n<m\), both coordinates increase, \(K_n\mid K_m\), and the \(A_i\) are coprime to six. With \(g=\gcd(|A_n|,|A_m|)\), the primitive integer eliminator is
\[
\lambda=A_m/g,\qquad \mu=-A_nK_m/(gK_n),
\]
\[
(\lambda+\mu)Z-(\lambda z_n+\mu z_m)=\lambda\rho_n+\mu\rho_m.
\tag{7}
\]
For \(t=|s_nr_m-s_mr_n|>0\), modular elimination gives \(g\mid\gcd(2^t-1,3^t-1)\); in particular \(t=1,2,3\) forces \(g=1\). This cancels the fixed real response without assuming it rational. ([Primitive arithmetic and independent proof](<paired_audit.md>))

Further affine reduction is a separate calculation. Put \(\ell=\operatorname{lcm}(\operatorname{den}z_n,\operatorname{den}z_m)\), \(M_i=\ell z_i\), \(k=\lambda+\mu\), and \(J=\lambda M_n+\mu M_m\). When \(k\ne0\), the affine prediction \(z_*=J/(k\ell)\) has exact reduced denominator and cleared error
\[
b_*=\frac{|k|\ell}{\gcd(|J|,|k|\ell)},\qquad
b_*|Z-z_*|=
\frac{\ell}{\gcd(|J|,|k|\ell)}|kZ-J/\ell|.
\tag{8}
\]
The gcd involves complete model numerators; the cross-gap gcd cannot substitute for it. If \(k=0\), the combination eliminates the target and is not an affine approximation. ([Complete normalization formulas CE5–CE7](<cheaper_return.md>), [normalization audit](<paired_audit.md>))

Repeated response states force \(s_m\ge(5/2)s_n\). For adjacent indices, equality of both mediant residues forces the intervening continued-fraction digit to be a positive multiple of three; for nonadjacent indices, the ordinary recurrence gives the bound directly. Combining this spacing with (1) proves that \(|\lambda|2^{-(s_n+q_n)}\) diverges as \(n\to\infty\), uniformly over later same-state partners. Thus the existing separate bounds on \(\rho_n,\rho_m\), inserted into a triangle inequality for (7), do not certify a small primitive residual. This concerns a diverging **upper-bound expression**, not growth of the actual correlated residual. Extra cancellation in that residual or in (8) remains possible. ([Spacing, uniform scale proof and limitations](<paired_audit.md>))

The complete actual pair at current models \(12/19\) and \(306/485\) fails even after affine reduction. Their first mediants \(53/84\) and \(971/1539\) share state \(R_3=(2,0,2+\omega)\), their determinant has magnitude three, and \(g=1\). The primitive coefficients have **1530 and 2986 bits**; \(z_*\) has a **5975-bit reduced denominator**. Independent complete model evaluation and a \(1800\times1200\) actual-target rectangle, with both infinite exterior strips bounded before multiplication by \(|k|\), prove
\[
\boxed{2^{4408}<b_*|Z-z_*|<2^{4409}.}
\]
This is a rigorous failure of that named return, rather than a nominal-denominator calculation or an all-pair impossibility theorem. ([Independent full interval certificate](<paired_audit.md>), [independent exact evaluator](<paired_audit_check.py>))

| Proof obligation | Current progress |
|---|---|
| Density reduction, global finite optimum and exact birth encoding | Complete in the accepted written foundation |
| Complete rational scalar models and integer clearing | Proved |
| Complete jumps, both Farey variations and quantitative approximation error | Proved |
| Uniform correct-side nonvanishing on eligible balanced first mediants | **Now proved**, with no ratio, following-digit or child-sign restriction |
| Actual infinite eligible supply with \(Q-5q\to+\infty\) | **Open** |
| Cheaper arithmetic closure or adequate alternative rational return | Open; the two tested mechanisms do not provide one |
| Actual infinite hierarchy of small real residuals | Already proved |
| Cheap arithmetic for the hierarchy's full boundary, and residual nonvanishing | Separate open obligations |
| Irrationality of the density | Not established |

The hierarchy's proved identity \(81\Pi_mZ=B_m+\mathcal R_m\), with exponentially small actual real residuals, remains distinct from the scalar theorem. Its full \(B_m\) contains infinite boundary and low-row values without sufficiently cheap rational clearing; nonzero \(\mathcal R_m\) infinitely often is also unproved. Scalar nonvanishing does not transfer to these signed residuals. ([Actual infinite real-residual theorem](<../hybrid-arithmetic-closure/REPORT.md>), [complete boundary arithmetic audit](<../signed-arithmetic-returns/hierarchy_boundary_audit.md>))

The present advance removes an analytic obstruction from the scalar finish and leaves its missing infinitude statement sharply defined. A successful next argument must prove that actual favorable states and adequate gaps occur jointly infinitely often, or supply an arithmetic identity controlling complete weighted boundary values or correlated errors at a lower cost. Neither ordinary shifting nor leading-response elimination supplies that theorem by itself. All three supplied and three independent checkers pass, and the written audits find no substantive erratum; these are internal validations of the stated auxiliary results, not an unconditional proof of #168(ii). ([Audited nonvanishing](<fixed_logs_audit.md>), [audited boundaries](<weighted_audit.md>), [audited elimination](<paired_audit.md>))

Skipped: new research or tests for this synthesis, Matveev's full proof, constant optimization, Lean, external review and priority verification. Material risk: uniform nonvanishing on eligible indices does not establish infinitely many adequate eligible returns.
