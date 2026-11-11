# Signed returns isolate Erdős’s remaining supply

**The cheap signed scalar route now has a complete criterion proving its correct-side error nonzero, and an exact return at \(53/84\) excludes rational target denominators through \(2^{56}\).** The argument controls an entire one-sided jump, then bounds every remaining jump in both Farey child intervals. It therefore goes beyond proving that two models differ from each other. Two asymptotic regimes make this nonvanishing criterion effective on a suitable infinite sequence. The missing theorem is the actual infinite supply of convergents satisfying the state and adequate-gap conditions. The separate hierarchy still lacks boundary arithmetic. Three fresh audits pass; Erdős #168(ii) and the active goal remain **open**. ([Scalar audit](<signed_scalar_audit.md>), [boundary audit](<hierarchy_boundary_audit.md>), [seed audit](<seed_arithmetic_audit.md>))

## A complete jump survives its infinite tail

Let \(c\) be the limiting maximum density of sets avoiding \(\{n,2n,3n\}\). The established finite theorem gives birth digits \(\eta_{a,b}\in\{0,1\}\) and
\[
Z=\sum_{a,b\ge0}(1-3\eta_{a,b})2^{-a}3^{-b}=9c-6.
\]
The accepted scalar models \(\widetilde Z^\pm_{p,q}\) use the two one-sided rational slope conventions, retaining all low rows and isolated/patch corrections. For nonresonant \(p+q\not\equiv0\pmod3\), their complete values satisfy
\[
D_{p,q}\widetilde Z^\pm_{p,q}\in\mathbb Z,\qquad
D_{p,q}=27(2^{3q}-1)(3^{3p}-1).
\]
These signed values credit model births; they are not the actual-maximum coupling costs whose crossover denominators were charged in the previous report. ([Accepted target and model distinction](<../boundary-return-mechanisms/REPORT.md>))

Write \(c^\pm_{a,b}=1-3\widetilde\eta^\pm_{a,b}\) and \(d_{a,b}=c^+_{a,b}-c^-_{a,b}\). Complete rational-grade conservation gives zero total difference on every chain \(pa+qb=g\). It supplies the boundary term needed for the infinite factorization
\[
\sum d_{a,b}X^aY^b=(X^q-Y^p)\mathcal Q(X,Y),
\qquad |Q_{a,b}|\le3(1+b/p).
\]
Explicitly,
\[
Q_{a,b}=\sum_{\ell=1}^{\lfloor b/p\rfloor+1}
d_{a+\ell q,b-(\ell-1)p}.
\]
Subtraction recovers the original coefficient when \(a\ge q\). For \(a<q\), the missing horizontal term is replaced by the zero total on the complete nonnegative grade chain. This also handles the singleton chain when \(a<q,b<p\). The factorization has no omitted negative-coordinate remainder, and its summand count gives the stated uniform coefficient bound.
The full paired jump is \((2^{-q}-3^{-p})\mathcal Q(1/2,1/3)\). For \(B\le p\), the omitted quotient outside \(a<A,b<B\) is bounded by
\[
\frac{27}{2}2^{-A}+\frac{45}{2}3^{-B}.
\]
The infinite sides are evaluated by an absolute tail bound; they are not silently discarded. ([Complete quotient and boundary proof, SS1–SS2](<signed_scalar.md>))

With \(\omega^2+\omega+1=0\), define \(H(p,q)=\sum_{a<q}\omega^{a+\lfloor pa/q\rfloor}\). Assume \(3/5<p/q<2/3\), \(p,q>24\), nonresonance, and agreement with \(\alpha=\log_3 2\) on the first 23 direct and reciprocal floors. The balanced rational states give these **complete**, tail-inclusive enclosures:

| \((p\bmod3,q\bmod3,H)\) | \(\mathcal Q(1/2,1/3)\) |
|---|---|
| \((0,1,1)\) | \((9/20,1/2)\) |
| \((1,1,1)\) | \((-3/50,-1/20)\) |
| \((2,0,2+\omega)\) | \((-11/10,-1)\) |
| \((2,2,2)\) | \((7/5,3/2)\) |

Consequently
\[
|\widetilde Z^+_{p,q}-\widetilde Z^-_{p,q}|
>\frac1{20}|2^{-q}-3^{-p}|.
\]
The finite response uses a \(24\times24\) rectangle and the full exterior bound. This domain includes suitable semiconvergents; its state is a rational triangle state, not automatically an actual critical reset. Nor is the full quotient asserted to be a fixed rational coefficient for the seed theorem. **Paired nonvanishing alone still allows the correct model to equal \(Z\).** ([Independent four-state reconstruction](<signed_scalar_audit.md>))

## Both Farey children control the correct error

The scalar sum as a function of slope has purely atomic variation at rational floor breakpoints. A direct floor event of index \(n\) can affect only horizontal indices \(a\ge n\), with total variation at most \(9\,2^{-n}\); a reciprocal event costs at most \(9\,3^{-n}\). Their summed variation converges, leaving no hidden continuous part. On an open Farey interval inside \((3/5,2/3)\), with positive endpoints \(a/b,c/d\) and \(|ad-bc|=1\), let \(A=b+d,B=a+c\). Farey exclusion and geometric summation give
\[
\mathcal V(a,b;c,d)=9\left[
2^{1-A}\left(1+\frac{A+1}{bd}\right)
+3^{-B}\left(\frac32+\frac{\tfrac32B+\tfrac34}{ac}\right)
\right]
\]
as an upper bound for its entire variation, including simultaneous events and all later jumps. ([Total-variation proof, SS3](<signed_scalar.md>))

The constants follow from counting every possible event: no direct breakpoint has index below \(A\), and none of the reciprocal breakpoints has index below \(B\). At index \(n\), their counts are at most \(1+n/(bd)\) and \(1+n/(ac)\). Summing geometric series and their first moments gives the displayed bound. This estimate does not require resonance restrictions and does not guess which later jump is largest.

Take consecutive actual convergents \(p/q,P/Q\), with the current model nonresonant, and put
\[
r=p+P,\quad s=q+Q,\quad
J=\widetilde Z^+_{r,s}-\widetilde Z^-_{r,s},\quad
R=\mathcal V(p,q;r,s)+\mathcal V(r,s;P,Q).
\]
Every interior rational has denominator at least \(s\) and numerator at least \(r\), so the mediant shares the required small floor word when \(r,s>24\). Its rational balance state must still be checked. The actual slope lies beyond that mediant from the current endpoint, giving, for \(\sigma=\operatorname{sign}(\alpha-p/q)\),
\[
\left|(Z-\widetilde Z^\sigma_{p,q})-\sigma J\right|\le R.
\]
The current endpoint jump is excluded by starting on its correct side, the mediant jump is included exactly, and the successor endpoint is not crossed. A certified jump lower bound \(L>R\) therefore proves the **correct-side** error nonzero. ([Complete cluster and endpoint audit](<signed_scalar_audit.md>))

Exact certificates pass for current models \(12/19,53/84,306/485\), with mediants \(53/84,359/569,971/1539\). At \(12/19\), \(L/R>34\); an independent \(160\times110\) true-series enclosure confirms the predicted positive error. At \(53/84\), the ratio exceeds \(9\cdot10^{20}\), and the error is negative. The last model has positive error even though its successor is resonant. These examples establish the criterion's actual use, not its infinite frequency. ([Independent exact certificates](<signed_scalar_audit_check.py>))

For \(53/84\), retain the complete rectangle exterior
\[
w=2^{-569}+3^{-359}-2^{-569}3^{-359},\qquad
D=27(2^{252}-1)(3^{159}-1).
\]
The coefficient difference bound gives \(|Z-\widetilde Z|\le9w\), and exact integer comparisons prove
\[
0<D(L-R)\le|D(Z-\widetilde Z)|\le9Dw<2^{-56}.
\]
If \(Z=A/B\) were rational, \(BD(Z-\widetilde Z)\) would be a nonzero integer, forcing \(B>2^{56}\). Since \(Z=9c-6\), its denominator divides that of rational \(c\), so the same exclusion holds for the density. **This is a finite exclusion, not irrationality or a claimed best numerical bound.** ([Fully charged finite corollary](<signed_scalar_audit.md>))

## The seed makes a precise infinite criterion

Kruer–Kohlmeyer's Proposition 7.4 treats nonzero mixed S-unit forms with fixed rational coefficients and fixed dimension, retaining their minimum-unit scale. Applied to \(u=2^s/3^r\in[1/2,2]\), integer \(N=1\), \(t=\min(1,u)\), and primitive projective height \(\max(2^s,3^r)\), it gives, for every fixed \(\epsilon>0\),
\[
|s\log2-r\log3|\ge c_\epsilon2^{-\epsilon s}.
\]
This is uniform over close rational pairs, including mediants. At actual convergents, comparison with \(\log3/Q\) yields \(\log Q=o(q)\). A fixed-degree polynomial clearing factor in \(Q\) would therefore be affordable; \(2^Q\) would not. ([Pinned primary Proposition 7.4, p. 12](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos1062-fork-free-density.pdf#page=12), [uniform normalization audit](<seed_arithmetic_audit.md>))

For balanced nonresonant mediants, the child remainder is \(R=O(2^{-(s+q)})\), while the jump is at least
\[
\frac1{20}2^{-s}|2^s/3^r-1|.
\]
Thus dominance follows from \(-\log|2^s/3^r-1|=o(q)\). A **fixed bound** \(Q/q\le C\) supplies this through the seed, since \(s=O(q)\). Alternatively, if the following continued-fraction digit \(a_{n+2}\ge2\), opposite convergent errors satisfy
\[
|s\alpha-r|\ge\tfrac12|q\alpha-p|>
\frac1{2(q+Q)}.
\]
Then \(\log Q=o(q)\) supplies the required old-\(q\) scale without a bounded-ratio assumption. An unbounded ratio alone does not permit replacing \(o(s)\) by \(o(q)\). ([Both asymptotic regimes, SS5](<signed_scalar.md>))

The resulting conditional theorem is now complete: suppose an **actual infinite sequence** has nonresonant current models, balanced nonresonant mediants, \(Q-5q\to+\infty\), and one of those dominance regimes. The new argument supplies nonvanishing, while accepted scalar arithmetic gives
\[
0<D_{p,q}|Z-\widetilde Z^\sigma_{p,q}|
\le486(1+o(1))2^{5q-Q}\longrightarrow0.
\]
A hypothetical fixed rational denominator of \(Z\) would convert these into nonzero integers tending to zero. **The actual infinite supply premise remains unproved.** It is no longer necessary to add an independent nonvanishing assumption on such a sequence. ([Conditional finish and precise gap](<signed_scalar_audit.md>))

The primary pin is commit 8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23, with blob c2c73046708d64d06456cfe486b1144d6f5f2ec7 and size 194024 bytes. The complete cached text and remote Git metadata were checked independently; the PDF binary was not retrieved anew. This establishes the input edition, not publication or formal certification. ([Source verification record](<seed_arithmetic_audit.md>))

## Countermodels prevent automatic supply

The fixed-dimensional bound cannot simply receive a dimension-uniform constant. For even \(n\), an explicit Bezout/digit construction gives at most \(2n\) distinct positive units, all with coefficient one, such that
\[
E=\sum u_i-1=6^{-n},\quad
t=\min u_i=3^{-n},\quad H(1:u)=6^n.
\]
No proper subsum vanishes, including cancellation against the integer one. Yet
\[
\left(E/(tH^{-1/4})\right)^4=(3/8)^n\to0.
\]
This refutes the proposed uniform constant already at \(O(\log H)\) terms. It neither contradicts the seed nor excludes every sparser or dimension-dependent extension. ([Construction and independent arithmetic replay](<seed_arithmetic_audit.md>))

Generic algebraic-approximation information also does not supply adequate gaps. The earlier balanced-state loop family \(33,1323\) admits a separated Bernoulli measure with interval mass \(O(|I|^{1/11})\). Counting roots by the **naive height of their primitive minimal polynomial** shows that it contains transcendental slopes with only finitely many degree-at-most-\(D\) approximants closer than \(H^{-11(D+2)}\), simultaneously for every \(D\). This is an existence theorem, not an explicit computable slope. Those abstract slopes still have outgoing ratios below four, so they fail the required adequate-gap hypothesis. They are not the actual logarithmic slope and need not match every numerical logarithm-specific bound. ([Measure, root count and scope](<seed_arithmetic_audit.md>))

The summability is explicit. Degree-at-most-\(D\) algebraic numbers of naive height at most \(T\) number \(O_D(T^{D+1})\). In the shell \(2^j\le H<2^{j+1}\), the approximation intervals therefore have total measure \(O_D(2^{-j})\). Their tail union has measure tending to zero. A countable intersection handles every degree, and non-atomicity removes the algebraic slopes themselves. Finite exceptional approximants depend on the chosen slope and degree; no effective constants for a specified slope are supplied.

## The separate boundary still needs evaluation

The hierarchy cannot inherit the scalar nonvanishing theorem. Its proposed doubling potential exposes an exact cancellation. With \(F_i=\sum_b\eta_{i,b}3^{-b}\), \(G_j=\sum_a\eta_{a,j}2^{-a}\), \(M=\sum\eta_{a,b}2^{-a}3^{-b}\), and
\[
h(t)=\tau(2t)-\tau(t)-\#\{k\ge0:3^{3k+2}\le2t\},
\]
the full Mellin moment \(\int_0^\infty h(t)t^{-2}\,dt\) is \(M-3/13\). Its original-grid jump part is \(M-2F_0\); its fractional-axis part is \(2F_0-3/13\). Actual fractional jumps include \(+1\) at \(27/2\) and \(-1\) at \(3^{11}/2\). The unknown column cancels in the full sum, so its rationality under \(M\in\mathbb Q\) does not evaluate either part. ([Complete small-cutoff and jump audit](<hierarchy_boundary_audit.md>))

Pure dilation filters retain triangular relations
\[
E_A-2E_{A-1}=2F_{A-1},\qquad
T_B-3T_{B-1}=3G_{B-1};
\]
mixed filters add their finite corner. The free row \(G_0=0\) does not propagate to later rows. For the full product hierarchy numerator, use the distinct signed profiles \(U_i=3/2-3F_i\), \(V_j=2-3G_j\). Its exact dictionary is
\[
\mathcal B_P=\sum_{i<A_{\max}}\alpha_iU_i+
\sum_{1\le j<B_{\max}+4}\beta_jV_j+K_P,
\]
with integer coefficients and finite integer \(K_P\), now including the known contribution \(2\beta_0\) from \(V_0=2\). The low rows \(V_1,V_2,V_3\) remain explicit in the row sum. The outer coefficients are \(\alpha_{A_{\max}-1}=162\) and \(\beta_{B_{\max}+3}=3\). Neither independence nor irrationality of the remaining actual profiles is asserted. Their complete combination still lacks a cheap rational clearing theorem. ([Full dictionary and independent reconstruction](<hierarchy_boundary_audit.md>))

The integer corner assertion is termwise: each finite denominator divides its displayed shift multiplier. It does not absorb an unevaluated infinite side into the integer symbol. The formally growing profile list identifies the arithmetic still required, while allowing that additional actual-orbit identities could relate its values.

Three supplied and three independent exact checkers pass with the written proofs. The scalar route now has a usable correct-side criterion and a finite cleared return; its next theorem must establish actual infinite state-and-gap supply. The hierarchy instead needs arithmetic evaluation of its complete boundary combination and separate residual nonvanishing. These obligations cannot be exchanged between routes. The goal remains **active and unfinished**.

Skipped: new research or tests for this synthesis, Lean, external review and priority checks. Material risk: treating a finite exclusion or a complete conditional criterion as the still-unproved adequate infinite return.
