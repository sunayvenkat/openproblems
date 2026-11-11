# Independent audit of paired response elimination

## Are the primitive coefficients and complete affine denominator correct?

### Takeaway

**PASS.** CE2–CE7 are correct, including the signed physical gaps, all powers of two and three, and the additional gcd needed after affine normalization. The gap-numerator gcd alone does not control the final reduced denominator. — [Audited derivation](cheaper_return.md), [independent exact evaluator](paired_audit_check.py).

### Cited Findings

- The accepted expansion is \(Z-z_i=d_iG_R+\rho_i\), with \(d_i=\sigma_i(2^{-s_i}-3^{-r_i})\) and a complete remainder bounded by a fixed multiple of \(2^{-(s_i+q_i)}\). Its response constants are actual real weighted profiles; their rationality is not assumed. — [Accepted response expansion, RR7–RR8](../response-closure-tests/response_relations.md).
- Complete rational scalar models retain the exceptional origin digit, all low rows, and both infinite periodic directions. The known scalar clearer is an upper bound for a reduced denominator, not its definition. — [Accepted scalar arithmetic](../signed-arithmetic-returns/REPORT.md), [audited implementation](cheaper_return_check.py).
- Running the supplied checker reproduced its advertised numerical output. The independent checker computes its own axes, digit rules, complete rational model sums and actual-target interval without importing the companion implementation. A separate exact comparison confirmed equality of both independently computed rational model values with the supplied evaluator. — [Independent checker](paired_audit_check.py).

### Inferences

Write
\[
A_i=\sigma_i(3^{r_i}-2^{s_i}),\qquad
K_i=2^{s_i}3^{r_i},\qquad d_i=A_i/K_i.
\]
Positive mediant coordinates imply \(\gcd(A_i,6)=1\), and unique factorization implies \(A_i\ne0\). For later actual first mediants both coordinates increase, so \(K_n\mid K_m\). Multiplying an integer cancellation \(\lambda d_n+\mu d_m=0\) by \(K_m\) yields
\[
\lambda A_n(K_m/K_n)+\mu A_m=0.
\]
Because \(K_m/K_n\) has no prime factors other than two and three, the gcd of these two integer coefficients is exactly
\(g=\gcd(|A_n|,|A_m|)\). Hence every integer eliminator is a multiple of the primitive pair
\[
(\lambda,\mu)=\bigl(A_m/g,-A_nK_m/(gK_n)\bigr).
\]
This proves the primitive claim rather than merely exhibiting one solution. The signs \(\sigma_i\) affect the signs of the coefficients but not their gcd.

Modulo \(g\), both \(2^{s_i}\equiv3^{r_i}\), and two and three are units. Eliminating the powers of three gives
\(2^{s_nr_m-s_mr_n}\equiv1\); eliminating powers of two gives the analogous congruence for three. Negative exponents can be inverted. Thus, for \(D=|s_nr_m-s_mr_n|>0\),
\[
g\mid\gcd(2^D-1,3^D-1).
\]
For \(D=0\) the congruence yields no useful numerical bound; the note correctly states CE4 only when \(D>0\). Actual distinct first mediants are reduced fractions with increasing denominators, so proportional exponent pairs do not arise in the advertised application. For \(D=1,2,3\), the displayed gcd is one.

For the complete model constants, set
\[
\ell=\operatorname{lcm}(\operatorname{den}z_n,\operatorname{den}z_m),\quad
M_i=\ell z_i,\quad k=\lambda+\mu,\quad J=\lambda M_n+\mu M_m.
\]
When \(k\ne0\), the affine prediction is exactly \(z_*=J/(k\ell)\), so elementary fraction reduction gives
\[
b_*:=\operatorname{den}(z_*)=
\frac{|k|\ell}{\gcd(|J|,|k|\ell)}.
\]
Moreover \(J\equiv\lambda(M_n-M_m)\pmod{k}\), and
\(\gcd(\lambda,k)=\gcd(\lambda,\mu)=1\). This proves CE6. The exact identity
\[
b_*|Z-z_*|=
\frac{\ell}{\gcd(|J|,|k|\ell)}
\left|kZ-J/\ell\right|
\]
then proves CE7, including its absolute-value normalization. When \(k=0\), the combination eliminates the target and is not an affine approximation to it. None of these steps assumes \(Z\) or \(G_R\) rational. — [CE2–CE7 under audit](cheaper_return.md), [independent numerical verification](paired_audit_check.py).

### Gaps

The gcd involving \(J\) remains an actual model-numerator question. CE4 does not bound it. No all-pair or all-level reduced-denominator lower bound follows from these formulas. — [Explicit limitations in the source note](cheaper_return.md).

## Is the repeated-state spacing and separate-majorant theorem valid?

### Takeaway

**PASS.** The continued-fraction spacing proof is uniform over later repeated states, including arbitrarily distant pairings. The conclusion concerns a diverging *upper-bound expression*, not a lower bound for the true correlated residual or for the optimally normalized affine error. — [CE8–CE9](cheaper_return.md), [fixed-log input](fixed_logs.md).

### Cited Findings

- Equality of the four response states includes equality of both mediant coordinates modulo three. — [Canonical four-state definitions](../response-closure-tests/response_relations.md).
- The fixed-logarithm input gives \(q_{j+1}\le Cq_j^K\) and \(|s\log2-r\log3|\ge cs^{-K}\) for close positive integer pairs, with fixed \(c,C,K\). Its primary-source application is separately audited in this round; this audit checks the consequences assuming that input. — [Fixed-logarithm derivation](fixed_logs.md).

### Inferences

Let \(h=q_{n-1},q=q_n,Q=q_{n+1}\), so \(Q=aq+h\) with \(a\ge1\), and put \(s_n=q+Q\). If \(m=n+1\), write \(q_{n+2}=bQ+q\). The difference of consecutive first-mediant vectors is \(b(p_{n+1},Q)\). Equal residues of both coordinates force \(3\mid b\), because this successor vector is primitive and therefore is not the zero vector modulo three. Thus \(b\ge3\), and
\[
s_m=q+(b+1)Q,\qquad
s_m-2s_n-q=(b-1)Q-2q\ge2(Q-q)\ge2h.
\]
If \(m\ge n+2\), positivity of every subsequent partial quotient gives
\[
s_m\ge2q+3Q,\qquad s_m-2s_n-q\ge Q-q\ge h.
\]
Since \(Q>q\), both cases give \(s_m\ge(5/2)s_n\), as claimed. The argument needs only equality of residue pairs, not any assertion about the mediant transform or signs.

For sufficiently late first mediants, closeness to the actual slope and the fixed-logarithm estimate give
\[
|A_m|\ge c_2,2^{s_m}s_m^{-K},\qquad |A_n|\le C_2,2^{s_n}.
\]
Since \(g\le|A_n|\), the primitive first coefficient consequently satisfies
\[
|\lambda|2^{-(s_n+q)}\ge c_3,2^T s_m^{-K},
\qquad T=s_m-2s_n-q\ge h.
\]
Uniform divergence requires a scale check, which the source correctly supplies. If \(s_m>6s_n\), then \(q<s_n/2\) yields \(T>s_m/2\), and exponential growth beats \(s_m^K\). Otherwise \(s_m\le6s_n=O(q^K)\), so \(\log s_m=O(\log q)\). Applying the successor bound also to \(h,q\) gives \(h\ge c_4q^{1/K}\), hence \(T-K\log_2s_m\to+\infty\). This proves divergence for every allowed choice of \(m=m(n)>n\).

Accordingly, substituting only the existing independent estimates into
\[
|\lambda\rho_n+\mu\rho_m|
\le C\bigl(|\lambda|2^{-(s_n+q_n)}+|\mu|2^{-(s_m+q_m)}\bigr)
\]
does not yield a small primitive integer residual. The mathematical statement is that this particular right-hand side grows; it does not say the left-hand side grows. — [Source derivation and its scope](cheaper_return.md).

### Gaps

Correlated residual cancellation can be much stronger than this triangle estimate. The factor \(\ell/\gcd(|J|,|k|\ell)\) in the complete affine error can also change the arithmetic scale. Thus the divergence theorem is not an impossibility theorem for all same-state affine returns. — [CE5–CE9 and their explicit caveats](cheaper_return.md).

## Does the fully charged named example survive an independent reconstruction?

### Takeaway

**PASS, with no numerical correction.** The complete actual same-response example has a fully reduced denominator of 5975 bits and cleared error strictly between \(2^{4408}\) and \(2^{4409}\). It fails as an adequate return by a very large margin after every affine cancellation has been paid. — [Independent checker](paired_audit_check.py), [companion checker](cheaper_return_check.py).

### Cited Findings

- The independent checker obtains rigorous rational intervals for \(\log2\) and \(\log3\) from the positive \(\operatorname{atanh}\) series, with explicit geometric tail bounds. Continued-fraction extraction from the quotient interval confirms the actual current/successor pairs \((12/19,41/65)\) and \((306/485,665/1054)\). Integer power comparisons separately confirm their correct signs \(-,+\). — [Independent exact inputs](paired_audit_check.py).
- The mediants \(53/84\) and \(971/1539\) both have canonical state \((2,0,2+\omega)\), as verified by direct finite root-of-unity summation. Their exponent determinant has absolute value three. — [Independent state check](paired_audit_check.py).
- The independently computed complete models agree *exactly* with the companion values, not merely in denominator bit lengths. The evaluator retains all low rows and subtracts the exceptional \((0,1)\) contribution exactly once after periodic summation. — [Independent evaluator](paired_audit_check.py), [source evaluator](cheaper_return_check.py).

### Inferences

The determinant bound forces \(g=1\). Exact arithmetic then gives:

| Quantity | Independently verified result |
|---|---|
| Primitive coefficient bit lengths | 1530 and 2986 |
| Original model reduced-denominator bit lengths | 108 and 2908 |
| Affine prediction reduced-denominator bit length | 5975 |
| Primitive actual residual | \(2^{1419}<|kZ-J/\ell|<2^{1420}\) |
| Fully reduced affine error | \(2^{4408}<b_*|Z-z_*|<2^{4409}\) |

The complete actual-target enclosure uses a \(1800\times1200\) rectangle evaluated with a column-major integer Horner scheme, independently of the companion row-major evaluator. All direct and reciprocal floors are computed by exact integer power comparisons. The exterior bound is
\[
|Z-Z_{1800,1200}|\le
6\bigl(2^{-1800}+3^{-1200}-2^{-1800}3^{-1200}\bigr).
\]
Its constant follows from \(|c_{a,b}|\le2\) and the complete geometric mass of the two omitted strips, with their intersection removed once. Multiplication by \(|k|\) pays the entire exterior before either quoted power-of-two inequality is asserted. Spot checks also reconstruct actual coefficients directly from differences of the finite-board optimum, including the exceptional origin digit. — [Independent full interval certificate](paired_audit_check.py).

Both supplied and independent scripts passed with the installed Python 3.14 interpreter. The independent checker takes approximately six seconds and uses only the standard library. A separate exact equality check of the two complete model evaluators also passed. No solver status, floating-point logarithm, nominal denominator or finite-to-infinite inference is used.

### Gaps

The audit accepts the already-audited finite optimum and exact axis digit formulas as inputs; it does not reconstruct their complete global proof. The Matveev specialization is checked by the parallel fixed-logarithm auditor. No actual infinite suitable-state supply, universal two-index obstruction, correlated-error theorem or cheaper adequate infinite arithmetic return follows here. Skipped: Lean, external review and additional research branches. Material risk: promoting the divergent separate-error bound or the one failed actual pair into a global impossibility statement.
