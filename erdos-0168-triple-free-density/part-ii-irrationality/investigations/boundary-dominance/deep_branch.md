# Exclusion of the deep branch with two incomparable axis roots

Research derivation, 7 November 2026. This proves that a positive critical owner set with two incomparable least axis roots cannot have its forced meeting point at or below \(2t/9\). The argument is a strict owner-neighborhood count, with no filling, submodularity, or independent-component premise. It does not establish the global finite optimum.

## What is the precise statement and its scope?

### Takeaway

Let a critical set have least horizontal root \(x=2^A\) and least vertical root \(y=3^B\), with \(A/2<B<2A\). Put \(r=(2A-B)/3\), \(s=(2B-A)/3\), and \(z=2^{2r}3^{2s}\). Then \(z\le2t/9\) is impossible. Combined with the previously derived vertical-strip dichotomy, this forces \(y>t/3\). [Earlier two-cone derivation](<../global-boundary-proof/vertical_critical.md>).

### Cited Findings

- For a critical \(U\), a minimum vertex cover \(W\) of \(B(U)\) has the essential-cover property and the strict inequality \(|N_W(S)|\ge|S|+1\), where \(N_W(S)\) means all owners of available edges incident with \(S\subset W\). [Independent audit](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>).
- The same strict inequality and essentiality hold for an inclusion-minimal maximum-deficiency set, even when its deficiency exceeds one. [Canonical repair proof](<../global-boundary-proof/canonical_phase.md>).

### Inferences

Here \(D_t=\{2^a3^b\le t:a,b\ge0\}\), the owner color is \(a-b\pmod3\), and
\[
N(u)=(u/3,2u/3),\quad E(u)=(3u/2,u/2),\quad R(u)=(2u,3u).
\]
These edges require respectively \(b\ge1\); \(a\ge1,3u\le2t\); and \(3u\le t\).

The proof below actually needs only the following hypotheses:

1. \(U\) is one color, \(W\) covers \(B(U)\), every \(w\in W\) uniquely covers at least two distinct owners, and every nonempty \(S\subset W\) satisfies \(|N_W(S)|\ge|S|+1\).
2. \(x,y\in U\) are its least horizontal and vertical roots, \(r,s\) are positive integers, and
\[
g=4/3,\quad q=9/2,\quad x=2^{2r+s},\quad y=3^{r+2s},\quad
y=xg^{-r}q^s.
\]
3. Every owner lies in the union of the two nonnegative \((g,q)\)-cones based at \(x\) and \(y\).

For a critical set these hypotheses follow from the audited owner lists and predecessor argument: each interior owner has one of \(u/6,2u/9,3u/4\) as a predecessor; descending chains end on an axis; roots of one color differ by powers of \(8=g^2q\) or \(27=gq^2\). That derivation applies without assuming the rest of the set avoids the vertical axis.

Set
\[
u_n=xq^n\ (0\le n\le s),\qquad
v_m=yg^m\ (0\le m\le r),\qquad
u_s=v_r=z.
\]
The contradiction below assumes \(z\le2t/9\). Both \(r,s\ge1\) are essential: neither the origin case nor a degenerate one-chain case is included.

### Gaps

This statement does not exclude the high branch or either degenerate case \(r=0\) or \(s=0\). It is not a statement about an arbitrary set merely contained in two cones; the cover and strict expansion hypotheses are required.

## Why do the two selected strips force a contradiction?

### Takeaway

The horizontal and vertical strips have one more possible owner than selected vertices. Their owner lists overlap only at \(z\). Two further selected vertices at the meeting point can add at most one further owner, contradicting strict expansion.

### Cited Findings

The complete endpoint owner lists are:
\[
l:\ l/2,\ 2l/3,\ 3l;\qquad
r':\ r'/3,\ 3r'/2,\ 2r'.
\]
They are derived and audited in [the incidence audit](<../global-boundary-proof/combinatorial_and_coefficient_audit.md>). All counts below use these full lists, not only uniquely covered edges.

### Inferences

#### Forced chains and endpoint orientations

For \(m<r\), the alternative owners at the left endpoint of \(N(v_m)\) are \(v_m/6\) and \(2v_m/9\). In coordinates based at \(x\), they have second coordinate \(s-1\) and negative first coordinate, so they lie outside both cones. The left endpoint is a leaf; hence \(2v_m/3\in W\). Essentiality forces \(E(v_{m+1})\) uniquely, with
\[
v_{m+1}\in U,\qquad 2v_m\notin W.
\]
This forces the vertical chain to \(z\), and its last step gives
\[
3z/2=2v_{r-1}\notin W. \tag{D1}
\]

For \(n<s\), the alternative owners at the right endpoint of \(E(u_n)\) are \(u_n/6\) and \(3u_n/4\). Their \(g\)-coordinate is \(-1\), and their \(q\)-coordinate is below \(s\), so neither is in either cone. The east edge is available: \(a(u_n)=2r+s-n>0\) and \(u_n\le z\le2t/9\). Its right endpoint is a leaf; hence \(3u_n/2\in W\). Essentiality forces \(N(u_{n+1})\) uniquely, giving
\[
u_{n+1}\in U,\qquad 3u_n\notin W.
\]
The last step yields
\[
2z/3=3u_{s-1}\notin W. \tag{D2}
\]

#### The horizontal selected set

Every \(R(u_n)\), \(n<s\), is available, since \(u_n\le z/q\le4t/81<t/3\). Its right endpoint is outside \(W\), so \(2u_n\in W\). Define
\[
S_h=\{3u_n/2,2u_n:0\le n<s\}.
\]
These are \(2s\) distinct left vertices. Their full owner neighborhood is contained in
\[
\mathcal H=\{u_0,\ldots,u_s\}\cup\{gu_1,\ldots,gu_s\},\qquad |\mathcal H|=2s+1. \tag{D3}
\]
At \(3u_n/2\), the additional possible owner \(3u_n/4\) is excluded by the two cones; at \(2u_n\), the list is \(u_n,gu_n,gu_{n+1}\). The expression \(gu_0=gx\) has negative \(3\)-exponent. Strict expansion forces every owner in (D3), in particular \(gz\in U\).

#### The vertical selected set

Every \(R(v_m)\), \(m<r\), is available, since \(v_m\le z/g\le t/6<t/3\). Its left endpoint is outside \(W\), so \(3v_m\in W\). Define
\[
S_v=\{2v_m/3,3v_m:0\le m<r\}.
\]
These are \(2r\) distinct right vertices. Their full owner neighborhood is contained in
\[
\mathcal V=\{v_0,\ldots,v_r\}\cup\{qv_1,\ldots,qv_r\},\qquad |\mathcal V|=2r+1. \tag{D4}
\]
At \(2v_m/3\), the additional possible owner \(2v_m/9\) is excluded by the cones; at \(3v_m\), the list is \(v_m,qv_m,qv_{m+1}\). The expression \(qv_0=qy\) has negative \(2\)-exponent. Strict expansion forces every owner in (D4), in particular \(qz\in U\).

#### Exact overlap and the two new selected vertices

Using \((g,q)\)-coordinates based at \(x\), the four owner groups have coordinates
\[
\begin{array}{c|c}
\mathcal H\text{ first group}&(0,n),\ 0\le n\le s\\
\mathcal H\text{ second group}&(1,n),\ 1\le n\le s\\
\mathcal V\text{ first group}&(m-r,s),\ 0\le m\le r\\
\mathcal V\text{ second group}&(m-r,s+1),\ 1\le m\le r .
\end{array}
\]
Their only common point between \(\mathcal H\) and \(\mathcal V\) is \((0,s)=z\). Consequently
\[
|\mathcal H\cup\mathcal V|=2r+2s+1.
\]
The selected sets themselves are disjoint because they have different bipartition colors, and \(|S_h\cup S_v|=2r+2s\).

The owner \(gz\) has an available east edge, since its left endpoint is \(2z\le4t/9<t\). Its right endpoint is \(2z/3\notin W\), by (D2), so \(2z\in W\). The forced owner \(qz\) has an available north edge with left endpoint \(3z/2\notin W\), by (D1); hence \(3z\in W\).

These are two new selected vertices. The left vertex \(2z\) is neither \(2u_n\) with \(n<s\), nor \(3u_n/2\), by independence of \(g,q\). The corresponding argument separates the right vertex \(3z\) from all \(3v_m,2v_m/3\), \(m<r\). Left and right colors exclude all remaining coincidences.

Finally, the complete possible owner lists at these two vertices are
\[
2z:\ z,gz,6z;\qquad
3z:\ z,qz,6z.
\]
Only \(6z\) is new relative to \(\mathcal H\cup\mathcal V\); it may even be absent or unavailable, which only reduces the count. For
\[
S=S_h\cup S_v\cup\{2z,3z\}
\]
we therefore obtain
\[
|N_W(S)|\le (2r+2s+1)+1=2r+2s+2=|S|,
\]
contradicting strict expansion. This proves the deep-branch exclusion.

### Gaps

None was identified in this local counting argument. No assertion that \(6z\in U\), no closure of \(U\), and no decomposition of deficiency is needed. The availability and distinctness of every selected vertex, and the full neighborhood overlap, are explicit above.

## What does this change for the global problem?

### Takeaway

Every critical set with genuinely incomparable least axis roots has its vertical root in \((t/3,t]\). Hence such critical sets can occur in only one color at a fixed \(t\), since that interval contains only the largest pure power of three on the board. This still leaves degenerate and origin-containing critical sets in the other colors.

### Cited Findings

The previously proved vertical-strip dichotomy says that, for \(r\ge1\), either \(z\le2t/9\), or \(y>t/3\) and \(r\in\{1,2\}\). The high cases \(r=2\) and the remaining \(r=1\) window were derived with explicit qualifications in [vertical_critical.md](<../global-boundary-proof/vertical_critical.md>).

### Inferences

Combining that dichotomy with the present proof leaves only the high branch for \(r,s\ge1\). Its least vertical root is the unique pure power of three exceeding \(t/3\), so all incomparable-root critical sets share that root and its color. The remaining high family \(r=1,s\ge2\), with \(t/2<z\le9t/16\), is not excluded by this proof.

The count itself also applies to a canonical maximum-deficiency set whenever it has the stated two-cone and incomparable-root hypotheses. Thus its use is not restricted to deficiency one. A separate argument is still required to obtain those hypotheses for a restricted canonical maximizer after excluding an exceptional root; no independence of its forest components is being assumed.

### Gaps

The global inequality \(\max_U d(U)\le K_j-\min_\ell(K_\ell-\delta_\ell)\) is not proved here. Neither a three-critical collision theorem nor the required aggregate winning-phase bound follows merely because all incomparable-root obstructions use one vertical root. The cases \(r=0\), \(s=0\), and the origin remain separate, and the high branch must still be compared with the adjusted phase counts.
