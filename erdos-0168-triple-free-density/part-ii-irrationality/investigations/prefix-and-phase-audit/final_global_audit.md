# Fresh adversarial audit of the global finite-cover formula

Audit completed 7 November 2026. **Verdict: PASS for the finite formula (C).** I reconstructed the dependencies below from their arguments, rather than accepting earlier PASS labels. I found no fatal mathematical gap in the current assembly in `prefix_audit.md`, `patch_global.md`, and `high_phase.md`. In particular, the single-owner lemma supplies the common optimum actually needed by the collision argument, and the high-prefix exchange supplies a universal augmentation rather than a numerical extrapolation.

The accepted conclusion is precisely
\[
\tau(t)=\min_{j\in\mathbb Z/3\mathbb Z}
\bigl(K_j(t)-I_j(t)-P_j(t)\bigr),\qquad t\ge3.
\tag{C}
\]
Here the board, corners, coloring, and indicators are those in the assignment. This verdict makes no claim about irrationality, historical priority, or any arithmetic transfer. The current prefix-and-phase folder contained `prefix_audit.md`, which I read; it did not contain a separate `global_finite_proof.md` when I inspected it.

## Do the foundations and the axis-avoiding classification support the required universal input?

### Takeaway

Yes. The exact matching reduction, the classification of every axis-avoiding critical set, and the passage from that classification to every allowed axis-avoiding subset are valid. The classification has no hidden one-root or independent-component hypothesis. Its small vertical-patch exception is respected by the current global proof.

### Cited Findings

- The original construction, board definitions, and exact matching reduction are in [168_grid.md](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>); the current complete statement is also at the beginning of [prefix_audit.md](<prefix_audit.md:19>).
- The classification argument under review is the full three-strip argument in [multiroot.md](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>), including its extension from critical sets to all axis-avoiding sets. I also read the explicit incidence reconstruction in [combinatorial_and_coefficient_audit.md](<../global-boundary-proof/combinatorial_and_coefficient_audit.md:20>).
- The canonical matching correspondence and deletion inequalities are stated in [canonical_phase.md](<../global-boundary-proof/canonical_phase.md:25>). Their restricted, inclusion-minimal formulation is stated and proved in [prefix_audit.md](<prefix_audit.md:74>).

### Inferences

#### Exact matching and cover correspondence

Fix a color \(j\). Each corner has exactly one owner in \(C_j\). Its opposite pair is an edge of the graph on the two remaining colors. Solving for which position the owner occupies gives exactly
\[
N(u)=(u/3,2u/3),\quad
E(u)=(3u/2,u/2),\quad
R(u)=(2u,3u).
\]
Their respective availability conditions are \(b\ge1\); \(a\ge1,3u/2\le t\); and \(3u\le t\). In particular, a vertical owner never acquires an east edge merely because its numerical cutoff holds.

The full possible-owner lists at a physical left or right vertex are
\[
l:\quad l/2,\ 2l/3,\ 3l;
\qquad
r:\quad r/3,\ 3r/2,\ 2r,
\tag{1}
\]
with nonsmooth, off-board, absent, and unavailable possibilities removed. These lists are obtained directly from the three edge formulas and are exhaustive.

If \(W\) covers \(B(U)\), then
\((C_j\setminus U)\cup W\) hits every corner. Conversely, a corner cover \(F\) gives
\(U=C_j\setminus F\), \(W=F\setminus C_j\), with \(W\) covering \(B(U)\). Bipartite matching-cover equality therefore gives
\[
\tau=K_j-D_j,\qquad
D_j=\max_{U\subset C_j}\bigl(|U|-\nu(B(U))\bigr).
\tag{2}
\]
For **every** globally minimum \(F\), its omitted set attains \(D_j\) in **every** color. Indeed, a smaller graph cover or a larger deficiency would produce a smaller original cover. This requires no simultaneous canonical tie-breaker.

#### Essentiality and strict expansion at arbitrary restricted deficiency

Let \(A_j\subseteq C_j\) be the allowed pool, let \(D_j^*>0\) be its maximum deficiency, and let \(U\subset A_j\) be inclusion-minimal among its maximizers. Choose any minimum graph cover \(W\), so
\(|U|-|W|=D_j^*\).

If a selected vertex uniquely covers edges of no owner, it is redundant. If it uniquely covers only one owner \(u\), deleting that vertex and \(u\) leaves a cover and a proper subset of deficiency at least \(D_j^*\). An improvement contradicts maximality; equality contradicts inclusion-minimality. Thus every selected vertex uniquely supports at least two distinct owners, and a leaf cannot be selected.

For nonempty \(S\subset W\), let \(T(S)\) contain the owners of **all** available edges incident to \(S\), including edges covered at both ends. Then \(W\setminus S\) covers \(B(U\setminus T(S))\), and
\[
d(U\setminus T(S))\ge D_j^*+|S|-|T(S)|.
\]
If \(|T(S)|\le|S|\), this contradicts maximality or inclusion-minimality. The empty-remainder case is harmless: if \(T(S)=U\), then
\(|T(S)|=|W|+D_j^*>|S|\) directly. Consequently
\[
|T(S)|\ge |S|+1\qquad(\varnothing\ne S\subset W).
\tag{3}
\]
Deleting owners preserves the allowed pool. No unrestricted exchange, deficiency-one assumption, or claim about components is being inserted here.

#### Predecessor lemma

For an owner \(u\) with \(a,b\ge1\), suppose none of
\(u/6,2u/9,3u/4\) lies in \(U\). By (1), the north-left endpoint is a leaf, forcing its right endpoint. Essentiality there forces \(E(4u/3)\) uniquely, excluding \(2u\) from \(W\) and implying \(2u\le t\). Hence \(E(u)\) exists. Its right endpoint is a leaf, forcing its left endpoint. Essentiality there forces \(N(9u/2)\) uniquely, excluding \(3u\) from \(W\). The forced owner \(9u/2\le t\) makes \(R(u)\) available with neither endpoint selected, a contradiction.

This derivation uses only essentiality and the fact that this particular owner has both exponents positive. Other owners may lie on either axis.

Put \(g=4/3,q=9/2\). Reversing the decreasing predecessor steps multiplies by \(g,q,gq\). Same-color horizontal roots differ by powers of \(8=g^2q\); same-color vertical roots differ by powers of \(27=gq^2\). Thus descending predecessor paths give the asserted cone inclusions, without forward closure. Equality of two \((g,q)\)-coordinate representations is equality of their integer exponent pairs, because the exponent matrix has determinant three.

#### Reconstructing the axis-avoiding classification

For a critical set, minimal positive deficiency implies \(d(U)=1\): deleting one owner gives matching number at least \(|U|-1\), while positivity gives the reverse upper bound. Hence \(|W|=|U|-1\), and essentiality and (3) apply.

If the set avoids the vertical axis, descending predecessors terminate at horizontal roots. Let its least such root be \(x=2^A\), \(A\ge1\). Every owner lies in the nonnegative \((g,q)\)-cone above \(x\). If \(x>2t/3\), it has no edge and criticality makes the set exactly \(\{x\}\).

Otherwise write
\[
u_n=xq^n,\quad v_n=xgq^n,\quad
w_n=xg^2q^n,\quad z_n=xg^3q^n.
\]
The negative-\(g\) alternatives at the east-right endpoint of \(u_n\) are outside this cone. While its east edge exists, leaf exclusion and essentiality force
\(L_n=3u_n/2\in W\), \(u_{n+1}\in U\), and \(3u_n\notin W\). Since the set avoids the vertical axis, the chain cannot terminate by crossing that axis. It must terminate at some \(u_k\) with
\[
k\ge1,\quad 2t/3<u_k\le t,\quad A-k\ge1.
\]
All preterminal rooted edges exist, and they force \(A_n=2u_n\in W\), \(0\le n<k\). The \(2k\) selected vertices \(L_n,A_n\) have at most the \(2k+1\) owners
\[
u_0,\ldots,u_k,\quad v_1,\ldots,v_k.
\]
Here \(v_0\) is nonsmooth. Strict expansion forces every listed owner, in particular
\(u_k\le3t/4\) and \(v_k\le t\).

The next cap is \(w_k>32t/27>t\). If \(\beta_n=2v_n/3\) were selected, its north edge would already be covered by \(A_{n-1}\). The other two owners would both have to support it uniquely, forcing \(2v_n\notin W\). For \(n<k\), the available rooted edge propagates this selection to \(\beta_{n+1}\). At the cap \(\beta_k\), the required owner \(w_k\) is absent. Backward induction therefore excludes every \(\beta_n\) and forces \(2v_n\in W\) for \(1\le n<k\). The resulting \(3k-1\) selected vertices force all \(3k\) owners through \(w_{k-1}\).

If \(k\ge2\), all rooted edges of \(w_1,\ldots,w_{k-1}\) exist because
\(w_{k-1}\le8t/27<t/3\). The cap \(\gamma_k=2w_k/3=3w_{k-1}\) is an actual board vertex and a leaf: its other owners \(w_k,z_k\) are off-board. The same backward induction excludes \(\gamma_2,\ldots,\gamma_k\), forcing \(2w_n\in W\), \(1\le n<k\). For \(n=1\) this uses the rooted edge and \(\gamma_2\), not a nonexistent north edge of the horizontal root \(w_1\).

The final \(4k-2\) selected vertices have owners contained in
\[
\{u_0,\ldots,u_k\}\cup\{v_1,\ldots,v_k\}
\cup\{w_1,\ldots,w_{k-1}\}\cup\{z_2,\ldots,z_{k-1}\},
\]
also of size \(4k-2\), contradicting (3). The omitted formal owner \(z_1\) is nonsmooth and \(z_k>t\). At \(k=2\) the final range is empty and the same count remains valid. The selected vertices are distinct: after division by \(2x\), their \(g\)-coordinates are respectively \(-1,0,1,2\). This also verifies that no extra root or off-chain owner is missing from the counts.

Thus \(k=1\). It forces exactly the critical patch
\[
\{x,9x/2,6x\},\quad A\ge2,\quad 6x\le t<27x/4.
\]
The four owned edges form a five-vertex path, covered by \(3x/2,2x\), with a matching of size two. Since this is already a positive subset, criticality makes it the whole set. This reconstructs the classification for arbitrary axis-avoiding critical sets, including sets initially allowed arbitrarily many horizontal roots.

#### The precise all-subset input and the upper construction

There is at most one dyadic root in either exceptional interval. An active patch satisfies \(6e\le t<27e/4<8e\); the largest dyadic board point is \(4e\le2t/3\), excluding an isolate. Thus there is at most one exceptional root across all colors. Every such root is greater than \(4t/27\).

Delete this root from its color's allowed pool, if it exists. Every positive axis-avoiding subset would contain a critical positive subset. The classification would make that critical subset an isolate or patch containing the deleted root. This is impossible. Therefore the exact input used later is
\[
d(V)\le0\quad\text{for every allowed axis-avoiding }V.
\tag{4}
\]
It applies to arbitrary subsets, not merely to selected critical components.

The construction patch permits \(A=1\), whereas the axis-avoiding classification requires \(A\ge2\). At \(e=2\), the owner 9 is vertical. This does not invalidate (4): an axis-avoiding critical set can never be that patch. Nor does the global proof identify a constrained optimum with a vertical phase in this exceptional window. The current construction simply replaces the three same-color vertices by the two displayed opposite vertices, which covers all four opposite edges and saves one. Together with isolated-point removal it gives
\(\tau\le Q:=\min_j(K_j-I_j-P_j)\).

### Gaps

No gap was found in the foundations required for (C). The earlier claim of exact constrained equality for a prescribed vertical phase is false for the small \(e=2\) patch, but the current proof uses neither that claim nor any global vertical-phase normalization. The allowed-pool assertion (4), which it does use, is valid.

## Do root balance, the prefix restrictions, and one common optimum justify the aggregate collision?

### Takeaway

Yes. The geometric restrictions extend to inclusion-minimal restricted maximizers of arbitrary positive deficiency. The mandatory-owner statement holds for every maximizing omitted set in the relevant pool. The one-owner lemma produces one actual global optimum to which all three statements apply, so the collision does not combine three incompatible covers.

### Cited Findings

- The original two-cone and chain arguments are in [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>); I also inspected the local reconstruction in [vertical_audit_and_transfer.md](<../boundary-dominance/vertical_audit_and_transfer.md:19>).
- The deep exclusion is the exact two-strip count in [deep_branch.md](<../boundary-dominance/deep_branch.md:63>).
- The earlier P1/P2 and collision derivation is in [canonical_audit_and_collision.md](<../boundary-dominance/canonical_audit_and_collision.md>). The current arbitrary-deficiency root-balance proof, prefix repairs, and mandatory-owner table are in [prefix_audit.md](<prefix_audit.md:92>).
- The common-optimum lemma is proved in [patch_global.md](<patch_global.md>) and restated with the global contradiction in [prefix_audit.md](<prefix_audit.md:198>).

### Inferences

#### Both axes and root balance before deficiency is known to be one

The north edges of the nonhorizontal owners form a matching. Thus a positive-deficiency set has a horizontal owner. Equation (4) supplies a vertical owner for a positive allowed maximizer. If it contains 1, both least roots are 1. Otherwise let the least roots be \(x=2^A,y=3^B\), \(A,B\ge1\). The predecessor argument gives
\[
U\subset x\langle g,q\rangle_{\ge0}\ \cup\ y\langle g,q\rangle_{\ge0},
\qquad y=xg^{(B-2A)/3}q^{(2B-A)/3}.
\tag{5}
\]

The current root-balance proof works without criticality. If \(A>2B\), both cones lie in the vertical cone. Along \(yg^m\), \(0\le m<B\), north-left alternatives have negative \(q\)-coordinate. Leaf exclusion and essentiality force the next east owner. No early cutoff is permissible: unavailable continuation would already contradict essentiality. The chain reaches \(2^{2B}\), smaller than the alleged least horizontal root.

If \(B>2A\), both cones lie in the horizontal cone, and \(y'=3^{2A}<y\le t\). Every preterminal label of the chain from \(x\) to \(y'\) is at most \(y'/q\le2t/9\), so its east edge exists. Negative-\(g\) alternatives are excluded, and essentiality forces the entire chain to the forbidden smaller vertical root. This is a direct contradiction and avoids extending the older critical-only argument by fiat.

Hence
\[
r=(2A-B)/3\ge0,\quad s=(2B-A)/3\ge0,
\qquad A=2r+s,\ B=r+2s.
\tag{6}
\]

#### Incomparable roots: exact strips, deep exclusion, and the top color

For \(r,s\ge1\), let \(u_n=xq^n\), \(v_m=yg^m\), and \(z=u_s=v_r\). Along the vertical chain, the north-left alternatives are outside both cones, forcing
\[
2v_m/3\in W,\quad 2v_m\notin W\quad(m<r),
\qquad 3z/2\le t.
\]
The analogous horizontal chain forces
\[
3u_n/2\in W,\quad 3u_n\notin W,\quad 2u_n\in W\quad(n<s).
\]
Its \(2s\)-vertex owner count forces the first strip \(gu_1,\ldots,gu_s\).

The vertical rooted-edge indices, when nonempty, are \(0,\ldots,h\). The selected vertices \(2v_m/3\), \(m<r\), and \(3v_m\), \(m\le h\), have only the chain owners and \(qv_1,\ldots,qv_{h+1}\). Their count is one larger than the selected count, so (3) forces \(qv_{h+1}=6v_h\in U\). If \(h<r-1\), then \(v_{h+1}\le2t/9<t/3\), contradicting the endpoint of the available-index interval. Thus either \(z\le2t/9\) and \(qz\in U\), or \(y>t/3\) and \(g^r<2\), whence \(r\in\{1,2\}\).

The low alternative contradicts (3) independently of the value of the deficiency. In coordinates based at \(x\), the horizontal selected strip has possible owners
\[
H=\{(0,n):0\le n\le s\}\cup\{(1,n):1\le n\le s\},
\]
while the vertical selected strip has possible owners
\[
V=\{(m,s):-r\le m\le0\}\cup\{(m,s+1):1-r\le m\le0\}.
\]
They intersect only at \(z=(0,s)\). Together they have \(2r+2s\) selected vertices and \(2r+2s+1\) owners. The forced owners \(gz,qz\) and the last chain exclusions force two further selected vertices \(2z,3z\). Their owner lists add at most the single new owner \(6z\). The vertices are new and distinct by their coordinates and opposite bipartition colors. Hence \(|T(S)|\le|S|\), contradicting (3). Double coverage of \(R(z)\) causes no exception, since (3) counts all incident owners.

Therefore \(y>t/3\). It is the largest vertical power on the entire board, so this case occurs only in its color \(q_{\rm top}\). It is also the only vertical owner of \(U\); the next same-color vertical power is \(27y>t\). Deleting \(y\) leaves an allowed axis-avoiding set. Matching monotonicity and (4) give
\[
0<D_j^*=d(U)\le d(U\setminus\{y\})+1\le1.
\tag{7}
\]
Thus the deficiency becomes one only here, and inclusion-minimality now makes \(U\) genuinely critical. There has been no decomposition of an aggregate maximizer into critical components.

#### Degenerate-prefix gains and their exact allowed-pool condition

For \(s=0\), \(A=2B\). With \(k=a+2b,k_0=2B\), the vertical cone is exactly the preferred-color region \(k\ge k_0\) in the nonnegative quadrant. The forced vertical chain selects every right-color point on \(k=k_0-1\). Add all preferred-color points on \(k_0-3,k_0-6,\ldots\), and repair with all right-color points on \(k_0-4,k_0-7,\ldots\).

A new north/east edge has its right endpoint on \(k-1\), and a new rooted edge has its right endpoint on \(k+2\). Each lies either in the new repair or on the selected frontier. All added owners are on-board and at most \(x/8\le t/12\); every exceptional root exceeds \(4t/27\), so no forbidden owner is reintroduced. The diagonal size is \(f(k)=\lfloor k/2\rfloor+1\), with \(f(-1)=0\). Pairing each owner diagonal with the diagonal immediately below gives gain \(\lfloor B/3\rfloor\). Maximality therefore gives \(B\le2\).

For \(r=0\), use \(k=2a+b,k_0=2A\), and the horizontal chain's left-color frontier. The same endpoint check gives gain \(\lfloor A/3\rfloor\). Every added owner is at most \(y/27\le t/27\), also below the exceptional window. Thus \(A\le2\).

These are augmentations on the original board in the entire allowed pool. They do not have to preserve the old least roots, and need no smaller-board induction or full-class-filling principle. Overlap of the repair with \(W\) only improves the gains.

#### The mandatory-owner table is a conditional statement about every maximizer

Outside the top color, every inclusion-minimal positive restricted maximizer is origin-containing or degenerate. The prefix limits leave exactly these cases:

| Color | Least-root case | Required owner |
|---|---|---:|
| 0 | origin | 6 |
| 1 | \(r=0,A=1\), or \(s=0,B=2\) | 12 |
| 2 | \(r=0,A=2\), or \(s=0,B=1\) | 18 |

For the origin, \(R(1)\) selects at least one of 2 and 3. Selecting both makes their common edge double-covered; each then has at most the single other owner 6 to support uniquely, violating essentiality. The selected endpoint therefore forces 6.

In color 1, the chain from 2 to 9 and its first selected strip force 12; alternatively the vertical chain is \(9,12,16\). In color 2, the chain from 4 to 81 passes through 18. In the other color-2 case the chain \(3,4\) selects 2 and excludes 6. For \(t\ge18\), \(R(3)\) forces 9 into \(W\). The selected pair \(\{2,9\}\) has possible owners only \(\{3,4,18\}\), forcing 18 by (3).

A useful availability qualification is that the last forcing also requires the actual edge \(E(18)\), hence \(t\ge27\). Consequently such a canonical configuration cannot exist for \(18\le t<27\). The conditional statement “if it exists, it contains 18” is valid throughout \(t\ge18\); no unavailable edge is counted as present. This slightly sharper observation is consistent with the qualification already noted in `patch_global.md`.

Every maximizing set contains an inclusion-minimal maximizing subset: the pool is finite. Therefore the required owner belongs to **every** maximizing set in each relevant allowed pool. The same table applies to a top-color minimal maximizer when it is origin-containing or degenerate.

#### One-owner deletion and the common-optimum quantifiers

If \(e\) is the single excluded owner in color \(p\), let \(D,D^*\) be the unrestricted and restricted maxima. For any owner set containing \(e\), edge inclusion gives
\[
d(U)\le d(U\setminus\{e\})+1.
\]
Since the restricted pool is contained in the unrestricted pool,
\[
D^*\le D\le D^*+1.
\tag{8}
\]
This direction is important: deletion can raise the deficiency of an individual nonmaximizing set, but that does not harm (8).

If \(D=D^*+1\), every unrestricted maximizer contains \(e\), and deleting \(e\) from **any** of them leaves deficiency exactly \(D^*\). Thus every global optimum already has the required restricted omission in this color.

If \(D=D^*\), choose any restricted maximizer \(V\) and a minimum cover \(W\) of its graph. Then
\(F=(C_p\setminus V)\cup W\) is a global optimum, selects \(e\), and omits precisely \(V\) in color \(p\). By (2), the omissions of this same \(F\) in both other colors are unrestricted maximizers. There is at most one excluded color, so there is no competition between two such choices.

Thus **one** global optimum has all three prescribed omitted restrictions maximizing. One may take an inclusion-minimal maximizing subset of each of these three restrictions. Each such subset remains contained in the omissions of that same \(F\). Its separately chosen minimum graph cover need not be a subset of \(F\); the proof never needs that. The collision only uses the owners in those subsets. This resolves the main potential incompatible-canonical-cover gap.

#### The aggregate collision and one-unit deficit

Let \(\delta_j=I_j+P_j\), \(Q_j=K_j-\delta_j\), \(Q=\min_j Q_j\), and suppose \(t\ge18\), \(\tau<Q\). Then
\(D_j=K_j-\tau>\delta_j\) in every color. Equation (8) gives \(D_j^*>0\) in every allowed pool. Choose the common optimum just constructed.

The two non-top colors omit their required members of \(\{6,12,18\}\) from this same optimum. If a top-color minimal maximizing subset were origin-containing or degenerate, it would force the third member to be omitted too. The existing corner rooted at 6 would then be uncovered. Thus the top restricted maximizer is incomparable, and (7) gives \(D_{q_{\rm top}}^*=1\).

If \(\delta_{q_{\rm top}}=0\), its unrestricted deficiency is 1. If \(\delta_{q_{\rm top}}=1\), the counterexample hypothesis and (8) force its unrestricted deficiency to be 2. In either case
\[
\tau=Q_{q_{\rm top}}-1.
\]
Since \(\tau<Q\le Q_{q_{\rm top}}\) and these quantities are integers,
\[
Q=Q_{q_{\rm top}},\qquad \tau=Q-1.
\tag{9}
\]
This is a valid aggregate reduction. In particular, an exact one-unit patch deletion drop is concluded only where the counterexample hypothesis forces it, not assumed universally.

### Gaps

No aggregate or common-cover gap was found. The proof needs exactly one excluded owner across all colors; it should not be generalized to arbitrary simultaneous exclusions without a new argument. It also needs minimality among maximizers in the full allowed pool, rather than mere criticality, for the prefix augmentations. The current assembly has both hypotheses.

## Do the high-prefix repair, finite comparisons, and base cases finish the universal proof?

### Takeaway

Yes. The strip cap reduces the incomparable case to the stated high family and two smaller cases. The new prefix gives positive gain for every \(s\ge4\). Each surviving finite interval has a strictly losing adjusted top phase, contradicting (9). The small boards are handled directly.

### Cited Findings

- The original high-cap and high-window derivation is V9–V10 in [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>), with its required endpoint details reconstructed in [vertical_audit_and_transfer.md](<../boundary-dominance/vertical_audit_and_transfer.md:107>).
- The new high-prefix argument is H1–H3 in [high_phase.md](<high_phase.md>) and the independent reconstruction in [patch_global.md](<patch_global.md>). The current assembled P4 and finite comparison table are in [prefix_audit.md](<prefix_audit.md:274>).
- The exact intended endpoint checks are readable in [prefix_phase_checks.py](<prefix_phase_checks.py>). I read it but did not execute its file-writing path; the bounded independent check described below made no file changes.

### Inferences

#### The high cap uses only already justified local properties

In the incomparable high case, \(r\in\{1,2\}\), \(z\le2t/3\), and \(y>t/3\). Suppose \(s\ge2\) and \(g^2z>t\). Use horizontal columns \(u_n=xq^n,v_n=gu_n,w_n=g^2u_n,z_n=g^3u_n\). The first selected strip and first owner strip were already forced above.

The same two backward inductions as in the axis-avoiding proof apply. The first cap is \(w_s>t\). For the lower first-strip owners,
\(v_n\le gz/q\le16t/81<t/3\), so their rooted edges exist. The next count forces \(w_1,\ldots,w_{s-1}\). Their rooted edges exist because
\(w_n\le g^2z/q\le64t/243<t/3\). The second cap is the actual leaf \(3w_{s-1}\). The final selected set has \(4s-2\) vertices and at most \(4s-2\) owners. The bottom formal owners \(v_0,z_1\) are nonsmooth, and \(w_s,z_s\) are off-board. Distinct \(g\)-coordinates again verify every cardinality. This contradicts (3), including at \(s=2\).

For \(r=2\), \(z=g^2y>16t/27\), so the cap holds and \(s=1\). Its chain cutoff gives \([216,243)\). For \(r=1\), initially \(z>4t/9\). If \(z\le t/2\), the forced owner \(gz\) has its east edge with its right endpoint excluded by the final horizontal-chain step, forcing \(2z\in W\). The only other possible owners there are \(z\) and \(6z\); the first has no rooted edge because \(z>t/3\), and the second is off-board. This violates essentiality. Hence \(z>t/2\).

At \(s=1\) this gives \([54,72)\). For \(s\ge2\), avoiding the cap also gives \(z\le9t/16\), hence
\[
r=1,\quad s\ge2,\quad
64\cdot9^{s-1}\le t<8\cdot9^s.
\tag{10}
\]
No assertion about numerical windows alone replacing actual maximizers is used.

#### Reconstructing the new prefix and its missing frontier

In the \(r=1\) family, \(A=s+2,B=2s+1\). Put \(k=2a+b,k_0=2A\). The horizontal cone lies in \(k\ge k_0\). In x-based coordinates the vertical cone starts at \((-1,s)\). A point in that cone below \(k_0\) must have g-coordinate \(-1\), and then ordinary first exponent \(s-n\), with \(n\ge s\). Nonnegativity forces \(n=s\), giving precisely \(y\). Thus
\[
U\cap\{k<k_0\}=\{y\}.
\]

Let \(P_0\) be every preferred-color point on diagonals \(k_0-3,k_0-6,\ldots\ge0\), let \(P=P_0\setminus\{y\}\), and let \(L\) consist of the left-color points on \(k_0-4,k_0-7,\ldots\ge0\). Then \(P\cap U=\varnothing\).

Every new north/east left endpoint lies one diagonal below its owner and is in \(L\). A new rooted left endpoint lies two diagonals above its owner. Except on the highest owner diagonal, it is also in \(L\). On that highest diagonal it lies on the frontier \(k_0-1=2s+3\).

The forced vertices \(3u_n/2\), \(0\le n<s\), are exactly its points with first exponent \(a=2,\ldots,s+1\). The two missing frontier points are \(2y\), with \(a=1\), and \(9y\), with \(a=0\). The latter is off-board because \(t<3y\). A newly added owner on the highest prefix diagonal cannot need \(2y\) as its rooted left endpoint: the only such owner would be \(y\), which was removed from \(P\). All other new owners have \(a\ge1\), hence rooted-left exponent \(a+1\ge2\). Equivalently, the complete possible owner list at \(2y\) is \(\{y,4y/3,6y\}\), and none is a newly added owner. Every old edge, including an edge of \(y\), retains its old cover. Therefore \(W\cup L\) covers all of \(B(U\cup P)\).

All new points are on-board: the largest label on \(2a+b=k\) is \(3^k\), and the highest owner diagonal has maximum \(y\le t\). After removing \(y\), its maximum is \(2y/9=z/6\le t/9\); lower owner diagonals are smaller. Thus no exceptional root, which exceeds \(4t/27\), can be added. The repair points are at most \(y/3\le t/3\).

Pairing the full owner and repair diagonals gives
\[
|P_0|-|L|=\lfloor A/3\rfloor,
\qquad |P|-|L|=\lfloor(s-1)/3\rfloor.
\]
Hence
\[
d(U\cup P)\ge D_j^*+\lfloor(s-1)/3\rfloor.
\tag{11}
\]
For every \(s\ge4\), this contradicts maximality in the original allowed pool. This is an unbounded algebraic argument; it does not infer the general claim from a finite list of examples.

As a targeted attempt to break the missing-frontier assertion, I checked its first excluded case \(s=4,t=46656\). Here \(y=19683\), so \(2y=39366\) is on-board and was deliberately absent from the repairing set. Enumerating just the specified new prefix and its owned edges showed that every available new edge had its left endpoint in the prescribed repair or forced frontier; the new-owner/repair count difference was exactly 1. The check also asserted that every added owner was below \(4t/27\). This found no counterexample. It is only a bounded consistency check of (11), whose proof is the preceding diagonal argument.

#### The exact finite contradiction

The remaining incomparable cases and their adjusted phase counts are:

| Parameters | Interval | \(K\) | \(I\) | \(P\) | Top color | \(K-I-P\) |
|---|---|---|---|---|---:|---|
| \(r=s=1\) | \([54,64)\) | \((6,5,5)\) | \((0,0,0)\) | \((0,0,0)\) | 0 | \((6,5,5)\) |
| \(r=s=1\) | \([64,72)\) | \((7,5,5)\) | \((1,0,0)\) | \((0,0,0)\) | 0 | \((6,5,5)\) |
| \(r=2,s=1\) | \([216,243)\) | \((9,8,9)\) | \((0,0,0)\) | \((0,0,0)\) | 2 | \((9,8,9)\) |
| \(r=1,s=2\) | \([576,648)\) | \((12,12,11)\) | \((1,0,0)\) | \((0,0,0)\) | 1 | \((11,12,11)\) |
| \(r=1,s=3\) | \([5184,5832)\) | \((20,19,20)\) | \((1,0,0)\) | \((0,0,0)\) | 2 | \((19,19,20)\) |

I independently verified all five rows with exact board generation and integer comparisons, including that no smooth birth, isolate cutoff, patch activation, or patch deactivation lies in an interval's interior. The top vertical color was checked separately from the count vector. The comparisons show \(Q_{q_{\rm top}}>\min_j Q_j\) in every row, contradicting (9). The intervals are correctly half-open: a patch ending at 54 or 216 is already inactive at that endpoint; an upper-cap equality \(g^2z=t\) remains included where used.

The finite checker in this audit ran in JavaScript with safe integer board values and asserted all endpoint integrality, distinct board labels, prescribed gains, and coverage properties. An initial attempt to use `python` failed because the local WindowsApps alias could not be started; no result is attributed to that failed invocation. The successful independent check printed: `PASS: first excluded high-prefix geometry (s=4) and all five surviving phase intervals; no files changed.`

#### Small boards and closure of the universal quantifiers

For \(3\le t<9\), \(\{2\}\) hits every existing corner and the corner at 1 requires a nonempty cover, so \(\tau=1\). Direct counts give \(Q=1\) on \([3,4),[4,6),[6,8),[8,9)\), with the isolate active on the second and fourth intervals.

For \(9\le t<18\), \(\{3,4\}\) hits every corner; the possible roots are among \(1,2,3,4\). The three existing corners rooted at \(1,2,3\) have empty common intersection, so \(\tau=2\). Direct counts give \(Q=2\) on \([9,12),[12,27/2),[27/2,16),[16,18)\). The nonsmooth endpoint \(27/2\) terminates the small construction indicator and is correctly retained even though the board does not change there.

For \(t\ge18\), a hypothetical strict failure produces the common optimum and top incomparable restricted maximizer by the aggregate argument. The cap reduction leaves only (10) and the two smaller cases. Equation (11) excludes every unbounded parameter \(s\ge4\). The finite table excludes all surviving cases. Thus no strict failure exists. Combined with the explicit construction upper bound and the small-board argument, this proves (C) for every real \(t\ge3\).

### Gaps and final scope

No fatal gap was found in the complete finite-formula chain. The substantive qualifications to preserve in any polished proof are: the deleted owner is unique globally; strict expansion counts all incident owners; new-prefix gains require maximality over the entire allowed pool; separately chosen graph covers are not identified with pieces of the common optimum; the small vertical patch is not an axis-avoiding critical set; and the mandatory-18 implication imposes its own stronger edge-availability cutoff when that configuration exists. Each qualification is satisfied by the current assembled proof.

Skipped: no Lean work, broad sweep, older-file modification, external-status check, or irrationality/novelty assessment. The remaining limitation is that this is a written mathematical audit, not machine verification; no additional finite-combinatorial lemma remains open in the reviewed chain.
