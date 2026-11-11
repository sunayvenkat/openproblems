# Independent vertical audit and six-shell boundary dominance

Research round, 7 November 2026. The source-first audit below independently reconstructs V1–V10 and their exceptions. It also proves the subsequent exclusion of the deep branch when both root coordinates are positive. That exclusion strengthens the earlier note; it does not establish the global formula (C). The final section records the exact boundary statistic used in the continuing transfer investigation. No earlier folder is edited and no Lean work is used.

## Do V1–V10 and the exceptional endpoint cases survive independent derivation?

### Takeaway

Yes. The two-cone inclusion, root balance, meeting chains, vertical-strip dichotomy, and high-case reductions have no local gap in this reconstruction. The origin, the zero coordinates r or s, and the small vertical patch must retain their stated exceptions. The original deep branch is further restricted by the separate proof in the next section.

### Cited Findings

- The exact statements under audit, including the high-case table and the longer small-patch interval, are in [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>).
- The established inputs are the axis-avoiding classification, complete incidence lists, essential-cover property, and strict deletion inequality in [combinatorial_and_coefficient_audit.md](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>). The present audit independently checks their use when vertical owners are present.
- The source checker tests every proper subset, rather than just one-point deletions, in each named finite critical example. Its source was read in this audit. [Checker](<../global-boundary-proof/vertical_critical_check.py>), [saved certificates](<../global-boundary-proof/vertical_critical_check.json>).

### Inferences

#### Definitions and the exact input from criticality

Write \(D_t=\{2^a3^b\le t:a,b\ge0\}\) and color by \(a-b\pmod3\). For a fixed-color owner set \(U\), its possible edges are

\[
N(u)=(u/3,2u/3),\quad E(u)=(3u/2,u/2),\quad R(u)=(2u,3u).
\]

They exist respectively when \(b(u)\ge1\), when \(a(u)\ge1\) and \(3u/2\le t\), and when \(3u\le t\). At a left vertex \(l\), the possible owners are \(l/2,2l/3,3l\); at a right vertex \(v\), they are \(v/3,3v/2,2v\). These lists are complete, with availability imposed separately.

For an inclusion-minimal positive-deficiency set \(U\), a minimum cover \(W\) of \(B(U)\) has size \(|U|-1\). Each member of \(W\) uniquely covers edges from at least two distinct owners. For every nonempty \(S\subset W\), let \(T(S)\) include owners of all edges incident to \(S\), including doubly covered edges. Then

\[
|T(S)|\ge|S|+1. \tag{A1}
\]

Indeed, \(W\setminus S\) covers \(B(U\setminus T(S))\). If \(T(S)\ne U\) and \(|T(S)|\le|S|\), this proper subset has deficiency at least one. If \(T(S)=U\), then \(|T(S)|=|W|+1>|S|\) directly. Nothing in this argument demands axis avoidance. A leaf cannot belong to \(W\), because it cannot uniquely support two owners.

#### V1 and V2: the union of two cones is an inclusion

The north edges of nonhorizontal owners are pairwise disjoint. Positive deficiency therefore forces a horizontal owner. At an owner \(u\) with both ordinary exponents positive, the predecessor proof uses no axis restriction on other owners: if none of \(u/6,2u/9,3u/4\) belongs to \(U\), the north-left endpoint is a leaf, forcing its right endpoint and then \(E(4u/3)\) uniquely. This gives \(2u\notin W\) and makes \(E(u)\) available. Its right endpoint is likewise a leaf, forcing its left endpoint and then \(N(9u/2)\) uniquely. Thus \(3u\notin W\), while \(9u/2\in U\) makes \(R(u)\) available. Both endpoints of that edge are outside \(W\), a contradiction.

Following these numerically decreasing predecessors terminates on an axis. Let \(x=2^A,y=3^B\) be the least horizontal and vertical owners. All other horizontal roots are \(x8^k\), and all vertical roots are \(y27^k\), with \(k\ge0\). Put \(g=4/3,q=9/2\); then \(gq=6,g^2q=8,gq^2=27\). Reversing predecessors proves

\[
U\subset x\langle g,q\rangle_{\ge0}\ \cup\ y\langle g,q\rangle_{\ge0}. \tag{A2}
\]

This does not force any absent forward neighbor into \(U\). Equality of \(g^m q^n\) expressions is equality of their exponent pairs, since the exponent matrix has determinant three. Equal color gives \(A+B\equiv0\pmod3\), and solving the exponent equations yields

\[
y=xg^{(B-2A)/3}q^{(2B-A)/3}. \tag{A3}
\]

These observations justify excluding off-chain owners by excluding a coordinate pair from both cones.

#### V3: both root-balance inequalities are valid

If the origin belongs to \(U\), both least roots equal one. Otherwise \(A,B\ge1\). Suppose first \(A>2B\). The x-cone is contained in the y-cone, because the coordinates of x relative to y are \(((2A-B)/3,(A-2B)/3)\), both nonnegative. For \(v_m=yg^m\), \(0\le m<B\), the alternative owners at the left endpoint of \(N(v_m)\) have q-coordinate \(-1\), outside the common cone. That endpoint is a leaf. Its selected opposite endpoint forces \(E(gv_m)\) uniquely, so \(v_{m+1}\in U\). If this edge were unavailable, essentiality itself would fail; there is no permitted early cutoff termination. The chain reaches \(yg^B=2^{2B}\), contradicting minimality of \(2^A\).

Suppose instead \(B>2A\). Both cones lie in the x-cone. The usual horizontal q-chain starts at x. It cannot reach \(xq^A=3^{2A}\), a smaller vertical root than y. If x is isolated, criticality already contradicts a vertical owner. Otherwise the chain terminates numerically at \(u_k=xq^k\), with \(k<A\) and \(2t/3<u_k\le t\). All labels in the three-strip argument have first exponent at least \(A-k\ge1\); thus the argument remains available, even though some other owners of U are vertical. It leaves only the isolate or the three-label patch, both wholly axis-avoiding, or a contradiction for \(k\ge2\). Criticality makes the surviving positive subset the whole U, contradicting the vertical hypothesis. Therefore

\[
A/2\le B\le2A. \tag{A4}
\]

#### V4–V7: forced chains and the first horizontal strip

Set

\[
r=(2A-B)/3,\quad s=(2B-A)/3,
\quad A=2r+s,\quad B=r+2s,
\quad z=xq^s=yg^r=2^{2r}3^{2s}. \tag{A5}
\]

Assume \(r\ge1\), permitting \(s=0\). At \(v_m=yg^m\), \(0\le m<r\), the north-left alternatives have x-coordinates \((m-r-1,s-1)\), \((m-r,s-1)\). Their first coordinate excludes the x-cone; their second excludes the y-cone. The north-left endpoint is consequently a leaf. Essentiality at \(2v_m/3\in W\) forces \(E(v_{m+1})\) uniquely, giving \(2v_m\notin W\), \(v_{m+1}\in U\), and \(2v_m\le t\). At the final step this is \(3z/2\le t\), so

\[
z\le2t/3. \tag{A6}
\]

For \(u_n=xq^n\), \(0\le n<s\), the east-right alternative owners have coordinates \((-1,n-1),(-1,n)\). They are outside both cones. The east edge exists: \(a(u_n)=2r+s-n>0\), and \(u_n\le z\le2t/3\). Thus \(L_n=3u_n/2\in W\), \(u_{n+1}\in U\), and \(3u_n\notin W\). Since \(u_n\le z/q\le4t/27\), its rooted edge also exists and \(A_n=2u_n\in W\).

For \(s\ge1\), these are \(2s\) distinct selected left vertices. Their possible owners are exactly contained in

\[
\{u_0,\ldots,u_s\}\cup\{gu_1,\ldots,gu_s\}. \tag{A7}
\]

The formal owner \(gu_0=gx\) is nonsmooth, having b-exponent \(-1\). The list has \(2s+1\) members, so (A1) forces all to occur. Distinctness follows after division by \(2x\): L and A have g-coordinates \(-1,0\), respectively. This proves V7 without an uncounted extra owner from the second cone.

When \(r=0\), there is no vertical chain and no deduction (A6). Instead \(s=A\ge1\), \(y=xq^s\), and every horizontal preterminal label is at most \(y/q\le2t/9\). That directly supplies both its east and rooted edges, so the same chain and first-strip proof work. If \(y>2t/3\), the usual upper cap excludes \(s\ge2\), and \(s=1\) leaves \(\{2,9,12\}\). The argument never uses a positive-length horizontal chain when \(s=0\).

#### V8: the vertical-strip count and its high alternative

For \(r\ge1\), all \(\beta_m=2v_m/3\), \(0\le m<r\), are selected. If \(v_m\le t/3\), then \(R(v_m)\) and the known exclusion of \(2v_m\) force \(D_m=3v_m\in W\). The available indices, if nonempty, are \(0,\ldots,h\).

Select the r vertices \(\beta_m\) and the \(h+1\) vertices \(D_m\). The first group has possible owners only \(v_0,\ldots,v_r\). Indeed its third possibility \(v_m/q\) is excluded by both cones. The second group adds only \(qyg^m\), \(1\le m\le h+1\); \(qy\) is nonsmooth. Both groups are internally and mutually distinct: after division by \(3y\), their coordinate forms are \(q^{-1}g^m\) and \(g^m\). Thus \(r+h+1\) selected vertices have at most \(r+h+2\) possible owners. Strict expansion forces every listed owner, including

\[
qyg^{h+1}=6v_h\in U.
\]

Hence \(v_h\le t/6\). If \(h<r-1\), the next label \(v_{h+1}=gv_h\le2t/9<t/3\) would also have its rooted edge, a contradiction. Therefore \(h=r-1\), \(qz\in U\), and \(z\le2t/9\). The same list includes \(qyg=6y\).

If the rooted-edge index set is empty, \(y>t/3\). By (A6), \(g^r=z/y<2\), so \(r\in\{1,2\}\). The strict inequality matters: \((4/3)^3>2\). This proves V8 exactly as stated, with its standing assumption \(r\ge1\).

#### V9–V10: why the three-strip contradiction still applies

The high-case reuse of the horizontal strip argument does not require that z itself terminate an east chain. What it needs is the already forced L/A strip, \(gu_n\in U\) for \(1\le n\le s\), a cap \(g^2z>t\), and availability of the lower rooted edges.

For clarity, write \(v_n=gu_n,w_n=g^2u_n,z_n=g^3u_n\) in this paragraph only. The selected \(N(v_n)\)-left endpoint is \(A_{n-1}\). If \(2v_n/3\) were selected, this north edge would be doubly covered, so essentiality would force both other owners, including \(w_n\), uniquely. At \(n=s\), \(w_s>t\) rules this out. For smaller n, the rooted edge of \(v_n\) propagates such a selection to the next index; backward induction excludes every \(2v_n/3\). It forces \(2v_n\in W\), \(1\le n<s\). The resulting \(3s-1\) selected vertices have at most \(3s\) owners, forcing \(w_1,\ldots,w_{s-1}\).

All rooted edges of this second strip are available, because

\[
w_{s-1}=\frac{g^2}{q}z\le\frac{32}{81}\frac{2t}{3}=\frac{64t}{243}<t/3.
\]

The terminal right vertex \(3w_{s-1}=2w_s/3\) is a leaf: its other possible owners \(w_s,z_s\) are beyond t. The next backward induction excludes \(2w_n/3\), \(2\le n\le s\), and forces \(2w_n\in W\), \(1\le n<s\). At n=1 this uses the rooted edge, not a nonexistent north edge of the horizontal owner \(w_1\). The final \(4s-2\) selected vertices have at most \(4s-2\) owners, since \(z_1\) is nonsmooth and \(z_s>t\). This contradicts (A1). At \(s=2\), the last interior range is empty and the cap alone supplies the needed forced vertex; the contradiction is six owners versus at least seven. Selected-vertex g-coordinates \(-1,0,1,2\), after division by \(2x\), certify every cardinality.

In the high branch with \(r=2\), \(z=g^2y>16t/27\), hence \(g^2z>256t/243>t\). Therefore \(s\le1\). If \(r=1,s\ge1\), then \(z>4t/9\). If also \(z\le t/2\), the forced owner gz has its east edge. Its right endpoint \(2z/3=3u_{s-1}\) is outside W, forcing \(2z\in W\). The only other possible owners at \(2z\) are z and 6z; the z rooted edge is absent because \(z>t/3\), and 6z is beyond t. This selected vertex would support only one owner, impossible. Thus \(z>t/2\), proving V9. For \(s\ge2\), the preceding strip contradiction excludes \(g^2z>t\), proving

\[
r=1,\quad s\ge2,\quad t/2<z\le9t/16. \tag{A8}
\]

The upper endpoint is included because its cap owner is then on the board. Since \(z=4\cdot9^s\), the equivalent t-window is \([64\cdot9^{s-1},8\cdot9^s)\).

#### Finite high cases and the separate small patch

The cases \((r,s)=(1,0),(2,0),(2,1)\) have respectively the forced sets and intervals

\[
\{3,4\},\ [6,9);\qquad
\{9,12,16\},\ [24,27);\qquad
\{32,81,108,144,192\},\ [216,243).
\]

The intervals follow directly from \(3z/2\le t<3y\). At their left endpoints the required final east edge exists; at their upper endpoints a new rooted edge enters. Direct substitution in N/E/R confirms that the graphs stay constant on each stated half-open interval. Covers of sizes 1, 2, and 4 are respectively \(\{2\},\{6,8\},\{48,54,64,72\}\), matching the saved matching certificates. The proper-subset assertions are checked by the named exact certificate routine; this audit read that routine but did not rerun its subset enumeration.

At \((r,s)=(1,1)\), V9 sharpens the interval to \([54,72)\), with \(U=\{8,27,36,48\}\). Its graph is the union of paths \(4-12-24-16-32\) and \(9-18-54\). The cover \(\{12,16,18\}\) has size three; the next owned edge enters at t=72. The stated color comparisons on \([54,64)\) and \([64,72)\) account for the newly isolated 64 in the latter range.

For the high family at \(s=2,t=576\), the displayed cover of the seven-owner example hits every N/E/R edge. A size-six matching is
\((24,8),(32,64),(108,36),(144,288),(81,162),(192,384)\).
The first additional edge is \(E(432)\) at 648, so the graph is constant on \([576,648)\). Its criticality is the saved all-proper-subset certificate, not a general argument for every s.

Finally, \(\{2,9,12\}\) has the path \(1-3-6-4-8\) throughout \([12,18)\), covered by \(\{3,4\}\), with a size-two matching. Each singleton has an edge; each proper pair has two disjoint edges, so criticality follows directly. The east edge of owner 9 is permanently absent, and the first extra edge is \(E(12)\) at 18. Its critical interval really is longer than the sufficient construction window \([12,27/2)\). In that latter window it touches the vertical phase at 9, so the prescribed-phase optimum cannot be identified with the patched count for color one.

### Gaps

The audit finds no local failure in V1–V10, but these statements do not bound aggregate deficiency of arbitrary unions. The origin case has not been classified. The finite certificates certify only their specified owner sets. The companion forest and incidence representations do not make their components independent deficiency components. The next section supersedes one previously open branch by an additional strict-expansion argument.

## Can the deep branch contain two incomparable least roots?

### Takeaway

No. If \(r,s\ge1\), the low branch \(z\le2t/9\) is impossible. The horizontal and vertical forced strips meet in exactly one owner, and the two additional forced selected vertices add at most one owner, violating strict expansion. This is a new exclusion relative to the source V8, independently reconstructed here from its established chains.

### Cited Findings

- The input forced chains, first strip, and low-branch vertical strip are V4–V8 of [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>), independently audited in the preceding section.
- The crucial expansion is the all-incident-owner inequality (A1), whose double-coverage scope is proved above and in the [earlier independent audit](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>).

### Inferences

Assume for contradiction \(r,s\ge1\) and \(z\le2t/9\). Write \(u_n=xq^n\), \(v_m=yg^m\). The forced horizontal selected set is

\[
S_h=\{3u_n/2,2u_n:0\le n<s\},\qquad |S_h|=2s,
\]

all on the left physical color. Its entire possible owner set is

\[
H=\{u_n:0\le n\le s\}\cup\{gu_n:1\le n\le s\},\qquad |H|=2s+1.
\]

The low branch makes every \(R(v_m)\), \(0\le m<r\), available and forces

\[
S_v=\{2v_m/3,3v_m:0\le m<r\},\qquad |S_v|=2r,
\]

all on the right physical color. Its entire possible owner set is

\[
V=\{v_m:0\le m\le r\}\cup\{qv_m:1\le m\le r\},\qquad |V|=2r+1.
\]

In coordinates \(xg^a q^b\), these are

\[
\begin{aligned}
H&=\{(0,n):0\le n\le s\}\cup\{(1,n):1\le n\le s\},\\
V&=\{(m,s):-r\le m\le0\}\cup\{(m,s+1):1-r\le m\le0\}.
\end{aligned}
\]

Thus \(H\cap V=\{(0,s)\}=\{z\}\), exactly. In particular \(gz\in H\subset U\) and \(qz\in V\subset U\). These are actual forced owners, not merely coordinate possibilities.

The edge \(E(gz)=(2z,2z/3)\) exists: \(a(gz)=2r+2>0\) and \(2z\le4t/9<t\). The last horizontal step excludes

\[
2z/3=3u_{s-1}
\]

from W. Therefore \(2z\in W\). The edge \(N(qz)=(3z/2,3z)\) exists because qz is a board owner with positive b-exponent. The last vertical step excludes

\[
3z/2=2v_{r-1}
\]

from W, so \(3z\in W\).

These selected vertices are new. After dividing horizontal selected vertices by \(2x\), their forms are \(g^{-1}q^n\) or \(q^n\), with \(n<s\); \(2z/(2x)=q^s\) is neither. After dividing vertical selected vertices by \(3y\), their forms are \(q^{-1}g^m\) or \(g^m\), with \(m<r\); \(3z/(3y)=g^r\) is neither. Opposite physical colors exclude all other cross coincidences.

At \(2z\) the only possible owners are \(z,gz,6z\); at \(3z\) they are \(z,qz,6z\). Consequently for

\[
S=S_h\cup S_v\cup\{2z,3z\}
\]

we have

\[
|S|=2r+2s+2,
\qquad T(S)\subset H\cup V\cup\{6z\},
\qquad |T(S)|\le2r+2s+2.
\]

If 6z or one of its edges is unavailable, the owner count only decreases. The rooted edge \(R(z)\) is indeed doubly covered by \(2z,3z\); this does not weaken the contradiction because (A1) counts all incident owners, not only uniquely hit ones. We have contradicted (A1).

Therefore an origin-free critical set with \(r,s\ge1\) cannot lie in the deep branch. Combining this with the audited high reductions leaves only \((r,s)=(2,1)\), \((1,1)\), or the still-unbounded family

\[
r=1,\quad s\ge2,\quad t/2<z\le9t/16.
\]

The comparable-root cases \(r=0\) or \(s=0\) are not covered by the contradiction: one selected strip is then empty and the necessary last-step exclusion is absent. No conclusion about those cases is inferred by continuity or by inserting an empty range.

### Gaps

This excludes a whole family of critical sets, but still does not compare arbitrary vertical-touching unions in a minimizing adjusted color. The high family, the comparable-root cases, and the origin require further work. No numerical check is needed for the coordinate-count contradiction itself.

## What boundary statistic does the six-shell transfer actually require?

### Takeaway

For one fixed inner cover, the exact extension cost is a zero-run statistic of its two axis words. The origin coupling can be absorbed into one mandatory edge of a single path. This gives an explicit min-plus boundary potential to investigate, but no dominance theorem closing it under repeated shells has yet been proved.

### Cited Findings

- The exact decomposition over all inner covers and the two conditioned path problems are proved in [boundary_calibration.md](<../global-boundary-proof/boundary_calibration.md>). The present derivation simplifies their extension functional; it does not restrict the inner optimization to minimum covers.
- The known local LP-cut family fails its uniform ceiling claim by the [exact 534-vertex certificate](<../global-boundary-proof/calibration_cap_probe.json>). No new cut trials are performed here.

### Inferences

Put \(T=t/6\) and fix any cover G of \(D_T\). Let \(h=\lfloor\log_2T\rfloor\), \(b=\lfloor\log_3T\rfloor\), and \(B=\lfloor\log_3t\rfloor\). Define the inner bit words

\[
w_H=(1_G(2^a))_{a=0}^{h},\qquad
w_V=(1_G(3^a))_{a=0}^{B-2}.
\]

The horizontal word is the complete inner horizontal axis, since \(\lfloor\log_2(t/3)\rfloor=h+1\). The vertical word is either the complete inner vertical axis or its prefix omitting the last point, since \(B\in\{b+1,b+2\}\). An empty prefix is allowed: for \(6\le t<9\), B=1 and \(w_V\) is empty. Whenever it is nonempty, its first bit is the same inner-origin bit that starts \(w_H\).

On the outer horizontal and vertical axes, the required edges have indicators \(1-w_H\) and \(1-w_V\). The remaining corner is \(\{1,2,3\}\). In a minimum extension the outer origin need not be selected: replace a selected 1 by 2, or remove 1 if 2 is already selected. This preserves every corner because 1 participates only in this corner. Thus the origin condition can be replaced, at no cost in the minimum, by the required edge \(\{2,3\}\) joining the two axis paths.

For a finite binary word w, define

\[
R(w)=\sum_{\text{maximal zero runs }J\text{ of }w}\left\lceil\frac{|J|}{2}\right\rceil.
\]

A run of k required edges in a path has minimum vertex-cover size \(\lceil k/2\rceil\). Components separated by absent edges have disjoint vertex sets. Unconstrained terminal horizontal vertices cost zero. The exact extension cost is therefore

\[
\boxed{\mathcal E_t(G)=R\bigl(\operatorname{rev}(w_H)\,0\,w_V\bigr).} \tag{T1}
\]

Equivalently, if \(\ell_H,\ell_V\) are the initial zero-run lengths of the two words, including length zero, then

\[
\boxed{\mathcal E_t(G)=R(w_H)+R(w_V)
+\mathbf1_{\ell_H\equiv\ell_V\equiv0\pmod2}.} \tag{T2}
\]

Indeed the only affected zero runs merge into a run of length \(\ell_H+1+\ell_V\). Subtracting \(\lceil\ell_H/2\rceil+\lceil\ell_V/2\rceil\) from its rounded half gives exactly the displayed indicator. Thus the origin coupling has not been dropped.

The global identity remains

\[
\tau(t)=\min_{G\text{ covers }D_{t/6}}
\left[|G|+R\bigl(\operatorname{rev}(w_H)\,0\,w_V\bigr)\right]. \tag{T3}
\]

For this one extension, the two run costs and two initial parities suffice to evaluate the boundary term. This is not yet a closed state description for the distribution of attainable outer words, which becomes relevant at the next shell. The missing implication is a lower bound for the total cost of every inner cover with each such boundary statistic, strong enough to survive the next transfer.

#### The evaluated one-step signature is not a closed state

The natural first candidate was the tuple
\((|G|,R(w_H),R(w_V),\ell_H\bmod2,\ell_V\bmod2)\).
It determines (T2) exactly, but does not determine the best result after another shell. On \(D_4\), both \(G=\{2\}\) and \(G=\{3\}\) are covers. For extension to \(D_{24}\), their horizontal words are 010 and 000, and their common required vertical word is 0. Both signatures are \((1,2,1,1,1)\), with one-shell total four. Yet the optimal totals after two shells, through \(D_{24}\) to \(D_{144}\), are seven and eight, respectively. The middle witnesses are \(\{2,9,12,16\}\) and \(\{2,8,9,18\}\).

These conditional minima were checked exactly by enumerating only the 128 outer-axis choices for each of these two fixed covers, retaining every valid extension, not merely minimum intermediate covers. [Exact checker](<transfer_signature_check.py>), [saved results](<transfer_signature_check.json>). This is a counterexample to this specific state closure, not to (C).

#### Even complete endpoint matrices and color counts do not close

A more informative proposed state retains the full min-plus endpoint response on each path. If w has m bits, define

\[
M(w)_{p,q}=\min\left\{\sum_{i=1}^{m}v_i:
v_0=p,\ v_m=q,\ w_i+v_{i-1}+v_i\ge1\ (1\le i\le m)\right\}.
\]

With min-plus matrix multiplication,

\[
M(w)=M_{w_1}\cdots M_{w_m},\qquad
M_0=\begin{pmatrix}\infty&1\\0&1\end{pmatrix},\quad
M_1=\begin{pmatrix}0&1\\0&1\end{pmatrix}. \tag{T4}
\]

This is an exact finite-state compression for concatenating a word within one path. In fact, after subtracting the smallest finite entry there are only eight possible matrices. If w contains a 1, write its leading and trailing zero lengths as a,b. Since \(M_1\) has min-plus rank one, its normalized product is

\[
\begin{pmatrix}p&p+q\\0&q\end{pmatrix},\qquad
p=a\bmod2,\quad q=1-(b\bmod2).
\]

The remaining possibilities are the empty-word identity, the one-letter \(M_0\), and the two alternating normalized products for all-zero lengths at least two. This finite concatenation property does not imply closure under shell extension, which chooses new words.

Here is an actual-board counterexample even after adding all three color counts to this matrix state. On \(D_{64}\), set

\[
\begin{aligned}
G_A&=\{3,6,8,9,12,18,24,36,48,54\},\\
G_B&=\{2,3,6,8,9,12,24,32,36,48\}.
\end{aligned}
\]

Both cover every corner, both have size ten, and both have color counts \((4,3,3)\). Their horizontal words are
\(w_A=0001000\), \(w_B=0101010\); their common required vertical word for \(D_{384}\) is \(w_V=0110\). Direct multiplication gives

\[
M(w_A)=M(w_B)=\begin{pmatrix}4&4\\3&3\end{pmatrix},\qquad
M(w_V)=\begin{pmatrix}2&2\\1&1\end{pmatrix}.
\]

Both one-shell totals are sixteen. Nevertheless, their exact best totals through \(D_{384}\) to \(D_{2304}\) are respectively **22 and 21**. The following short response calculation proves this without relying on a large search.

For an inner path word w, define

\[
J_w(s)=\min\left\{|v|+R(v):v_1=s,\ |v|\text{ here counts 1's},
\ w_i+v_i+v_{i+1}\ge1\right\},
\]

where the binary word v has length one more than w. For the three specified words,

\[
(J_{w_A}(0),J_{w_A}(1))=(7,7),\quad
(J_{w_B}(0),J_{w_B}(1))=(7,6),\quad
(J_{w_V}(0),J_{w_V}(1))=(4,4). \tag{T5}
\]

For \(w_A\), the inequality proved just below gives \(|v|+R(v)\ge8-1=7\). Witnesses 01100110 and 10100101 attain seven with each first bit. For \(w_B\), four disjoint required edges force at least four selected vertices. A cost of six is attained by 10011001. If the first bit is zero, its initial zero run has length one, so at four selected vertices the remaining three zeros need at least two more run units; this gives cost at least seven. At five or more selected vertices the same lower bound persists. The word 01100110 attains seven. For \(w_V\), the two disjoint end edges force two selections; three remaining zero positions cost at least two run units. Words 01001 and 10010 attain four with each first bit.

On these actual boards the second extension reads all middle horizontal and vertical bits. Both first required edges are present, so a first zero bit is followed by a one. If their first bits are h,v, minimizing the middle origin selection contributes exactly \(1+\mathbf1_{h=v}\) in addition to the two J responses. To check this, an unselected origin requires \(h\lor v\); (T2) gives coupling one for opposite first bits and two for two ones. A selected origin instead contributes two in total and permits two zeros. Thus the two-shell minima are

\[
10+\min_{h,v\in\{0,1\}}\bigl(J_{w_A}(h)+J_{w_V}(v)+1+\mathbf1_{h=v}\bigr)=22,
\]
\[
10+\min_{h,v\in\{0,1\}}\bigl(J_{w_B}(h)+J_{w_V}(v)+1+\mathbf1_{h=v}\bigr)=21.
\]

For explicit witnesses, use the middle covers

\[
6G_A\cup\{3,4,8,64,81,128\},\qquad
6G_B\cup\{2,9,16,32,243,256\}.
\]

Each has size sixteen; their next extension costs are six and five. The checker independently confirms corner coverage, color counts, matrices, and the three short conditional response tables by enumerating only length-eight and length-five path words. [Checker and exact assertions](<transfer_signature_check.py>), [results](<transfer_signature_check.json>).

Thus size, the three global phase intersection counts, and even both full one-step endpoint matrices are not a sufficient state for exact shell transfer. This does not refute every bounded-state dominance inequality, nor every possible three-phase potential. It identifies which evaluated responses cannot be used as a closed state.

#### A quantitative identity for a redesigned boundary potential

There is a useful exact identity that retains the lost position information. Let w have m bits and v have m+1 bits, with \(w_i+v_i+v_{i+1}\ge1\). Let e be the number of indices with \(w_i=1\) but \((v_i,v_{i+1})\ne(0,0)\). Let \(\ell_1,\ldots,\ell_k\) be the nonempty zero-run lengths of v. Then

\[
\boxed{|w|+|v|+R(v)=m+1+
e+\sum_{j=1}^k\left(\left\lceil\ell_j/2\right\rceil-1\right).} \tag{T6}
\]

Here \(|w|,|v|\) mean the numbers of selected bits. Indeed every adjacent 00 pair of v requires the corresponding w-bit to be one, so
\(|w|=e+\sum_j(\ell_j-1)\).
Adding \(|v|+R(v)\), and using \(|v|+\sum_j\ell_j=m+1\), proves (T6). Its defect term is nonnegative. Equality holds precisely when w is the indicator of adjacent 00 pairs in v and every zero run of v has length at most two. This is a proved boundary energy identity, not an assumption of periodicity.

The next response \(J_w\) is therefore naturally position-sensitive. It has an exact three-state weighted automaton: state A means the last v-bit is one; B means the current zero run has odd length; C means it has positive even length. Appending a one costs one and goes to A. Appending a zero from A costs one and goes to B; from B it costs zero and goes to C; from C it costs one and goes to B. When the corresponding w-bit is zero, the B-to-C and C-to-B moves are forbidden by the cover constraint. Initialize the first bit with cost one in either state A or B. This counts \(|v|+R(v)\) exactly and preserves the location of each required edge.

This is the appropriate immediate redesign after the two-state failure: use the conditioned three-state response before attempting any further quotient, and keep the nonnegative defect in (T6). No claim is made that its products, or the attainable inner-cover costs associated with them, collapse to three phase costs and a bounded defect state under arbitrarily many shells.

### Gaps

No closed global dominance invariant has been established. The actual board cutoffs and empty-prefix cases are retained throughout; the two counterexamples are genuine smooth caps, not arbitrary substituted shapes. A successful invariant must bound all inner covers, retain enough phase and position information to survive repeated extension, and ultimately control arbitrary vertical-touching unions. The strict expansion exclusion of the deep incomparable branch is proved separately above and does not depend on these still-incomplete transfer ideas. No further word or board sweep was performed.
