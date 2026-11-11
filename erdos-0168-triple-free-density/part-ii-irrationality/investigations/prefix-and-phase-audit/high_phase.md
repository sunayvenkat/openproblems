# High-branch phase comparison and a further prefix exchange

Research derivation, 7 November 2026. The large-window raw-count shortcut is false. A new explicit prefix exchange excludes \(r=1,s\ge4\) for a restricted maximum-deficiency set. It has now received an independent derivation and a separate adversarial audit with no gap reported. The finite intervals and base boards have exact certificates. Together with the common-optimum reduction this gives a complete candidate proof of the finite formula, pending the coordinator's final fresh-context audit of the assembled argument. It does not establish the separate irrationality assertion in Erdős #168.

## Can the top vertical color minimize its count inside the high window?

### Takeaway

Yes. At the lower endpoint with \(s=17\), all three raw color counts tie. Numerical window membership alone therefore cannot prove dominance. This supplies neither a critical owner set nor a counterexample to the candidate finite formula. [Arithmetic row-count source](<../boundary-and-arithmetic/arithmetic.md>).

### Cited Findings

- The remaining high window is \(r=1,s\ge2\), \(x=2^{s+2}\), \(y=3^{2s+1}\), \(z=4\cdot9^s\), and
  \[
  64\cdot9^{s-1}\le t<8\cdot9^s.
  \]
  Its top color is \(j=s+2\pmod3\). [Two-cone and high-window derivation](<../global-boundary-proof/vertical_critical.md>).
- Color counts admit exact integer row summation, independently of the finite-optimum candidate. [Arithmetic separation source](<../boundary-and-arithmetic/arithmetic.md>).
- The exact finite checks, their independent row-count consistency checks, four specified prefix-incidence examples, and the large raw tie are reproducible in [high_phase_check.py](<high_phase_check.py>), with saved [certificate data](<high_phase_check.json>). The script ran successfully; it performs no broad owner-subset enumeration.

### Inferences

If row \(b\) has maximum \(2\)-exponent \(m_b=\lfloor\log_2(t/3^b)\rfloor\), its number of color-\(j\) points is
\[
R_j(m_b,b)=
\begin{cases}
0,&r_j>m_b,\\
1+\lfloor(m_b-r_j)/3\rfloor,&r_j\le m_b,
\end{cases}
\qquad r_j\equiv j+b\pmod3,\quad0\le r_j<3.
\]
For integer \(t\), \(m_b\) is the bit length of \(\lfloor t/3^b\rfloor\), minus one. Separating the two new bottom rows gives
\[
K_j(9t)=K_{j-1}(t)+R_j(\lfloor\log_2(9t)\rfloor,0)
+R_j(\lfloor\log_2(3t)\rfloor,1).
\]
Starting at \(t=64\), \(K=(7,5,5)\), the first lower endpoint among \(s=1,\ldots,17\) where the top raw count attains the minimum is
\[
s=17,\quad t=64\cdot9^{16}=118593292086517824,\quad
j_{\rm top}=1,\quad (K_0,K_1,K_2)=(354,354,354).
\]
An independent direct sum over every row confirms this one-board recurrence result. The earlier 16 endpoints are a bounded diagnostic, not an irrational-rotation distribution theorem.

At this particular raw tie, however, the patch root
\[
e=2^{54}=18014398509481984
\]
has color zero and satisfies
\[
6e=108086391056891904
\le t
<121597189939003392=27e/4.
\]
There is no isolated point, so \(I=(0,0,0)\), \(P=(1,0,0)\), and the adjusted counts are \((353,354,354)\). The top color is not an adjusted minimizer at this board. This exact correction was checked independently before declining an unnecessary MILP calculation.

### Gaps

The raw-tie example is only a falsification of the raw-count window shortcut. It supplies no counterexample to the adjusted formula and no critical family. Neither a MILP optimum nor a rotation-distribution assumption is used in the proof below.

## Does a controlled prefix rule out the remaining unbounded parameter?

### Takeaway

A restricted maximum-deficiency set in the high \(r=1\) case must have \(s\le3\). The repair is a triangular prefix with one already present owner omitted; its exact deficiency gain is \(\lfloor(s+2)/3\rfloor-1\). The new exchange passed a separate adversarial audit. [Source of the prefix method and canonical hypotheses](<../boundary-dominance/canonical_audit_and_collision.md>); [independent current audit](<patch_global.md>).

### Cited Findings

- In an inclusion-minimal positive restricted maximizer, the predecessor cones and forced horizontal chain follow from essentiality and strict owner expansion. The allowed pool excludes the unique exceptional horizontal root \(e\), if present. [Restricted canonical reduction](<../boundary-dominance/canonical_audit_and_collision.md>).
- In the high \(r=1\) case, with \(g=4/3,q=9/2\), the chain \(u_n=xq^n\), \(0\le n\le s\), is forced, all \(3u_n/2\), \(0\le n<s\), lie in a minimum cover \(W\), and \(y>t/3\). [Chain proof](<../global-boundary-proof/vertical_critical.md>).
- Owned edges are \(N(u)=(u/3,2u/3)\), \(E(u)=(3u/2,u/2)\), \(R(u)=(2u,3u)\), with the usual smoothness/cutoff conditions. The first endpoint displayed has left color \(j+1\). [Owner-list audit](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>).

### Inferences

#### Hypotheses and cone geometry

Let \(U\) maximize deficiency in color \(j\) with \(e\) excluded, and suppose its least roots have \(r=1,s\ge2\). Set
\[
A=s+2,\quad x=2^A,\quad y=3^{2s+1},\quad
k(a,b)=2a+b,\quad k_0=2A=2s+4.
\]
For a minimum cover \(W\), write \(|U|-|W|=D_j^*\).

The horizontal nonnegative \((g,q)\)-cone based at \(x\) is exactly the color-\(j\) part of \(k\ge k_0\). Its coordinates are
\[
m=(2a+b-2A)/3,\qquad n=(a+2b-A)/3.
\]
The second is nonnegative whenever the first is nonnegative in the nonnegative quadrant.

In coordinates based at \(x\), the vertical root is \((-1,s)\). An owner in its cone outside the horizontal cone must have coordinates \((-1,s+n)\), \(n\ge0\). Its \(2\)-exponent is \(-n\), so smoothness forces \(n=0\). Consequently
\[
U\subseteq\{(a,b)\in C_j:2a+b\ge k_0\}\cup\{y\}. \tag{H1}
\]
The root \(y\) lies on diagonal \(k_0-3\).

#### The added prefix and cover

Let \(P\) contain all preferred-color points on diagonals
\[
k=k_0-3,k_0-6,\ldots\ge0.
\]
Let \(R\) contain all left-color points on diagonals
\[
k=k_0-4,k_0-7,\ldots\ge0.
\]
By (H1), \(U\cap P=\{y\}\). Add exactly \(P\setminus\{y\}\).

All these points are in \(D_t\): on \(2a+b=k\), the largest value is \(3^k\). The top owner diagonal has maximum \(3^{k_0-3}=y\le t\), and the top cover diagonal has maximum \(y/3\).

For an owner on diagonal \(k\), its left endpoint has diagonal \(k-1\) for \(N,E\), and \(k+2\) for \(R\). Hence every newly owned edge has its left endpoint in \(R\), except possibly a rooted edge from the top prefix diagonal, whose left endpoint lies on \(k_0-1\).

The frontier consists of
\[
(a,b)=(a,2s+3-2a),\qquad0\le a\le s+1.
\]
The \(a=0\) label is \(9y>t\). The \(a=1\) label is \(2y\), whose unique possible lower-prefix rooted owner is \(y\); that owner was not added, and \(R(y)\) is unavailable because \(3y>t\). Every point with \(2\le a\le s+1\) equals
\[
3u_n/2,\qquad n=s+1-a,\qquad0\le n<s,
\]
and already belongs to \(W\). Thus
\[
W\cup R\text{ covers }B(U\cup P). \tag{H2}
\]
Every old edge, including those of \(y\), remains covered by \(W\).

The excluded exceptional root is not introduced. Every horizontal point in \(P\) has preferred exponent at most \(A-3=s-1\), hence value at most \(x/8=2^{s-1}\). (The weaker bound \(2^s\) would also suffice.) Every exceptional isolate or patch root obeys \(e>4t/27\), and
\[
4t/27\ge(256/243)\,9^s>2^s
\]
throughout the high window. The enlarged set stays in the allowed pool.

#### Exact count

The full diagonal \(k\ge0\) has \(\lfloor k/2\rfloor+1\) points; assign count zero to \(k=-1\). Pair each owner diagonal \(k_0-3n\) with the cover diagonal one below it. The count difference is one exactly when \(n\) is even. Therefore
\[
|P|-|R|=\lfloor A/3\rfloor=\lfloor(s+2)/3\rfloor.
\]
Only the already present owner \(y\) is subtracted. Any overlap of \(R\) with \(W\) makes the repair cheaper. Hence
\[
\begin{aligned}
d(U\cup P)&\ge |U|+|P|-1-|W|-|R|\\
&=D_j^*+\lfloor(s+2)/3\rfloor-1. \tag{H3}
\end{aligned}
\]
For \(s\ge4\), this contradicts maximality. Thus a restricted canonical high obstruction has \(s\in\{2,3\}\).

### Gaps

The proof requires canonical maximality, not only criticality. It does not say that an arbitrary critical set with \(s\ge4\) is impossible: adding the prefix may produce a different set of larger deficiency. It makes no unrestricted full-class-filling assertion. No local proof gap was identified in the independent review; the final assembled global proof still receives its separate review.

## What finite phase comparisons would complete the aggregate argument?

### Takeaway

Each surviving high case has an adjusted phase strictly smaller than its top vertical phase. The common-optimum compatibility and collision arguments pass the independent audit below, and the base boards are exact. Thus these lemmas give a complete candidate finite-formula proof, subject to the final assembled-proof review. [Aggregate source](<../boundary-dominance/canonical_audit_and_collision.md>).

### Cited Findings

- The \(r=2,s\le1\) and \(r=1,s\le1\) cases have finite forced sets and parameter intervals. [Earlier high-case proof](<../global-boundary-proof/vertical_critical.md>).
- The same-optimum collision at \(\{6,12,18\}\) forces a counterexample into the top-color incomparable-root case. The old saved version assumed no active patch; the current one-owner compatibility proof extends that step. [Original reduction](<../boundary-dominance/canonical_audit_and_collision.md>); [current patch analysis](<patch_global.md>).

### Inferences

The required finite comparisons are as follows; endpoints shown on the right are excluded.

| Case | Cutoff interval | Top color | \(K\) | \(I\) | \(P\) | Adjusted \(K-I-P\) |
|---|---|---:|---|---|---|---|
| \(r=1,s=0\) | \([6,8)\) | 2 | \((2,1,2)\) | \((0,0,0)\) | \((0,0,0)\) | \((2,1,2)\) |
| \(r=1,s=0\) | \([8,9)\) | 2 | \((3,1,2)\) | \((1,0,0)\) | \((0,0,0)\) | \((2,1,2)\) |
| \(r=2,s=0\) | \([24,27)\) | 1 | \((3,4,4)\) | \((0,0,0)\) | \((0,0,1)\) | \((3,4,3)\) |
| \(r=1,s=1\) | \([54,64)\) | 0 | \((6,5,5)\) | \((0,0,0)\) | \((0,0,0)\) | \((6,5,5)\) |
| \(r=1,s=1\) | \([64,72)\) | 0 | \((7,5,5)\) | \((1,0,0)\) | \((0,0,0)\) | \((6,5,5)\) |
| \(r=2,s=1\) | \([216,243)\) | 2 | \((9,8,9)\) | \((0,0,0)\) | \((0,0,0)\) | \((9,8,9)\) |
| \(r=1,s=2\) | \([576,648)\) | 1 | \((12,12,11)\) | \((1,0,0)\) | \((0,0,0)\) | \((11,12,11)\) |
| \(r=1,s=3\) | \([5184,5832)\) | 2 | \((20,19,20)\) | \((1,0,0)\) | \((0,0,0)\) | \((19,19,20)\) |

All eight rows were checked exactly, including every smooth-label and correction transition. Each displayed interval has no interior event. The optional \(s=0\) rows are included for completeness; the \(t\ge18\) incomparable-root contradiction only requires \(s\ge1\). In particular, root \(1\) is not a permitted patch root, and the \(t=24\) board has eleven vertices, with \(K=(3,4,4)\).

For \(s=2,3\), the isolated roots are respectively \(512=2^9\) and \(4096=2^{12}\); their condition \(e>2t/3\) holds throughout the interval. There is no power of two in the patch-root interval \((4t/27,t/6]\). The eight exact comparison records are saved in the certificate JSON.

#### Independent audit of one-owner compatibility

Let \(D=\max_{U\subset C_p}d(U)\), and let \(D^*\) restrict the pool by excluding the sole exceptional owner \(e\), if one exists. The direct edge-inclusion inequality
\[
d(U)\le d(U\setminus\{e\})+1
\]
gives \(D^*\le D\le D^*+1\), including the empty-set case.

If \(D=D^*+1\), every unrestricted maximizer contains \(e\), and deleting it from any such maximizer leaves deficiency exactly \(D^*\). If \(D=D^*\), select a restricted maximizer \(V\), a minimum graph cover \(W\), and the global optimum \(F=(C_p\setminus V)\cup W\). This \(F\) contains \(e\) and omits precisely \(V\) in color \(p\). In either case one obtains a single optimum whose prescribed restricted omissions maximize in color \(p\). Its omissions in the other colors automatically maximize unrestricted deficiency by the exact cover correspondence. This audit confirms the proof in [patch_global.md](<patch_global.md>); no equality exchange of a chosen canonical cover is needed.

#### Independent audit of the aggregate contradiction

Write \(\delta_j=I_j+P_j\), \(M=\min_j(K_j-\delta_j)\), and let \(q\) be the color of the largest vertical power of three. There is at most one exceptional root across all colors: an active patch with root \(e\) has \(6e\le t<27e/4<8e\), so the largest power of two is \(4e\le2t/3\), excluding an isolate.

Suppose \(\tau<M\). The common optimum just constructed has restricted omitted maximizers in all three colors, each with positive deficiency because \(D_j=K_j-\tau>\delta_j\) and a single exclusion lowers the maximum by at most one. Take inclusion-minimal maximizing subsets within these same omitted sets.

The audited P1/P2 prefix repairs and root-balance/deep-branch lemmas show that in a color other than \(q\), such a subset is origin-containing or degenerate, and it forces respectively owner 6, 12, or 18 in colors 0, 1, or 2. The same holds for a top-color subset if it is origin-containing or degenerate. These owners are not pure powers of two, so none is the excluded \(e\). If the top subset were also degenerate or origin-containing, all three owners of the actual corner \(\{6,12,18\}\) would lie outside the same optimum \(F\), impossible for \(t\ge18\).

Thus the top color has an incomparable-root restricted maximizing subset \(U\). Its least vertical owner \(y>t/3\) is its only vertical owner. Removing \(y\) leaves an allowed axis-avoiding set of nonpositive deficiency, so
\[
0<D_q^*=d(U)\le d(U\setminus\{y\})+1\le1.
\]
Hence \(D_q^*=1\), and the inclusion-minimal maximizer really is a critical set. Since \(D_q>\delta_q\), while \(D_q-D_q^*\le\delta_q\), one obtains \(D_q=\delta_q+1\). Therefore
\[
\tau=K_q-\delta_q-1,\qquad M=K_q-\delta_q.
\]
In particular the adjusted top phase must attain the minimum. This uses aggregate maximizers before reaching deficiency one, not an unsupported decomposition into critical subsets.

The previous high-case analysis allows only \(r=2,s=1\), \(r=1,s=1\), or \(r=1,s\ge2\). The finite table excludes the first two; (H3) excludes \(r=1,s\ge4\); the \(s=2,3\) rows exclude the rest. This is a contradiction. The route uses no discrepancy estimate, equidistribution assertion, first-failure induction, or broad computational extrapolation.

#### Exact small boards

For \(3\le t<9\), the point 2 hits every corner and at least one corner exists, so \(\tau=1\). Exact counts at the breakpoints \(3,4,6,8,9\) give \(M=1\).

For \(9\le t<18\), the points \(\{3,4\}\) hit every corner. Already at \(t=9\), the three corners \(\{1,2,3\}\), \(\{2,4,6\}\), and \(\{3,6,9\}\) have empty common intersection; thus no one-point cover exists. Hence \(\tau=2\). The exact breakpoints \(9,12,27/2,16,18\), including the termination of the small patch at \(27/2\), give \(M=2\) throughout. The script verifies these covers, the empty intersection, and the exact indicator counts on all eight base intervals.

### Gaps

No new mathematical gap was found in the compatibility lemma, the aggregate use of maximizers, the high-prefix exchange, the endpoint comparisons, or the small boards. The final fresh-context audit of the entire dependency chain is still pending; earlier lemmas must be included or precisely cited in the final assembled proof. Even a verified finite formula leaves the irrationality target unresolved.

