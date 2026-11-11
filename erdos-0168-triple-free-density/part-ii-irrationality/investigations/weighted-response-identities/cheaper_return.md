# Repeated responses expose a costly eliminator

No adequate infinite arithmetic return is constructed here. The new results are an exact primitive-coefficient and reduced-denominator formula for two-index response elimination, a theorem explaining why the existing separate remainder bounds do not certify that method, and a complete actual-target counterexample to the most direct same-response extrapolation. These are scoped results about this construction, not a universal return impossibility. — [Exact checker](cheaper_return_check.py), [accepted response expansion](../response-closure-tests/response_relations.md).

## What must a two-index response elimination actually clear?

### Takeaway

The fixed real response can indeed be eliminated without assuming it rational. The resulting affine rational prediction has a separate, exactly identifiable denominator; omitting either that denominator or the physical-gap coefficient denominators gives a false price. — [Exact formulas and finite verification](cheaper_return_check.py).

### Cited Findings

- For an applicable actual convergent indexed by \(i\), with first mediant \(r_i/s_i\), the proved expansion is
  \[
  E_i:=Z-z_i=d_iG_R+\rho_i,\qquad
  d_i=\sigma_i(2^{-s_i}-3^{-r_i}),\qquad
  |\rho_i|\le C2^{-(s_i+q_i)}.
  \tag{CE1}
  \]
  Here \(z_i\) is the complete correct-side rational scalar model, \(q_i\) its current denominator, and the uniform constant \(C\) pays both child variations, the quotient approximation and all low rows. This is not a rationality assertion for \(G_R\). — [RR7–RR8](../response-closure-tests/response_relations.md).
- The complete scalar model is rational with a known integer clearer \(27(2^{3q_i}-1)(3^{3p_i}-1)\). This nominal clearer need not be its reduced denominator. — [Accepted complete model and clearing](../signed-arithmetic-returns/REPORT.md).

### Inferences

Take two indices \(n<m\) in the same response state \(R\), and set
\[
A_i=\sigma_i(3^{r_i}-2^{s_i}),\qquad
K_i=2^{s_i}3^{r_i},\qquad d_i=A_i/K_i.
\]
Both mediant coordinates increase, so \(K_n\mid K_m\). Every \(A_i\) is nonzero and coprime to six. Put \(g=\gcd(|A_n|,|A_m|)\). The primitive integer solution of \(\lambda d_n+\mu d_m=0\) is, up to simultaneous sign,
\[
\boxed{\lambda=A_m/g,\qquad
\mu=-A_nK_m/(gK_n).}
\tag{CE2}
\]
Indeed, after multiplying by \(K_m\), the coefficient pair is \((A_nK_m/K_n,A_m)\), whose gcd is exactly \(g\), since \(A_m\) is coprime to six. Consequently \(\gcd(\lambda,\mu)=1\), and every integer eliminator is a multiple of CE2. Elimination gives the exact actual identity
\[
(\lambda+\mu)Z-(\lambda z_n+\mu z_m)
=\lambda\rho_n+\mu\rho_m.
\tag{CE3}
\]
No arithmetic property of \(G_R\) has been used. — [Integer and rational verification](cheaper_return_check.py).

There is a useful exact cross-gap restriction. If \(D=|s_nr_m-s_mr_n|>0\), then
\[
\boxed{g\mid\gcd(2^D-1,3^D-1).}
\tag{CE4}
\]
Modulo \(g\), both \(2^{s_i}=3^{r_i}\), with two and three invertible. Raising the two equalities to \(r_m,r_n\) and cancelling gives \(2^D=1\); raising to \(s_m,s_n\) gives \(3^D=1\). Negative determinant is handled by inversion. In particular \(D\in\{1,2,3\}\) forces \(g=1\). This bound is independent of model numerator cancellation. — [Exact determinant/gcd assertions](cheaper_return_check.py).

For the actual affine prediction, let \(\ell=\operatorname{lcm}(\operatorname{den}z_n,\operatorname{den}z_m)\), \(M_i=\ell z_i\in\mathbb Z\), \(k=\lambda+\mu\), and \(J=\lambda M_n+\mu M_m\). If \(k\ne0\), the unique affine combination cancelling this response is
\[
z_*=(\lambda z_n+\mu z_m)/k=J/(k\ell),
\]
with **actual reduced denominator**
\[
\boxed{b_*={|k|\ell\over\gcd(|J|,|k|\ell)}.}
\tag{CE5}
\]
Moreover,
\[
\gcd(|k|,|J|)=\gcd(|k|,|M_n-M_m|),
\tag{CE6}
\]
because \(J\equiv\lambda(M_n-M_m)\pmod k\) and \(\gcd(\lambda,k)=1\). The exact fully cleared error is
\[
b_*|Z-z_*|
={\ell\over\gcd(|J|,|k|\ell)}
\left|kZ-J/\ell\right|.
\tag{CE7}
\]
Thus genuine cancellation can still occur, but must be proved for the displayed gcd involving the **complete model numerators**. No gap-numerator gcd or formal pole argument substitutes for this calculation. — [Independent Fraction/gcd checks](cheaper_return_check.py).

### Gaps

CE4 is not a bound on \(\gcd(J,k\ell)\). CE5 leaves open a specially structured infinite sequence with large extra scalar cancellation. If \(k=0\), CE3 eliminates the target itself and gives a relation between the two model constants instead; it is not a rational approximation to \(Z\).

## Why do the available separate remainder bounds fail to certify this method?

### Takeaway

For any pairing of later actual first mediants in the same one of the four response states, even the first term in the primitive integer eliminator's separate-error majorant tends to infinity. This is a theorem about the strength of the existing estimates; it is not a lower bound for the correlated right-hand side of CE3 or an impossibility theorem for the affine prediction. — [CE1 source](../response-closure-tests/response_relations.md), [fixed-logarithm estimates used below](fixed_logs.md).

### Cited Findings

- The new fixed-logarithm specialization gives constants \(c>0,K\ge1\) with \(|s\log2-r\log3|\ge cs^{-K}\) for close integer pairs, and successor denominators obey \(q_{i+1}\le C_1q_i^K\). Its algebraic numbers, heights and term count are fixed. — [Parallel derivation FL1–FL7](fixed_logs.md), [Matveev's primary Theorem 2.1](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3).
- Equality of response state includes equality of both first-mediant residues modulo three, in addition to its transform. — [Four state definitions](../response-closure-tests/response_relations.md).

### Inferences

Write current and successor denominators at \(n\) as \(q,Q\), and preceding denominator as \(h\), so \(Q=aq+h\), \(a\ge1\), and \(s_n=q+Q\). Let \(s_m\) be the later first-mediant denominator.

If \(m=n+1\), write \(q_{n+2}=bQ+q\). The mediant vector difference is \(b(p_{n+1},Q)\). Equal numerator and denominator residues modulo three force \(3\mid b\), because the successor vector is primitive. Thus \(b\ge3\), and
\[
s_m=q+(b+1)Q,\qquad
s_m-2s_n-q=(b-1)Q-2q\ge2(Q-q)\ge2h.
\]
If \(m\ge n+2\), the continued-fraction recurrence gives
\[
s_m\ge2q+3Q,\qquad s_m-2s_n-q\ge Q-q\ge h.
\]
In both cases,
\[
s_m\ge\tfrac52s_n,\qquad
T:=s_m-2s_n-q\ge h.
\tag{CE8}
\]
These inequalities use only equality of the two mediant residue pairs; no favorable sign class is needed.

For sufficiently late first mediants, the fixed-logarithm bound and the mean-value theorem give
\[
|A_m|\ge c_2 2^{s_m}s_m^{-K},\qquad |A_n|\le C_2 2^{s_n}.
\]
Since \(g\le|A_n|\), CE2 gives
\[
\boxed{|\lambda|2^{-(s_n+q)}
\ge c_3 2^T s_m^{-K}.}
\tag{CE9}
\]
The right-hand side tends to infinity for every such pairing as \(n\to\infty\). To see the uniformity, split into two cases. If \(s_m>6s_n\), then \(q<s_n/2\) gives \(T>s_m/2\). Otherwise \(\log s_m=O(\log q)\), since \(s_n=q+Q\le C_3q^K\). Applying the same successor bound to the preceding convergent yields \(h\ge c_4q^{1/K}\); hence \(T\ge h\gg\log s_m\). This proves CE9 diverges in either case. — Derivation from the cited fixed-log theorem and elementary convergent recurrence.

Therefore the bound
\[
|\lambda\rho_n+\mu\rho_m|
\le C\bigl(|\lambda|2^{-(s_n+q_n)}
+|\mu|2^{-(s_m+q_m)}\bigr)
\]
does **not** establish a small primitive integer residual. A successful version must exploit correlated later errors, the exact affine gcd in CE5, or additional identities; cancelling only the common leading \(G_R\) does not provide that information.

### Gaps

The actual two remainders could cancel much more strongly than their separate bounds. Rational affine normalization can also alter the arithmetic price, which is why CE5–CE7 must be used. CE9 alone is not a theorem that every same-state affine extrapolation fails, and does not replace a reduced-denominator calculation.

## Does a complete actual same-response example improve the return?

### Takeaway

No. The natural pair of correct-side models at \(12/19\) and \(306/485\), whose first mediants share response \(R_3\), gives a fully cleared error between \(2^{4408}\) and \(2^{4409}\). This is a complete actual-target certificate, not a nominal-denominator estimate or a general all-pair obstruction. — [Exact checker](cheaper_return_check.py).

### Cited Findings

- The established actual convergents include \(12/19\) with successor \(41/65\), and \(306/485\) with successor \(665/1054\). Their first mediants are \(53/84\) and \(971/1539\). Both are balanced nonresonant state \((2,0,2+\omega)\), with \(G_3\in(-11/10,-1)\). Their correct horizontal sides are minus and plus, respectively. — [Accepted actual certificates](../signed-arithmetic-returns/REPORT.md), [exact state and side reconstruction](cheaper_return_check.py).
- The new checker reconstructs the complete rational models with integer Horner summation, compares that evaluator with the archived complete evaluator at \(5/8,12/19,53/84\), and retains all origin, low-row and isolate/patch conventions. It uses the accepted actual-axis formulas for its target rectangle, not numerical logarithms. — [Checker](cheaper_return_check.py), [archived model evaluator](../reflected-return-models/two_sided_models_check.py).

### Inferences

For these two mediants,
\[
|84\cdot971-1539\cdot53|=3,
\]
so CE4 gives \(g=1\). The primitive coefficient bit lengths are **1530 and 2986**. The actual reduced denominators of the two original models have **108 and 2908 bits**; the affine prediction \(z_*\), after every cancellation in CE5, has a **5975-bit** reduced denominator. — [Exact integer output](cheaper_return_check.py).

The target is enclosed by a complete \(1800\times1200\) rectangle. Its omitted exterior is bounded using \(|c_{a,b}|\le2\) by
\[
|Z-Z_{1800,1200}|
\le6(2^{-1800}+3^{-1200}-2^{-1800}3^{-1200}).
\tag{CE10}
\]
The exceptional original birth at \((0,1)\) is explicitly included by subtracting one after summing the no-origin-exception digit rules. The geometric exterior includes both entire strips and subtracts their intersection once. Multiplying this exact interval by the integer \(k\) and subtracting \(J/\ell\) proves
\[
2^{1419}<|kZ-J/\ell|<2^{1420}.
\]
The fully normalized, fully reduced return consequently satisfies
\[
\boxed{2^{4408}<b_*|Z-z_*|<2^{4409}.}
\tag{CE11}
\]
This rules out adequacy of this actual comparison even after optimal rational affine normalization. It does not assume rational \(Z\). — [Optimizer-free integer/Fraction certificate](cheaper_return_check.py).

The checker passes in approximately 1.3 seconds with the installed Python interpreter and no dependencies. The finite rectangle is used only to enclose this named actual return; the general statements CE2–CE9 are written proofs. — [Checker source and reproducible command](cheaper_return_check.py).

### Gaps

No all-level reduced-denominator lower bound, actual infinite suitable-state supply, or successful cheaper arithmetic return is proved. This branch identifies the exact scalar gcd or correlated-remainder theorem a future two-index construction would need. Skipped: Lean, external review, installations, priority research and broad scans. Material risk: treating a diverging independent-error majorant or one failed actual pair as a universal impossibility theorem.
