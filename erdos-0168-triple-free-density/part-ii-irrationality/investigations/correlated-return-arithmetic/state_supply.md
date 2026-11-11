# Actual state supply and resonant mediants

## What exactly must the actual continued fraction supply?

### Takeaway

The scalar adequacy condition is precisely a fixed-digit visit condition, not unbounded partial quotients: an adequate infinite subsequence exists exactly when infinitely many eligible indices have next digit at least five. The balanced-mediant eligibility condition has twelve explicit neighboring-state rows and sixteen oriented current-parent cases. This is an exact reformulation and state classification, not a proof of actual infinite supply. — [Accepted scalar criterion](../weighted-response-identities/REPORT.md), [new exact checker](state_supply_check.py).

### Cited Findings

- For consecutive actual convergents \(p_n/q_n,p_{n+1}/q_{n+1}\) of \(\alpha=\log2/\log3\), the accepted scalar model has clearing factor \(27(2^{3q_n}-1)(3^{3p_n}-1)\), and its cleared error is bounded by \(486(1+o(1))2^{5q_n-q_{n+1}}\). Uniform correct-side nonvanishing is already proved when the current model is nonresonant and its first mediant is in the four balanced nonresonant states. — [Previous fully audited theorem](../weighted-response-identities/REPORT.md), [primary-logarithm audit](../weighted-response-identities/fixed_logs_audit.md).
- The full neighboring Christoffel data are lower/upper residues \(u,v\), multipliers \(x=\omega^{u_p+u_q},y=\omega^{v_p+v_q}\), transforms \(H_U,H_V\), and commutator \(C=(1-y)H_U-(1-x)H_V=\omega^k(1-\omega)\). There are exactly twenty-four reachable residue/phase states after the actual interval \(5/8<12/19\), with one phase for each determinant-minus-one residue pair. — [GS1–GS3 and closed graph proof](../response-closure-tests/general_states.md), [earlier independent state audit](../response-closure-tests/states_audit.md).

### Inferences

**SD1. Exact digit threshold.** Put \(q=q_n,Q=q_{n+1},h=q_{n-1}\), with \(n\) large enough that \(0<h<q\). The defining recurrence gives
\[
Q-5q=(a_{n+1}-5)q+h.
\]
If \(a_{n+1}\le4\), this is at most \(h-q<0\). If \(a_{n+1}\ge5\), it is at least \(h\). Since \(h\to\infty\), for every infinite index set \(I\),
\[
Q-5q\longrightarrow+\infty\quad(n\to\infty,n\in I)
\quad\Longleftrightarrow\quad
a_{n+1}\ge5\text{ for all sufficiently large }n\in I.
\tag{SD1}
\]
Consequently, if \(\mathcal E\) denotes any stated eligibility set, there is an adequate infinite subsequence in \(\mathcal E\) if and only if \(\{n\in\mathcal E:a_{n+1}\ge5\}\) is infinite. A tail consisting only of digit five would already give the adequacy margin \(h\to\infty\); no digit tending to infinity is required. The checker exhaustively verifies the elementary integer inequalities for small parameters, while the displayed argument proves all parameters. — [Exact threshold checks](state_supply_check.py), [accepted adequacy exponent](../weighted-response-identities/REPORT.md).

**SD2. The finite balanced-parent cylinder.** Write residue pairs in \((p,q)\) order, with lower endpoint before upper, and let \(h_m=H(UV)\). For a balanced nonresonant mediant, \(h_m\) is prescribed by the four-state table. The exact equations
\[
H_V=\frac{(1-y)h_m-C}{1-xy},\qquad H_U=h_m-xH_V
\tag{SD2}
\]
give the following complete list inside the twenty-four-state graph. Entries \((a,b)\) in the transform columns mean \(a+b\omega\). “Both” allows either endpoint as current; the other choices exclude the resonant current endpoint.

| Lower residue \(u\) | Upper residue \(v\) | \(k\) | \(H_U\) | \(H_V\) | Allowed current |
|---|---|---:|---|---|---|
| \((0,1)\) | \((1,0)\) | 0 | \((1,0)\) | \((0,0)\) | Both |
| \((0,2)\) | \((2,0)\) | 1 | \((3,2)\) | \((2,1)\) | Both |
| \((0,2)\) | \((2,1)\) | 2 | \((3,2)\) | \((1,0)\) | Lower |
| \((1,0)\) | \((1,2)\) | 2 | \((3,0)\) | \((1,1)\) | Lower |
| \((1,2)\) | \((0,2)\) | 1 | \((1,1)\) | \((0,-1)\) | Upper |
| \((1,2)\) | \((1,1)\) | 1 | \((1,1)\) | \((1,0)\) | Upper |
| \((2,0)\) | \((1,1)\) | 1 | \((2,1)\) | \((1,0)\) | Both |
| \((2,0)\) | \((2,1)\) | 2 | \((2,1)\) | \((1,0)\) | Lower |
| \((2,1)\) | \((0,1)\) | 0 | \((1,0)\) | \((1,0)\) | Upper |
| \((2,1)\) | \((1,0)\) | 0 | \((1,0)\) | \((0,0)\) | Upper |
| \((2,2)\) | \((0,1)\) | 0 | \((2,0)\) | \((1,0)\) | Both |
| \((2,2)\) | \((1,2)\) | 2 | \((2,0)\) | \((1,1)\) | Lower |

There are sixteen oriented cases. For actual neighboring endpoints in the graph, membership in a row, including the actual values of BOTH transforms, is equivalent to balanced nonresonant mediant eligibility with the indicated nonresonant current. This is not a finite-residue-only test: arbitrary transforms at the same residue pair need not satisfy the row. Equation SD2 proves necessity and sufficiency; the checker enumerates the closed graph and solves the exact Eisenstein equations. — [Checker function balanced_parent_cylinders](state_supply_check.py), [accepted commutator and balance table](../response-closure-tests/general_states.md).

### Gaps

- No argument here forces the actual logarithmic trajectory to enter these rows infinitely often with \(a_{n+1}\ge5\). A finite exact state algorithm is not a frequency theorem. — [Prior actual-state scope](../boundary-return-mechanisms/cf_return_state.md).
- SD1 is an equivalence for the proved scalar sufficient bound, not a necessary condition for every possible irrationality proof or every possible scalar denominator saving. — [Arithmetic scope](../weighted-response-identities/REPORT.md).

## Can resonant first mediants be used without bounded parent transforms?

### Takeaway

Yes. Every sufficiently late actual resonant first mediant has one of only two fixed nonzero response states, independent of the possibly unbounded parent transforms. The current model is automatically nonresonant, and the Matveev one-node argument extends uniformly to this entire resonant-mediant class. No resonant scalar clearing theorem is assumed. — [New exact resonant classification and certificate](state_supply_check.py), [accepted resonance-independent jump conservation](../response-closure-tests/general_states.md).

### Cited Findings

- Grade conservation, the toric paired-jump factorization, and its exterior coefficient bound hold at resonance. The earlier proof explicitly distinguishes an analytic resonant jump from rationality or cheap arithmetic of either resonant scalar value. — [GS2, resonance justification](../response-closure-tests/general_states.md), [original-token independent audit](../response-closure-tests/states_audit.md).
- The shifted endpoint and all low-row response rules depend on the rational residues, its transform, and the matching short actual floor word; their formula does not divide by \(1-\rho\) or require nonresonance. — [Complete endpoint formula](../signed-arithmetic-returns/signed_scalar_check.py), [accepted canonical response construction](../response-closure-tests/response_relations.md).

### Inferences

**SD3. Resonance removes the unbounded parent parameter.** If the first mediant is resonant, \(xy=1\). Neither parent can have multiplier one: if one did then both would, placing both residue vectors in the same one-dimensional kernel of \((p,q)\mapsto p+q\) over \(\mathbb F_3\), contrary to their nonzero determinant. Thus both parent models are nonresonant. From \(h_m=H_U+xH_V\) and the commutator,
\[
(1-x)h_m=(1-xy)H_U-xC=-xC,
\qquad h_m=-\frac{xC}{1-x}.
\tag{SD3}
\]
For \(x=\omega\), this is \(-\omega^{k+1}\); for \(x=\omega^2\), it is \(\omega^k\). Hence no bound on either \(H_U\) or \(H_V\) is needed. Of the twenty-four reachable neighboring residue/phase states, precisely these six have resonant mediant:

| \(u\) | \(v\) | \(k\) | Mediant \((r,s,H)\) modulo three |
|---|---|---:|---|
| \((0,1)\) | \((1,1)\) | 1 | \((1,2,1+\omega)\) |
| \((0,2)\) | \((2,2)\) | 0 | \((2,1,1)\) |
| \((1,0)\) | \((0,2)\) | 1 | \((1,2,1+\omega)\) |
| \((1,1)\) | \((1,0)\) | 0 | \((2,1,1)\) |
| \((2,0)\) | \((0,1)\) | 0 | \((2,1,1)\) |
| \((2,2)\) | \((2,0)\) | 1 | \((1,2,1+\omega)\) |

The table is exhaustive by the closed graph induction; substitution in SD3 establishes the transform independently of its parents' unknown sizes. — [Exact six-state enumeration](state_supply_check.py), [accepted graph closure](../response-closure-tests/general_states.md).

**SD4. Explicit original-state formulas for both new response arrays.** Write the actual coefficient state as
\[
z(a,b)=A_a+B_b-1+C_{a,b}-E_b\quad(b\ge4),
\]
and omit \(E_b\) for \(b\le3\). Here \(A_0=B_0=1\) are the accepted actual axes, \(C_{a,b}\) is the periodic color correction, and \(E_b\) is the high-row isolate/patch correction. For the two resonant classes the shifted endpoint is always \(A_s^+=1,A_s^-=0\), and the displacement direction is \(\omega^{2r-s}=1\). Define, with \(j=a-b\pmod3\),
\[
D_j^+=(0,1,-\omega)_j,
\qquad D_j^-=(0,1+\omega,1)_j.
\]
Then their actual canonical arrays are exactly
\[
g_\pm(a,b)=-3\bigl[\Phi_b(z(a,b)+D_j^\pm)
-\Phi_b(z(a,b)+D_j^\pm-1)\bigr],
\tag{SD4}
\]
where, for \(z=x+y\omega\),
\[
\begin{array}{c|l}
b&\Phi_b(z)\\\hline
0&0\\
1&\mathbf1_{\{x\ge1,\ y\ge0\}}\\
2&\mathbf1_{\{x\le-1,\ x-y\le0\}}\\
3&\mathbf1_{\{\min(x,0)\le y\}}\\
\ge4&\mathbf1_{\{x\le0,\ x-y\le0\}}.
\end{array}
\]
The original target has a forced exceptional birth at \((0,1)\); SD4 does NOT insert it into the shifted responses, whose original horizontal coordinate is positive. Every displayed low row is retained. — [Accepted original and shifted birth rules](../response-closure-tests/response_relations.md), [new full displacement check](state_supply_check.py).

For a direct proof of SD4, let \(S(m)=\sum_{j=0}^m\omega^{2j}\), extended periodically. The exact identities
\[
S(m+1)=1+\omega^2S(m),\qquad S(m+2)=-\omega+\omega S(m)
\]
show that the shifted-plus horizontal increment differs from the original increment by \(\omega^{1-a}\) in class \((1,2)\), and by \(-\omega^{-a}\) in class \((2,1)\). Their accumulated differences are respectively \((0,1,-\omega)_{a\bmod3}\) and \((0,-\omega^2,1)_{a\bmod3}\). Adding \(C_{a+s,b}-C_{a,b}\) changes the index from \(a\) to \(a-b\). This last identity is a nine-entry periodic calculation in each case. Subtracting the unit endpoint displacement and applying the complete row tests proves SD4 coefficientwise on the entire quadrant. The checker compares the resulting weighted rectangle with the independent canonical endpoint formula in both classes. — [Canonical increment and correction definitions](../signed-arithmetic-returns/signed_scalar_check.py), [displaced_response checker](state_supply_check.py).

Define the absolutely convergent actual constants \(\Gamma_\pm=\sum_{a,b\ge0}g_\pm(a,b)2^{-a}3^{-b}\). A \(32\times32\) low rectangle, with the full bound \((27/2)2^{-32}+(45/2)3^{-32}\), proves
\[
\Gamma_+\in(77/100,79/100),\qquad
\Gamma_-\in(-11/20,-27/50).
\tag{SD5}
\]
The same enclosures hold for the complete rational quotient in a matching sufficiently large resonant state: its low coefficients agree, and its complete exterior has the stated bound. For the actual bounded array alone, the simpler exterior bound \(9(2^{-32}+3^{-32}-2^{-32}3^{-32})\) is smaller. These are the same two response classes previously encountered as resonant children, but the new SD3 argument removes any bounded-parent or balanced-parent hypothesis. — [Exact full enclosures](state_supply_check.py), [previous child enclosures and tail proof](../response-closure-tests/general_states.md).

**SD5. Uniform resonant-mediant nonvanishing.** Take any sufficiently late actual current/successor pair \(p/q,P/Q\) with resonant first mediant \(r/s\). Both parents are nonresonant by SD3. The accepted complete jump comparison gives
\[
|E-\sigma J|\le R,
\quad |J|>\tfrac12|2^{-s}-3^{-r}|,
\quad R<432\,2^{-(s+q)}.
\]
The primary Matveev argument already audited in the previous round supplies
\[
Q\le Cq^K,\qquad
|2^{-s}-3^{-r}|\ge c\,2^{-s}q^{-K^2}.
\]
Thus \(R/|J|\to0\) uniformly on this entire class. In particular \(E\ne0\) eventually, with no assumption on either parent transform, no successor-ratio or digit restriction, and no resonant scalar denominator. The same low-rectangle equality and complete exterior comparison as RR7 give
\[
E=\sigma(2^{-s}-3^{-r})\Gamma_\pm
\bigl(1+O(q^{K^2}2^{-q})\bigr).
\tag{SD6}
\]
The eventual error sign is minus the sign of \(\Gamma_\pm\). The floor-word hypothesis is automatic at a sufficiently late first mediant, as before. — [Complete jump comparison and primary scale proof](../weighted-response-identities/fixed_logs_audit.md), [resonance-independent grade conservation](../response-closure-tests/general_states.md), [new resonant enclosures](state_supply_check.py).

**SD6. A complete actual new case.** Current \(41/65\), successor \(53/84\), and mediant \(94/149\) give the resonant state \((1,2,1+\omega)\). Exact evaluation proves
\[
|2^{-149}-3^{-94}|\,(|Q_{32}|-T_{32})
>\mathcal V(41,65;94,149)+\mathcal V(94,149;53,84).
\]
It therefore certifies the correct-side error is nonzero. The checker also recomputes the \(8\times8\) quotient directly from retimed original tokens in rational grades and obtains the identical canonical value; simultaneous arrivals and all low-token conventions are retained. This verifies the implementation's use at a resonant first mediant, while the preceding proof establishes the uniform theorem. — [Exact actual and original-token certificate](state_supply_check.py).

Combining SD1 with the uniform theorem SD5 gives a strictly enlarged conditional scalar finish: infinitely many actual indices with next digit at least five and either a balanced nonresonant first mediant as in SD2, or ANY resonant first mediant, would prove \(Z\), hence the density, irrational. In the resonant branch, eligibility is now a six-cylinder residue/phase condition without any transform bound. — [Accepted scalar clearing](../weighted-response-identities/REPORT.md), [SD1 and exact new class checks](state_supply_check.py).

### Gaps

- Neither infinitely many resonant mediants nor infinitely many adequately large next digits jointly with them are proved for the actual logarithm ratio. — [Exact recurrence and its scope](../boundary-return-mechanisms/cf_return_state.md).
- The new real constants \(\Gamma_\pm\) have not been shown rational under rationality of \(Z\). The scalar finish above does not need them rational, but a different arithmetic closure using them must prove its own interface. — [Previously audited arithmetic distinction](../weighted-response-identities/weighted_audit.md).

## Can transcendence or finite approximation measures force the new visits?

### Takeaway

No generic argument of that form is valid. There are transcendental abstract slopes sharing the actual prefix through \(12/19\), having finite algebraic approximation exponents in every bounded degree, with all partial quotients at most three and no later resonant first mediant at all. A primary source documents the broader bounded-partial-quotient question as unresolved in 2022; it does not establish the present fixed-threshold joint-visit question's current literature status. — [New full-state avoidance loops](state_supply_check.py), [Spiegelhofer, primary preprint, p. 1](https://arxiv.org/pdf/2105.11173v2#page=1).

### Cited Findings

- The original 2022 version of Spiegelhofer's subsequently accepted paper on digit-sum collisions introduces \(\log3/\log2\), says the boundedness of its partial quotients is not known, and separately cites Baker-type polynomial rational-approximation bounds. The arXiv record identifies v2 as dated 20 April 2022 and accepted for Israel Journal of Mathematics. — [Primary text, pp. 1–2](https://arxiv.org/pdf/2105.11173v2#page=1), [author submission/version record](https://arxiv.org/abs/2105.11173).
- The exact full-state recursion retains both transforms, both residue pairs, and parity; at the actual prefix \([0;1,1,1,2,2]\), it is \((1,(2,2,2),(0,1,1))\), with integer-pair notation for transforms understood. It is valid at resonant intermediate convergents. — [CR3 and initial state](../boundary-return-mechanisms/cf_return_state.md).

### Inferences

**SD7. A new exact resonant-avoidance loop.** Start from
\[
\mathfrak s_0=(\text{odd},(2,2,H=2),(0,1,H=1)).
\]
Both blocks
\[
A=(3,3),\qquad C=(2,1,1,2,1,1)
\tag{SD7}
\]
return this entire state exactly. The current states during \(C\) are
\[
(2,1,1),\ (2,2,2),\ (1,0,3),\ (1,2,1+\omega),\ (2,2,2),\ (0,1,1).
\]
At every intermediate step of both blocks, the sum of the two endpoint multiplier exponents is nonzero modulo three. Hence the first mediant is never resonant; the same is true at block boundaries. All digits are at most three. The exact recurrence, including its resonant intermediate steps, proves the two block identities; the checker replays every state and tests every mediant residue. Arbitrary infinite concatenations inherit the avoidance by induction. — [Full loop replay](state_supply_check.py), [accepted exact recurrence](../boundary-return-mechanisms/cf_return_state.md).

**SD8. Quantitatively non-Liouville transcendental countermodels.** There are such avoidance slopes with finite approximation exponents to algebraic numbers of EVERY bounded degree; thus the objection is stronger than a sparse quadratic-Liouville example. Here is a self-contained existence proof.

For a tail parameter \(t\in[0,1]\), the two even-length block maps are
\[
f_A(t)=\frac{3+t}{10+3t},\qquad
f_C(t)=\frac{12+7t}{31+18t}.
\]
Their interval images are separated by
\[
\frac{12}{31}-\frac4{13}=\frac{32}{403}=:g>0,
\]
and both derivatives lie between \(1/2401\) and \(1/100\). These claims follow from their determinant-one matrices and endpoint denominators; their exact constants are checked in the certificate. Give A and C independent probabilities one half and push the Bernoulli measure onto the resulting continued-fraction Cantor set. Distinct level-n cylinder intervals are separated by at least \(g\,2401^{-(n-1)}\), because at their first differing block the initial separation is multiplied by at least \(2401^{-1}\) per earlier block. Thus an interval \(I\) with
\[
g\,2401^{-n}\le |I|<g\,2401^{-(n-1)}
\]
meets at most one level-n cylinder, and its measure is at most \(2^{-n}\). Since \(2401<2^{12}\),
\[
\mu(I)\le C|I|^{1/12}.
\tag{SD8}
\]
Larger intervals only change the constant. Appending the fixed actual prefix is a fixed Möbius map with derivative bounded above and away from zero on \([0,1]\), so its pushed measure obeys the same exponent and is supported on slopes in the actual prefix cylinder, all satisfying SD7.

There are \(O_D(T^{D+1})\) algebraic numbers of degree at most D and naive height at most T: count integer polynomials and their at most D roots. In the shell \(2^j\le H<2^{j+1}\), the union of intervals
\[
|\beta-\xi|<H(\xi)^{-12(D+2)}
\]
has measure \(O_D(2^{-j})\) by SD8. The shell sums converge. Therefore for \(\mu\)-almost every slope, only finitely many such approximations occur, simultaneously for every D by countable intersection. The measure is nonatomic, so removing all algebraic slopes still leaves measure one. Consequently there are transcendental \(\beta\), sharing the actual prefix, avoiding every later resonant first mediant, with all digits at most three, and with a finite naive-height approximation exponent \(12(D+2)\) in each bounded degree. Finitely many exceptions can be absorbed into a positive constant depending on \(\beta,D\). No such \(\beta\) is asserted to equal \(\log2/\log3\). — [Exact block and constant certificate](state_supply_check.py), [precedent for the same elementary counting-measure mechanism](../signed-arithmetic-returns/seed_arithmetic_audit.md).

The new example shows why neither transcendence nor adding generic finite approximation measures forces the new resonant visits or adequate scalar digits. The earlier actual-logarithm source does not change that logical conclusion: it concerns a stronger global boundedness question and is dated 2022. Absence of a located modern joint-visit theorem is recorded as a research gap, not as a proved impossibility or a claim that no such theorem exists. — [Primary dated statement](https://arxiv.org/pdf/2105.11173v2#page=1), [new exact recurrence countermodel](state_supply_check.py).

### Gaps

- No logarithm-specific infinite favorable-state/digit theorem was obtained. The needed fixed threshold \(a_{n+1}\ge5\) is weaker than unbounded partial quotients, and eligibility adds another condition; the primary 2022 statement cannot establish the weaker statement is currently open. No current primary theorem proving the required joint visits was located in the focused search.
- SD8 is an existence theorem on abstract slopes; it does not transfer the actual \(2,3\) coefficient array to a different slope, and it does not duplicate every arithmetic property of the actual logarithm ratio. It blocks only the stated generic inference.
- Skipped: Lean, external review, a complete literature survey, new actual continued-fraction scans beyond the exact named cases, and any assertion of historical novelty. Material risk: treating uniform nonvanishing on the enlarged class as a proof that actual adequate indices visit it infinitely often.
