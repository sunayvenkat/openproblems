# Prefix repairs settle Erdős’s finite optimum

**The global finite formula (C) holds for every real \(t\ge3\): the vertical-axis case is resolved.** The proof controls maximum deficiency over whole allowed owner pools, then uses one exceptional-owner exclusion to put the three relevant omitted sets inside one global optimum. A hypothetical failure would be exactly one below the proposed value and would force the top vertical color to minimize its adjusted phase count. Explicit prefix augmentations eliminate the unbounded geometric family; every surviving finite window contradicts that minimizing condition. Both final fresh-context mathematical audits report **PASS** after reconstructing the dependency chain, including the missing-frontier and common-optimum issues. This supersedes the earlier report’s statement that the global finite optimum remained unproved. The result is a complete ordinary finite proof with internal adversarial audits and exact bounded certificates; it establishes neither Erdős #168(ii)’s irrationality assertion nor formal verification, external review, or historical priority. ([Complete assembly](<prefix_audit.md>), [final global audit](<final_global_audit.md>), [final prefix audit](<final_prefix_audit.md>))

## One exceptional owner makes the proposed optimum explicit

Let
\[
D_t=\{2^a3^b\le t:a,b\in\mathbb Z_{\ge0}\},\qquad
C_j=\{2^a3^b\in D_t:a-b\equiv j\pmod3\},\qquad K_j=|C_j|.
\]
A corner is \(\{u,2u,3u\}\subset D_t\). A cover meets every corner, and \(\tau(t)=\tau(D_t)\) is its minimum cardinality. Each corner has one point of each color, so each \(C_j\) is a cover.

For \(e=2^A\), \(A\ge1\), let \(I_j(t)\) indicate an isolated root of color \(j=A\bmod3\) satisfying
\[
2t/3<e\le t,
\]
and let \(P_j(t)\) indicate a patch root of that color satisfying
\[
6e\le t<27e/4.
\]
Both indicators are zero if no such root exists. The isolated point belongs to no corner and can be removed. In the patch window the three same-color owners
\[
\{e,9e/2,6e\}
\]
have precisely the four opposite edges
\[
(3e/2,e/2),\quad(2e,3e),\quad(3e/2,3e),\quad(2e,4e).
\]
Replacing those three phase points by \(\{3e/2,2e\}\) preserves the cover and saves one. Root \(e=1\) is not permitted, since \(9e/2\) would not be a board point. The construction with \(e=2\) is valid even though its owner \(9\) is on the vertical axis. ([Construction and exact incidences](<prefix_audit.md>))

Each root interval has multiplicative width less than two, hence contains at most one power of two. If a patch is active, \(6e\le t<27e/4<8e\); the largest dyadic board point is \(4e\le2t/3\), so an isolate cannot coexist with it. Thus **at most one exceptional root exists across all colors**, and any such root satisfies \(e>4t/27\). Write
\[
\delta_j=I_j+P_j,\qquad Q_j=K_j-\delta_j,\qquad M(t)=\min_jQ_j.
\]
The construction proves \(\tau(t)\le M(t)\). The theorem proved below is
\[
\boxed{\tau(D_t)=\min_{j\in\mathbb Z/3\mathbb Z}
\bigl(K_j(t)-I_j(t)-P_j(t)\bigr)\quad\text{for every real }t\ge3.}
\tag{C}
\]

The lower bound becomes an exact matching problem. For \(U\subset C_j\), let \(B(U)\) contain the opposite pair of every corner whose color-\(j\) owner lies in \(U\). Its bipartition has colors \(j+1,j+2\). An owner \(u=2^a3^b\) has the following edges, with the left endpoint written first:
\[
\begin{array}{c|c|l}
 &\text{opposite edge}&\text{availability}\\ \hline
N(u)&(u/3,2u/3)&b\ge1\\
E(u)&(3u/2,u/2)&a\ge1,\ 3u/2\le t\\
R(u)&(2u,3u)&3u\le t.
\end{array}
\tag{1}
\]
In particular a vertical owner has no east edge, irrespective of its numerical size. Solving these endpoint formulas gives the complete possible-owner lists
\[
l:\quad l/2,\ 2l/3,\ 3l;\qquad
v:\quad v/3,\ 3v/2,\ 2v,
\tag{2}
\]
subject to smoothness, membership in \(U\), and the actual edge cutoffs.

Put \(d(U)=|U|-\nu(B(U))\), where \(\nu\) is the maximum matching size. If \(W\) covers \(B(U)\), then \((C_j\setminus U)\cup W\) covers all corners; conversely every corner cover \(F\) yields \(U=C_j\setminus F\) and \(W=F\setminus C_j\). Bipartite matching-cover equality gives
\[
D_j:=\max_{U\subset C_j}d(U)=K_j-\tau(t).
\tag{3}
\]
For **every** global optimum \(F\), its omissions \(C_j\setminus F\) attain \(D_j\) in every color. A smaller graph cover or larger deficiency would produce a smaller corner cover. This identity is the basis for the later common-optimum argument. ([Matching correspondence and foundation audit](<final_global_audit.md>))

## Strict expansion reduces arbitrary deficiency to two boundary cones

Exclude the exceptional root \(e\) from its color’s pool, if it exists, and exclude nothing elsewhere. Denote the resulting pools by \(\mathcal A_j\) and their maximum deficiencies by \(D_j^*\). The established axis-avoiding classification supplies the universal input
\[
d(V)\le0\quad
\text{for every }V\subset\mathcal A_j\text{ with no point on }a=0.
\tag{4}
\]
Here “axis-avoiding” means avoiding the vertical axis. The classification concerns every inclusion-minimal positive-deficiency set of this kind, with no one-root or hole-free hypothesis: it is either an isolated dyadic root or exactly the patch \(\{e,9e/2,6e\}\), with \(A\ge2\) and the window above. Any positive finite set contains such a minimal positive subset, and both possibilities contain the excluded root. The \(e=2\) patch touches the vertical axis, so it does not invalidate (4). ([Authoritative classification](<../../early-attacks/augmentation-and-return-attacks/multiroot.md>), [full independent incidence reconstruction](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>), [final reconstruction](<final_global_audit.md>))

The strip mechanism behind that classification is worth retaining because it also controls the vertical case. With \(g=4/3\), \(q=9/2\), a forced horizontal chain \(u_n=xq^n\) terminates numerically at \(2t/3<u_k\le t\). Its \(2k\) selected vertices \(3u_n/2,2u_n\), \(n<k\), have at most \(2k+1\) owners, forcing the first owner strip \(gu_1,\ldots,gu_k\). The cap \(g^2u_k>t\) initiates a backward essentiality argument: a selected right endpoint of a north edge already hit on the left would require the missing capped owner uniquely. This excludes those right endpoints and forces another \(k-1\) selected vertices. A second backward argument starts from the leaf \(3g^2u_{k-1}\). For \(k\ge2\), the final \(4k-2\) selected vertices have at most
\[
(k+1)+k+(k-1)+(k-2)=4k-2
\]
owners, contradicting strict expansion. The rooted edges used are available because \(g^2u_{k-1}\le8t/27<t/3\). The bottom formal owners are nonsmooth, the cap owners are off-board, and distinct \(g\)-coordinates certify the counts. At \(k=2\) the final range is empty and the contradiction still holds. Only the isolate or the \(k=1\) patch survives. The cited proofs give the full endpoint lists and both backward inductions.

Now suppose \(D_j^*>0\), choose \(U\) inclusion-minimal among sets attaining that maximum, and choose a minimum graph cover \(W\). **The next properties hold at arbitrary positive deficiency.** Each \(w\in W\) uniquely covers edges of at least two distinct owners: zero such owners makes it redundant; just one owner \(u\) permits deletion of \(w,u\), leaving a proper allowed subset with deficiency at least \(D_j^*\). Improvement contradicts maximality, and equality contradicts inclusion-minimality.

For nonempty \(S\subset W\), let \(T_U(S)\) contain the owners of all available edges incident with \(S\), including doubly covered edges. Since \(W\setminus S\) covers \(B(U\setminus T_U(S))\),
\[
d(U\setminus T_U(S))\ge D_j^*+|S|-|T_U(S)|.
\]
Deleting owners stays in the allowed pool. Maximality and inclusion-minimality therefore imply
\[
|T_U(S)|\ge|S|+1.
\tag{5}
\]
If \(T_U(S)=U\), the same conclusion follows directly from \(|U|=|W|+D_j^*>|S|\). This handles the empty remainder and double coverage explicitly. ([Restricted-maximizer proof](<prefix_audit.md>))

The north edges of nonhorizontal owners form a matching, so positive deficiency forces a horizontal owner; (4) forces a vertical owner. For any interior owner \(u\), at least one predecessor \(u/6,2u/9,3u/4\) belongs to \(U\). Otherwise the north-left endpoint is a leaf. Its selected opposite endpoint must uniquely support \(E(4u/3)\), forcing \(2u\notin W\) and placing \(2u\) on the board. Hence \(E(u)\) exists. Its right endpoint is then a leaf, and the selected left endpoint must uniquely support \(N(9u/2)\), forcing \(3u\notin W\). The forced owner \(9u/2\le t\) makes \(R(u)\) available with neither endpoint selected, a contradiction.

If \(1\in U\), keep the origin case separate. Otherwise let the least axis roots be \(x=2^A,y=3^B\), \(A,B\ge1\). Decreasing predecessors terminate on an axis. Reversing them multiplies by \(g,q,gq\); other same-color roots differ by \(8=g^2q\) or \(27=gq^2\). Thus
\[
U\subset x\langle g,q\rangle_{\ge0}\cup y\langle g,q\rangle_{\ge0},
\qquad
y=xg^{(B-2A)/3}q^{(2B-A)/3}.
\tag{6}
\]
This is a containment statement, not forward closure. The exponent matrix has determinant three, so coordinates are unique.

Root balance also uses only essentiality. If \(A>2B\), both cones lie in the vertical cone; the chain \(yg^m\), \(m<B\), has leaf north-left endpoints and forces its continuation to the smaller horizontal root \(2^{2B}<x\). If \(B>2A\), both cones lie in the horizontal cone. The endpoint \(y'=3^{2A}<y\le t\) is already on-board, and every preterminal \(xq^n\), \(n<A\), is at most \(y'/q\le2t/9\); its east edge exists and forces the next owner. This reaches the forbidden smaller vertical root. Therefore
\[
r=(2A-B)/3\ge0,\qquad s=(2B-A)/3\ge0,\qquad
A=2r+s,\quad B=r+2s.
\tag{7}
\]
No criticality assumption is needed for this simpler root-balance proof. ([Current reconstruction](<final_prefix_audit.md>))

For incomparable roots \(r,s\ge1\), put
\[
u_n=xq^n,\quad v_m=yg^m,\quad
z=u_s=v_r=2^{2r}3^{2s}.
\]
The alternatives outside both cones force the vertical selections \(2v_m/3\in W\), \(2v_m\notin W\), \(m<r\), and the horizontal selections \(3u_n/2,2u_n\in W\), \(3u_n\notin W\), \(n<s\). The last vertical step gives \(z\le2t/3\). Strict expansion of the \(2s\) horizontal selected vertices forces all owners \(gu_1,\ldots,gu_s\).

If vertical rooted edges exist through index \(h<r\), their selected right endpoints together with the north-right selections have \(r+h+1\) vertices and at most \(r+h+2\) owners. Expansion forces \(qv_{h+1}=6v_h\in U\). An index \(h<r-1\) would then give \(v_{h+1}\le2t/9<t/3\), contradicting the claimed last rooted edge. Thus either \(qz\in U,z\le2t/9\), or no such rooted edge exists and \(y>t/3\), with \(g^r=z/y<2\), hence \(r\in\{1,2\}\).

The deep alternative \(z\le2t/9\) is impossible. In coordinates based at \(x\), the horizontal and vertical selected strips have possible-owner sets
\[
\begin{aligned}
H&=\{(0,n):0\le n\le s\}\cup\{(1,n):1\le n\le s\},\\
V&=\{(m,s):-r\le m\le0\}\cup\{(m,s+1):1-r\le m\le0\}.
\end{aligned}
\]
Their intersection is exactly \(\{z\}\). They give \(2r+2s\) selected vertices and \(2r+2s+1\) owners. The forced owners \(gz,qz\) then force two new selected vertices, \(2z,3z\), because the opposite endpoints \(2z/3,3z/2\) were excluded by the last chain steps. Their full owner lists are \(\{z,gz,6z\}\) and \(\{z,qz,6z\}\), adding at most one owner. This violates (5). Different bipartition colors and the cone coordinates verify distinctness; double coverage of \(R(z)\) is already covered by (5). ([Deep-strip proof](<../boundary-dominance/deep_branch.md>), [independent vertical audit](<../boundary-dominance/vertical_audit_and_transfer.md>))

Consequently an incomparable restricted maximizer has \(y>t/3\). It is the highest power of three on the whole board, and the only vertical owner in \(U\), since the next same-color one is \(27y>t\). Removing \(y\) leaves an allowed axis-avoiding set. Matching monotonicity and (4) give
\[
0<D_j^*=d(U)\le d(U\setminus\{y\})+1\le1.
\tag{8}
\]
**Only at this point does the arbitrary-deficiency maximizer become a critical set of deficiency one.**

## Two prefix gains force a collision inside one optimum

The degenerate cases \(s=0\) and \(r=0\) require augmentations, rather than an assertion that arbitrary omitted sets can be filled.

If \(s=0\), then \(A=2B\). Set \(k=a+2b,k_0=2B\). The vertical cone in the nonnegative quadrant is exactly the preferred-color part of \(k\ge k_0\), and the forced vertical chain selects every right-color point on \(k=k_0-1\). Its last east edge gives \(x\le2t/3\). Add the full preferred-color diagonals \(k_0-3,k_0-6,\ldots\ge0\), and repair with the right-color diagonals \(k_0-4,k_0-7,\ldots\ge0\). A new north/east right endpoint lies on \(k-1\); a rooted right endpoint lies on \(k+2\). Each is in the repair or the selected frontier, so all new edges are covered. The additions are disjoint from \(U\); every new owner is at most \(x/8\le t/12<4t/27\), so the excluded root is not introduced.

A diagonal has \(h(k)=\lfloor k/2\rfloor+1\) points, with \(h(-1)=0\). Pair each owner diagonal with the cover diagonal immediately below it. The difference is one precisely for even diagonal index \(n\) in \(k_0-3n\). The guaranteed deficiency gain is \(\lfloor B/3\rfloor\). Maximality gives
\[
s=0\Longrightarrow B\le2. \tag{P1}
\]
If \(r=0\), use \(k=2a+b,k_0=2A\), the horizontal chain’s left-color frontier, and the same-spaced owner and left-cover diagonals. The identical endpoint check applies; each new owner is at most \(y/27\le t/27\). The guaranteed gain is \(\lfloor A/3\rfloor\), hence
\[
r=0\Longrightarrow A\le2. \tag{P2}
\]
Every repairing point is on-board, and overlap with \(W\) can only improve either gain. These augmentations need maximality over the entire allowed pool; mere criticality would not suffice. ([Full prefix constructions and counts](<prefix_audit.md>), [final prefix audit](<final_prefix_audit.md>))

Let \(j_{\mathrm{top}}=-\lfloor\log_3t\rfloor\bmod3\). Incomparable maximizers occur only in that color by (8). For \(t\ge18\), P1–P2 leave the following mandatory owners outside the top color; the table also applies in the top color if its minimal maximizer is origin-containing or degenerate.

| Color | Remaining least-root case | Mandatory owner |
|---|---|---:|
| \(0\) | Origin | \(6\) |
| \(1\) | \(r=0,A=1\), or \(s=0,B=2\) | \(12\) |
| \(2\) | \(r=0,A=2\), or \(s=0,B=1\) | \(18\) |

At the origin, \(R(1)\) forces one of \(2,3\) into \(W\). Selecting both would leave either with at most one uniquely supported owner, violating essentiality; the selected one therefore requires owner \(6\). For color one, the chain from \(2\) and its first strip force \(12\), or the vertical chain is \(9,12,16\). For color two, the horizontal chain from \(4\) passes through \(18\). In the remaining case \((A,B)=(2,1)\), the chain \(3,4\) selects \(2\) and excludes \(6\). The available \(R(3)\) forces \(9\). The selected pair \(\{2,9\}\) has possible owners only \(\{3,4,18\}\); expansion requires owner \(18\) and its actual edge \(E(18)\). That edge requires \(t\ge27\), so the configuration cannot exist on \(18\le t<27\). The conditional mandatory-owner statement remains valid throughout \(t\ge18\). Every maximizing set contains an inclusion-minimal maximizing subset, so the mandatory owner belongs to every relevant maximizer. ([Mandatory-owner and availability audit](<final_global_audit.md>))

It remains essential to put these statements in **one optimum**. For the exceptional color, let \(D,D^*\) denote the unrestricted and restricted maxima. Edge inclusion gives
\[
d(U)\le d(U\setminus\{e\})+1,\qquad D^*\le D\le D^*+1.
\tag{9}
\]
If \(D=D^*+1\), every unrestricted maximizer contains \(e\); deleting it from any such maximizer gives deficiency exactly \(D^*\). Thus any global optimum supplies the required restricted omission. If \(D=D^*\), choose a restricted maximizer \(V\) and a minimum cover \(W\) of its graph. Then
\[
F=(C_j\setminus V)\cup W
\]
is a global optimum, contains \(e\), and omits exactly \(V\) in that color. In the other two colors, the omissions of this same \(F\) maximize automatically by (3). There is at most one excluded color, so these choices do not compete. This is a generic one-exclusion argument; it assumes no fixed deficiency drop for patch deletion. ([Compatibility proof](<patch_global.md>))

Suppose \(t\ge18\) and \(\tau<M\). Then \(D_j>\delta_j\), so (9) gives \(D_j^*>0\) in all colors. Choose the common optimum \(F\) just constructed, and within each of its restricted omitted sets choose an inclusion-minimal maximizing subset \(U_j\). **Each \(U_j\) uses its own independently chosen minimum graph cover in the geometric proof. Those graph covers need not lie in \(F\). Only the owner containment \(U_j\subset C_j\setminus F\) is used for the collision.**

The two non-top colors omit their corresponding two members of \(\{6,12,18\}\) from this same \(F\). An origin-containing or degenerate top maximizer would force the third omission, leaving the existing corner \(\{6,12,18\}\) uncovered. Thus the top maximizer is incomparable and (8) gives \(D_{\mathrm{top}}^*=1\). From the counterexample hypothesis and (9),
\[
1+\delta_{\mathrm{top}}\le D_{\mathrm{top}}
\le D_{\mathrm{top}}^*+\delta_{\mathrm{top}}=1+\delta_{\mathrm{top}}.
\]
Consequently
\[
\boxed{\tau=Q_{\mathrm{top}}-1,\qquad M=Q_{\mathrm{top}}.} \tag{10}
\]
The second equality follows from \(\tau<M\le Q_{\mathrm{top}}\) and integrality. Thus any failure has exactly a one-unit deficit and a minimizing adjusted top phase. This controls aggregate deficiency without adding deficiencies of critical components or identifying separately chosen canonical covers. Both final audits explicitly checked these quantifiers.

## The high prefix eliminates every unbounded parameter

The remaining incomparable maximizer has \(r\in\{1,2\}\). The same strip mechanism used in the axis-avoiding theorem shows that, when \(s\ge2\), a cap \(g^2z>t\) is impossible. For \(u_n=xq^n\), use the owner columns \(u_n,gu_n,g^2u_n,g^3u_n\). The rooted edges below the caps exist because
\[
gu_n\le gz/q\le16t/81<t/3,\qquad
g^2u_n\le g^2z/q\le64t/243<t/3\quad(n<s).
\]
The first backward induction excludes the second column’s north-right endpoints and forces its rooted-left selections; expansion forces the third owner column. The second induction starts at the leaf \(3g^2u_{s-1}\). The final \(4s-2\) selected vertices have possible owners contained in
\[
\{u_0,\ldots,u_s\}\cup\{gu_1,\ldots,gu_s\}
\cup\{g^2u_1,\ldots,g^2u_{s-1}\}
\cup\{g^3u_2,\ldots,g^3u_{s-1}\},
\]
also of size \(4s-2\), contradicting (5). The bottom formal owners \(gx,g^3xq\) are nonsmooth; the top \(g^2z,g^3z\) are off-board. Distinct \(g\)-coordinates justify the selected count, including \(s=2\), where the last range is empty. ([High-cap proof and endpoint reconstruction](<../boundary-dominance/vertical_audit_and_transfer.md>), [current full audit](<final_global_audit.md>))

For \(r=2\), \(z=g^2y>16t/27\), so \(g^2z>t\). Hence \(s=1\), with \(x=32,y=81,z=144\), and \(216\le t<243\). For \(r=1\), \(z=gy>4t/9\). If \(z\le t/2\), the forced owner \(gz\) has an east edge with excluded right endpoint \(2z/3\), forcing \(2z\in W\). Its only other possible owners are \(z\), whose rooted edge is unavailable, and \(6z>t\). Essentiality fails. Therefore \(z>t/2\). At \(s=1\) this gives \([54,72)\); at \(s\ge2\), avoiding the cap gives
\[
r=1,\qquad z=4\cdot9^s,\qquad
64\cdot9^{s-1}\le t<8\cdot9^s.
\tag{11}
\]

The new prefix augmentation eliminates every \(s\ge4\) in (11). Put \(A=s+2\), \(y=3^{2s+1}\), \(k=2a+b\), and \(k_0=2A\). In coordinates \(u=xg^mq^n\),
\[
a=A+2m-n,\qquad b=2n-m,\qquad k=k_0+3m.
\]
The horizontal cone is exactly the preferred-color region \(k\ge k_0\). The vertical cone starts at \((-1,s)\); a point below \(k_0\) must have \(m=-1,n\ge s\), and then \(a=s-n\ge0\) forces \(n=s\). Hence
\[
U\cap\{k<k_0\}=\{y\}. \tag{12}
\]
Let \(\mathcal P_0\) contain every preferred-color point on \(k_0-3,k_0-6,\ldots\ge0\), let \(\mathcal P=\mathcal P_0\setminus\{y\}\), and let \(\mathcal L\) contain the left-color points on \(k_0-4,k_0-7,\ldots\ge0\). By (12), the added owners \(\mathcal P\) are disjoint from \(U\).

Every new north/east left endpoint is on \(k-1\), hence in \(\mathcal L\). Every rooted left endpoint from a lower added diagonal is there too. A rooted edge from the highest added diagonal meets frontier \(k_0-1=2s+3\). The forced selections \(3u_n/2\), \(0\le n<s\), are precisely its points with first exponent \(a=2,\ldots,s+1\). The two missing formal frontier points are \(9y\), which is off-board, and \(2y\). **No new edge needs \(2y\): its only lower-prefix rooted owner is \(y\), which was already present and was excluded from the additions.** Equivalently, its complete owner list is \(\{y,4y/3,6y\}\); the last two lie on \(k_0\), outside the added prefix, and \(6y>t\). Also \(R(y)\) is unavailable since \(3y>t\). Old edges retain their cover in \(W\). Therefore \(W\cup\mathcal L\) covers \(B(U\cup\mathcal P)\).

All additions are on-board. On \(2a+b=k\), the largest label is \(3^k\); the top owner diagonal has maximum \(y\le t\). After removing \(y\), its largest added owner is \(2y/9=z/6\le t/9\); lower owner diagonals are smaller. Repair points are at most \(y/3=z/4\le t/6\). Thus no exceptional root \(e>4t/27\) is introduced, including with an active patch.

The same exact diagonal pairing as P2 gives
\[
|\mathcal P_0|-|\mathcal L|=\lfloor A/3\rfloor,\qquad
|\mathcal P|-|\mathcal L|=\lfloor(s-1)/3\rfloor.
\]
Hence
\[
\boxed{d(U\cup\mathcal P)\ge D_j^*+\lfloor(s-1)/3\rfloor.} \tag{P4}
\]
Overlap between \(W\) and \(\mathcal L\) only improves this inequality. For \(s\ge4\), its positive gain contradicts **maximality over the entire allowed pool**. Criticality alone would not justify the contradiction; the set produced by (10) retains the necessary maximum property. ([Prefix derivation](<high_phase.md>), [independent missing-frontier reconstruction](<patch_global.md>), [final prefix audit](<final_prefix_audit.md>))

Only five high subintervals remain. All are left-closed and right-open; vector coordinates are ordered \(0,1,2\).

| Parameters | Interval | \(K\) | \(I\) | \(P\) | \(Q=K-I-P\) | Top color |
|---|---|---|---|---|---|---:|
| \(r=1,s=1\) | \([54,64)\) | \((6,5,5)\) | \((0,0,0)\) | \((0,0,0)\) | \((6,5,5)\) | 0 |
| \(r=1,s=1\) | \([64,72)\) | \((7,5,5)\) | \((1,0,0)\) | \((0,0,0)\) | \((6,5,5)\) | 0 |
| \(r=2,s=1\) | \([216,243)\) | \((9,8,9)\) | \((0,0,0)\) | \((0,0,0)\) | \((9,8,9)\) | 2 |
| \(r=1,s=2\) | \([576,648)\) | \((12,12,11)\) | \((1,0,0)\) | \((0,0,0)\) | \((11,12,11)\) | 1 |
| \(r=1,s=3\) | \([5184,5832)\) | \((20,19,20)\) | \((1,0,0)\) | \((0,0,0)\) | \((19,19,20)\) | 2 |

**The adjusted top coordinate is strictly greater than the minimum in every row**, contradicting (10). There is no active patch in these intervals: the preceding patches are already inactive at their strict upper endpoints \(54,216\). The last two isolates are \(512,4096\), both color zero. The lower-cap equalities at \(576,5184\) are included; the upper endpoints \(648,5832\) are excluded by \(z>t/2\). Exact event checks show no smooth birth or indicator transition inside a listed interval. ([Exact checker](<prefix_phase_checks.py>), [certificate](<prefix_phase_checks.json>))

For completeness, the eight remaining base intervals are:

| Interval | \(K\) | \(I\) | \(P\) | \(M\) |
|---|---|---|---|---:|
| \([3,4)\) | \((1,1,1)\) | \((0,0,0)\) | \((0,0,0)\) | 1 |
| \([4,6)\) | \((1,1,2)\) | \((0,0,1)\) | \((0,0,0)\) | 1 |
| \([6,8)\) | \((2,1,2)\) | \((0,0,0)\) | \((0,0,0)\) | 1 |
| \([8,9)\) | \((3,1,2)\) | \((1,0,0)\) | \((0,0,0)\) | 1 |
| \([9,12)\) | \((3,2,2)\) | \((1,0,0)\) | \((0,0,0)\) | 2 |
| \([12,27/2)\) | \((3,3,2)\) | \((0,0,0)\) | \((0,1,0)\) | 2 |
| \([27/2,16)\) | \((3,3,2)\) | \((0,0,0)\) | \((0,0,0)\) | 2 |
| \([16,18)\) | \((3,4,2)\) | \((0,1,0)\) | \((0,0,0)\) | 2 |

For \(3\le t<9\), \(\{2\}\) hits every corner and the corner at \(1\) requires a nonempty cover, so \(\tau=1\). For \(9\le t<18\), \(\{3,4\}\) hits every corner, whose roots are among \(1,2,3,4\). The three existing corners rooted at \(1,2,3\) have empty common intersection, so \(\tau=2\). The table gives \(M\) equal to these optima throughout. The real threshold \(27/2\) is indispensable even though the smooth board does not change there. The actual critical patch \(\{2,9,12\}\) lasts through \([12,18)\), longer than its sufficient construction-indicator window; the direct base proof respects that distinction. ([Base certificate and real endpoint audit](<final_prefix_audit.md>))

The upper construction, contradiction for \(t\ge18\), and direct base covers prove (C) for **every real** \(t\ge3\). The universal conclusion comes from the symbolic maximum-deficiency, cone, strip, and prefix arguments; finite arithmetic is used only after those arguments reduce the possibilities to the displayed intervals.

## Adversarial checks validate the proof without replacing it

The strongest challenges concerned hidden quantifiers and boundary edges. Both final reviewers reconstructed the foundations, checked arbitrary-deficiency essentiality and expansion, and followed the single-exclusion lemma through the same-optimum collision. They explicitly allowed each minimal maximizing subset its own graph cover. They checked both zero-coordinate cases separately, the \(t\ge27\) availability required in the degenerate color-two case, double coverage in the deep-strip contradiction, the missing frontier \(2y\), and the exclusion bound for every newly added owner. Both reported **PASS for the complete finite formula**, with no remaining finite-combinatorial lemma identified as open. These are internal mathematical audits, not external peer review or formal proofs. ([Final global audit](<final_global_audit.md>), [final prefix audit](<final_prefix_audit.md>))

Earlier attempts also produced concrete counterexamples to tempting stronger premises. At \(t=54\), the unique optimum maximizing color zero is \(\{1,6,12,16,18\}\), which contains no complete vertical phase; matching rank also fails submodularity there, with ranks \(2,4,5,2\) on the two sets, their union, and their intersection. Unrestricted full-class filling fails at \(t=1536\). Equal one-step boundary signatures, even strengthened by complete endpoint matrices and color counts, can have different two-shell optima: the explicit \(D_{64}\) pair gives \(22\) and \(21\). None of those false normalizations is used above. ([Canonical and submodularity audit](<../boundary-dominance/canonical_audit_and_collision.md>), [filling counterexample recorded in the earlier report](<../global-boundary-proof/REPORT.md>), [exact transfer counterexamples](<../boundary-dominance/vertical_audit_and_transfer.md>))

Numerical high-window membership alone also cannot replace the augmentation. At \(s=17\), the lower endpoint \(t=118593292086517824\) has raw counts \((354,354,354)\); the active color-zero patch changes them to \((353,354,354)\). This breaks the raw-count shortcut without producing a counterexample to (C). P4 instead gives a positive gain for every \(s\ge4\), regardless of any raw phase tie. The local LP-cut ceiling proposal and bottom-preserving parity repair likewise have explicit failures in the earlier work; neither supplies a premise of this proof. ([High-phase analysis and exact data](<high_phase.md>), [energy, LP, and parity audit](<../boundary-dominance/energy_audit_and_parity.md>))

The bounded verification is precise. The coordinator read and reran both current standard-library checkers successfully. The prefix checker certifies the eight base intervals and five surviving high subintervals with exact rational endpoints, separate \(K,I,P\) counts, absence of interior events, and the required phase comparisons. The high-phase checker independently cross-checks row counts, verifies four specified prefix geometries at \(s=2,3,4,17\), and records the large raw tie; its finite-case table also contains three additional degenerate intervals. The final prefix auditor used a separate exact BigInt row-width and event certificate for the thirteen base/high subintervals. A row of width \(3q+r\) contributes \(q\) of each color plus residues \(-b,\ldots,r-1-b\), while quarter-unit arithmetic retains the fractional correction endpoints. The final global auditor separately tested the first excluded prefix case \(s=4,t=46656\), deliberately leaving the on-board point \(2y\) out of the repair. These checks found no inconsistency, but their finite samples do not prove the unbounded lemmas. This report adds no experiments and changes no prior research notes. ([Prefix checker and output](<prefix_phase_checks.py>), [prefix certificate](<prefix_phase_checks.json>), [high-phase checker](<high_phase_check.py>), [high-phase certificate](<high_phase_check.json>), [independent BigInt certificate](<final_prefix_audit.md>))

## Conclusion

The decisive change is a way to compare aggregate optima without normalizing an arbitrary boundary word or asserting that all minimum covers contain a vertical phase. One excluded owner permits the necessary common optimum, while controlled prefixes provide the maximum-deficiency contradictions. Those mechanisms close the finite task despite the counterexamples to stronger geometric and algebraic shortcuts.

For Erdős #168(ii), the remaining work is arithmetic: obtain an adequate infinite return sequence for the corrected approximation argument and prove the required nonvanishing of the resulting errors. The finite theorem removes its combinatorial condition; it does not supply either arithmetic obligation. No Lean work, external review, historical-priority assessment, or irrationality proof is claimed. The material limitation is that acceptance presently rests on the written dependency chain, two internal fresh-context audits, and the specified exact finite certificates. ([Earlier corrected arithmetic obligations; its finite-status statement is superseded](<../global-boundary-proof/REPORT.md>), [current audit scope](<final_global_audit.md>))
