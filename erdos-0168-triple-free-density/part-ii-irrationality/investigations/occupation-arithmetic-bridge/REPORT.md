# Pure guards expose the occupation gap

**Finite horizontal phase codes that are nonconstant on intervals now have simultaneous rational models with adequate nonzero arithmetic returns along a proved actual infinite subsequence.** Their common clearing factor is \(8^q-1\), and the construction works at resonant as well as nonresonant convergents. It requires neither unbounded partial quotients nor a conjectural digit-frequency statement. Complete physical transport and a quantitative state-height estimate clarify why this success does not yet transfer to the occupation returns needed for the density. The transport retains joint state-and-phase cone values, and its displayed integer identity has zero bulk target coefficient. Three independent audits report PASS with no substantive erratum, supported by three supplied and three standalone exact checkers. **No exact or approximate occupation arithmetic bridge, adequate infinite return for the density, or proof of Erdős #168(ii) has been obtained.** ([Guard audit](<guard_audit.md>), [transport audit](<transport_audit.md>), [height audit](<height_audit.md>))

**The occupation route has a precise positivity and arithmetic budget.** Let \(c\) be the limiting maximum density of sets avoiding \(\{n,2n,3n\}\). The completed finite-cover theorem supplies its birth digits and the exact target \(Z=9c-6\). In the accepted occupation notation,
\[
Z=2-3Q_{\rm full}(0),\qquad Q_H=Q_{\rm full}-L.
\]
Here \(Q_{\rm full}\) is the unexceptional all-row readout; the original birth override at \((0,1)\), of weight \(1/3\), is accounted for once in the constant two. The four low rows in \(L\) still extend infinitely horizontally. The earlier construction gives actual occupied states \(z_n\), first total-index arrivals \(N_n\to\infty\), and
\[
\mathcal E_n=\nu^H(z_n)
=D_\omega D_{\omega^2}Q_H(-z_n)>0,\qquad
\mathcal E_n\le6\,2^{-N_n}-3\,3^{-N_n}\to0.
\tag{1}
\]
The point-source Green stencil underlying this family is archival; its complete occupation application and actual-support proof are established inputs here. Neither the stencil nor positivity evaluates the four translated cone values arithmetically. ([Accepted positive family and normalization](<../numerator-and-residuals/occupation_audit.md>), [finite foundation](<../prefix-and-phase-audit/REPORT.md>))

An approximate bridge would suffice. Choose a first-arrival witness \((a_n,b_n)\), with \(a_n+b_n=N_n\), and set \(w_n=2^{-a_n}3^{-b_n}\). It is an actual positive contribution, so \(3^{-N_n}\le w_n\le\mathcal E_n\). Suppose a construction proved
\[
R_n=\frac{u_nZ+v_n}{T_n},\qquad
T_n\in\mathbb Z_{>0},\quad u_n,v_n\in\mathbb Z,\qquad
|R_n-\mathcal E_n|\le\vartheta w_n,\quad 0\le\vartheta<1.
\tag{2}
\]
Then \(R_n\ge(1-\vartheta)w_n>0\) and \(R_n\le(6+\vartheta)2^{-N_n}\). If \(T_n2^{-N_n}\to0\), hypothetical rationality \(Z=A/B\) would make \(BT_nR_n=u_nA+Bv_n\) a positive integer tending to zero. No separate height bound on \(u_n,v_n\) is needed. A conservative error bound \(\vartheta3^{-N_n}\) also works; an unspecified absolute error tending to zero does not ensure positivity. **No relation satisfying (2) has been constructed.** ([Positivity-aware criterion AB1](<approximate_bridge.md>), [independent deduction](<guard_audit.md>))

A target-free rational replacement cannot provide the missing cheap multiplier. If a positive reduced rational \(r_n/s_n\) satisfies that accuracy, its upper bound forces
\[
s_n\ge\frac1{R_n}\ge\frac{2^{N_n}}{6+\vartheta}.
\]
Every integer clearing it is a multiple of \(s_n\), so its cleared positive value is at least one. This applies after genuine denominator cancellation. It excludes that replacement strategy, not a target-dependent identity with nonzero \(u_n\). ([AB2 and its scope](<guard_audit.md>))

**Pure horizontal guards have an automatic infinite arithmetic supply.** Put \(\alpha=\log2/\log3\). For a finite nonempty set \(S\) of positive offsets, \(s_*=\max S\), and a Boolean function \(f\), define
\[
g_n=f\bigl((\lfloor(3n+s)\alpha\rfloor\bmod3)_{s\in S}\bigr),
\qquad G_f=\sum_{n\ge0}8^{-n}g_n.
\]
Take consecutive actual convergents \(p/q,P/Q\), and let \(\sigma=\operatorname{sign}(\alpha-p/q)\). At positive indices the correct one-sided rational floor is
\[
\lfloor kp/q\rfloor_\sigma
=\lfloor kp/q\rfloor-\mathbf1_{\{\sigma<0,\ q\mid k\}}.
\]
Replacing every floor gives \(\widehat g_n\). Increasing \(n\) by \(q\) adds \(3p\) to the floors and preserves the tie rule, proving exact \(q\)-periodicity. Thus
\[
\widehat G_f=
\frac{\sum_{r=0}^{q-1}8^{-r}\widehat g_r}{1-8^{-q}},
\qquad D_q\widehat G_f\in\mathbb Z,\quad D_q=8^q-1.
\tag{3}
\]
The full \(n=0\) term is retained. Positive offsets avoid a hidden lower-sided index-zero override. No nonresonance condition enters this argument. ([Complete guard construction AB3](<approximate_bridge.md>), [independent period reconstruction](<guard_audit.md>))

Farey exclusion gives actual/model floor agreement for \(0<k<q+Q\). The code words therefore agree through \(n<m\), where
\[
m=\left\lceil\frac{q+Q-s_*}{3}\right\rceil>0.
\]
Boolean range bounds the entire remaining difference by \((8/7)8^{-m}\), giving the common estimate
\[
\boxed{D_q|G_f-\widehat G_f|
\le\frac87\,2^{s_*+2q-Q}.}
\tag{4}
\]
It is simultaneous for every Boolean code on the context: the constant does not grow with the number of labels. This is a complete tail estimate, not agreement of finite words promoted to equality of sums. ([AB3 and exact tail audit](<guard_audit.md>))

There are infinitely many actual indices with \(Q-2q>q/3\). Prime valuations exclude rational \(\alpha\), while Gelfond–Schneider excludes algebraic irrational \(\alpha\), since \(3^\alpha=2\). Hence its continued fraction cannot be eventually all ones, which would be quadratic. If next digits at least three occur infinitely, \(Q-2q\ge q+q_{n-1}\) there. Otherwise the tail digits are at most two and infinitely many next digits equal two; at those late indices,
\[
q=a_nq_{n-1}+q_{n-2}<3q_{n-1},\qquad
Q-2q=q_{n-1}>q/3.
\tag{5}
\]
The external transcendence theorem is an established input: both researchers checked its statement and specialization, rather than reconstructing its proof. Neither an unbounded-partial-quotient hypothesis nor a favorable congruence state is used. ([Soundararajan course notes, Theorem 10, PDF p. 9](https://math.stanford.edu/~ksound/TransNotes.pdf#page=9), [actual-supply audit](<guard_audit.md>))

Equations (4)–(5) make the cleared errors tend to zero for fixed contexts, and uniformly for growing contexts with \(s_*=o(q)\), even when the Boolean codes change. Changing codes means changing real target values. Nonzero returns require a phase function genuinely nonconstant on positive-length intervals. An eventually periodic orbit word would make its finite essential boundary invariant under an irrational rotation, by density of the tail orbit; that is impossible. Base-eight digits zero and one therefore give an irrational \(G_f\), distinct from every rational model. Constant and boundary-only codes are excluded from this assertion. There is no claim of rational independence among guards, nor any extension of this common-denominator theorem to joint horizontal/vertical guards or density readouts. ([Nonperiodicity and growing-context qualifications](<guard_audit.md>))

This simultaneous arithmetic does not invoke a growing-dimensional S-unit estimate. Its denominator and error come directly from one period and one matching prefix, regardless of how many Boolean labels the context defines. It therefore needs no dimension-uniform version of the Kohlmeyer–Kruer seed. That advantage concerns the phase words actually represented in (3); it does not license a new periodic state model or arithmetic for an unknown cone value. ([Complete AB3–AB6 derivation](<approximate_bridge.md>))

Independent exact reconstruction verifies matching lengths **27, 189 and 8593** for \(S=\{1,2,3\}\) at \(12/19\to41/65\), \(53/84\to306/485\), and resonant current \(665/1054\to15601/24727\). These finite examples validate the conventions; (3)–(5) prove the infinite result. The unrestricted supply does not prove the original scalar route's joint eligible digit-\(\ge5\) visits, or the fan route's joint state conditions. ([Actual examples and complete periods](<guard_audit.md>))

**Complete transport preserves the mixed readouts that guards alone cannot evaluate.** The horizontal lift is explicit. With \(Y_n=A_{3n}\), \(x_n=\{n\alpha\}\), \(\mathcal S=(1,-\omega,0)\) periodic, put
\[
\Psi_i(x)=\sum_{s=1}^i\omega^{-s}\mathcal S(\lfloor3x+s\alpha\rfloor),
\quad \Phi=\Psi_3,\quad
T_A(y,x)=(y+\Phi(x),\{x+\alpha\}).
\]
Then \(A_{3n+i}=Y_n+\Psi_i(x_n)\), and
\[
\Omega=\sum_{n\ge0}8^{-n}\delta_{(Y_n,x_n)}
=\delta_{(1,0)}+\tfrac18(T_A)_*\Omega.
\tag{6}
\]
The phase coordinate is essential. The vertical lift uses \(\beta=1/\alpha\), \(V_m=B_{3m}\), \(v_m=\{m\beta\}\), and the periodic partial sum \(\mathcal P=(1,-\omega^2,0)\):
\[
\Xi_j(v)=\sum_{s=1}^j\omega^{-2s}\mathcal P(\lfloor3v+s\beta\rfloor),
\qquad T_B(w,v)=(w+\Xi_3(v),\{v+\beta\}).
\]
Thus \(B_{3m+j}=V_m+\Xi_j(v_m)\). The discount is \(1/27\), and the high-row starts are \(m_j=(2,1,1)_j\), or \(b_j=(6,4,5)_j\):
\[
\Pi_j=27^{-m_j}\delta_{(V_{m_j},v_{m_j})}
+\tfrac1{27}(T_B)_*\Pi_j.
\]
The high correction remains the exact guarded function \(E_{3m+j}=e_j(v_m)\), including its isolate and patch tests and negative-offset floors. The independent checker reconstructs these guards from the original numerical root windows on every phase cell. Low rows retain their separate \(\Phi_b\) tests. ([Complete lifts ET1–ET5](<exact_transport.md>), [original-window audit](<transport_audit.md>))

The product resolvent gives the exact integer-\(216\) identity. For brackets against \(\Omega\otimes\Pi_j\),
\[
216\langle h\rangle-27\langle h\circ T_A\rangle
-8\langle h\circ T_B\rangle+\langle h\circ T_AT_B\rangle
=216\,27^{-m_j}h(1,V_{m_j},0,v_{m_j}).
\tag{7}
\]
Every finite rectangle retains its two terminal edges and corner before the convergent infinite limit. If
\[
Q_H^{uv}(t)=\sum_{a\ge0,b\ge4}2^{-a}3^{-b}
F(\zeta_{a+3u,b+3v}+t),
\]
the complete physical form is
\[
216Q_H^{00}-27Q_H^{10}-8Q_H^{01}+Q_H^{11}
=216\sum_{i,j=0}^2 2^{-i}3^{-b_j}F(\zeta_{i,b_j}+t).
\tag{8}
\]
The nine-cell source is rational and becomes integral after multiplication by \(27\). The low rows separately satisfy
\[
8L(t)-L^{10}(t)=
8\sum_{i=0}^2\sum_{b=0}^3
2^{-i}3^{-b}\Phi_b(\zeta_{i,b}+t).
\]
No vertical low-to-high substitution is made. **The bulk target coefficient in (8) is zero:** \(216-27\cdot8-8\cdot27+216=0\). Applying the state Green differences produces shifted or guarded vertex values and the finite source; it does not produce \(T\mathcal E=uZ+v\). ([Full sources, low rows and zero-bulk audit](<transport_audit.md>))

The most direct closure shortcuts fail in precise scopes. After \(L\) horizontal three-step shifts, the displacement has exactly \(9L\) distinct nonzero phase jumps. A finite invariant interval partition would require a finite boundary set invariant under an irrational rotation, which is impossible. A global fixed affine physical shift \(A_{a+h}=\gamma A_a+t\) also fails: bounded increments and actual unboundedness exclude \(\gamma\ne1\), while the genuine cuts exclude constant displacement for \(\gamma=1\). Proper finite-interval guard masses are irrational in bases eight and twenty-seven even though their total masses are rational. These facts neither bound a bridge multiplier nor exclude special weighted-value cancellation. Arbitrary linear combinations can cancel, and no independence claim follows. ([Cut, shift and guard proofs ET5–ET10](<transport_audit.md>))

Periodic guard replacement makes the remaining arithmetic explicit. For a bounded actual-state observable \(h_n\),
\[
\sum_{n\ge0}8^{-n}\widehat g_nh_n
=\sum_{r=0}^{q-1}8^{-r}\widehat g_r
\underbrace{\sum_{k\ge0}8^{-qk}h_{r+kq}}_{H_{q,r}}.
\tag{9}
\]
The replacement error has the same complete-tail bound multiplied by \(\|h\|_\infty\). But the \(H_{q,r}\) remain unknown actual-state readouts. They equal the rational geometric factor when \(h=1\); no such evaluation is proved for general cones. At the resonant example, \(A_{3q}\ne A_0\) despite periodicity of the rational guard code. ([Decimated-state formula AB6](<guard_audit.md>))

There is an actual infinite-sum certificate against scalar factorization. For \(g_n=\mathbf1_{\{\lfloor(3n+1)\alpha\rfloor\equiv0(3)\}}\), and separately \(h_n=\mathbf1_{\{A_{3n}=1\}}\) or \(h_n=F(A_{3n}-1)\), let \(\Omega(h)=\sum8^{-n}h_n\). Then
\[
\frac1{10}<
\Omega(gh)-\frac{\Omega(g)\Omega(h)}{8/7}
<\frac16.
\tag{10}
\]
Both marginal tails and the joint tail after 28 original-board samples are paid. This excludes the stated independence factorization; it is no prohibition on other target-dependent relations. ([Independent correlation intervals](<guard_audit.md>))

**State height leaves room for a proved low-cost bridge.** Use \(R(x+y\omega)=\max(|x|,|y|)\). Archived CS1–CS3 already establish actual color discrepancy \(W(T)=o(T)\); qualitative sublinearity is not newly discovered here. The exact board identities give \(A_a=o(a)\), \(B_b=o(b)\), and the state corrections lie in finite sets. Uniformly,
\[
R(\zeta_{a,b})\le\varepsilon(a+b)+C_\varepsilon,
\qquad R(z)=o(N(z))
\tag{11}
\]
at first arrivals. This is stronger than unboundedness alone and applies to the actual occupied family. ([Archived discrepancy](<../rational-coupling-construction/coupling_strictness.md>), [first-arrival application](<height_audit.md>))

The quantitative extension uses an elementary all-phase grid estimate. For \(g(u)=\omega^{\lfloor3u\rfloor}\), a \(\beta=\log_2 3\) convergent denominator \(q\) gives a block bound \(30\), hence
\[
\sup_x\left|\sum_{k=0}^{n-1}g(x+k\beta)\right|
\le30n/q+q.
\]
Matveev's two-fixed-logarithm theorem gives \(q_{\rm next}\le Cq^K\). Choose the largest such \(q\le n^\kappa\), with \(\kappa=K/(K+1)\); its successor exceeds the cutoff, so \(q>C^{-1/K}n^{1/(K+1)}\). Both terms above are \(O(n^\kappa)\). The exact row sum uses the same estimate at step \(-\beta\), uniformly in its moving phase, yielding
\[
\boxed{R(z)\le C_1(N(z)+1)^{K/(K+1)}.}
\tag{12}
\]
There is no bounded-partial-quotient or \(O(\log N)\) discrepancy assumption. Constants are fixed and effective but enormous and unoptimized; the inverse inequality is a lower bound on first arrival, not an upper escape-time estimate. ([Matveev, Theorem 2.1](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng#page=3), [independent rate derivation](<height_audit.md>))

Consequently a **genuine** bridge with \(\log T=O(R)\) would satisfy \(\log T=o(N)\). More generally \(\log T=O(R^d)\) is affordable for every fixed \(d<1+1/K\). This is a conditional budget, not an achieved coefficient estimate; arbitrary polynomial costs are not covered. The actual witness \(A_0=A_9=1\), with \(A_3-A_0=-\omega\) and \(A_{12}-A_9=\omega^2\), prevents a deterministic state-only three-step rule, even with the same physical residue modulo three. It refutes neither every finite augmentation nor a general arithmetic bridge. ([Budget and original-board witness](<height_audit.md>))

Verification separates finite implementation checks from infinite arguments. The independent scripts import no companion project helpers. They reconstruct original colored-board axes, certify phase-breakpoint order with rational logarithm intervals, retain the finite terminal sources, and pay the complete tails in the guard and correlation examples. The height checker covers every phase at the named \(\beta\)-convergent block denominators \(1,2,5,12,41,53,306\), rather than sampling a phase grid. Periodicity, density, the block proof and the checked external theorems establish the infinite statements; the examples alone do not. ([Transport certificate](<transport_audit.md>), [guard certificate](<guard_audit.md>), [all-phase height certificate](<height_audit.md>))

The completed and outstanding obligations remain distinct:

| Proof obligation or route | Current progress |
|---|---|
| Finite optimum, density encoding and complete scalar arithmetic | Proved in the accepted written foundation |
| Uniform scalar nonvanishing on the six-state class | Proved |
| Actual infinite eligible next digits at least five | Open; new unrestricted guard supply does not establish it |
| Full fan expansion and corrected nonvanishing on the following-digit subfamily | Previously proved; joint infinite applicability remains open |
| Occupation infinitude, positivity and decay | Proved |
| Complete guarded transport and conditional state-height budget | Proved here |
| Adequate horizontal phase-only arithmetic returns | Proved here on an actual infinite subsequence |
| Exact or positivity-preserving approximate occupation bridge | Open |
| Actual fan response arithmetic, sufficient whole-model gcd and infinite applicability | Open |
| Hierarchy full-boundary arithmetic and its own residual nonvanishing | Open |
| Irrationality of the density | Not established |

The finite exclusion for a rational density remains a reduced denominator exceeding \(2^{56}\). Six exact checkers and three fresh audits validate the present auxiliary statements; they add no stronger density denominator exclusion. The next decisive identity must retain a nonzero integer coefficient of \(Z\) while eliminating or controlling the mixed state-and-phase cone readouts, within the witness-relative error and multiplier budgets. Pure-guard periodicity, rational total measure, positivity and a small state radius provide no such identity by themselves. ([Recorded verification](<guard_audit.md>), [transport gap](<transport_audit.md>), [budget gap](<height_audit.md>), [finite density exclusion](<../signed-arithmetic-returns/REPORT.md>))

Skipped: Lean, external review, priority verification and full reconstruction of the external theorems. Material risk: affordable pure guards, sublinear state height and positive real returns do not supply the missing target-dependent occupation bridge.
