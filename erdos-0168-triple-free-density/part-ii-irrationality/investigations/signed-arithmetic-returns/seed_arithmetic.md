# Seed arithmetic and quantitative return limits

## What actual arithmetic budget follows from the pinned seed?

### Takeaway

The seed gives \(\log q_{\rm next}=o(q)\). Thus a clearing factor polynomial in the immediate successor denominator would be cheap enough for the existing hierarchy, if a rational boundary with that clearing factor were constructed. Neither that boundary nor a useful-state supply theorem follows. — [Primary Proposition 7.4](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos1062-fork-free-density.pdf#page=12).

### Cited Findings

- The PDF's latest path commit, checked through the GitHub connector on 7 November 2026, is 8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23, dated 10 October 2026. Its tree records blob c2c73046708d64d06456cfe486b1144d6f5f2ec7, size 194024 bytes. This pins the source, not journal acceptance. — [Commit](https://github.com/JENW1N/complete-math-solutions/commit/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23); [pinned manuscript](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos1062-fork-free-density.pdf).
- Proposition 7.4 bounds a nonzero mixed form with fixed rational coefficient vector and fixed term count by \(CtH^{-\epsilon}\), where \(t\) does not exceed one or any positive unit. The source separately constructs sparse events and a nonzero two-cutoff remainder. — [Primary §§6.4–7.3](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos1062-fork-free-density.pdf#page=10); [complete cached text](<../../../../meta/theorem-transfer-survey/erdos1062-fork-free-density.pdf.txt>).

### Inferences

**SA1. Subexponential immediate-successor growth.** For an actual convergent \(p/q\) to \(\alpha=\log_3 2\), use the mixed form
\[
u=2^q/3^p,\quad E=u-1,\quad N=1,\quad
t=\min(1,u),\quad H(1:u)=\max(2^q,3^p).
\]
The projective height is the maximum, not the product: the primitive pair is \((3^p,2^q)\). Unique factorization gives \(E\ne0\). This uses one fixed coefficient equal to one, so the seed applies directly. — [Primary Proposition 7.4](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos1062-fork-free-density.pdf#page=12).

Along convergents, \(u\to1\). Eventually \(1/2\le u\le2\), \(t\ge1/2\), and \(H\le2^{q+1}\). For each fixed \(\epsilon>0\),
\[
|u-1|\ge C_\epsilon 2^{-1-\epsilon}2^{-\epsilon q}.
\]
The mean-value theorem gives
\[
|q\log2-p\log3|=|\log u|\ge\tfrac12|u-1|
\ge c_\epsilon2^{-\epsilon q},
\quad c_\epsilon=C_\epsilon2^{-2-\epsilon}>0.
\]
The convergent upper bound is
\[
|q\log2-p\log3|<\frac{\log3}{q_{\rm next}}.
\]
Thus
\[
q_{\rm next}<\frac{\log3}{c_\epsilon}2^{\epsilon q}
\quad\text{for every fixed }\epsilon>0,\qquad
\boxed{\log q_{\rm next}=o(q).}
\]
The constants depend on \(\epsilon\), not on the convergent. This is a corollary of the source, not a uniform effective estimate for its constants.

**Uniform close-rational version.** The same argument applies to every positive integer pair \(r,s\) satisfying \(1/2\le2^s/3^r\le2\), without assuming it is a convergent. The coefficient, integer \(N=1\), and dimension stay fixed, while
\[
H(1:2^s/3^r)\le2^{s+1},\qquad t\ge1/2.
\]
Consequently
\[
|s\log2-r\log3|\ge c_\epsilon2^{-\epsilon s},\qquad
|2^{-s}-3^{-r}|\ge C_\epsilon2^{-1-\epsilon}2^{-(1+\epsilon)s}.
\]
This uniform form is the one used at rational mediants in the signed-cluster argument. If \(p/q,P/Q\) are consecutive actual convergents and \(r/s=(p+P)/(q+Q)\), the Farey interval width gives
\[
|s\alpha-r|<(q+Q)/(qQ)=1/q+1/Q\longrightarrow0.
\]
Thus the mediants eventually satisfy the displayed unit-ratio condition. The separate conclusion \(\log q_{\rm next}=o(q)\) additionally uses the convergent approximation bound.

If an actual boundary clearing obeyed \(S\le Cq_{\rm next}^{A}\), for fixed \(A,C\), then \(\log S=o(q)\). In contrast, \(2^{q_{\rm next}}\) has logarithm \(q_{\rm next}\log2\), which is not \(o(q)\) since \(q_{\rm next}>q\). Polynomial dependence on an index and prime-power dependence with that index as exponent have different arithmetic costs. The hierarchy's boundary is still not proved rational. — [Actual hierarchy](<../hybrid-arithmetic-closure/REPORT.md>).

### Gaps

- No polynomial boundary clearing, signed nonvanishing or needed scalar large-gap supply is obtained. — [Current frontier](<../boundary-return-mechanisms/REPORT.md>).
- The complete cached primary text, including §§5–7, was read; remote commit/blob metadata was verified. The PDF binary was not redownloaded byte-for-byte: the raw web fetch returned a cache miss. No fresh Lean or journal certification is claimed.
- No varying-algebraic-coefficient logarithm theorem is invoked. A fully verified primary statement with its parameters was not needed for the results below.

## Can the seed bound have a dimension-uniform constant?

### Takeaway

No. Even with all coefficients one, positive distinct units, the actual minimum-unit scale and no vanishing subsum, \(O(\log H)\) terms permit a mixed form much smaller than \(tH^{-1/4}\). This limits an extension, not the fixed-dimensional seed theorem. — [Exact certificate](<seed_arithmetic_check.py>).

### Cited Findings

- Proposition 7.4 permits positive units and a separate integer \(N\). Their positivity does not prevent cancellation against \(N\). Fixed dimension is part of its quantified data. — [Primary statement](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos1062-fork-free-density.pdf#page=12).
- The following construction is elementary and has a standalone rational-arithmetic certificate. — [Companion checker](<seed_arithmetic_check.py>).

### Inferences

**SA2. A positive, nondegenerate logarithmic-dimension family.** For even \(n\ge2\), choose
\[
1\le a<2^n,\quad a3^n\equiv1\pmod{2^n},\qquad
b=\frac{6^n+1-a3^n}{2^n}.
\]
Then \(1\le b<3^n\), \(a\) is odd, and \(b\equiv1\pmod3\). Expand \(a/2^n\) in binary and \(b/3^n\) in ternary. Encode each nonzero ternary digit \(d\in\{1,2\}\) as the positive unit \(d3^{-k}\), retaining coefficient one. This gives distinct units \(u_i\in(0,1)\), with \(m\le2n\), and
\[
E_n=\sum_{i=1}^m u_i-1=6^{-n},\quad
t_n=\min_i u_i=3^{-n},\quad
H(1:u_1:\cdots:u_m)=6^n.
\]
The endpoint digits ensure that \(2^{-n}\) and \(3^{-n}\) occur. After clearing by \(6^n\), coordinates include \(3^n,2^n\), whose gcd is one; the coordinate of \(1\) is \(6^n\). This proves the claimed projective height and minimum exactly. — [Certificate](<seed_arithmetic_check.py>).

No nonempty subsum of the positive units is zero. Nor does any subset cancel the integer one: such a subset would imply
\[
A3^n+B2^n=6^n,\quad
0\le A\le a<2^n,\quad0\le B\le b<3^n.
\]
Modulo \(2^n\), \(A=0\), then \(B=3^n\), a contradiction. Thus an optional nondegeneracy condition does not remove the example.

For the fixed \(\epsilon=1/4\),
\[
\left(\frac{|E_n|}{t_nH^{-1/4}}\right)^4
=\left(\frac38\right)^n\longrightarrow0.
\]
No dimension-uniform positive constant can therefore work, even for the singleton coefficient palette \(\{1\}\). Here \(m\le(2/\log6)\log H\). This does not address every sparser dimension regime or rule out valid dimension-dependent quantitative estimates. — [Exact fourth-power check](<seed_arithmetic_check.py>).

### Gaps

- The actual hierarchy is not asserted to have this pattern. Its boundary is not thereby rational, and thinning does not turn a dimension-dependent theorem into a uniform one. — [Hierarchy obligations](<../hybrid-arithmetic-closure/REPORT.md>).

## Does finite bounded-degree approximation restore generic state supply?

### Takeaway

No. There exist transcendental slopes in the full balanced-state loop set with finite approximation exponents in every bounded algebraic degree. This strengthens the sparse-loop counterexample: excessive quadratic repetition is unnecessary. It is an existence theorem, not a statement that the actual logarithmic slope belongs to that set. — [Audited loop input](<../boundary-return-mechanisms/cf_state_audit.md>); [new constants](<seed_arithmetic_check.py>).

### Cited Findings

- After the prefix through \(12/19\), arbitrary concatenations of \(A=(3,3)\) and \(B=(1,3,2,3)\) return the full state. Every intermediate abstract critical state is balanced and nonresonant; all outgoing ratios are below four. — [CR5 and independent audit](<../boundary-return-mechanisms/cf_state_audit.md>).
- The new proof uses exact Möbius contractions, a Bernoulli interval bound, integer-polynomial root counting and a summable union bound. It assumes no metric theorem about \(\log_3 2\). — [Matrix and constant certificate](<seed_arithmetic_check.py>).

### Inferences

**SA3. Bad-state slopes with controlled algebraic approximation.** The two block maps on \([0,1]\) are
\[
F_A(x)=\frac{3+x}{10+3x},\quad
F_B(x)=\frac{24+7x}{31+9x}.
\]
Their positive derivatives lie between \(\lambda=1/1600\) and \(1/100\), and their image intervals have gap
\[
g=\frac{24}{31}-\frac4{13}=\frac{188}{403}>0.
\]
Distinct block-depth-\(k\) cylinders have separation at least \(g\lambda^{k-1}\). Give each mass \(2^{-k}\). For an interval \(J\) of length \(\ell\), choose \(k\) with
\(g\lambda^k<\ell\le g\lambda^{k-1}\). It meets at most two level-\(k\) cylinders. Since \(1600<2^{11}\), \(s=1/11\) gives \(2^{-k}\le\lambda^{ks}\), hence
\[
\mu(J)\le2^{1-k}\le2g^{-s}\ell^s.
\]
Increasing the constant handles larger intervals. This also proves there are no atoms. — [Exact branch calculations](<seed_arithmetic_check.py>).

Prepending the fixed prefix \((1,1,1,2,2)\) applies
\[
F_0(x)=\frac{12+5x}{19+8x},\qquad
|F_0'(x)|\ge1/729.
\]
The pushed-forward measure \(\nu\), supported on the audited bad-state slopes, therefore satisfies \(\nu(J)\le C|J|^{1/11}\).

Here the algebraic height \(H_{\rm alg}(\gamma)\) means the maximum absolute coefficient of the primitive irreducible minimal polynomial of \(\gamma\) over \(\mathbb Z\). It is NOT the rational projective height used in SA1–SA2. Fix degree \(D\ge1\) and \(K_D=11(D+2)\). There are at most \(D(2T+1)^{D+1}\) real algebraic numbers of degree at most \(D\) and naive height at most \(T\): count nonzero integer polynomials and at most \(D\) roots each.

In the exact dyadic shell \(2^j\le H_{\rm alg}(\gamma)<2^{j+1}\), the measure of the union of intervals
\[
|\beta-\gamma|<H_{\rm alg}(\gamma)^{-K_D}
\]
is at most
\[
C_D2^{j(D+1)}2^{-jK_D/11}=C_D2^{-j}.
\]
Summing over \(j\) is finite. The measure of the union of all shells \(j\ge J\) tends to zero, so almost every supported slope has only finitely many exceptions. Intersect over all \(D\) and remove the countable algebraic slopes, each of mass zero. A full-measure set of transcendental bad-state slopes remains. For each such \(\beta\) and each \(D\), the finite exceptional set, depending on \(\beta,D\), can be absorbed into a constant \(c_D(\beta)>0\), giving
\[
\boxed{|\beta-\gamma|\ge c_D(\beta)
H_{\rm alg}(\gamma)^{-11(D+2)}}
\]
for every real algebraic \(\gamma\) of degree at most \(D\).

All these slopes still have balanced critical states and outgoing ratios below four. Thus the mere finiteness of every bounded-degree approximation exponent cannot restore the generic escape-or-ratio-\(>5\) inference. No claim compares these constants with every explicit numerical inequality for the actual logarithm, or identifies an explicit computable slope with this property. — [Full-state input](<../boundary-return-mechanisms/cf_return_state.md>).

### Gaps

- The actual slope has not been placed in this Cantor set. The result concerns generic properties, not all consequences of the rational group generated by \(2,3\).
- A logarithm-specific encoding into a fixed-dimensional nonzero \(S\)-unit form could still work. No such encoding, actual signed nonvanishing theorem or rational hierarchy boundary is proved here.
- Skipped Lean, installations and further literature expansion. The material risk is treating an arithmetic budget or an abstract countermodel as a solution of Erdős168.
