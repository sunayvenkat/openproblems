# Ordered first exits give rational complete sources

## Can renewal stopping rationalize the complete target while preserving positivity?

### Takeaway

**Yes, with positivity after the complete occupation pairing.** Ordered one-axis Dirichlet problems produce, for every integer state radius, a finite rational-step source for the full density, including all low rows, and a strictly positive residual tending to zero. This is a different construction from the unrestricted coupled Dirichlet solution: it deliberately permits a signed pointwise interface, whose complete pairing is positive. Affordable reduced denominators remain unproved. — [Exact construction and checker](renewal_check.py), [accepted transport](../occupation-arithmetic-bridge/exact_transport.md).

### Cited Findings

- The actual commuting lifts have discounted resolvents with bases 8 and 27; their full adjoint factors as \(\mathcal L=(8I-U_A)(27I-U_B)\). The high source has nine terms and the low source twelve separate terms. The target is \(Z=2-3Q_{\rm full}(0)\). — [ET1–ET8](../occupation-arithmetic-bridge/exact_transport.md), [independent normalization audit](../occupation-arithmetic-bridge/transport_audit.md).
- Uniform finite horizontal exit, including one-sided phase itineraries, is already proved; finite common refinements must retain reward cuts. The accepted exact actual axis relation is \(A_a=\omega^{-a}\mathcal K(2^a)\). — [Finite-exit audit](../finite-volume-calibration/calibration_audit.md), [original-board and actual-orbit audit](../numerator-and-residuals/occupation_audit.md).
- The accepted Kesten criterion concerns the discrepancy at a fixed starting point: an interval of length \(\ell\) has bounded discrepancy under irrational rotation by \(\theta\) exactly when \(\ell\in\mathbb Z\theta+\mathbb Z\). — [Primary Kelly–Sadun Theorem 1 and proof](https://arxiv.org/html/1404.0455), [accepted independent application](../numerator-and-residuals/occupation_audit.md).

### Inferences

**R1. The actual vertical axis also escapes every finite box.** This is proved from original column sums, rather than assumed from horizontal escape. Let
\[
\mathcal K(t)=\sum_{2^a3^b\le t}\omega^{a-b},\qquad
\alpha=\log_3 2,\quad \beta=1/\alpha.
\]
Partitioning the board into its bottom row and the points divisible by three gives \(\mathcal K(3^b)=\omega^{-1}\mathcal K(3^{b-1})+\sum_{a=0}^{\lfloor b\beta\rfloor}\omega^a\). After multiplying by \(\omega^{-2b}\), this is exactly the accepted recurrence for \(B_b\), with the same initial value. Thus \(B_b=\omega^{-2b}\mathcal K(3^b)\), hence \(B_{3m}=\mathcal K(3^{3m})\). Put \(L_m=\lfloor3m/\alpha\rfloor\). In column \(a\), the final vertical index is \(3m-\lceil\alpha a\rceil\). Its geometric color sum yields exactly
\[
(1-\omega^{-1})B_{3m}
=\sum_{a=0}^{L_m}\omega^a
-\omega^{-1}\sum_{a=0}^{L_m}\omega^{\lceil(\alpha+1)a\rceil}.       \tag{R1}
\]
The first sum is uniformly bounded. For positive \(a\), with \(\theta=(\alpha+1)/3\), the second summand takes values \(\omega,\omega^2,1\) on the successive thirds of \(\{a\theta\}\). No positive iterate is an endpoint. Its real part is \(3/2\) times the discrepancy of the final third. Since \(\theta\) is irrational and \(1/3\notin\mathbb Z\theta+\mathbb Z\), the accepted fixed-start Kesten criterion makes that discrepancy unbounded. The sequence \(L_m\) has bounded gaps; indeed \(3/2<\beta<5/3\) follows from \(2^3<3^2\) and \(3^3<2^5\), so the gaps are four or five. Bounded increments show that sampling only these indices preserves unboundedness. Thus the precise actual \(B_{3m}\) is unbounded. The checker verifies (R1) against original boards for \(m=0,\ldots,12\); those samples check the formula, while Kesten supplies the infinite conclusion. — [Exact check](renewal_check.py), [primary criterion](https://arxiv.org/html/1404.0455).

The all-phase and uniform-exit upgrade is the same elementary argument as the accepted horizontal proof. For the vertical drift \(\Xi_3(v)\), a bounded orbit at one phase would bound the cocycle at all its translates; density and continuity of each finite sum at zero would bound the actual phase-zero orbit. The genuine drift cuts are \((k-s\beta)/3\), \(s=1,2,3\), and no nonnegative orbit of zero hits them. A phase orbit hits at most one drift cut; hence either one-sided limiting itinerary differs from the actual one by only a bounded eventual displacement. All are unbounded. Compactness of one-sided itineraries now gives a uniform finite exit time from every finite state box. For the full high state, the extra terms \(\Psi_i(x),\Xi_j(v),C_{ij},e_j(v)\) are uniformly bounded finite-step corrections, and the other axis is frozen. Staying in a fixed \(\rho\)-box would bound the corresponding pure-axis cocycle. Their extra finite cut families are included in the common refinement and do not change the escape argument. The same reasoning applies to the fixed low-row offsets. — [Accepted compactness proof to which this is applied](../finite-volume-calibration/calibration_audit.md), [actual lifted state formulas](../occupation-arithmetic-bridge/exact_transport.md).

**R2. Ordered Dirichlet construction.** Fix one actual high residue block and write its Boolean target as \(h\). Let \(\zeta\) be its full state and
\[
\rho(x+y\omega)=\max(|y-x|,|x|),\qquad D_R=\{\rho(\zeta)\le R\}.
\]
Define \(q_R\) by the horizontal problem
\[
(8I-U_A)q_R=h\quad\hbox{in }D_R,
\qquad q_R=(1+h)/7\quad\hbox{outside }D_R.                  \tag{R2}
\]
At a point whose horizontal first exit is \(a\), its exact value is
\[
q_R=\sum_{n<a}8^{-n-1}h\circ T_A^n
       +8^{-a}(1+h\circ T_A^a)/7.                         \tag{R3}
\]
This formula includes \(a=0\). Uniform horizontal exit proves that it is a finite rational-step function on a common phase refinement, with \(0\le q_R\le2/7\). Set \(e_A=(8I-U_A)q_R-h\). It vanishes inside and satisfies
\[
6/7\le e_A\le9/7\quad\hbox{outside}.                    \tag{R4}
\]
These inequalities include re-entry: outside, \(e_A=(8+h)/7-q_R\circ T_A\).

Next define \(p_R\) by the vertical problem
\[
(27I-U_B)p_R=q_R\quad\hbox{in }D_R,
\qquad p_R=(1+q_R)/26\quad\hbox{outside }D_R.              \tag{R5}
\]
At vertical first exit \(t\),
\[
p_R=\sum_{m<t}27^{-m-1}q_R\circ T_B^m
       +27^{-t}(1+q_R\circ T_B^t)/26.                    \tag{R6}
\]
Uniform vertical exit and the finite refinement of \(q_R\) prove that this is again finite rational-step. Pulled-back reward cuts in both phase coordinates must be included. No finite invariant phase partition or terminating arbitrary alternating path is asserted. Positivity and a geometric sum give \(0\le p_R\le9/182\). With \(e_B=(27I-U_B)p_R-q_R\),
\[
e_B=0\quad\hbox{inside},\qquad
90/91\le e_B\le191/182\quad\hbox{outside}.                \tag{R7}
\]
Indeed outside, \(e_B=(27+q_R)/26-p_R\circ T_B\). All constants are uniform in \(R\). — [Exact formulas and residual checks](renewal_check.py).

**R3. The signed interface disappears under the correct pairing.** Algebra gives
\[
\mathcal Lp_R=h+e_A+(8I-U_A)e_B.                           \tag{R8}
\]
The last term need not be pointwise nonnegative. This is intentional. For the complete block measure \(W_j=\Omega\otimes\Pi_j\), the exact horizontal resolvent gives
\[
W_j((8I-U_A)e_B)
=8\,\Pi_j\bigl(e_B(1,\cdot,0,\cdot)\bigr)\ge0.          \tag{R9}
\]
There is no unknown hybrid in (R9): it is a positive residual, rather than a proposed rational constant. The source \(p_R\) itself has a proved finite rational formula. Boundedness justifies every infinite telescoping limit. Finite rectangles have the three terminal edges/corner of ET6; the checker retains and verifies them explicitly. — [Accepted ET6](../occupation-arithmetic-bridge/exact_transport.md), [exact terminal check](renewal_check.py).

Apply (R2) separately to each of the twelve low kernels; there is no vertical shift of a low kernel. With \((b_0,b_1,b_2)=(6,4,5)\), assemble
\[
S_R=216\sum_{i,j=0}^2 2^{-i}3^{-b_j}
 p_{ij,R}(1,V_{m_j},0,v_{m_j})
 +8\sum_{i=0}^2\sum_{b=0}^3 2^{-i}3^{-b}q_{i,b,R}(1,0).     \tag{R10}
\]
Every term of \(S_R\) is rational by the finite formulas above. Complete high and low pairing gives
\[
S_R=Q_{\rm full}(0)+\Psi_R,\qquad
Z=2-3S_R+3\Psi_R,\qquad \Psi_R>0.                          \tag{R11}
\]
Here \(\Psi_R\) is the sum of all \(e_A\) occupation integrals, plus the positive line integrals (R9). It is strictly positive for every radius because the actual high occupation has infinite support and \(e_A\ge6/7\) at every occupied exterior state. The exceptional original birth is already included in the constant two, exactly once. — [Complete target normalization](../numerator-and-residuals/occupation_audit.md), [infinite support and height-tail audit](../finite-volume-calibration/exterior_audit.md), [assembled finite source check](renewal_check.py).

**R4. Full residual tail.** The \(e_B\) line is a subset of physical indices \(a=i\), \(i=0,1,2\). Its factor eight in (R9) is retained. Consequently
\[
0<\Psi_R\le\left(\frac97+8\frac{191}{182}\right)
  \sum_{\rho(\zeta_{a,b})>R}2^{-a}3^{-b}
=\frac{881}{91}\sum_{\rho(\zeta_{a,b})>R}2^{-a}3^{-b}.       \tag{R12}
\]
The low rows use their own state formulas in this sum. The accepted complete state-height bound, enlarged by finitely many low offsets, gives fixed \(C_\rho>0\), \(0<\kappa<1\), and \(m_R=\max(0,\lfloor(R/C_\rho)^{1/\kappa}\rfloor)\) such that
\[
0<\Psi_R\le\frac{881}{91}(6\,2^{-m_R}-3\,3^{-m_R})
\le\frac{5286}{91}2^{-m_R}\longrightarrow0.                 \tag{R13}
\]
Thus every radius gives a positive complete real return with a **rational** comparison source. This settles rational source existence for this ordered family, not cheap clearing. — [Accepted full tail and state-height inputs](../finite-volume-calibration/exterior_audit.md).

### Gaps

- There is no proof that the reduced denominator of \(S_R\) times \(\Psi_R\) tends to zero along an infinite sequence. The actual checked examples fail this condition badly. — [Arithmetic analysis and exact checker](renewal_check.py).
- This construction does not prove rationality of the *previous* unrestricted coupled Dirichlet source, or pointwise positivity of its own complete product residual. It supplies a different rational source with proved paired positivity. — [Distinction from previous construction](../finite-volume-calibration/exterior_audit.md).

## What is the complete denominator cost, including the nine high and twelve low sources?

### Takeaway

A common clear factor is explicit, but it is provably inadequate without substantial gcd saving. The necessary saving is quantified for the **whole source**, rather than inferred from one local term. Exact actual radii zero, one and two show only small gcd cancellation and huge cleared positive errors. — [Exact reduced-source arithmetic](renewal_check.py).

### Cited Findings

- At one high source, let \(t\) be its vertical first exit; for \(m<t\), let \(a_m\) be the horizontal exit at \(T_B^m\xi_0\). Write
  \[
  q_m=\frac{N_m}{7\,8^{a_m}},\qquad
  N_m=1+h_{m,a_m}+7\sum_{n<a_m}8^{a_m-1-n}h_{m,n}.
  \]
  With \(H=\max_{m<t}a_m\), or zero for an empty prefix, formula (R6) becomes
  \[
  p_0=\frac{N}{182\,8^H27^t},\quad
  N=26\sum_{m<t}27^{t-1-m}8^{H-a_m}N_m+8^H(8+h_t).         \tag{R14}
  \]
  This follows by exact substitution; \(h_t\) is Boolean since the vertical exit is outside the common domain. — [Source formula check](renewal_check.py).
- For this fixed boundary prescription, \(N\bmod13=8^H(8+h_t)\ne0\); hence 13 does not cancel from one unscaled \(p\)-source. A sum of all sources can cancel it, as radius two demonstrates. — [Exact local and whole-source tests](renewal_check.py).

### Inferences

**R5. A complete common denominator and a necessary full gcd condition.** Let \(H_R\) be the largest horizontal exit among all \(q\)-values in the nine vertical source prefixes and the twelve low sources; let \(T_R\) be the largest of the nine vertical source exits. Then
\[
D_R^0=91\,8^{H_R}27^{T_R+1},\qquad D_R^0S_R\in\mathbb Z.  \tag{R15}
\]
For a high term, \(216\,2^{-i}3^{-b_j}/182\) has its factor two canceled because \(i\le2\), and needs at most an extra \(3^3=27\), because \(b_j\le6\). For a low term, \(8\,2^{-i}/7\) is integral apart from its seven, and \(3^{-b}\) needs at most 27. This proves (R15), including all physical weights.

Put \(J_R=D_R^0S_R\), \(g_R=\gcd(D_R^0,J_R)\). The true reduced denominator is \(D_R=D_R^0/g_R\). Let \(\tau_R\) be the first horizontal exit on the actual fixed row \((a,b)=(3n,4)\). Its initial state is zero, so its initial \(q\)-value occurs in the corresponding vertical source prefix and \(H_R\ge\tau_R\). At the occupied exterior cell \((3\tau_R,4)\), inequality (R4) gives the positive witness
\[
\Psi_R\ge\frac67\,8^{-\tau_R}3^{-4}.
\]
Therefore
\[
D_R^0\Psi_R\ge26\,8^{H_R-\tau_R}27^{T_R},\qquad
D_R\Psi_R\ge\frac{26\,8^{H_R-\tau_R}27^{T_R}}{g_R}.        \tag{R16}
\]
The naive common clear factor always fails. For the reduced factor to be adequate along a sequence, it is **necessary** that
\[
\frac{g_R}{8^{H_R-\tau_R}27^{T_R}}\longrightarrow\infty.    \tag{R17}
\]
No general upper bound on this actual full-source gcd is proved. This is a necessary condition for this family, not a universal no-go theorem. — [Exact common denominator and witness checks](renewal_check.py).

The exact checker gives:

| Radius | \(H_R,T_R,\tau_R\) | Reduced denominator of \(S_R\) | \(g_R\) | Certified lower bound for \(D_R\Psi_R\) |
|---|---|---|---:|---|
| 0 | \(3,3,1\) | \(2^6 3^{10}13\), 26 bits | 504 | \(>2^{15}\) |
| 1 | \(200,125,32\) | \(2^{599}3^{376}91\), 1202 bits | 18 | \(>2^{1097}\) |
| 2 | \(1282,689,1065\) | \(2^{3844}3^{2068}7\), 7125 bits | 468 | \(>2^{3921}\) |

All state norms here are the Green norm \(\rho(x+y\omega)=\max(|y-x|,|x|)\). These are not the square-coordinate first exits 2 and 67 from the preceding one-axis experiment. The checker uses exact logarithm enclosures, accepted exact actual axes and event rules, exact fractions, and original-board verification of the new vertical reduction. It checks four-by-four full product pairings including terminal sources and all stated residual bounds. Its initial development accidentally used integer `/` in a finite weighted target sum; that check was corrected to exact `Fraction` multiplication before the final passing run. No floating-point assertion supports any result above. — [Checker](renewal_check.py).

### Gaps

- The sample gcds do not prove bounded gcd cancellation for all radii or rule out an adequate subsequence. A new arithmetic mechanism must either create enough actual cancellation or change the source construction. — [Exact scope of R16–R17](renewal_check.py).
- The finite-source rationality theorem alone is compatible with rational targets; multiplying a positive rational error by its denominator cannot tend to zero. The required statement remains about the actual nonrationality-sensitive whole source. — [Final integer-affine acceptance criterion](../finite-volume-calibration/REPORT.md).

## Can bounded boundary slack remove the second-axis denominator without changing positivity?

### Takeaway

Yes, locally under an explicit interval-width condition. A rational boundary constant can be chosen by one congruence to cancel all vertical powers without adding a larger horizontal denominator. This is a possible arithmetic lever; it does not remove the first-axis cost or prove adequate full-source cancellation. — [R14 and exact source construction](renewal_check.py).

### Cited Findings

- Keep the horizontal problem unchanged and replace the outer vertical prescription by \(p=c_B+q/26\), with \(1/26\le c_B\le2/26\). Positivity and the maximum principle give \(0\le p\le c_B+1/91\). The outside residual satisfies
  \[
  26c_B-1/91\le e_B\le27c_B+1/91,
  \]
  hence \(90/91\le e_B\le190/91\) throughout the permitted interval. The complete paired positivity argument is unchanged. — [Direct substitution into R5–R9](renewal_check.py).

### Inferences

At one source set
\[
B=26\sum_{m<t}27^{t-1-m}8^{H-a_m}N_m+8^H(1+h_t).
\]
Then
\[
p_0=\frac{B+182\,8^Hc_B}{182\,8^H27^t}.                 \tag{R18}
\]
Choose \(c_B=k/(182\,8^H)\). Its allowed interval is exactly
\[
7\,8^H\le k\le14\,8^H.
\]
If \(7\,8^H\ge27^t\), that interval contains a representative of every residue modulo \(27^t\). Taking \(k\equiv-B\pmod{27^t}\) cancels the entire vertical power in (R18), while \(\operatorname{den}(p_0)\) divides \(182\,8^H\). One may also use a larger common horizontal exponent than the local \(H\). Constants can be chosen independently for the nine high residue blocks. This is an exact integer-congruence argument with bounded positive boundary data, not an appeal to a solver or an independence assumption. — [Exact R14 source algebra](renewal_check.py).

The lemma is deliberately local. Removing a factor \(27^t\) can leave a prohibitively large horizontal factor. Simultaneous full-source optimization must retain the coefficient of \(Z\), the full range restrictions, all low sources and residual amplitudes. Other coordinated research is examining that global congruence problem; no conclusion from it is used here.

### Gaps

- No affordable infinite return, completion of step 9, or proof of Erdős #168(ii) is established. The positive change is a proved every-radius rational full-source construction with nonzero complete residual, plus exact arithmetic constraints for the next attempt.
- Skipped Lean, external review, priority checks and an independent reproof of Kesten's theorem. The main risk is equating rational source existence or local CRT cancellation with an adequate reduced denominator for the complete source.
