# Prefix audit and a complete finite-cover proof candidate

Research round, 7 November 2026. This note independently audits P1–P3 from the preceding round, removes P3's restriction to an inactive patch, and supplies the missing prefix repair for the high incomparable-root case. The resulting assembly proves the global formula if all the explicitly stated lemmas below survive the requested fresh final audit. **The complete assembly is a proof candidate awaiting that final review; this is not an irrationality proof or a Lean verification.** No historical priority is claimed. The only computation is an exact check of eight small base intervals and five specified high-window subintervals.

## Do the restricted-maximizer arguments and P1–P2 hold as stated?

### Takeaway

Yes. Restricted maximality gives exactly the essentiality and strict expansion needed by the two-cone argument, even at arbitrary deficiency. Both prefix repairs cover every new edge, their frontier lists are complete, and their gains are precisely the stated floors. The root-balance proof can be simplified: when B exceeds 2A, the entire forced horizontal chain is already below the known vertical root, so no numerical-cap alternative is needed.

### Cited Findings

- The statements being audited are P1–P3 and their preparatory claims in [canonical_audit_and_collision.md](<../boundary-dominance/canonical_audit_and_collision.md>).
- The established unconditional input is the general axis-avoiding critical classification and its all-subset consequence. It was proved in [multiroot.md](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>) and independently reconstructed in [combinatorial_and_coefficient_audit.md](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>) and [independent_audit.md](<../global-boundary-proof/independent_audit.md>). It does not assume (C).
- The original two-cone deductions and their complete independent audit, including the deep-branch exclusion, are in [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>) and [vertical_audit_and_transfer.md](<../boundary-dominance/vertical_audit_and_transfer.md>).

### Inferences

#### The board, correction indicators, and the construction upper bound

Let \(D_t=\{2^a3^b\le t:a,b\in\mathbb Z_{\ge0}\}\), color by \(a-b\pmod3\), and put \(C_j=C_j(D_t)\), \(K_j=|C_j|\). A cover meets each corner \(\{u,2u,3u\}\subset D_t\); its minimum size is \(\tau(t)\). Every corner has one vertex of each color, so \(C_j\) is a cover.

For a power \(x=2^A\), \(A\ge1\), the isolate correction applies when \(2t/3<x\le t\). This point belongs to no corner and can be deleted. The patch correction applies when

\[
6x\le t<27x/4.
\]

Its three same-color owners \(x,9x/2,6x\) have exactly the four opposite edges

\[
(3x/2,x/2),\ (2x,3x),\ (3x/2,3x),\ (2x,4x).
\]

They are covered by \(\{3x/2,2x\}\). Thus deleting those three phase vertices and adding these two vertices preserves the corner cover and saves one. For x=2 the east edge of owner 9 is absent by its zero first exponent; the displayed construction window is still valid. Let \(I_j,P_j\) indicate these corrections in the root's color, and put

\[
\delta_j=I_j+P_j,\qquad Q_j=K_j-\delta_j,\qquad Q=\min_jQ_j.
\]

Each root window has multiplicative width less than two. If a patch root x exists, \(6x\le t<27x/4<8x\), and the largest dyadic point is \(4x\le2t/3\); therefore an isolate cannot coexist with a patch. There is at most one exceptional root e across all colors, \(\delta_j\in\{0,1\}\), and every exceptional root exceeds \(4t/27\). The construction proves

\[
\tau(t)\le Q(t). \tag{1}
\]

#### Matching reduction and the allowed pools

For \(U\subset C_j\), let \(B(U)\) consist of the opposite edges of corners whose color-j owner lies in U. Orient its bipartition as colors \(j+1,j+2\). Its owned edges are

\[
N(u)=(u/3,2u/3),\quad E(u)=(3u/2,u/2),\quad R(u)=(2u,3u),
\tag{2}
\]

available respectively for \(b(u)\ge1\), for \(a(u)\ge1\) and \(3u/2\le t\), and for \(3u\le t\). At a physical left vertex l, the possible owners are \(l/2,2l/3,3l\); at a right vertex v they are \(v/3,3v/2,2v\), with availability imposed. These are complete lists.

Write \(d(U)=|U|-\nu(B(U))\). The bipartite matching-cover theorem gives

\[
D_j:=\max_{U\subset C_j}d(U)=K_j-\tau. \tag{3}
\]

Indeed, any vertex cover W of B(U) gives the corner cover \((C_j\setminus U)\cup W\), and every corner cover has this form. For any globally minimum F, its omitted set \(C_j\setminus F\) attains \(D_j\), and \(F\setminus C_j\) is a minimum cover of its graph.

Let the allowed pool \(A_j\) be \(C_j\setminus\{e\}\) if the exceptional root has color j, and \(C_j\) otherwise. Put \(D_j^*=\max_{U\subset A_j}d(U)\). The audited axis-avoiding theorem implies the following precise input:

\[
\nu(B(V))\ge|V|\quad\text{for every }V\subset A_j\text{ avoiding }a=0. \tag{4}
\]

To see why the excluded root suffices, every positive finite V contains an inclusion-minimal positive subset. The classification says that an axis-avoiding critical subset is an isolated root or its three-owner patch, and either contains the exceptional root. The small x=2 patch touches the vertical axis and introduces no exception to (4).

#### Strict expansion for an inclusion-minimal restricted maximizer

Suppose \(D_j^*>0\). Choose U inclusion-minimal among allowed sets attaining it, and a minimum cover W of B(U). Every \(w\in W\) uniquely covers edges from at least two owners. If it uniquely covers none, it is redundant. If it uniquely covers only owner u, then \(W\setminus\{w\}\) covers \(B(U\setminus\{u\})\), whose deficiency is at least \(D_j^*\); this contradicts either maximality or inclusion-minimality. The same argument works at arbitrary deficiency.

For nonempty \(S\subset W\), let T be the owners of all edges incident to S, including doubly covered edges. Deleting T preserves the allowed pool, and

\[
d(U\setminus T)\ge D_j^*+|S|-|T|.
\]

If \(|T|\le|S|\), this contradicts maximality or inclusion-minimality. If T=U, use \(|U|=|W|+D_j^*>|S|\) directly. Hence

\[
|T|\ge|S|+1. \tag{5}
\]

No criticality, independent-component decomposition, hole normalization, or simultaneous canonical tie-breaker is assumed.

#### The two cones and root balance at arbitrary deficiency

The disjoint north edges force a horizontal owner whenever deficiency is positive. Equation (4) forces a vertical owner. The predecessor argument for an owner with both exponents positive uses only the preceding essentiality: at least one of \(u/6,2u/9,3u/4\) belongs to U. Otherwise its north-left endpoint is a leaf, forcing \(E(4u/3)\) uniquely and \(2u\notin W\); its east-right endpoint is then a leaf, forcing \(N(9u/2)\) uniquely and \(3u\notin W\). The latter owner makes R(u) available, a contradiction.

If \(1\in U\), both least roots are the origin; retain this case separately. Otherwise let \(x=2^A,y=3^B\) be the least roots, with \(A,B\ge1\). Set \(g=4/3,q=9/2\). Reversing decreasing predecessors, and using \(8=g^2q,27=gq^2\), gives

\[
U\subset x\langle g,q\rangle_{\ge0}\ \cup\ y\langle g,q\rangle_{\ge0},
\quad y=xg^{(B-2A)/3}q^{(2B-A)/3}. \tag{6}
\]

Coordinates are unique by the determinant-three exponent transformation. If \(A>2B\), the x-cone is inside the y-cone. The chain \(v_m=yg^m\), \(0\le m<B\), has a leaf at each north-left endpoint: both alternative owners have q-coordinate minus one. Essentiality forces the next east owner, reaching \(2^{2B}\), a smaller horizontal root than x.

If \(B>2A\), both cones lie inside the x-cone. Put \(y'=3^{2A}<y\le t\). For \(u_n=xq^n\), \(n<A\), the first exponent is positive and
\(u_n\le y'/q=2y'/9\le2t/9\), so E(u_n) is available. Both alternative owners at its right endpoint have g-coordinate minus one. Essentiality at the selected left endpoint forces \(u_{n+1}\). The chain reaches the forbidden smaller vertical root \(y'\). This proves, without a numerical-terminal argument,

\[
A/2\le B\le2A,\quad r=(2A-B)/3\ge0,\quad s=(2B-A)/3\ge0,
\quad A=2r+s,\ B=r+2s. \tag{7}
\]

#### The degenerate prefix repairs P1 and P2

Suppose \(s=0\). Then \(A=2B\), \(x=4^B\). For \(k=a+2b\), \(k_0=2B\), the y-cone in the nonnegative quadrant is exactly the preferred-color set with \(k\ge k_0\). To verify both directions, its q-coordinate is \((k-2B)/3\); once this is nonnegative, its g-coordinate \((a+n)/2\) is nonnegative too. The forced chain \(yg^m\), \(0\le m<B\), selects its north-right endpoints
\(2^{2m+1}3^{B-m-1}\). These are exactly every nonnegative point on \(k=k_0-1\). The last forced east edge gives \(x\le2t/3\).

Add all preferred-color diagonals \(k_0-3,k_0-6,\ldots\ge0\) as P, and all right-color diagonals \(k_0-4,k_0-7,\ldots\ge0\) as R. P is disjoint from U. A new north/east edge has its right endpoint on k−1, and a new rooted edge has it on k+2; therefore it meets R or the already selected frontier. Thus \(W\cup R\) covers \(B(U\cup P)\). The maximum label on \(a+2b=k\) is \(2^k\), so every added owner is at most \(x/8\le t/12\), below the exceptional-root window. Cover points are also on the board.

The diagonal size is \(f(k)=\lfloor k/2\rfloor+1\), with f(−1)=0. Pair owner diagonal \(k_0-3n\) with cover diagonal \(k_0-3n-1\). Their difference is one precisely for even n, so

\[
d(U\cup P)\ge D_j^*+|P|-|R|=D_j^*+\lfloor B/3\rfloor. \tag{P1}
\]

Maximality gives \(B\le2\). Overlap between R and W could only improve this inequality.

For \(r=0\), use \(k=2a+b,k_0=2A\). The x-cone is exactly the preferred-color set with \(k\ge k_0\). The q-chain's selected east-left endpoints cover the whole frontier \(k_0-1\): their coordinates are \((A-n-1,2n+1)\), \(0\le n<A\). Each preterminal q-label is at most \(y/q\le2t/9\), so all edges used exist. Add the same-spaced preferred diagonals as P and left-color diagonals as R. North/east left endpoints lie on k−1 and rooted left endpoints on k+2. Every new edge is covered. The maximal label on this diagonal is \(3^k\), so new owners are at most \(y/27\le t/27\), again excluding e. The same count proves

\[
d(U\cup P)\ge D_j^*+\lfloor A/3\rfloor,\qquad A\le2. \tag{P2}
\]

These repairs use a specified prefix and repairing cover; they do not assume unrestricted full-class filling. No zero coordinate is treated as a positive-length chain. The small vertical patch retains its actual critical interval \([12,18)\), rather than being truncated at the construction endpoint \(27/2\).

### Gaps

No gap was found in P1, P2, or the extension of their prerequisite root arguments to restricted maximizers. The original P3's proof is valid with its inactive-patch hypothesis; the next section supplies the missing compatibility statement and removes that restriction. None of the arguments here uses matching-rank submodularity or adds deficiencies of distinct critical components.

## Does one common optimum give a universal one-unit gap?

### Takeaway

Yes, for every \(t\ge18\): \(\tau(t)\ge Q(t)-1\). If equality with the construction fails, the highest vertical color must minimize the adjusted phase count and its restricted maximum deficiency is exactly one. This conclusion includes active patches; it does not assume that deleting a patch root always lowers deficiency by one.

### Cited Findings

- The source P3 proves the inactive-patch version and identifies the precise compatibility gap for active patches. [Source P3](<../boundary-dominance/canonical_audit_and_collision.md>).
- The two-cone chains and deep exclusion needed below have full independent derivations in [vertical_audit_and_transfer.md](<../boundary-dominance/vertical_audit_and_transfer.md>). Their dependence is only on the cone inclusion, essentiality and (5), so the following application to restricted maximizers is legitimate.

### Inferences

#### Incomparable roots give a unique top owner and deficiency one

For \(r,s\ge1\), put

\[
u_n=xq^n,\quad v_m=yg^m,\quad z=u_s=v_r=2^{2r}3^{2s}.
\]

The north-left alternatives along \(v_m\), \(m<r\), are outside both cones. They force \(2v_m/3\in W\), \(2v_m\notin W\), and the next east owner. The last edge gives \(z\le2t/3\). The east-right alternatives along \(u_n\), \(n<s\), are likewise outside both cones. They force \(3u_n/2\in W\), \(3u_n\notin W\), and \(u_{n+1}\in U\). Since \(u_n\le z/q\le4t/27\), rooted edges force \(2u_n\in W\). Their \(2s\)-vertex owner count forces all \(gu_n\), \(1\le n\le s\).

On the vertical chain, if any rooted edge exists, say exactly for indices \(0\le m\le h<r\), the selected set \(\{2v_m/3:m<r\}\cup\{3v_m:m\le h\}\) has \(r+h+1\) vertices and at most \(r+h+2\) owners. Expansion forces \(qv_{h+1}=6v_h\in U\). If \(h<r-1\), then \(v_{h+1}\le2t/9<t/3\), a contradiction. Thus h=r−1 and \(qz\in U,z\le2t/9\). If none exists, \(y>t/3\) and \((4/3)^r=z/y<2\), so \(r\in\{1,2\}\).

The deep alternative is impossible when both r,s are positive. Its forced horizontal selected set has owner coordinates

\[
H=\{(0,n):0\le n\le s\}\cup\{(1,n):1\le n\le s\},
\]

in the x-based \((g,q)\) system. The vertical selected set has owners

\[
V=\{(m,s):-r\le m\le0\}\cup\{(m,s+1):1-r\le m\le0\}.
\]

These sets intersect only at z. They have \(2s+1\) and \(2r+1\) owners, while their selected vertex sets have \(2s\) left and \(2r\) right vertices. The forced owners gz and qz then force two new selected vertices: E(gz) has excluded right endpoint \(2z/3=3u_{s-1}\), hence \(2z\in W\); N(qz) has excluded left endpoint \(3z/2=2v_{r-1}\), hence \(3z\in W\). The new vertices lie beyond the selected ranges and are distinct. Their possible owners are \(\{z,gz,6z\}\) and \(\{z,qz,6z\}\), adding at most one owner. This gives \(2r+2s+2\) selected vertices with at most that many owners, contradicting (5). The double coverage of R(z) is harmless because (5) counts all incident owners.

Therefore incomparable roots force \(y>t/3\), \(r\in\{1,2\}\). There is only one vertical owner: the next same-color vertical root is 27y>t. Removing y leaves an allowed axis-avoiding set, so (4) gives \(d(U)\le1\). Thus \(D_j^*=1\), and inclusion-minimality now makes U genuinely critical. Also y is the highest vertical point of the entire board, since \(y\le t<3y\).

#### Forced owners for every non-top restricted maximizer

Let \(j_{\rm top}=-\lfloor\log_3t\rfloor\pmod3\). If \(j\ne j_{\rm top}\) and \(D_j^*>0\), an inclusion-minimal maximizer has the origin or a degenerate root pair, since the incomparable case was just placed in the top color. P1 and P2 then give:

\[
\begin{array}{c|c|c}
j&\text{possible least-root case}&\text{forced owner }m_j\\\hline
0&1\in U&6\\
1&r=0,A=1\text{ or }s=0,B=2&12\\
2&r=0,A=2\text{ or }s=0,B=1&18.
\end{array} \tag{8}
\]

For the origin case, R(1) forces one of 2,3 into W. Both cannot be selected: their common edge would be doubly hit, leaving either endpoint at most one unique owner. Whichever endpoint is selected forces owner 6. For color one, the q-chain from 2 and its first strip force 12, or the g-chain from 9 passes through 12. For color two, the q-chain from 4 passes through 18. In the other case the chain 3,4 selects 2 and excludes 6; for \(t\ge18\), R(3) forces 9, and the selected pair \(\{2,9\}\) has possible owners only \(\{3,4,18\}\). Equation (5) forces 18.

Every maximizing set contains an inclusion-minimal maximizing subset. Hence the relevant \(m_j\) belongs to every restricted maximizing set, not just to some separately chosen canonical representative.

#### The single-exclusion compatibility lemma

For the exceptional color, abbreviate its unrestricted and restricted maxima as D,D*. Removing one owner from a maximizing set decreases its deficiency by at most one, because matching number cannot increase under edge deletion. Consequently

\[
D-1\le D^*\le D. \tag{9}
\]

If D*=D, choose an allowed maximizing set U* and its minimum cover W*. The corner cover \((C_j\setminus U^*)\cup W^*\) is globally minimum, selects e, and its omitted restriction is a restricted maximizer. If D*=D−1, every unrestricted maximizing set contains e; otherwise it would be an allowed set of deficiency D. For each such set U, the deletion inequality and restricted maximality give \(d(U\setminus\{e\})=D^*\). Thus any global minimum already has the required restricted maximizer in this case.

There is at most one exceptional color. It follows that **one global minimum F can be chosen so that all three omitted restrictions are simultaneously restricted maximizers**. Other colors automatically have unrestricted maximizing omitted sets by (3). This lemma is valid for a patch root as well as an isolate. It does not claim a fixed deletion drop in the patch case. For an isolate the drop is exactly one because its graph is empty.

#### Universal one-unit-gap theorem and generalized P3

Assume \(t\ge18\) and suppose \(\tau<Q\). Then \(D_j>\delta_j\) for every color. Equation (9) ensures \(D_j^*>0\) in every allowed pool. Choose the common optimum F just constructed. The two non-top colors omit their corresponding two members of \(\{6,12,18\}\) from this same F, by (8).

If an inclusion-minimal maximizing subset in the top omitted restriction contained the origin or had degenerate roots, it would force the third member outside F as well, leaving the valid corner \(\{6,12,18\}\) uncovered. Hence the top restricted pool has an incomparable maximizing subset, and \(D_{j_{\rm top}}^*=1\).

If \(\delta_{j_{\rm top}}=0\), unrestricted and restricted maxima coincide, so \(D_{j_{\rm top}}=1\). If \(\delta_{j_{\rm top}}=1\), the counterexample assumption gives \(D_{j_{\rm top}}>1\); combined with (9) and D*=1 this forces \(D_{j_{\rm top}}=2\). Thus the deletion drop in the top color is forced to be one, rather than assumed. In all cases

\[
\boxed{\tau=K_{j_{\rm top}}-\delta_{j_{\rm top}}-1=Q_{j_{\rm top}}-1.} \tag{P3+}
\]

Since \(\tau<Q_j\) for every j and these numbers are integers, \(Q_{j_{\rm top}}\le Q_j\) for every j. Therefore

\[
\boxed{\tau\ge Q-1\quad(t\ge18),}
\]

and any failure of equality must have exactly this one-unit gap, with the top color adjusted-minimizing and supporting an incomparable critical restricted maximizer. This is an aggregate theorem: it follows from maxima over entire allowed pools, not from summing deficiency-one components.

### Gaps

P3+ alone does not prove equality. The original active-patch gap is repaired by the compatibility lemma, but a contradiction still requires excluding a winning top incomparable maximizer. The next prefix repair and finite counts supply that missing step in the assembled candidate.

## Does the high-prefix repair finish the global finite formula?

### Takeaway

The new repair limits the remaining r=1 high family to s≤3. All surviving incomparable windows have a top adjusted count strictly above another phase. This contradicts P3+, yielding a complete proof candidate for (C), including the small boards treated directly below. The high-prefix lemma and the complete assembly are written here in a form suitable for the requested fresh final audit.

### Cited Findings

- The previously audited high-case reductions are V9–V10 of [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>), with their full independent reconstruction in [vertical_audit_and_transfer.md](<../boundary-dominance/vertical_audit_and_transfer.md>). The required cap argument is restated below to make the global assembly reviewable.
- The exact endpoint table in this section was checked with integer and rational arithmetic by [prefix_phase_checks.py](<prefix_phase_checks.py>); the [saved certificate](<prefix_phase_checks.json>) records K, I, P and adjusted counts separately. It checks only the listed intervals, not a prefix sweep.

### Inferences

#### The high cap leaves r=2,s=1 or the r=1 family

For the incomparable maximizer from P3+, retain \(u_n=xq^n\), and now denote \(v_n=gu_n,w_n=g^2u_n,z_n=g^3u_n\). The horizontal selected strip consists of \(L_n=3u_n/2,A_n=2u_n\), \(0\le n<s\), and forces \(v_1,\ldots,v_s\). Suppose \(s\ge2\) and \(w_s=g^2z>t\).

The north edge of \(v_n\) already has its left endpoint \(A_{n-1}\in W\). If its right endpoint \(\beta_n=2v_n/3\) were selected, essentiality would require both other owners uniquely, including \(w_n\), and would exclude \(2v_n\). At n=s this is impossible because \(w_s>t\). At smaller n, the available rooted edge propagates a selected \(\beta_n\) to \(\beta_{n+1}\); indeed \(v_n\le gz/q\le16t/81<t/3\). Backward induction excludes all these \(\beta_n\), forcing \(2v_n\in W\), \(1\le n<s\). The resulting \(3s-1\) selected vertices have at most \(3s\) owners, so (5) forces \(w_1,\ldots,w_{s-1}\).

Their rooted edges are available because \(w_n\le g^2z/q\le64t/243<t/3\). The cap vertex \(\gamma_s=2w_s/3=3w_{s-1}\) is a leaf: its other possible owners \(w_s,z_s\) are outside the board. It is excluded from W. A second backward induction, using the same double-coverage and essentiality argument, excludes \(\gamma_2,\ldots,\gamma_s\), and forces \(2w_n\in W\), \(1\le n<s\). For n=1 only its rooted edge is used, not a nonexistent north edge.

These final \(4s-2\) selected vertices have owners contained in

\[
\{u_0,\ldots,u_s\}\cup\{v_1,\ldots,v_s\}
\cup\{w_1,\ldots,w_{s-1}\}\cup\{z_2,\ldots,z_{s-1}\},
\]

also of size \(4s-2\), contradicting (5). The bottom formal owners \(v_0,z_1\) are nonsmooth, and \(w_s,z_s\) exceed t. At s=2 the last range is empty; the cap itself supplies the needed selection. All selected vertices are distinct because after division by 2x their g-coordinates are −1,0,1,2 and their q-coordinates are their displayed indices.

For r=2, the high condition gives \(z=g^2y>16t/27\), so \(g^2z>256t/243>t\). Hence s=1. Then \(x=32,y=81,z=144\), and \(3z/2\le t<3y\) gives \([216,243)\).

For r=1, \(y>t/3\) gives \(z>4t/9\). In fact \(z>t/2\): otherwise E(gz) is available with excluded right endpoint \(2z/3=3u_{s-1}\), forcing \(2z\in W\). Its other possible owners are z and 6z; R(z) is unavailable because \(z>t/3\), and 6z is outside the board. It would support only one owner. This violates essentiality. For s=1, \(z=36\), yielding \([54,72)\). For s≥2, the cap contradiction also gives

\[
r=1,\quad t/2<z\le9t/16,
\quad z=4\cdot9^s,
\quad64\cdot9^{s-1}\le t<8\cdot9^s. \tag{10}
\]

#### The new high-prefix repair P4

Suppose r=1 and s≥1. Then \(A=s+2,B=2s+1\), \(y=3^{2s+1}\), \(z=4y/3\). Put \(k=2a+b\), \(k_0=2A\). The horizontal cone is exactly the preferred-color region k≥k0. In x-based coordinates the vertical cone begins at \((-1,s)\). Any of its points below k0 must have first cone coordinate −1; its ordinary first exponent is then \(s-n\), while n≥s. Nonnegativity forces n=s. Therefore

\[
U\cap\{k<k_0\}=\{y\},\qquad k(y)=k_0-3. \tag{11}
\]

Let P0 be all preferred-color diagonals \(k_0-3,k_0-6,\ldots\ge0\), let \(P=P_0\setminus\{y\}\), and let R be all left-color diagonals \(k_0-4,k_0-7,\ldots\ge0\). Equation (11) makes P disjoint from U.

The q-chain selects the frontier left vertices L_n for \(0\le n<s=A-2\). Their ordinary first exponents are \(A-1,A-2,\ldots,2\), so they are exactly the k0−1 frontier points with a≥2. A new north or east edge has its left endpoint on a diagonal k−1 in R. A new rooted edge has its left endpoint on k+2. For a new owner below the first prefix diagonal, this endpoint is in R. On the first diagonal, the only owner with a=0 is y, which was excluded from P. Every remaining new owner has a≥1, so its rooted-left endpoint has a≥2 and lies on the selected frontier. **The missing frontier point 2y would be needed only for the old owner y, whose edges remain covered by W.** No new edge needs that point. Thus \(W\cup R\) covers \(B(U\cup P)\).

All added points lie on the board. After removing y, the largest owner on the first prefix diagonal is \((2/9)y=z/6\); lower diagonals have maxima at most y/27. Hence every added owner is at most \(z/6\le t/9\), using \(z\le2t/3\). Every cover point in R is at most \(y/3=z/4\le t/6\). In particular no added owner is the excluded exceptional root, which exceeds \(4t/27>t/9\). This checks the allowed-pool condition even during an active patch.

The same diagonal pairing used in P2 gives \(|P_0|-|R|=\lfloor A/3\rfloor\). Removing y subtracts exactly one. Therefore

\[
\boxed{d(U\cup P)\ge D_j^*+\lfloor A/3\rfloor-1
=D_j^*+\lfloor(s-1)/3\rfloor.} \tag{P4}
\]

Since U maximizes over its allowed pool, P4 rules out **every s≥4**. No equality-exchange compatibility is needed for s=1,2,3; the exact phase comparisons below suffice. P4 does not assume that the whole color class can be filled, nor that a critical set is forward closed.

#### Every remaining incomparable window has a losing top phase

Only the following windows remain. Intervals are left-closed and right-open. The first r=1,s=1 interval is split at the birth of the isolate 64.

| Case | t interval | K | I | P | Adjusted Q-vector | Top color |
|---|---|---|---|---|---|---:|
| r=1,s=1 | [54,64) | (6,5,5) | (0,0,0) | (0,0,0) | (6,5,5) | 0 |
| r=1,s=1 | [64,72) | (7,5,5) | (1,0,0) | (0,0,0) | (6,5,5) | 0 |
| r=2,s=1 | [216,243) | (9,8,9) | (0,0,0) | (0,0,0) | (9,8,9) | 2 |
| r=1,s=2 | [576,648) | (12,12,11) | (1,0,0) | (0,0,0) | (11,12,11) | 1 |
| r=1,s=3 | [5184,5832) | (20,19,20) | (1,0,0) | (0,0,0) | (19,19,20) | 2 |

The top coordinate is strictly larger than the minimum in every row. There is no active patch on these windows. At t=54 and t=216 the previous patch ends at its strict upper endpoint; it must not be retained. The isolates in the last two rows are 512 and 4096, both color zero, and persist throughout the stated intervals. At the cap equality in the last two cases, the allowed endpoint \(g^2z=t\) is included.

These are direct finite counts. For example, at 5184 the eight row lengths for b=0,…,7 are 13,11,10,8,7,5,3,2, giving K=(20,19,20). There is no smooth point strictly between 5184 and 5832. The exact checker verifies no smooth birth or indicator threshold lies inside any listed interval, and verifies the top color and strict adjusted comparison separately. Its output was `Verified eight exact base intervals and five high-window subintervals.` The coordinator independently read and replayed this checker, which exited zero, and reported a successful separate high-phase checker replay including four prefix-geometry samples. Those replays support the finite endpoints and specified geometry only; the uniform prefix argument is the proof above.

P3+ requires the top phase to minimize the adjusted count whenever \(\tau<Q\). The table contradicts that requirement. Consequently no counterexample exists for t≥18.

#### The small boards and complete conclusion

For completeness, the remaining real intervals \(3\le t<18\) are:

| t interval | K | I | P | Q=min adjusted count | Cover |
|---|---|---|---|---:|---|
| [3,4) | (1,1,1) | (0,0,0) | (0,0,0) | 1 | {2} |
| [4,6) | (1,1,2) | (0,0,1) | (0,0,0) | 1 | {2} |
| [6,8) | (2,1,2) | (0,0,0) | (0,0,0) | 1 | {2} |
| [8,9) | (3,1,2) | (1,0,0) | (0,0,0) | 1 | {2} |
| [9,12) | (3,2,2) | (1,0,0) | (0,0,0) | 2 | {3,4} |
| [12,27/2) | (3,3,2) | (0,0,0) | (0,1,0) | 2 | {3,4} |
| [27/2,16) | (3,3,2) | (0,0,0) | (0,0,0) | 2 | {3,4} |
| [16,18) | (3,4,2) | (0,1,0) | (0,0,0) | 2 | {3,4} |

Below nine, the nonempty corner at one gives lower bound one. From nine onward the three corners rooted at 1,2,3 have empty common intersection, giving lower bound two. The displayed covers meet every corner for their entire intervals. The indicator transition at 27/2 is retained even though it is not a smooth integer birth. This proves equality on the small boards directly.

Combining the construction (1), the contradiction for t≥18, and the small-board table yields the assembled candidate theorem

\[
\boxed{\tau(D_t)=\min_{j\in\mathbb Z/3\mathbb Z}
\bigl(K_j(t)-I_j(t)-P_j(t)\bigr)\qquad(t\ge3).} \tag{C}
\]

### Gaps and final-review scope

The proof candidate's exact logical dependencies are: the unconditional axis-avoiding classification giving (4); the finite bipartite matching-cover theorem; restricted minimal-maximizer essentiality and expansion (5); the independently reconstructed two cones, root balance and deep exclusion; P1–P2; the single-exclusion compatibility lemma and same-optimum collision P3+; the cap count, new high-prefix repair P4, and the specified exact finite table. Each implication used in the global assembly is displayed above. No independent-deficiency decomposition, full-class filling, submodularity, disjoint-tripod theorem, unproved finite-state compression, or arithmetic conjecture is used.

The requested final fresh audit should attack this whole chain, especially the new prefix's missing-frontier treatment and the simultaneous restricted-maximizer quantifiers. No additional exploratory work follows this saved assembly. The certificate script has assert-based checks and uses only the standard library; it does not validate an unbounded theorem by enumeration. Even acceptance of (C) proves only the finite combinatorial formula: the separate irrationality-return and nonvanishing obligations for Erdős #168(ii) remain. No Lean verification or external submission was performed.
