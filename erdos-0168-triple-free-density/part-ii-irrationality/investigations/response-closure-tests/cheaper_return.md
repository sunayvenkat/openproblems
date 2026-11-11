# Toric normalization retains the named axis arithmetic

Research note, 7 November 2026. No cheaper infinite return is obtained. Two precise results survive: adjoining the toric-divided readouts does not evade the existing named-model vertical-pole obstruction, and a fixed monomial/toric-power axis-cancelling coefficient has an asymptotic arithmetic price of at least three binary exponent units. These are restricted obstructions, not impossibility theorems for other actual response identities.

## Does dividing by the complete paired jump make the model arithmetically cheap?

### Takeaway

The division is legitimate, including its full low-row corrections, but the resulting rational response still has a 499-bit reduced denominator at 53/84. This is an exact finite calculation, not a lower bound on every later model. — [Exact checker](cheaper_return_check.py).

### Cited Findings

Write

\[
u=2^q,\quad v=3^p,\quad D=27(u^3-1)(v^3-1),\quad
N_\Delta=D(\widehat Z^+_{p,q}-\widehat Z^-_{p,q}).
\]

The complete accepted model has \(N_\Delta\in\mathbb Z\), and grade conservation proves \(u-v\mid N_\Delta\). The archived model evaluator includes the low-row and origin rules. — [Definitions, grade divisibility and old denominator audit](../reflected-return-models/two_sided_models.md), [archived evaluator](../reflected-return-models/two_sided_models_check.py).

### Inferences

Put \(T=N_\Delta/(u-v)\). The complete toric response satisfies the exact identity

\[
\mathcal Q_{p,q}(1/2,1/3)
=\frac{\widehat Z^+_{p,q}-\widehat Z^-_{p,q}}{u^{-1}-v^{-1}}
=-\frac{uvT}{D}.
\tag{CR1}
\]

Consequently its **actual reduced denominator** is

\[
\operatorname{den}\mathcal Q=D/\gcd(D,uvT).
\tag{CR2}
\]

| p/q | D / den(Q) | den(Q) bit length | gcd(abs(u-v), D) |
|---|---:|---:|---:|
|5/8|486|44|13|
|53/84|1458|499|1|

The checker reconstructs both complete models, verifies (CR1), and computes (CR2) with integer gcds. At 53/84 the toric normalization removes only the displayed smooth factor, retaining almost all of the nominal exponent-six denominator. — [Exact reconstruction](cheaper_return_check.py).

### Gaps

No all-level lower bound for the reduced denominator of \(\mathcal Q_{p,q}\) follows. In particular, neither formal poles nor these two gcd calculations rule out a specially engineered scalar cancellation on an infinite subsequence. Rationality of the full quotient also does not make it a fixed coefficient for the seed theorem. — [Seed coefficient and minimum-unit requirements](../signed-arithmetic-returns/seed_arithmetic.md).

## Can adjoining the toric-divided columns cancel an axis pole for free?

### Takeaway

For the named models 5/8 and 53/84, extending the old four-column module by its two toric-divided columns gives no new effective vertical-pole cancellation. This extends the archived Laurent-coefficient statement to localization at \(X-Y\); the underlying rank-four certificate itself is old. — [Old residue proof](../reflected-return-models/two_sided_models.md), [localized exact check](cheaper_return_check.py).

### Cited Findings

Let \(X=x^q,Y=y^p\), and let \(F_{+,0},F_{+,1},F_{-,0},F_{-,1}\) be the four high-column readouts of the archived model. Their vertical residue matrices have rank four over \(\mathbb Q(\omega)(X)\), both at \(Y=1\) and at \(Y=\omega\). Nonzero minors are certified at \(X=2\) for each named model. Low-column terms and finite defects have no vertical pole. — [Archived proof, equation T8](../reflected-return-models/two_sided_models.md), [exact residue reconstruction](cheaper_return_check.py).

### Inferences

Adjoin the explicitly defined readouts

\[
Q_j=(F_{+,j}-F_{-,j})/(X-Y),\qquad j=0,1,
\]

and allow coefficients in

\[
R=\mathbb Q[X^{\pm1},Y^{\pm1},(X-Y)^{-1}].
\]

Every combination of the six columns reduces by these definitions to four effective coefficients \(E_i\in R\). At a vertical root \(Y=\zeta\), the element \(X-\zeta\) is invertible in \(\mathbb Q(\omega)(X)\). Therefore cancellation of the entire vertical pole still forces \(E_i(X,\zeta)=0\) for every \(i\), by the archived full rank. — [Algebra and exact six-column verification](cheaper_return_check.py).

Clear a common power of \(X-Y\) and Laurent monomials. Since neither \(Y-1\) nor \(Y^2+Y+1\) divides \(X-Y\), the respective prime factor must divide every effective numerator. Rational conjugation supplies the \(\omega^2\) root. Thus cancellation of \(1-Y^3\) requires every effective coefficient to lie in \((1-Y^3)R\). The added columns have their defining relations, rather than a new free cancellation direction. Low-row additions divided by \(X-Y\) remain regular at these generic vertical roots, so they do not change the conclusion. — [Preceding rank argument; exact column relations](cheaper_return_check.py).

### Gaps

This is a formal statement for two named finite rational model families. It is not a uniform all-slope rank theorem, a statement about arbitrary affine cone readouts, or a real-value independence statement for the new actual boundary-ray constants. It also does not prohibit extra scalar gcd cancellation after evaluating \(x=1/2,y=1/3\).

## What does a pure axis-factor cancellation cost after monomial normalization?

### Takeaway

Here is a separate, asymptotic **scalar** price for a specific plausible coefficient family. Fix integers \(a,b\), and a fixed integer \(k\ge0\). At convergents to \(\log_3 2\), set \(X=u^{-1},Y=v^{-1}\) and

\[
C_{a,b,k}=X^aY^b\frac{1-Y^3}{(X-Y)^k}.
\tag{CR3}
\]

Its rational projective height satisfies

\[
\log H(C_{a,b,k})\ge\max(3,k)q\log2-o(q).
\tag{CR4}
\]

If \(a+b=k\), so its real magnitude is subexponential on this scale, its **actual reduced denominator** already satisfies the same lower bound. The balanced case therefore cannot reduce this family's asymptotic clearing cost below three. — Proof below, using [Corvaja–Zannier's primary S-unit gcd statement and Corollary 1](https://arxiv.org/html/math/0311030v2), [accepted seed normalization](../signed-arithmetic-returns/seed_arithmetic.md).

### Cited Findings

Corvaja–Zannier's integer S-unit gcd bound has only finitely many exceptions, for each fixed positive epsilon, among multiplicatively independent integer S-unit pairs. Apply it to \((u^3,v^3)=(2^{3q},3^{3p})\). These pairs lie in the fixed S-unit group for \(S=\{\infty,2,3\}\) and are always multiplicatively independent; hence they cannot lie in the exceptional multiplicative-dependence subgroups of Proposition 2. Their common gcd is coprime to 6, so the off-S gcd is exactly the full integer gcd. Thus

\[
\log\gcd(u^3-1,v^3-1)=o(q).
\tag{CR5}
\]

No effective finite cutoff is asserted. — [Primary paper, introduction, Corollary 1 and Proposition 2](https://arxiv.org/html/math/0311030v2).

The audited fixed-coefficient seed applied to \(u/v-1\) gives, for each positive epsilon, a lower bound of order \(2^{-\epsilon q}\) for its absolute value. Since \(p\log3=q\log2+o(1)\), this yields

\[
\log|u-v|=q\log2-o(q).
\tag{CR6}
\]

This retains the minimum-unit scale and uses only the fixed coefficients \(1,-1\), not the varying coefficients in (CR3). — [Seed normalization proof](../signed-arithmetic-returns/seed_arithmetic.md).

### Inferences

Write \(A=u-v\) and \([z]_+=\max(z,0)\). Directly,

\[
C_{a,b,k}=(-1)^k
\frac{u^{k-a}v^{k-b-3}(v^3-1)}{A^k}.
\]

Because \(\gcd(A,uv)=1\), its exact reduced denominator is

\[
\frac{u^{[a-k]_+}v^{[b+3-k]_+}|A|^k}
{\gcd\big(u^{[a-k]_+}v^{[b+3-k]_+}|A|^k,\ v^3-1\big)}.
\tag{CR7}
\]

The \(v\)-part of the gcd is one. The logarithm of its \(u\)-part is \(O(\log p)=o(q)\), since \(v_2(3^{3p}-1)\le2+\log_2p\). Its remaining part is subexponential: for fixed \(k\),

\[
\gcd(|A|^k,v^3-1)
\le\gcd(|A|,v^3-1)^k
\le\gcd(u^3-1,v^3-1)^k.
\]

The last divisibility follows by reducing \(u^3\) modulo any common divisor of \(u-v\) and \(v^3-1\). Using (CR5) and (CR6) in (CR7) proves the exact asymptotic formula

\[
\log\operatorname{den}C_{a,b,k}
=\big([a-k]_++[b+3-k]_++k\big)q\log2-o(q).
\tag{CR8}
\]

Also \(\log|C_{a,b,k}|=(k-a-b)q\log2+o(q)\). For a reduced rational, \(H\) is the maximum of the absolute numerator and positive denominator, so its logarithm is (CR8) plus \([k-a-b]_+q\log2+o(q)\). The resulting coefficient is at least \(k\). For \(k\le3\), use

\[
[x]_++[y]_++[3-k-x-y]_+\ge3-k,
\quad x=a-k,\quad y=b+3-k,
\]

to prove (CR4). If \(a+b=k\), the height and denominator logarithms differ by only \(o(q)\), proving the claimed denominator statement. — [Algebra above; named exact formula checks](cheaper_return_check.py).

At 53/84, the balanced examples \(C_{k,0,k}\), for \(k=0,1,2,3,4\), have denominator bit lengths \(253,244,235,226,301\), while their projective-height bit lengths are \(253,253,253,253,337\). The finite denominators can therefore be smaller than their asymptotic exponent suggests; (CR8) is not an effective finite lower bound. — [Exact integer output](cheaper_return_check.py).

The proved eligible supply guarantees ratios above \(C_*=(15+\sqrt5)/10\) infinitely often, but does not guarantee ratios above two. Its available raw exponent at the lower endpoint is \(1+C_*\approx2.7236\), below three. Thus the balanced coefficient family (CR3) does not close the budget on that supply theorem alone. — [Supply theorem and scope](../infinite-return-construction/diophantine_supply.md).

### Gaps

The integers \(a,b,k\) are fixed throughout the asymptotic theorem; no assertion is made for degrees growing with \(q\). Projective height alone is not a reduced-denominator bound for unbalanced coefficients. No lower bound is asserted for arbitrary combined returns, whose other exact numerators might cancel additional factors. Nor is (CR3) itself a fixed rational coefficient admissible to the seed. This result prices one proposed cancellation architecture; it does not resolve the arithmetic of the actual boundary-ray responses or construct an adequate infinite return.

## What was verified, and what remains?

### Takeaway

The exact checker passes in about three seconds with stdlib rational and integer arithmetic. Its finite certificates support the named calculations; the written proof supplies the fixed-family asymptotic result. Erdős #168(ii) remains open in this branch. — [Checker](cheaper_return_check.py).

### Cited Findings

Command: `python -B research_notes/Erdos 168 response closure tests/cheaper_return_check.py`. The checker reconstructs the archived models read-only, verifies the full toric quotient, tests the reduced-denominator formula on named positive and negative monomial cases, and certifies rank four after the two toric columns are adjoined. — [Checker source](cheaper_return_check.py).

### Inferences

A useful escape would require an additional exact identity involving the actual response family, together with all model numerators, boundary terms, minimum units and nonzero residuals. The finite pole module and coefficient family above do not supply such an identity.

### Gaps

Skipped: Lean, installations, external review, priority research and broad numerical scans. Material risk: extending a named formal module obstruction or a fixed-family coefficient price to all possible scalar returns. No such extension is claimed.
