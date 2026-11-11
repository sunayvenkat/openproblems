# Energy calibration audit and the parity route

Research and independent audit, 7 November 2026. The global finite optimum
\(\tau(t)=\min_j(K_j-I_j-P_j)\) remains unproved. This note audits the preceding calibration and a new critical-set exclusion, establishes the exact parity parametrization and a restricted ray-constant result, and identifies two precise failures of proposed shortcuts. No minimum-energy normalization theorem is asserted.

## Are the preceding calibration and new deep-branch arguments valid?

### Takeaway

The directional charges, translated cuts, rational LP certificates, and six-shell recursion pass independent review. The separately requested deep-branch exclusion also passes: its two strips have exactly one common owner, and the two new selected vertices create the strict counting contradiction claimed.

### Cited Findings

- The audited calibration statements are in [boundary_calibration.md](<../global-boundary-proof/boundary_calibration.md>).
- The saved rational certificates are checked without an optimizer by [verify_calibration_certificates.py](<../global-boundary-proof/verify_calibration_certificates.py>). I reran this verifier read-only and separately checked the small primal's upper bounds.
- The independently reviewed new strip argument is [deep_branch.md](<deep_branch.md>). Its precise cover, cone, and strict-expansion hypotheses are retained below.

### Inferences

#### Directional charges and cuts

For a binary cover write \(e(u)=f(u)+f(2u)+f(3u)-1\ge0\). The two inequalities

\[
(f(6v)-f(v))_+\le e(2v)+e(3v)\quad(9v\le t)
\]

and

\[
(f(v)-f(6v))_+\le e(v)+e(4v)+e(9v)\quad(27v\le t)
\]

have valid binary case proofs. In the second nontrivial case, \(f(v)=1,f(6v)=0,e(v)=0\) forces \(f(4v)=f(9v)=1\); the corner at \(6v\) then forces at least one of \(12v,18v\) to be selected. The stated cutoff includes every corner used.

Their algebraic rearrangements are exactly the six-vertex cut with right side two and the nine-vertex cut with right side three in the source note. The fixed-color injectivity argument is correct: the two charging anchor sets in the first inequality have different colors, and the three in the second have different colors. The two directions must remain separate, and summing over colors does not preserve a one-charge bound. The original note states these limitations correctly.

The scalar identity \(3|F|=M+B(F)+E\), the three disjoint root-color packings, and their explicit boundary-site formulas are also correct. The packing argument works because the three possible roots of corners containing a fixed vertex have three different colors. The packet lift correctly represents the two intervening constraints; it supplies no automatic contour or phase simplification.

#### Rational certificate scope

The optimizer-free verifier passed for both stored instances. At \(t=486\), the rational primal and dual have the same objective \(235/23\); every primal coordinate is also at most one. Thus the strengthened relaxation has that exact value and its ceiling is 11.

At \(t=990677827584\), the saved rational point satisfies all 1367 translated inequalities and all coordinate bounds. Its objective is \(176511563/10^6<177\), whereas the candidate is 178. This disproves the uniform assertion \(\Lambda(t)>Q(t)-1\) for those cut families. It does **not** give an integer cover of size 177, establish the large instance's exact integer optimum, or refute the global candidate. The additive gap certified here is a gap below the candidate value; no stronger integer conclusion is warranted.

#### Six-shell recursion, including the origin

For real \(t\ge6\), the vertices with both exponents positive are exactly \(6D_{t/6}\); the remaining sites are the two axes, with the origin counted once. A corner rooted off the axes lies entirely in the dilated inner board. A corner rooted at \(2^a\), \(a\ge1\), has the inner vertex \(6\cdot2^{a-1}\); a corner rooted at \(3^b\), \(b\ge1\), has the inner vertex \(6\cdot3^{b-1}\). The only leftover corner is \(\{1,2,3\}\).

Therefore, for any inner cover \(G\), the source note's required horizontal and vertical path edges are exactly correct. The origin bit costs one exactly when the two first-axis bits are both zero. This proves the extension formula and

\[
\tau(t)=\min_{G\text{ covers }D_{t/6}}
\bigl(|G|+\mathcal E_t(G)\bigr).
\]

Every outer cover restricts to such a \(G\), and every admissible path extension covers all remaining corners. The minimization really is over **all** inner covers. No argument justifies substituting a minimum inner cover or retaining only its size. I found no missing small-\(t\) or endpoint case in the stated \(t\ge6\) formula.

#### Independent audit of the deep-branch exclusion

Assume the hypotheses of `deep_branch.md`: strict owner-neighborhood expansion and essentiality, two least axis roots

\[
x=2^{2r+s},\quad y=3^{r+2s},\quad r,s\ge1,
\quad g=4/3,\ q=9/2,
\]

and containment in the two nonnegative \((g,q)\)-cones. Write \(z=xq^s=yg^r\), and suppose \(z\le2t/9\).

In coordinates based at \(x\), the complete candidate owner sets of the two selected strips are

\[
\begin{aligned}
\mathcal H&=\{(0,n):0\le n\le s\}
\cup\{(1,n):1\le n\le s\},\\
\mathcal V&=\{(m,s):-r\le m\le0\}
\cup\{(m,s+1):-r+1\le m\le0\}.
\end{aligned}
\]

Their intersection is exactly \(\{(0,s)\}=\{z\}\). The horizontal strip has \(2s\) selected left vertices and the vertical strip has \(2r\) selected right vertices. All vertical root edges used exist: for \(m<r\), \(yg^m\le z/g\le t/6\). The horizontal root-edge cutoff is even stronger. The separate strict counts force \(gz,qz\in U\).

The last horizontal uniqueness condition excludes \(2z/3\) from \(W\); the last vertical uniqueness condition excludes \(3z/2\). The available edge \(E(gz)\) therefore forces \(2z\in W\), and \(N(qz)\) forces \(3z\in W\). For the borderline \(r=s=1\), \(qz\) still has positive 2-exponent and \(gz\) positive 3-exponent, so neither edge disappears at an axis. The two new vertices are larger than all earlier selected vertices on their respective sides and cannot coincide with vertices on the other bipartition side.

Their full owner lists are \(\{z,gz,6z\}\) and \(\{z,qz,6z\}\). Thus the selected set gains two vertices but at most one new owner. Starting with \(2r+2s\) selected vertices and \(2r+2s+1\) possible owners gives a set with at most as many owners as selected vertices, contradicting strict expansion. If \(6z\) is absent or unavailable, the contradiction only strengthens.

No closure or independent-component premise is needed. I found no gap in this exclusion under its stated hypotheses. Its corollary about the top vertical root additionally uses the previously established vertical-strip dichotomy; origin and \(r=0\) or \(s=0\) cases remain excluded from this argument.

### Gaps

The calibration audit supplies no boundary dominance theorem. The deep-branch result eliminates one critical-set regime but is not a global deficiency bound. Neither audit supplies the missing minimum-energy normalization.

## What exact parity structure is available, and what has it proved?

### Takeaway

Odd-hit covers form an explicitly parametrized binary code with one free bottom row. Its ray-constant sector has exactly the expected three phases, up to an isolated endpoint. General odd-hit covers can be much less rigid, and any nonzero parity-preserving modification must reach the board boundary.

### Cited Findings

- The energy identity and the fact that the ordinary patch has exactly one double-hit corner were established in [168_cover_review.md](<../../early-attacks/open-conjecture-transfer-search/168_cover_review.md>).
- The only new parity enumeration in this round is [parity_1536.py](<parity_1536.py>) with exact output [parity_1536.json](<parity_1536.json>).

### Inferences

#### Parity syndrome and minimum energy are different data

For any cover define its syndrome at a corner root by

\[
\sigma(a,b)=e(2^a3^b)\pmod2.
\]

A double-hit corner has \(\sigma=1\), while one-hit and triple-hit corners have \(\sigma=0\). If \(T(F)\) is the number of triple-hit corners, then

\[
E(F)=|\sigma|+2T(F).
\tag{P1}
\]

Thus syndrome zero does not mean energy zero. Among covers of a fixed cardinality, minimizing \(E\) is equivalently minimizing \(\sum_{v\in F}\deg(v)\), or maximizing the boundary penalty \(B(F)\). Existence of such a minimizer is immediate from finiteness; the assertion that a globally minimum cover can be chosen with \(E\le1\) is not established.

Set \(g=1-f\). Over \(\mathbb F_2\), the syndrome equation is

\[
g(a,b)+g(a+1,b)+g(a,b+1)=\sigma(a,b).
\tag{P2}
\]

An odd-hit cover has \(\sigma=0\). Conversely any binary solution of the homogeneous equation gives a valid cover: every corner then has an odd number of selected vertices, hence either one or three.

#### Exact bottom-row parametrization

Let \(H=\lfloor\log_2t\rfloor\). Row \(b\) has length

\[
w_b=1+\left\lfloor\log_2(t/3^b)\right\rfloor.
\]

Every next nonempty row is shorter by one or two. Its entire row is therefore determined from the preceding row by

\[
g(a,b+1)=g(a,b)+g(a+1,b)\pmod2.
\tag{P3}
\]

Every choice of the \(H+1\) bottom bits gives exactly one odd-hit cover, and all odd-hit covers arise this way. Iterating gives

\[
g(a,b)=\sum_{k=0}^{b}\binom bk g(a+k,0)\pmod2.
\tag{P4}
\]

All required bottom indices exist: \(2^{a+b}\le2^a3^b\le t\), so \(a+b\le H\). This also makes the Pascal/fractal dependence on a bottom perturbation exact, rather than heuristic.

In the usual fixed-row elementary-cellular-automaton convention, (P3) is Rule 102, the reflection of Rule 60. Under the staggered spatial coordinate \(i=2a+b\), the parents have coordinates \(i-1,i+1\), giving the Rule-90 form on the appropriate parity sublattice. Periodic-boundary results for these different fixed-width presentations must not be interchanged without transforming their boundaries.

#### No strictly interior parity-preserving flip

Suppose two odd-hit covers differ on a nonempty finite set consisting only of vertices of corner degree three. Let \(h\) be their binary difference and extend it by zero to all of \(\mathbb Z^2\). Every full-plane upward corner meeting the support lies inside the original board, so

\[
h(a,b)+h(a+1,b)+h(a,b+1)=0
\]

holds everywhere. On the highest row containing a nonzero value, the next row is zero. Hence \(h(a,b)=h(a+1,b)\) for every integer \(a\). That row must be constant, and finite support makes it zero, a contradiction.

Therefore every nonzero odd-sector modification touches a vertex of degree less than three. A strictly interior bounded parity gadget cannot perform the required normalization. This statement does not prohibit exchanges that temporarily change the parity syndrome.

#### The ray-constant odd sector is completely classified

Index the \(6\)-rays by \(k=a-b\). A ray has length

\[
L_k=\begin{cases}
1+\lfloor(\log t-k\log2)/\log6\rfloor,&k\ge0,\\
1+\lfloor(\log t+k\log3)/\log6\rfloor,&k\le0.
\end{cases}
\]

If \(f\) is constant on each ray, write its value as \(b_k\). Let \(B=\lfloor\log_3t\rfloor\), and \(h=\lfloor\log_2(t/3)\rfloor\). The corner-root indices are exactly \(1-B\le k\le h\). Odd covering is equivalent to

\[
b_{k-1}+b_k+b_{k+1}=1\pmod2
\quad(1-B\le k\le h).
\]

This recurrence forces \(b_{k+3}=b_k\) throughout the constrained interval. Its four possibilities are the three one-hot period-three words and the all-one word. The active variables range from \(-B\) to \(h+1\). This includes every ray except possibly \(k=H\); the exception occurs exactly when \(2^H>2t/3\), and that ray is the single isolated vertex.

Consequently, for \(t\ge3\), the minimum size in the **odd-hit, ray-constant** sector is exactly

\[
\min_j(K_j-I_j).
\tag{P5}
\]

The missing step is a cardinality-preserving or improving compression into this sector. Nothing here establishes such compression for arbitrary odd covers, much less arbitrary covers.

#### One exact finite test

At \(t=1536\), there are 45 vertices, bottom width 11, and \((K_0,K_1,K_2)=(15,15,15)\). The new checker expanded all \(2^{11}=2048\) bottom words and independently checked that every resulting corner has one or three hits. The minimum odd-hit cover size is 15. Among odd covers of that size, the minimum energy is zero, attained by six boundary variants including the three pure phases.

The known patch cover has size 14 and energy one. Thus this particular saving genuinely requires at least one even-hit corner; no odd/fractal codeword duplicates it on this board. This is a finite result, not a proof of the general odd-cover inequality \(|F|\ge\min_j(K_j-I_j)\).

### Gaps

The general odd-cover weight inequality, a cost-controlled parity repair, and the minimum-energy bound \(E\le1\) are all open here. The exact formulas provide a representation of competitors, not their sharp optimum.

## Can parity repair or periodic plaquette results supply the missing normalization?

### Takeaway

The natural bottom-preserving parity repair can have unbounded cost even for a single syndrome. Relevant primary plaquette papers identify the correct cellular automaton, but their periodic magnetization statement does not control the free boundary in this problem. A zero-cost phase gluing premise also fails explicitly.

### Cited Findings

- Sfairopoulos, Causer, Mair, and Garrahan explicitly distinguish Rule 60 from Rule 90 for the Newman–Moore model; their Appendix A treats additional rectangular boundary conditions. It does not give a minimum-field-weight theorem for this logarithmic cap. [Primary paper, introduction and Appendix A](https://arxiv.org/html/2301.02826v3).
- Sfairopoulos and Garrahan's longitudinal-field Appendix A treats \(3P\times3Q\) **periodic** lattices. Its block argument relies on matching adjacent tiles; it provides no explicit charge for our free boundary. [Primary paper, Appendix A](https://arxiv.org/html/2409.09235v2).
- The \(t=54\) cover used below is the exact canonical example established in [canonical_phase.md](<../global-boundary-proof/canonical_phase.md>).

### Inferences

#### A single syndrome can have unbounded bottom-preserving repair cost

For arbitrary \(t\ge3\), put \(B=\lfloor\log_3t\rfloor\) and

\[
F=D_t\setminus\{3,9,\ldots,3^B\}.
\tag{P6}
\]

The origin 1 remains selected. The corner at 1 has two selected vertices. Every other vertical-root corner has exactly one, its off-axis vertex. Every corner rooted off the vertical axis has all three vertices selected. Hence \(F\) is a valid cover with exactly one nonzero parity syndrome.

Its bottom row is all selected. The odd-cover recurrence in selection bits,

\[
f(a,b+1)=1+f(a,b)+f(a+1,b)\pmod2,
\]

maps an all-one row to an all-one row. Therefore the unique odd-hit cover with this same bottom row is all of \(D_t\). The repair adds exactly \(B\) vertices, which is unbounded as \(t\) grows.

This refutes a bound on the cost of the **bottom-preserving** parity projection in terms of syndrome count alone. It does not refute an optimized repair that changes the boundary, nor any statement restricted to cardinality-minimum, minimum-energy covers: (P6) is not such a cover.

#### Why the literature does not currently close the boundary gap

With spins \(s=2f-1\), odd covering makes every upward plaquette product \(+1\). A field favoring negative spins favors fewer selected vertices, so the unexcited classical plaquette sector is the relevant analogy. The full finite-field model also permits configurations with empty corners and is not identical to the cover problem.

For a periodic board with every vertex in three corners, the bulk count already gives \(3|F|\ge M\). Pure phases attain it when periods permit. In the present cap the exact correction is \(B(F)+E\), whose comparison with the three phase-boundary costs is precisely the unresolved problem. The inspected periodic block proof supplies no controlled replacement for that term.

The rectangular open-boundary model has a different set of free boundary bits from (P3). Thus even its ground-state counting cannot be transferred as a minimum-weight assertion for \(D_t\). No theorem from these papers was imported into the finite-cover proof.

#### A concrete failure of zero-cost exterior phase filling

At \(t=54\), the cover

\[
F=\{1,6,12,16,18\}
\]

is odd-hit: it has one triply hit corner and all other corners are singly hit. Extend it to the full quadrant by selecting a pure phase outside \(D_{54}\), without changing the inside cover. Every choice fails:

| Exterior phase | Uncovered crossing corner |
|---|---|
| 0 | \(\{36,72,108\}\) |
| 1 | \(\{27,54,81\}\) |
| 2 | \(\{32,64,96\}\) |

In each case the chosen phase's vertex lies inside \(D_{54}\) and was omitted by \(F\); the remaining vertices are either also omitted inside or excluded by the exterior phase. Therefore a torus or full-plane comparison cannot discard the repair halo. An equal-cardinality change of the inside cover may still fix the problem, but proving that is the normalization being sought.

### Gaps

No general energy-reducing exchange or sharp boundary charge was obtained. Minimum energy and arbitrary preferred-color canonicality must remain separate: the \(t=54\) canonical cover has energy two, while another minimum cover has energy zero. The parity parametrization, restricted-sector theorem, and failed invariants are auxiliary results; they do not establish the global finite optimum or #168(ii) irrationality. No broad board sweep, large decimal computation, new dependency, Lean work, or modification of earlier research folders was undertaken.
