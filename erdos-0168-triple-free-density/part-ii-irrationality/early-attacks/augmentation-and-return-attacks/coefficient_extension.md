# Fixed-term Subspace bounds with variable integer coefficients

Research note, 7 November 2026. This is a derived extension of the finite-S-unit lower-bound argument used in the KK transfer investigation. No priority claim is made. It does not supply the missing sparse return identity for Erdős #269.

## What uniform lower bound is available?

### Takeaway

For a fixed number of summands, bounded non-S factors cost an explicit power of their size. The constant in the lower bound is independent of that size. Consequently, integer coefficients of subexponential size do not by themselves obstruct a Subspace-Theorem contradiction at an exponential return scale.

### Cited Findings

The arithmetic input is the one-form version of the p-adic Subspace Theorem, stated as Theorem 1 of Luca–Ouaknine–Worrell. In the rational specialization, let \(S^*=\{\infty\}\cup S\), let \(L\) be fixed, and let its coefficient at a distinguished index \(k\) be nonzero. For each \(\epsilon>0\), the S-integer vectors satisfying

\[
 |L(\mathbf z)|\prod_{(i,v)\ne(k,\infty)}|z_i|_v
 \le H(\mathbf z)^{-\epsilon},\qquad v\in S^*,
\]

are contained in finitely many proper rational linear subspaces. Each can be enlarged to a rational hyperplane. The theorem applies in dimension at least two. [Primary theorem and height convention](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1).

### Inferences

**Definitions.** Fix a finite set of rational primes \(S\). Write

\[
\mathcal O_S=\mathbb Z[1/p:p\in S],\qquad
A_S(x)=|x|\prod_{p\in S}|x|_p\quad(x\in\mathcal O_S\setminus\{0\}),
\]

with \(|p|_p=p^{-1}\). The number \(A_S(x)\) is the positive integer obtained by removing all S-prime factors from the numerator of \(x\) in lowest terms; in particular, \(A_S(x)\ge1\). Use the projective rational height

\[
H(z_1:\cdots:z_n)=\prod_{v\in M(\mathbb Q)}\max_i |z_i|_v.
\]

It is at least one. Deleting coordinates from a nonzero vector cannot increase this height: at every place the local maximum weakly decreases.

**Theorem P — pure form.** Fix \(m\ge1\), \(d_1,\ldots,d_m\in\mathbb Q\), and \(\epsilon>0\). There is a constant \(C_P>0\), depending only on these data and \(S\), such that for every \(B\ge1\), every nonzero \(x_i\in\mathcal O_S\) with \(A_S(x_i)\le B\), and every

\[
0<t\le\min(1,|x_1|,\ldots,|x_m|),
\]

the nonzero form \(E=\sum_i d_ix_i\) satisfies

\[
\boxed{|E|\ge C_P\,t\,B^{-m}\,H(x_1:\cdots:x_m)^{-\epsilon}.}\tag{P}
\]

**Theorem M — form with an integer term.** For the same fixed data there is \(C_M>0\), independent of \(B,N,\mathbf x,t\), such that for every \(N\in\mathbb Z\), under the preceding assumptions,

\[
E=\sum_i d_ix_i-N\ne0
\quad\Longrightarrow\quad
\boxed{|E|\ge C_M\,t\,B^{-m}\,H(N:x_1:\cdots:x_m)^{-\epsilon}.}\tag{M}
\]

Both statements allow negative \(x_i\) and zero fixed coefficients \(d_i\). Nonvanishing of \(E\) is essential.

### Gaps

The constants obtained from the qualitative Subspace Theorem are not made effective. Neither statement bounds the number of summands when \(m\) grows; all quantifiers keep \(m\) fixed.

## Why do the exceptional hyperplanes preserve the bound?

### Takeaway

Prove all pure dimensions first, then the mixed statement by dimension induction. Elimination leaves the surviving coordinates unchanged, so their non-S factors, absolute-value lower bound, and projective height remain controlled. This avoids an unsupported passage from the original height to the height of a shortened vector.

### Cited Findings

Only the one-form covering theorem stated above is used as an external arithmetic input. The proof below is the present note's derivation, rather than a claim that the source states (P) or (M). [Luca–Ouaknine–Worrell, Theorem 1](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1).

### Inferences

**Proof of (P), by induction on \(m\).** If all \(d_i\) vanish, the nonzero hypothesis has no instances. For \(m=1\) with \(d_1\ne0\),

\[
|d_1x_1|\ge |d_1|t\ge |d_1|t B^{-1}H(x_1)^{-\epsilon},
\]

because the height of a one-coordinate projective vector is one.

Suppose \(m\ge2\), and choose \(k\) with \(d_k\ne0\). For the covering theorem's product,

\[
\Phi_P
=\frac{|E|}{|x_k|}\prod_{i=1}^m A_S(x_i)
\le \frac{|E|}{t}B^m.\tag{1}
\]

Outside the fixed finite union of covering hyperplanes, \(\Phi_P>H(\mathbf x)^{-\epsilon}\). Equation (1) then gives (P) with constant one.

On a covering hyperplane \(\sum_i a_ix_i=0\), choose an index \(\ell\) with \(a_\ell\ne0\). Substitution gives

\[
E=\sum_{i\ne\ell}\left(d_i-d_\ell\frac{a_i}{a_\ell}\right)x_i.
\]

The new rational coefficients are fixed for this hyperplane. The retained coordinates still satisfy \(A_S(x_i)\le B\) and \(|x_i|\ge t\). The dimension-\(m-1\) induction hypothesis gives

\[
|E|\ge C_{\mathcal H}tB^{-(m-1)}
 H((x_i)_{i\ne\ell})^{-\epsilon}
\ge C_{\mathcal H}tB^{-m}H(\mathbf x)^{-\epsilon}.
\]

If the new coefficient vector is zero, this branch has no admissible nonzero \(E\), and needs no constant. The minimum of one and the finitely many nonvacuous branch constants proves (P). This completes the proof for every pure dimension before the mixed induction begins.

**Proof of (M), by induction on \(m\).** In dimension zero, \(E=-N\ne0\) is an integer, so \(|E|\ge1\); the one-coordinate height is one. For \(m\ge1\), the case \(N=0\) follows from (P), since adjoining a zero coordinate leaves the height unchanged.

For \(N\ne0\), apply the covering theorem to the vector \((N,x_1,\ldots,x_m)\), the form \(-N+\sum_i d_ix_i\), and distinguished coordinate \(N\). Integrality of \(N\) gives

\[
\Phi_M=|E|\left(\prod_{p\in S}|N|_p\right)
             \prod_{i=1}^m A_S(x_i)
\le |E|B^m.\tag{2}
\]

Outside the covering hyperplanes, (2) yields

\[
|E|>B^{-m}H(N:\mathbf x)^{-\epsilon}
\ge tB^{-m}H(N:\mathbf x)^{-\epsilon}.
\]

On a covering hyperplane \(a_0N+\sum_i a_ix_i=0\), there are two cases.

* If \(a_0\ne0\), eliminate \(N\). Then
  \(E=\sum_i(d_i+a_i/a_0)x_i\).
  The already proved pure statement in dimension \(m\) applies. Its height \(H(\mathbf x)\) is at most \(H(N:\mathbf x)\), and its B-exponent is exactly \(-m\).
* If \(a_0=0\), choose \(a_\ell\ne0\) and eliminate \(x_\ell\). This leaves the integer term \(-N\) and a fixed-coefficient mixed form in \(m-1\) unchanged coordinates. Apply the mixed induction hypothesis. The B-exponent \(-(m-1)\) and the shortened height give at least the desired lower bound. A hyperplane forcing the sole retained nonzero coordinate to vanish has no admissible vector.

Take the minimum of one, the pure constant for the \(N=0\) case, and the finitely many nonvacuous branch constants. This proves (M), with no dependence of the constant on \(B\). All formulas use absolute values, so signs cause no change. Zero coefficients arising after elimination are explicitly permitted by the induction. \(\square\)

### Gaps

There is no arithmetic gap in this derivation identified in the present review, conditional on the quoted Subspace Theorem. Independent final review remains appropriate before the bound is used in a claimed solution of an open problem.

## What does this permit in a return argument?

### Takeaway

Polynomially growing multiplicities can be absorbed into a fixed number of S-unit endpoint terms. The remaining requirements are a bounded number of grouped terms, controlled height, an exponential saving relative to their common lower scale, and a nonzero remainder.

### Cited Findings

The original application sought a fixed-S-unit lower bound as the arithmetic component of a return argument. The extension here is derived above; it should not be reported as a new theorem found in the literature. The same primary source also treats polynomial factors in its own, more specific transcendence argument, but its hypotheses are not automatically verified for the repeated LCM series. [Luca–Ouaknine–Worrell](https://arxiv.org/html/2412.07908v2).

### Inferences

**Integer-coefficient corollary.** Let \(u_i>0\) be rational S-units, let \(c_i\in\mathbb Z\) with \(|c_i|\le B\), and fix \(d_i\in\mathbb Q\). For \(0<t\le\min(1,u_1,\ldots,u_m)\) and \(N\in\mathbb Z\), there is a constant \(C>0\), independent of \(B,c_i,u_i,N,t\), such that

\[
\sum_i d_ic_iu_i-N\ne0
\quad\Longrightarrow\quad
\boxed{\left|\sum_i d_ic_iu_i-N\right|
\ge Ct B^{-m-\epsilon}H(N:u_1:\cdots:u_m)^{-\epsilon}.}\tag{3}
\]

To prove this first suppose each \(c_i\ne0\), and put \(x_i=c_iu_i\). Then \(A_S(x_i)=A_S(c_i)\le|c_i|\le B\), and \(|x_i|\ge u_i\ge t\). At every nonarchimedean place, multiplication of individual coordinates by integers can only decrease the local maximum. At the real place it increases the maximum by at most \(B\). Therefore

\[
H(N:c_1u_1:\cdots:c_mu_m)\le B H(N:u_1:\cdots:u_m).
\]

Substitute this in (M). If some \(c_i=0\), delete those coordinates and apply the corresponding support's statement; its height and B-loss are no worse than those in (3). There are only finitely many supports, so choose the minimum of their constants. The empty support gives a nonzero integer and is immediate. Negative coefficients cause no change. The pure analogue follows by omitting \(N\).

**Return-scale consequence.** Suppose a fixed \(m\) and fixed \(S,d_i\) give nonzero remainders along an unbounded scale \(L\) with

\[
H(N_L:u_{1,L}:\cdots:u_{m,L})\le e^{C_0L},\qquad
B_L=e^{o(L)},\qquad
0<|E_L|\le t_Le^{-\eta L},
\]

where \(C_0<\infty\), \(\eta>0\), and \(0<t_L\le\min(1,u_{i,L})\). Choose \(\epsilon>0\) with \(C_0\epsilon<\eta\) (any positive \(\epsilon\) works when \(C_0=0\)). Bound (3) gives

\[
|E_L|\ge Ct_L\exp(-C_0\epsilon L-o(L)),
\]

contradicting the upper bound for all sufficiently large \(L\). This includes polynomial \(B_L\). Thus “the coefficients are not from a finite alphabet” is not, by itself, a valid obstruction when the number of endpoint terms is fixed.

**External-height formulation.** Given \(m\ge1\) and a desired exponent \(\epsilon>0\), apply (P) or (M) with exponent \(\epsilon/2\). If

\[
\mathscr H\ge\max(2,H(N:\mathbf x)),\qquad
A_S(x_i)\le\mathscr H^\delta,\qquad
\delta\le\epsilon/(2m),
\]

then \(|E|\ge Ct\mathscr H^{-\epsilon}\). The pure version is identical. The same external height can be retained throughout; no inference about growth of a shortened vector's height is required.

### Gaps

No fixed-term compression, exponential return saving, or nonvanishing statement for the repeated LCM series is established here. A dense collection of boundary terms is not compressed merely by bounding each coefficient polynomially. The functional translation obstruction and exact boundary identities in [lcm.md](<lcm.md>) delimit one possible compression mechanism, but do not rule out all sparse approximate returns.
