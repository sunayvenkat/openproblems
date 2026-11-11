# Independent audit of toric normalization and its restricted coefficient cost

7 November 2026. **PASS, within the stated scope.** No mathematical correction to [cheaper_return.md](cheaper_return.md) is required. The finite normalizations and residue certificates check independently, and the fixed-parameter height argument follows from an applicable primary gcd theorem. These results do not construct an adequate infinite return for Erdős #168(ii).

## Does the complete toric quotient have the asserted normalization?

### Takeaway

Yes. The reduced denominators are exactly (D/486) at (5/8), of bit length 44, and (D/1458) at (53/84), of bit length 499. These are named finite calculations. — [Independent checker](cheaper_audit_check.py), [supplied checker](cheaper_return_check.py).

### Cited Findings

With (u=2^q,v=3^p,D=27(u^3-1)(v^3-1)), the independent checker constructs the underlying retimed integer-grade stream, groups simultaneous effective exponents, and sums its exact birth coefficients over the accepted periodic cells. It imports neither the supplied checker nor the archived evaluator. Thus it reconstructs the complete scalar models, including the low rows and origin correction, by a separate route. Their period extension remains an accepted read-only dependency, rather than a new proof of periodicity. — [Independent implementation, `grade_births`](cheaper_audit_check.py), [accepted model definition](../reflected-return-models/two_sided_models.md).

### Inferences

For both named models, exact rational arithmetic verifies that

\[
T=\frac{D(\widehat Z^+-\widehat Z^-)}{u-v}\in\mathbb Z,
\qquad
\mathcal Q=\frac{\widehat Z^+-\widehat Z^-}{u^{-1}-v^{-1}}
=-\frac{uvT}{D}.
\]

Consequently the actual denominator is (D/\gcd(D,uvT)); the independent computation gives the two ratios and bit lengths above. In particular, replacing (u^{-1}-v^{-1}) by (u-v) without the factor (-uv) would be incorrect; the note retains that factor. — [Independent exact normalization](cheaper_audit_check.py).

### Gaps

Neither two values nor the formal poles prove a universal lower bound on later reduced denominators. Additional numerator gcd cancellation on a different subsequence is not excluded. The integrality mechanism for general slopes is accepted from the earlier grade-divisibility proof; the present computation independently checks it only at the two named slopes.

## Does adjoining only the two toric columns evade the existing vertical residue obstruction?

### Takeaway

No. The old four columns and the extended six columns both have rank four at each tested vertical root, for each named slope. The conclusion applies to this explicitly defined module over the localization at (X-Y). — [Independent field-arithmetic checker](cheaper_audit_check.py), [earlier residue theorem](../reflected-return-models/two_sided_models.md).

### Cited Findings

The checker independently reconstructs the axis sums, event corrections and two centered color readouts. It compares the first readout at every high-cell position against the separately constructed token births. It then forms the residue rows at (X=2), (Y=1,\omega), using exact arithmetic in \(\mathbb Q(\omega)\), and checks both old and extended ranks. This verifies the needed nonzero specialization certificates without importing the companion matrix code. — [Independent implementation, `readout`, `field_rank` and `case`](cheaper_audit_check.py).

### Inferences

Order the old columns as (F_{+,0},F_{+,1},F_{-,0},F_{-,1}). Adding (Q_j=(F_{+,j}-F_{-,j})/(X-Y)) makes every six-column combination equal to an old four-column combination with effective coefficients

\[
E_{+,j}=c_{+,j}+d_j/(X-Y),\qquad
E_{-,j}=c_{-,j}-d_j/(X-Y).
\]

At (Y=\zeta\), (X-\zeta) is a nonzero invertible element of the residue field \(\mathbb Q(\omega)(X)\). The rank-four old matrix therefore forces every (E_i(X,\zeta)=0) when the whole vertical residue vanishes. Clearing Laurent monomials and powers of (X-Y) is legitimate, since the vertical prime factors are coprime to (X-Y). Rational conjugation supplies the root \(\omega^2\), so full cancellation of (1-Y^3) requires every (E_i\in(1-Y^3)R). Low-row terms divided by (X-Y) are regular at these generic vertical roots. — [Localized argument in the audited note](cheaper_return.md), [independent column-relation checks](cheaper_audit_check.py).

Over the residue field, the six-column kernel consequently has exactly the two defining quotient directions. The evaluated rank calculation is a certificate for generic full rank, not a claim that one point alone determines every specialized kernel.

### Gaps

This is not a rank theorem for all slopes, a module containing new actual boundary-ray profiles, or a theorem of independence of their real values. Scalar gcd cancellation after evaluation is a separate question.

## Is the Corvaja–Zannier gcd input valid for these pairs?

### Takeaway

Yes. I accessed the primary PDF directly and read its introduction, Corollary 1, Proposition 2 and the proof's closing classification of exceptional curves. No secondary quotation was substituted for the statement. — [Corvaja–Zannier, *A lower bound for the height of a rational function at S-unit points*, arXiv:math/0311030v2, pp. 1–2, 7 and 12–13](https://arxiv.org/pdf/math/0311030v2).

### Cited Findings

Corollary 1 gives the needed gcd bound, with finitely many exceptions for each epsilon, on multiplicatively independent pairs in a fixed finitely generated group. Proposition 2 identifies infinite exceptional families for this specialization as subgroups (U^r=V^s), rather than arbitrary translated cosets; the final paragraph of its proof makes this distinction explicit. The more general results elsewhere in the paper do allow translates. — [Primary Corollary 1 and Proposition 2](https://arxiv.org/pdf/math/0311030v2).

### Inferences

Take (K=\mathbb Q), (S=\{\infty,2,3\}), (U=2^{3q}), (V=3^{3p}). These lie in the fixed group generated by ((2,1),(1,3)). A relation (U^r=V^s) forces (r=s=0) by the valuations at 2 and 3. Hence no exceptional dependence subgroup contains a pair. For this application the all-place negative-log expression is exactly minus the logarithm of the full integer gcd: the archimedean contribution is zero; at 2, (U-1) is a unit; at 3, (V-1) is a unit. Thus the common gcd is coprime to 6 and no unaccounted S-part remains. Since \(\max(\log U,\log V)=3q\log2+o(1)\), the result is

\[
\log\gcd(u^3-1,v^3-1)=o(q).
\]

Even a fixed translated equation (U^rV^s=c) would not cause an infinite exceptional subsequence here: valuations fix (q) when (r\ne0), and fix (p) when (s\ne0), whereas both tend to infinity along the actual convergents. This is an additional check, not a substitute for reading the specialized theorem.

### Gaps

The theorem gives no effective cutoff used in this note. The primary source was accessed through the web tool's parsed PDF; I did not independently reproduce its Subspace Theorem proof or download and hash the binary.

## Are the coefficient denominator and projective-height exponents correct?

### Takeaway

Yes, for fixed integers (a,b) and fixed integer (k\ge0). The denominator formula is exact. The height lower bound is general within this fixed family; its advertised denominator lower bound is asserted on the balanced subfamily (a+b=k). — [Audited derivation](cheaper_return.md), [independent positive and negative monomial checks](cheaper_audit_check.py).

### Cited Findings

The accepted seed normalization has fixed dimension and coefficient, nonzero form (u/v-1), and minimum unit bounded below along convergents. It gives \(\log|u/v-1|\ge-o(q)\). The convergent upper bound and \(p\log3=q\log2+o(1)\) then yield \(\log|u-v|=q\log2-o(q)\). No varying coefficient from the new family is inserted into that seed. — [Read-only seed corollary SA1](../signed-arithmetic-returns/seed_arithmetic.md).

### Inferences

Put (A=u-v), (B=v^3-1). Direct substitution gives

\[
C_{a,b,k}=(-1)^k u^{k-a}v^{k-b-3}B/A^k,
\quad \gcd(A,uv)=1.
\]

The exact denominator is therefore

\[
d_C=\frac{M}{\gcd(M,B)},\qquad
M=u^{[a-k]_+}v^{[b+3-k]_+}|A|^k.
\]

The (v)-factor is coprime to (B). Also

\[
v_2(B)=\begin{cases}1,&p\text{ odd},\\2+v_2(p),&p\text{ even},\end{cases}
\]

so cancellation against the (u)-factor costs only (O(\log p)) in the logarithm. Finally

\[
\gcd(|A|^k,B)\le\gcd(|A|,B)^k
\le\gcd(u^3-1,v^3-1)^k,
\]

where the last divisibility uses (u\equiv v\) modulo any common divisor of (A,B). The preceding gcd theorem and seed scale prove

\[
\log d_C=Lq\log2+o(q),\qquad
L=[a-k]_++[b+3-k]_++k.
\]

As \(\log|C|=(k-a-b)q\log2+o(q)\), the rational projective height has exponent

\[
L+[k-a-b]_+\ge\max(3,k).
\]

For the inequality, put (x=a-k,y=b+3-k); the exponent is (k+x_++y_++[3-k-x-y]_+), which is at least (k), and at least 3 when (k\le3). Under (a+b=k) height and denominator have the same leading exponent. Without such a restriction a denominator bound of 3 is false: (a=0,b=-3,k=0) gives the integer (v^3-1), with denominator one. This example is consistent with the stated height theorem.

The fixed-family lower exponent 3 exceeds \((25+\sqrt5)/10\approx2.7236\), the already proved available supply budget. It therefore does not close that particular interface. — [Read-only supply theorem, equation (8)](../infinite-return-construction/diophantine_supply.md).

### Gaps

All parameters are fixed before taking (q\to\infty); the conclusion is asymptotic and ineffective. Finite denominators can be below the leading-exponent heuristic. A coefficient's cost is not a universal lower bound for a combined return containing additional exact numerator cancellations. Neither global optimality nor impossibility of other response identities follows.

## What was executed and what is the final audit status?

### Takeaway

**PASS.** Both checkers completed successfully with the prescribed Python executable and `-B`. — [Supplied checker](cheaper_return_check.py), [independent checker](cheaper_audit_check.py).

### Cited Findings

The supplied checker passed in about three seconds. The independent checker also passed in about three seconds and reports, for both slopes, exact token-grade scalar reconstruction, denominator ratios 486 and 1458, bit lengths 44 and 499, and vertical ranks ((4,4)). It additionally checks exact denominator reduction on balanced and unbalanced monomials, including negative exponents. — [Executable independent certificate](cheaper_audit_check.py).

### Inferences

No substantive erratum is needed. The source citation can use the directly accessed [primary PDF](https://arxiv.org/pdf/math/0311030v2). The present result is a valid restricted obstruction and a coefficient-price theorem, not a completed proof of #168(ii).

### Gaps

Skipped: Lean, installations, archived edits, broader scans, further cancellation research and external review. The remaining mathematical risk is extending these restricted results to arbitrary actual return identities; that extension is not proved or claimed here.
