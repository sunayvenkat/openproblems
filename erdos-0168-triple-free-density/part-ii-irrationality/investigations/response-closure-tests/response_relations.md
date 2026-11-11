# Fixed actual responses and their remaining ray profiles

## Do four fixed actual response constants exist?

### Takeaway

**Yes, as explicitly defined actual-axis series, independently of any infinite supply assertion.** Whenever balanced rational models approach the actual slope in one of the four states, their complete toric quotients converge to the corresponding constant with a fully charged error bound. This is a finite-four-coefficient analytic reduction; the coefficients are not proved rational or algebraic under target rationality. — [Exact certificate](response_relations_check.py), [accepted paired quotient](../signed-arithmetic-returns/signed_scalar.md).

### Cited Findings

- Write \(\omega^2+\omega+1=0\), \(\alpha=\log_3 2\), and use the actual axes \(A_a,B_b\), the residue correction \(C_{a,b}\), and the actual high-row isolate/patch vector \(E_b\). Their origin conventions are \(A_0=B_0=1\), and \(E_b\) is used only for \(b\ge4\). The finite cover theorem underlying these arrays is an accepted proved input; obsolete conditional wording in the original separation note is superseded. — [Axis definitions and exact separation](../boundary-and-arithmetic/arithmetic.md), [completed finite theorem](../prefix-and-phase-audit/REPORT.md).
- For a reduced nonresonant model \(p/q\), the complete plus/minus difference factors as \((X^q-Y^p)\mathcal Q_{p,q}(X,Y)\). Its coefficients obey \(|Q^{p,q}_{a,b}|\le3(1+b/p)\); for \(b<p\), they are exactly \(c^+_{q+a,b}-c^-_{q+a,b}\). The full exterior outside \(a<A,b<B\), \(B\le p\), is bounded by \((27/2)2^{-A}+(45/2)3^{-B}\). — [SS1–SS4 and endpoint formula SS6](../signed-arithmetic-returns/signed_scalar.md).
- The four balanced states give exact endpoint data, not numerically fitted parameters. — [Endpoint reconstruction and full rational-model comparison](response_relations_check.py).

### Inferences

**RR1. Explicit actual-axis arrays.** Put
\[
P_a^-=\sum_{k=1}^a\omega^{-k},\qquad
S(m)=\sum_{j=0}^m\omega^{2j},
\]
with \(S\) extended three-periodically, so \(S(-1)=0\). The states \(R\), their plus endpoint \(e_R\), and rotation \(\gamma_R\) are

| \((p_0,q_0,H)\), residues modulo three | \(e_R=A_q^+\) | \(\gamma_R=\omega^{2p_0-q_0}\) |
|---|---|---|
| \((0,1,1)\) | \(-\omega\) | \(\omega^2\) |
| \((1,1,1)\) | \(0\) | \(\omega\) |
| \((2,0,2+\omega)\) | \(1\) | \(\omega\) |
| \((2,2,2)\) | \(1\) | \(\omega^2\) |

Define, for every actual index \(a\ge0\),
\[
\mathscr A_R^+(a)
=e_R+\gamma_R(A_a-1)
 +\omega^{-q_0}S(p_0-1)P_a^-,
\qquad
\mathscr A_R^-(a)=\mathscr A_R^+(a)-\gamma_R.
\tag{RR1}
\]
This formula follows from
\(S(p+m)=S(p-1)+\omega^{2p}S(m)\) in the exact shifted-axis sum. Let
\[
z_R^+(a,b)=\mathscr A_R^+(a)+B_b-1+C_{a+q_0,b}
 -\mathbf1_{\{b\ge4\}}E_b,
\quad z_R^-=z_R^+-\gamma_R.
\tag{RR2}
\]
Use the high cone \(F(x+y\omega)=\mathbf1_{\{x\le0,x-y\le0\}}\) for \(b\ge4\). For \(b=0,1,2,3\), respectively use
\[
f_0=0,\quad f_1(x,y)=\mathbf1_{\{x\ge1,y\ge0\}},\quad
f_2(x,y)=\mathbf1_{\{x\le-1,x-y\le0\}},\quad
f_3(x,y)=\mathbf1_{\{y\ge\min(x,0)\}}.
\]
Set \(g_R(a,b)=-3[f_b(z_R^+)-f_b(z_R^-)]\), with \(f_b=F\) in high rows. **There is no exceptional origin birth in these response tests:** their model index is \(q+a>0\), even when the new index \(a=0\). The original target array still retains its exceptional birth at \((0,1)\). Every \(g_R\) is in \(\{-3,0,3\}\), so
\[
G_R=\sum_{a,b\ge0}g_R(a,b)2^{-a}3^{-b}
\tag{RR3}
\]
exists absolutely. It is defined directly from the actual axes, whether or not that rational state occurs infinitely often.

**RR2. Quantified convergence, with no supply assumption hidden.** Suppose a reduced model is in state \(R\), \(A\le q,B\le p\), and its direct floors through \(A-1\) and reciprocal floors through \(B-1\) agree with the actual slope. Then on \(a<A,b<B\), the additional horizontal shifts have no rational tie and the vertical corrections agree. The exact coefficient equality is
\[
Q^{p,q}_{a,b}=g_R(a,b).
\]
The actual response exterior is at most \(9(2^{-A}+3^{-B})\), using \(|g_R|\le3\). Adding this to the model quotient exterior proves
\[
\boxed{|\mathcal Q_{p,q}(1/2,1/3)-G_R|
\le\frac{45}{2}2^{-A}+\frac{63}{2}3^{-B}.}
\tag{RR4}
\]
Hence any state-fixed reduced rational sequence approaching the actual irrational slope with \(p,q\to\infty\) has quotient limit \(G_R\). For every fixed rectangle the floor conditions eventually hold, and RR4 tends to zero after taking successively larger rectangles. **This conclusion is conditional on having such a sequence; it does not establish one.** It also gives the same four complete nonzero enclosures as the previous jump theorem, now for the fixed constants:
\[
G_1\in(9/20,1/2),\quad G_2\in(-3/50,-1/20),\quad
G_3\in(-11/10,-1),\quad G_4\in(7/5,3/2).
\]
The checker reconstructs RR1–RR4 against four full rational quotients at \(5/8,12/19,41/65,53/84\); it does not infer any infinite state frequency. — [Full exact comparison](response_relations_check.py).

### Gaps

- No \(G_R\in\mathbb Q+\mathbb Q Z\) statement, nor algebraicity of \(G_R\), is proved. Four fixed real coefficients are not the fixed rational coefficients required by the arithmetic seed. — [Seed hypotheses](../signed-arithmetic-returns/seed_arithmetic.md).
- State-fixed convergence does not assert that all four states recur infinitely for the actual logarithm. — [Actual versus abstract supply](../boundary-return-mechanisms/cf_return_state.md).

## What actual profiles do the four constants retain?

### Takeaway

The complete response has an explicit low-row boundary-ray part and a strictly negative high-row ray part. Thus the four constants are concrete weighted crossing observables, not automatically evaluations of the original density. — [Ray dictionary and actual witnesses](response_relations_check.py).

### Cited Findings

- The cone and low-row tests above include every equality convention; their directional differences can be computed by subtracting the two integer inequalities. — [Accepted low-row rules](../reflected-return-models/two_sided_models_check.py), [new exact ray verification](response_relations_check.py).
- Earlier generic translated-ray modules were explicitly not proved finite-dimensional. The present reduction concerns only these four special actual-axis arrays. — [Weighted ray limitations](../infinite-return-construction/REPORT.md).

### Inferences

**RR3. Complete ray dictionary.** Write \(z_R^+=x+y\omega\). The following table is an exact identity on **every integer state**, not a sample of the actual orbit:

| Row | \(g_R\) if \(\gamma_R=\omega\) | \(g_R\) if \(\gamma_R=\omega^2\) |
|---|---|---|
| \(b=0\) | \(0\) | \(0\) |
| \(b=1\) | \(-3\mathbf1_{\{x\ge1,y=0\}}\) | \(3\mathbf1_{\{x=0,y\ge-1\}}+3\mathbf1_{\{x\ge1,y=-1\}}\) |
| \(b=2\) | \(-3\mathbf1_{\{x=y\le-1\}}\) | \(-3\mathbf1_{\{x=-1,y\ge-1\}}\) |
| \(b=3\) | \(-3\mathbf1_{\{y=\min(x,0)\}}\) | \(3\mathbf1_{\{x\ge0,y=-1\}}\) |
| \(b\ge4\) | \(-3\mathbf1_{\{x=y\le0\}}\) | \(-3\mathbf1_{\{x=0,y\ge0\}}\) |

For example, in high rows \(F(z)-F(z-\omega)\) is exactly \(\mathbf1_{\{x=y\le0\}}\), while \(F(z)-F(z-\omega^2)\) is \(\mathbf1_{\{x=0,y\ge0\}}\). The other rows follow by the same direct subtraction; the two positive terms in row one have disjoint \(x\)-ranges.

Define \(L_R\) as the weighted contribution of rows one through three and \(T_R\) as the high-row indicator sum from the last row of the table. Then
\[
\boxed{G_R=L_R-3T_R.}\tag{RR5}
\]
Here \(L_R\) is an explicit finite combination of actual one-dimensional binary-weighted boundary-ray series, and \(T_R\) is an actual two-dimensional weighted-ray series. Neither is assumed rational. All four \(T_R\) are strictly positive: indicator witnesses occur at \((4,23),(5,11),(5,4),(4,16)\), respectively, so \(T_R\ge2^{-a}3^{-b}>0\) at the corresponding point. This proves that discarding the high-row profile changes every response value; it does not prove irrationality of that profile. — [Independent original-board/axis witnesses](response_relations_check.py).

**RR4. A narrow actual coefficient obstruction.** At the six actual points
\[
(4,4),(4,16),(4,23),(5,4),(5,6),(5,11),
\]
the rows of \((1,c_{a,b},g_1,g_2,g_3,g_4)\) are
\[
\begin{pmatrix}
1&1&0&0&0&0\\
1&1&0&0&0&-3\\
1&1&-3&0&0&-3\\
1&1&0&0&-3&0\\
1&-2&0&0&0&0\\
1&1&0&-3&0&0
\end{pmatrix}.
\tag{RR6}
\]
Its determinant has magnitude \(3^5=243\). The checker computes the original \(c\) independently from the finite board's original color counts and isolate/patch corrections, rather than identifying it with a response. It follows that no nontrivial rational constant-coefficient **pointwise** identity
\[
\lambda_0+\lambda_Z c_{a,b}+\sum_R\lambda_R g_R(a,b)=0
\]
holds on the whole high-row actual array. In particular these series do not collapse to the original array by a direct same-index affine coefficient identity, even after ignoring rows zero through three.

This is **not** a theorem that the six numerical weighted values are rationally independent. Weighted coboundaries, shifted arrays, boundary series or identities special to evaluation at \((1/2,1/3)\) remain possible. No growing-boundary or localization obstruction from earlier rational models is being silently transferred to these four new actual profiles. — [Six-row exact determinant certificate](response_relations_check.py).

### Gaps

- RR6 rules out only the stated direct pointwise closure. It does not rule out \(G_R\in\mathbb Q+\mathbb Q Z\) through a genuinely new weighted identity.
- The boundary-ray and high-ray values in RR5 have not been evaluated arithmetically. Their explicit appearance is the remaining closure gap, not a proof that closure is impossible.

## Does the fixed-response expansion yield an infinite arithmetic return?

### Takeaway

It gives a new exact finite-four-coefficient analytic form of the signed error, with a uniform fully charged remainder. The same four coefficients can be used at every applicable actual Farey pair. **An arithmetic closure or cheaper clearing theorem is still missing.** — [Prior complete Farey criterion](../signed-arithmetic-returns/signed_scalar.md), [coefficient convergence certificate](response_relations_check.py).

### Cited Findings

- For actual consecutive convergents \(p/q,P/Q\), let \(r=p+P,s=q+Q\), \(\sigma=\operatorname{sign}(\alpha-p/q)\), and suppose the mediant is in one of the four balanced nonresonant rational states. The complete cluster theorem gives \(|(Z-\widetilde Z^\sigma_{p,q})-\sigma J|\le R\), where \(R\) is the sum of the two explicit open-child total-variation bounds. — [SS8–SS10](../signed-arithmetic-returns/signed_scalar.md).
- Farey exclusion implies that this mediant shares all actual direct floors through \(s-1\) and reciprocal floors through \(r-1\). Thus RR4 applies with \(A=s,B=r\), without incorrectly calling the mediant an actual convergent. — [Precise semiconvergent domain](../signed-arithmetic-returns/signed_scalar.md).

### Inferences

**RR5. Four fixed coefficients, with the complete error retained.** Put \(u_{r,s}=2^{-s}-3^{-r}\) and
\[
\varepsilon_{r,s}=\frac{45}{2}2^{-s}+\frac{63}{2}3^{-r}.
\]
Combining the exact paired jump with RR4 and the complete Farey criterion gives
\[
\boxed{\left|(Z-\widetilde Z^\sigma_{p,q})-
\sigma u_{r,s}G_R\right|
\le R+|u_{r,s}|\varepsilon_{r,s}.}\tag{RR7}
\]
Every quantity in the right-hand bound is explicit. No quotient tail, low row or additional rational slope jump has been dropped. Along actual convergents, \(3^{-r}\asymp2^{-s}\), and the prior child bound is \(R=O(2^{-(s+q)})\). The extra response error is \(O(2^{-2s})\). Therefore
\[
\boxed{Z-\widetilde Z^\sigma_{p,q}
=\sigma(2^{-s}-3^{-r})G_R+O(2^{-(s+q)}).}\tag{RR8}
\]
The constants are uniform over the four states. Even if the states vary, the same four fixed real values suffice. None of these statements asserts an infinite supply of applicable mediants.

This removes the model-dependent real quotient from the leading analytic coefficient. It does **not** make the leading coefficient rational under \(Z\in\mathbb Q\), nor remove the original model's period denominator. In particular it is not yet an admissible fixed-rational-coefficient seed form. A repeated-state elimination must also retain both original model numerators/denominators and the small unit gaps. Rational numerical relations, or a new actual weighted symmetry, would have to be proved before using this reduction as an arithmetic finish.

### Gaps

- No actual infinite arithmetic return or irrationality proof is obtained. The original goal remains active.
- Actual value relations, a sufficiently cheap same-family clearing, and any needed infinite state/gap supply remain open. Neither coefficient rank nor the four response enclosures resolves them.
- Skipped: Lean, external review, installations, priority verification and broad scans. Material risk: treating four fixed **real** coefficients as fixed **rational** coefficients, or treating pointwise coefficient rank as numerical value independence.
