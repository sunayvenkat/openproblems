# Erdős 168: classification of critical sets avoiding the vertical axis

This round gives a proposed general proof of the deficiency bound for every set avoiding the vertical axis, with arbitrarily many horizontal roots allowed. The proof below is self-contained and ready for independent review. It does not prove the global patched finite-cover formula or the irrationality assertion in #168(ii). No new numerical search, MILP run, or computer-assisted certificate was used in this argument.

## What does criticality force before any matching paths are chosen?

### Takeaway

Every critical set avoiding the vertical axis lies in a two-generator cone above its smallest horizontal root. A strict owner-neighborhood inequality for its minimum vertex cover will replace the invalid inference that different horizontal rows automatically supply disjoint augmenting paths.

### Cited Findings

- The finite board, coloring, and matching reduction are established in [168_grid.md](<../open-conjecture-transfer-search/168_grid.md>). The previously open fixed-boundary inequality is stated there explicitly.
- Criticality, the essential-cover property, and the single-root argument were proved in [boundary.md](<../../investigations/boundary-and-arithmetic/boundary.md>) and assessed in [boundary_review.md](<../../investigations/boundary-and-arithmetic/boundary_review.md>).
- Maximal-cardinality hole normalization is a different choice of representative from inclusion-minimal criticality; see [hole_filling.md](<../open-proof-gap-attacks/hole_filling.md>). No hole-free assumption is made below.

### Inferences

#### Definitions and the three possible owners

Let

\[
D_t=\{2^a3^b:a,b\in\mathbb Z_{\ge0},\ 2^a3^b\le t\},
\qquad c(2^a3^b)=a-b\pmod3.
\]

Fix a color \(j\) and a set \(U\subset C_j=D_t\cap c^{-1}(j)\). Its bipartite graph \(B(U)\) has left color \(j+1\), right color \(j+2\), and the following edges owned by \(u=2^a3^b\in U\):

\[
\begin{array}{c|c|c|c}
&\text{left endpoint}&\text{right endpoint}&\text{availability}\\\hline
N(u)&u/3&2u/3&b\ge1\\
E(u)&3u/2&u/2&a\ge1,\ 3u\le2t\\
R(u)&2u&3u&3u\le t.
\end{array}
\]

Write \(d(U)=|U|-\nu(B(U))\). A set is **critical** if \(d(U)>0\) and every proper subset has nonpositive deficiency. Throughout the classification proof, \(U\) avoids the vertical axis: every label has \(a\ge1\). A horizontal root is a label with \(b=0\).

For any physical left vertex \(l\), the only possible owners of its incident edges are

\[
R(l/2),\qquad E(2l/3),\qquad N(3l).
\tag{1}
\]

For any physical right vertex \(r\), they are

\[
R(r/3),\qquad N(3r/2),\qquad E(2r).
\tag{2}
\]

These lists name possibilities only: nonsmooth labels, labels outside \(U\), and unavailable edges contribute nothing.

#### Critical covers and a strict deletion inequality

If \(U\) is critical and \(m=|U|\), then deleting any label gives a graph with matching number at least \(m-1\). Hence \(\nu(B(U))=m-1\), so \(d(U)=1\). By the bipartite matching-cover theorem, let \(W\) be a minimum vertex cover of size \(m-1\).

Every \(w\in W\) uniquely covers edges of at least two distinct owners in \(U\); an edge is uniquely covered by \(w\) when its other endpoint is outside \(W\). Otherwise, deleting \(w\) and its sole uniquely supported owner leaves a smaller positive-deficiency set. If no edge is uniquely supported, \(w\) is redundant. In particular, a degree-one vertex cannot be in \(W\).

For any nonempty \(S\subset W\), let \(T\subset U\) be the owners of **all** edges incident to \(S\), including edges whose other endpoints also lie in \(W\). Then

\[
|T|\ge |S|+1.
\tag{3}
\]

Indeed, \(W\setminus S\) covers \(B(U\setminus T)\), and essentiality ensures \(T\ne\varnothing\). If \(T\ne U\) and \(|T|\le |S|\), the nonempty proper subset \(U\setminus T\) has deficiency at least

\[
(|U|-|T|)-(|W|-|S|)=1+|S|-|T|\ge1,
\]

contrary to criticality. If \(T=U\), the same cardinality hypothesis contradicts \(|S|\le |W|=|U|-1\) directly. This handles the empty-remainder case as well.

#### Predecessor lemma

For each nonaxis label \(u\in U\), so **both** \(a,b\ge1\), at least one of

\[
u/6,\qquad 2u/9,\qquad 3u/4
\tag{4}
\]

belongs to \(U\).

Suppose none does. The left endpoint \(u/3\) of \(N(u)\) is a leaf by (1), so it is outside \(W\) and \(2u/3\in W\). At this right endpoint, (2) and essentiality force the edge \(E(4u/3)\), with its opposite endpoint \(2u\notin W\). In particular \(2u\le t\), which ensures that \(E(u)\) is available; here \(a\ge1\) is needed.

The right endpoint \(u/2\) of \(E(u)\) is also a leaf, since its alternative owners are \(u/6\) and \(3u/4\). Thus \(3u/2\in W\). Essentiality at this left vertex forces \(N(9u/2)\), with \(3u\notin W\). Its owner lies in \(U\), so \(u\le2t/9\). Therefore \(R(u)\) is present and both its endpoints \(2u,3u\) are outside \(W\), a contradiction.

#### The two-generator cone

All three predecessors in (4) are numerically smaller. Following predecessors must terminate at a horizontal root. In particular the smallest label of \(U\) is a horizontal root \(x=2^A\), with \(A\ge1\). Since all roots have the same color, every other root is \(x8^\ell\), \(\ell\ge0\).

Put

\[
g=\frac43,\qquad q=\frac92,\qquad gq=6,\qquad g^2q=8.
\]

Reversing a predecessor step multiplies by \(g\), \(q\), or \(gq\). Thus every \(u\in U\) has the unique representation

\[
u=xg^m q^n,\qquad m,n\in\mathbb Z_{\ge0}.
\tag{5}
\]

Its ordinary exponents are

\[
a=A+2m-n,\qquad b=2n-m,
\tag{6}
\]

so additionally \(A+2m-n\ge1\) and \(2n-m\ge0\). In particular, any expression with \(m<0\) is forbidden as a label of \(U\), even when it is smooth and lies on the board. Uniqueness follows from multiplicative independence of \(g\) and \(q\), or the determinant-three exponent transformation (6).

### Gaps

The predecessor argument uses \(a\ge1\) to make \(E(u)\) available. It cannot be extended to vertical-axis labels by dropping that hypothesis. No claim about arbitrary vertical-touching critical sets is established in this section.

## Can a critical set avoiding the vertical axis contain several horizontal roots?

### Takeaway

No. Three successive column counts, with essentiality propagating backward from the upper boundary, force a contradiction for every continuation beyond the known patch. Consequently every critical set avoiding the vertical axis is a singleton isolate or the three-label patch.

### Cited Findings

- The isolate and patch are actual positive-deficiency constructions; their parameter windows and exact small examples are recorded in [168_grid.md](<../open-conjecture-transfer-search/168_grid.md>).
- The earlier proof stopped at one horizontal root because residual paths can share sources and exits. That restriction, including the correction to the disjoint-row inference, is explicit in [boundary.md](<../../investigations/boundary-and-arithmetic/boundary.md>). The present argument uses (3), not any path-disjointness assertion.

### Inferences

#### Boundary ray and the first column count

Let \(x=2^A\) be the smallest label of a critical axis-avoiding \(U\). If \(x>2t/3\), it owns no edge: \(N\) is absent because \(b=0\), and \(E,R\) are beyond the cutoff. Criticality then gives \(U=\{x\}\). Assume henceforth \(x\le2t/3\).

Define four formal columns

\[
u_n=xq^n,\qquad v_n=xgq^n,\qquad
w_n=xg^2q^n,\qquad z_n=xg^3q^n.
\tag{7}
\]

Whenever \(u_n\in U\) and \(E(u_n)\) is available, its right endpoint \(u_n/2\) is a leaf. Its other possible owners \(u_n/6=xg^{-1}q^{n-1}\) and \(3u_n/4=xg^{-1}q^n\) are forbidden by (5). Thus

\[
L_n:=3u_n/2\in W.
\]

At \(L_n\), its other possible owner \(3u_n/4\) is again forbidden, so essentiality forces \(N(u_{n+1})\), with \(3u_n\notin W\). Iterating gives a finite terminal label \(u_k\), where

\[
k\ge1,\qquad u_0,\ldots,u_k\in U,\qquad 2t/3<u_k\le t.
\tag{8}
\]

The iteration cannot stop by hitting \(a=0\): the forced next owner would violate the axis-avoiding hypothesis. Finiteness and multiplication by \(q>1\) ensure a terminal step, and since every existing label has \(a\ge1\), termination means precisely that its \(E\) edge is beyond the cutoff.

For every \(0\le n<k\), \(u_n\le u_k/q\le2t/9\), so \(R(u_n)\) is present. Its right endpoint \(3u_n\) is outside \(W\), forcing

\[
A_n:=2u_n\in W.
\]

Take \(S_0=\{L_n,A_n:0\le n<k\}\), so \(|S_0|=2k\). The possible owners from (1) are

\[
\begin{array}{c|c}
\text{selected vertex}&\text{possible owners in }U\\\hline
L_n&u_n,u_{n+1}\\
A_n&u_n,v_n,v_{n+1}.
\end{array}
\tag{9}
\]

Here \(v_0\) has exponent \(b=-1\), so it is not a board label. The owner neighborhood therefore has at most \(2k+1\) labels: \(u_0,\ldots,u_k\) and \(v_1,\ldots,v_k\). Inequality (3) forces all of them to occur. In particular,

\[
v_1,\ldots,v_k\in U,
\qquad \frac{2t}{3}<u_k\le\frac{3t}{4},
\qquad \frac{8t}{9}<v_k\le t.
\tag{10}
\]

#### Backward propagation in the second column

For \(1\le n\le k\), the left endpoint of \(N(v_n)\) is

\[
v_n/3=A_{n-1}\in W.
\]

Let \(\beta_n=2v_n/3\) be its right endpoint. If \(\beta_n\in W\), the \(N\) edge is doubly covered, so essentiality requires both remaining possibilities at that vertex: \(R(v_{n-1})\) and \(E(w_n)\), uniquely covered there. In particular their latter opposite endpoint satisfies \(2v_n\notin W\).

But

\[
w_k=g^2u_k>\frac{32t}{27}>t,
\tag{11}
\]

so \(E(w_k)\) is absent. Hence \(\beta_k\notin W\). For \(n<k\), the bound \(v_n\le v_k/q\le2t/9\) makes \(R(v_n)\) available. If \(\beta_n\in W\), then \(2v_n\notin W\), so its right endpoint \(3v_n=\beta_{n+1}\) must lie in \(W\). Backward induction from \(\beta_k\notin W\) gives

\[
\beta_1,\ldots,\beta_k\notin W,
\qquad B_n:=2v_n\in W\quad(1\le n<k).
\tag{12}
\]

Now set \(S_1=S_0\cup\{B_n:1\le n<k\}\), of size \(3k-1\). Each new vertex has possible owners

\[
B_n:\quad v_n,w_n,w_{n+1}.
\]

Since \(w_k\) is outside the board, the complete owner neighborhood is contained in

\[
\{u_0,\ldots,u_k\}\cup
\{v_1,\ldots,v_k\}\cup
\{w_1,\ldots,w_{k-1}\},
\]

a set of \(3k\) labels. By (3), all these labels occur in \(U\). In particular \(w_1=8x\) would be a second horizontal root whenever \(k\ge2\).

#### Backward propagation in the third column and the final contradiction

Assume \(k\ge2\). All \(R(w_n)\) for \(1\le n<k\) are available because

\[
w_{k-1}=\frac{g^2}{q}u_k
=\frac{32}{81}u_k\le\frac{8t}{27}<\frac t3.
\tag{13}
\]

For \(2\le n<k\), the left endpoint of \(N(w_n)\) is \(w_n/3=B_{n-1}\in W\). Put \(\gamma_n=2w_n/3\) for \(2\le n\le k\). Even though \(w_k\) is outside the board, \(\gamma_k=3w_{k-1}\) is a board vertex incident to the available edge \(R(w_{k-1})\). Its only other possible owners, \(w_k\) and \(z_k=gw_k\), lie outside the board. Therefore \(\gamma_k\) is a leaf and \(\gamma_k\notin W\).

For \(2\le n<k\), if \(\gamma_n\in W\), its \(N(w_n)\) edge is doubly covered. Essentiality requires both \(R(w_{n-1})\) and \(E(z_n)\) to be uniquely covered there, forcing \(2w_n\notin W\). The available \(R(w_n)\) then forces \(3w_n=\gamma_{n+1}\in W\). Backward induction gives

\[
\gamma_2,\ldots,\gamma_k\notin W,
\qquad C_n:=2w_n\in W\quad(1\le n<k).
\tag{14}
\]

The argument includes \(n=1\) in the second assertion: its right endpoint is \(\gamma_2\), so no \(N(w_1)\) edge is required. This is essential because \(w_1\) is a horizontal root.

Finally let

\[
S_2=S_1\cup\{C_n:1\le n<k\},\qquad |S_2|=4k-2.
\]

Each \(C_n\) has possible owners \(w_n,z_n,z_{n+1}\). The expression \(z_1\) has exponent \(b=-1\), and \(z_k>t\). Hence the complete owner neighborhood is contained in

\[
\{u_0,\ldots,u_k\}\cup
\{v_1,\ldots,v_k\}\cup
\{w_1,\ldots,w_{k-1}\}\cup
\{z_2,\ldots,z_{k-1}\}.
\tag{15}
\]

There are at most

\[
(k+1)+k+(k-1)+(k-2)=4k-2=|S_2|
\]

such owners, contradicting (3). For \(k=2\), the last range is empty and contributes zero, as required.

All selected vertices counted above are distinct. Indeed, after factoring out \(2x\), the four kinds \(L_n,A_n,B_n,C_n\) have the forms \(g^s q^n\) with respectively \(s=-1,0,1,2\). Multiplicative independence of \(g,q\) prevents coincidences. The owner columns in (15) are likewise distinct. Membership of \(u_k\) in the axis-avoiding set also ensures \(A-k\ge1\); no endpoint calculation silently crosses the vertical axis.

#### Classification theorem

The contradiction excludes \(k\ge2\), leaving \(k=1\). The forced labels are

\[
\{x,9x/2,6x\}\subset U,
\qquad 6x\le t<27x/4.
\tag{16}
\]

The lower bound follows from \(v_1=6x\in U\); the strict upper bound follows from \(u_1=9x/2>2t/3\). The set in (16) has deficiency one: its edges are covered by the two left vertices \(3x/2,2x\), and it has a matching of size two. Criticality therefore makes it all of \(U\).

**Theorem.** Every critical \(U\subset C_j(D_t)\) avoiding \(a=0\) is exactly one of:

1. \(U=\{x\}\), where \(x=2^A\), \(A\ge1\), and \(2t/3<x\le t\);
2. \(U=\{x,9x/2,6x\}\), where \(x=2^A\), \(A\ge2\), and \(6x\le t<27x/4\).

The condition \(A\ge2\) in the patch case is forced by the label \(9x/2\) avoiding the vertical axis. In particular there is no critical axis-avoiding set with two or more horizontal roots. The proof applies to arbitrary critical sets, without assuming connectedness, absence of holes, a specified matching, or one matched edge per owner.

### Gaps

This proof has been written for independent review; it is not backed by a new finite sweep. Its delicate points are the complete incidence lists (1)–(2), the all-incident-owner definition in (3), and the boundary starts \(v_0,z_1\) and caps \(w_k,z_k\). Those points are explicitly retained above for audit.

## What finite-cover lower bound follows, and what remains open?

### Takeaway

The critical classification yields \(d(U)\le I_j(t)+P_j(t)\) for every axis-avoiding \(U\), regardless of its number of roots or components. It supplies the lower bound for covers containing a complete vertical color phase, but it does not yet prove that some globally minimum cover can be chosen with such a phase.

### Cited Findings

- For \(t\ge3\), the construction indicators \(I_j,P_j\), their disjoint parameter windows, and the conjectural formula \(\tau(t)=\min_j(K_j-I_j-P_j)\) are defined in [168_grid.md](<../open-conjecture-transfer-search/168_grid.md>).
- The separate arithmetic obstacles after an exact finite-cover formula, including nonlinear color selection and return-compression/nonvanishing obligations, are described in [arithmetic.md](<../../investigations/boundary-and-arithmetic/arithmetic.md>) and [arithmetic_review.md](<../../investigations/boundary-and-arithmetic/arithmetic_review.md>).
- The reviewed status before this round is summarized in [Erdos 168 boundary and arithmetic.md](<../../investigations/boundary-and-arithmetic/REPORT.md>). This note does not change any external problem-status record or make a priority claim.

### Inferences

#### Extension from critical sets to every axis-avoiding set

For a fixed \(t\), there is at most one isolated pure power of two in \((2t/3,t]\), and at most one patch start in \((4t/27,t/6]\). Moreover these alternatives cannot coexist. If a patch starts at \(x\), then \(6x\le t<27x/4<8x\), so the largest pure power of two at most \(t\) is \(4x\le2t/3\), excluding an isolate. Thus, over all colors, there is at most one possible exceptional horizontal root.

For \(t\ge3\), fix a color \(j\), put \(\delta_j=I_j+P_j\), and let \(U\subset C_j\) avoid the vertical axis. If \(\delta_j=0\), any positive-deficiency \(U\) would contain a critical subset, contradicting the classification. Hence \(d(U)\le0\).

If \(\delta_j=1\), let \(x\) be the unique exceptional root. Every critical positive subset of \(U\) must contain \(x\). Consequently \(U\setminus\{x\}\) has nonpositive deficiency: otherwise it contains a critical subset avoiding \(x\). Monotonicity of matching number gives

\[
\nu(B(U))\ge\nu(B(U\setminus\{x\}))\ge |U|-1,
\]

and therefore

\[
\boxed{d(U)\le I_j(t)+P_j(t)\quad
\text{for every }U\subset C_j(D_t)\text{ avoiding }a=0.}
\tag{17}
\]

If the construction's patch starts at \(x=2\), its label \(9\) lies on the vertical axis, so it cannot occur inside such a \(U\). Bound (17) remains valid but is then slack; this distinction should not be suppressed when asserting an exact constrained optimum.

#### Consequence for a prescribed complete vertical phase

Let \(F\subset D_t\) hit every corner \(\{u,2u,3u\}\). Suppose that it contains every vertical-axis vertex of color \(j\). Put \(U=C_j\setminus F\), which avoids the vertical axis, and \(W=F\setminus C_j\). Every edge of \(B(U)\) must meet \(W\), since its omitted third corner is in \(U\). Thus

\[
|F|=K_j-|U|+|W|
\ge K_j-|U|+\nu(B(U))
\ge K_j-I_j-P_j.
\tag{18}
\]

Except for the small \(x=2\) patch issue just noted, the known construction itself respects the prescribed vertical phase, so (18) identifies its constrained optimum. For the global conjecture, the lower bound (18) alone is the relevant established conclusion.

#### The precise remaining combinatorial obligation

To obtain the global patched formula from (18), it would suffice to prove:

> Some minimum corner-hitting set contains every vertical-axis point of at least one color \(j\).

This is an existential normalization statement. It is false with “every minimum” in place of “some”: at \(t=18\), the minimum cover \(\{2,6,12\}\) omits every vertical label \(1,3,9\), whereas the minimum cover \(\{1,4,6\}\) contains the complete vertical phase of color zero. To verify minimality directly, the five corners have roots \(1,2,3,4,6\). Any two-point cover would choose one point of \(\{1,2,3\}\). If it chooses 1, the remaining four corners have empty common intersection; if it chooses 2, the remaining corners rooted at 3 and 4 are disjoint; if it chooses 3, the remaining corners rooted at 2, 4, and 6 have empty common intersection. Thus no two-point cover exists.

An alternative sufficient route is to control every vertical-touching critical component by comparison with a competing adjusted color class. Neither route follows merely from criticality, and no combination of criticality with maximal-cardinality hole normalization has been assumed here.

### Gaps

- The global vertical-phase normalization/comparison remains unproved. Therefore the global finite-cover formula remains a conjectural input.
- Even that finite formula would not finish #168(ii): the return-compression and arithmetic nonvanishing obligations in the linked arithmetic notes remain separate.
- No claim of historical novelty, external peer review, or current external problem-status verification is made. This round's contribution is the explicit combinatorial argument (1)–(18), awaiting independent audit.
