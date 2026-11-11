# Independent audit of the axis-avoiding classification and coefficient extension

Audit completed 7 November 2026. The current authoritative versions of `multiroot.md` and `coefficient_extension.md` were reread, and the arithmetic input was checked directly against the primary paper. Both central proofs pass the independent derivations below. This is an audit of those statements, not a proof of the global finite optimum, a proof of irrationality, a novelty claim, or a Lean verification. No computational sweep was used.

## Does the critical-set argument classify every set avoiding the vertical axis?

### Takeaway

Yes. The strict owner-neighborhood inequality, the predecessor cone, and the three successive strip counts are valid. They classify every inclusion-minimal positive-deficiency set avoiding the vertical axis as an isolated horizontal root or the stated three-label patch; connectedness and hole-freeness are unnecessary. [Audited argument](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>).

### Cited Findings

- The finite board is \(D_t=\{2^a3^b\le t:a,b\ge0\}\), with color \(a-b\pmod3\); the corner matching reduction and the construction indicators are defined in [168_grid.md](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>).
- The proof under review uses inclusion-minimal positive deficiency and a minimum bipartite vertex cover. It does not assume the stronger-looking but unproved claim that different horizontal roots supply disjoint augmenting paths. [multiroot.md](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>).

### Inferences

The following independently reconstructs the proof in the cited note. Fix one color \(j\), put \(U\subset C_j(D_t)\), and suppose every owner in \(U\) has \(a\ge1\). Let \(B(U)\) have left color \(j+1\), right color \(j+2\), and deficiency \(d(U)=|U|-\nu(B(U))\).

#### Incidence and criticality

The three owned edges, including their availability, are

\[
N(u)=(u/3,2u/3)\quad(b\ge1),\qquad
E(u)=(3u/2,u/2)\quad(a\ge1, 3u\le2t),\qquad
R(u)=(2u,3u)\quad(3u\le t).
\]

Solving these endpoint equations gives the complete owner lists:

\[
\begin{array}{c|ccc}
\text{physical vertex}&\text{first possibility}&\text{second possibility}&\text{third possibility}\\\hline
\text{left }l&R(l/2)&E(2l/3)&N(3l)\\
\text{right }r&R(r/3)&N(3r/2)&E(2r).
\end{array}
\]

Only owners in \(U\) with available edges contribute. In particular, formally smooth expressions with negative exponents, owners outside \(U\), and endpoints beyond \(t\) cannot be counted as actual edges.

Suppose \(U\) is critical, meaning \(d(U)>0\) and no proper subset has positive deficiency, and set \(m=|U|\). For each \(u\in U\), criticality and matching monotonicity give

\[
m-1\le\nu(B(U\setminus\{u\}))\le\nu(B(U))<m.
\]

Thus \(\nu(B(U))=m-1\). By the bipartite matching-cover theorem there is a minimum vertex cover \(W\) of size \(m-1\).

Each \(w\in W\) must uniquely cover edges of at least two distinct owners. If it uniquely covers none, removing it preserves a cover and contradicts minimality of \(W\). If it uniquely covers only one owner \(u\), then \(W\setminus\{w\}\) covers \(B(U\setminus\{u\})\), giving that proper subset deficiency at least one. Here \(w\in W\) implies \(m\ge2\), so the remainder is nonempty. A leaf is consequently outside \(W\).

For nonempty \(S\subset W\), define \(T(S)\) to contain owners of **all** edges incident with \(S\), not just uniquely covered edges. Essentiality makes \(T(S)\) nonempty, and \(W\setminus S\) covers \(B(U\setminus T(S))\). If \(T(S)\ne U\), the contrary inequality \(|T(S)|\le|S|\) would give

\[
d(U\setminus T(S))\ge (m-|T(S)|)-(m-1-|S|)
=1+|S|-|T(S)|>0.
\]

If \(T(S)=U\), the same contrary inequality is impossible directly, since \(|T(S)|=m>|W|\ge|S|\). Thus the empty remainder is handled without applying criticality to it, and

\[
|T(S)|\ge |S|+1. \tag{A1}
\]

#### Predecessors and the cone

Let \(u\in U\) have \(a,b\ge1\), and suppose none of \(u/6,2u/9,3u/4\) belongs to \(U\). The left endpoint \(u/3\) of \(N(u)\) is then a leaf. Hence \(2u/3\in W\). At that right vertex, essentiality forces \(E(4u/3)\) to be uniquely covered, so its opposite endpoint \(2u\notin W\). Its availability gives \(2u\le t\), and therefore \(E(u)\) is available because \(a\ge1\).

Now the right endpoint \(u/2\) of \(E(u)\) is a leaf, so \(3u/2\in W\). Essentiality there forces \(N(9u/2)\) uniquely, whence \(3u\notin W\). Its owner satisfies \(9u/2\le t\), so \(R(u)\) exists with both endpoints outside \(W\), a contradiction. Therefore one of those three smaller predecessors is in \(U\).

Every descending predecessor chain terminates at a horizontal root, since all labels avoid the vertical axis. The smallest label is \(x=2^A\), \(A\ge1\). Any other horizontal root has the same color and is \(x8^\ell\), \(\ell\ge0\). With

\[
g=4/3,\qquad q=9/2,\qquad gq=6,\qquad g^2q=8,
\]

reversing predecessor steps shows that every owner has a representation

\[
u=xg^r q^s,\qquad r,s\ge0,\qquad
a=A+2r-s\ge1,\quad b=2s-r\ge0. \tag{A2}
\]

The exponent matrix has determinant three, so the representation is unique. In particular, an expression with \(r=-1\) cannot secretly equal an allowed owner. This cone conclusion includes all horizontal roots; it does not presuppose a single root.

#### Terminal ray and first strip

If \(x>2t/3\), it has no owned edge and criticality gives \(U=\{x\}\). Otherwise define

\[
u_n=xq^n,\quad v_n=xgq^n,\quad w_n=xg^2q^n,\quad z_n=xg^3q^n.
\]

Whenever \(u_n\in U\) has \(E(u_n)\), the alternative owners at its right endpoint \(u_n/2\) are \(xg^{-1}q^{n-1}\) and \(xg^{-1}q^n\), forbidden by (A2). That endpoint is a leaf. Thus \(L_n=3u_n/2\in W\), and essentiality at \(L_n\) forces \(N(u_{n+1})\) uniquely, with \(3u_n\notin W\).

Iteration must terminate because \(U\) is finite and \(q>1\). It cannot terminate by reaching \(a=0\): while \(E(u_n)\) is available, the next owner is forced to lie in the axis-avoiding \(U\). The terminal owner therefore satisfies

\[
u_0,\ldots,u_k\in U,\qquad k\ge1,\qquad 2t/3<u_k\le t,\qquad A-k\ge1. \tag{A3}
\]

For \(n<k\), \(u_n\le u_k/q\le2t/9\), so \(R(u_n)\) is available. As its right endpoint \(3u_n\notin W\), its left endpoint \(A_n=2u_n\in W\).

Let \(S_0=\{L_n,A_n:0\le n<k\}\). The complete possible owner lists are

\[
L_n:\ u_n,u_{n+1};\qquad A_n:\ u_n,v_n,v_{n+1}.
\]

Since \(v_0\) has \(b=-1\), (A1) and \(|S_0|=2k\) force all \(2k+1\) owners \(u_0,\ldots,u_k,v_1,\ldots,v_k\) to occur. Hence

\[
2t/3<u_k\le3t/4,\qquad 8t/9<v_k\le t. \tag{A4}
\]

#### First backward induction and second strip

For \(1\le n\le k\), \(N(v_n)\) has left endpoint \(v_n/3=A_{n-1}\in W\). Write \(\beta_n=2v_n/3\). Its three possible owners are

\[
R(v_{n-1}),\quad N(v_n),\quad E(w_n).
\]

If \(\beta_n\in W\), its north edge is doubly covered, so essentiality requires both other owned edges to be uniquely covered. In particular \(E(w_n)\) forces \(2v_n\notin W\). But \(w_k=g^2u_k>32t/27>t\), so the necessary edge \(E(w_k)\) is absent, proving \(\beta_k\notin W\).

For \(n<k\), \(v_n\le v_k/q\le2t/9\), so \(R(v_n)\) is available. The implication

\[
\beta_n\in W\ \Longrightarrow\ 2v_n\notin W
\ \Longrightarrow\ 3v_n=\beta_{n+1}\in W
\]

propagates backward from the cap to give \(\beta_1,\ldots,\beta_k\notin W\). Consequently \(B_n=2v_n\in W\) for \(1\le n<k\).

Set \(S_1=S_0\cup\{B_n:1\le n<k\}\), of size \(3k-1\). Each \(B_n\) has possible owners \(v_n,w_n,w_{n+1}\). Since \(w_k>t\), its whole owner neighborhood is contained in the \(3k\) labels

\[
\{u_0,\ldots,u_k\}\cup\{v_1,\ldots,v_k\}\cup\{w_1,\ldots,w_{k-1}\}.
\]

Inequality (A1) forces every displayed label into \(U\). If \(k\ge2\), this includes the second horizontal root \(w_1=8x\).

#### Second backward induction and third strip

Assume \(k\ge2\). For \(1\le n<k\), the rooted edge \(R(w_n)\) is available, because

\[
w_n\le w_{k-1}=(g^2/q)u_k=(32/81)u_k\le8t/27<t/3.
\]

For \(2\le n<k\), \(N(w_n)\) has left endpoint \(w_n/3=B_{n-1}\in W\). Put \(\gamma_n=2w_n/3\), \(2\le n\le k\). Its possible owners are

\[
R(w_{n-1}),\quad N(w_n),\quad E(z_n).
\]

At \(n=k\), the last two owners are beyond the board. The vertex \(\gamma_k=3w_{k-1}\) nevertheless exists as an endpoint of \(R(w_{k-1})\); it is a leaf and is outside \(W\). For \(2\le n<k\), membership \(\gamma_n\in W\) would doubly cover the north edge, force the other two edges uniquely, imply \(2w_n\notin W\), and then force \(3w_n=\gamma_{n+1}\in W\). Backward induction gives \(\gamma_2,\ldots,\gamma_k\notin W\), and therefore \(C_n=2w_n\in W\) for every \(1\le n<k\).

The assertion for \(n=1\) uses \(R(w_1)\) and \(\gamma_2\notin W\); it does **not** use a nonexistent \(N(w_1)\). This resolves the horizontal-root boundary of the induction.

Let \(S_2=S_1\cup\{C_n:1\le n<k\}\). Its size is \(4k-2\). Each new vertex has possible owners \(w_n,z_n,z_{n+1}\). The bottom expression \(z_1\) has \(b=-1\), while \(z_k=gw_k>t\). Consequently

\[
T(S_2)\subset
\{u_0,\ldots,u_k\}\cup\{v_1,\ldots,v_k\}\cup
\{w_1,\ldots,w_{k-1}\}\cup\{z_2,\ldots,z_{k-1}\}.
\]

The upper bound is \((k+1)+k+(k-1)+(k-2)=4k-2=|S_2|\), contradicting (A1). At \(k=2\), the last range is empty, the second backward induction consists only of its leaf cap, and the incompatible bounds remain \(|T(S_2)|\le6\) and \(|T(S_2)|\ge7\). No induction over an empty interval is being used to force an additional fact.

All these cardinalities are exact where claimed. Dividing \(L_n,A_n,B_n,C_n\) by \(2x\) gives \(g^r q^n\) with \(r=-1,0,1,2\), respectively. The same determinant-three calculation proves distinctness of every selected vertex. Owner columns have \(r=0,1,2,3\) and are likewise distinct. The boundary condition \(A-k\ge1\) ensures no asserted owner accidentally crosses the vertical axis.

#### The surviving case \(k=1\)

It forces \(\{x,9x/2,6x\}\subset U\) with

\[
6x\le t<27x/4,\qquad A\ge2.
\]

In this window the owned graph of these three labels has precisely the four edges \(E(x),R(x),N(9x/2),N(6x)\). They form the path

\[
x/2\;--\;3x/2\;--\;3x\;--\;2x\;--\;4x.
\]

The two left vertices cover every edge, and \(E(x),N(6x)\) give a matching of size two. Thus the three-label subset has deficiency one, forcing equality with \(U\) by criticality. Its proper subsets have nonpositive deficiency: any pair containing \(x\) has the two disjoint edges \(E(x),R(x)\), and the remaining pair has disjoint north edges. The singleton and patch descriptions therefore give the exact critical classification, including their converse.

### Gaps

No gap was found in this classification. Its proof uses \(a\ge1\) essentially when it makes \(E(u)\) available in the predecessor argument; it establishes no classification for vertical-touching critical sets. It is independent of the conjectural global formula (C), and it does not justify removing the vertical-axis hypothesis. [Scope of the audited statement](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>).

## Does the classification give the stated bound for arbitrary sets and covers?

### Takeaway

Yes: for \(t\ge3\), every \(U\subset C_j(D_t)\) avoiding the vertical axis satisfies \(d(U)\le I_j(t)+P_j(t)\). The prescribed-phase cover lower bound follows, but the small patch rooted at \(x=2\) makes a claimed constrained equality false in that one window. The audited note already preserves that exception. [multiroot.md](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>).

### Cited Findings

- The isolate interval is \(2t/3<x\le t\), and the patch interval is \(4t/27<x\le t/6\) for pure powers \(x=2^A\), \(A\ge1\). The indicators record the color of this root. [Construction definitions](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>).
- The current note limits its global conclusion to covers containing a complete vertical color phase and explicitly leaves the existence of a global minimum of that form unproved. [Audited cover consequence](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>).

### Inferences

Each exceptional interval has multiplicative width less than two, so contains at most one power of two. If a patch root \(x\) exists, then \(6x\le t<27x/4<8x\); the largest power of two at most \(t\) is \(4x\le2t/3\). Thus an isolate cannot coexist with a patch. There is at most one exceptional root over all colors.

Fix \(j\) and set \(\delta_j=I_j+P_j\in\{0,1\}\). Every positive-deficiency finite \(U\) contains an inclusion-minimal positive subset. If \(\delta_j=0\), the classification precludes such a subset, proving \(d(U)\le0\). If \(\delta_j=1\) with exceptional root \(x\), every critical subset of this color must contain \(x\). Hence \(U\setminus\{x\}\) has nonpositive deficiency. This gives

\[
\nu(B(U))\ge\nu(B(U\setminus\{x\}))\ge|U\setminus\{x\}|\ge|U|-1.
\]

This reasoning also covers \(x\notin U\), disconnected \(U\), holes, and \(U=\varnothing\). It proves the stated inequality without summing deficiencies over components or combining incompatible critical and hole-normalized representatives.

If \(F\subset D_t\) meets every corner and contains all vertical-axis vertices of color \(j\), then \(U=C_j\setminus F\) avoids the vertical axis. Every edge of \(B(U)\) must meet \(W=F\setminus C_j\), since the corner's color-\(j\) vertex is omitted. Therefore

\[
|F|=K_j-|U|+|W|\ge K_j-|U|+\nu(B(U))\ge K_j-I_j-P_j. \tag{A5}
\]

When there is no correction, the color class attains this bound. Removing the isolate also preserves the required vertical phase. For a patch with \(A\ge2\), all three removed owners avoid the vertical axis, so the known replacement preserves it too.

For \(x=2\), however, the removed owner \(9x/2=9\) lies on the vertical axis. In its window \(12\le t<27/2\), color \(j=1\) has no critical axis-avoiding subset at all, so the sharper constrained lower bound is \(K_1\), attained by \(C_1\). For example, at \(t=12\), \(K_1=3\) and \(P_1=1\). A cover forced to contain the vertical vertex \(9\) cannot have size two: its remaining point would need to meet the three corners with roots \(1,2,4\), whose common intersection is empty. The cover \(\{2,4,9\}\) attains size three. Thus the constrained optimum is \(3\ne K_1-P_1=2\). This is a direct small check, not a solver inference. It confirms the exception in the current note and prevents importing an unqualified constrained-equality statement from older notes.

Finally, the \(t=18\) example is valid. Its five corner roots are \(1,2,3,4,6\). Both \(\{2,6,12\}\) and \(\{1,4,6\}\) meet all five corners. A two-point cover must choose a point of \(\{1,2,3\}\). Choosing 1 leaves four corners with no common second point; choosing 2 leaves the disjoint corners rooted at 3 and 4; choosing 3 leaves the corners rooted at 2, 4, and 6 with empty common intersection. Thus both displayed size-three covers are minimum. The first contains none of \(1,3,9\), while the second contains the complete vertical phase of color zero. The proposed normalization can only be existential.

### Gaps

The audit does not establish that **some** global minimum contains a complete vertical color phase. That statement, or a comparison controlling vertical-touching critical sets against another adjusted color class, remains the exact additional combinatorial obligation needed to pass from (A5) to the global formula. Neither the classification nor (A5) assumes (C). Any later arithmetic use of (C) remains conditional until this obligation is proved. [Remaining obligation in multiroot.md](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>).

## Is the Subspace-Theorem bound uniform in the coefficient size?

### Takeaway

Yes. Both the pure and mixed inductions are valid, with constants independent of \(B\). For a fixed number \(m\) of terms, replacing S-units by integer multiples of size at most \(B\) yields precisely the asserted loss \(B^{-m-\epsilon}\), with signs and zero coefficients handled as stated. [Audited extension](<../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md>).

### Cited Findings

The primary source defines projective height by the product of local coordinate maxima and permits S-integer vectors in its one-form Subspace Theorem. Specializing Theorem 1 to \(K=\mathbb Q\), the real distinguished place, fixed rational \(L\), and a distinguished coordinate with nonzero coefficient gives finitely many proper rational subspaces containing all solutions of

\[
|L(\mathbf z)|\prod_{\substack{(i,v)\in\{1,\ldots,n\}\times S^*\\(i,v)\ne(k,\infty)}}|z_i|_v
\le H(\mathbf z)^{-\epsilon},\qquad n\ge2,\quad S^*=\{\infty\}\cup S.
\]

This is the exact input used below; it requires S-integers, not S-units. The source was reread directly, including the height and absolute-value conventions preceding the theorem. [Luca–Ouaknine–Worrell, *Transcendence of Hecke-Mahler Series*, arXiv:2412.07908v2, Section 2 and Theorem 1](https://arxiv.org/html/2412.07908v2#S2.Thmtheorem1).

### Inferences

The following reconstructs the argument of [coefficient_extension.md](<../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md>) from that input. Fix the finite prime set \(S\), dimension \(m\), rational coefficients \(d_i\), and exponent \(\epsilon>0\). These are fixed throughout; \(B,N,x_i,t\) may vary.

#### Heights and admissible coordinates

For nonzero \(x\in\mathbb Z[1/p:p\in S]\),

\[
A_S(x)=|x|\prod_{p\in S}|x|_p
\]

is the positive S-free numerator of \(x\) in lowest terms and is at least one. If a nonzero coordinate is retained, deleting other coordinates decreases each local maximum, so it cannot increase projective height. The resulting product still has only finitely many nonunit factors. In particular, a single-coordinate projective height \(H([x])\) is one by the product formula. This should not be confused with the affine scalar height \(H([1:x])\).

All invocations of the theorem have dimension at least two. Pure dimension one and mixed dimension zero are handled directly; mixed dimension \(m\ge1\) uses \(m+1\ge2\) coordinates. The prime set need not be enlarged when integer coefficients introduce numerator primes outside \(S\).

#### Pure induction

Assume \(x_i\ne0\), \(A_S(x_i)\le B\), \(B\ge1\), and \(0<t\le\min(1,|x_i|)\). For a nonzero pure form \(E=\sum d_ix_i\), the desired statement is

\[
|E|\ge C_PtB^{-m}H(\mathbf x)^{-\epsilon}. \tag{A6}
\]

It is vacuous when all \(d_i=0\), and at \(m=1\) follows with \(C_P=|d_1|\) when \(d_1\ne0\). For \(m\ge2\), select \(k\) with \(d_k\ne0\). The product in the primary theorem is exactly

\[
\Phi_P=\frac{|E|}{|x_k|}\prod_{i=1}^m A_S(x_i)
\le (|E|/t)B^m.
\]

Outside its finite family of exceptional subspaces, this is greater than \(H(\mathbf x)^{-\epsilon}\), proving (A6) with constant one. Enlarge each exceptional rational subspace to a fixed rational hyperplane \(\sum a_ix_i=0\), choose \(a_\ell\ne0\), and eliminate \(x_\ell\). The form becomes

\[
E=\sum_{i\ne\ell}(d_i-d_\ell a_i/a_\ell)x_i.
\]

The retained coordinates themselves have not changed. Their S-free numerators are still bounded by the same \(B\), their absolute values still exceed \(t\), and their height is at most the original height. Induction in dimension \(m-1\) gives the stronger loss \(B^{-(m-1)}\), hence (A6). If the reduced form is zero identically, that branch has no admissible \(E\ne0\). If a hyperplane forces a nonzero coordinate to vanish, its admissible set is empty. Taking the minimum of one and the finitely many nonvacuous branch constants gives a positive constant independent of \(B\). Proving the assertion for all rational coefficient vectors at each dimension makes every eliminated coefficient vector a legitimate induction instance.

#### Mixed induction

For \(E=\sum d_ix_i-N\ne0\), \(N\in\mathbb Z\), the claimed bound is

\[
|E|\ge C_MtB^{-m}H(N:\mathbf x)^{-\epsilon}. \tag{A7}
\]

At \(m=0\), the nonzero integer \(-N\) has absolute value at least one. At \(m\ge1\), \(N=0\) follows from the already proved pure statement; adjoining a zero coordinate leaves the height unchanged.

For \(N\ne0\), apply the primary theorem to \((N,x_1,\ldots,x_m)\), with \(N\) distinguished and coefficient \(-1\). Its product is

\[
\Phi_M=|E|\left(\prod_{p\in S}|N|_p\right)\prod_i A_S(x_i)
\le |E|B^m,
\]

because \(N\) is an integer. There is no real factor \(|N|\) in this product, since the real distinguished coordinate is excluded. Outside the exceptional hyperplanes this gives (A7) with constant one, using \(t\le1\).

On \(a_0N+\sum a_ix_i=0\), if \(a_0\ne0\), eliminate \(N\) and use the pure dimension-\(m\) assertion for coefficients \(d_i+a_i/a_0\). This retains the exponent \(-m\) and decreases height. If \(a_0=0\), eliminate some \(x_\ell\) and use the mixed dimension-\(m-1\) assertion with the integer \(N\) unchanged. This decreases height and improves the B-exponent. As in the pure induction, a finite minimum of constants works uniformly for every \(B,N,t,\mathbf x\). The order “all pure dimensions first, then mixed induction” removes any circular dependence.

#### Integer coefficients, zero supports, and the exact exponent

Let \(B\ge1\), let \(u_i>0\) be rational S-units, and let \(c_i\in\mathbb Z\) satisfy \(|c_i|\le B\). On a nonzero support put \(x_i=c_iu_i\). Then

\[
A_S(x_i)=A_S(c_i)\le|c_i|\le B,\qquad |x_i|\ge u_i\ge t.
\]

At every finite place, multiplication of each individual coordinate by an integer weakly decreases the local maximum. At the real place it increases it by at most \(B\); the unchanged \(N\) coordinate also satisfies that upper bound since \(B\ge1\). Therefore

\[
H(N:c_1u_1:\cdots:c_mu_m)\le B H(N:u_1:\cdots:u_m).
\]

Substitution into (A7) gives

\[
\left|\sum_i d_ic_iu_i-N\right|
\ge Ct B^{-m-\epsilon}H(N:u_1:\cdots:u_m)^{-\epsilon}, \tag{A8}
\]

provided the expression is nonzero. This accounts separately for \(B^{-m}\) from S-free numerators and \(B^{-\epsilon}\) from the height change; neither factor is missing.

If some \(c_i=0\), delete those coordinates before invoking (A7). A support of size \(r\le m\) has loss \(B^{-r-\epsilon}\ge B^{-m-\epsilon}\) and no larger height. There are finitely many supports, so their constants have a positive minimum. The empty support is a nonzero integer case, or is excluded by nonvanishing. Negative \(c_i\), negative \(x_i\), and zero fixed or eliminated coefficients cause no problem: every size estimate uses absolute values, and the induction explicitly allows zero coefficient vectors when its nonzero condition makes them vacuous.

Consequently, for fixed \(m,S,d_i\), height at most \(e^{C_0L}\), coefficient size \(B_L=e^{o(L)}\), and nonzero error at most \(t_Le^{-\eta L}\), choosing \(C_0\epsilon<\eta\) makes (A8) contradictory for sufficiently large \(L\). This conclusion needs an unbounded family of **nonzero** errors; identically zero returns are not excluded by it.

The external-height formulation also checks. Applying (A6) or (A7) with exponent \(\epsilon/2\), \(B=\mathscr H^\delta\), and \(\mathscr H\ge\max(2,H)\), gives

\[
|E|\ge Ct\mathscr H^{-m\delta-\epsilon/2}\ge Ct\mathscr H^{-\epsilon}
\quad\text{if }\delta\le\epsilon/(2m).
\]

For nonempty admissible coordinates, \(A_S(x_i)\ge1\) already forces \(\delta\ge0\). The external height can be retained under elimination; the proof never needs a lower bound on the growth of a shortened vector's height.

### Gaps

No gap was found in the uniform coefficient estimate. A standalone statement of the integer-coefficient corollary should explicitly repeat \(B\ge1\), as done above; the main theorem already imposes it. The estimate is a consequence of the cited established Subspace Theorem, not conditional on (C), and its constants remain qualitative and ineffective in this argument. The number of coordinates, prime set, rational coefficient vector, and exponent must remain fixed. It does not establish a bounded-term return representation, an exponential saving, or nonvanishing for either Erdős target; these are separate application obligations. No global boundary proof or Lean formalization was attempted in this audit round. [Scope of the coefficient extension](<../../early-attacks/augmentation-and-return-attacks/coefficient_extension.md>).
