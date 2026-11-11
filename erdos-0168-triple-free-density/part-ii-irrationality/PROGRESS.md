# Erdos 168 consolidated progress

Updated 2026-11-10. This is the current progress record; older reports remain historical records of their respective stages.

Part (i) remains provisionally complete as a structural determination; its final comprehensive rigor and novelty review is deferred. The numerical denominator exclusion is conditional on rationality, the working model theorems and the stored large-model evaluation. Part (ii) remains unproved.

Latest Route P review: the archived Green stencils and a flux lemma for genuinely decaying functions are valid. Their application to Q_H(-z) fails the decay hypothesis and reflection shift. Actual slice complexity/nonperiodicity, slice transcendence, nonrationality/natural boundary of the actual bivariate generating function, and the target-value arithmetic bridge are NOT proved by the new files. The verifier tests a driving floor word instead of the actual birth word. [Review](<investigations/potential-theoretic-obstruction/codex_review.md>). Route P is an exploratory alternative, not a completed bypass of the other proof gaps. The new adversarial audit also overstates its conclusions: failed empirical upper-bound margins do not prove actual divergence, and a genuinely independent arithmetic-separation theorem would be a valid approach.

The latest incorporated Claude work is the nine-file [cheap-clearer investigation](<investigations/cheap-clearer-search/notes.md>). It adds a valid conditional modular obstruction to a rational target denominator; its infinite arithmetic supply remains unproved. [The latest integration review](<investigations/cheap-clearer-search/codex_review.md>) records its proof scope, checks and corrected finite statistics. All nine source files, and the 28 source files in the preceding integration, remain unchanged.

The [remaining proof checklist](<todo.md>) breaks the open routes into individual lemma targets with finish conditions and dependencies. Complete one route and the final checks; the alternative routes are not cumulative requirements. [The plan](<plan.md>) gives the dependency map.

The main refinement is that, for convergent rational models, unbounded denominators are equivalent to infinitely-often nonvanishing. On an infinite family already covered by the existing nonvanishing theorems, no separate primitive-prime argument is needed. The main missing theorem for that route is actual infinite adequate supply. Larger finite certificates, including a giant partial quotient of Z, do not establish that infinitude.

The latest Antigravity additions are [the half-cleared series notes](<investigations/half-cleared-vertical-series/notes.md>) and verify.py. H1 and H2 are now working-complete: the complete normalized hybrid and the uniform bound |E_n|<=9*2^(2q_n-q_(n+1)) have written proofs. H3 remains open: actual infinite nonresonant next-digit-at-least-two supply is not implied by transcendence, and the modulo-nine decomposition leaves an uncontrolled infinite remainder. [The integration review](<investigations/half-cleared-vertical-series/codex_review.md>) distinguishes the proved identities from those unsupported consequences. Checklist H5 and H6 isolate these remaining subtargets.

Latest verification (2026-11-10): the new tail-gcd notes and master synthesis do not solve part (ii). Their claimed completion of M2–M7 has been withdrawn from this record. [The review and exact counterexamples](<investigations/tail-gcd-obstruction/codex_review.md>) explain the cross-factor, valuation and infinite-quantifier failures. H1–H2 remain working-complete; actual supply and arithmetic separation remain open.

Current revision review (2026-11-10): the rewritten single-clearer implication is valid conditional on an arbitrarily late adequate index coprime to M_B. A three-clearer pigeonhole lemma is also valid with pairwise coordinate coprimality and explicit exceptional-prime conditions. Neither proves actual infinite supply or visits. M2–M6 remain open as infinite-visit tasks; checklist M8 and M9 isolate the two alternative supply theorems. The single-clearer script loses CF accuracy at n=487; the triple script has interval-verified finite examples through the tested cutoffs, not an all-cutoff theorem. [Updated rigorous review](<investigations/tail-gcd-obstruction/codex_review_update.md>).

## Incorporated part i files

The files from ../part-i-density-formula have been copied without modification into [the part i snapshot](<../part-i-density-formula/README.md>). The snapshot contains 29 proof, report, code, audit, and output files. Source and destination SHA256 hashes matched for every copied file; [SOURCE_MANIFEST.json](<../part-i-density-formula/SOURCE_MANIFEST.json>) records the exact versions.

The main imported results are:

1. A self-contained ordinary proof of the finite minimum-cover formula for every cutoff, in [PROOF.md](<../part-i-density-formula/PROOF.md>).
2. An explicit rule for all cover increments, the density series, a gauge-integral representation, and an exact numerical enclosure, in [REPORT.md](<../part-i-density-formula/REPORT.md>).
3. The accompanying [Claude audit](<../part-i-density-formula/audit/AUDIT.md>) and its scripts/output, preserved as evidence rather than substituted for the mathematical argument.

During the preceding bounded review, the full finite proof was read without finding a substantive gap. Re-execution reproduced the brute-force checks, zero mismatches at 190 smooth cutoffs through 10^7, and the numerical interval of width 1.319190289287 × 10^(-128) at cutoff 10^130. The numerical enclosure remains conditional on the finite formula and increment rule. Those checks are not a final universal proof audit or a novelty review.

## Working mathematical foundation

Let F(N) be the largest size of a subset of {1,...,N} containing no complete triple {n,2n,3n}, and let c = lim F(N)/N.

Write
\[
D_t=\{2^a3^b\le t:a,b\ge0\}.
\]
Let tau(t) be the minimum cardinality of a set meeting every corner {u,2u,3u} in D_t. Color 2^a3^b by a-b modulo three, with color counts K_j(t).

The working finite theorem is
\[
\tau(t)=\min_{j=0,1,2}\bigl(K_j(t)-I_j(t)-P_j(t)\bigr),\qquad t\ge3.
\]
For 1 <= t < 3, tau(t)=0.

I_j records an isolated dyadic root e=2^A, A>=1, A congruent to j modulo three, with 2t/3 < e <= t. For consistency with the imported increment and gauge formulas, P_j uses patch roots A>=2 with 6e <= t < 27e/4. The original A>=1 patch convention gives the same minimum: its extra window [12,27/2) does not change tau. Do not mix these conventions inside the adjusted count vector.

Let Q_j=K_j-I_j-P_j and let eta_(a,b) be the TRUE jump of tau at d=2^a3^b. The adjusted vector increases by one in the following colors:

| New point d | Colors increased, modulo three |
|---|---|
| 2^a, a>=1 | None |
| 3*2^a, a<=2 | a+1 and a+2 |
| 3*2^a, a>=3 | a+1 |
| 27*2^a | a and a+2 |
| All remaining d>=3 | a-b |

The jump eta_(a,b)=1 exactly when every minimizing color of Q(d-) is increased. The small values are eta_(0,0)=eta_(1,0)=0 and eta_(0,1)=1.

Put
\[
M=\sum_{a,b\ge0}\eta_{a,b}2^{-a}3^{-b}.
\]
The exact normalizations are
\[
c=1-M/3,\qquad Z=9c-6=3-3M.
\]
The later transport notation uses an UNEXCEPTIONAL all-row readout Q_full(0), with the sole removed birth at (0,1):
\[
M=Q_{\rm full}(0)+1/3,\qquad Z=2-3Q_{\rm full}(0).
\]
The true and unexceptional arrays must not be interchanged without this correction. Every low row still has infinite horizontal extent.

The imported alternative representation is
\[
c=\frac{757}{972}+\frac29\int_3^\infty H(\widehat S(t))\,t^{-2}\,dt,
\quad
\widehat S(t)=\sum_{j=0}^2Q_j(t)\omega^j,
\quad
H(z)=\max_j\operatorname{Re}(-\omega^{-j}z),
\]
where omega^2+omega+1=0. This uses the A>=2 patch convention above. It is an additional exact working representation, not an irrationality theorem.

The computed density begins
\[
c=0.80096575500655898909042032638808241\ldots.
\]

## Current proof roadmap

| Component | Working status |
|---|---|
| Existence of c and decomposition into m*2^a*3^b components | Established background |
| Universal finite optimum, including boundary and patch cases | Working proof complete; imported consolidation and internal audits retained |
| Explicit true birth increments and structural determination of c | Incorporated from the part i files |
| Certified numerical evaluation | Imported exact enclosure reproduced in the preceding review |
| Complete rational scalar models, known clearing D and rectangle/error bounds | Working proofs available; full low rows and corrections retained |
| Correct-side scalar nonvanishing in four balanced and two resonant-mediant states | Working proof complete for sufficiently late applicable indices |
| Exact Christoffel recurrence and residue-only resonant-mediant test | Incorporated; an algorithm/classification, not an infinite-visit theorem |
| Unbounded denominators iff infinitely-often nonvanishing for convergent models | Proved; automatic on any infinite known nonvanishing family |
| Actual infinite adequate scalar supply in a known nonvanishing class | OPEN: L_E below; the simpler sufficient subcase is L_* |
| Nonvanishing/denominator growth outside the known scalar classes | OPEN if selecting a different actual G1 family |
| Modular obstruction replacing a separate nonvanishing proof | Proved: rational Z forces B to divide every late adequate clearer D_n |
| Single-clearer and triple-clearer implications | Working-proved conditionally; actual coprime-locus/triple supply remains OPEN (M8/M9) |
| Actual adequate supply K = {n : sigma_n != 0, a_{n+1} >= 5} | OPEN (Task M1 / A1); Diophantine barrier connected to open CF problem of log2/log3 |
| Resonant-current scalar route | Complete rational examples available; uniform cost, effective-error/nonvanishing and adequate infinite supply remain open |
| Half-cleared vertical series (H1–H2) | Working proof complete: exact normalized W_n and uniform error bound |E_n| <= 9 * 2^(2q_n - q_{n+1}); arithmetic separation H3 open |
| Ordered renewal sources | Rational source and positive vanishing residual available; affordable clearing remains open |
| Route P: potential and slice approach | Stencils/decaying-function flux valid; target application invalid; actual slice transcendence and natural boundary unproved (P2–P6) |
| Final contradiction | Ready conditionally for established scalar/positive-residual routes; no route has supplied all its required infinite arithmetic hypotheses |
| Final comprehensive rigor and novelty review | Deferred by the user |

Overall, the structural/combinatorial part is working-complete. The standard nonresonant scalar route can now be stated as one explicit missing infinite-visit theorem, with its nonvanishing and clearing already supplied by the working inputs. Other routes have their own arithmetic gaps; they are alternatives rather than additional tasks all of which must be completed.

## What part ii must prove

It suffices to construct actual rational models z_n and positive integers d_n with
\[
d_nz_n\in\mathbb Z,\qquad 0<|d_n(Z-z_n)|\longrightarrow0.
\]
If Z=A/B were rational, B*d_n*(Z-z_n) would be a nonzero integer tending to zero. A positive real error tending to zero before clearing does not meet this requirement.

### Exact missing lemma for the original scalar route

Let alpha=log(2)/log(3), p/q=p_n/q_n and P/Q=p_(n+1)/q_(n+1) be consecutive ACTUAL convergents, with next digit a_(n+1). Let r=p+P, s=q+Q be their first mediant. Define
\[
\sigma_n=p_n+q_n\pmod3,\qquad
H(r,s)=\sum_{j=0}^{s-1}\omega^{j+\lfloor rj/s\rfloor}.
\]
The known eligible set of mediant states (r modulo 3,s modulo 3,H) is
\[
\mathcal E=\underbrace{\{(0,1,1),(1,1,1),(2,0,2+\omega),(2,2,2)\}}_{\mathcal B}
\cup\{(1,2,1+\omega),(2,1,1)\}.
\]

The following ingredients are already working-proved:

1. For a nonresonant CURRENT model (sigma_n!=0), its complete correct-side rational value z_n has
   \[
   D_n=27(2^{3q}-1)(3^{3p}-1),\quad D_nz_n\in\mathbb Z,
   \quad D_n|Z-z_n|\le486(1+o(1))2^{5q-Q}.
   \]
   The side is the limit from alpha. The two evaluators use opposite sign names for this same choice.
2. For sufficiently late applicable n with first-mediant state in E, Z!=z_n. Both full Eisenstein transforms matter in the balanced branch. Resonant mediants need no bounded-parent-transform assumption.
3. Q-5q=(a_(n+1)-5)q+q_(n-1). A selected family has Q-5q -> infinity exactly when its late selected next digits are at least five.

**Missing L_E:** prove that there are infinitely many actual n for which sigma_n!=0, a_(n+1)>=5, and the first-mediant state belongs to E. No such infinitude theorem is proved in these files. A finite exact scan, graph reachability, transcendence of alpha, or a bound above on its partial quotients does not establish L_E.

Two sufficient subcases exhaust this particular eligible-set supply:

- **Missing L_* (resonant mediant):** infinitely many n satisfy a_(n+1)>=5 and sigma_n+sigma_(n+1)=0 modulo three. The determinant condition automatically makes both current and successor nonresonant. Equivalently, with t_n=sigma_(n-1)/sigma_n, require sigma_n!=0 and a_(n+1)=-1-t_n modulo three. The archived commutator theorem supplies one of the two eligible resonant response states automatically. This is the cleanest missing lemma: no unbounded transform appears in its formulation.
- **Missing L_B (balanced mediant):** infinitely many n satisfy sigma_n!=0, a_(n+1)>=5, and first-mediant state in B, including the actual value of H. Residue recurrence alone does not prove this branch.

Once either lemma holds, restrict to its infinite sufficiently late tail. The existing nonvanishing theorem and error bound give 0<D_n|Z-z_n|->0. Multiplication by a hypothetical fixed denominator of Z gives the contradiction. No further cyclotomic denominator theorem is required on this family. These are sufficient missing lemmas for the present route, not necessary conditions for every possible proof of irrationality.

### What remains of the second, denominator-growth approach

For any infinite family of rational z_n converging to Z,
\[
\operatorname{den}(z_n)\text{ unbounded}
\quad\Longleftrightarrow\quad
z_n\ne Z\text{ infinitely often}.
\]
Bounded denominators put a convergent family in a fixed discrete rational lattice, forcing eventual equality to Z. The complete actual models converge by the rectangle estimate.

Thus, on ANY infinite known eligible family, the unbounded-denominator condition G2 is automatic. The first and second approaches meet at the same missing adequate supply there. For a different nonresonant family outside E, two obligations remain: prove an actual infinite K with Q-5q -> infinity (G1), and prove infinitely-often nonvanishing on that SAME K (equivalently G2). One possible arithmetic proof of G2 is to show that a primitive prime of a period factor survives cancellation in the WHOLE numerator N_n=D_nz_n infinitely often. Its existence before cancellation is insufficient. Separate unrelated infinite supply and denominator-growth families do not suffice.

### New modular alternative: prevent persistent divisibility

On any infinite actual nonresonant family K with a_(n+1)>=5, hypothetical rationality Z=A/B forces z_n=Z and B divides D_n for every sufficiently late n in K. This follows from the existing integer/error estimate and does not require a first-mediant state or an independent nonvanishing theorem.

The new conditional theorem closes the proof if K also satisfies ND: for every fixed integer M>=2, infinitely many n in K have both p_n and q_n coprime to M. Multiplicative-order and valuation identities then contradict B dividing all late D_n, using the earlier finite certificate B>2^56. Both actual adequate supply and ND remain unproved.

A weaker sufficient target is
\[
\gcd\{D_n:n\in K,\ n\ge N\}\le447174=2\cdot27\cdot49\cdot169
\quad\text{for every sufficiently large }N.
\]
Equivalently one may construct arbitrarily late finite adequate blocks with that small gcd. A finite gcd near the start of a prefix does not control unknown late tails.

This target splits into separate missing primewise statements on K: v_2(D_n)<=1 infinitely often; v_3(D_n)<=3 infinitely often; v_7(D_n)<=2 infinitely often; v_13(D_n)<=2 infinitely often; and, for each fixed outside prime ell, ell does not divide D_n infinitely often. Different primes may use different subsequences of the same K. For outside primes, define m_2=ord_ell(2)/gcd(ord_ell(2),3) and m_3=ord_ell(3)/gcd(ord_ell(3),3); avoidance is exactly m_2 not dividing q_n AND m_3 not dividing p_n. The arithmetic classification is proved; its actual infinite visits are not. Tasks M1–M7 in the checklist isolate these obligations.

### Other sufficient routes and their exact gaps

- **Resonant-current models.** Complete rational cone models and isolated successful examples exist. An infinite proof needs: (a) a usable bound for the full reduced denominator d_n, including powers of 2 and 3; (b) a proved real error bound, potentially stronger than the floor-agreement rectangle; (c) correct-side nonvanishing infinitely often; and (d) an infinite actual resonant family on which log_2(d_n)+log_2|Z-z_n| -> minus infinity. For example, proposed bounds log_2(d_n)<=Cq+o(q) and |Z-z_n|<=2^(-(1+theta)(q+Q)) still require an infinite family with (1+theta)(q+Q)-Cq-o(q) -> infinity. The effective-window conjecture R-EW alone supplies neither full cost, nonvanishing nor that supply.
- **Cheaper complete models without digit-five supply.** One sufficient construction would cover every sufficiently late index with a_(n+1)>=2, in ALL residue classes, with z_n!=Z,
  \[
  \log_2d_n\le3q_n+o(q_{n-1}),\qquad
  |Z-z_n|\le2^{-(q_n+q_{n+1})+o(q_{n-1})},\qquad d_nz_n\in\mathbb Z.
  \]
  Infinitely many such indices exist because alpha is not a quadratic irrational with an eventual all-one tail. Then the cleared exponent is at most -q_(n-1)+o(q_(n-1)). This construction, its budget and nonvanishing remain unproved. A finite lower bound at q=84 does not refute an eventual asymptotic construction. An O(2^(2q)) clearer with the old error is another sufficient target; colour tripling does not prohibit alternative constructions or scalar cancellation.
- **Ordered renewal sources.** The complete identity Z=2-3S_R^ord+3Psi_R has rational S_R^ord, positive Psi_R and Psi_R->0. The missing theorem is an infinite family of positive integers d_R clearing 2-3S_R^ord with d_R*Psi_R->0. Positivity and real tail decay are already supplied. Retain all nine high and twelve low sources (or consistently remove the zero row); do not assume auxiliary coupled sources are rational.
- **Half-cleared vertical series (H1–H2 working-complete).** Horizontal periodization gives the complete exact identity (2^(3q_n)-1)Z=W_n+E_n with W_n = sum_{b>=0} G_n(b) 3^{-b} - (2^{3q_n}-1), where G_n(b) = sum_{a=0}^{3q_n-1} (1-3\widetilde\eta'_{a,b}) 2^{3q_n-a} in Z, retaining all low rows, true vertical walk B_b and events E_b, and the exact Z=3-3M normalization. Within the accepted state/model framework, the written full-tail proof gives |E_n| <= 9 * 2^(2q_n - q_{n+1}) (Tasks H1 and H2 completed in `research_notes/Erdos 168 half-cleared vertical series/notes.md`). Since 2q_n - q_{n+1} <= -q_{n-1} whenever a_{n+1} >= 2, E_n -> 0 exponentially fast on any nonresonant family with next digit at least two (whose infinitude for the actual alpha remains unproved). If Z=A/B were rational, ||B W_n|| <= 9B * 2^(2q_n - q_{n+1}) -> 0. Proving arithmetic separation ||B W_n|| >= \epsilon_B > 0 (Task H3) remains the open research step.
- **Occupation, fan or hierarchy bridges.** A new complete integer-affine identity with Z must evaluate or eliminate all auxiliary translated/phase/boundary readouts, charge its full multiplier and prove a nonzero residual within that budget. Rationality of Z does not rationalize those readouts. The known state-height exterior decay exp(-gamma*R^(1/kappa)), 0<kappa<1, would accommodate a genuine bridge with log(multiplier*amplitude)=o(R^(1/kappa)); no such bridge follows from geometric boundary counts alone.

### Latest finite progress and conditional enhancements

- Exact logarithm intervals now certify 600 digits of alpha. On n=3,...,591 the review reproduces 39 adequate eligible visits: 38 resonant-mediant and one balanced. This certifies a finite prefix; L_E and L_* still require infinitely many visits.
- Nonvanishing is checked at n=4,...,12 (q from 8 through 125743), using later-model intervals and, for n=12, the complete resonant-mediant jump criterion. This is a finite list, not a universal nonvanishing theorem outside E.
- Both full tested cyclotomic factors survive in eight stored actual nonresonant models through q=125743. Claude reports a ninth at q=176251; that full value was not regenerated in this review.
- The stored q=125743 model, with the FULL rectangle-error radius, yields 71,933 common CF terms of Z. A partial quotient at index 10,707 has 27,607 bits; the preceding convergent is exactly the resonant 665/1054 model. The exact enclosure arithmetic was reproduced, conditional on the working model theorem and stored value. The correct radius lies between 2^(-301990) and 2^(-301989); one printed exponent in Claude's note drops a factor near two.
- That enclosure excludes rational denominators below 2^150990 for Z and also for c, since den(9c-6) divides den(c). It replaces the previous >2^56 exclusion. The largest stored model center was not recomputed from its full tile in this bounded review.
- The new Subspace-Theorem argument conditionally excludes algebraic irrational Z if infinitely many applicable nonresonant next digits are at least six. With nonvanishing on that same family it proves transcendence. Its hypothesis remains unproved, so it does not solve part (ii).
- The new tail-gcd claim is invalid. Exact gcd(D(5,8),D(12,19))=24570>4914 refutes its general coprime-pair inference; cross factors were omitted. The verifier uses reciprocal convergents, bounded primes and finitely many cutoffs. M2–M7 have been restored as open tasks.
- On Route H, the horizontal hybrid series is fully normalized (H1) and its uniform error bound |(2^{3q_n}-1)Z - W_n| <= 9 * 2^{2q_n - q_{n+1}} is proved and verified (H2). The Ternary Digit Law (Theorem 5) establishes G_n(b) = C_0(L) - 3 Delta_n(b) mod 9 and W_n = 2(2^L-1) - 3 D_n + 9 R_n, advancing H3.
- Continued fraction dichotomy: By transcendence of log2/log3, partial quotients a_{n+1} >= 2 occur infinitely often. An algebraic 8-cycle analysis in F_3^2 proves that if all sufficiently late nonresonant digits were 1, the CF of log2/log3 would eventually be forced into the periodic-block structure (A_k, 1, 1, 1) in the Fuchsian congruence subgroup Gamma_0(3). Hence, either infinitely many nonresonant digits satisfy a_{n+1} >= 2 (supplying Route H), or all large digits sit at resonant indices in Gamma_0(3).

## Limits already identified

1. Convex boundary tuning realizes rational aggregate sources in shrinking intervals. Internal potential denominators need not be cleared. However, the least model denominator d_R satisfies d_R*W_R -> 0 IF AND ONLY IF Z is irrational for these intervals. Width decay alone is not an independent supply theorem.
2. The radius-two optimized model 5201/4303 has 0 < 4303*(Z-5201/4303) < 2^(-10). It does not improve either the older >2^56 exclusion or the latest finite bound above.
3. Nonperiodic Boolean coefficients in this two-base series can still have a rational total. A rational total need not make boundary suffixes rational. The final-round carry countermodel is generic, not the actual Erdos array.
4. The exact ten-dimensional pure-horizontal guard module and the at-most-100-dimensional actual product span do not close joint accumulated-state/phase observables. State flux cannot be discarded.
5. Full shifts commute; boundary-killed shifts need not commute. The unrestricted Frobenius shortcut is invalid for the killed operator.
6. For the specified large-offset coupled Picard family, a nonzero full-source residue implies v_3(den S_(R,m))=3m+3. Finite residue observations do not prove an infinite supply; a failed upper error majorant is not a lower bound on actual error. Changing exterior offsets changes the arithmetic family.
7. A five-row witness excludes state-only potentials plus arbitrary additive pure-phase forcing on the full lifted radius-one box. It does not exclude genuine state/phase interaction or identities restricted to actual support.
8. The final-round boundary-response obstruction concerns a universal exact small integer-network representation of the FULL response map. It does not prohibit cancellation in one specially chosen aggregate source. These final-round carry/boundary notes have no fresh independent audit.
9. A raw-state period does not force the full nominal geometric-series denominator after reduction. The new colour-tripling argument therefore does not prove a universal denominator-cost barrier. Its actual affine return holds for a<Q; three successive applications require a+2q<Q.
10. The colour-tripling report's two cyclotomic-loss examples are nonconvergent upper slopes with the opposite tie convention from the actual ordering. They refute unrestricted two-sided divisibility, not the correctly oriented actual-convergent claim. Both the older 127-term and newer 71,933-term CF prefixes of Z remain finite evidence. For the toy sum, only eight terms are certified by its checked tail enclosure; its reported 802-bit quotient is outside that prefix.
11. Lemma C's infinite abstract (A,1,1,1) block construction shows that transcendence alone cannot force large nonresonant next digits. Finite greedy-avoidance experiments do not prove infinite avoidance. Neither type of countermodel determines the actual tail of alpha or excludes all other irrationality methods.
12. The kappa_min calculation is a necessary denominator lower bound at a finite input, not an attained optimum and not a disproof of the conditional cheap-model lemma. The original certify.py nonvanishing test adds both model radii and cannot pass for two valid enclosures; the corrected test uses only the later model's radius. See the integration review.
13. The new divisibility_check.py swaps p_n and q_n through its initial recurrence values; the corrected statistics above govern this record. Its arithmetic theorem is unaffected. A returned LLL basis and a finite subproduct scan do not exclude every small-coefficient clearer or prove a universal cost barrier. The raw character derivation omits corrections and low rows and does not establish a minimum denominator for the complete scalar value.

## Integration correction and source map

The imported report's phrase that optimizers are completely described should be read as the existence of an optimum of the stated form, not a classification of all optima. At t=9, the mixed minimum deletion cover {2,3} is another optimum. The source snapshot is preserved unchanged; this correction governs the consolidated record.

The staircase generalization in the source report is computational evidence only. Neither the imported decimal computation nor the gauge formula establishes irrationality. Claims of historical novelty in source documents remain claims for the final review.

Read the following for exact hypotheses and constructions:

- [Part i source snapshot and integration notes](<../part-i-density-formula/README.md>).
- [Ordered renewal report](<investigations/arithmetic-renewal/REPORT.md>) and its three audits.
- [Exact state and phase transport](<investigations/occupation-arithmetic-bridge/exact_transport.md>).
- [Numerator, fan and occupation results](<investigations/numerator-and-residuals/REPORT.md>).
- [Scalar signed returns](<investigations/signed-arithmetic-returns/REPORT.md>), with the later numerator/residual report for extended nonvanishing scopes.
- [Claude's colour-tripling and denominator criterion](<investigations/colour-tripling-barrier/REPORT.md>), with [scope corrections and selected exact checks](<investigations/colour-tripling-barrier/codex_review.md>).
- [Claude's scalar supply refinement](<investigations/scalar-supply-barrier/supply_barrier.md>) and [actual supply/model results](<investigations/actual-supply-and-denominators/theory.md>), with [the current integration review](<investigations/actual-supply-and-denominators/codex_review.md>) and [exact checker](<investigations/actual-supply-and-denominators/codex_review_check.py>).
- [Claude's cheap-clearer and modular-divisibility work](<investigations/cheap-clearer-search/notes.md>), with [the latest integration review](<investigations/cheap-clearer-search/codex_review.md>).
- [Remaining proof checklist](<todo.md>) and [route/dependency plan](<plan.md>).
- [Final-round carry analysis](<investigations/rationality-rigidity/carries.md>) and [boundary-response analysis](<investigations/rationality-rigidity/boundary.md>).
- [Part ii research prompt](<prompts/Erdos 168 part ii irrationality.md>).

No autonomous proof-search goal is active. The prior goal was cleared by the user; this update incorporates the newly located Claude work and revises the roadmap, without starting another proof-search round.

