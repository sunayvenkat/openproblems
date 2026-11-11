# Hole filling narrows the unresolved proof

**The main advance is a proved, independently reviewed hole-filling theorem for the matching problem behind Erdős #168(ii).** Filling omitted hexagonal faces cannot decrease matching deficiency and gives a stronger gain when the filled region has several holes. This reduces the finite optimization to disjoint simply connected components meeting specified boundaries. **No different currently open conjectures.io entry has been solved; the requested goal remains active.** The finite cover bound and the irrationality argument still have separate gaps. The report distinguishes these deductions from finite checks and makes no priority claim. ([Proof](<hole_filling.md>), [independent review](<hole_review.md>))

## The target still requires irrationality

Let \(F(N)\) be the largest size of a subset of \([1,N]\) avoiding every triple \(\{n,2n,3n\}\). The limit \(c=\lim F(N)/N\) exists; #168(ii) asks whether it is irrational. Its live page was rechecked on 7 November 2026 UTC, 6 November locally, and remained open. Kohlmeyer–Kruer's #1062 supplies a lower bound for nonzero linear forms in a **fixed number of S-units with fixed rational coefficients**; the inputs making that theorem useful must be established anew here. ([Target](https://conjectures.io/problems/erdos168-erdos-168-parts-ii), [#1062, §§6–7](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf))

Put \(S=\{2^a3^b:a,b\ge0\}\), \(D_t=\{(a,b)\ge0:2^a3^b\le t\}\), and \(K(t)=|D_t|\). Write \(\alpha(t)\) for the **local** maximum corner-free subset size and \(\tau(t)=K(t)-\alpha(t)\). Color vertices by \(j=a+2b\bmod3\), with class size \(K_j\). For \(t\ge3\), let \(I_j\) indicate an isolated power \(2^a\in(2t/3,t]\) of color \(j\); let \(P_j\) indicate the patch replacing \(\{2s,9s,12s\}\) by \(\{3s,4s\}\), where \(s=2^a\), \(12s\le t<27s/2\), and \(j\equiv a+1\pmod3\). The construction proves
\[
\tau(t)\le\min_j(K_j-I_j-P_j);
\]
**equality remains conjectural.** ([Component reduction](https://arxiv.org/html/2604.15515v1), [patch and matching reduction](<../open-conjecture-transfer-search/168_grid.md>))

## Hole filling removes every bounded complement component

For \(U\subseteq C_j\), form \(B(U)\) by joining the other two vertices of each corner whose color-\(j\) vertex lies in \(U\). Bipartite vertex-cover duality gives
\[
d(U)=|U|-\nu(B(U)),\qquad \tau(t)=K_j-\max_U d(U).
\]
Removing color \(j\) from the triangular lattice leaves a honeycomb; each label owns three alternating sides of its hexagon.

**Filling theorem.** Let \(V\), disjoint from \(U\), consist of \(m\) faces connected by shared sides. Require every face in \(V\) to have all three owned edges available, and every boundary edge owned outside \(V\) to belong already to \(B(U)\). If the union has \(h\) geometric holes, then
\[
\nu(B(U\cup V))-\nu(B(U))\le m-\lfloor h/2\rfloor,
\qquad d(U\cup V)\ge d(U)+\lfloor h/2\rfloor.
\]
In \(D_t\), availability means both exponents are positive and \(3u\le t\). These hypotheses exclude unjustified filling of truncated boundary faces. ([Full theorem and review](<hole_review.md>))

Here is the proof. At every boundary vertex, exactly one of its two boundary edges is owned outside \(V\), including at concave corners and hole boundaries. These old edges form a perfect boundary matching. Let \(I,B,E_{\rm int}\) count interior vertices, boundary vertices, and internal edges. Edge ownership and Euler's formula give
\[
3m=E_{\rm int}+B/2,\qquad I-E_{\rm int}+m=1-h,
\qquad I+B/2=2m+1-h.
\]
Take a maximum matching after filling and retain every edge outside the region's one-skeleton, including edges lying in holes. If \(b\) boundary vertices remain free, the discarded part has at most \(\lfloor(I+b)/2\rfloor\) edges. Removing occupied vertices from the old boundary matching leaves at least \(\max(0,b-B/2)\) compatible edges. Replacement therefore loses at most
\[
\left\lfloor\frac{I+b}{2}\right\rfloor-\max(0,b-B/2)
\le\left\lfloor\frac{I+B/2}{2}\right\rfloor
=m-\lfloor h/2\rfloor.
\]
This proves the theorem without assuming simple connectivity.

Every finite component \(V\) of the complement of \(U\) in the **full infinite face lattice** automatically qualifies. All its external neighboring faces belong to \(U\). At a minimum first exponent, the neighbor with step \((-2,1)\) forces \(a\ge2\); the step \((1,-2)\) similarly forces \(b\ge2\). At the largest label \(u\), the neighbor \(6u\in U\) forces \(u\le t/6\). Thus all omitted faces are safely interior. A maximum-deficiency set of largest cardinality consequently has connected full-plane complement.

Its face-connected components have vertex-disjoint matching graphs, so deficiencies add. Negative-deficiency components cannot occur in a maximizer; discarding zero-deficiency components leaves simply connected positive-deficiency components. Each must meet \(b=0\): otherwise the north-parent edges \(\{u/3,2u/3\}\) match every label. Each fixed edge type is itself a matching. The same argument for east-parent and root edges forces a label with \(a=0\) or \(u>2t/3\), and a label with \(u>t/3\). **The missing theorem is still**
\[
\sum_i d(U_i)\le I_j(t)+P_j(t)
\]
for a color \(j\) minimizing the proposed cover bound. A single boundary cycle does not prevent several axis contacts from sharing a matching bottleneck. ([Normalization and remaining inequality](<hole_filling.md>))

## Exact checks eliminate specific finite shortcuts

The first failure of rounding the unrestricted fractional optimum occurs at **\(t=486\)**: exact integer dynamic programming gives \(\tau=11\), while rational primal and dual certificates give fractional optimum \(2468/249\), whose ceiling is 10. Every earlier smooth prefix was checked. This refutes that LP route without refuting the candidate integer formula. Separately, exact enumeration found no counterexample among **3,787** complete shapes of widths 21–34 whose row drops avoid \(11\) and \(222\). Those restrictions hold for the actual slope \(\log_2 3\), but the finite search proves no uniform normalization. ([Certificates and verifier](<verify_cover_certificates.py>), [enumeration record](<cover_words_exact_results.json>))

Retain only north-parent \(N(u)=\{u/3,2u/3\}\) and east-parent \(E(u)=\{u/2,3u/2\}\) edges. Their components are paths: alternating continuation multiplies labels by six, excluding cycles. If \(r,q\) count missing \(N,E\) edges and \(o\) counts odd-length paths, then
\[
\nu_{NE}=|U|-(r+q-o)/2.
\]
Root edges \(R(u)=\{2u,3u\}\) must provide the missing augmentations. At \(t=18\), \(U=\{4,18\}\) has matching number two, attained using both edges owned by 4; no matching of that size uses one edge per label. Thus a “rainbow” assignment is invalid. ([Derivation and exact obstruction](<cover.md>))

## The weighted identity controls height but lacks compression

The arithmetic advance is unconditional. Set \(a_d=3\Delta\alpha(d)-2\in\{1,-2\}\) for \(d\in S\), and \(a_x=0\) off \(S\). The density identity gives
\[
Z=\sum_{d\in S}\frac{a_d}{d}=9c-6.
\]
For \(q=2^Q\), \(B=\lfloor\log_3q\rfloor\), and \(b_Q(r)=a_{qr}-a_r\), reindexing proves
\[
3^B(q-1)Z-N_Q=\sum_{r>1}\frac{3^Bb_Q(r)}r,\qquad
N_Q=3^B\left(q\sum_{\substack{d\in S\\d\le q}}\frac{a_d}{d}-1\right)\in\mathbb Z.
\]
Integrality follows because every such \(d\) divides \(3^Bq\); the sums over \(r\) are supported on \(q^{-1}S\).

Truncate at \(r\le e^T\). Under the temporary assumption \(c\in\mathbb Q\), coefficients belong to the fixed finite set \(\{\pm Z,\pm1,\pm2,\pm3\}\), and
\[
H\le42e^{2T+2Q\log2},\qquad
|E_Q(T)|\le(3Q+6T/\log2+18)\,3^Be^{-T}.
\]
For \(T\ge Q\log2\), every retained unit is at least \(t_0=3^Be^{-T}\le1\). The error bound is only a polynomial multiple of this scale. The height is controlled, but **the number of terms is not fixed, the tail lacks an extra exponential saving, and nonvanishing remains unproved**. Those are distinct prerequisites for the #1062 transfer. ([Identity, height proof, and tail estimate](<weighted.md>))

Exact returns at endpoints do not supply weighted cancellation. With \(g=\alpha-2K/3\), \(Q=9\), and \(q=512\), all color-count differences and \(g\) return at the paired cutoffs \(10,5120\) and \(60,30720\), yet
\[
\int_{10}^{60}\frac{g(512s)-g(s)}{s^2}\,ds
=\frac{2135}{236196}\ne0.
\]
The underlying optima were checked by exhaustive integer DP. Moreover, negative-two-exponent atoms \(r=2^{a-Q}3^b\), \(0\le a<Q\), contribute \(QL/\log3+O(Q)\) mandatory nonzero jumps in a logarithmic window of length \(L\). Pointwise return equality cannot hold on an interval longer than \(\log3\). This counts the direct expansion; it does not exclude a different algebraic compression. ([Exact replay](<weighted_check.json>))

Nonvanishing also needs more than distinct jumps: at \(Q=6\), the contributions from \(d=432,864\) cancel exactly as \(64/432-128/864=0\). A mixed difference \(J(t)=g(t)-g(t/8)-g(t/27)+g(t/216)\) has jump \(-1\) at \(157464\), even though the corresponding linear color renewal and axis corrections cancel. Nonlinear changes of minimizing color survive. These examples obstruct specified shortcuts; they prove no impossibility theorem for the broader method. ([Weighted analysis](<weighted.md>))

## Other transfers do not close an eligible target

The actual audited #944 seed has **girth four**, but fewer than \(n^2/50\) edges, so it does not challenge #23 or satisfy #128's required density premise. Its all-orders existence extension was already public in October and cannot count as a different solution. The narrow two-disk geometry used for #96/#97 has an endpoint determining at least \(\lceil n/2\rceil\) distances, excluding that family as a #982 counterexample. The difference-of-powers graph encoding for #774 turns dissociated sets into forests; high-chromatic critical subgraphs force their proportional size below \(2/q\), destroying the required uniform positive fraction. These are restrictions on those transfers. ([Alternate deductions](<alternates.md>), [#944 priority audit](<../../../../erdos-0944-critical-graphs-all-orders/novelty-and-audit/REPORT.md>))

## Conclusion

The next finite step is to classify root-edge augmentations on the normalized simply connected boundary components and prove their **total** deficiency bound. The arithmetic step is to compress a proved weighted identity into boundedly many S-unit terms with fixed coefficients, exponentially improved error, and verified nonvanishing. Repeating LP rounding or endpoint-return arguments cannot replace these obligations.

All recorded processes are terminal: session 30936 was interrupted; 14469 and 55089 exited successfully. No Lean formalization was attempted, as requested; this synthesis did not rerun computations or conduct additional source searches. Priority remains unchecked, and the two missing proofs remain the material risk: **the open-target goal is unmet and active.**

