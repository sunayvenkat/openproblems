# Independent audit of seed arithmetic

## Does the pinned seed give the stated actual-logarithm budget?

### Takeaway

**PASS.** Proposition 7.4 applies to the fixed mixed form \(2^s/3^r-1\), uniformly over all sufficiently close rational pairs, including mediants. Its convergent corollary is \(\log q_{\mathrm{next}}=o(q)\). It supplies neither a rational boundary nor a nonzero signed return. — [Primary Proposition 7.4, p. 12](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos1062-fork-free-density.pdf#page=12), [clarified source application](seed_arithmetic.md).

### Cited Findings

- An independent GitHub-connector check of the path's latest commit returns 8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23, dated 10 October 2026. Its tree contains the target PDF as blob c2c73046708d64d06456cfe486b1144d6f5f2ec7, size 194024 bytes. This verifies metadata, not a fresh PDF-byte retrieval or publication status. — [Pinned commit](https://github.com/JENW1N/complete-math-solutions/commit/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23), [verified tree](https://api.github.com/repos/JENW1N/complete-math-solutions/git/trees/202a6635c10b6990d9857a682089498016e595d3?recursive=1).
- The cached complete source defines rational projective height by local maximum norms; for a primitive integer vector it equals the largest absolute coordinate. Proposition 7.4 fixes the rational coefficient vector and its length, permits a separate integer \(N\), and bounds a nonzero mixed form below by \(CtH^{-\epsilon}\), with \(t\le\min(1,u_i)\). The preceding one-form theorem and finite-hyperplane induction are present in the cached text. — [Cached source, notation and §§7.1–7.2](<../../../../meta/theorem-transfer-survey/erdos1062-fork-free-density.pdf.txt>).
- The supplied and independent checkers pass under Python 3.14. The independent checker imports no companion code and uses integer coordinates, extended Euclid and literal continued-fraction evaluation. — [Supplied checker](seed_arithmetic_check.py), [independent checker](seed_arithmetic_audit_check.py).

### Inferences

For any positive integers \(r,s\) with \(u=2^s/3^r\in[1/2,2]\), set \(N=1\), \(t=\min(1,u)\). The primitive pair is \((3^r,2^s)\), so
\[
H(1:u)=\max(3^r,2^s)\le2^{s+1},\qquad t\ge1/2.
\]
Prime factorization proves \(u\ne1\). The same fixed coefficient and dimension therefore give
\[
|u-1|\ge C_\epsilon2^{-1-\epsilon}2^{-\epsilon s}.
\]
Since \(|\log u|\ge|u-1|/2\) on this interval,
\[
|s\log2-r\log3|\ge c_\epsilon2^{-\epsilon s},
\qquad c_\epsilon=C_\epsilon2^{-2-\epsilon}>0.
\]
Also
\[
|2^{-s}-3^{-r}|=2^{-s}|1-u|
\ge C_\epsilon2^{-1-\epsilon}2^{-(1+\epsilon)s}.
\]
No convergent hypothesis enters these uniform estimates. — [Uniform close-rational version added to SA1](seed_arithmetic.md).

For a mediant \(r/s=(p+P)/(q+Q)\) of consecutive actual convergents, Farey width gives
\[
|s\alpha-r|<(q+Q)/(qQ)=1/q+1/Q\longrightarrow0.
\]
Its unit ratio therefore eventually belongs to \([1/2,2]\). This is the exact uniformity needed by the signed-cluster proof; replacing \(s\) by an earlier denominator without an additional comparison would not be valid. — [Signed-cluster domain](signed_scalar.md).

For an actual convergent \(p/q\), the additional upper bound
\[
|q\log2-p\log3|<\log3/q_{\mathrm{next}}
\]
implies \(\limsup \log q_{\mathrm{next}}/q\le\epsilon\log2\) for every fixed \(\epsilon>0\), hence the asserted limit. Source constants need not be effective for this qualitative conclusion. Dropping coordinates has the correct projective-height direction in the source induction; eliminating \(N\) invokes the pure-form step already proved at the current dimension. — [Primary proof and SA1](seed_arithmetic.md).

Thus \(S\le Cq_{\mathrm{next}}^A\), with fixed \(A,C\), is subexponential in \(q\). Prime powers with exponent \(q_{\mathrm{next}}\) are not: their logarithm divided by \(q\) is bounded below by a positive constant. Unrestricted growth of the polynomial degree also needs a separate bound. — [SA1 scope](seed_arithmetic.md).

### Gaps

- No PDF binary was retrieved or compared with a local hash. The audit independently checked remote metadata and read the complete cached primary text.
- Neither a rational boundary nor useful-state supply follows from the budget. The original seed obtains sparsity and nonzero errors separately.
- No varying-algebraic-coefficient logarithm theorem or Lean certification is invoked.

## Does the positive-unit family refute a dimension-uniform extension?

### Takeaway

**PASS.** The example has distinct positive units, coefficients one and the separate integer \(N=1\). It satisfies the exact minimum-unit and height conditions, with no vanishing subsum. It refutes a dimension-uniform constant at \(m=O(\log H)\), without contradicting the fixed-dimensional theorem. — [SA2](seed_arithmetic.md), [independent replay](seed_arithmetic_audit_check.py).

### Cited Findings

- For even \(n\ge2\), choose the inverse \(a\) of \(3^n\) modulo \(2^n\), with \(0<a<2^n\), and
  \[
  b=(6^n+1-a3^n)/2^n.
  \]
  Then \(0<b<3^n\), \(a\) is odd and \(b\equiv1\pmod3\). — [SA2 construction](seed_arithmetic.md).
- Independent repeated-division digit extraction and primitive integer-coordinate checks pass for \(n=2,4,8,16,32,64\). Small subset-sum checks use integer sets rather than the supplied checker's mask enumeration. — [Independent certificate](seed_arithmetic_audit_check.py).

### Inferences

Binary digits of \(a/2^n\) and ternary digits of \(b/3^n\) yield at most \(2n\) positive units. A ternary digit two is the single unit \(2\cdot3^{-k}\). Prime factorization proves distinctness between and within the two digit families. All units lie strictly below one, and the last digits supply \(2^{-n}\) and \(3^{-n}\). Every unit is at least \(3^{-n}\). — [SA2](seed_arithmetic.md).

After clearing by \(6^n\), the projective vector contains \(6^n,3^n,2^n\), has content one, and has no larger coordinate. Thus its height is exactly \(6^n\), not an upper bound, and
\[
E=6^{-n},\qquad t=3^{-n}.
\]
A subset summing to one would give
\[
A3^n+B2^n=6^n,\quad0\le A\le a<2^n,\quad0\le B\le b<3^n.
\]
Modulo \(2^n\), \(A=0\); then \(B=3^n\), a contradiction. Positive-only subsums cannot vanish. — [SA2 proof and integer-coordinate check](seed_arithmetic_audit_check.py).

For \(\epsilon=1/4\),
\[
\left(E/(tH^{-1/4})\right)^4=(3/8)^n\longrightarrow0.
\]
No positive constant uniform in dimension can hold on this family. Its coefficient palette is fixed, but its vector length is not. — [Exact fourth-power identity](seed_arithmetic.md).

### Gaps

- No conclusion is drawn for every sparser dimension regime or against valid dimension-dependent estimates.
- The actual hierarchy is not asserted to have this pattern. The example supplies no boundary rationality theorem.

## Does the loop-set measure prove the stated approximation control?

### Takeaway

**PASS.** The separated-loop measure has the claimed interval exponent, and the naive-height algebraic root count yields a summable exceptional set for each degree. Almost every supported slope is transcendental with the stated bounded-degree approximation exponents. This is an abstract existence result. — [SA3](seed_arithmetic.md), [accepted full-state loop audit](<../boundary-return-mechanisms/cf_state_audit.md>).

### Cited Findings

- Literal CF evaluation independently recovers
  \[
  F_A(x)=(x+3)/(3x+10),\qquad F_B(x)=(7x+24)/(9x+31).
  \]
  Both determinants are one. Their derivative bounds are \(1/1600\le F'\le1/100\), and their image gap is exactly \(188/403\). — [Independent branch certificate](seed_arithmetic_audit_check.py).
- The earlier independent audit establishes full-state preservation for every concatenation of \(33\) and \(1323\), after the prefix through \(12/19\). This is a named dependency, not a consequence inferred from the IFS geometry alone. — [CR5 audit](<../boundary-return-mechanisms/cf_state_audit.md>).

### Inferences

Let \(\lambda=1/1600\), \(g=188/403\), \(s=1/11\). Two depth-\(k\) cylinders first differing after \(j\le k-1\) common blocks have separation at least \(g\lambda^j\ge g\lambda^{k-1}\). Give every cylinder mass \(2^{-k}\). If
\[
g\lambda^k<|J|\le g\lambda^{k-1},
\]
the interval meets at most two depth-\(k\) cylinders. Since \(1600<2^{11}\),
\[
\mu(J)\le2^{1-k}\le2\lambda^{ks}<2g^{-s}|J|^s.
\]
Larger intervals require only a changed constant. This proves non-atomicity. The prefix \((5x+12)/(8x+19)\) has absolute derivative at least \(1/729\), so the pushed-forward measure has the same exponent. — [SA3 proof](seed_arithmetic.md).

Fix \(D\) and \(K_D=11(D+2)\). The height here is the maximum absolute coefficient of the primitive minimal polynomial, not rational projective or Weil height. Counting all degree-at-most-\(D\) integer polynomials and at most \(D\) roots each gives \(O_D(T^{D+1})\) algebraic numbers of naive height at most \(T\). On the shell \(2^j\le H_{\rm alg}<2^{j+1}\), the union of approximation balls has measure at most
\[
O_D\!\left(2^{j(D+1)}2^{-jK_D/11}\right)=O_D(2^{-j}).
\]
The union of all shells after \(J\) has measure tending to zero. Therefore almost every supported slope has finitely many exceptions for this \(D\); a countable intersection handles all \(D\). Removing all algebraic points leaves full measure, by non-atomicity. — [SA3 summability argument](seed_arithmetic.md).

For each remaining \(\beta,D\), the finite exceptional distances are positive. Their minimum after multiplying by \(H_{\rm alg}^{K_D}\), capped at one, gives \(c_D(\beta)>0\). Hence
\[
|\beta-\gamma|\ge c_D(\beta)H_{\rm alg}(\gamma)^{-11(D+2)}
\]
for every real algebraic \(\gamma\) of degree at most \(D\). The constant is not effective or explicitly computable. Every supported slope retains the accepted balanced nonresonant state and outgoing ratios below four. — [SA3 conclusion](seed_arithmetic.md).

### Gaps

- This does not place \(\log_3 2\) in the loop set or match every numerical bound specific to that logarithm.
- No actual infinite favorable-state supply or adequate infinite arithmetic return is obtained.
- Skipped Lean, PDF binary retrieval, installations and broader searches. The material risk is treating a budget or an abstract countermodel as the missing actual return.
