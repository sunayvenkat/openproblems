# Audit of critical continued fraction states

## Does the rational triangle describe every sufficiently late actual critical interval?

### Takeaway

**PASS.** The comparison is a proved all-convergent statement under the explicit small-error inequality, not an extrapolation from five examples. Actual low-row delays and the fractional token at \(27/2\) are retained. — [Corrected source, CR1–CR2](cf_return_state.md), [independent certificate](cf_state_audit_check.py).

### Cited Findings

- The supplied checker passes under Python 3.14 with `-B`. The independent checker imports no companion code and reconstructs actual arrivals as doubled integers, the rational triangle by a different recursive staircase count, and Christoffel transforms from literal words. — [Supplied checker](cf_return_state_check.py), [independent checker](cf_state_audit_check.py).
- Independent enumeration recovers the pre-states \((43,43,43)\), \((189,189,189)\), \((1900,1900,1900)\), \((3127,3127,3127)\), and \((99852,99851,99852)\) at \(5/8,12/19,41/65,53/84,306/485\). In every case the closed critical interval contains exactly the three prescribed tokens and no others. — [Function actual_interval and exact assertions](cf_state_audit_check.py).
- The actual continued-fraction prefix through \(665/1054\) is certified with integer comparisons \(2^{1054}<3^{665}\) and \(2^{1539}>3^{971}\). These place the logarithmic slope in the relevant continued-fraction cylinder; no floating logarithm is used. — [Independent prefix replay](cf_state_audit_check.py).

### Inferences

Put \(u=2^q,v=3^p\), \(\delta=q\log_3 2-p\), and assume the stated inequality \(3\max(u^2,v^2)<4\min(u^2,v^2)\). The critical interval has endpoints \(9\min(u^2,v^2)\) and \(9\max(u^2,v^2)\), centered logarithmically at \(9uv\). An ordinary high-row point has logarithmic displacement \(h\alpha+k\), where \(h=a-q,k=b-p-2\). Points with \(a>2q,b\ge2\) lie above the interval by the small-error inequality. For \(0<|h|<q\), convergent best approximation gives \(|h\alpha+k|>|\delta|\); its sign is unchanged upon replacing \(\alpha\) by \(p/q\), because the perturbation is less than \(1/q\), the minimum nonzero rational mesh. The cases \(h=0,\pm q\) leave precisely the three critical points. Thus all earlier high-row points are exactly
\[
pa+q(b-2)<2pq,\qquad a\ge0,\ b\ge2.
\]
The proof needs no assumption \(q_{\rm next}>2q\). — [CR1](cf_return_state.md).

The best-approximation input also reconstructs directly in the current/preceding unimodular basis. After changing signs to make \(h>0\), mixed-sign coefficients add the magnitudes of opposite convergent errors. Same-sign nonnegative coefficients either have denominator at least \(q\) or are a positive multiple of the preceding vector, whose error exceeds \(|\delta|\). Both negative coefficients cannot give \(h>0\). This establishes the required strict inequality for \(0<|h|<q\). — [CR1 and exact actual interval reconstruction](cf_return_state.md), [independent checker](cf_state_audit_check.py).

Relative to \(9u^2\), the last included and first excluded dyadic arrivals have ratios \(2/3,4/3\); the corresponding row-one ratios are \(3/4,3/2\). The same small-error inequality separates all four from the critical interval. Hence the two low rows terminate at \(a=2q+2\) and \(a=2q+1\), respectively. This explicitly includes the delayed row-one root and does not replace its arrival by an ordinary monomial. — [CR1](cf_return_state.md).

Splitting the strict triangle into residues modulo three yields nine ordinary floor sums. Reversing the horizontal or vertical enumeration gives equivalent Euclidean recursions; the independent checker uses the last-column threshold identity
\[
\sum_{i<n}\left\lfloor\frac{ai+b}{m}\right\rfloor
=nY-\sum_{j<Y}\left\lfloor\frac{mj+m-b+a-1}{a}\right\rfloor,
\quad Y=\left\lfloor\frac{a(n-1)+b}{m}\right\rfloor,
\]
after quotient reduction, with \(a>0\); the \(a=0\) case is immediate. The strict triangle has \(2pq+p+q-1\) points, and the low rows add \(4q+5\), proving \(N=2pq+p+5q+4\). — [CR2](cf_return_state.md), [independent staircase and direct triangle checks](cf_state_audit_check.py).

### Gaps

- Exact examples supplement the all-convergent proof; they do not establish any actual infinite supply of favorable states. The \(O(\log q)\) bound counts Euclidean steps, not unit-cost bit operations on arbitrarily large integers. — [CR1–CR2 and stated gaps](cf_return_state.md).

## Are the Christoffel recurrence and complete nonresonant balance table correct?

### Takeaway

**PASS after two presentation corrections.** The odd recurrence branch needed a missing plus sign, and the unit-coefficient claim required clearing \(1-\omega^{-1}\). The code already used the correct addition; neither correction changes the balance table or subsequent conclusions. — [Corrected CR3–CR4](cf_return_state.md), [independent literal-word and unit checks](cf_state_audit_check.py).

### Cited Findings

- With parent authorization, this audit inserted the missing `+` in display (7) and qualified the coefficient statement before the table. No algorithm or checker in the source was changed. — [Corrected source](cf_return_state.md).
- The independent certificate compares literal continued-fraction word concatenations with direct floor words, validates the cleared imbalance against direct triangle color counts, and checks all six primitive nonresonant residue classes. — [Independent checker](cf_state_audit_check.py).

### Inferences

An east step at horizontal coordinate \(a\) starts after \(a+\lfloor pa/q\rfloor\) letters. Therefore its transform is exactly \(H(p,q)\). For neighboring slopes with determinant one, the lower Christoffel word of the mediant is the lower word followed by the upper word: on each segment the discrepancy from the corresponding rational mesh is strictly less than one mesh spacing. Applying that identity repeatedly gives
\[
H_n=\begin{cases}
G_{a_n}(\rho_{n-1})H_{n-1}+\rho_{n-1}^{a_n}H_{n-2},&n\text{ odd},\\
H_{n-2}+\rho_{n-2}G_{a_n}(\rho_{n-1})H_{n-1},&n\text{ even}.
\end{cases}
\]
The denominator-zero initial endpoint is handled by the explicit first word \(E^{a_1}N\), not by applying the finite-mediant mesh proof at infinity. Resonant phases use \(G_d(1)=d\). — [CR3](cf_return_state.md), [literal-word replay](cf_state_audit_check.py).

Vertical geometric summation proves the displayed formulas for \(S_1,S_2\); the low rows then give (8). Multiplying (8) by \(1-\omega^{-1}\) makes the coefficient of \(H\) a unit for every nonresonant pair. This is the precise normalization: the coefficient in \(W\) itself includes that denominator. Solving the cleared equation and checking the total modulo three gives exactly the four listed balanced classes and excludes \((p,q)\equiv(0,2),(1,0)\). The independent code represents roots by three-color cyclic convolution, independently of the supplied two-coordinate Eisenstein arithmetic. — [CR4](cf_return_state.md), [cleared_imbalance and unit assertions](cf_state_audit_check.py).

The quoted relation to the older axis transform also checks: at the positive endpoint, replacing \(k=0\) by \(k=q\) changes the transform from \(H\) to \(H-1+\omega^{p+q}\). Conjugation and multiplication by \(\omega^2\) give the old \(H_A\). Its negative-side endpoint changes the last exponent to \(p+q-1\). The old center-sum law therefore does not bound the full state individually. — [Older definitions](../infinite-return-construction/skew_denominator.md), [CR4](cf_return_state.md).

### Gaps

- The recurrence is exact but does not prove that the actual logarithmic trajectory visits a desired state infinitely often. — [CR4 gaps](cf_return_state.md).

## Does the bounded-digit countermodel rigorously defeat the generic return dichotomy?

### Takeaway

**PASS.** The two blocks return the full state, not just the convergent residues. Their sparse concatenation is provably transcendental while keeping every later state balanced and every outgoing ratio below four. This defeats the stated inference from transcendence alone. — [CR5–CR6](cf_return_state.md), [independent full-state loop replay](cf_state_audit_check.py).

### Cited Findings

- Starting at the actual prefix through \(12/19\), with current index odd, both \(33\) and \(1323\) return parity, preceding/current residues and both preceding/current transforms. Every intermediate state is nonresonant and meets the full balance table. — [Independent literal-word loop checks](cf_state_audit_check.py).
- The source explicitly evaluates the abstract slope's CF-state map; it does not claim that the fixed \(2,3\) tokens acquire different actual states. Its optional model with ordinary arrivals \(3^{a\beta+b}\) and fixed delay factors \(3/2,9/8\) is consistent on the indicated prefix cylinder. — [CR5 scope paragraph](cf_return_state.md).

### Inferences

The loop assertion extends to every concatenation by induction on blocks because the complete state, including parity, returns. All appended digits are at most three, and \(q_{n-1}<q_n\), so \(q_{n+1}/q_n<4\). There is no hidden resonance between blocks. The counting interpretation for an abstract slope only needs the stated strict low-row inequalities; on the fixed cylinder inside \((3/5,2/3)\), those have positive margins, so the small convergent errors eventually preserve the same cutoffs. — [CR5](cf_return_state.md).

For the sparse construction, let \(m_j\) count digits through the block at position \(j!\). Then \(m_j=2j!+2j+1\) for the stated five-digit prefix, so \(m_{j+1}/m_j\to\infty\). The all-threes-tail approximants \(\beta_j\) are distinct quadratic irrationals with polynomial heights \(O(16^{m_j})\). Agreement through just before the next exceptional block gives error \(O(2^{-m_{j+1}})\). If \(\beta\) were algebraic of degree \(d\), all but finitely many of their quadratic polynomials have nonzero resultant with its minimal polynomial. Isolating the \(\beta\) factor bounds \(|Q_j(\beta)|\) below by \(cH(Q_j)^{-(d-1)}\); the derivative bound on the fixed interval gives \(|\beta-\beta_j|\ge c'H(Q_j)^{-d}\). This contradicts the error estimate for every fixed \(d\). Nonperiodicity alone is not used as a transcendence argument. — [CR6 elementary proof](cf_return_state.md).

### Gaps

- The countermodel is not \(\log_3 2\), and it need not have all arithmetic or quantitative approximation properties of that logarithm. It rules out the generic transcendence/nonperiodicity argument, not a logarithm-specific theorem. — [CR6 scope](cf_return_state.md).
- Neither these state formulas nor the countermodel provides the actual infinite favorable-state supply or the complete affordable nonzero returns required for irrationality. — [Current remaining objective](../adaptive-shape-couplings/REPORT.md).
- Skipped: Lean, installations, external review and broader exploration. Material risk: treating an exact CF-state algorithm or an abstract countermodel as a conclusion about actual infinite return feasibility.
