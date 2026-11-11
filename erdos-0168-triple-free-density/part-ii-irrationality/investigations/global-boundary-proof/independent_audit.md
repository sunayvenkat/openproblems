# Independent audit of the axis-avoiding classification and return model

Audit completed 7 November 2026. Scope: the ordinary mathematical claims in `multiroot.md` and `returns.md` from the preceding round, their definitions, the supplied return checker, and the cited primary arithmetic proposition. This audit does not investigate new vertical-axis configurations or claim the global finite optimum. No earlier file was edited.

**Verdict.** The general axis-avoiding critical-set classification and its deficiency corollary pass independent derivation. The return argument passes with two explicit scope corrections: require **\(1\le Y<X\)** in the tail estimate, and **\(3/5<p/q<2/3\)** in the rational model. The corrected statement is given below. Neither correction affects sufficiently late convergents or the conditional implication. The global formula (C), an infinite suitable long-return sequence, and nonvanishing remain separate missing inputs.

## Does the general axis-avoiding critical classification hold?

### Takeaway

Yes. The strict expansion inequality for owners, the predecessor cone, and all three selected-vertex counts are valid. The proof includes the \(k=2\) case and uses no disjoint-path assumption, hole normalization, or restriction on the number of horizontal roots.

### Cited Findings

* The audited definitions, criticality argument, four formal columns, classification, and constrained-cover corollary are in [multiroot.md](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>).
* The board and original corner-cover reduction are in [168_grid.md](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>). The present proof is checked directly below rather than inferred from the earlier single-root result in [boundary.md](<../boundary-and-arithmetic/boundary.md>).

### Inferences

**Incidence and availability.** Write \(D_t=\{2^a3^b\le t:a,b\ge0\}\), color \(a-b\pmod3\), and let \(U\) have one fixed color. For an owner \(u\), its three possible edges between the other colors are

\[
N(u)=(u/3,2u/3),\quad E(u)=(3u/2,u/2),\quad R(u)=(2u,3u).
\]

They exist respectively when \(b\ge1\), when \(a\ge1\) and \(3u/2\le t\), and when \(3u\le t\). Inverting these endpoint formulas gives exactly

\[
\begin{array}{c|ccc}
\text{vertex}&\multicolumn{3}{c}{\text{possible owners}}\\\hline
l\text{ left}&R(l/2)&E(2l/3)&N(3l)\\
r\text{ right}&R(r/3)&N(3r/2)&E(2r).
\end{array}
\]

Each list is complete. Invalid smooth labels and unavailable edges are omitted, never implicitly added. The nonnegative-coordinate constraints are essential at the starts of the later columns.

**Criticality and strict expansion.** Let \(m=|U|\), and suppose \(U\) is inclusion-minimal with \(d(U)=m-\nu(B(U))>0\). Deleting any owner gives matching number at least \(m-1\), so \(\nu(B(U))=m-1\). A minimum vertex cover \(W\) consequently has size \(m-1\).

Every \(w\in W\) uniquely covers edges from at least two owners. If it uniquely covers none, it is redundant. If all its uniquely covered edges have one owner \(u\), then \(W\setminus\{w\}\) covers \(B(U\setminus\{u\})\), giving deficiency at least one for that proper subset. Both alternatives are impossible. In particular a leaf cannot lie in \(W\).

For nonempty \(S\subseteq W\), let \(T\) contain every owner of every edge incident to \(S\), including doubly covered edges. Removing \(T\) leaves a graph covered by \(W\setminus S\). If \(T\ne U\) and \(|T|\le|S|\), its deficiency is at least

\[
(m-|T|)-((m-1)-|S|)=1+|S|-|T|>0.
\]

The remaining owner set is nonempty and proper: \(T\ne\varnothing\) follows from essentiality. If \(T=U\), then \(|T|=m>|S|\) follows from \(|S|\le m-1\). Hence in all cases

\[
\boxed{|T|\ge |S|+1.}\tag{A1}
\]

The all-incident-owner definition is sufficient for this deletion proof; it does not require every edge at \(S\) to be uniquely covered.

**Predecessor and cone.** Assume every owner avoids \(a=0\). For \(u\in U\) with \(b\ge1\), suppose none of \(u/6,2u/9,3u/4\) belongs to \(U\). Then \(u/3\) is a leaf of \(N(u)\), forcing \(2u/3\in W\). Essentiality there forces \(E(4u/3)\) uniquely, hence \(2u\notin W\) and \(2u\le t\). Thus \(E(u)\) exists: smoothness uses \(a\ge1\).

Its right endpoint \(u/2\) is also a leaf, forcing \(3u/2\in W\). Essentiality forces \(N(9u/2)\) uniquely, so \(3u\notin W\) and \(9u/2\le t\). Therefore \(R(u)\) exists with both endpoints outside \(W\), a contradiction. At least one of the three predecessors is in \(U\).

All predecessors are smaller. Every descending chain therefore ends at \(b=0\); it cannot end at \(a=0\). The smallest owner is a horizontal root \(x=2^A\), \(A\ge1\). Every other root is \(x8^\ell\), \(\ell\ge0\), because the color is fixed. Put \(g=4/3\), \(q=9/2\). Reversing predecessors multiplies by \(g,q,gq\), and \(8=g^2q\). Hence every owner has the unique form

\[
xg^m q^n,\qquad m,n\ge0,\qquad
a=A+2m-n\ge1,\quad b=2n-m\ge0.\tag{A2}
\]

Uniqueness follows from the nonsingular exponent matrix with columns \((2,-1)\) and \((-1,2)\). A negative \(m\) is forbidden even when the resulting rational number happens to be a smooth integer on the board.

**The first forced ray.** If \(x>2t/3\), it has no edge, so criticality gives \(U=\{x\}\). Otherwise set

\[
u_n=xq^n,\quad v_n=xgq^n,\quad w_n=xg^2q^n,\quad z_n=xg^3q^n.
\]

Whenever \(E(u_n)\) exists, its right endpoint is a leaf: both alternative owners have \(m=-1\). Thus \(L_n=3u_n/2\in W\). At \(L_n\), essentiality forces \(N(u_{n+1})\) uniquely and \(3u_n\notin W\). A forced successor with \(a=0\), or outside the board, would itself be a contradiction; it is not an alternative termination of an existing critical set. Therefore an existing set has a terminal \(u_k\), \(k\ge1\), with

\[
u_0,\ldots,u_k\in U,\qquad 2t/3<u_k\le t,
\qquad A-k\ge1.
\]

For \(n<k\), \(u_n\le u_k/q\le2t/9\), so \(R(u_n)\) exists and forces \(A_n=2u_n\in W\). The \(2k\) vertices \(L_n,A_n\), \(0\le n<k\), have possible owner set contained in

\[
\{u_0,\ldots,u_k\}\cup\{v_1,\ldots,v_k\}.
\]

The excluded \(v_0\) has \(b=-1\). The potential set has \(2k+1\) members. Inequality (A1) forces every member to occur as an owner, yielding

\[
v_1,\ldots,v_k\in U,\qquad
2t/3<u_k\le3t/4,\qquad8t/9<v_k\le t.\tag{A3}
\]

This deduction is valid even if a potential edge would otherwise be unavailable: that would shrink the owner set and contradict (A1) earlier.

**Second column and backward cap.** For \(1\le n\le k\), the \(N(v_n)\) edge joins \(A_{n-1}\in W\) to \(\beta_n=2v_n/3\). If \(\beta_n\in W\), this edge is doubly covered. Its two remaining possible owners, \(v_{n-1}\) and \(w_n\), must both supply uniquely covered edges, forcing \(2v_n\notin W\). At the top, \(w_k=g^2u_k>32t/27>t\), so \(\beta_k\notin W\). For \(n<k\), \(v_n\le2t/9\), and \(R(v_n)\) would propagate \(\beta_n\in W\) to \(3v_n=\beta_{n+1}\in W\). Backward induction excludes all \(\beta_n\).

Consequently \(B_n=2v_n\in W\) for \(1\le n<k\). Adjoining these vertices gives \(3k-1\) selected vertices. Their owner set is contained in the preceding \(u,v\) columns together with \(w_1,\ldots,w_{k-1}\), exactly \(3k\) potential owners. Again (A1) forces all of them into \(U\).

**Third column, including \(k=2\).** Suppose \(k\ge2\). Equation (A3) gives

\[
w_{k-1}=(32/81)u_k\le8t/27<t/3,
\]

so every \(R(w_n)\), \(1\le n<k\), is available. For \(2\le n<k\), \(N(w_n)\) joins \(B_{n-1}\in W\) to \(\gamma_n=2w_n/3\). The vertex \(\gamma_k=3w_{k-1}\) is on the board, although the formal owner \(w_k\) is not. Its only other possible owners are \(w_k,z_k\), both outside the board; hence it is a leaf and lies outside \(W\).

If \(\gamma_n\in W\) at an intermediate index, its N edge is doubly covered. Essentiality forces the other two owners uniquely, in particular \(E(z_n)\) with opposite endpoint \(2w_n\notin W\). The available \(R(w_n)\) then propagates membership to \(\gamma_{n+1}\). Backward induction therefore excludes \(\gamma_2,\ldots,\gamma_k\). It follows that \(C_n=2w_n\in W\) for every \(1\le n<k\), including \(n=1\) by the R edge alone. No nonexistent \(N(w_1)\) is used.

The final selected set has size \(4k-2\). Its owner set is contained in

\[
\{u_0,\ldots,u_k\}\cup\{v_1,\ldots,v_k\}
\cup\{w_1,\ldots,w_{k-1}\}\cup\{z_2,\ldots,z_{k-1}\},
\]

also of size \(4k-2\). Here \(z_1\) has \(b=-1\), while \(z_k>t\). This contradicts (A1). When \(k=2\), the final z-range is empty, and the count is \(3+2+1+0=6\) versus the required seven. The induction at intermediate \(\gamma_n\) is empty in this case; the cap \(\gamma_2\notin W\) directly forces \(C_1\in W\).

There are no hidden coincidences in these counts. After removing the common factor \(2x\), the four selected-vertex types are \(g^s q^n\) with \(s=-1,0,1,2\); independence of \(g,q\) makes all pairs distinct. The four owner columns have distinct first exponents \(m=0,1,2,3\) in (A2).

**Classification and boundary cases.** Only \(k=1\) remains, forcing \(\{x,9x/2,6x\}\subseteq U\) and \(6x\le t<27x/4\). Its only edges are

\[
E(x),\ R(x),\ N(9x/2),\ N(6x).
\]

They are covered by the two left vertices \(3x/2,2x\), and \(E(x),N(6x)\) are disjoint, so its matching number is exactly two. Every proper owner subset has a saturating matching. Criticality therefore makes this the whole set. Axis avoidance requires \(A\ge2\), since \(9x/2\) has first exponent \(A-1\). At \(t=27x/4\), its E edge becomes available, so the upper endpoint really is excluded. At \(x=2t/3\), an E edge exists, so the isolate interval is also correctly open at its lower endpoint.

Thus every critical axis-avoiding set is precisely the claimed isolate or patch. This is an unconditional finite combinatorial result.

**Deficiency and prescribed vertical phase.** At most one pure power lies in either exceptional interval, and the two types cannot coexist: a patch root \(x\) gives \(6x\le t<27x/4<8x\), making \(4x\) the largest power of two at most \(t\), with \(4x\le2t/3\). If \(I_j+P_j=0\), any positive set would contain a forbidden critical subset. If \(I_j+P_j=1\), deleting the unique exceptional root destroys every possible critical subset, so \(\nu(B(U))\ge|U|-1\). Hence \(d(U)\le I_j+P_j\) for all axis-avoiding \(U\).

For a corner cover containing the entire vertical phase of color \(j\), its omitted color-j set is axis-avoiding. Its other-color vertices cover the corresponding bipartite graph, proving the lower bound \(K_j-I_j-P_j\). The \(x=2\) patch touches the vertical axis at nine and is explicitly excluded from a claimed constrained-optimum equality; the lower bound remains valid. The corrected \(t=18\) example also checks: both printed three-point sets hit the five corners, while conditioning on the selected point of \(\{1,2,3\}\) rules out two-point covers.

### Gaps

This audit establishes no normalization of arbitrary minimum covers to a complete vertical phase. It does not extend the predecessor proof to \(a=0\), combine criticality with maximal-cardinality hole filling, or prove the global formula (C). Those are different assertions from the verified axis-avoiding theorem.

## Are the double-return algebra, low-column rules, and rational model valid?

### Takeaway

The double identity, both infinite side sums, the mixed bound, and the low-column corrections check. The rational model and its integer denominator work with the corrected slope range \(3/5<p/q<2/3\). A specific input \(p/q=4/7\) disproves the checker's broader implicit no-overlap claim.

### Cited Findings

* The audited equations (1)–(11), model, and claimed finite checks are in [returns.md](<../../early-attacks/augmentation-and-return-attacks/returns.md>), [returns_check.py](<../../early-attacks/augmentation-and-return-attacks/returns_check.py>), and [returns_check.json](<../../early-attacks/augmentation-and-return-attacks/returns_check.json>).
* The state separation and original correction vector are in [arithmetic.md](<../boundary-and-arithmetic/arithmetic.md>). The unconditional normalization \(Z=9c-6\) and coefficient range are in [weighted.md](<../../early-attacks/open-proof-gap-attacks/weighted.md>).

### Inferences

**Unconditional double identity.** Let \(c_{a,b}=1-3\eta_{a,b}\in\{1,-2\}\), \(Z=\sum c_{a,b}2^{-a}3^{-b}\), \(u=2^P\), and \(v=3^Q\). Absolute convergence follows from the coefficient bound. Let \(R\) be the corner sum \(a<P,b<Q\), and \(H,V\) the full strips \(a<P\) and \(b<Q\). Direct reindexing gives

\[
\begin{aligned}
\sum\delta_H\delta_V c\,2^{-a}3^{-b}
 &=(u-1)(v-1)Z-u(v-1)H-v(u-1)V+uvR,\\
\sum_{a<P,b\ge0}\delta_Vc\,2^{-a}3^{-b}&=(v-1)H-vR,\\
\sum_{a\ge0,b<Q}\delta_Hc\,2^{-a}3^{-b}&=(u-1)V-uR.
\end{aligned}
\]

Multiplying the last two lines by \(u,v\) and adding yields exactly the printed identity with integer head \(N_{P,Q}=uvR\). Each corner summand clears to \(c_{a,b}2^{P-a}3^{Q-b}\). No infinite side series disappears.

**Mixed-state support and constants.** Conditional on (C), subtracting the correction vector from \(B_b\) makes the cone rule \(F(A_a+T_b-1+C)\), with \(F(x+y\omega)=1_{x\le0,\,x-y\le0}\). When \(P,Q\) are multiples of three, the residue table C is unchanged. The four-term mixed difference in the note follows by substitution. It vanishes if either state increment is zero, including correction changes inside \(T_b\).

For \(R\ge0\), \(S\ge4\), good ranges \(a<R\) and \(4\le b<S\) leave mixed support only at \(a\ge R,b\ge S\). Since \(|\delta_H\delta_Vc|\le6\), its geometric weight is at most

\[
6\,(2\,2^{-R})\,((3/2)3^{-S})=18\,2^{-R}3^{-S}.
\]

The side coefficients have absolute value at most three. Their remaining tails are at most \(9u3^{-S}\) and \(9v2^{-R}\), respectively, besides the explicitly retained \(b=0,1,2,3\) terms. The low-column exception prevents silently claiming all horizontal differences vanish merely because A returns.

**Corrected model definition.** Use coprime \(p,q>0\) satisfying

\[
\boxed{3/5<p/q<2/3,\qquad p+q\not\equiv0\pmod3.}\tag{A4}
\]

Let \(\alpha=\log_3 2\), \(\sigma=\operatorname{sign}(\alpha-p/q)\), and use the usual floor except that a positive-index exact tie is lowered by one on the negative side. Set \(\widetilde A_0=\widetilde B_0=1\), with increments

\[
\begin{aligned}
\widetilde A_a-\widetilde A_{a-1}
 &=\omega^{-a}S(\lfloor ap/q\rfloor_\sigma),\\
\widetilde B_b-\widetilde B_{b-1}
 &=\omega^{-2b}P_0(\lfloor bq/p\rfloor_{-\sigma}),
\end{aligned}
\]

where \(S(m)=\sum_{j=0}^m\omega^{2j}\) and \(P_0(m)=\sum_{i=0}^m\omega^i\), extended three-periodically. The subscript distinguishes the latter function from the period \(P=3q\); let \(Q=3p\).

For \(b\ge4\), put \(\widetilde m_b=\lfloor bq/p\rfloor_{-\sigma}\). Set the correction at color \(\widetilde m_b-2b\) to one when \(\widetilde m_b-\widetilde m_{b-1}=2\), and at color \(\widetilde m_{b-1}-1-2b\) to one when \(\widetilde m_{b-1}-\widetilde m_{b-3}=4\); all indices are modulo three. Under (A4), \(3/2<q/p<5/3\), so these tests cannot both hold: together they would give a three-step floor increase of six, whereas three times the slope is below five.

Use the cone rule with the state

\[
\widetilde Z_{a,b}=\widetilde A_a+\widetilde B_b-1+C_{a\bmod3,b\bmod3},\qquad
C=\begin{pmatrix}0&0&0\\0&1&-\omega^2\\0&-\omega&1\end{pmatrix}.
\]

Subtract the correction vector in Eisenstein coordinates before applying F. For \(b<4\), if \(\widetilde Z_{a,b}=x+y\omega\), use the four tests from the note:

\[
\begin{array}{c|l}
b&\widetilde\eta_{a,b}\\\hline
0&0\\
1&1_{x\ge1,\,y\ge0},\text{ except }\widetilde\eta_{0,1}=1\\
2&1_{x\le-1,\,x-y\le0}\\
3&1_{\min(x,0)\le y}.
\end{array}\tag{A5}
\]

This defines an artificial rational model independently of (C). Identifying it with true birth digits in a matching window uses (C).

**The broader-range regression witness.** The earlier checker initially permits \(1/2<p/q<2/3\) and then asserts the two correction tests never overlap. Take \(p/q=4/7\). It is coprime and nonresonant. Since \(2^7>3^4\), \(\sigma=+1\), so the reciprocal floor lowers exact integer ties. At \(b=7\),

\[
\widetilde m_4=6,\qquad \widetilde m_6=10,\qquad
\widetilde m_7=12.
\]

Thus \(\widetilde m_7-\widetilde m_6=2\) and \(\widetilde m_6-\widetilde m_4=4\), violating that assertion. Both proposed colors are the same modulo three, but this does not repair the checker's assertion or specify whether simultaneous model corrections should be merged or added. Restriction (A4) removes the ambiguity and is sufficient for every use in the return theorem. This exact calculation is a regression witness, not a numerical sweep.

**State periodicity.** The one-sided convention respects \(\lfloor (a+q)p/q\rfloor_\sigma=\lfloor ap/q\rfloor_\sigma+p\) for positive indices. Therefore A increments have period \(3q\). Their sum over one period is zero: the constant geometric term sums to zero, and grouping \(a=r+jq\), \(1\le r\le q\), \(0\le j<3\), gives common ratio \(\omega^{2p-q}\ne1\) in the other term. The B calculation has common ratio \(\omega^{q-2p}\ne1\). Hence the states themselves, not only their increments, have periods \(P,Q\), including at their index-zero states.

**True correction tests and the low columns.** For the true \(m_b=\lfloor b\log_2 3\rfloor\), the isolate inequality is equivalent to \(m_b\ge m_{b-1}+2\); its increment is one or two. The largest possible patch root exponent is \(m_{b-1}-1\). Its strict upper cutoff is equivalent to \(m_{b-1}-m_{b-3}\ge4\); the difference is three or four. These reproduce the tests and colors exactly for \(b\ge4\).

At \(b=0\), the new vertex participates in no newly completed corner, so its birth digit is zero. At \(b=1,a\ge2\), the inserted color-zero count and newly created patch cancel in the adjusted count, while disappearance of the isolate raises only adjusted color two. Its being a minimum after insertion gives \(x\ge1,y\ge0\). At \(a=1\) that test gives the true digit zero directly; at \(a=0\) the digit is one. At \(b=2\), the indicator is always the isolated color two and is unchanged at the birth, giving \(x\le-1,x-y\le0\). At \(b=3\), adjusted colors zero and two both rise; the minimum rises exactly when \(\min(K_0,K_2)\le K_1\), equivalent to the final test in (A5). Thus no low-column endpoint is being inferred from the unchanged-indicator cone rule.

**Integer denominator.** The corrections have period Q because \(\widetilde m_{b+Q}=\widetilde m_b+3q\). Before the unique exception in (A5), the digit array is P-periodic in a and Q-periodic in b for \(b\ge4\). The exception changes the coefficient from one to minus two at weight \(1/3\), subtracting exactly one from the sum. Writing \(\widetilde c=1-3\widetilde\eta\) and \(\widetilde Z=\sum\widetilde c_{a,b}2^{-a}3^{-b}\), the low part has denominator dividing \(27(u-1)\). The tail tile has denominator dividing \(27(u-1)(v-1)\): its initial factor \(3^{-4}\) combines with the finite tile denominators and the factor \(v/(v-1)\) to leave at most \(3^3\). Therefore

\[
D=27(u-1)(v-1),\qquad N=D\widetilde Z\in\mathbb Z.\tag{A6}
\]

All coefficients still lie in \(\{1,-2\}\), giving \(|\widetilde Z|\le6\). Thus \(H(N:uv:u:v:1)\le162uv\); the coordinates are integers and the final coordinate one makes their common gcd one.

### Gaps

The supplied Python source and saved results were read, but the checker was not rerun in this audit. Its three finite exact comparisons are evidence about those inputs, not proofs of (C), a general skew identity, or infinitely many successful returns. The broader-range assertion should not be reused without (A4) or a separately specified overlapping-correction convention. No old file was modified.

## Do the Farey window and corrected return theorem justify the claimed arithmetic implication?

### Takeaway

Yes, with the two scope corrections above. Consecutive convergents give the stated exact floor window, and \(q'/q>5+\delta\) is a sufficient asymptotic threshold for this model. The conclusion is eventual equality of the rational model values under rationality, not irrationality without an additional nonstabilization argument.

### Cited Findings

* The precise fixed-dimensional lower bound and its required nonzero hypothesis are Proposition 7.4 of the [primary KK manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf). I read Proposition 7.4, Corollary 6.5, and §7.3 in the [saved primary text](<../../../../meta/theorem-transfer-survey/erdos1062-fork-free-density.pdf.txt>). The source supplies nonvanishing separately in its own application.
* The audited matching-window, four-unit form, resonance qualifications, and finite skew observation are in [returns.md](<../../early-attacks/augmentation-and-return-attacks/returns.md>). This audit does not review its author's separate coefficient extension.

### Inferences

**Farey matching, including ties.** Let \(p'/q'\) immediately follow \(p/q\) among the convergents of \(\alpha\). Their determinant is \(\pm1\). Writing the remaining tail as \(t>1\) gives

\[
\alpha=\frac{p't+p}{q't+q},
\]

so the mediant lies strictly between \(p/q\) and \(\alpha\). Any reduced rational strictly between the two convergents has numerator and denominator \(kp+lp'\), \(kq+lq'\), with positive integers \(k,l\), by the unimodular basis change. Its denominator is at least \(q+q'\). A floor disagreement at index \(n\) would cross such a threshold with reduced denominator at most n, unless it is the tie at \(p/q\) itself. The one-sided convention treats that tie in the direction of \(\alpha\), so it does not cause an earlier disagreement. At \(n=q+q'\), the mediant threshold has been crossed. Thus the first disagreement is exactly that index.

Inversion gives the same argument for \(\beta=1/\alpha\), with the opposite side convention and threshold \(p+p'\). Consequently the A and B states agree through the strict index ranges \(a<q+q'\), \(b<p+p'\). Corrections use only b and smaller positive indices in the high range. The low rules (A5) were checked separately. Conditional on (C), digit agreement therefore holds on the whole rectangle of those index ranges, in particular whenever

\[
2^a3^b<X:=\min(2^{q+q'},3^{p+p'}).\tag{A7}
\]

The first disagreement of a floor word need not change a cone digit. No inference of a nonzero weighted error follows from it.

**Tail estimate with its corrected quantifier.** For

\[
\boxed{1\le Y<X,}\tag{A8}
\]

let \(n=\lfloor\log_2Y\rfloor\ge0\). Each row \(0\le a\le n\) of the inclusive tail \(2^a3^b\ge Y\) has reciprocal weight at most \(3/(2Y)\). The remaining dyadic rows have total weight \((3/2)2^{-n}<3/Y\). Therefore

\[
\begin{aligned}
|Z-\widetilde Z|
 &\le\frac{3((3/2)\lfloor\log_2Y\rfloor+9/2)}Y,\\
|DZ-N|
 &\le\frac{81(u-1)(v-1)((3/2)\lfloor\log_2Y\rfloor+9/2)}Y.
\end{aligned}\tag{A9}
\]

The earlier wording “any \(Y<X\)” is false without a lower restriction. For example \(Y=1/16\) gives \(\lfloor\log_2Y\rfloor=-4\), making the first displayed bound's right side \(-72\), which cannot bound an absolute value. This is a literal quantifier error, not an asymptotic failure. Every Y used in the subsequent exponential argument is greater than one.

**Corrected conditional return theorem.** Suppose (C) holds for the true finite optima. Let an unbounded sequence of convergents \(p/q\), with successors \(p'/q'\), satisfy

\[
p+q\not\equiv0\pmod3,\qquad q'/q>5+\delta
\]

for a fixed \(\delta>0\). For sufficiently late members define the model by (A4)–(A6). If \(Z\) is rational, then

\[
\boxed{\widetilde Z=Z\quad\text{for every sufficiently late member of this sequence}.}\tag{A10}
\]

Proof: rationality makes

\[
E=DZ-N=27Zuv-27Zu-27Zv+27Z-N
\]

a four-unit form with fixed rational coefficients and positive \(\{2,3\}\)-units \(uv,u,v,1\), all at least one. Its height is at most \(162uv\). For convergents,

\[
\log(uv)=6q\log2+o(1),\qquad
\log X=(q+q')\log2+o(1).
\]

The second estimate follows because both \((p-q\alpha)\log3\) and \((p'-q'\alpha)\log3\) tend to zero. The ratio hypothesis leaves a fixed positive gap between \(\log X\) and \(6q\log2\). Choose Y whose logarithm lies between \((6+\delta/3)q\log2\) and \((6+2\delta/3)q\log2\); for all sufficiently large q, (A8) holds. Equation (A9) gives \(|E|\le e^{-\kappa q}\) for some fixed \(\kappa>0\).

KK Proposition 7.4 with smallest-unit parameter one gives, whenever \(E\ne0\),

\[
|E|\ge C H(N:uv:u:v:1)^{-\epsilon}
\ge C(162uv)^{-\epsilon}.
\]

Choose fixed \(\epsilon>0\) with \(6\epsilon\log2<\kappa\). This contradicts the upper bound for every sufficiently late nonzero E. Hence E is eventually zero, proving (A10). The proof does not assume its needed nonvanishing; it identifies precisely what rationality would force.

**Why the errata preserve the application.** The exact integer inequalities \(2^5=32>27=3^3\) and \(2^3=8<9=3^2\) imply \(3/5<\alpha<2/3\). Convergents approach \(\alpha\), so all sufficiently late ones satisfy (A4)'s slope range. The three printed models \(5/8,12/19,53/84\) also lie in this narrower interval. The exponential choices of Y above satisfy \(Y\ge1\) automatically. Thus neither correction loses any eventual member needed by the conditional theorem.

**Resonance and skew scope.** If \(p+q\equiv0\pmod3\), the increment periods still hold, but their sums need not vanish. The printed affine recurrences with drifts \(d_A,d_B\) are exact. On tail residue classes, chosen with b-representatives at least four, the cone inequalities become integer linear inequalities in the block indices. That establishes neither the nonresonant denominator formula nor a new threshold for the resonant case.

The claimed rotations of the nonperiodic parts are also consistent: their q- and p-shift multipliers are \(\omega^{2p-q}\) and \(\omega^{q-2p}\), which are inverse nontrivial cube roots in the nonresonant case. Combining shifts can align those parts after recentering. It does not automatically align all residue and correction terms. The displayed skew sums for three finite models remain finite exact observations; no general denominator reduction is proved. Likewise, a state agreement up to index N only gives a period return through indices less than \(N-P\), not N. The note correctly accounts for that loss.

### Gaps

The corrected result is (A10), not an unconditional irrationality theorem. No proof is provided of (C), infinitely many convergents simultaneously satisfying nonresonance and \(q'/q>5+\delta\), or failure of eventual stabilization of their model values. Nonstabilization along such a sequence would combine with (A10) to give irrationality, but remains unproved. No new global-boundary exploration, broad computation, decimal expansion, Lean work, or external submission was performed in this audit.
