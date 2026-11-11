# Independent audit of state height budgets

## Do the actual discrepancy estimates prove the claimed first arrival bounds?

### Takeaway

**PASS; no substantive erratum found.** The qualitative first-arrival statement follows uniformly from the archived actual discrepancy theorem. The quantitative exponent \(K/(K+1)\) follows from the same elementary block argument and the correctly specialized primary Matveev theorem. Neither uses bounded partial quotients or a logarithmic discrepancy estimate. — [Audited HB1–HB5](height_budget.md), [archived CS1–CS3](../rational-coupling-construction/coupling_strictness.md), [primary Matveev, Theorem 2.1](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3).

### Cited Findings

- CS1 proves interval averaging uniformly in starting phase by comparison with a rational convergent grid. CS2 gives the exact raw color row sum; CS3 includes only bounded retiming changes. The uncorrected complex imbalance itself satisfies \(W(T)=o(T)\). — [Archived proof, CS1–CS3](../rational-coupling-construction/coupling_strictness.md).
- The actual board identities are \(A_a=\omega^{-a}W(a\log2)\) and \(B_b=\omega^bW(b\log3)\). The high state is \(A_a+B_b-1+C_{a,b}-E_b\), where \(C_{a,b},E_b\) take values in fixed finite sets. — [Accepted actual state and occupation audit](../numerator-and-residuals/occupation_audit.md), [canonical definitions](../response-closure-tests/response_relations.md).
- I independently opened Matveev's original English paper and checked its definitions and Theorem 2.1 on journal pp. 1218–1219. With degree one, positive real logarithms of 3 and 2, fixed heights \(A_1=A_2=2\), and integer coefficients \(q,-p\), all parameters except the logarithm of the coefficient size are fixed. Prime valuations give integer independence and nonvanishing. — [Primary definitions and theorem](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3), [previous specialization audit](../weighted-response-identities/fixed_logs_audit.md).

### Inferences

The finite values of the correction terms and the unit modulus of each color rotation give, for every \(\varepsilon>0\), one \(C_\varepsilon\) such that
\[
R(\zeta_{a,b})\le\varepsilon(a+b)+C_\varepsilon
\qquad(a\ge0,\ b\ge4),
\quad R(x+y\omega)=\max(|x|,|y|).
\]
Indeed, the archived \(o(T)\) estimate bounds both actual axes separately, and the finitely many small indices can be included in \(C_\varepsilon\). Evaluating at a first-arrival witness \(a+b=N(z)\) proves \(R(z)=o(N(z))\), uniformly along any occupied sequence with \(N(z)\to\infty\). This does not follow from unboundedness alone. It is an application of an already-proved qualitative sublinearity statement, not a new proof of that statement. — [CS2 and HB1–HB2](height_budget.md), [archived actual discrepancy](../rational-coupling-construction/coupling_strictness.md).

For the rate, put \(\beta=\log_2 3\), and let \(p/q\) be one of its convergents. The rational grid has interval-count error at most two. For \(0\le k<q\), the actual displacement from that grid is less than \(1/q\); only grid points within that distance of either interval endpoint can change membership. Ten is a safe uniform block error, including endpoint conventions. For
\[
g(u)=\omega^{\lfloor3u\rfloor},\qquad \int_0^1g(u)\,du=0,
\]
the three interval terms therefore give
\[
\sup_x\left|\sum_{k=0}^{q-1}g(x+k\beta)\right|\le30.
\]
Splitting an arbitrary block into full \(q\)-blocks and a remainder yields
\[
\sup_x\left|\sum_{k=0}^{n-1}g(x+k\beta)\right|
\le30n/q+q.
\tag{A1}
\]
The same proof applies to \(-\beta\), with the same denominators. No special initial phase or nonresonance condition is needed. — [CS1 and HB4](height_budget.md), [independent all-phase certificate](height_audit_check.py).

Matveev gives fixed effective constants \(c,C>0,K\ge1\), after absorbing the finite initial list, with
\[
|q\log3-p\log2|\ge c q^{-K},\qquad q_{\rm next}\le Cq^K.
\tag{A2}
\]
Here \(p\le2q\) eventually, and the usual convergent upper bound is \(\log2/q_{\rm next}\), so the coefficient and denominator scales agree. The theorem is applied to two fixed algebraic numbers and integer coefficients; no unknown occupation value is a coefficient. — [Primary Theorem 2.1](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3), [HB3](height_budget.md).

Set \(\kappa=K/(K+1)\), and choose the largest convergent denominator \(q\le n^\kappa\). Its successor exceeds \(n^\kappa\), so (A2) gives
\[
C^{-1/K}n^{1/(K+1)}<q\le n^\kappa.
\]
Both terms in (A1) are \(O(n^\kappa)\). This choice is valid even when the convergents have large gaps; no denominator near \(n^{1/2}\) has been assumed. — [HB2 rate derivation](height_budget.md).

In the exact CS2 row sum, the part with \(b=3k+r\) is a unit multiple of a \(g\)-sum at step \(-\beta\), starting at the moving phase \((T/\log2-\beta r)/3\). The first geometric sum is bounded. Uniformity in (A1) consequently proves
\[
|W(T)|\le C_1(T+1)^\kappa.
\]
The board identities, norm equivalence on \(\mathbb Z[\omega]\), bounded corrections, and concavity then give
\[
R(\zeta_{a,b})\le C_2(a+b+1)^\kappa,
\qquad
\boxed{R(z)\le C_2(N(z)+1)^\kappa.}
\tag{A3}
\]
All constants are fixed; their effective but enormous numerical values are not optimized. The reciprocal inequality bounds first arrival from below in terms of radius. It does not give an upper escape-time bound or a matching lower estimate for state growth. — [Exact CS2 decomposition](../rational-coupling-construction/coupling_strictness.md), [HB5](height_budget.md).

### Gaps

- The global finite optimum and canonical state formulas are accepted theorem inputs, not independently reproved here. The complete external proof of Matveev's theorem is also an input. — [Accepted occupation audit](../numerator-and-residuals/occupation_audit.md), [primary theorem](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3).
- No \(O(\log N)\) discrepancy, bounded partial quotients, or numerical escape-time assertion follows. The exponent is the weak fixed exponent justified above. — [Audited scope](height_budget.md).

## Which multiplier costs would suffice for an actual bridge?

### Takeaway

**PASS for the conditional budget.** A genuine bridge with multiplier bit cost \(O(R)\) is affordable. More generally \(O(R^d)\) is affordable for every fixed \(d<1+1/K\). No such arithmetic identity has been obtained. — [HB6–HB8](height_budget.md), [accepted positive-return criterion](../numerator-and-residuals/occupation_audit.md).

### Cited Findings

- The actual family has \(0<\mathcal E(z)\le6\,2^{-N(z)}-3\,3^{-N(z)}\). Its proposed bridge is \(T\mathcal E=uZ+v\), with positive integer \(T\) and integers \(u,v\). — [Actual family and arithmetic gap](../numerator-and-residuals/occupation_audit.md).
- A first-arrival cell supplies a positive witness \(w=2^{-a}3^{-b}\), where \(a+b=N(z)\), so \(\mathcal E(z)\ge w\ge3^{-N(z)}\). — [Occupation definition](../numerator-and-residuals/response_arithmetic.md), [independent witness checks](height_audit_check.py).

### Inferences

If the integer identities were proved and \(\log T=O(R)\), qualitative first-arrival sublinearity would give \(\log T=o(N)\). From (A3), the stronger condition
\[
\log T=O(R^d),\qquad \kappa d<1
\]
also gives \(\log T=o(N)\). A hypothetical \(Z=A/B\) would make \(BT\mathcal E=uA+Bv\) a positive integer bounded by \(6BT2^{-N}\to0\), a contradiction. The integer coefficients \(u,v\) need no independent height bound. At \(d=1/\kappa\), an \(O\)-bound alone is insufficient because its constant may consume the decay margin. — [HB3 and the accepted bridge deduction](height_budget.md).

For an approximate bridge \(R_*=(uZ+v)/T\), the stated witness budget
\[
|R_*-\mathcal E|\le\vartheta w,\qquad 0\le\vartheta<1,
\]
implies \((1-\vartheta)\mathcal E\le R_*\le(1+\vartheta)\mathcal E\). Thus positivity survives and the same multiplier budgets force \(TR_*\to0\). The uniform absolute budget \(\vartheta3^{-N}\) is sufficient because it is no larger than \(\vartheta w\). An arbitrary absolute error merely tending to zero does not suffice. — [HB4](height_budget.md), [first-arrival definition](../numerator-and-residuals/occupation_audit.md).

### Gaps

- Exact and approximate bridges remain hypotheses. A short formal state stencil or a small state radius does not supply target-dependent integer arithmetic. — [Explicit bridge gap](height_budget.md).
- No lower bound on any possible multiplier \(T\) is established. Physical index operations may create huge integer coefficients of \(Z\), which are distinct from denominator cost. — [Complete boundary dictionary](../weighted-response-identities/weighted_audit.md).

## Do the actual ambiguity and finite certificates reconstruct independently?

### Takeaway

**PASS; no substantive erratum.** Both supplied and independent checkers pass. The independent checker imports no project module, orders all phase cuts by rigorous rational isolation, and constructs the actual axes directly from original colored boards. — [Supplied checker](height_budget_check.py), [independent checker](height_audit_check.py).

### Cited Findings

- The supplied script reproduces complex block-norm squares \(1,1,1,3,1,1,3\) at \(\beta\)-convergent denominators \(1,2,5,12,41,53,306\), the actual ambiguity witness, and 24 states with first arrival below total index 80. — [Supplied checker, rerun successfully](height_budget_check.py).
- The independent checker confirms the same block maxima for both \(+\beta\) and \(-\beta\), the exact original-board witness, and 25 occupied states with first arrival below 86. The different state count is due to the larger finite triangle, not a disagreement. — [Independent checker](height_audit_check.py).

### Inferences

The independent phase certificate isolates every point \(r/3-k(\pm\beta)\) modulo one using rigorous rational logarithm intervals. All \(3q\) discontinuities are distinct, their intervals are disjoint, and their exact order is certified. Starting from the direct integer-power computation at phase zero, it updates the three counts across each individual jump. Right continuity assigns every endpoint to the following cell. This covers every phase for each named finite block, rather than merely a phase grid. The written rational-grid argument proves the all-\(q\) estimate; these finite checks validate its concrete implementation. — [Independent phase construction](height_audit_check.py).

Direct colored-board counts give
\[
A_0=A_9=1,\qquad A_3-A_0=-\omega,\qquad A_{12}-A_9=\omega^2.
\]
Thus \(Y_n=A_{3n}\) has the same value at \(n=0,3\), and physical residue \(a\bmod3=0\) in both cases, but different next three-step increments. A deterministic function of that state alone cannot give the actual next displacement. This does not refute every finite augmented state model, a guarded weighted-value cancellation, or a general arithmetic bridge. — [Independent original-board certificate](height_audit_check.py), [actual cocycle definitions](../boundary-and-arithmetic/arithmetic.md).

The guarded marginal renewal remains exact:
\[
\mu=\delta_1+\frac18\sum_v\tau_v\mu_v,\qquad
\sum_v\mu_v=\mu,
\]
where \(\mu_v\) records the actual indices with outgoing displacement \(v\). It follows by reindexing the absolutely convergent positive series. The witness gives \(\mu_{-\omega}(\{1\})\ge1\) and \(\mu_{\omega^2}(\{1\})\ge8^{-3}\), so those two guarded measures cannot be replaced by a single state-only outgoing rule. The renewal retains unknown guarded readouts and does not yield \(T\mathcal E=uZ+v\). — [HB9](height_budget.md), [independent witness](height_audit_check.py).

### Gaps

- **Final disposition: PASS; no substantive audit correction.** Neither exact nor approximate occupation arithmetic is constructed, and no infinite arithmetic return for \(Z\) follows from the budget alone. — [Audited scope](height_budget.md).
- Skipped Lean, external review, optimized numerical constants, a full reconstruction of Matveev's proof, and a new global proof of the archived finite optimum. Material risk: treating conditional state-cost feasibility or a finite-state counterexample as an actual arithmetic bridge or a universal impossibility theorem.
