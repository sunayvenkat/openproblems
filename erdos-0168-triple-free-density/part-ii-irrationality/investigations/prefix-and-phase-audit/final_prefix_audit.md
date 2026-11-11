# Final fresh-context audit of the Erdős 168 finite formula

7 November 2026. **Verdict: PASS for the finite formula (C).** I independently reconstructed the geometric reductions, decisive high-prefix exchange, one-exclusion compatibility and same-optimum collision, and checked the specified real endpoint intervals by a separate exact integer certificate. I found no missing case or invalid inference in the assembled proof in [prefix_audit.md](<prefix_audit.md>). This verdict concerns finite corner-cover optimality only; it does not establish irrationality, historical novelty, external review or formal verification.

## Do the geometric and boundary reductions hold for arbitrary restricted maximizers?

### Takeaway

Yes. Inclusion-minimal maximum deficiency supplies the exact essentiality and strict expansion used by every subsequent strip argument. The axis classification, predecessor cones, root balance, degenerate prefixes, vertical dichotomy and deep-branch contradiction work with the stated cutoff and axis qualifications.

### Cited Findings

- The owned-edge definitions, axis-avoiding classification, three-strip proof and extension from critical subsets to all axis-avoiding subsets are in [multiroot.md](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>).
- The two-cone, root-balance, forced-chain and high-case claims being audited are in [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>).
- The independent deep-strip argument is in [deep_branch.md](<../boundary-dominance/deep_branch.md>).
- The restricted pool, aggregate-maximizer version and degenerate prefix repairs are in [canonical_audit_and_collision.md](<../boundary-dominance/canonical_audit_and_collision.md>); their consolidated reconstruction, including a simpler root-balance proof, is in [prefix_audit.md](<prefix_audit.md>).

### Inferences

The following is my reconstruction, rather than reliance on numerical success or the earlier notes' audit labels.

#### Incidence and canonical quantifiers

Fix owner color \(j=a-b\pmod3\), with left and right colors \(j+1,j+2\). The complete opposite edges of an owner \(u=2^a3^b\) are
\[
 N(u)=(u/3,2u/3),\quad
 E(u)=(3u/2,u/2),\quad
 R(u)=(2u,3u),
\]
available respectively when \(b\ge1\), when \(a\ge1\) and \(3u/2\le t\), and when \(3u\le t\). All cutoff inequalities are non-strict availability inequalities. At a left vertex \(l\), the possible owners are \(l/2,2l/3,3l\); at a right vertex \(v\), they are \(v/3,3v/2,2v\). These lists follow by solving each of the three displayed endpoint formulas. They include double coverage; smoothness, membership and edge availability must still be imposed.

Let \(U\) be inclusion-minimal among sets attaining a positive maximum \(D^*\) over its allowed pool, and let \(W\) be a minimum graph cover. Then \(|W|=|U|-D^*\). If \(w\in W\) uniquely covers edges of only one owner \(u\), deleting \(w,u\) leaves a smaller set of deficiency at least \(D^*\). This contradicts maximality or inclusion-minimality. A vertex uniquely covering none is redundant. Thus every selected vertex uniquely supports at least two owners.

For any nonempty \(S\subset W\), delete the owners \(T\) of all edges incident with \(S\). The remaining graph is covered by \(W\setminus S\), so
\[
 d(U\setminus T)\ge D^*+|S|-|T|.
\]
Consequently \(|T|\ge |S|+1\). When \(T=U\), the same result follows directly from \(|U|=|W|+D^*>|S|\). Every deletion stays in the allowed pool. No assumption that \(D^*=1\) has entered.

#### Axis-avoiding input, checked at its delicate boundaries

For an inclusion-minimal positive axis-avoiding set, criticality gives deficiency one. An interior owner lacking all three predecessors \(u/6,2u/9,3u/4\) leads to a contradiction as follows. Its north-left vertex is a leaf. The selected north-right vertex must therefore uniquely support \(E(4u/3)\), excluding \(2u\) from \(W\) and placing \(2u\) on the board. This makes \(E(u)\) available because \(a(u)\ge1\). Its east-right vertex is then a leaf. The selected east-left vertex forces \(N(9u/2)\) uniquely, excluding \(3u\) from \(W\). Since \(9u/2\le t\), \(R(u)\) exists with neither endpoint selected. This proves the predecessor lemma without applying it to a vertical owner.

For an axis-avoiding critical set, decreasing predecessors end on the horizontal axis. With least root \(x=2^A\), all owners lie in \(xg^mq^n\), \(m,n\ge0\), where \(g=4/3,q=9/2\). The forced boundary ray \(u_n=xq^n\) reaches a numeric terminal \(u_k\) with \(2t/3<u_k\le t\); it cannot terminate by reaching \(a=0\) inside an axis-avoiding set.

Here is the complete strip accounting. The \(2k\) selected vertices \(3u_n/2,2u_n\), \(0\le n<k\), have at most \(2k+1\) owners, forcing \(gu_1,\ldots,gu_k\). In particular \(u_k\le3t/4\), while \(g^2u_k>t\). With \(\beta_n=2gu_n/3\), the north edge is already covered at its left endpoint. A selected \(\beta_n\) requires both remaining owners uniquely, including \(g^2u_n\), and excludes \(2gu_n\). At the cap this is impossible; available rooted edges propagate any smaller selected \(\beta_n\) to the next one. Backward induction therefore selects \(2gu_n\), \(1\le n<k\). There are now \(3k-1\) selected vertices and at most \(3k\) owners, forcing \(g^2u_1,\ldots,g^2u_{k-1}\).

Their rooted edges exist: \(g^2u_{k-1}\le8t/27<t/3\). The cap \(3g^2u_{k-1}=2g^2u_k/3\) is a leaf, since its other owners \(g^2u_k,g^3u_k\) are off-board. A second backward induction selects \(2g^2u_n\), \(1\le n<k\). For \(n=1\), this uses only its rooted edge; it does not require a north edge at the horizontal root \(g^2u_1=8x\). The \(4k-2\) selected vertices then have at most
\[
 (k+1)+k+(k-1)+(k-2)=4k-2
\]
owners: the formal bottom owners \(gx,g^3u_1\) are nonsmooth, and the top \(g^2u_k,g^3u_k\) are off-board. This contradicts strict expansion for \(k\ge2\), including \(k=2\), where the last range is empty. Distinctness follows by dividing all selected left vertices by \(2x\): their \(g\)-coordinates are \(-1,0,1,2\), and \(g,q\) are independent.

Thus an axis-avoiding critical set is a singleton isolated root or the patch \(\{x,9x/2,6x\}\), \(6x\le t<27x/4\), with \(A\ge2\) in this axis-avoiding case. The small \(A=1\) patch touches the vertical axis and is not an exception to this classification. Every positive finite axis-avoiding set contains a critical subset, so excluding the unique exceptional dyadic root removes all positive axis-avoiding sets.

#### Two cones and root balance

The north edges are pairwise vertex-disjoint, so positive deficiency forces a horizontal owner. The preceding allowed-pool axis result forces a vertical owner. If the origin is present, retain that case separately. Otherwise take least roots \(x=2^A,y=3^B\), \(A,B\ge1\). Interior predecessors decrease numerical value and terminate on an axis. Other same-color horizontal roots differ by \(8=g^2q\); vertical roots differ by \(27=gq^2\). Therefore
\[
 U\subset x\langle g,q\rangle_{\ge0}\cup y\langle g,q\rangle_{\ge0}.
\]
The coordinates of \(y\) based at \(x\) are \(((B-2A)/3,(2B-A)/3)\); integrality follows from the same color condition.

If \(A>2B\), the horizontal cone lies in the vertical cone. The chain \(yg^m\), \(0\le m<B\), has leaf north-left endpoints: both alternative owners have negative \(q\)-coordinate. Essentiality forces the chain to the smaller horizontal root \(2^{2B}<x\). This is impossible.

If \(B>2A\), the vertical cone lies in the horizontal cone. The intended endpoint \(y'=3^{2A}<y\le t\) is already on the board. Every preterminal \(xq^n\), \(n<A\), has positive first exponent and is at most \(y'/q\le2t/9\), so its east edge exists. The east-right alternatives have negative \(g\)-coordinate. Essentiality forces the entire chain to the smaller vertical root \(y'\), again impossible. This avoids reliance on a separate numerical-terminal claim.

Thus
\[
 A/2\le B\le2A,\quad
 r=(2A-B)/3,\ s=(2B-A)/3\ge0,
\quad A=2r+s,\ B=r+2s.
\]
The origin and the two equality cases remain distinct from incomparable \(r,s\ge1\).

#### Both degenerate prefixes

For \(s=0\), \(A=2B\), use \(k=a+2b,k_0=2B\). The vertical cone is exactly the preferred-color part of \(k\ge k_0\) in the nonnegative quadrant. Its \(q\)-coordinate is \((k-2B)/3\); nonnegativity also makes the other coordinate nonnegative. The vertical chain selects every right vertex on \(k=k_0-1\), and its last forced east edge gives \(x\le2t/3\).

Add preferred diagonals \(k_0-3,k_0-6,\ldots\) and right-cover diagonals \(k_0-4,k_0-7,\ldots\). New north/east right endpoints have diagonal \(k-1\), and rooted right endpoints have \(k+2\). They therefore meet the added cover or the selected frontier. All new owners are at most \(2^{k_0-3}=x/8\le t/12\), and all new cover points are on-board. The owners are disjoint from \(U\).

For \(r=0\), use \(k=2a+b,k_0=2A\). The horizontal cone is exactly the preferred-color part of \(k\ge k_0\). The horizontal chain selects every left vertex on \(k_0-1\); each preterminal label is at most \(y/q\le2t/9\), so no east or rooted edge used is missing. Add the same-spaced owner diagonals and left-cover diagonals. North/east left endpoints have diagonal \(k-1\), rooted left endpoints \(k+2\). Added owners are at most \(3^{k_0-3}=y/27\le t/27\).

For either diagonal convention, the full diagonal has \(h(k)=\lfloor k/2\rfloor+1\) points, \(h(-1)=0\). Pairing each preferred diagonal \(k_0-3n\) with the cover diagonal immediately below gives difference one exactly for even \(n\). The gains are \(\lfloor B/3\rfloor\) and \(\lfloor A/3\rfloor\). Maximum deficiency therefore gives \(B\le2\) and \(A\le2\), respectively. Exceptional roots exceed \(4t/27\), so neither prefix introduces the forbidden owner. Possible overlap with \(W\) only reduces repair cost.

#### Incomparable chains, vertical dichotomy and deep exclusion

For \(r,s\ge1\), set \(u_n=xq^n\), \(v_m=yg^m\), \(z=u_s=v_r\). North-left alternatives along \(v_m\), \(m<r\), have coordinates outside both cones. They force \(2v_m/3\in W\), \(2v_m\notin W\), and the next east owner. The last edge gives \(z\le2t/3\). East-right alternatives along \(u_n\), \(n<s\), also lie outside both cones. They force \(3u_n/2\in W\), \(3u_n\notin W\), and the next north owner. Since \(u_n\le z/q\le4t/27<t/3\), rooted edges select \(2u_n\). Strict expansion of these \(2s\) left vertices forces \(gu_1,\ldots,gu_s\).

If vertical rooted edges exist exactly through index \(h<r\), the \(r\) selected north-right vertices and the \(h+1\) rooted-right vertices have at most \(r+h+2\) owners. Expansion forces \(qv_{h+1}=6v_h\in U\), hence \(v_h\le t/6\). If \(h<r-1\), then \(v_{h+1}\le2t/9<t/3\), contradicting the last-rooted index. Thus \(h=r-1\) and \(qz\in U,z\le2t/9\). If no rooted edge exists, \(y>t/3\); combined with \(g^ry=z\le2t/3\), this gives \(g^r<2\), so \(r=1\) or \(2\).

In the deep alternative \(z\le2t/9\), the horizontal selected strip has owner coordinates
\[
 H=\{(0,n):0\le n\le s\}\cup\{(1,n):1\le n\le s\},
\]
and the vertical selected strip has
\[
 V=\{(m,s):-r\le m\le0\}\cup\{(m,s+1):1-r\le m\le0\}.
\]
Their only overlap is \(z=(0,s)\). They comprise \(2r+2s\) selected vertices, in different bipartition colors, with \(2r+2s+1\) possible owners. The forced \(gz\) has an available east edge, with excluded right endpoint \(2z/3\), forcing \(2z\in W\). The forced \(qz\) has a north edge with excluded left endpoint \(3z/2\), forcing \(3z\in W\). These two vertices are distinct from the old selected ranges. Their owner lists are \(\{z,gz,6z\}\) and \(\{z,qz,6z\}\), so they add at most one possible owner. Strict expansion fails. This excludes the deep branch without assuming \(6z\in U\), cone closure or component independence.

Consequently an incomparable restricted maximizer has \(y>t/3\). This \(y\) is the highest power of three on the whole board. It is also its only vertical owner, since the next same-color one is \(27y>t\). Deleting \(y\) leaves an allowed axis-avoiding set of nonpositive deficiency. The single-owner deletion inequality gives \(0<D^*\le1\). Now, and only now, the inclusion-minimal maximizer becomes a critical set.

### Gaps

None found in the audited geometric reductions. The old long numerical-terminal root-balance discussion is unnecessary; the shorter on-board chain in the current assembly is sufficient. Criticality alone is not used where maximum deficiency is required.

## Does the high-prefix repair eliminate every unbounded high parameter?

### Takeaway

Yes. The three-strip cap leaves the stated \(r=2,s=1\) and \(r=1\) windows. In the latter family, the added triangular prefix needs no missing frontier vertex: the only corresponding lower owner is the already present \(y\). Its exact gain is \(\lfloor(s-1)/3\rfloor\), excluding all \(s\ge4\) by maximality.

### Cited Findings

- The proposed high-prefix repair and finite windows are in [high_phase.md](<high_phase.md>).
- The alternate incidence reconstruction is in [patch_global.md](<patch_global.md>).
- The consolidated high cap and repair P4 are in [prefix_audit.md](<prefix_audit.md>).

### Inferences

#### High cap and exact surviving windows

Suppose \(s\ge2\) and \(g^2z>t\). The same three-column argument reconstructed above applies with chain length \(s\). Its required inequalities follow already from \(z\le2t/3\):
\[
 gu_n\le gz/q\le16t/81<t/3,\qquad
 g^2u_n\le g^2z/q\le64t/243<t/3 \quad(n<s).
\]
The north-left endpoints in the second column are already selected first-column rooted-left endpoints. A selected second-column north-right endpoint requires the capped owner uniquely and propagates forward through its rooted edge; backward induction excludes every such endpoint. The ensuing strict owner count forces the third column. Its terminal rooted-right vertex is a leaf, because both possible cap owners are off-board. A second backward induction supplies the final selected third-column left vertices. The final \(4s-2\) versus \(4s-2\) count contradicts expansion. The formal bottom owners \(gx,g^3xq\) have negative 3-exponent; \(g^2z,g^3z\) are off-board. At \(s=2\) the final extra-owner range is empty, as it must be.

For \(r=2\), \(z=g^2y>16t/27\), so \(g^2z>256t/243>t\). Hence \(s=1\), giving \(x=32,y=81,z=144\) and \(216\le t<243\).

For \(r=1\), initially \(z=gy>4t/9\). If \(z\le t/2\), the forced owner \(gz\) has an available east edge with excluded right endpoint \(2z/3\), forcing \(2z\in W\). The only other possible owners there are \(z\) through an unavailable rooted edge, and \(6z>t\). This violates essentiality. Thus \(z>t/2\). At \(s=1\), this gives \(54\le t<72\). At \(s\ge2\), the cap contradiction requires \(g^2z\le t\), hence
\[
64\cdot9^{s-1}\le t<8\cdot9^s.
\]
Equality at the lower cap is included; equality at the upper essentiality boundary is excluded. Degenerate \(s=0\) configurations were already treated separately and are not lost here.

#### Cone truncation and the missing frontier

Put \(A=s+2\), \(k=2a+b\), \(k_0=2A\). For \(u=xg^mq^n\),
\[
 a=A+2m-n,\quad b=2n-m,\quad k=k_0+3m.
\]
The horizontal cone is exactly the preferred-color part of \(k\ge k_0\); \(m\ge0\) implies \(n\ge0\) in the nonnegative ordinary quadrant. The vertical cone begins at \((-1,s)\). Below \(k_0\), its integer first coordinate can only be \(-1\), where \(a=s-n\) and \(n\ge s\), so only \(n=s\) survives. Thus \(U\cap\{k<k_0\}=\{y\}\).

Let \(P_0\) contain full preferred diagonals \(k_0-3,k_0-6,\ldots\ge0\), add \(P=P_0\setminus\{y\}\), and add left-cover diagonals \(k_0-4,k_0-7,\ldots\ge0\), denoted \(L\). The sets \(P,U\) are disjoint.

The chain-selected frontier vertices \(3u_n/2\), \(0\le n<s\), have first exponents \(s+1,s,\ldots,2\). These are exactly all frontier \(k_0-1=2s+3\) points with \(a\ge2\). The other formal frontier points are \(2y\), \(a=1\), and \(9y\), \(a=0\). The latter is off-board because \(t<3y\). Every new north/east edge has left endpoint on an \(L\) diagonal. A lower-prefix rooted edge does too. A top-prefix rooted edge has frontier first exponent at least two, because its only possible top owner with \(a=0\) is \(y\), which was not added.

Equivalently, the complete possible owners at \(2y\) are \(y\) via \(R\), \(4y/3=z\) via \(E\), and \(6y\) via \(N\). The latter two are on diagonal \(k_0\), outside the added prefix; \(6y>t\). The owner \(y\) was already present and its rooted edge is unavailable since \(3y>t\). Therefore no new edge requires \(2y\). All old edges remain covered by \(W\). This proves that \(W\cup L\) covers the enlarged graph without deleting or exchanging any selected vertex.

#### Board cutoff, forbidden root and exact gain

On \(2a+b=k\), the largest label is \(3^k\). The entire top preferred diagonal is on-board since its maximum is \(y\le t\); all lower diagonals and cover diagonals are also on-board. More sharply, after deleting \(y\), the largest added top-diagonal owner is \(2y/9=z/6\le t/9\); lower owner diagonals have maxima at most \(y/27\). Added cover points are at most \(y/3=z/4\le t/6\). Every exceptional root exceeds \(4t/27>t/9\), so no forbidden owner is introduced, including during an active patch. Alternatively, new dyadic owners are bounded by \(x/8\le t/8<4t/27\).

The full diagonal count is \(h(k)=\lfloor k/2\rfloor+1\), \(h(-1)=0\). Pairing each owner diagonal \(k_0-3n\), \(n\ge1\), with the cover diagonal immediately below gives difference one exactly when \(n\) is even. Hence
\[
 |P_0|-|L|=\lfloor A/3\rfloor,\qquad
 |P|-|L|=\lfloor A/3\rfloor-1=\lfloor(s-1)/3\rfloor.
\]
Possible overlap between \(W,L\) only helps. Therefore
\[
 d(U\cup P)\ge D^*+\lfloor(s-1)/3\rfloor.
\]
This contradicts maximum deficiency for all \(s\ge4\). The proof does not claim that criticality alone forbids those parameters; that stronger statement would be unjustified. The allowed-pool maximizer obtained in the global argument retains the required maximality.

### Gaps

None found. The potentially fatal missing-frontier objection does not apply: \(y\) is the only new-prefix candidate requiring \(2y\), and it is an old owner. No numerical extrapolation, equality-preserving exchange, unrestricted filling or forward closure is used.

## Do compatibility, collision and exact real endpoint checks establish (C)?

### Takeaway

Yes. One excluded owner permits a single optimum with all three restricted omissions maximizing at once. A hypothetical counterexample forces the top adjusted phase to minimize, while every surviving high window has a strictly larger top coordinate. Exact base covers finish all \(3\le t<18\), including the real threshold \(27/2\).

### Cited Findings

- The one-exclusion compatibility lemma and aggregate collision are in [patch_global.md](<patch_global.md>).
- The full construction, consolidated common-optimum argument and final formula are in [prefix_audit.md](<prefix_audit.md>).
- I read [prefix_phase_checks.py](<prefix_phase_checks.py>) and [high_phase_check.py](<high_phase_check.py>) before checking the finite data. I did not rerun their already-replayed sweeps. The new bounded certificate below uses a different row-width residue count and exact BigInt quarter-units.

### Inferences

#### Construction and one-owner compatibility

A dyadic \(e>2t/3\) owns no corner and can be deleted from its phase. For \(6e\le t<27e/4\), the three same-color owners \(e,9e/2,6e\) have just the four opposite edges covered by \(\{3e/2,2e\}\), giving a saving of one. At \(e=2\), the vertical owner's east edge is absent, which does not invalidate this sufficient construction. Root \(e=1\) is not permitted: \(9/2\) is not a board point.

Each defining dyadic interval has ratio less than two. An active patch gives \(6e\le t<27e/4<8e\), so the largest dyadic board point is \(4e\le2t/3\); an isolate cannot coexist. Hence at most one owner is excluded across all colors. Write \(\delta_j=I_j+P_j\), \(Q_j=K_j-\delta_j\), \(Q=\min_jQ_j\). The construction proves \(\tau\le Q\).

Matching-cover correspondence gives \(D_j=\max d(U)=K_j-\tau\). For the exceptional color, let \(D^*\) exclude \(e\). Edge inclusion gives
\[
 d(U)\le d(U\setminus\{e\})+1,\qquad D^*\le D\le D^*+1.
\]
If \(D=D^*+1\), every unrestricted maximizer contains \(e\), and its deletion has deficiency exactly \(D^*\). Thus any optimum supplies the required restricted omission. If \(D=D^*\), build an optimum from a restricted maximizing set and a minimum cover of its graph; this optimum contains \(e\) and omits exactly that restricted maximizer in the exceptional color. In every other color the same optimum's omitted set automatically maximizes unrestricted deficiency. The empty set is permitted throughout. This proves the common-optimum quantifiers without requiring simultaneous canonical tie-breakers.

#### Mandatory omissions and collision

Assume \(t\ge18\) and \(\tau<Q\). Then \(D_j>\delta_j\), and the deletion bound gives \(D_j^*>0\) in all three pools. Within the same optimum's restricted omissions choose inclusion-minimal maximizing subsets. The preceding geometric classification places every incomparable subset in the top vertical color.

For origin/degenerate cases the mandatory owners are \(6,12,18\) in colors \(0,1,2\). Here are the local checks. In the origin case, \(R(1)\) selects one of \(2,3\); selecting both leaves either with at most one uniquely supported owner. Whichever is selected requires owner \(6\). In color one, the remaining degenerate roots are \(r=0,A=1\), whose first horizontal selected strip forces \(12\), or \(s=0,B=2\), whose vertical chain includes \(12\). In color two, \(r=0,A=2\) forces \(18\) along the horizontal chain. For \(s=0,B=1\), the vertical chain \(3,4\) selects \(2\) and excludes \(6\). Since \(t\ge18\), \(R(3)\) exists and forces \(9\). The selected pair \(\{2,9\}\) has at most the owners \(\{3,4,18\}\), so expansion forces \(18\). Any stronger edge cutoff can rule out a configuration but cannot remove its mandatory-owner conclusion.

These owners belong to every maximizing omitted set in the relevant pool, because every maximizer contains an inclusion-minimal one. None is dyadic, so none is the excluded owner. If the top color were also origin/degenerate, the same optimum would omit the entire existing corner \(\{6,12,18\}\), impossible. It therefore has an incomparable restricted maximizer, whose deficiency is one as proved above.

Thus \(D_{\rm top}^*=1\). The counterexample hypothesis and deletion bound imply \(D_{\rm top}=\delta_{\rm top}+1\), and hence
\[
 \tau=Q_{\rm top}-1.
\]
Since \(\tau<Q\le Q_{\rm top}\) and all counts are integers, \(Q=Q_{\rm top}\). This is precisely the minimizing-top conclusion contradicted by the remaining windows. No independent-component or critical-subset additivity is involved.

#### Independent exact finite certificate and its output

For each fixed row \(b\), let \(w_b\) be its width. A width \(w_b=3q+r\) contributes \(q\) vertices of each color, plus colors \(-b,1-b,\ldots,r-1-b\). The independent check below counts only these row widths. For each row, it verifies that the first excluded smooth label is at least the upper endpoint; it verifies the next vertical row similarly. It separately excludes every interior correction transition \(e,3e/2,6e,27e/4\) for dyadic roots. All arithmetic uses integer quarter-units. No finite optimum, owner subset, matching solver or unbounded parameter sweep is computed.

| Interval | Row widths at left endpoint | Adjusted vector | Top color if high |
|---|---|---|---:|
| [3,4) | 2,1 | (1,1,1) | — |
| [4,6) | 3,1 | (1,1,1) | — |
| [6,8) | 3,2 | (2,1,2) | — |
| [8,9) | 4,2 | (2,1,2) | — |
| [9,12) | 4,2,1 | (2,2,2) | — |
| [12,27/2) | 4,3,1 | (3,2,2) | — |
| [27/2,16) | 4,3,1 | (3,3,2) | — |
| [16,18) | 5,3,1 | (3,3,2) | — |
| [54,64) | 6,5,3,2 | (6,5,5) | 0 |
| [64,72) | 7,5,3,2 | (6,5,5) | 0 |
| [216,243) | 8,7,5,4,2 | (9,8,9) | 2 |
| [576,648) | 10,8,7,5,3,2 | (11,12,11) | 1 |
| [5184,5832) | 13,11,10,8,7,5,3,2 | (19,19,20) | 2 |

Every high top coordinate is strictly larger than the minimum. At 54 and 216, the previous patch is already inactive because its upper inequality is strict. At 576 and 5184 the isolated roots are 512 and 4096, color zero. The cap equalities at these left endpoints are retained. The last high endpoints 648 and 5832 are excluded by the strict upper essentiality inequality. These intervals exhaust the surviving incomparable parameters; \(s\ge4\) was excluded symbolically.

The following exact JavaScript was run in functions.exec and returned PASS. Endpoint pairs are \(4\) times the actual endpoints. It is saved here instead of creating any additional script or output file.

~~~javascript
const cases=[
 [12n,16n,[1,1,1],[0,0,0],[0,0,0],null],
 [16n,24n,[1,1,2],[0,0,1],[0,0,0],null],
 [24n,32n,[2,1,2],[0,0,0],[0,0,0],null],
 [32n,36n,[3,1,2],[1,0,0],[0,0,0],null],
 [36n,48n,[3,2,2],[1,0,0],[0,0,0],null],
 [48n,54n,[3,3,2],[0,0,0],[0,1,0],null],
 [54n,64n,[3,3,2],[0,0,0],[0,0,0],null],
 [64n,72n,[3,4,2],[0,1,0],[0,0,0],null],
 [216n,256n,[6,5,5],[0,0,0],[0,0,0],0],
 [256n,288n,[7,5,5],[1,0,0],[0,0,0],0],
 [864n,972n,[9,8,9],[0,0,0],[0,0,0],2],
 [2304n,2592n,[12,12,11],[1,0,0],[0,0,0],1],
 [20736n,23328n,[20,19,20],[1,0,0],[0,0,0],2]
];
const ok=(p,msg)=>{if(!p)throw Error(msg);};
const eq=(a,b)=>a.every((x,i)=>x===b[i]);
for(const [L,H,wanted,iso,patch,top] of cases){
 let widths=[],K=[0,0,0],b=0,p3=1n;
 while(4n*p3<=L){
  let u=p3,width=0;
  while(4n*u<=L){u*=2n;width++;}
  ok(4n*u>=H,"interior smooth event");
  widths.push(width);
  let q=Math.floor(width/3),r=width%3;
  K=K.map(x=>x+q);
  for(let a=0;a<r;a++)K[((a-b)%3+3)%3]++;
  p3*=3n;b++;
 }
 ok(4n*p3>=H,"interior vertical event");
 ok(eq(K,wanted),"counts");
 let I=[0,0,0],P=[0,0,0],e=2n,a=1;
 while(4n*e<=H){
  for(const event of [4n*e,6n*e,24n*e,27n*e])
   ok(!(L<event&&event<H),"interior correction event");
  if(4n*e<=L&&2n*L<12n*e)I[a%3]++;
  if(24n*e<=L&&L<27n*e)P[a%3]++;
  e*=2n;a++;
 }
 ok(eq(I,iso)&&eq(P,patch),"corrections");
 let Q=K.map((v,j)=>v-I[j]-P[j]);
 if(top!==null)
  ok((((1-b)%3)+3)%3===top&&Q[top]>Math.min(...Q),"top comparison");
 else
  ok(Math.min(...Q)===(L<36n?1:2),"base adjusted count");
}
text("PASS: 13 prescribed subintervals; exact boundaries and all interior events.");
~~~

#### Base covers and final implication

For \(3\le t<9\), the possible corner roots are \(1,2\), so \(\{2\}\) meets every corner. The corner rooted at one exists, giving lower bound one. For \(9\le t<18\), possible corner roots are \(1,2,3,4\), whose corners are all met by \(\{3,4\}\). The corners rooted at \(1,2,3\), namely \(\{1,2,3\},\{2,4,6\},\{3,6,9\}\), have empty common intersection, so one point cannot suffice. Thus the exact optima are one and two, respectively, matching the table.

At \(27/2\) the small patch indicator turns off although the smooth board stays unchanged; the adjusted minimum remains two. Its actual vertical patch remains critical up to 18, which is harmless because the base argument is explicit. No argument silently equates its true critical interval with its sufficient construction interval.

The construction gives \(\tau\le Q\). For \(t\ge18\), a strict failure forces a top-minimizing incomparable restricted maximizer; the high-prefix and exact remaining comparisons rule that out. The base covers prove equality below 18. Therefore the audited finite conclusion is
\[
 \boxed{\tau(D_t)=\min_{j\in\mathbb Z/3\mathbb Z}
 \bigl(K_j(t)-I_j(t)-P_j(t)\bigr)\qquad\text{for every real }t\ge3.}
\]

### Gaps

No mathematical gap found in (C)'s dependency chain or real endpoint treatment. This is an independent mathematical audit with bounded arithmetic checks, not a formal machine proof. The default Python alias was inaccessible; the new certificate instead ran successfully using exact BigInt arithmetic in functions.exec. No broad sweep, new dependency, archived-note edit, subagent delegation, Lean work, external submission or irrationality calculation was performed. The separate irrationality and novelty questions remain unproved by this audit.

