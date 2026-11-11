# Vertical critical sets: two-cone restrictions and the remaining phase comparison

Research round, 7 November 2026. This note proves additional restrictions on vertical-touching critical sets and gives exact counterexamples to several stronger shortcuts. It does **not** prove the global formula \(\tau(D_t)=\min_j(K_j-I_j-P_j)\). The new arguments use the audited axis-avoiding proof but do not assume that formula. No Lean work or broad numerical sweep was performed.

## What do the two least axis roots force?

### Takeaway

Every positive critical set has a horizontal root. If it also touches the vertical axis and omits the origin, its least roots \(2^A,3^B\) satisfy \(A/2\le B\le2A\). Between these roots, exact forced chains meet at a determined lattice point; an additional strict owner count puts that meeting point either deep inside the board or in a narrow boundary case. [Audited ingredients](<combinatorial_and_coefficient_audit.md>).

### Cited Findings

- The owned edges and critical-cover inequality are independently audited in [combinatorial_and_coefficient_audit.md](<combinatorial_and_coefficient_audit.md>). For a critical \(U\), a minimum cover \(W\) of \(B(U)\) has size \(|U|-1\); each selected vertex uniquely covers at least two owners; and every nonempty \(S\subset W\) has at least \(|S|+1\) incident owners.
- The same audit proves the full axis-avoiding classification and records the precise small-\(x=2\) constrained-cover caveat. It does not establish a vertical-axis normalization. [Audited classification and scope](<combinatorial_and_coefficient_audit.md>).

### Inferences

All new derivations in this section use those incidence identities and the strict owner count. Write \(c(2^a3^b)=a-b\pmod3\), \(D_t=\{2^a3^b\le t:a,b\ge0\}\), and \(d(U)=|U|-\nu(B(U))\). A critical set means inclusion-minimal positive deficiency, not merely minimal under one deletion.

For clarity, the three edge types are

\[
N(u)=(u/3,2u/3),\quad
E(u)=(3u/2,u/2),\quad
R(u)=(2u,3u).
\]

Their conditions are respectively \(b\ge1\), \(a\ge1\) and \(3u\le2t\), and \(3u\le t\). The possible owners at a physical left vertex \(l\) are \(l/2,2l/3,3l\); those at a right vertex \(r\) are \(r/3,3r/2,2r\). Availability must still be imposed.

#### Two cones, including all off-chain owners

The north edges of distinct nonhorizontal owners form a matching. Thus \(d(U)>0\) forces at least one horizontal root. For an interior owner \(u\), the audited predecessor proof still applies even when other owners are vertical: its proof requires only that this particular \(u\) have \(a,b\ge1\). Hence at least one of

\[
u/6,\qquad 2u/9,\qquad 3u/4
\]

belongs to \(U\). Following decreasing predecessors ends on one of the two axes.

Suppose \(U\) also contains a vertical root. Let \(x=2^A\) and \(y=3^B\) be its least roots on the horizontal and vertical axes. All horizontal roots of its color are \(x8^\ell\), and all vertical roots are \(y27^\ell\). Put

\[
g=4/3,\qquad q=9/2,\qquad gq=6,\qquad g^2q=8,\qquad gq^2=27.
\]

Every owner therefore lies in the union

\[
U\subset \{xg^m q^n:m,n\ge0\}
\ \cup\
\{yg^m q^n:m,n\ge0\}. \tag{V1}
\]

This is an inclusion, not a closure or filling assertion. Smoothness, nonnegative ordinary exponents, and the board cutoff are additionally required.

In coordinates based at \(x\), the vertical root is

\[
y=xg^{(B-2A)/3}q^{(2B-A)/3}. \tag{V2}
\]

The exponents are integers because \(A+B\equiv0\pmod3\). Multiplicative independence of \(g,q\) makes the coordinates unique. Consequently, excluding a coordinate from both cones excludes all possible off-chain owners at that location.

#### Root balance

If \(1\in U\), then \(A=B=0\). Treat that case separately. Otherwise \(A,B\ge1\), and

\[
\boxed{A/2\le B\le2A.} \tag{V3}
\]

To prove \(A\le2B\), suppose \(A>2B\). The horizontal cone is then contained in the vertical cone, and the coordinates of \(x\) relative to \(y\) have positive \(q\)-exponent. On the boundary labels \(v_m=yg^m\), \(0\le m<B\), the two alternative owners at the left endpoint of \(N(v_m)\) are \(v_m/6\) and \(2v_m/9\). Both have \(q\)-exponent \(-1\), outside both cones. That left endpoint is a leaf. Essentiality at the selected right endpoint forces \(E(gv_m)\) uniquely. Thus the chain must reach \(yg^B=2^{2B}\in U\), a smaller horizontal root than \(x\), a contradiction.

For the other inequality, suppose \(B>2A\). Now the whole set lies in the horizontal cone. Starting from \(x\), the same leaf argument as in the audited proof forces \(x,xq,\ldots\) while the east edge is available. It cannot reach \(xq^A=3^{2A}\), since this would be a smaller vertical root than \(y\). A numeric terminal label \(u_k\), \(k<A\), must therefore satisfy \(2t/3<u_k\le t\). The audited three-strip proof applies to this terminal ray: its required negative-\(g\) owners are excluded by the cone, and all labels used in the proof have positive first exponent because \(k<A\). It gives the isolate or the three-label patch, or a contradiction for \(k\ge2\). The isolate and this patch have no vertical owner, contradicting the present hypothesis. This proves \(B\le2A\).

Define nonnegative integers

\[
r=(2A-B)/3,\qquad s=(2B-A)/3.
\]

Then

\[
A=2r+s,\quad B=r+2s,\quad
y=xg^{-r}q^s,\quad
z=xq^s=yg^r=2^{2r}3^{2s}. \tag{V4}
\]

#### Forced meeting chains

Assume first \(r\ge1\), allowing \(s=0\). On \(v_m=yg^m\) for \(0\le m<r\), the alternative owners at the north-left endpoint have coordinates

\[
(m-r-1,s-1),\qquad(m-r,s-1)
\]

relative to \(x\). They are outside the horizontal cone because their first coordinate is negative, and outside the vertical cone because their second coordinate is below \(s\). Thus \(N(v_m)\)'s left endpoint is a leaf; its right endpoint is selected; and \(E(v_{m+1})\) is forced uniquely. In particular,

\[
v_0,\ldots,v_r=z\in U,\qquad 2v_m\notin W,\qquad
2v_m\le t\quad(0\le m<r).
\]

The last inequality at \(m=r-1\) gives \(3z/2\le t\), so

\[
z\le2t/3. \tag{V5}
\]

For \(u_n=xq^n\), \(0\le n<s\), the alternative owners at the east-right endpoint have coordinates \((-1,n-1)\) and \((-1,n)\). They are outside both cones. The east edge is available since \(u_n\le z\le2t/3\) and its first exponent is positive. Consequently the horizontal chain is forced too:

\[
u_0,\ldots,u_s=z\in U,\qquad
L_n=3u_n/2\in W,\quad 3u_n\notin W\quad(0\le n<s). \tag{V6}
\]

If \(s\ge1\), all \(R(u_n)\), \(n<s\), are available because \(u_n\le z/q\le4t/27<t/3\). Thus \(A_n=2u_n\in W\). The strict owner count for the \(2s\) vertices \(L_n,A_n\) forces the additional first strip

\[
gxq^n\in U\qquad(1\le n\le s). \tag{V7}
\]

Indeed their only possible owners are \(u_0,\ldots,u_s\) and \(gxq,\ldots,gxq^s\), a total of \(2s+1\); the formal owner \(gx\) has negative \(3\)-exponent.

If \(r=0\), the horizontal cone contains the whole set and \(s=A\ge1\). The chain \(x,\ldots,xq^s=y\) is still forced: all its east edges before the vertical endpoint are available since \(xq^{s-1}=y/q\le2t/9\). The same first-strip count gives (V7), using this bound to make every required rooted edge available. Here (V5) does not follow from a vertical chain. If \(y>2t/3\), the same three-strip cap argument rules out \(s\ge2\); \(s=1\) leaves the small set \(\{2,9,12\}\). These boundary qualifications are essential.

#### A strict vertical-strip dichotomy

For \(r\ge1\), the selected vertices \(2v_m/3\), \(0\le m<r\), are already known. Whenever \(v_m\le t/3\), \(R(v_m)\) is available and \(2v_m\notin W\), so \(3v_m\in W\).

If at least one such rooted edge exists, the indices are \(0,\ldots,h\). Select all \(r\) vertices \(2v_m/3\), together with the \(h+1\) vertices \(3v_m\). They are distinct by independence of \(g,q\). The first group has only the chain owners \(v_0,\ldots,v_r\). The second group can add only

\[
qyg^m,\qquad 1\le m\le h+1;
\]

the expression \(qy\) is nonsmooth. There are at most \(r+h+2\) owners for \(r+h+1\) selected vertices. Strict expansion forces every one, particularly

\[
qyg^{h+1}=6v_h\in U,\qquad v_h\le t/6.
\]

If \(h<r-1\), then \(v_{h+1}=gv_h\le2t/9<t/3\), contrary to the definition of \(h\). Hence \(h=r-1\), and \(qz\le t\).

If there is no such rooted edge, \(y>t/3\). Together with \(z=g^ry\le2t/3\), this implies \(g^r<2\), hence \(r\le2\). We have proved

\[
\boxed{\text{Either }z\le2t/9\text{ and }qz\in U,
\quad\text{or }y>t/3\text{ and }r\in\{1,2\}.} \tag{V8}
\]

The low branch also forces \(6y\in U\). For \(s\ge1\), (V7) separately forces \(6x\in U\).

### Gaps

These are restrictions on actual critical sets, not a characterization of all sets in the two cones. Origin-containing sets, the deep branch of (V8), and the \(r=0\) boundary still require an exact comparison with competing color counts. Nothing here implies that a critical set fills either cone or can be filled to the whole color class without loss.

## How far do the upper-boundary cases reduce?

### Takeaway

The high branch of (V8) has several completely determined small cases. Its remaining \(r=1,s\ge2\) branch is real, not an empty artifact: an exact critical set occurs at \(t=576\). These reductions improve the boundary description but do not finish the phase comparison. [Exact certificates](<vertical_critical_check.json>).

### Cited Findings

- The existing exact integer augmenting-path matcher was reused, without modifying its earlier folder. [Existing matcher](<../boundary-and-arithmetic/dual_check.py>).
- Six specified critical sets were checked against every proper subset. Each also has an explicit cover and a matching of size one less than its number of owners. The saved checker and JSON provide reproducible certificates. [Checker](<vertical_critical_check.py>); [certificate data](<vertical_critical_check.json>).

### Inferences

Assume the high branch \(y>t/3\) of (V8).

For \(r=2\), \(z=g^2y>16t/27\), so \(g^2z>t\). If \(s\ge2\), the audited three horizontal strip argument applies to the forced \(q\)-chain of length \(s\), even though its terminal label is not an east-cutoff terminal. The needed facts are exactly: the selected \(L_n,A_n\) of (V6); the first strip (V7); the cap \(g^2z>t\); and availability of the lower rooted edges. The latter follows from

\[
\frac{g^2}{q}z\le \frac{32}{81}\frac{2t}{3}=\frac{64t}{243}<t/3.
\]

Its second and third backward inductions and owner counts therefore contradict strict expansion. Thus \(s\le1\). This produces precisely:

| \(r,s\) | Least roots \(x,y\) | Forced critical set | Parameter interval | A competing phase |
|---|---|---|---|---|
| \(2,0\) | \(16,9\) | \(\{9,12,16\}\) | \(24\le t<27\) | \(K_0=3<K_1=4\) |
| \(2,1\) | \(32,81\) | \(\{32,81,108,144,192\}\) | \(216\le t<243\) | \(K_1=8<K_2=9\) |

The intervals follow from \(3z/2\le t<3y\). The forced sets have deficiency one throughout each interval, because their owned graphs do not change before the upper endpoint. Criticality makes them the entire \(U\). The phase-count comparisons are direct counts on those boards.

For \(r=1,s=0\), the forced chain is \(\{3,4\}\), with \(6\le t<9\). Its sole required cover vertex is \(2\), and \(K_1=1\) is smaller than the color-2 count. This completely resolves that high case.

Now let \(r=1,s\ge1\). Since \(y=z/g>t/3\), initially \(z>4t/9\). In fact

\[
z>t/2. \tag{V9}
\]

If \(z\le t/2\), the forced owner \(gz\) has an east edge whose right endpoint \(2z/3\) is outside \(W\), by the last horizontal-chain step. Thus \(2z\in W\). But the other possible owners at \(2z\) are \(z\), via a rooted edge, and \(6z\), via a north edge. The former edge is unavailable since \(z>t/3\), and the latter owner is beyond the board. The selected vertex would have just one incident owner, contradicting essentiality.

At \(s=1\), (V9) leaves \(54\le t<72\) and the forced set

\[
U=\{8,27,36,48\}.
\]

It has the cover \(\{12,16,18\}\) and a size-three matching, and all its proper subsets have nonpositive deficiency. Its graph is constant on that interval, so this is the entire critical set. For \(54\le t<64\), \(K=(6,5,5)\); for \(64\le t<72\), \(K=(7,5,5)\) and color zero also has the isolated point \(64\). In both subintervals another adjusted phase is strictly smaller.

For \(s\ge2\), the same three-strip contradiction would apply if \(g^2z>t\). Therefore the remaining high branch must satisfy

\[
\boxed{r=1,\quad s\ge2,\quad t/2<z\le9t/16.} \tag{V10}
\]

Equivalently, since \(z=4\cdot9^s\), its window is
\(64\cdot9^{s-1}\le t<8\cdot9^s\).

This branch cannot be discarded. At \(s=2,t=576\), the set

\[
U=\{16,72,96,243,324,432,576\}
\]

is critical. The cover \(\{24,32,108,144,162,192\}\) and the saved size-six matching certify deficiency one; all 127 proper subsets were checked. Its least roots are \(16,243\), and its meeting point is \(324=9t/16\). The graph remains unchanged for \(576\le t<648\). Here \(K=(12,12,11)\), so this particular obstruction is paid by color two. The proof does not establish the corresponding comparison for every \(s\).

The separate small vertical patch deserves care:

\[
\{2,9,12\}\text{ is critical for }12\le t<18.
\]

Its graph is the path \(1-3-6-4-8\): the vertices \(3,4\) cover it and it has a matching of size two. Any proper pair containing owner \(2\) has its disjoint east and rooted edges; the other pair has disjoint north edges. Its east edge at owner \(9\) is permanently absent because \(9\) lies on the vertical axis. Its first additional owned edge is \(E(12)\), at \(t=18\). Thus its actual critical interval is longer than the construction indicator's sufficient interval \(12\le t<27/2\). At \(t=12\), it belongs to a winning adjusted phase and contains the exceptional patch root \(2\). This is why the proposed three-critical obstruction must exclude the exceptional root and cannot simply ban every vertical critical set in a winning phase.

### Gaps

The finite cases above are paid for, but this is not a proof that arbitrary vertical-touching deficiency is paid for by a competing phase. The remaining families include the deep branch, (V10) for unbounded \(s\), \(r=0\) beyond its small patch case, and critical sets containing the origin. Independent positive critical sets may overlap in their owner-neighborhood structure; their deficiencies cannot simply be added.

## What do the exact obstructions leave for the global proof?

### Takeaway

Criticality does not imply forward closure, and a vertical-touching positive set need not retain its deficiency when filled to the full color class. The two-cone chains give some exact collision criteria, but they do not yet rule out three simultaneous critical colors. The global finite optimum remains unproved by this round. [Saved exact checks](<vertical_critical_check.json>).

### Cited Findings

- The known color-2 patch at \(t=1536\) produces a cover of size 14, with all three color counts equal to 15. [Construction](<../../early-attacks/open-conjecture-transfer-search/168_grid.md>).
- The stronger shortcuts below were tested on specified small sets or one existing patch board; the only complete critical-subset enumeration was the single board \(t=216\), with 1,277 nonempty masks. [Exact checker](<vertical_critical_check.py>).
- Connectivity and three boundary contacts alone are already insufficient, as certified at \(t=729\). That earlier witness has negative deficiency and does not decide the stronger criticality-dependent statement. [Spanning-obstruction audit](<arithmetic_and_obstruction_audit.md>).

### Inferences

#### Forward closure fails

At \(t=216\), the critical color-zero set

\[
U=\{1,6,27,36,162,216\}
\]

has the five-vertex cover \(\{2,9,12,54,72\}\), a size-five matching, and no positive proper subset. But \(g\cdot6=8\) and \(g\cdot36=48\) lie on the board outside \(U\). The incomparable, origin-free example at \(t=576\) also misses \(g\cdot96=128\). Hence even the genuine two-cone case does not force \(g\)-closure.

At \(t=216\), the critical color-two set
\(\{3,4,18,24,32,81,108,144\}\) omits \(6\cdot32=192\), so a proposed closure under all available larger same-color neighbors also fails.

For completeness, the exact critical lists at that one board are:

| Color | \(K_j\) | All inclusion-minimal positive subsets |
|---|---:|---|
| 0 | 9 | \(\{1,6,27,36,162,216\}\) |
| 1 | 8 | none |
| 2 | 9 | \(\{32,81,108,144,192\}\); \(\{3,4,18,24,32,81,108,144\}\); \(\{3,4,18,24,32,81,108,192\}\) |

The enumeration processes subsets by increasing cardinality and discards a set containing an already found critical subset. It therefore verifies true inclusion-minimality, not merely the one-deletion condition. A three-color critical-union test at this board is vacuous because color one has no positive subset.

The same complete list disproves a different shortcut: positive critical owner sets do not form the circuits of a matroid. The two color-two critical sets
\(\{32,81,108,144,192\}\) and \(\{3,4,18,24,32,81,108,144\}\) share owner \(32\), but every color-two critical set on this board contains \(32\). Their union with \(32\) removed contains no positive critical subset, violating circuit elimination. This does not refute a hypergraphic-matroid construction based on the different ground set of neighborhoods of one fixed canonical cover.

#### Unrestricted full-class filling fails

At \(t=1536\), take

\[
F=(C_2\setminus\{256,1152,1536\})\cup\{384,512\}.
\]

The checker verifies every corner is met and \(|F|=14\). Let

\[
U=C_0\setminus\{384,512\},\qquad W=F\setminus C_0.
\]

Then \(|U|=13\), \(W\) is a size-12 cover of \(B(U)\), and the saved matching has size 12, so \(d(U)=1\). In contrast, the saved matching of \(B(C_0)\) has size 15, equal to \(|C_0|\); hence \(d(C_0)=0\). All matching edges and both covers are in the JSON certificate.

At this board \(\delta_0=I_0+P_0=0\), so the audited axis-avoiding theorem guarantees that a critical subset of \(U\) touches the vertical axis. Thus this is an exact obstruction to the unrestricted claim that vertical-touching positive sets may always be filled to their entire color class without decreasing deficiency. A restricted theorem for a winning adjusted phase is different and is not disproved here.

#### The canonical incidence graph and three boundary matchings

There is a valid additional representation, suggested by the coordinator, which uses maximum deficiency rather than criticality. Fix \(j\), let \(D_j=\max_{U\subset C_j}d(U)>0\), choose an inclusion-minimal maximizer \(U\), and let \(W\) be a minimum cover of \(B(U)\). Form the bipartite incidence graph \(H\) on owners \(U\) and selected vertices \(W\), joining an owner to a selected vertex when the vertex is on one of its available owned edges.

For nonempty \(S\subset W\), put \(T=N_H(S)\). Since \(W\setminus S\) covers \(B(U\setminus T)\),

\[
d(U\setminus T)\ge D_j+|S|-|T|.
\]

If \(|T|<|S|\), this contradicts maximality of \(D_j\). Equality contradicts inclusion-minimality of \(U\). In the empty-remainder case, \(|T|=|U|>|W|\ge|S|\) because \(D_j>0\). Thus \(|N_H(S)|\ge|S|+1\), and Hall's criterion gives a matching saturating \(W\).

Three partial matchings of \(H\) can be extended to such a matching:

1. The north edges of the nonhorizontal owners have disjoint endpoints. Choosing a \(W\)-endpoint on each yields a matching saturating all nonhorizontal owners.
2. The rooted edges of all owners \(u\le t/3\) also have disjoint endpoints and give a matching saturating these low owners.
3. Let \(A\) be the nonvertical owners, excluding the unique exceptional horizontal root if its color is \(j\). For every \(A'\subset A\), the axis-avoiding theorem and exclusion of that root give \(\nu(B(A'))\ge|A'|\). The set \(N_H(A')\) covers \(B(A')\), so \(|N_H(A')|\ge|A'|\). Hall's criterion gives a matching saturating \(A\).

Ordinary augmenting paths increase the size of a partial matching without unmatching any previously matched owner. Since a \(W\)-saturating matching exists, each of these partial matchings can be extended to one. The \(D_j=|U|-|W|\) unmatched owners of the three resulting matchings lie respectively on the horizontal axis, in the outer band \(u>t/3\), and on the vertical axis together with the possible exceptional root.

The graph \(H\) is planar: it is a subgraph of the nearest-neighbor triangular lattice, equivalently drawn by center-to-corner segments in the same-color honeycomb faces. In the union of the three matchings, each connected component has exactly
\[
|U_{\rm comp}|-|W_{\rm comp}|\ge0
\]
unmatched owners of **each** matching, since each matching saturates every selected vertex in that component. A positive component consequently contacts all three boundary sets. Isolated unmatched owners are included in this count.

This does not produce \(D_j\) disjoint tripods, and it is not a deficiency decomposition for arbitrary critical subsets. A component may contain several unmatched owners of each type, and unused third owners in an independent choice of neighborhood pairs can couple putative forest components. No planar-web theorem converting this representation to the needed adjusted color comparison has been established here.

#### A sufficient global collision statement

Let \(M=\min_j(K_j-\delta_j)\). If a cover \(F\) had size less than \(M\), its omitted sets \(U_j=C_j\setminus F\) would satisfy

\[
d(U_j)\ge K_j-|F|>\delta_j.
\]

Remove the unique exceptional horizontal root from its color, if there is one. Removing one owner decreases deficiency by at most one, since matching number cannot increase. Each color still has a positive subset and hence a critical subset \(V_j\). The axis-avoiding theorem makes these \(V_j\) vertical-touching, and their union is corner-free because it lies outside \(F\).

Therefore it would suffice to rule out three such critical sets, one of each color, whose union is corner-free and which avoid the exceptional root. The chains above give genuine local collision tests:

- If a critical set has \(s\ge1\), then it contains \(6x\). If the two other sets contain the horizontal roots \(2x,4x\), their union contains the corner \(\{2x,4x,6x\}\).
- If it has \(r\ge1\) and \(y\le t/3\), it contains \(6y\). If the other sets contain the vertical roots \(3y,9y\), their union contains \(\{3y,6y,9y\}\).

These conditions resolve the motivating weak \(t=729\) pattern once the missing forced labels are inserted. They do not show that arbitrary least-root exponents necessarily align in either pattern. Their residues alone do not imply consecutive horizontal or vertical roots.

### Gaps

The exact missing statement remains a winning-phase inequality, an existential complete vertical phase for a minimum cover, or the strengthened three-critical collision theorem just formulated. The established two-cone inclusion and forced chains do not prove any of these. No full candidate global proof emerged, and no claim of completion of step 6 or of irrationality is made. The new contribution is (V1)–(V10), the resolved finite high cases, and explicit obstructions that a successful global argument must avoid.
