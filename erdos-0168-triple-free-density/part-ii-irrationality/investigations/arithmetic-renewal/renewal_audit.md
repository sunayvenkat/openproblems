# Independent foundation and source audit of the ordered renewal construction

## Does the actual vertical axis escape, with the uniform phase exit needed by the construction?

### Takeaway

**PASS.** The original-column identity proves unboundedness of the precise actual sequence \(B_{3m}\), using fixed-start Kesten discrepancy and bounded sampling gaps. The all-phase, one-sided and uniform-exit upgrades are valid. No substantive correction to R1–R4 is required; the finite-state compactness argument should be understood in the combined lattice offset, as made explicit below. — [Audited construction](renewal.md), [accepted horizontal exit audit](../finite-volume-calibration/calibration_audit.md), [independent exact checker](renewal_audit_check.py).

### Cited Findings

- The accepted inputs are the finite cover/birth theorem, actual horizontal unboundedness, complete transport and normalization, and the quantitative actual state-height theorem. This audit does not supply a new proof of those inputs. — [Accepted progress report](../finite-volume-calibration/REPORT.md), [complete transport](../occupation-arithmetic-bridge/exact_transport.md), [accepted exterior audit](../finite-volume-calibration/exterior_audit.md).
- Kelly–Sadun introduce the discrepancy using a specified starting point \(x\), then give Theorem 1 with the interval-length criterion. Their strip interpretation retains that starting point; their proof also explains why finitely many boundary hits do not affect boundedness. Thus this is the required fixed-start theorem, rather than an almost-everywhere substitute. — [Primary Theorem 1, introduction and proof](https://arxiv.org/html/1404.0455).
- Both the supplied checker and the independent checker pass. The independent checker imports no project code, uses integer powers to certify every required logarithmic floor, reconstructs the axes against original colored boards, and checks the new column identity and real-part encoding. Finite checks validate formulas; they do not prove unboundedness. — [Supplied checker](renewal_check.py), [independent checker](renewal_audit_check.py).

### Inferences

Write \(\alpha=\log_3 2\), \(\beta=1/\alpha\), and \(\mathcal K(t)=\sum_{2^a3^b\le t}\omega^{a-b}\). Splitting off the bottom row gives
\[
\mathcal K(3^b)=\omega^{-1}\mathcal K(3^{b-1})+
\sum_{a=0}^{\lfloor b\beta\rfloor}\omega^a.
\]
Multiplication by \(\omega^{-2b}\) gives exactly the accepted recurrence and initial value of \(B_b\). Thus \(B_b=\omega^{-2b}\mathcal K(3^b)\). At \(b=3m\), summing each column geometrically gives
\[
(1-\omega^{-1})B_{3m}=
\sum_{a=0}^{L_m}\omega^a-
\omega^{-1}\sum_{a=0}^{L_m}\omega^{\lceil(1+\alpha)a\rceil},
\qquad L_m=\lfloor3m\beta\rfloor.
\]
The endpoint \(a=0\) contributes one to the second sum and must be retained. It does not change unboundedness. — [R1](renewal.md), [original-board and column checks](renewal_audit_check.py).

For positive \(a\), let \(\theta=(1+\alpha)/3\). The summand in the second sum equals \(\omega,\omega^2,1\) on successive thirds of \(\{a\theta\}\), without endpoint hits. Therefore
\[
\operatorname{Re}\sum_{a=1}^N\omega^{\lceil(1+\alpha)a\rceil}
=\frac32\left(\#\{1\le a\le N:\{a\theta\}\in(2/3,1)\}-N/3\right).
\]
Irrationality of \(\theta\) excludes \(1/3\in\mathbb Z\theta+\mathbb Z\), so the quoted fixed-start criterion makes this discrepancy unbounded. The inequalities \(3/2<\beta<5/3\) give gaps \(L_{m+1}-L_m\in\{4,5\}\). Since each summand has modulus one, every unsampled partial sum is within five of a sampled one. Sampling cannot make these partial sums bounded. The first geometric sum is bounded and \(1-\omega^{-1}\ne0\), proving actual \(B_{3m}\) unboundedness. — [R1 and its source](renewal.md), [primary discrepancy criterion](https://arxiv.org/html/1404.0455), [independent encoding check](renewal_audit_check.py).

For completeness, the phase upgrade is sound. Put \(D_n(v)=\sum_{k<n}\Xi_3(v+k\beta)\). A bound \(\|D_n(v_*)\|\le C\) would imply \(\|D_n(v_*+m\beta)\|\le2C\) for all \(m,n\), by the cocycle identity. Each fixed finite sum is continuous at zero: a forward zero iterate hitting a drift cut would force \((3k+s)\beta\in\mathbb Z\), with \(k\ge0\), \(s\in\{1,2,3\}\). Density would then bound \(D_n(0)\), a contradiction. Two drift-cut hits on one orbit would force \(3(k-k')=s'-s\); hence there is at most one hit. Each one-sided itinerary therefore differs from its actual itinerary by at most one increment and remains unbounded. Compactness now excludes arbitrarily long surviving one-sided itineraries in a fixed finite lattice box. This is the same legitimate discontinuity argument used in the accepted horizontal proof. — [R1 phase upgrade](renewal.md), [accepted compactness proof](../finite-volume-calibration/calibration_audit.md).

For the complete state, the bounded phase corrections \(\Psi_i,\Xi_j,C_{ij},e_j\) do not alter escape. **The finite lattice variable for compactness is the combined offset \(y+w\), which lies in an enlarged finite box whenever the corrected state lies in \(D_R\). The raw pair \((y,w)\) need not range over a finite set.** Both ordered problems depend only on this combined offset and their phase coordinates. Uniform exits thus apply to the actual complete high states and the fixed low offsets. A finite common refinement includes every state-correction cut, every pulled-back reward cut, and its endpoint values. Bounded horizons make that refinement finite; no invariant phase partition or arbitrary alternating exit assertion is needed. — [Complete lifted state](../occupation-arithmetic-bridge/exact_transport.md), [R1–R6](renewal.md), [accepted reward-cut qualification](../finite-volume-calibration/calibration_audit.md).

### Gaps

- Uniform exit is qualitative here. The finite examples do not give a general upper bound for its horizon. Kesten's theorem itself remains an imported theorem, with the required fixed-start scope checked above. — [Accepted exit scope](../finite-volume-calibration/calibration_audit.md), [primary theorem](https://arxiv.org/html/1404.0455).

## Do the ordered equations give a rational complete source and a positive vanishing full residual?

### Takeaway

**PASS.** For every nonnegative integer radius, the ordered construction gives rational source values for every one of the nine high and twelve low terms. It yields the complete identity
\[
S_R=Q_{\rm full}(0)+\Psi_R,\qquad
Z=2-3S_R+3\Psi_R,\qquad \Psi_R>0,\quad\Psi_R\to0.
\]
Pointwise positivity of the product residual is unnecessary: its signed interface pairs to a positive initial-horizontal line with its factor eight intact. — [R2–R13](renewal.md), [complete transport](../occupation-arithmetic-bridge/exact_transport.md), [independent checker](renewal_audit_check.py).

### Cited Findings

- The exact high operator is \((8I-U_A)(27I-U_B)\). The accepted high occupation decomposes into nine residue blocks with vertical starts \((6,4,5)\); all twelve low rules have their separate horizontal resolvents. The accepted full normalization is \(Z=2-3Q_{\rm full}(0)\), with the exceptional birth inserted once in the constant two. — [ET1–ET8](../occupation-arithmetic-bridge/exact_transport.md), [normalization audit](../numerator-and-residuals/occupation_audit.md).
- The independent checker verifies all nine high and twelve low finite pairing identities with exact fractions and every terminal edge/corner. It also reproduces the actual source prefix records in the supplied JSON. — [Independent checker](renewal_audit_check.py), [source records](renewal_source_data.json).

### Inferences

The finite first-exit sums solve the two stated equations exactly, including zero-depth exits. Their bounds are
\[
0\le q_R\le2/7,\qquad 0\le p_R\le9/182.
\]
Outside the domain,
\[
e_A=(8+h)/7-q_R\circ T_A\in[6/7,9/7],
\qquad
e_B=(27+q_R)/26-p_R\circ T_B\in[90/91,191/182].
\]
These estimates allow re-entry and do not assume that the next point is also outside. Both errors vanish inside. Uniform finite horizons and complete reward refinements prove rational-valued finite-step formulas, including every starting source value. — [R2–R7](renewal.md), [independent recurrence and residual checks](renewal_audit_check.py).

Algebra gives \(\mathcal Lp_R=h+e_A+(8I-U_A)e_B\). For \(W_j=\Omega\otimes\Pi_j\), the horizontal resolvent gives exactly
\[
W_j((8I-U_A)e_B)=8\Pi_j(e_B(1,\cdot,0,\cdot)).
\]
There is no extra unknown term or cancellation of the eight. For finite rectangles its omitted-at-infinity term is the horizontal terminal line; the product identity additionally has both source edges and their corner. All vanish in the infinite limit by the uniform bounds above and geometric discounting. — [R8–R9 and ET6](renewal.md), [all-block finite-terminal checks](renewal_audit_check.py).

With \(b_j=(6,4,5)_j\), the resulting source has precisely the weights
\[
216\sum_{i,j=0}^2 2^{-i}3^{-b_j}p_{ij,R}(1,V_{m_j},0,v_{m_j})
+8\sum_{i=0}^2\sum_{b=0}^3 2^{-i}3^{-b}q_{i,b,R}(1,0).
\]
Every low row is retained as an infinite horizontal row under its own rule; no vertical low-row shift is used. The residual is the sum of all \(e_A\) occupations and the nonnegative \(e_B\) initial-horizontal line integrals. Infinite actual high support and the strict exterior lower bound for \(e_A\) make it strictly positive at every radius. — [R10–R11](renewal.md), [accepted support and normalization](../finite-volume-calibration/exterior_audit.md).

The initial-horizontal lines have physical indices \(a=i\in\{0,1,2\}\). They are a subset of the full exterior sum, with coefficient eight. Thus
\[
0<\Psi_R\le\left(\frac97+8\frac{191}{182}\right)
\sum_{\rho(\zeta_{a,b})>R}2^{-a}3^{-b}
=\frac{881}{91}\sum_{\rho(\zeta_{a,b})>R}2^{-a}3^{-b}.
\]
The low states in this expression use their separate formulas. The accepted height estimate, enlarged by their finitely many offsets, and the complete quadrant tail give
\[
0<\Psi_R\le\frac{881}{91}(6\,2^{-m_R}-3\,3^{-m_R})
\le\frac{5286}{91}2^{-m_R}\to0.
\]
There is no missing infinite low tail or exceptional birth in this calculation. — [R12–R13](renewal.md), [accepted complete tail proof](../finite-volume-calibration/exterior_audit.md), [exact coefficient check](renewal_audit_check.py).

### Gaps

- This proves the new ordered source rational. It does not rationalize the earlier unrestricted coupled Dirichlet source. The product residual may be signed before pairing. — [Construction's stated scope](renewal.md), [earlier real construction](../finite-volume-calibration/exterior_audit.md).

## Are the complete denominators, actual data and limited boundary congruence lemma correct?

### Takeaway

**PASS.** R14–R18 have the stated scope. The common denominator and whole-source gcd formulas are valid, and the three reported actual examples are reproduced independently. They fail the required small-cleared-error condition by the stated certified lower bounds; they do not settle the behavior of an infinite subsequence. — [R14–R18](renewal.md), [independent checker](renewal_audit_check.py).

### Cited Findings

- The supplied checker was run once and passed. The independent no-project-import checker passed in approximately four seconds and reproduces the high \((t,H,B)\) records, low \((a,N)\) records, and global \((R,H,T,\tau)\) records in the JSON. Its logarithmic floors come from exact integer powers, independently of the supplied checker's rational logarithm enclosures. — [Supplied checker](renewal_check.py), [independent checker](renewal_audit_check.py), [source data](renewal_source_data.json).
- The exact reproduced whole-source data are:

  | \(R\) | \((H_R,T_R,\tau_R)\) | Reduced denominator | \(g_R\) | Certified \(D_R\Psi_R\) lower bound |
  |---|---|---|---:|---|
  | 0 | \((3,3,1)\) | \(2^6 3^{10}13\), 26 bits | 504 | \(>2^{15}\) |
  | 1 | \((200,125,32)\) | \(2^{599}3^{376}91\), 1202 bits | 18 | \(>2^{1097}\) |
  | 2 | \((1282,689,1065)\) | \(2^{3844}3^{2068}7\), 7125 bits | 468 | \(>2^{3921}\) |

  These are inequalities from one positive occupied witness, not numerical estimates of the full infinite residual. — [Independent exact assertions](renewal_audit_check.py).

### Inferences

At a high source, the terminal vertical point is outside, so its horizontal value is \((1+h_t)/7\). Substitution into the vertical sum gives
\[
p_0=\frac{N}{182\,8^H27^t},\qquad
N=26\sum_{m<t}27^{t-1-m}8^{H-a_m}N_m+8^H(8+h_t).
\]
Thus \(N\not\equiv0\pmod{13}\), including \(t=0\). This local uncancelled factor is not automatically a factor of the assembled source denominator; the actual radius-two source cancels it. The independent checker obtains the same value by backwards evaluation of the defining recurrence before checking this numerator formula. — [R14](renewal.md), [independent checker](renewal_audit_check.py).

Every high coefficient reduces to \(2^{2-i}3^{3-b_j}/91\) times its nested base-eight/base-27 numerator factor. Since \(b_j\le6\), at most one extra factor 27 is needed. The twelve low coefficients need at most \(7\cdot27\) beyond their horizontal powers. Therefore
\[
D_R^0=91\,8^{H_R}27^{T_R+1},\qquad J_R=D_R^0S_R\in\mathbb Z,
\qquad D_R=D_R^0/\gcd(D_R^0,J_R).
\]
This pays all physical weights and applies to the whole source. — [R15](renewal.md), [independent whole-source assembly](renewal_audit_check.py).

The actual row \((3n,4)\) starts at state zero. Its first exit \(\tau_R\) is included in a vertical source prefix, so \(H_R\ge\tau_R\). Its physical weight and \(e_A\ge6/7\) give
\[
\Psi_R\ge\frac6{7\,8^{\tau_R}3^4},\qquad
D_R\Psi_R\ge\frac{26\,8^{H_R-\tau_R}27^{T_R}}{g_R}.
\]
Consequently the common clear factor is always inadequate, and adequacy of the reduced factor along a sequence necessarily requires
\(g_R/(8^{H_R-\tau_R}27^{T_R})\to\infty\). This necessary condition is not a general gcd bound or a universal impossibility theorem. — [R16–R17](renewal.md), [independent witness checks](renewal_audit_check.py).

The limited boundary-congruence lemma is also algebraically correct. Under \(p=c_B+q/26\), \(c_B\in[1/26,2/26]\), the exterior residual stays in \([90/91,190/91]\). Writing \(c_B=k/(182\,8^H)\) gives the exact allowed integer interval \([7\,8^H,14\,8^H]\). If \(7\,8^H\ge27^t\), it contains every residue modulo \(27^t\); choosing \(k\equiv-B\pmod{27^t}\) removes that vertical power in this one source. It does not remove the remaining horizontal cost or establish simultaneous affordable whole-source clearing. — [R18 and its explicit scope](renewal.md).

### Gaps

- **Strongest validated theorem:** every integer radius gives a complete rational source \(S_R\) with a strictly positive residual \(\Psi_R\to0\), the stated explicit clear factor, and the stated necessary whole-source gcd saving. **Residual arithmetic gap:** no infinite sequence is proved for which the actual reduced denominator satisfies \(D_R\Psi_R\to0\). Erdős #168(ii) remains unproved. — [R11–R17](renewal.md), [accepted integer-affine acceptance criterion](../finite-volume-calibration/REPORT.md).
- No additional audit round, new research direction, Lean work, installation, external posting or novelty claim was undertaken. The JSON's additional boundary-optimization summaries and the separate colleague's global tuning results are outside this foundation/source audit; only the source-prefix records and horizons listed above were checked. The material risk is promoting rational source existence or a local congruence cancellation to an adequate infinite arithmetic return. — [Audited scope and stated remaining gap](renewal.md), [checked JSON fields](renewal_audit_check.py).
