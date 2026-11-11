# Independent audit of pure guard arithmetic

## Is the positivity-aware approximate occupation criterion sufficient?

### Takeaway

**PASS; no substantive erratum.** AB1–AB2 give a valid sufficient criterion and a correctly scoped obstruction to target-free rational replacements. They construct no integer-affine occupation bridge. — [Audited note](<approximate_bridge.md>), [accepted positive family](<../numerator-and-residuals/occupation_audit.md>).

### Cited Findings

- The accepted actual atom has \(E_n=\nu^H(z_n)>0\) and \(E_n\le6\,2^{-N_n}-3\,3^{-N_n}\). A first-arrival witness \((a_n,b_n)\), \(a_n+b_n=N_n\), contributes \(w_n=2^{-a_n}3^{-b_n}\). The target uses \(Z=2-3Q_{\rm full}(0)\), with all low rows retained separately. — [Accepted normalization and atom theorem](<../numerator-and-residuals/occupation_audit.md>).
- AB1 posits, rather than proves, an integer-affine \(R_n=(u_nZ+v_n)/T_n\), with \(T_n>0\) integer, \(u_n,v_n\) integers, error at most \(\vartheta w_n\), and \(0\le\vartheta<1\). — [AB1](<approximate_bridge.md>).

### Inferences

The witness satisfies \(3^{-N_n}\le w_n\le2^{-N_n}\) and \(E_n\ge w_n\). Consequently
\[
R_n\ge E_n-\vartheta w_n\ge(1-\vartheta)w_n>0,
\qquad
R_n\le E_n+\vartheta w_n\le(6+\vartheta)2^{-N_n}.
\]
If \(T_n2^{-N_n}\to0\), then \(T_nR_n\to0\). Under a hypothetical \(Z=A/B\), the number
\[
BT_nR_n=u_nA+Bv_n
\]
is a positive integer tending to zero. This contradiction needs no separate bound on the size of \(u_n,v_n\). An error bound \(\vartheta3^{-N_n}\) is a conservative sufficient substitute, whereas an absolute error merely tending to zero need not preserve positivity. — [AB1 and complete occupation tail](<approximate_bridge.md>).

For a positive reduced rational replacement \(R_n=r_n/s_n\), one has \(s_n\ge1/R_n\), so the same positivity and upper bound require
\[
s_n\ge\frac{2^{N_n}}{6+\vartheta}.
\]
Every integer multiplier clearing this rational replacement is a multiple of \(s_n\), and its product with \(R_n\) is at least one. This rules out the stated target-free rational replacement as a cheap bridge, even after actual fraction reduction. It says nothing adverse about an as-yet-unproved relation with nonzero \(u_n\). — [AB2](<approximate_bridge.md>).

### Gaps

- No actual \(R_n=(u_nZ+v_n)/T_n\) satisfying these hypotheses is established. This audit accepts the previously audited occupation family as an input; it does not reprove the global finite optimum.
- A rational model atom is not automatically a target-affine approximation. The necessary reduced-denominator bound is not a lower bound on a signed target error. — [Accepted arithmetic limitations](<../numerator-and-residuals/occupation_audit.md>).

## Do pure guards have the claimed simultaneous adequate arithmetic approximants?

### Takeaway

**PASS.** The one-sided models are \(q\)-periodic without a nonresonance assumption, the displayed bound pays the entire discounted tail, and the actual infinite linear-margin supply is proved. Nonzero returns require genuinely nonconstant phase coding; changing contexts are changing target values. — [AB3–AB5](<approximate_bridge.md>), [standalone certificate](<guard_audit_check.py>).

### Cited Findings

- I independently opened the first-party Stanford notes. Theorem 10 appears on PDF page 9 and states the Gelfond–Schneider result for algebraic irrational exponents. The notes are a course by Kannan Soundararajan, typeset by Ian Petrow. — [Theorem 10](https://math.stanford.edu/~ksound/TransNotes.pdf#page=9).
- The supplied checker passes its three actual current/successor pairs, all nine three-floor cell guards, complete tail comparisons, and both correlations. The independent checker imports no project module and also passes. — [Supplied checker](<approximate_bridge_check.py>), [independent checker](<guard_audit_check.py>).

### Inferences

Let \(S\) be finite, nonempty and contained in the positive integers, \(s_*=\max S\), and let \(f\) be Boolean. For \(\alpha=\log2/\log3\), define
\[
g_n=f\bigl((\lfloor(3n+s)\alpha\rfloor\bmod3)_{s\in S}\bigr),
\qquad G_f=\sum_{n\ge0}8^{-n}g_n.
\]
For a convergent \(p/q\) with immediate successor \(P/Q\), set \(\sigma=\operatorname{sign}(\alpha-p/q)\). At positive \(k\), the prescribed rational floor is
\[
\lfloor kp/q\rfloor_\sigma
=\lfloor kp/q\rfloor-\mathbf1_{\{\sigma<0,\ q\mid k\}}.
\]
It can equivalently be evaluated as \((kp-\mathbf1_{\{\sigma<0\}})\mathbin{//}q\). Increasing \(n\) by \(q\) adds \(3p\) to each floor and preserves the tie test, proving exact \(q\)-periodicity of \(\widehat g_n\). Positive offsets ensure that no undefined lower-sided index-zero override is being periodized. Hence
\[
\widehat G_f=
\frac{\sum_{r=0}^{q-1}8^{-r}\widehat g_r}{1-8^{-q}},
\qquad D_q\widehat G_f\in\mathbb Z,\quad D_q=8^q-1.
\tag{A1}
\]
Neither this identity nor its proof uses \(p+q\not\equiv0\pmod3\). — [AB3](<approximate_bridge.md>).

The endpoints \(p/q,P/Q\) are Farey neighbors. A floor discrepancy at a positive \(k<q+Q\), apart from the correctly sided endpoint tie, would put an interior rational of denominator below \(q+Q\) between the endpoints. Thus all actual and rational code coordinates agree for
\[
0\le n<m,\qquad
m=\left\lfloor\frac{q+Q-1-s_*}{3}\right\rfloor+1
=\left\lceil\frac{q+Q-s_*}{3}\right\rceil,
\]
when \(m>0\). Boolean range bounds the remaining difference by the full geometric tail. Since \(m\ge(q+Q-s_*)/3\),
\[
|G_f-\widehat G_f|\le\frac87\,8^{-m},
\qquad
D_q|G_f-\widehat G_f|
\le\frac87\,2^{s_*+2q-Q}.
\tag{A2}
\]
The bound is uniform in the Boolean function and number of code labels because it uses only the common coordinate prefix and a difference bounded by one. It retains the full \(n=0\) term in A1. — [AB3 and independent complete-period calculation](<guard_audit_check.py>).

For the actual number, prime valuations exclude rational \(\alpha\). If it were algebraic irrational, Gelfond–Schneider with base 3 would make \(3^\alpha\) transcendental, contradicting \(3^\alpha=2\). Thus it is nonquadratic. An eventually all-one continued-fraction tail equals the golden-ratio tail followed by a finite integer Möbius transformation, and is quadratic irrational; the actual continued fraction cannot have that form. — [Checked external theorem](https://math.stanford.edu/~ksound/TransNotes.pdf#page=9), [audited specialization AB4](<approximate_bridge.md>).

Here is the automatic supply proof, reconstructed without an unbounded-partial-quotient assumption. If \(a_{n+1}\ge3\) infinitely often, then \(Q-2q\ge q+q_{n-1}>q/3\) at those indices. Otherwise the tail digits are at most two and digits two occur infinitely often. At those late indices,
\[
q=a_nq_{n-1}+q_{n-2}<3q_{n-1},
\qquad Q-2q=q_{n-1}>q/3.
\tag{A3}
\]
This proves an actual infinite subsequence with A3, regardless of resonance. Fixed contexts therefore have cleared error tending to zero. The same holds uniformly for contexts with \(s_*=o(q)\), and even changing Boolean functions, because \(s_*+2q-Q\le o(q)-q/3\to-\infty\). Such changing codes define changing numbers \(G_f\), not one fixed density target. No occupation first-arrival or positivity budget follows from A2 alone. — [AB4](<approximate_bridge.md>).

For the nonzero assertion, the phase function
\[
\varphi(x)=f\bigl((\lfloor3x+s\alpha\rfloor\bmod3)_{s\in S}\bigr)
\]
is a finite step function. If its orbit code were eventually periodic of period \(d\), density of \(\{n\alpha\}\), away from finitely many discontinuities, would give \(\varphi(x)=\varphi(x+d\alpha)\) at all common continuity points. A genuinely nonconstant finite step function has a nonempty finite essential boundary, which this equality would make invariant under an irrational rotation. That is impossible. The base-eight digits are zero or one, so rationality would imply eventual periodicity of this unambiguous expansion. Therefore \(G_f\) is irrational and every rational model in A1 differs from it. Constants and functions varying only on isolated boundary points are excluded. This does not imply rational independence of multiple guard values. — [AB5 and exact guard irrationality proof](<exact_transport.md>).

### Gaps

- Gelfond–Schneider is an established external input, not reconstructed here. The source statement and the positive-real specialization were checked.
- Adequate returns for \(G_f\) are not returns for \(Z\) or \(\nu^H(z)\). No rational-affine relation between those quantities has been proved. A growing context also carries its explicit \(s_*\) cost. — [AB5–AB6 limitations](<approximate_bridge.md>).

## Do periodic replacement and the actual correlation checks respect the state dependence?

### Takeaway

**PASS.** Periodic guard replacement leaves unknown decimated actual-state readouts. Both actual correlation intervals reproduce from original-board data and complete tails, so the scalar-factorization shortcut fails. Neither result excludes general target-dependent cancellation. — [AB6–AB7](<approximate_bridge.md>), [independent checker](<guard_audit_check.py>).

### Cited Findings

- The independent checker obtains actual floors from rigorous rational logarithm intervals using a separate Horner evaluation of the atanh series, rather than the companion integer-power floor sequence. Continued-fraction interval extraction confirms the three actual pairs below; integer powers separately confirm the one-sided signs. — [Independent implementation](<guard_audit_check.py>).
- The independent original-board routine counts each color arithmetically within each ternary row; it does not import the companion axis or skew recurrence. It evaluates cone births by differences of minima. — [Standalone board construction](<guard_audit_check.py>).

### Inferences

For every bounded actual-state readout \(h_n\), the same full tail yields
\[
\left|\sum8^{-n}(g_n-\widehat g_n)h_n\right|
\le\frac87\|h\|_\infty8^{-m}.
\]
Regrouping the other sum is exact:
\[
\sum_{n\ge0}8^{-n}\widehat g_nh_n
=\sum_{r=0}^{q-1}8^{-r}\widehat g_r
\underbrace{\sum_{k\ge0}8^{-qk}h_{r+kq}}_{H_{q,r}}.
\tag{A4}
\]
The \(H_{q,r}\) remain actual state/cone values. If \(h_n=1\) they are the rational geometric factor; for a general state readout neither that substitution nor rationality is justified. The independent checker also finds \(A_{3\cdot1054}\ne A_0\) at the named resonant current, despite the \(q\)-periodic rational guard code. — [AB6 and independent state check](<guard_audit_check.py>).

For the phase guard \(g_n=\mathbf1_{\{\lfloor(3n+1)\alpha\rfloor\equiv0(3)\}}\), take separately \(h_n=\mathbf1_{\{A_{3n}=1\}}\) and \(h_n=F(A_{3n}-1)\). Let \(\Omega(h)=\sum8^{-n}h_n\), of total mass \(8/7\). The independent 28-term original-board calculation, with each complete tail \(\tau=(8/7)8^{-28}\), bounds
\[
\Omega(gh)-\frac{\Omega(g)\Omega(h)}{8/7}.
\]
If the three computed heads are \(J,G,H\), safe bounds are
\[
J-\frac{(G+\tau)(H+\tau)}{8/7}
\quad\hbox{and}\quad
J+\tau-\frac{GH}{8/7}.
\]
For both readouts these lie strictly inside \((1/10,1/6)\). The normalization is therefore correct, all marginal and joint tails are paid, and the assertion concerns the actual infinite sums. It refutes that particular independence factorization. — [Independent full interval certificate](<guard_audit_check.py>).

Both supplied and independent checkers pass. The standalone test also checks two positive contexts at each named case, all realized Boolean-cell indicator labels, full rational period values and exact nonzero intervals:

| Current / successor | Resonant current | Matching length for \(S=\{1,2,3\}\) |
|---|---:|---:|
| \(12/19,\ 41/65\) | no | 27 |
| \(53/84,\ 306/485\) | no | 189 |
| \(665/1054,\ 15601/24727\) | yes | 8593 |

The script imports no project helper and uses only integers and fractions. These finite checks certify the definitions and actual examples; A1–A3 and the nonperiodicity proof establish the infinite statements. — [Supplied certificate](<approximate_bridge_check.py>), [standalone certificate](<guard_audit_check.py>).

### Gaps

- **Final disposition: PASS; no substantive erratum found.** The approximate occupation bridge is still unconstructed. State/phase correlations, unknown decimated readouts and possible target-dependent cancellation remain distinct from the solved pure-guard approximation problem.
- Skipped Lean, external review, a full reproof of the transcendence theorem and further filter searches. Material risk: promoting adequate phase-only arithmetic returns, or target-free rational replacements, into an adequate infinite arithmetic return for the density.
