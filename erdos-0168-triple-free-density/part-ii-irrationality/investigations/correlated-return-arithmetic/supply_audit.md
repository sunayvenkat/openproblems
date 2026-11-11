# Independent audit of resonant mediants and supply

## Are the digit threshold and neighboring-state reductions exact?

### Takeaway

**PASS; no substantive correction.** The digit-five reformulation concerns existence of a subsequence satisfying the accepted scalar sufficient bound. Resonant first mediants have exactly two response states, and both parents are automatically nonresonant. Neither statement establishes actual infinite joint supply. — [Audited notes](state_supply.md), [independent checker](supply_audit_check.py).

### Cited Findings

- Accepted scalar arithmetic gives \(D_{p,q}=27(2^{3q}-1)(3^{3p}-1)\), \(D_{p,q}\widehat Z\in\mathbb Z\), and cleared error at most \(486(1+o(1))2^{5q-Q}\). — [Accepted scalar framework](../weighted-response-identities/REPORT.md).
- The accepted neighboring commutator is \(C=(1-y)H_U-(1-x)H_V=\omega^k(1-\omega)\), where \(x=\omega^{u_p+u_q}\) and \(y=\omega^{v_p+v_q}\). Replacing the lower endpoint by its mediant preserves \(C\); replacing the upper endpoint multiplies \(C\) by \(x\). — [Earlier commutator and graph proof](../response-closure-tests/general_states.md).
- The new independent checker imports no companion module. It reconstructs the finite graph and evaluates actual rational transforms directly as \(H(p,q)=\sum_{a<q}\omega^{a+\lfloor pa/q\rfloor}\). — [Independent implementation](supply_audit_check.py).

### Inferences

Write \(h=q_{n-1},q=q_n,Q=q_{n+1}\). Eventually \(0<h<q\), and
\[
Q-5q=(a_{n+1}-5)q+h.
\]
Digits at most four make this negative; digits at least five make it at least \(h\). Since \(q_{n-1}\to\infty\), a selected infinite index set has \(Q-5q\to+\infty\) exactly when its sufficiently late selected next digits are all at least five. Consequently an adequate infinite subsequence inside an eligibility set exists iff that set contains infinitely many next-digit-\(\ge5\) indices. No assertion about every infinite eligibility set is made. — [SD1](state_supply.md), [independent threshold checks](supply_audit_check.py).

The neighboring graph starting from \(5/8<12/19\) closes on 24 states. Direct sums verify its initial transforms \(H(5,8)=2,H(12,19)=1\) and commutator \(1-\omega\). For the four prescribed balanced mediant transforms, the exact equations
\[
H_V=\frac{(1-y)h_m-C}{1-xy},\qquad H_U=h_m-xH_V
\]
give twelve neighboring rows and sixteen allowed current-parent orientations, matching SD2. Actual values of both transforms are part of eligibility; residues alone are insufficient. — [SD2 table](state_supply.md), [independent 12/16 enumeration](supply_audit_check.py).

If \(xy=1\), one parent multiplier could equal one only if both did. Their residue vectors would then lie in the same one-dimensional kernel of \(p+q\) over \(\mathbb F_3\), contradicting determinant \(\pm1\). Thus \(x,y\ne1\), and
\[
(1-x)H(UV)=-xC,\qquad H(UV)=-\frac{xC}{1-x}.
\]
This removes every parent-transform parameter. Substitution over the 24 graph states gives six resonant neighboring cylinders and precisely
\[
(r\bmod3,s\bmod3,H(r,s))=(1,2,1+\omega),\quad(2,1,1).
\]
The independent enumeration reproduces both counts and states. No balanced-parent or bounded-parent-transform hypothesis enters this derivation. — [SD3](state_supply.md), [independent resonant enumeration](supply_audit_check.py).

### Gaps

- The earlier exact commutator recurrence and four balanced-state definitions are accepted proved inputs; this audit reconstructs their new application, not the entire finite-cover foundation. — [Earlier independent state audit](../response-closure-tests/states_audit.md).
- The threshold concerns the displayed sufficient scalar bound, not every possible irrationality argument or denominator saving. No actual infinite joint visits are proved. — [Arithmetic scope](../weighted-response-identities/REPORT.md).

## Does complete resonant nonvanishing survive independent reconstruction?

### Takeaway

**PASS.** The two full response intervals, actual resonant example and uniform Matveev-based extension are valid. Independent original-token enumeration reproduces all 1024 coefficients in each of two complete low response rectangles. — [New response formulas](state_supply.md), [independent checker](supply_audit_check.py).

### Cited Findings

- Complete grade conservation and the quotient exterior bound apply at resonance. The earlier proof uses resonant jumps analytically without claiming cheap arithmetic for a resonant scalar value. — [Resonance-independent quotient proof](../response-closure-tests/general_states.md), [original-token audit](../response-closure-tests/states_audit.md).
- Accepted Matveev/Farey estimates give \(Q\le Cq^K\), \(|2^{-s}-3^{-r}|\ge c2^{-s}q^{-K^2}\), and full two-child variation below \(432\,2^{-(s+q)}\). — [Independent primary-source and scale audit](../weighted-response-identities/fixed_logs_audit.md).
- Both the supplied and independent checkers pass. The independent one uses original colored boards for actual axes, original retimed-token groups for rational births and minimum differences for low-row tests. — [Supplied checker](state_supply_check.py), [independent checker](supply_audit_check.py).

### Inferences

Let \(\mathcal K(t)=K_0(t)+K_1(t)\omega+K_2(t)\omega^2\) be the original board's color imbalance. Direct row summation gives
\[
A_a=\omega^{-a}\mathcal K(2^a),\qquad B_b=\omega^b\mathcal K(3^b).
\]
These identities construct the actual axes independently of the companion recurrences. The color correction is \((1-\omega^{-a})(1-\omega^{-2b})/3\), retaining the separate high-row isolate/patch correction. — [Accepted axis/state definitions](../response-closure-tests/response_relations.md), [independent board reconstruction](supply_audit_check.py).

For both new classes the canonical shifted endpoints are \(A_s^+=1,A_s^-=0\), with unit displacement. Summing the shifted horizontal increments gives \((0,1,-\omega)_{a\bmod3}\) or \((0,1+\omega,1)_{a\bmod3}\). The color-correction difference changes the index to \(a-b\bmod3\), proving SD4. The independent checker verifies the shifted/displaced state equality at every point of both \(32\times32\) rectangles. Four distinct low-row minimum-difference rules are retained. The exceptional original \((0,1)\) birth is not inserted into a response shifted to positive horizontal index. — [SD4 derivation](state_supply.md), [independent minimum-difference implementation](supply_audit_check.py).

Separately, the checker enumerates original tokens, applies each exceptional retiming once, groups simultaneous rational arrivals, and computes minimum-count birth increments for both tie orders. At the matching resonant models \(94/149\) and \(65/103\), the quotient agrees at **all 1024 coefficients** with the independently reconstructed actual response rectangle. The nonsmooth retimed arrival \((-1,3)\) has zero birth in both orders. Row-zero dyadic births are absent after retiming. — [Independent original-token certificate](supply_audit_check.py).

Adding the entire quotient exterior
\[
T_{32}=\frac{27}{2}2^{-32}+\frac{45}{2}3^{-32}
\]
proves
\[
\Gamma_+\in(77/100,79/100),\qquad
\Gamma_-\in(-11/20,-27/50).
\]
The bounded actual response has a smaller exterior; the displayed larger bound safely encloses both it and a sufficiently large matching rational quotient. Each complete quotient has absolute value greater than one half. — [SD5 enclosures](state_supply.md), [independent exact interval checks](supply_audit_check.py).

Thus \(|J|>\frac12|2^{-s}-3^{-r}|\), and the full variation obeys
\[
R/|J|=O(q^{K^2}2^{-q})\longrightarrow0.
\]
Correct-side nonvanishing follows uniformly for every sufficiently late resonant first mediant, without bounds on parent transforms. The complete actual-response comparison also gives the relative expansion with \(\Gamma_\pm\). Since \(\sigma(2^{-s}-3^{-r})<0\), the eventual error sign is minus the sign of \(\Gamma_\pm\). The **current** nonresonant model supplies the clearing factor; the resonant mediant needs only its analytic jump theorem. — [Audited Matveev comparison](../weighted-response-identities/fixed_logs_audit.md), [new uniform extension](state_supply.md).

An independent positive-\(\operatorname{atanh}\)-series interval for each actual logarithm, with explicit rational tails, confirms that \(41/65,53/84\) are consecutive actual convergents. For their resonant mediant \(94/149\), the complete jump lower bound divided by both entire child variations exceeds
\[
8\,268\,912\,743\,835\,790.
\]
This finite certificate checks actual use; the preceding scale argument proves asymptotic uniformity. — [Independent exact actual certificate](supply_audit_check.py).

### Gaps

- Matveev's theorem and the earlier pure-jump/Farey representation remain proved inputs. No optimized numerical eventual threshold is computed. — [Prior primary-source audit](../weighted-response-identities/fixed_logs_audit.md).
- Rationality of \(\Gamma_\pm\) under rationality of \(Z\) is unproved. Scalar nonvanishing needs no such implication, but a new arithmetic closure must establish its own interface. — [Accepted arithmetic distinction](../weighted-response-identities/weighted_audit.md).
- Uniform nonvanishing supplies neither infinite visits nor nonvanishing of the separately corrected full-fan residual. — [Explicit scope](state_supply.md).

## Are the avoidance countermodels and literature claims correctly scoped?

### Takeaway

**PASS.** Both full-state loops avoid resonant mediants forever. The Cantor argument produces transcendental abstract examples with finite algebraic approximation exponents in every fixed degree. The primary literature statement is correctly dated 2022 and does not establish the current status of the narrower joint-visit problem. — [SD7–SD8](state_supply.md), [independent loop/map checks](supply_audit_check.py), [primary paper](https://arxiv.org/pdf/2105.11173v2#page=1).

### Cited Findings

- The exact continued-fraction state retains parity, both residue vectors and both full transforms. Its future recurrence depends only on these data and the next digit, including resonant intermediate convergents. — [Accepted full recurrence](../boundary-return-mechanisms/cf_return_state.md).
- The independent checker directly evaluates every intermediate transform for each individual loop and also replays \(AC,CA,CC\) using integer continuants. — [Independent full-state reconstruction](supply_audit_check.py).
- I independently opened Spiegelhofer's *Collisions of digit sums in bases 2 and 3*, arXiv v2. Its first page states the bounded-partial-quotient question for \(\log3/\log2\). The PDF and version record date v2 to 20 April 2022; the record says accepted for Israel Journal of Mathematics. — [Primary text, p. 1](https://arxiv.org/pdf/2105.11173v2#page=1), [version record](https://arxiv.org/abs/2105.11173).

### Inferences

From the actual prefix through \(12/19\), both \(A=33\) and \(C=211211\) return the complete parity/residue/transform state. Every intermediate adjacent pair has nonzero sum of multiplier exponents, so its first mediant is nonresonant. This also holds at the initial/final state. The exact recurrence and induction prove avoidance for arbitrary infinite concatenations, beyond the checked finite words. All digits, including the fixed prefix, are at most three. — [SD7](state_supply.md), [direct-transform loop checks](supply_audit_check.py).

The even-length block matrices give
\[
f_A(t)=\frac{3+t}{10+3t},\qquad
f_C(t)=\frac{12+7t}{31+18t}.
\]
Both determinants are one. Their images in \([0,1]\) have gap \(g=32/403\), and both derivatives lie between \(1/2401\) and \(1/100\). If two level-\(n\) cylinders first differ earlier, their separation is still at least \(g\,2401^{-(n-1)}\). An interval shorter than this meets at most one such cylinder. Bernoulli cylinder masses \(2^{-n}\), with \(2401<2^{12}\), imply
\[
\mu(I)\le C|I|^{1/12}.
\]
The fixed-prefix Möbius map has absolute derivative bounded above and away from zero, preserving this exponent under pushforward. Both the separation and derivative scales are needed, and both check. — [SD8 proof](state_supply.md), [exact matrices/constants](supply_audit_check.py).

Counting integer polynomials and their roots gives \(O_D(T^{D+1})\) real algebraic numbers of degree at most \(D\) and naive height at most \(T\). In the shell \(2^j\le H(\xi)<2^{j+1}\), the union of intervals
\[
|\beta-\xi|<H(\xi)^{-12(D+2)}
\]
therefore has measure \(O_D(2^{-j})\). Summability gives only finitely many exceptional approximants for almost every slope, for each \(D\). Intersecting the countably many full-measure sets and removing all algebraic slopes from the nonatomic measure produces the claimed transcendental avoidance examples. Constants and finite exceptions may depend on the chosen slope and degree; no effective constants for a specified abstract slope are supplied. — [SD8 counting-measure proof](state_supply.md).

Unbounded partial quotients would imply infinitely many unrestricted digits at least five, but would still require a separate eligibility argument. The fixed-threshold property can also hold with bounded digits. Consequently the primary 2022 boundedness discussion neither supplies the required joint visits nor establishes the current global status of the threshold or joint-visit statement. The audited note makes no such extrapolation. — [Primary dated statement](https://arxiv.org/pdf/2105.11173v2#page=1), [explicit literature limitations](state_supply.md).

### Gaps

- These countermodels are abstract slopes sharing a finite actual prefix. They do not equal the actual logarithm ratio, reproduce its full arithmetic, or transfer its \(2,3\) coefficient array. They defeat only the stated generic inference from transcendence, finite approximation measures and the recurrence. — [Explicit SD8 scope](state_supply.md).
- No logarithm-specific infinite favorable-state/digit theorem is proved or located here. That is an unfilled requirement in this work, not a comprehensive current literature-status conclusion. — [Focused source scope](state_supply.md).
- **Final disposition: PASS; no substantive audit erratum.** Supplied and independent checkers pass. Skipped Lean, external review, the full Matveev proof, broader literature searches and priority verification. Material risk: treating enlarged uniform nonvanishing or abstract countermodels as facts about actual infinite adequate returns. — [Independent certificate](supply_audit_check.py).
