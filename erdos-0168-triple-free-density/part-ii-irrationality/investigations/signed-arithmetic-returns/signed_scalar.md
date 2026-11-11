# Complete scalar jumps and a Farey cluster criterion

## Can a complete paired jump be proved nonzero from finitely many states?

### Takeaway

**Yes on the four balanced rational Christoffel states.** A complete infinite toric quotient has a uniform tail bound, so an exact24-by24 certificate proves
\[
|\widetilde Z^+_{p,q}-\widetilde Z^-_{p,q}|
>\frac1{20}|2^{-q}-3^{-p}|.
\]
The domain includes suitable semiconvergents, not only actual convergents. This paired theorem alone does not prove that the correct-side model differs from the target. — [Exact certificate](signed_scalar_check.py), [accepted scalar model](../reflected-return-models/two_sided_models.md).

### Cited Findings

- The accepted scalar model has coefficients \(c^\pm_{a,b}=1-3\widetilde\eta^\pm_{a,b}\in\{1,-2\}\), correct low-row rules and the isolated/patch indicators. Its complete sum clears by \(D=27(2^{3q}-1)(3^{3p}-1)\). It credits model-latest arrivals, not actual maxima. — [Audited definitions and implementation](../reflected-return-models/two_sided_models_check.py), [distinction from actual-max costs](../boundary-return-mechanisms/rational_order.md).
- At a rational grade, the two tie orders have the same counts before and after the grade. Therefore their total number of minimum-count births in that grade is equal. The sole fractional-time token has no birth in the stated slope interval and is retained in the accepted construction. — [Positive rational-order representation](../boundary-return-mechanisms/rational_order.md).
- The four balanced rational triangle states, written as \((p\bmod3,q\bmod3,H(p,q))\), are \((0,1,1),(1,1,1),(2,0,2+\omega),(2,2,2)\). This is a statement about a rational weighted triangle; an arbitrary semiconvergent is not being called an actual balanced reset. — [Complete state table](../boundary-return-mechanisms/cf_return_state.md).

### Inferences

**SS1. Infinite toric quotient, with a uniform coefficient bound.** Put
\[
d_{a,b}=c^+_{a,b}-c^-_{a,b},\qquad
P(X,Y)=\sum_{a,b\ge0}d_{a,b}X^aY^b.
\]
Then \(|d_{a,b}|\le3\), and the sum of the coefficients on every grade \(pa+qb=g\) is zero, by the grade-birth observation above. Define
\[
Q_{a,b}=\sum_{j=1}^{\lfloor b/p\rfloor+1}
d_{a+jq,b-(j-1)p},\qquad
\mathcal Q(X,Y)=\sum_{a,b\ge0}Q_{a,b}X^aY^b.
\tag{SS1}
\]
Direct subtraction gives \(P=(X^q-Y^p)\mathcal Q\). For a coefficient with \(a<q\), the otherwise missing negative-horizontal term is zero because it is the sum along the entire nonnegative grade chain; this is where grade conservation is essential. Moreover
\[
|Q_{a,b}|\le3(1+b/p).
\tag{SS2}
\]
Consequently the quotient converges absolutely at \((1/2,1/3)\), and
\[
\widetilde Z^+_{p,q}-\widetilde Z^-_{p,q}
=(2^{-q}-3^{-p})\mathcal Q(1/2,1/3).
\tag{SS3}
\]
This is an identity for the complete infinite jump, not a truncated numerator or a claim of formal free pole cancellation. For \(b<p\), its low coefficient is simply \(Q_{a,b}=d_{q+a,b}\).

If \(p\ge B\), the omitted quotient weight outside \(a<A,b<B\) is bounded by
\[
\left|\mathcal Q(1/2,1/3)-
\sum_{a<A,b<B}d_{q+a,b}2^{-a}3^{-b}\right|
\le \frac{27}{2}2^{-A}+\frac{45}{2}3^{-B},
\tag{SS4}
\]
provided \(B\le p\). To prove the bound, sum (SS2) over the two exterior strips, overcounting their intersection. The sums are
\(\sum_b(1+b/p)3^{-b}=3/2+3/(4p)\) and
\(\sum_{b\ge B}(1+b/p)3^{-b}=3^{-B}[\tfrac32(1+B/p)+3/(4p)]\).

**SS2. The local response has only four needed states.** Here is the precise domain. Assume \(3/5<p/q<2/3\), \(p,q>24\), \(p+q\not\equiv0\pmod3\), one of the four rational balance states above, and
\[
\lfloor n p/q\rfloor=\lfloor n\alpha\rfloor,
\qquad
\lfloor n q/p\rfloor=\lfloor n/\alpha\rfloor
\quad(1\le n\le23),\qquad \alpha=\log_3 2.
\tag{SS5}
\]
These hypotheses hold at sufficiently late balanced actual convergents. More generally they hold for a first mediant satisfying the stated rational balance condition, as proved below.

Let \(H=\sum_{a=0}^{q-1}\omega^{a+\lfloor pa/q\rfloor}\), \(E_q=\sum_{a=1}^q\omega^{-a}\), and \(\gamma=\omega^{2p-q}\). Summing the horizontal-axis increments gives the exact endpoints
\[
A_q^+=1+\frac{E_q-\omega^2\overline{H-1+\omega^{p+q}}}{1-\omega^2},
\qquad A_q^-=A_q^+-\gamma.
\tag{SS6}
\]
For \(0\le r<24\), the additional common increment is
\[
A_{q+r}^\pm-A_q^\pm
=\sum_{k=1}^r\omega^{-q-k}
S\bigl(p+\lfloor k\alpha\rfloor\bigr),
\qquad S(m)=\sum_{j=0}^m\omega^{2j}.
\]
The short vertical axis, low-row rules and patch tests also use only the floors in (SS5). Thus the entire24-by24 quotient rectangle depends only on the listed finite Eisenstein state and fixed actual short prefixes. No growing rational-grade profile is discarded: its contribution is bounded by (SS4).

The checker evaluates every rational rectangle exactly and includes its complete exterior. The resulting enclosures for the full quotient are

| Rational balance state \((p\bmod3,q\bmod3,H)\) | Complete quotient enclosure |
|---|---|
| \((0,1,1)\) | \((9/20,1/2)\) |
| \((1,1,1)\) | \((-3/50,-1/20)\) |
| \((2,0,2+\omega)\) | \((-11/10,-1)\) |
| \((2,2,2)\) | \((7/5,3/2)\) |

In particular \(|\mathcal Q|>1/20\), proving the stated paired-jump lower bound. The finite rectangle's values are rational, but the complete quotient is not being asserted to be a fixed rational coefficient. The seed theorem is applied later only to a single rational unit gap. — [Exact endpoints, all four rational enclosures and complete paired-value checks](signed_scalar_check.py).

### Gaps

- Paired nonvanishing does not by itself show \(Z\ne\widetilde Z^\sigma_{p,q}\); the opposite model could differ while the correct one equals \(Z\). The next section supplies a complete cluster estimate instead. — [Correct-side limitation](../hybrid-arithmetic-closure/final_hybrid_audit.md).
- The hypothesis (SS5) and the balanced rational state are explicit. No claim covers arbitrary unrelated rational slopes or all unbounded Eisenstein states. — [Certificate domain](signed_scalar_check.py).

## Can the first mediant prove correct-side nonvanishing?

### Takeaway

**Yes when an explicit leading-jump bound exceeds the complete variation in the two Farey children.** This establishes the correct error itself, with every later jump included. It yields a conditional infinite nonvanishing theorem and targeted exact certificates at \(12/19,53/84,306/485\). — [Full cluster certificate](signed_scalar_check.py).

### Cited Findings

- For irrational slope \(\beta\in(3/5,2/3)\), the scalar coefficient at \((a,b)\) depends only on the floors \(\lfloor n\beta\rfloor\), \(n\le a\), and \(\lfloor n/\beta\rfloor\), \(n\le b\). The patch tests use indices \(b,b-1,b-3\), so introduce no larger floor index. The coefficient changes by at most three at any breakpoint. — [Exact coefficient construction](../infinite-return-construction/REPORT.md), [audited implementation](../reflected-return-models/two_sided_models_check.py).
- The actual target is the value at \(\beta=\alpha\); the rational plus/minus models are the corresponding one-sided slope limits. The origin exception is constant and retained. — [Model definition and endpoint conventions](../reflected-return-models/two_sided_models.md).

### Inferences

**SS3. An explicit total-variation bound.** Write \(\mathscr Z(\beta)\) for that slope-dependent scalar sum, still evaluated at fixed weights \(2^{-a}3^{-b}\). A breakpoint of \(\lfloor n\beta\rfloor\) can affect only \(a\ge n\), so its total possible weighted variation is at most \(9\,2^{-n}\). A breakpoint of \(\lfloor n/\beta\rfloor\) similarly costs at most \(9\,3^{-n}\). Summing these bounds over all floor breaks converges. Hence \(\mathscr Z\) has bounded variation with purely atomic derivative: it is a sum of its rational jumps, without a hidden continuous variation term.

For an **open Farey interval** with positive endpoints \(a/b,c/d\), \(|ad-bc|=1\), put \(A=b+d,B=a+c\). There are no direct floor breaks of index below \(A\), nor reciprocal breaks of index below \(B\). At index \(n\), the numbers of possible breaks are at most \(n/(bd)+1\) and \(n/(ac)+1\). Therefore
\[
\operatorname{Var}_{(a/b,c/d)}\mathscr Z\le\mathcal V(a,b;c,d),
\]
\[
\boxed{\mathcal V=9\left[
2^{1-A}\left(1+\frac{A+1}{bd}\right)
+3^{-B}\left(\frac32+\frac{\tfrac32B+\tfrac34}{ac}\right)
\right].}
\tag{SS7}
\]
This charges every rational slope jump, including simultaneous floor events, and is independent of resonance. It follows by summing \(\sum_{n\ge A}2^{-n}\), \(\sum_{n\ge A}n2^{-n}\) and their ternary analogues. No empirical first-event dominance is assumed.

**SS4. Complete first-mediant criterion.** Let \(p/q,P/Q\) be consecutive actual convergents, with the current \(p/q\) nonresonant, and set
\[
r=p+P,\quad s=q+Q,\quad
J=\widetilde Z^+_{r,s}-\widetilde Z^-_{r,s},
\quad R=\mathcal V(p,q;r,s)+\mathcal V(r,s;P,Q).
\tag{SS8}
\]
The first mediant shares all actual direct floors of index less than \(s\) and reciprocal floors of index less than \(r\): every interior rational in the parent Farey interval has denominator at least \(s\) and numerator at least \(r\). Thus (SS5) is automatic when \(r,s>24\), even if \(r/s\) is only a semiconvergent. Its rational state must still be checked.

The actual slope lies between the successor and this mediant. Indeed it is \((p+tP)/(q+tQ)\) with \(t>1\). With \(\sigma=\operatorname{sign}(\alpha-p/q)\), pure-jump variation therefore gives
\[
\left|(Z-\widetilde Z^\sigma_{p,q})-\sigma J\right|\le R.
\tag{SS9}
\]
If the mediant is balanced and nonresonant, let \(S_{24}\) be its certified quotient rectangle and \(T_{24}\) the tail in (SS4). The **fully explicit criterion**
\[
L:=|2^{-s}-3^{-r}|\bigl(|S_{24}|-T_{24}\bigr)>R
\tag{SS10}
\]
proves \(|Z-\widetilde Z^\sigma_{p,q}|\ge L-R>0\), with sign \(\sigma J\). This conclusion is about the correct model, not merely its opposite-side difference.

At the actual pair \(12/19,41/65\), the mediant is \(53/84\), in state \((2,0,2+\omega)\). The certificate gives \(L/R>34\) and \(Z-\widetilde Z^-_{12,19}>0\). A separate exact160-by110 actual-series enclosure is inside the cluster interval. At \(53/84,306/485\), the mediant \(359/569\) is in state \((2,2,2)\), with \(L/R>9\cdot10^{20}\), and the correct error is negative. At \(306/485,665/1054\), the mediant \(971/1539\) is in state \((2,0,2+\omega)\); (SS10) again holds and the correct error is positive. The last case does not require the successor endpoint to be nonresonant. — [Exact integer powers, quotient states and all child-variation bounds](signed_scalar_check.py).

### Gaps

- The estimates do not assert a universal first-mediant dominance theorem. An exceptionally small mediant gap must be compared on the earlier denominator scale, as in the next section.
- No infinite supply of the balanced nonresonant mediant condition has been proved for the actual logarithmic slope. The state algorithms and abstract avoidance loops do not provide it. — [Actual versus abstract state scope](../boundary-return-mechanisms/cf_return_state.md).

## What infinite supply would now complete the signed scalar route?

### Takeaway

The argument closes nonvanishing under a precise leading-gap/state condition. **It does not prove the required actual infinite supply.** A targeted finite corollary excludes rational target denominators at most \(2^{56}\), without claiming irrationality or a best numerical exclusion. — [Exact cleared-error bound](signed_scalar_check.py), [seed normalization](seed_arithmetic.md).

### Cited Findings

- The checked seed consequence is \(\log q_{n+1}=o(q_n)\); its fixed mixed-form lower bound applies to a nonzero rational unit gap with coefficients \(1,-1\). It does not require or provide nonvanishing of a general scalar residual. — [Source-first seed analysis](seed_arithmetic.md).
- The accepted scalar estimate is
\[
D_{p,q}|Z-\widetilde Z^\sigma_{p,q}|
\le486(1+o(1))2^{5q-Q},
\qquad D_{p,q}=27(2^{3q}-1)(3^{3p}-1).
\]
It follows from the complete agreement rectangle \(a<q+Q,b<p+P\). — [Existing scalar theorem](../infinite-return-construction/REPORT.md).

### Inferences

**SS5. Conditional infinite nonvanishing.** Suppose infinitely many actual current convergents have a balanced nonresonant first-mediant state and
\[
-\log\left|2^s/3^r-1\right|=o(q),
\qquad r=p+P,\ s=q+Q.
\tag{SS11}
\]
Then (SS10) holds eventually. Indeed \(R=O(2^{-(s+q)})\), with uniform constants along actual consecutive convergents, while (SS2) gives \(|J|\ge(1/20)2^{-s}|2^s/3^r-1|=2^{-s}\exp(-o(q))\). Their ratio tends to infinity.

There are two useful sufficient conditions for (SS11):

1. **Bounded outgoing ratio:** if \(Q/q\le C\), the seed lower bound at the mediant gives \(-\log|2^s/3^r-1|=o(s)=o(q)\). This keeps the two scales explicit.
2. **Next digit at least two:** if \(a_{n+2}\ge2\), convergent errors \(\delta_n=q_n\alpha-p_n\) satisfy \(|\delta_n|\ge2|\delta_{n+1}|\). Thus
   \[
   |s\alpha-r|=|\delta_n+\delta_{n+1}|
   \ge\tfrac12|\delta_n|>\frac1{2(q+Q)}.
   \]
   The seed consequence \(\log Q=o(q)\) proves (SS11), with no bounded-ratio assumption. All errors tend to zero, so converting between \(s\alpha-r\) and \(2^s/3^r-1\) changes only bounded factors.

If the **same actual infinite sequence** additionally satisfies \(Q-5q\to+\infty\), then the accepted scalar denominator estimate and SS5 give nonzero integer-cleared errors tending to zero. Assuming \(Z=A/B\) would produce nonzero integers \(B D_{p,q}(Z-\widetilde Z^\sigma_{p,q})\) tending to zero, a contradiction. This is a conditional irrationality theorem. Its actual supply premise is unproved; no separate nonvanishing premise is needed once the cluster hypotheses hold.

**SS6. Fully charged finite exclusion at \(53/84\).** The agreement rectangle is \(R_0=569,S_0=359\). Its exterior geometric weight is
\[
3w,\qquad w=2^{-569}+3^{-359}-2^{-569}3^{-359}.
\]
Since coefficient differences have magnitude at most three, retain the full bound \(|Z-\widetilde Z|\le9w\). Exact integer arithmetic checks
\[
0<D_{53,84}(L-R)
\le D_{53,84}|Z-\widetilde Z^-_{53,84}|
\le9D_{53,84}w<2^{-56}.
\tag{SS12}
\]
If \(Z=A/B\) in lowest terms, its nonzero cleared difference is at least \(1/B\); hence \(B>2^{56}\). Since \(Z=9c-6\), a rational \(c\) would also have denominator exceeding \(2^{56}\). This finite exclusion is a corollary of the new cluster argument; the older bespoke saved enclosure can be sharper, and no record bound is asserted. — [Exact bound and independent true-series comparison](signed_scalar_check.py).

### Gaps

- An actual infinite sequence satisfying the mediant-state condition together with \(Q-5q\to\infty\) remains missing. The seed controls sizes of individual gaps and cannot be substituted for their required frequency.
- Correct scalar nonvanishing at three models, or even the finite bound (SS12), does not establish irrationality. No unconditional infinite return or boundary closure of the separate signed hierarchy is claimed.
- Skipped: Lean, external review, installations, historical priority and broad numerical scans. Material risk: confusing the proved complete cluster criterion with the still-unproved actual infinite supply.
