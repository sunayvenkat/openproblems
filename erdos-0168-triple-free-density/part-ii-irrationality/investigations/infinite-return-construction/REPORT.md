# Exact symmetries sharpen Erdős’s return barrier

**The requested infinite weighted-return construction for Erdős #168(ii) has not been proved, and that goal remains active.** The completed finite formula now supplies the correct birth digits unconditionally, and the present work proves several useful arithmetic and dynamical statements about them. These include sharp congruence-restricted convergent supply, full high-column skew covariance, a genuine rational generating function for resonant models, and a uniform obstruction to arbitrarily long windows with one fixed raw winning color. The current scalar model also admits a sharper sufficient condition, \(q'-5q\to+\infty\), by ordinary rational discreteness. None of these results supplies an adequate infinite sequence with the required weighted error, coefficient arithmetic, height, and nonzero remainder. **The remaining gap is larger than nonvanishing:** actual suitable supply is unproved for the scalar model, while the alternative constructions still lack the arithmetic compression of their weighted side or ray terms. The final internal audit passes the principal auxiliary proofs and explicitly rejects completion of the infinite-return goal. ([Final return audit](<final_return_audit.md>))

## Integer discreteness sharpens the scalar return threshold

Let \(D_t=\{2^a3^b\le t:a,b\ge0\}\), let \(\tau(D_t)\) be the minimum number of its points meeting every corner \(\{u,2u,3u\}\), and color \(2^a3^b\) by \(a-b\bmod3\). Write \(K_j(t)\) for the color counts. The earlier finite work proves, for every real \(t\ge3\),
\[
\tau(D_t)=\min_j\{K_j(t)-I_j(t)-P_j(t)\}. \tag{C}
\]
Here \(I_j\) records a dyadic root \(e=2^A\), \(A\ge1\), of color \(j\) with \(2t/3<e\le t\), and \(P_j\) records one with \(6e\le t<27e/4\). There is at most one such exceptional root across all colors. This report takes (C) as a proved input; statements in older return notes that still call it conditional are superseded. ([Complete finite proof and audits](<../prefix-and-phase-audit/REPORT.md>))

Let \(\eta_{a,b}\in\{0,1\}\) be the increment of \(\tau\) when \(2^a3^b\) is inserted, put \(c_{a,b}=1-3\eta_{a,b}\), and use the established normalization
\[
Z=\sum_{a,b\ge0}\frac{c_{a,b}}{2^a3^b}=9c-6,
\]
where \(c\) is the extremal density in #168(ii). Thus irrationality of \(Z\) is the density target. Absolute convergence follows from \(c_{a,b}\in\{1,-2\}\); the total geometric weight is \(3\), so \(|Z|\le6\). The exact separated state uses \(\omega^2+\omega+1=0\) and
\[
F(x+y\omega)=\mathbf1_{\{x\le0,\ x-y\le0\}},\qquad
C_{a,b}=\frac{(1-\omega^{-a})(1-\omega^{-2b})}{3}.
\]
For \(b\ge4\), its birth digit is \(F(A_a+B_b-1+C_{a,b}-E_b)\), with the isolated/patch correction \(E_b\) included. The two axis states are accumulated cocycles; no bounded-state description of the actual process is assumed. ([Exact return reduction](<../../early-attacks/augmentation-and-return-attacks/returns.md>), [state derivation](<../boundary-and-arithmetic/arithmetic.md>))

For a coprime rational \(p/q\), use the corrected admissible range
\[
\frac35<\frac pq<\frac23,\qquad
\sigma=\operatorname{sign}(\alpha-p/q),\qquad \alpha=\log_3 2.
\]
At positive indices, \(\lfloor np/q\rfloor_\sigma\) is the ordinary floor, with an exact integer lowered by one when \(\sigma<0\); the reciprocal slope uses the opposite sign. Set \(\widetilde A_0=\widetilde B_0=1\) separately and define
\[
\begin{aligned}
\widetilde A_a-\widetilde A_{a-1}
 &=\omega^{-a}S(\lfloor ap/q\rfloor_\sigma),&
 S(m)&=\sum_{j=0}^{m}\omega^{2j},\\
\widetilde B_b-\widetilde B_{b-1}
 &=\omega^{-2b}P(\lfloor bq/p\rfloor_{-\sigma}),&
 P(m)&=\sum_{i=0}^{m}\omega^i ,
\end{aligned}
\]
where \(S,P\) are extended three-periodically. With \(m_b=\lfloor bq/p\rfloor_{-\sigma}\), the high-column correction is the color \(m_b-2b\) when \(m_b-m_{b-1}=2\), or the color \(m_{b-1}-1-2b\) when \(m_{b-1}-m_{b-3}=4\). These tests cannot overlap in the corrected slope range. Apply \(F\) after subtracting that correction. For the four low columns, write \(\widetilde A_a+\widetilde B_b-1+C_{a,b}=x+y\omega\) and retain the distinct rules
\[
\begin{array}{c|l}
b&\widetilde\eta_{a,b}\\ \hline
0&0\\
1&\mathbf1_{\{x\ge1,\ y\ge0\}},\quad\text{except }\widetilde\eta_{0,1}=1\\
2&\mathbf1_{\{x\le-1,\ x-y\le0\}}\\
3&\mathbf1_{\{\min(x,0)\le y\}}.
\end{array}
\]
This specifies the artificial rational model used below. The narrower slope interval and the positive-index convention are substantive: the older broader range admits overlapping correction tests, and index zero must not inherit a negative-side tie rule. ([Audited model, (A4)–(A6)](<../global-boundary-proof/independent_audit.md>))

**Scalar-model theorem.** Suppose \(p/q\) is a convergent of \(\alpha\), \(p+q\not\equiv0\pmod3\), and \(p'/q'\) is its successor. Put
\[
U=2^{3q},\quad V=3^{3p},\quad
D=27(U-1)(V-1),\quad
\widetilde Z=\sum_{a,b\ge0}\frac{1-3\widetilde\eta_{a,b}}{2^a3^b}.
\]
Then \(N=D\widetilde Z\) is an integer, and the model agrees with the true digits throughout
\[
a<R=q+q',\qquad b<S_{\rm win}=p+p'. \tag{1}
\]
The proof of integrality uses actual state periods \(3q,3p\): summing the three blocks gives the nontrivial cube-root ratios \(\omega^{2p-q}\) and \(\omega^{q-2p}\), whose sums vanish. The corrections have the vertical period, while the low columns and their single exception give exactly the factor \(27\). For (1), consecutive convergents form a unimodular pair. Every rational threshold strictly between them has denominator at least \(q+q'\), and the mediant at that denominator lies between \(p/q\) and \(\alpha\). The one-sided convention handles ties at multiples of \(q\). Inversion gives the reciprocal threshold \(p+p'\). Thus the two floor words agree up to those strict bounds, their accumulated states and corrections agree there, and (C) identifies all birth digits in the rectangle. A first floor disagreement need not change a birth digit. Under rationality of \(Z\), the cleared form is
\[
DZ-N=27Z\,UV-27Z\,U-27Z\,V+27Z-N.
\]
It has four fixed rational coefficients and units \(UV,U,V,1\), all at least \(1\). Since \(|N|\le6D\le162UV\), its primitive integer projective coordinates satisfy \(H(N:UV:U:V:1)\le162UV\). The final coordinate \(1\) ensures primitivity. ([Farey matching, denominator, and height proofs](<../global-boundary-proof/independent_audit.md>))

**The full rectangle removes the old logarithmic loss.** A coefficient difference has absolute value at most \(3\). The geometric weight outside (1) is exactly
\[
3\{2^{-R}+3^{-S_{\rm win}}-2^{-R}3^{-S_{\rm win}}\}.
\]
Consequently
\[
\begin{aligned}
|Z-\widetilde Z|
 &\le9\{2^{-R}+3^{-S_{\rm win}}-2^{-R}3^{-S_{\rm win}}\},\\
|DZ-N|
 &\le243(U-1)(V-1)
 \{2^{-R}+3^{-S_{\rm win}}-2^{-R}3^{-S_{\rm win}}\}. \tag{2}
\end{aligned}
\]
Along convergents, \(p\log3-q\log2\to0\), and the same holds for \(p',q'\). Hence
\[
\boxed{|DZ-N|\le486(1+o(1))\,2^{\,5q-q'}.} \tag{3}
\]
If \(Z=A/B\) were rational, \(DZ-N\in B^{-1}\mathbb Z\). Therefore any infinite nonresonant sequence with **\(q'-5q\to+\infty\)** would force \(\widetilde Z=Z\) eventually. In particular, infinitely many nonresonant indices with next partial quotient at least \(5\) suffice for this implication, since
\[
q'-5q=(a_{n+1}-5)q+q_{n-1}\ge q_{n-1}\to\infty.
\]
The fixed margin \(q'/q>5+\delta\) is sufficient but stronger. **A Subspace Theorem adds no power for this integer-cleared model:** a remainder tending to zero already lies in a fixed rational lattice. Neither the actual infinite supply just specified nor nonstabilization of the resulting \(\widetilde Z\)'s has been proved. The jump \(53/84\to306/485\) is one exact instance, not an infinite sequence. ([Rectangle estimate and sharper criterion](<skew_denominator.md>), [final arithmetic audit](<final_return_audit.md>))

A different construction can use positive \(\{2,3\}\)-units that are not all integers, but must meet the full arithmetic acceptance condition. With fixed term count and fixed rational coefficients, it needs unbounded scales \(L\), constants \(C,\varepsilon_0>0\), and
\[
\begin{gathered}
E_L=\sum_{i=1}^{m}d_i u_{i,L}-N_L,\qquad N_L\in\mathbb Z,\\
0<t_L\le\min(1,u_{1,L},\ldots,u_{m,L}),\qquad
H(N_L:u_L)\le e^{CL},\\
\boxed{0<|E_L|\le t_L e^{-\varepsilon_0L}.} \tag{4}
\end{gathered}
\]
The primary mixed-form lower bound is KK Proposition 7.4: for nonzero \(E_L\), it gives \(|E_L|\ge c_\epsilon t_L H^{-\epsilon}\). Taking \(\epsilon C<\varepsilon_0\) contradicts (4) along unbounded \(L\). Its nonzero hypothesis and minimum-unit scale are essential. The cap \(t_L\le1\) has now been repaired in the current supply note. Without it, \(u_L=2^L\), \(N_L=2^L-1\), \(E_L=1\), \(t_L=2^L\) satisfies the uncapped exponential inequalities for \(0<\varepsilon_0<\log2\) and gives no contradiction. A proved fixed-term extension permits integer multiplicities bounded by \(B_L=e^{o(L)}\): its loss \(B_L^{m+\epsilon}\) can be absorbed into a fixed exponential margin. It does not permit an unbounded number of terms or erase exponential-height numerator costs. ([Repaired acceptance condition (15)](<diophantine_supply.md>), [saved primary manuscript, Proposition 7.4 and §7.3](<../../../../meta/theorem-transfer-survey/erdos1062-fork-free-density.pdf.txt>), [coefficient extension](<../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md>))

## Sharp congruence supply reaches a smaller clearing budget

Write \(p_n/q_n\) for the convergents of an irrational slope, and put
\[
s_n=p_n+q_n\bmod3,\qquad r_n=q_{n+1}/q_n,\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]
Call an index nonresonant when \(s_n\ne0\). The exact recurrences are
\[
s_{n+1}=a_{n+1}s_n+s_{n-1}\pmod3,\qquad
r_{n+1}=a_{n+2}+1/r_n. \tag{5}
\]
The determinant identity prevents consecutive resonances. **Among every four consecutive indices \(n,\ldots,n+3\), \(n\ge1\), one nonresonant index has \(r_i>\varphi\).** Indeed, if every nonresonant ratio in the block were at most \(\varphi\), its outgoing digit would be \(1\). Two consecutive nonresonant indices would then give \(r_{i+1}=1+1/r_i>\varphi\), since \(r_i\) is rational. Statuses must therefore alternate. At an interior nonresonant index preceded by a resonance, the outgoing digit \(1\) makes the next sum nonzero, contradicting alternation. The block length is sharp: the exact fractions \(18/29,23/37,64/103,87/140\) give a three-index nonresonant–resonant–nonresonant block whose two relevant ratios \(37/29,140/103\) are both below \(\varphi\). ([Supply theorem and exact obstruction](<diophantine_supply.md>))

**Improved supply theorem.** If the continued-fraction tail is not eventually all \(1\)'s, infinitely many nonresonant indices satisfy
\[
\boxed{r_n>C_*:=\frac{15+\sqrt5}{10}.} \tag{6}
\]
If outgoing digits at least \(2\) occur at nonresonant indices infinitely often, their ratios exceed \(2\) and the result follows. Otherwise all sufficiently late nonresonant outgoing digits are \(1\). There are then resonances exactly four indices apart, with sum pattern \(0,c,c,2c,0\). If \(R\) is a resonant ratio, the three intervening nonresonant ratios are
\[
1+\frac1R,\qquad
\frac{2R+1}{R+1},\qquad
\frac{3R+2}{2R+1},
\]
and successive resonant ratios obey
\[
R_{\rm next}=T_k(R),\qquad
T_k(R)=k+\frac{2R+1}{3R+2}.
\]
The map \(T_1\) is increasing and fixes \(\varphi\). There are infinitely many resonant digits \(k\ge2\); after the first, all resonant ratios exceed \(\varphi\), and at every later such digit they exceed \(T_2(\varphi)=\varphi^2\). The middle nonresonant ratio consequently exceeds
\[
2-\frac1{\varphi^2+1}=C_*.
\]
An eventually all-\(1\) tail would be quadratic. The actual \(\alpha=\log_3 2\) is transcendental: a rational value contradicts unique factorization, and an irrational algebraic value contradicts Gelfond–Schneider applied to \(3^\alpha=2\). Thus (6) applies to the actual slope. ([Complete proof and audit](<final_return_audit.md>), [Gelfond–Schneider, Theorem 10](https://math.stanford.edu/~ksound/TransNotes.pdf))

The constant \(C_*\) is **sharp even among transcendental slopes in \((3/5,2/3)\)**. Begin with six \(1\)'s, ending at the resonant \(8/13\), and append blocks \((k_j,1,1,1)\), with \(k_j=2\) at factorial block indices and \(k_j=1\) elsewhere. These choices preserve the four-step resonance pattern. Between increasingly sparse spikes, \(T_1'(R)=1/(3R+2)^2\) contracts the resonant ratios toward \(\varphi\); spike ratios approach \(\varphi^2\). The nonresonant limsup is therefore exactly \(C_*\). To prove transcendence, truncate after spike position \(m_j\) and replace the rest by all \(1\)'s. The quadratic approximant has an integer polynomial of height \(O(9^{m_j})\), while the shared digits through the next spike give distance \(O(2^{-m_{j+1}})\), with \(m_{j+1}/m_j\to\infty\). A nonzero integer resultant would force an algebraic number of fixed degree \(d\) to have distance at least a constant times that height to the power \(-d\). The other quadratic conjugate comes from a negative complete quotient and lies outside the positive-tail cylinder, so the resultant cannot vanish. The factorial gaps contradict the lower bound. This is an explicit limitation on what generic transcendence can supply; it asserts no adverse property of the actual logarithm. ([Sharpness construction and resultant proof](<diophantine_supply.md>))

The quantitative consequence for a replacement model is precise. If it has effective clearing cost
\[
\log D_q\le(\gamma+o(1))q\log2,
\]
the same matching window, controlled fixed-term arithmetic data, and an admissible minimum-unit scale, the supply (6) leaves a fixed exponential margin whenever
\[
\boxed{\gamma<1+C_*=\frac{25+\sqrt5}{10}.} \tag{7}
\]
The present exponent \(6\) is far above this budget; an exponent \(2\) would fit. Exponents \(3\) or larger are not justified by this interface. At equality, the strict inequalities in (6) can approach equality too quickly to leave a fixed margin. Any smaller minimum unit must be charged before using (7), and nonzero error remains a separate requirement. ([Clearing-cost interface](<diophantine_supply.md>))

Several natural supply repairs have exact limitations. Elsner's restricted approximation theorem, applied to \(1/(1+\alpha)\), gives infinitely many nonresonant convergents with error \(<\kappa/q^2\) for every fixed \(\kappa>1/\sqrt5\); it does not imply the scalar threshold \(q'-5q\to\infty\). A proper semiconvergent \(u/v=(kp_n+p_{n-1})/(kq_n+q_{n-1})\) first disagrees at index \(v+q_n<2v\), losing the long prefix. An arbitrary rational intercept cannot extend the original convergent prefix either: for \(N=q+q'\) and \(r=q_{n-1}\), every intercept fixes the rational floor difference at \((a_{n+1}+1)p\), while the true difference is that integer plus or minus \(1\). Replacing the successor by a later convergent ignores this first intervening defect. Taking a common period of consecutive models costs \(3qq'\) horizontally, against an established window of order \(q+q'\). None of these obstructions excludes a specially canceled combination or a genuinely shifted true-phase construction; those require their own weighted head, height, and scale proofs. ([Elsner, Proposition 2.1](https://www.fq.math.ca/Scanned/38-1/elsner.pdf), [window and intercept proofs](<diophantine_supply.md>), [precise common-period audit](<final_return_audit.md>))

## Skew covariance preserves four weighted side strips

For every admissible nonresonant rational model, put \(\rho=\omega^{2p-q}\), a nontrivial cube root. Exact summation of the axis increments gives
\[
\widetilde A_a=\frac23+\frac{\omega^{-a}}3+c_A+R_a,\quad
\widetilde B_b=\frac23+\frac{\omega^{-2b}}3+c_B+S_b,
\]
with \(R_{a+q}=\rho R_a\) and \(S_{b+p}=\rho^{-1}S_b\). The high-column correction satisfies \(E_{b+p}=\rho^{-1}E_b\). Thus the full corrected state is
\[
z_{a,b}=K+\frac{\omega^{-a-2b}}3+R_a+S_b-E_b,\qquad
z_{a+q,b+2p}=K+\rho(z_{a,b}-K). \tag{8}
\]
The center is **exactly one of two barycenters**:
\[
K=\frac{1-\omega}{3}
\quad\text{if }(p+q\bmod3,\sigma)=(1,+1)\text{ or }(2,-1),
\]
and \(K=(2+\omega)/3\) in the other two cases. Its proof evaluates \(c_A+c_B\) using the disjoint finite Beatty sets
\[
\{k+\lfloor kp/q\rfloor:1\le k<q\},\qquad
\{\ell+\lfloor\ell q/p\rfloor:1\le\ell<p\},
\]
which partition \(\{1,\ldots,p+q-2\}\); the one-sided endpoint terms determine which center occurs. Both the harmonic residue and \(E_b\) are retained in (8). ([Full center calculation and covariance](<skew_denominator.md>))

The cone partition includes every lattice tie. For \(K=(1-\omega)/3\), its three tests on an integer point \((x,y)\) are
\[
x\le\min(0,y),\qquad
y\ge0,\ x\ge1,\qquad
y\le-1,\ x\ge y+1.
\]
For \(K=(2+\omega)/3\), the latter two become \(y\ge1,x\ge1\) and \(y\le0,x\ge y+1\). Each list partitions \(\mathbb Z^2\) exactly. Combining this partition with (8) and the \(3p\) vertical period proves
\[
\sum_{i=0}^{2}\widetilde\eta_{a+iq,\ b+((j-i)\bmod3)p}=1
\qquad(a\ge0,\ b\ge4,\ j=0,1,2). \tag{9}
\]
The corresponding coefficients sum to zero. The theorem is restricted to high columns: in the valid \(5/8\) model, triples \((a,b,j)=(3,0,1),(0,1,0),(0,3,0)\) have sums \(0,2,2\). Thus the low rules cannot be absorbed into (9). ([Lattice partitions and low-column witnesses](<skew_denominator.md>))

**Skew symmetry does not automatically cancel a scalar denominator factor.** On a \(3\)-by-\(3\) block, (9) gives joint zeros \(\mathcal T(1,1)=\mathcal T(\omega,\omega)=\mathcal T(\omega^2,\omega^2)=0\). It does not give an identically zero polynomial at a fixed horizontal or vertical root. For example,
\[
\mathcal T(x,y)=(1+x+x^2)(1+y+y^2)-3(1+y+xy)
\]
has the same coefficient alphabet and exactly one selected cell on each \(i+j\bmod3\), but \(\mathcal T(1,y)=3y(y-1)\) and \(\mathcal T(x,1)=3(x^2-1)\). More decisively, the **actual \(53/84\) model has reduced denominator exactly \(D/6\)**: the independently reconstructed numerator satisfies \(\gcd(N,D)=6\), leaving 507 bits from a 509-bit nominal denominator. The proposed automatic removal of the large horizontal or vertical factors is therefore false. Special infinite-subsequence cancellations remain unexcluded. ([Algebraic obstruction and exact model reconstruction](<final_return_audit.md>))

There is nevertheless a useful degree-two interior operator:
\[
\widetilde c(a+2q,b)+\widetilde c(a+q,b+p)+\widetilde c(a,b+2p)=0
\quad(b\ge4).
\]
Its complete weighted identity makes the remaining cost visible. For any bounded integer array \(d(a,b)=c(a,b+4)\), put \(u=2^q,v=3^p\), let \(\mathcal D\) be its full reciprocal-weighted sum, let \(H_r\) sum the strip \(a<r\), let \(V_s\) sum the strip \(b<s\), and let \(\mathcal R\) sum the finite rectangle \(a<q,b<p\). If \(Ld=d(a+2q,b)+d(a+q,b+p)+d(a,b+2p)\), direct reindexing gives
\[
\begin{aligned}
(u^2+uv+v^2)\mathcal D
={}&u^2H_{2q}+uvH_q+uvV_p+v^2V_{2p}-uv\mathcal R\\
&+\sum_{a,b\ge0}\frac{Ld(a,b)}{2^a3^b}. \tag{10}
\end{aligned}
\]
The corner \(uv\mathcal R\) is an integer. **All four \(H,V\) terms are semi-infinite real weighted strips.** The original \(Z\) also retains its four low-column sums and \(\mathcal D/81\). The model kills the last series; for the actual array, agreement in (1) kills \(Ld\) only for \(a<R_A=q'-q,\ b<R_B=p'-p-4\). When these bounds are positive, \(|Ld|\le6\) gives the valid real residual estimate
\[
\left|\sum\frac{Ld(a,b)}{2^a3^b}\right|
\le18\{2^{-R_A}+3^{-R_B}-2^{-R_A}3^{-R_B}\}. \tag{11}
\]
The formal weight \(u^2+uv+v^2\) has logarithmic size \(2q\log2+O(1)\), compatible with the small-cost direction suggested by (7). Equations (10)–(11) do not yet form an arithmetic return: rationality or an adequate fixed-coefficient reduction of their four side values is missing. ([Retained-side proof, (W10)–(W12)](<weighted_returns.md>))

The exact response to correlated floor defects explains why the sides are difficult. Put \(m(Q)=\min(Q_0,Q_1,Q_2)\), \(D_i m(Q)=m(Q+e_i)-m(Q)\), and \(H_{ij}=D_iD_jm\). For an adjacent swap of physical weights \(d_1,d_2\) with colors \(i,j\), provided the correction indicators do not change, direct assignment of the increments to those same physical vertices gives
\[
\Delta\sum\frac{\eta}{d}
=H_{ij}(Q)(d_1^{-1}-d_2^{-1}),\qquad
\Delta\sum\frac{c}{d}
=-3H_{ij}(Q)(d_1^{-1}-d_2^{-1}), \tag{12}
\]
where
\[
H_{ij}=\mathbf1_{\{Q_i=Q_j<Q_k\}}\ (i\ne j),\qquad
H_{ii}=-\mathbf1_{\{Q_i+1=\min(Q_j,Q_k)\}}. \tag{13}
\]
These are weighted local times on a ray, or on shifted rays, of the count-state lattice modulo common translation. **Same-color crossings are not invisible.** At the abstract fixed-indicator state \(Q=(0,1,2)\), two color-zero insertions have increments \((1,0)\); exchanging symbolic distinct same-color weights changes their weighted sum from \(1/d_1\) to \(1/d_2\). This is a local algebraic example, not an exhibited adjacent smooth-board pair. The same-color invisibility argument was withdrawn. For finite reorderings, (12) telescopes only when each Hessian is evaluated in its current adjacent-swap context; low-column indicator events and an infinite-swap convergence argument remain additional obligations. ([Joint response and corrected illustration, (W1)–(W3)](<weighted_returns.md>))

Neither minimum identities nor a weighted Tanaka or resolvent notation closes those coefficients. Translates of \(H_{01}\) restricted to \(Q=(0,0,t)\) are the steps \(\mathbf1_{\{t+n\ge1\}}\); distinct jump locations make them linearly independent. An artificial separated state \(Q(a,b)=(0,0,x_a)\) can have a rational original birth sum while its ray sum is \((3/2)\sum_a x_a2^{-a}\), irrational for square-index binary digits. These examples disprove a generic finite translation module or a generic rationality transfer; they do not refute identities using the special actual rotation. For a \(P\)-periodic word, the exact resolvent
\[
G_a=\frac{\sum_{j=0}^{P-1}2^{P-1-j}h_{a+j}}{2^P-1},
\qquad h_a=2G_a-G_{a+1},
\]
has reduced denominator dividing \(2^P-1\), and its two-variable analogue has a common denominator \((2^P-1)(3^Q-1)\). These are divisibility statements: special words can cancel the factors completely, as \(h_a=1\) shows. Writing the resolvent proves neither such cancellation nor a small numerator. Finally, a fixed multiple of a convergent length contains only boundedly many floor defects, but each can translate every later accumulated state. Their paired reciprocal factor is only \(O(2^{-f}/q)\) under the available near-equality estimate; no extra fixed exponential margin follows from it. ([Translation, rationality, and resolvent limitations](<weighted_returns.md>), [denominator qualification](<final_return_audit.md>))

## Resonant cones retain substantial powers of two and three

When \(p+q\equiv0\pmod3\), the model states have affine drift instead of the nonresonant periods. Writing \(d_A=3h_A,d_B=3h_B\), exact finite floor sums give
\[
\widetilde A_{a+3q}=\widetilde A_a+d_A,\qquad
\widetilde B_{b+3p}=\widetilde B_b+d_B,\qquad
\boxed{h_A-h_B=\sigma}.
\]
The complete drift table is
\[
\begin{array}{c|c|c|c}
q\bmod3&\sigma&d_A&d_B\\ \hline
1&+1&2+\omega&-1+\omega\\
1&-1&-1+\omega&2+\omega\\
2&+1&1-\omega&-2-\omega\\
2&-1&-2-\omega&1-\omega.
\end{array}
\]
One evaluates the sums by writing \(p+q=3r\) and using the permutation \(rk\bmod q\); the finite Beatty partition supplies the relation between the two drifts. The sign is a difference, not a sum. A \(q\)-by-\(p\) shift still has a harmonic residue term; it disappears on the \(3q\)-by-\(3p\) sublattice. Positive shifts do not cancel the drift. Instead the full corrected state satisfies, for \(b\ge4\),
\[
z_{a+T_a,b+T_b}=z_{a,b}+\omega^q,\qquad
(T_a,T_b)=
\begin{cases}
(q,2p),&\sigma=+1,\\
(2q,p),&\sigma=-1.
\end{cases} \tag{14}
\]
The digit increases only on \(x\le0,\ x-y=1\) when \(q\equiv1\), or on \(x=1,\ x-y\le0\) when \(q\equiv2\). All ties are included. ([Universal drift and full-shift proofs](<resonant_models.md>))

**Resonant generating-function theorem.** The full digit generating function has the form
\[
f(U,V)=\sum_{a,b\ge0}\widetilde\eta_{a,b}U^aV^b
=\frac{P_0(U,V)}
{(1-U)(1-V)(1-U^{T_a}V^{T_b})}, \tag{15}
\]
with an integer polynomial \(P_0\). To see why the numerator is finite, restrict to a \(3q\)-by-\(3p\) residue class. Its two cone inequalities are integer affine inequalities in nonnegative block coordinates. In one drift case the cone is
\[
j\ge\max(0,2i+x,\lceil(i+x-y)/2\rceil);
\]
in its opposite case it is
\[
0\le j\le\min(2i-x,\lfloor(i-x+y)/2\rfloor).
\]
Each gives an explicit finite head and a rational geometric tail. More specifically, the line where the positive-shift difference in (14) is nonzero intersects that cone in only finitely many nonnegative block cells. The starting strips, including all low columns, become constant along their unbounded axes after finitely many blocks. Multiplication by the diagonal difference and then by \((1-U)(1-V)\) therefore leaves finite support. The other two drift cases exchange the block coordinates. This proves (15) and a genuine cancellation of the large axis-period poles after the complete residue sum. “Primitive” here refers to the block shift \((1,2)\) or \((2,1)\); no irreducibility of the binomial is asserted. ([Explicit cone sums and generating-function proof, (R7)–(R9)](<resonant_models.md>))

**The polynomial numerator carries a real preperiod cost.** Let \(M\ge1\) bound \(|x|\) and \(|x-y|\) for all corrected high base states and uncorrected low base states. With \(P=3q,Q=3p\), the proved safe support bounds are
\[
A_*=P(3M+4)+1,\qquad B_*=Q(3M+4)+4.
\]
Set
\[
\mathcal S=2^{A_*}3^{B_*},\quad
W=2^{T_a}3^{T_b},\quad
D_*=\mathcal S(W-1),\quad N_*=D_*\widetilde Z.
\]
Then \(N_*\in\mathbb Z\) and \(H(N_*:\mathcal S W:\mathcal S)\le6\mathcal S W\). The non-\(\{2,3\}\) part of the reduced denominator divides \(W-1\); it need not equal it. The bare diagonal has logarithmic cost \(3q\log2+o(1)\) along convergents, but the full proved bound is \(\log D_*=O((p+q)M)\). A useful uniformly small clearing exponent has not been obtained. ([Support, denominator, and height bounds, (R10)–(R12)](<resonant_models.md>))

The two exact requested models show why those powers cannot be omitted, even though both have \(M=3\):

| Model | Exact reduced denominator | First floor-disagreement rectangle |
|---|---|---|
| \(7/11\) | \(2^{13}3^5(2^{22}3^7-1)\) | \((19,12)\) |
| \(8/13\) | \(2^{29}3^{24}(2^{13}3^{16}-1)/7\) | \((8,5)\) |

These denominators have 55 and 103 bits. Their full low-column contributions are included, and the reduced powers differ substantially from the nominal diagonal cost. The slopes are not consecutive-convergent models for the actual logarithm; the short displayed windows are not \(q+q',p+p'\) windows. The exact cone formulas were compared independently with finite rectangles and rigorous geometric-tail bounds. ([Exact resonant evaluations](<resonant_models.md>), [targeted certificate](<resonant_models_check.py>))

For a genuine matching rectangle \(a<R,b<S_{\rm win}\), the sufficient integer-discreteness condition is
\[
D_*(2^{-R}+3^{-S_{\rm win}})\longrightarrow0. \tag{16}
\]
Under rationality, the cleared form is \(E=Z\mathcal S W-Z\mathcal S-N_*\); its admissible minimum-unit parameter is \(t=1\). Dividing by \(\mathcal S\) makes the integer term nonintegral. Expanding that term into smaller units must instead pay their minimum-unit scale. Thus rescaling cannot discard the preperiod factor. Even a hypothetical bare cost-three theorem would need appropriate actual resonant supply and nonstabilization; the full construction has additional height obligations. ([Resonant arithmetic criterion and scale audit](<final_return_audit.md>))

Transcendence alone does not even guarantee infinitely many resonances. After five initial \(1\)'s, the last two sums \(s_{n-1},s_n\) are \(2,1\bmod3\). When \(t=s_{n-1}/s_n=2\) in \(\mathbb F_3\), digit \(3\) preserves \(t=2\), while the block \((2,1)\) takes \(2\to1\to2\), without producing a zero sum. Append single-\(3\) blocks except for \((2,1)\) blocks at factorial positions. Every later index is nonresonant and every outgoing ratio is below \(4\). Replacing successive sparse tails by all \(3\)'s gives quadratic approximants of height \(O(16^{m_j})\) and error \(O(2^{-m_{j+1}})\); the same resultant argument proves this countermodel transcendental. It lies in the admissible slope interval. Consequently an arbitrary resonant-only improvement combined with the present nonresonant threshold-five model has no universal transcendence-based coverage. This is a counterexample to that inference, not a statement about the actual continued fraction of \(\log_3 2\). ([No-resonance countermodel and proof](<final_return_audit.md>))

## Actual dynamics bound fixed raw winners and leave rotating returns open

The final attack studies the actual cocycle rather than a rational model. Put
\[
W(T)=\sum_{j=0}^{2}\omega^j K_j(e^T).
\]
The exact strip recurrence is
\[
W(T+\log2)=\omega W(T)+S\!\left(\left\lfloor
\frac{T+\log2}{\log3}\right\rfloor\right),
\]
where \(S\) takes values \(1,-\omega,0\). If the same fixed raw color minimizes the adjusted counts at \(T,T+\log2,T+2\log2\), rotate that color to zero and write \(W(T)=x+y\omega\). Each minimizing test gives \(x\le1,\ x-y\le1\), including the bounded isolated/patch corrections. Applying the next two tests through the strip recurrence gives
\[
-2\le x\le1,\qquad -2\le y\le3,\qquad |W(T)|\le5. \tag{17}
\]
The correction indicators need not remain constant. ([Three-cutoff argument](<ray_return_attack.md>))

Sampling every three doublings gives the exact rotation cocycle
\[
\begin{aligned}
W(T+3n\log2)-W(T)&=\sum_{k=0}^{n-1}\Phi(x_0+k\alpha),\\
x_0&=T/(3\log3)\bmod1,\\
\Phi(x)&=\sum_{s=1}^{3}\omega^{-s}S(\lfloor3x+s\alpha\rfloor).
\end{aligned} \tag{18}
\]
The saved reduction to the thirds-interval discrepancy and Kesten's bounded-remainder criterion establish unbounded phase-zero sums for this precise cocycle. **Every phase has unbounded sums.** Otherwise a bound \(M\) at one phase would, by subtracting its prefixes, bound all forward orbit-start sums by \(2M\). For each fixed length, the phase-zero prefix sum is locally constant in a continuity cell; the exact breakpoint calculation shows that its orbit hits none of the breakpoints. Density would then bound every phase-zero prefix by \(2M\), a contradiction. ([Actual-cocycle reduction and proof](<ray_return_attack.md>), [Kesten's article](https://geodesic.mathdoc.fr/articles/10.4064/aa-12-2-193-212/), [Kelly–Sadun, Theorem 1](https://arxiv.org/html/1404.0455))

This upgrades to **uniform finite escape**: for each \(M\), there is finite \(N(M)\) such that every phase has a prefix of length at most \(N(M)\) whose sum exceeds \(M\). If arbitrarily long bounded prefixes existed, compactness would give a consistently one-sided limiting itinerary with all prefixes bounded. Along an irrational orbit each of the finitely many breakpoints is hit at most once, so this itinerary differs from the specified endpoint code by a uniformly bounded total error. It would produce an actual phase with bounded sums, contradicting the preceding argument. If a fixed raw winner persisted throughout \([T_0,T_0+L]\), (17) would bound the sampled differences in (18) by \(10\), hence
\[
\boxed{L<(3N(10)+2)\log2.} \tag{19}
\]
The bound depends on the fixed slope, not on \(T_0\); it is non-effective here. It rules out arbitrarily long windows with one fixed raw winner. It does not rule out a winner rotating in the frame \(V_n=\omega^{-n}W(T_0+n\log2)\), or switching between sampled cutoffs. Those switches are precisely where the weighted ray responses enter. ([Uniform escape proof and final audit](<final_return_audit.md>))

A hypothetical rotating excursion must also control its starting time. Suppose a coefficient model takes values in a fixed finite rational alphabet, has a full weighted sum with a fixed rational denominator, and agrees with all true events in \(e^{T_0}<d<e^{T_0+L}\). The rational alphabet supplies a common denominator for the model's finite head; rationality of its total alone would not do so. Keeping the exact true head therefore gives a denominator dividing a fixed multiple of
\[
\Lambda(T_0)=2^{\lfloor T_0/\log2\rfloor}
3^{\lfloor T_0/\log3\rfloor},\qquad
\log\Lambda(T_0)=2T_0+O(1).
\]
The integer-cleared form can use \(t=1\) and has height at most \(\exp(2T_0+O(1))\). The elementary tail bound then gives cleared error at most
\[
C(T_0+L+1)e^{T_0-L}. \tag{20}
\]
For this bound to tend to zero, the correct sufficient discreteness condition is
\[
\boxed{L-T_0-\log(T_0+L+1)\to+\infty.} \tag{21}
\]
The fixed exponential margin \(L-T_0\ge\eta L\) is stronger and suffices for the exponential estimate in (4); nonvanishing would still be separate. Merely \(L-T_0\to\infty\) is insufficient for (20): \(T_0=L-\tfrac12\log L\) leaves a growing bound. No suitable rotating model with a proved weighted switch description and the required starting-time relation has been constructed. Adjustable cutoff phase is not a freely assignable initial lattice state, and a scalar heavy-point theorem does not supply the two simultaneous cone inequalities and their weighted switches. ([Finite-head calculation with the rational-alphabet hypothesis](<ray_return_attack.md>), [sharpened discreteness condition](<final_return_audit.md>), [scope of Ralston's scalar theorem](https://arxiv.org/pdf/1106.0577))

The validation record separates exact checks from infinite proofs. The current audit independently reconstructed the \(53/84\) numerator and its gcd, checked the swap formulas, and reproduced both named resonant evaluations. The narrow certificate sources check the two affine partitions, three specified centers and low-column failures, rational cone sums with exact tail bounds, and the strip recurrence at fifty integer cutoffs. The weighted note also records finite checks of the Hessians and every retained sign in (10). These checks support the written proofs and expose incorrect shortcuts; no finite sample supplies an infinite-return theorem. The primary tools have correspondingly limited roles: Elsner gives restricted approximation, Gelfond–Schneider classifies the logarithmic slope, Kesten gives the unbounded-remainder input, and KK gives a lower bound only after the required arithmetic form is available. None of those sources asserts the missing actual-rotation ray theorem. This synthesis adds no research or experiments and makes no irrationality, novelty, Lean, or external-review claim. ([Final audit](<final_return_audit.md>), [skew certificate](<skew_denominator_check.py>), [resonant certificate](<resonant_models_check.py>), [actual-ray certificate](<ray_return_check.py>))

## Conclusion

The strongest new direction is the gap between a genuinely low-degree interior identity and the arithmetic complexity stored in its weighted boundaries. The sharp supply theorem makes the quantitative target concrete: a replacement with effective clearing exponent below \((25+\sqrt5)/10\) would fit the proved supply, provided its coefficient, minimum-unit, and nonzero-error obligations also hold. The exact \(53/84\) denominator and the resonant preperiod factors identify why the current symmetries do not yet achieve that target. The continued-fraction countermodels prevent replacing the missing slope-specific argument by a generic appeal to transcendence.

The next required theorem concerns the **actual logarithmic rotation and its weighted ray or switching returns**, with arithmetic compression and height proved together. Alternatively, the scalar route needs the actual infinite supply in (3) and a nonstabilization theorem; the resonant route needs full denominator control, suitable infinite supply, and nonstabilization. None of these packages is complete. The auxiliary results are established advances, while the user's infinite-return objective remains unresolved and active.
