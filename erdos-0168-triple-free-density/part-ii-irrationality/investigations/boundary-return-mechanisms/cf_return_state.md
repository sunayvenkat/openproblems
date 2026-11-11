# Exact continued fraction return states

## What is the actual state before the critical three arrivals?

### Takeaway

**The full pre-state has an exact rational-triangle formula, not merely a numerical approximation.** For every sufficiently late actual convergent \(p/q\) of \(\alpha=\log_3 2\), it is computable in \(O(\log q)\) Euclidean steps. The total count is \(2pq+p+5q+4\); this alone already explains why the actual \(306/485\) progression cannot be a balanced reset. — [Standalone certificate](cf_return_state_check.py).

### Cited Findings

- The accepted token at \((a,b)\) has color \(a-b\bmod3\), ordinary arrival \(2^a3^b\), dyadic factor \(3/2\) for \(a\ge1\), and row-one factor \(9/8\) for \(a\ge2\). The endpoint \(27/2\) is retained. — [Prior independently audited definitions](../adaptive-shape-couplings/adaptive_structure.md).
- Independent integer-time row counting agrees with both new Euclidean formulas at the five actual pairs below. No floating logarithms, event sort, optimizer, or imported companion checker is used. — [Functions actual_counts, rational_prestate and transform_prestate](cf_return_state_check.py).

| \(p/q\) | Counts before the first critical arrival |
|---|---|
| \(5/8\) | \(43,43,43\) |
| \(12/19\) | \(189,189,189\) |
| \(41/65\) | \(1900,1900,1900\) |
| \(53/84\) | \(3127,3127,3127\) |
| \(306/485\) | \(99852,99851,99852\) |

### Inferences

**CR1. Exact actual-to-rational comparison.** Put \(u=2^q,v=3^p\). Suppose \(p/q\) is an actual convergent and
\[
3\max(u^2,v^2)<4\min(u^2,v^2).
\tag{1}
\]
This holds eventually because the logarithmic errors tend to zero. The three critical points are
\[
(0,2p+2),\quad(q,p+2),\quad(2q,2),
\]
at times \(9v^2,9uv,9u^2\). Before their first arrival, the arrived high-row points are exactly
\[
\{(a,b):a\ge0,\ b\ge2,\ pa+q(b-2)<2pq\}.
\tag{2}
\]
The dyadic row consists of \(0\le a\le2q+2\), and row one of \(0\le a\le2q+1\). No other token arrives between the first and last critical times, inclusively.

Here is a proof, including the needed approximation property. Write \(\delta=q\alpha-p\). For an ordinary point, its logarithmic distance from the middle critical time, in units of \(\log3\), is
\[
d=(a-q)\alpha+(b-p-2)=h\alpha+k.
\]
Condition (1) excludes \(a>2q\), \(b\ge2\), from the critical interval and gives all small-error bounds used below. For \(0<|h|<q\), the convergent best-approximation property gives \(|h\alpha+k|>|\delta|\). To see that property directly, express \((h,-k)\) in the unimodular basis formed by the current and preceding convergents. Their errors have opposite signs. Mixed-sign coefficients add the magnitudes of their errors; same-sign nonnegative coefficients either have denominator at least \(q\), or are a positive multiple of the preceding vector, whose error is larger. This proves the strict inequality for \(0<|h|<q\).

Moreover \(|\delta|<1/q_{\mathrm{next}}<1/q\), so the sign of \(h\alpha+k\) agrees with the sign of \(hp/q+k\) whenever \(|h|<q\) and the latter is nonzero. It follows that (2) describes exactly the points before the interval. The rational equality line has only the three listed points, since \(\gcd(p,q)=1\). The cases \(h=0,\pm q\) give precisely those points.

For the low rows, divide arrival times by \(9u^2\). The last included and first excluded dyadic times have ratios \(2/3,4/3\), respectively; row one has ratios \(3/4,3/2\). Condition (1) separates these from the entire critical interval. The finite untimed row-one points \((0,1),(1,1)\) are already below it. This proves the actual statement without ignoring the delays. — [Integer comparisons and independent row counts](cf_return_state_check.py).

**CR2. Euclidean formula for all three counts.** Let
\[
F(p,q,L)=\#\{x,y\ge0:px+qy\le L\},\qquad F=0\ (L<0).
\]
For \(L\ge0\), put \(n=\lfloor L/p\rfloor+1,\ r=L-p(n-1)\). Then
\[
F(p,q,L)=n+\sum_{i=0}^{n-1}\left\lfloor\frac{pi+r}{q}\right\rfloor.
\tag{3}
\]
The floor sum \(f(n,m,a,b)\) is evaluated by removing integer quotients of \(a,b\), adding their explicit linear/quadratic contributions, and, for reduced \(0\le a,b<m\), replacing
\[
(n,m,a,b)\longmapsto
\left(\left\lfloor\frac{an+b}{m}\right\rfloor,\ a,\ m,\ (an+b)\bmod m\right).
\]
This is the transposition of the integer points under the corresponding staircase. The modulus follows the Euclidean algorithm; the certificate implements it and checks the identity against direct sums.

Split \(a=3x+r,\ b-2=3y+s\). The high-row contribution to color \(j\) is
\[
\sum_{\substack{0\le r,s<3\\r-s-2\equiv j\ (3)}}
F\!\left(p,q,\left\lfloor\frac{2pq-pr-qs-1}{3}\right\rfloor\right).
\tag{4}
\]
Add the two explicitly bounded low rows from CR1. This gives the exact actual pre-state in nine \(O(\log q)\) floor sums.

The strict triangle has \(2pq+p+q-1\) points. Indeed it splits into a \(q\)-by-\(p\) rectangle and two translates of the strict triangle \(pa+qb<pq\); reflection pairs its non-axis interior points, giving \((pq+p+q-1)/2\) points in the smaller triangle. The low rows add \(4q+5\). Hence
\[
N_{\mathrm{pre}}=2pq+p+5q+4.
\tag{5}
\]
For nonresonant \(p+q\not\equiv0\pmod3\), the three critical arrivals have three different colors, so the post-state is the pre-state plus \((1,1,1)\). A forced balanced reset occurs exactly when the pre-state is balanced. — [Exact total and independent formula replay](cf_return_state_check.py).

### Gaps

- Formula (5) is only a necessary congruence test for balance. Full balance requires the weighted state below.
- No formula here establishes infinitely many favorable states of the actual logarithmic slope. The comparison is exact, but state supply is a separate theorem. — [Remaining infinite-return obligation](../adaptive-shape-couplings/REPORT.md).

## Is there a genuine continued fraction recursion for the full weighted state?

### Takeaway

**Yes.** One Christoffel-word transform and the current/preceding residues give the exact state. The old bounded three-center identity does not replace this full transform. — [Independent floor-sum and Christoffel checks](cf_return_state_check.py), [older center law](../infinite-return-construction/skew_denominator.md).

### Cited Findings

- The older nonresonant center law controls \(c_A+c_B\) and high-column skew covariance; it does not assert that \(c_A\), \(c_B\), or the actual full pre-state form a finite alphabet. — [Exact center calculation and scope](../infinite-return-construction/skew_denominator.md).
- The certificate checks the recurrence below against direct weighted words and all three color counts for small coprime pairs, then against independent actual-time counts at the five specified convergents. — [Standalone checks](cf_return_state_check.py).

### Inferences

**CR3. Christoffel transform.** Let \(\omega^2+\omega+1=0\), \(G_k(z)=\sum_{i=0}^{k-1}z^i\), and
\[
H(p,q)=\sum_{a=0}^{q-1}\omega^{a+\lfloor pa/q\rfloor}.
\tag{6}
\]
Use the lower Christoffel word from \((0,0)\) to \((q,p)\): after the \(a\)-th east step, take enough north steps to reach \(\lfloor p(a+1)/q\rfloor\). The east-step starting positions are precisely \(a+\lfloor pa/q\rfloor\), so (6) is their transform.

For words \(U,V\), let \(\rho(U)=\omega^{|U|}\). Concatenation gives
\[
H(UV)=H(U)+\rho(U)H(V),\quad
H(U^d)=G_d(\rho(U))H(U).
\]
If two neighboring reduced slopes have determinant one, the lower Christoffel word of their mediant is the word of the lower slope followed by that of the upper slope. A direct floor proof suffices: on the first denominator-length segment the mediant line is displaced by less than one denominator mesh; on the remaining segment its excess over the translated upper line is \((1-t/q_2)/(q_1+q_2)<1/q_2\). Both floors are unchanged.

Write \(\alpha=[0;a_1,a_2,\ldots]\), with convergents indexed by \(p_0/q_0=0/1\), and put \(\rho_n=\omega^{p_n+q_n}\), \(H_n=H(p_n,q_n)\). Start with \(H_{-1}=0,H_0=1,\rho_{-1}=\rho_0=\omega\). The mediant rule gives
\[
H_n=
\begin{cases}
G_{a_n}(\rho_{n-1})H_{n-1}
 +\rho_{n-1}^{a_n}H_{n-2},&n\text{ odd},\\
H_{n-2}+\rho_{n-2}G_{a_n}(\rho_{n-1})H_{n-1},&n\text{ even},
\end{cases}
\tag{7}
\]
with \(\rho_n=\rho_{n-1}^{a_n}\rho_{n-2}\). This is an exact \(O(\log q)\) recurrence in Eisenstein integers, including resonant steps: when \(\rho=1\), \(G_d(\rho)=d\), not zero.
The first word is explicitly \(E^{a_1}N\); this covers the initial denominator-zero endpoint without applying the finite-mediant floor argument there.

**CR4. Recovering the actual imbalance.** Let \(S_1\) be the weighted strict triangle \(pa+qb<pq\), \(S_2\) the weighted strict triangle \(pa+qb<2pq\), with weight \(\omega^{a-b}\). Summing vertical geometric series and using the rectangle-plus-two-triangles split gives
\[
S_1=\frac{G_q(\omega)-\omega^{-p}H(p,q)}{1-\omega^{-1}},
\qquad
S_2=G_q(\omega)G_p(\omega^{-1})
+(\omega^q+\omega^{-p})S_1.
\]
Consequently the actual precritical imbalance is
\[
W=\omega S_2+G_{2q+3}(\omega)+\omega^{-1}G_{2q+2}(\omega).
\tag{8}
\]
If \(W=u+v\omega\), the counts follow from (5):
\[
C_2=(N-u-v)/3,\quad C_0=C_2+u,\quad C_1=C_2+v.
\]
The apparent division in \(S_1\) is exact in the Eisenstein ring for the word transform. The checker reconstructs this independently of (4).

For nonresonant pairs, multiplying (8) by \(1-\omega^{-1}\) makes the coefficient of \(H\) an Eisenstein unit. Solving \(W=0\), with the necessary \(N\equiv0\pmod3\), gives the complete balance table:

| \(p\bmod3,q\bmod3\) | Required \(H\) |
|---|---|
| \(0,1\) | \(1\) |
| \(1,1\) | \(1\) |
| \(2,0\) | \(2+\omega\) |
| \(2,2\) | \(2\) |

The other nonresonant primitive classes \((0,2),(1,0)\) have \(N\not\equiv0\) and cannot be balanced.

This transform is related to the older axis sum rather than contradicted by its three-center law. With ordinary positive-side endpoint convention,
\[
H_A=\omega^2\,\overline{H-1+\omega^{p+q}};
\]
the negative-side convention replaces the last exponent by \(p+q-1\). The old law constrains a combination of axis transforms, not \(H\) by itself. — [Definitions and one-sided endpoints](../infinite-return-construction/skew_denominator.md), [exact recurrence certificate](cf_return_state_check.py).

### Gaps

- The recurrence is exact at the actual slope but is not a proof that its trajectory visits any prescribed state infinitely often.
- Resonance and full state must be retained. Ignoring either can turn a false generic supply assertion into an apparently finite residue argument.

## Does transcendence force an escape state or a large approximation gap?

### Takeaway

**No, even the proposed dichotomy is false if it uses only generic transcendence.** There is a transcendental abstract slope sharing the actual prefix through \(12/19\), with every later state under (4)/(8) balanced and nonresonant and every outgoing denominator ratio less than four. This is a countermodel to that inference, not a claim about the actual \(\log_3 2\). — [Two exact full-state loops](cf_return_state_check.py).

### Cited Findings

- At the actual prefix \([0;1,1,1,2,2]\), the last two pairs have residues/transforms
\[
(p_4,q_4,H_4)\equiv(2,2,2),\quad
(p_5,q_5,H_5)\equiv(0,1,1),
\]
with current index odd. The two appended blocks
\[
A=(3,3),\qquad B=(1,3,2,3)
\tag{9}
\]
return this entire state exactly, including parity and both preceding/current transforms. — [Hardcoded loop replay](cf_return_state_check.py).

### Inferences

**CR5. Explicit balanced avoidance loops.** The current states after each digit are:

| Block | Intermediate current \((p\bmod3,q\bmod3,H)\) |
|---|---|
| \(A\) | \((2,2,2)\), \((0,1,1)\) |
| \(B\) | \((2,0,2+\omega)\), \((0,1,1)\), \((2,2,2)\), \((0,1,1)\) |

Every row is nonresonant and satisfies the complete table above. Formula (7) proves the return, so arbitrary infinite concatenations of \(A,B\) preserve balance at every later convergent. All digits are at most three; hence
\[
\frac{q_{n+1}}{q_n}=a_{n+1}+\frac{q_{n-1}}{q_n}<4.
\tag{10}
\]
Thus there need be neither infinitely many unbalanced escape states nor infinitely many outgoing ratios exceeding five.

The state assertion evaluates the exact map (4)/(8) on the abstract slope's convergents; it does not run the fixed \(2,3\) tokens at a different slope. If desired, it also has a direct counting interpretation with ordinary arrivals \(3^{a\beta+b}\) and the same two delay factors. For \(\beta\in(3/5,2/3)\), the strict inequalities \(3^{2\beta}<6<3^{3\beta}\) and \(3^\beta<8/3<3^{2\beta}\) give the same low-row cutoffs eventually, and the convergent comparison proof otherwise applies unchanged.

**CR6. A transcendental member, with an elementary proof.** Choose block \(B\) at block positions \(j!\), \(j\ge3\), and \(A\) elsewhere. Let the resulting slope be \(\beta\). Its fixed prefix places it inside \((3/5,2/3)\). Let \(m_j\) be the number of CF digits through the \(B\) at position \(j!\), and let \(\beta_j\) have that prefix followed entirely by threes. Then \(m_{j+1}/m_j\to\infty\). The numbers \(\beta_j\) are distinct quadratic irrationals, since their tails are Möbius transforms of the root of \(x^2-3x-1\).

All digits are at most three, so the prefix denominator is at most \(4^{m_j}\). Eliminating the quadratic tail gives an integer quadratic \(Q_j\) with
\[
Q_j(\beta_j)=0,\qquad H(Q_j)\le C16^{m_j}.
\]
The two expansions agree up to just before the next \(B\); since \(q_{n+2}\ge2q_n\),
\[
|\beta-\beta_j|\le C2^{-m_{j+1}+4}.
\tag{11}
\]
The harmless additive constant also absorbs the fixed prefix.

Suppose \(\beta\) were algebraic of degree \(d\), with minimal polynomial \(P\). For all but finitely many distinct \(\beta_j\), \(Q_j(\beta)\ne0\): otherwise infinitely many \(\beta_j\) would be roots or conjugates of the same degree-at-most-two algebraic number. The nonzero integer resultant gives
\[
|Q_j(\beta)|\ge c(P)H(Q_j)^{-(d-1)}.
\]
Indeed all other conjugate factors are \(O_P(H(Q_j))\). On the fixed real interval, \(|Q_j'|=O(H(Q_j))\), and the mean-value theorem therefore gives
\[
|\beta-\beta_j|\ge c'(P)H(Q_j)^{-d}\ge c''(P)16^{-dm_j}.
\tag{12}
\]
Equations (11)–(12) contradict \(m_{j+1}/m_j\to\infty\). Hence \(\beta\) is transcendental. This proof uses no unproved distribution property or irrationality-measure assumption.

### Gaps

- The countermodel concerns the exact CF return-state map, and generic arguments based on transcendence/nonperiodicity plus that map. It is not the actual logarithmic slope and need not share every quantitative or arithmetic property of that slope.
- A logarithm-specific infinite state-supply theorem, or a construction that handles the balanced states as well, is still needed. Neither (7) nor the countermodel supplies an adequate arithmetic return.
- Skipped: Lean, installations, external review, priority claims, and archived edits. Risk: confusing an exact state algorithm with actual infinite favorable-state supply, or using an abstract countermodel as a no-go theorem for \(\log_3 2\).
