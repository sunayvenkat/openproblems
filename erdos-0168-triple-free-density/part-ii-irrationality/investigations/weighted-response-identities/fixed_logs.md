# Fixed logarithms remove the dominance restrictions

## Does a primary fixed logarithm theorem give the required uniform bound?

### Takeaway

Yes. Matveev's original Theorem 2.1 gives fixed effective constants \(c>0\) and \(K\ge1\) such that
\[
|m\log2-n\log3|>c\max(1,m,n)^{-K}
\tag{FL1}
\]
for all positive integers \(m,n\). The algebraic numbers and heights are fixed; only the integer coefficients vary. This application uses neither the Kruer–Kohlmeyer seed nor unknown actual response constants. — [Primary English paper, journal page 1219](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3).

### Cited Findings

- E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64:6 (2000), 1217–1269, Theorem 2.1: for integer coefficients and independent fixed logarithms, its notation gives \(\log|\Lambda|>-C(n)C_0W_0D^2\Omega\). The definitions on journal page 1219 are \(\Omega=\prod A_j\), \(W_0=\log(1.5eBD\log(eD))\); (1.3) on page 1218 defines \(B\). The hypotheses include \(A_j\ge\max(Dh(\alpha_j),|\log\alpha_j|)\) and a nonzero last coefficient. — [Full primary text, pages 1218–1219](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=2), [publisher bibliographic record and DOI](https://www.mathnet.ru/eng/im314).
- The accepted scalar proof already provides a complete first-mediant jump and total-variation comparison; no new claim about its combinatorial foundation is needed here. — [Signed scalar proof, SS1–SS5](../signed-arithmetic-returns/signed_scalar.md).

### Inferences

**FL1: exact specialization.** Set the algebraic-number field to \(\mathbb Q\), hence \(D=1\) and \(\kappa=1\). Use \(\alpha_1=2,\alpha_2=3\), their real positive logarithms, and \(A_1=A_2=2\). These height choices satisfy the source hypotheses since \(h(2)=\log2<2\) and \(h(3)=\log3<2\). The two logarithms are independent over \(\mathbb Z\): an integer relation exponentiates to \(2^a3^b=1\), whose valuations force \(a=b=0\). For \(b_1=m,b_2=-n\ne0\), (1.3) gives \(B=\max(1,m,n)\), and \(\Omega=4\). Thus, writing the fixed positive source constant as \(A=4C(2)C_0\),
\[
\log|m\log2-n\log3|>-A\log(1.5eB).
\]
Choose \(K=\max(1,A)\) and \(c=(1.5e)^{-A}\). This proves (FL1), including constant uniformity in \(m,n\). The constant \(C_0\) here depends only on \(n=2,D=1\), not on the integer coefficients. This is an inference directly from the primary theorem above.

This specialization does not use Matveev with a changing number of terms, changing algebraic numbers, or any coefficient \(G_R\). It is the familiar fixed-logarithm integer-coefficient case. Every lower bound below uses this same pair \(2,3\) and the same constants \(c,K\).

### Gaps

- No explicit numerical optimization of the enormous constant \(K\) or the eventual index threshold is attempted. Both are effective from the displayed primary theorem. None of the conclusions below requires a practical threshold.
- Only the statement, definitions and applicability of Matveev's theorem were inspected. Its 53-page proof was not independently reconstructed. This is an established external theorem used as an input, not a new proof of a linear-form estimate.

## Does this force correct-side nonvanishing for every balanced first mediant?

### Takeaway

Yes, eventually and uniformly within the stated state domain. The first mediant's physical gap is at worst polynomially small in the *current* denominator \(q\), whereas the complete remainder has an additional factor \(2^{-q}\). Therefore the prior bounded-ratio, following-digit and two-node sign restrictions are unnecessary for sufficiently late balanced nonresonant first mediants. — [Accepted complete jump and variation criterion](../signed-arithmetic-returns/signed_scalar.md), [primary input for FL1](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3).

### Cited Findings

- Write \(\alpha=\log2/\log3\). For consecutive actual convergents \(p/q,P/Q\), let \(r=p+P,s=q+Q\), \(\sigma=\operatorname{sign}(\alpha-p/q)\), and (E=Z-\widetilde Z^\sigma_{p,q}\). The accepted proof gives
  \[
  |E-\sigma J|\le R,\quad J=\widetilde Z^+_{r,s}-\widetilde Z^-_{r,s},\quad
  R=\mathcal V(p,q;r,s)+\mathcal V(r,s;P,Q).
  \tag{FL2}
  \]
  It includes both entire open Farey child intervals and retains all endpoint conventions. — [SS3–SS4](../signed-arithmetic-returns/signed_scalar.md).
- With \(\omega^2+\omega+1=0\) and \(H(r,s)=\sum_{a=0}^{s-1}\omega^{a+\lfloor ra/s\rfloor}\), the four balanced nonresonant states are
  \[
  \mathcal B=\{(0,1,1),(1,1,1),(2,0,2+\omega),(2,2,2)\}.
  \]
  When \((r\bmod3,s\bmod3,H(r,s))\in\mathcal B\), \(r,s>24\), and the first 23 direct and reciprocal floors match the actual slope, its complete toric quotient satisfies
  \[
  |J|>\frac1{20}|2^{-s}-3^{-r}|.
  \tag{FL3}
  \]
  — [SS1–SS2 and explicit certificate domain](../signed-arithmetic-returns/signed_scalar.md).
- The fixed actual response theorem gives, for the same state (R_0\in\mathcal B\),
  \[
  E=\sigma(2^{-s}-3^{-r})G_{R_0}+O(2^{-(s+q)}),\quad |G_{R_0}|>1/20.
  \tag{FL4}
  \]
  This was previously asserted as an absolute expansion only. — [Complete fixed-response proof, RR7–RR8](../response-closure-tests/response_relations.md).

### Inferences

**FL2: the successor denominator is polynomially bounded.** For every sufficiently late actual convergent, \(0<p<q\), \(Q>q\ge2\), and the standard convergent bound gives
\[
0<|q\log2-p\log3|<\frac{\log3}{Q}.
\]
Apply (FL1), with \(B=q\), to get
\[
Q<C_1q^K,\qquad C_1=\max(1,\log3/c).
\tag{FL5}
\]
Consequently (s=q+Q<C_2q^K\) for \(C_2=1+C_1\). No claim of bounded (Q/q) is made: a polynomial upper bound permits unbounded ratios.

**FL3: the mediant gap is controlled on the earlier scale.** Apply (FL1) again, now to the integer coefficients \(s,-r\). Since \(0<r<s\), its coefficient bound is \(B=s\), and therefore
\[
|\Lambda_m|:=|s\log2-r\log3|>c s^{-K}>c_2q^{-K^2},
\qquad c_2=cC_2^{-K}>0.
\tag{FL6}
\]
The same constants apply; the coefficient pair is different but the logarithms and heights are unchanged. This is precisely the scale conversion missing from the earlier weak seed argument.

Let \(\delta=q\alpha-p\) and \(\delta'=Q\alpha-P\). Their absolute values are below \(1/Q\) for successive convergents, so \(|\Lambda_m|=\log3\,|\delta+\delta'|<2\log3/Q<1\) when (Q\ge3\). The mean-value theorem gives \(|e^x-1|\ge e^{-1}|x|\) for \(|x|\le1\). Hence
\[
|2^{-s}-3^{-r}|
=2^{-s}|1-e^{\Lambda_m}|
>e^{-1}c_2\,2^{-s}q^{-K^2}.
\tag{FL7}
\]
In particular \(-\log|2^s/3^r-1|=O(\log q)=o\(q\)\), with constants independent of the convergent. The statement holds for **every** sufficiently late first mediant, regardless of its balance state. Balance is needed later for the scalar jump bound.

**FL4: a completely uniform variation constant.** The accepted formula, for positive Farey endpoints \(a/b,c/d\), is
\[
\mathcal V=9\left[2^{1-A}\left(1+\frac{A+1}{bd}\right)
+3^{-B}\left(\frac32+\frac{\frac32B+\frac34}{ac}\right)\right],
\quad A=b+d,\ B=a+c.
\]
The two child pairs have \((A,B)=(q+s,p+r)\) and \((s+Q,r+P)\). Their differences (A\alpha-B) are (2\delta+\delta'\) and \(\delta+2\delta'\). Both have absolute value below (3/Q\le1\), so (3^{-B}\le3\,2^{-A}\). For positive integers (a,b,c,d),
\[
1+(A+1)/(bd)\le4,\qquad
\frac32+\frac{\frac32B+\frac34}{ac}\le\frac{21}4.
\]
Thus each variation is at most \((855/4)2^{-A}\). Since \(Q>q\), the complete sum satisfies
\[
R\le\frac{855}{2}2^{-(s+q)}<432\,2^{-(s+q)}.
\tag{FL8}
\]
No estimate discards either infinite side or assumes the following partial quotient is at least two.

**FL5: uniform eventual nonvanishing.** Combining (FL3), (FL7) and (FL8) gives
\[
\frac{R}{|J|}<\frac{8640e}{c_2}\,q^{K^2}2^{-q}\longrightarrow0.
\tag{FL9}
\]
There is a fixed effective \(q_0\) such that, for **every** actual consecutive pair with \(q\ge q_0\), nonresonant current model \(p+q\not\equiv0\pmod3\), and balanced first mediant in \(\mathcal B\), one has
\[
E\ne0,\qquad \operatorname{sign}E=\operatorname{sign}(\sigma J),\qquad
|E|>\frac{c_2}{40e}\,2^{-s}q^{-K^2}.
\tag{FL10}
\]
The last lower bound follows after enlarging \(q_0\) so that \(R<|J|/2\). All rational models lie in ((3/5,2/3)) eventually because the actual slope lies there. The first 23 floors match automatically once \(r,s>24\): every rational breakpoint strictly inside the parent Farey interval has denominator at least (s), and numerator at least (r) for reciprocal floors. The mediant's state must still be verified; neither floor matching nor Matveev proves balance.

**FL6: the response expansion is now relative.** Divide (FL4) by its nonzero leading term, using (FL7) and the uniform (|G_{R_0}|>1/20). This yields
\[
Z-\widetilde Z^\sigma_{p,q}
=\sigma(2^{-s}-3^{-r})G_{R_0}
\left(1+O(q^{K^2}2^{-q})\right).
\tag{FL11}
\]
Its constants are uniform over the finite four-state set. This removes the exceptionally-small-gap caveat for the asymptotic expansion in this domain. It proves no rationality implication for (G_{R_0}).

### Gaps

- The four-state complete jump bounds, the slope pure-jump representation and the finite combinatorial foundation are accepted earlier inputs. This note rechecks their domain and the new comparison, not their entire original proofs.
- The companion exact checker certifies the finite floor/state inputs, complete variation values and conservative constants at three named actual pairs. It cannot verify Matveev's theorem or substitute finite examples for (FL9).

## What remains before this proves irrationality?

### Takeaway

The uniform one-node theorem supersedes the earlier asymptotic dominance case split whenever the first mediant is balanced and nonresonant. The sole remaining supply premise for this particular scalar criterion is an actual infinite sequence of such eligible indices with \(Q-5q\to+\infty\). That premise is still unproved. — [Earlier scalar conditional finish](../signed-arithmetic-returns/signed_scalar.md), [prior two-node theorem and its scope](../response-closure-tests/general_states.md).

### Cited Findings

- The full scalar arithmetic estimate is
  \[
  D_{p,q}\widetilde Z^\sigma_{p,q}\in\mathbb Z,\qquad
  D_{p,q}=27(2^{3q}-1)(3^{3p}-1),
  \]
  \[
  D_{p,q}|Z-\widetilde Z^\sigma_{p,q}|
  \le486(1+o(1))2^{5q-Q}.
  \]
  Its correct domain is a nonresonant current model, with all low rows and boundary terms retained. — [Accepted full arithmetic and error estimate](../signed-arithmetic-returns/REPORT.md).
- The earlier two-node argument handles five same-sign child classes, including four resonant children, and did not settle the eleven opposite-sign classes by that argument. — [Independent state audit](../response-closure-tests/states_audit.md).

### Inferences

**FL7: fully quantified conditional irrationality theorem.** Suppose there exists an unbounded set \(I\) of actual continued-fraction indices of \(\alpha=\log2/\log3\) such that, with \(p/q=p_n/q_n\), \(P/Q=p_{n+1}/q_{n+1}\), and \(r=p+P,s=q+Q\), all of the following hold:

1. \(p+q\not\equiv0\pmod3\);
2. \((r\bmod3,s\bmod3,H(r,s))\in\mathcal B\);
3. (Q-5q\longrightarrow+\infty) as (n\in I\) tends to infinity.

Then (Z\), and hence (c=(Z+6)/9\), is irrational. Indeed, after finitely many indices (FL10) gives nonzero errors, while the displayed arithmetic estimate makes their cleared absolute values tend to zero. If (Z=A/B\) in lowest terms, every
\[
BD_{p,q}(Z-\widetilde Z^\sigma_{p,q})
\]
would be a nonzero integer tending to zero, a contradiction. No bounded-ratio hypothesis, following-digit condition, favorable two-node sign class or independent nonvanishing assumption remains in this conditional theorem.

Within the balanced-first-mediant domain, (FL10) covers all sixteen compatible children, including the eleven previously opposite-sign cases: it never adds the child jump, so opposite signs cannot cause cancellation in its proof. The earlier two-node theorem remains valid and can give better finite or numerical certificates; it is no longer needed to remove asymptotic dominance restrictions in this domain. This does **not** prove a nonvanishing theorem for arbitrary unbalanced first mediants.

The Kruer–Kohlmeyer seed is completely absent from FL1–FL11 and from the conditional theorem's arithmetic implication. Matveev supplies the growth bound and the earlier-scale gap estimate directly. This does not audit or invalidate the seed's other uses elsewhere, and does not replace it with an illicit lower bound involving the real constants \(G_R\).

### Gaps

- No actual infinite state/gap supply theorem is proved here. In particular a polynomial *upper* bound on (Q) provides no *lower* bound \(Q>5q\), and neither theorem supplies infinitely many balanced mediants. The goal remains active and open.
- No cheaper clearing factor, rational relation among actual weighted responses, hierarchy boundary arithmetic, Lean formalization or historical priority check is obtained here.

Skipped: optimizing the logarithmic-form constants and rebuilding the accepted finite foundation. Material risk: treating the uniform nonvanishing theorem as the still-unproved infinite adequate-gap supply theorem.
