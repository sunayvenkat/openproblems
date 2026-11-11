# State radius and the occupation arithmetic budget

## How small is an actual state compared with its first arrival?

### Takeaway

**The actual state radius is sublinear in its first-arrival index.** Consequently an integer bridge whose multiplier has bit length linear in state radius would already meet the required arithmetic budget. The underlying qualitative color-discrepancy estimate is archival; its first-arrival application and the quantitative budget below are deductions here. No arithmetic bridge is constructed. — [Archived uniform discrepancy CS1–CS3](../rational-coupling-construction/coupling_strictness.md), [occupation definitions and positive family](../numerator-and-residuals/occupation_audit.md).

### Cited Findings

- The actual board imbalance is \(W(T)=\sum_{\lambda a+\mu b\le T}\omega^{a-b}\), where \(\lambda=\log2,\mu=\log3\). The archived proof establishes \(W(T)=o(T)\) using uniform interval averaging, not an assumed rate or bounded partial quotients. Its elementary rational-grid argument bounds the discrepancy of every interval in a convergent-denominator block by ten, uniformly in starting phase. — [CS1–CS3](../rational-coupling-construction/coupling_strictness.md), [independent earlier audit](../rational-coupling-construction/final_coupling_audit.md).
- Exact original-board identities give \(A_a=\omega^{-a}W(a\lambda)\), \(B_b=\omega^bW(b\mu)\). The high state is \(\zeta_{a,b}=A_a+B_b-1+C_{a,b}-E_b\), with bounded residue and patch terms. Its first arrival is \(N(z)=\min\{a+b:b\ge4,\zeta_{a,b}=z\}\). — [Original-board/occupation audit](../numerator-and-residuals/occupation_audit.md), [state definitions](../response-closure-tests/response_relations.md).
- Matveev's original Theorem 2.1 applies to the fixed logarithms of two and three with integer coefficients. Equal fixed height choices \(A_1=A_2=2\), degree one and prime valuations give a polynomial lower bound for the nonzero form. I read the primary statement and definitions on journal pp. 1218–1219. — [Primary Matveev theorem](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3), [earlier independently verified specialization](../weighted-response-identities/fixed_logs_audit.md).
- The new exact checker certifies all interval phases at seven actual convergent block denominators of \(\beta=\log_2 3\), independently checks original-board axes, and verifies finite first-arrival witness weights. These finite tests do not establish an asymptotic rate by themselves. — [Checker](height_budget_check.py).

### Inferences

**HB1. Qualitative first-arrival theorem.** Use \(R(x+y\omega)=\max(|x|,|y|)\). The two coordinates are bounded by a constant times the complex norm. From the archived \(W(T)=o(T)\),
\[
R(A_a)=o(a),\qquad R(B_b)=o(b).
\]
For every \(\varepsilon>0\), finitely many initial indices can therefore be absorbed into a constant \(C_\varepsilon\), giving the **uniform two-index inequality**
\[
R(\zeta_{a,b})\le\varepsilon(a+b)+C_\varepsilon\qquad(a\ge0,b\ge4).
\tag{HB1}
\]
At a first arrival, \(a+b=N(z)\). Thus along any sequence of occupied states with \(N(z_n)\to\infty\),
\[
\boxed{R(z_n)=o(N(z_n)).}
\tag{HB2}
\]
This is not inferred merely from unboundedness. It needs the uniform upper bound (HB1). The infinite distinct family already constructed in the occupation note has such first arrivals; bounded balls in \(\mathbb Z[\omega]\) contain finitely many points, so its radii also tend to infinity. — [Archival discrepancy input](../rational-coupling-construction/coupling_strictness.md), [actual infinite family and first-arrival selection](../numerator-and-residuals/occupation_audit.md).

**HB2. A quantitative version without bounded partial quotients.** Let \(p_j/q_j\) be convergents of \(\beta=\log_2 3\). Since eventually \(p_j\le2q_j\), the primary fixed-logarithm bound and the convergent upper bound give fixed effective constants \(c,C>0,K\ge1\) with
\[
|q_j\log3-p_j\log2|\ge c q_j^{-K},\qquad
q_{j+1}\le Cq_j^K.
\tag{HB3}
\]
The last coefficient is nonzero and the logarithms are integer-linearly independent by unique factorization. Heights and the number of terms stay fixed. Enlarging the constants handles the finite initial list. No actual digit-frequency statement follows. — [Matveev, Theorem 2.1](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3).

Here is the full rate derivation. Set \(g(u)=\omega^{\lfloor3u\rfloor}\) on the phase circle; it has mean zero and is a sum of three interval indicators with unit coefficients. For a convergent denominator \(q\), the archived rational-grid proof gives
\[
\sup_x\left|\sum_{k=0}^{q-1}g(x+k\beta)\right|\le30.
\]
Indeed \(|k(\beta-p/q)|<1/q\), so only rational-grid points within \(1/q\) of the two interval endpoints can change membership; the bound ten includes the grid-count error and endpoint conventions. Splitting an arbitrary \(n\)-block into \(q\)-blocks and a remainder yields
\[
\sup_x\left|\sum_{k=0}^{n-1}g(x+k\beta)\right|
\le30n/q+q.
\tag{HB4}
\]
Put \(\kappa=K/(K+1)<1\), and choose the largest convergent denominator \(q\le n^\kappa\). By (HB3),
\[
q\ge C^{-1/K}n^{1/(K+1)}.
\]
Consequently (HB4) is \(O(n^\kappa)\), uniformly in the starting phase. This uses no logarithmic-discrepancy hypothesis. The constants are effective but neither optimized nor evaluated numerically. — [Elementary block proof CS1](../rational-coupling-construction/coupling_strictness.md), [exact all-phase finite block checks](height_budget_check.py).

The exact row-sum formula CS2 splits its second sum into \(b=3k+r\), with each part a rotation sum of \(g\) at step \(-\beta\). Its first geometric sum is bounded. The same argument applies to \(-\beta\), so uniformly in the moving cutoff phase,
\[
|W(T)|=O((T+1)^\kappa).
\]
The board identities and bounded corrections now give, for one fixed \(D>0\),
\[
R(\zeta_{a,b})\le D(a+b+1)^\kappa,\qquad
\boxed{R(z)\le D(N(z)+1)^\kappa.}
\tag{HB5}
\]
Concavity, for example \((a+1)^\kappa+(b+1)^\kappa\le2^{1-\kappa}(a+b+2)^\kappa\), pays simultaneous growth of the axes. The reciprocal form is \(N(z)\ge(R(z)/D)^{1/\kappa}-1\). It is a lower bound on first arrival in terms of state radius, **not** an upper escape-time estimate. — [Exact row decomposition CS2](../rational-coupling-construction/coupling_strictness.md), [state definitions](../numerator-and-residuals/response_arithmetic.md).

### Gaps

- Qualitative sublinearity itself is not new; it is explicitly archived. HB2 and HB5 make its consequence for occupation arithmetic and an elementary quantitative extension explicit. — [Archived statement](../rational-coupling-construction/coupling_strictness.md).
- No bounded-partial-quotient assumption, \(O(\log N)\) discrepancy, effective numerical escape time, or matching lower bound for state growth is claimed. — [Hypotheses and actual support distinction](../numerator-and-residuals/occupation_audit.md).

## Which multiplier costs would actually finish the occupation route?

### Takeaway

**A true bridge with multiplier bit cost \(O(R)\) is sufficient, with no restriction on the heights of its integer target coefficients.** Quantitatively, any fixed cost exponent below \(1+1/K\) in state radius is affordable. These are usable sufficient budgets, not constructions of the arithmetic identities. — [Accepted bridge criterion RA11](../numerator-and-residuals/occupation_audit.md), [HB1–HB5 above](height_budget.md).

### Cited Findings

- Actual positive atoms satisfy \(0<\mathcal E(z)\le6\,2^{-N(z)}-3\,3^{-N(z)}\). A bridge \(T\mathcal E=uZ+v\), with positive integer \(T\) and integer \(u,v\), proves irrationality along an infinite family if \(\log T=o(N)\). — [Exact occupation-return and lattice deduction](../numerator-and-residuals/occupation_audit.md).
- At a first arrival \((a,b)\), \(a+b=N\), its single positive weight supplies \(\mathcal E(z)\ge2^{-a}3^{-b}\ge3^{-N}\). The checker confirms this inequality at every finite first-arrival cell it constructs. — [Occupation definition](../numerator-and-residuals/response_arithmetic.md), [exact witness checks](height_budget_check.py).

### Inferences

**HB3. State-radius budget.** Suppose actual integer identities
\[
T_n\mathcal E(z_n)=u_nZ+v_n,
\quad T_n\in\mathbb Z_{>0},\quad u_n,v_n\in\mathbb Z
\tag{HB6}
\]
were proved. If \(\log_2T_n=O(R(z_n))\), then HB2 gives \(\log T_n=o(N_n)\), regardless of the fixed constant in the \(O\)-term. More generally HB5 allows
\[
\log T_n=o(R(z_n)^{1/\kappa}),
\]
and in particular
\[
\boxed{\log T_n=O(R(z_n)^d),\qquad d<1/\kappa=1+1/K.}
\tag{HB7}
\]
If \(Z=A/B\) were rational, \(BT_n\mathcal E(z_n)=u_nA+Bv_n\) would be a positive integer bounded by \(6BT_n2^{-N_n}\to0\). The integer coefficients \(u_n,v_n\) can be arbitrarily large; their heights do not enter this elementary fixed-lattice contradiction. At the critical exponent \(d=1/\kappa\), a mere \(O\)-bound does not guarantee a saving: its constant would have to be compared with the decay margin. — [Accepted exact bridge deduction](../numerator-and-residuals/occupation_audit.md), [proved state bound HB5](height_budget.md).

**HB4. The same budget applies to a sufficiently accurate approximate bridge.** Let \(R_n=(u_nZ+v_n)/T_n\). If a construction proves
\[
|R_n-\mathcal E(z_n)|\le\vartheta\,2^{-a_n}3^{-b_n},\quad
0\le\vartheta<1,\quad a_n+b_n=N_n,
\tag{HB8}
\]
then \((1-\vartheta)\mathcal E(z_n)\le R_n\le(1+\vartheta)\mathcal E(z_n)\). The preceding multiplier budgets force \(T_nR_n\to0\) while preserving strict positivity. The stronger uniform error \(\vartheta3^{-N_n}\) is sufficient too. This demonstrates exactly how a first-arrival witness can pay positivity; an unspecified small absolute error cannot replace HB8. No such approximate bridge has been constructed here. — [Positive first-arrival weights and tail](../numerator-and-residuals/occupation_audit.md), [finite witness checks](height_budget_check.py).

### Gaps

- HB6 and HB8 are arithmetic hypotheses. Small state radius, a unit-coefficient Green stencil, and rational total measure do not imply them. — [Explicit arithmetic gap](../numerator-and-residuals/occupation_audit.md).
- Coefficient bit cost and multiplier bit cost are different. A physical index shift can create a huge integer coefficient of \(Z\) without increasing \(T\); conversely, unknown guarded boundary values may prevent any arithmetic identity at all. No lower bound on \(T\) follows from operation count alone. — [Complete weighted boundary dictionary](../weighted-response-identities/weighted_audit.md).

## Does the actual state alone provide the required cheap transport?

### Takeaway

**No deterministic state-only three-step closure is valid even on the actual orbit.** An exact small witness shows the missing phase information. This rules out that tempting closure, not all target-dependent bridges or a multiplier-height bound. — [Actual cocycle](../boundary-and-arithmetic/arithmetic.md), [independent original-board certificate](height_budget_check.py).

### Cited Findings

- In the accepted three-step description, \(Y_n=A_{3n}\), \(x_n=\{n\alpha\}\), \(Y_{n+1}=Y_n+\Phi(x_n)\), where \(\alpha=\log_3 2\) and \(\Phi\) is the nonconstant nine-breakpoint step function. — [Equations (5)–(7)](../boundary-and-arithmetic/arithmetic.md), [actual R3](../infinite-return-construction/ray_return_attack.md).
- Exact recurrence and direct original-board counts independently give
  \[
  A_0=A_9=1,\qquad A_3-A_0=-\omega,\qquad A_{12}-A_9=\omega^2.
  \]
  The checker verifies both methods. — [New finite certificate](height_budget_check.py).

### Inferences

**HB5. Actual ambiguity.** There is no function of \(Y_n\) alone giving its next three-step displacement for all actual indices: the same state \(1\), at \(n=0\) and \(n=3\), has two different outgoing displacements. The physical residue \(a\bmod3\) is zero in both cases. At fixed high row \(b=4\), the target state is \(Y_n\) plus one constant, so the same ambiguity remains for the actual high-state occupation. A proof of a bridge must therefore retain or correctly eliminate phase information; choosing a path of unit state directions does not realize a path of actual index shifts. — [Actual cocycle and fixed-row formula](../numerator-and-residuals/occupation_audit.md), [exact witness](height_budget_check.py).

The exact marginal renewal still exists. Define positive guarded measures
\[
\mu=\sum_{n\ge0}8^{-n}\delta_{Y_n},\qquad
\mu_v=\sum_{\Phi(x_n)=v}8^{-n}\delta_{Y_n}.
\]
With \(\tau_v\) denoting state translation by \(v\), absolute convergence gives
\[
\boxed{\mu=\delta_1+\frac18\sum_v\tau_v\mu_v,
\qquad\sum_v\mu_v=\mu.}
\tag{HB9}
\]
Both \(\mu_{-\omega}(\{1\})\ge1\) and \(\mu_{\omega^2}(\{1\})\ge8^{-3}\) are positive. Multiplying HB9 by eight yields integer coefficients, but leaves the distinct guarded readouts. It does not identify any translated cone value with an integer-affine function of \(Z\). The companion exact-transport work studies the full phase lift; HB9 and the actual witness show why its guards cannot simply be discarded. — [Accepted actual skew product](../boundary-and-arithmetic/arithmetic.md), [companion transport investigation](exact_transport.md), [new exact witness](height_budget_check.py).

### Gaps

- No genuine exact or approximate occupation bridge has been obtained. The height budget is now sufficient for any proved linear-state-cost mechanism, but existence of such a mechanism remains open. — [Stated bridge interface](../numerator-and-residuals/occupation_audit.md).
- The checker uses only standard-library integers and fractions. It validates all actual interval phases at block denominators \(1,2,5,12,41,53,306\), the board-axis identities, the ambiguity witness and finite arrival weights. Infinite sublinearity/rate claims rest on the written block and fixed-logarithm proofs, not finite extrapolation. — [Checker](height_budget_check.py).
- Skipped: Lean, external review, optimized numerical Matveev constants and reproof of the archived finite optimum. Material risk: mistaking a cheap formal state stencil or a state-growth estimate for an arithmetic bridge with its phase guards and boundaries controlled.
