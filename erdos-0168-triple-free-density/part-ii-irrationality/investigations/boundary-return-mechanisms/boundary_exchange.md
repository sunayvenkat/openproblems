# Repeatable exchanges and charged boundary completion

## Does the entire three-triple exchange repeat, and can it compress continued-fraction motifs?

### Takeaway

**Yes.** The entire exchange preserves ordinary maxima as well as the exceptional actual maxima, so positive two-dimensional period-six translations are valid. A bounded unimodular change of coordinates produces a parameterized, maximum-preserving compression by at least one seventh in both coordinate spans. This is a local mechanism, not a supply theorem for a suitable optimal parent coupling. — [Standalone certificate](boundary_exchange_check.py).

### Cited Findings

- Write the two seed families as
  \[
  \begin{aligned}
  P={}&\bigl(\{(2,8),(10,3),(14,0)\},
  \{(13,1),(12,2),(7,5)\},
  \{(4,7),(1,9),(9,4)\}\bigr),\\
  R={}&\bigl(\{(13,1),(10,3),(14,0)\},
  \{(4,7),(12,2),(7,5)\},
  \{(2,8),(1,9),(9,4)\}\bigr).
  \end{aligned}
  \]
  They use the same nine points, one point of each color in each triple. All nine points have distinct residues modulo \(6\mathbb Z^2\). — [Functions check_trade and complete_roots](boundary_exchange_check.py).
- Their ordinary maximum times, in the displayed order, are exactly \(27648,36864,41472\), identical to the actual maxima. The earlier warning about loss of an individual low-row tie does not show that the whole exchange fails vertically. — [Exact ordinary and actual assertions](boundary_exchange_check.py); [earlier limited warning](../adaptive-shape-couplings/adaptive_structure.md).
- The parameterized checker obtains parent/child coordinate spans \((37,24)\to(26,17)\), \((227,143)\to(181,114)\), and \((623,393)\to(474,299)\) from the specified Farey bases. Charged embedding cuts remain respectively \((60,36),(348,222),(888,564)\), each with one donor period. These cuts must not be replaced by the smaller child spans. — [Function transformed_trade](boundary_exchange_check.py).

### Inferences

**BE1. Maximum-preserving substitutions.** If a complete fractional coupling contains disjoint parent blocks, replacing each block by a weighted family on the same token multiset preserves unit marginals. If the completion-time multiset, with weights, is unchanged in every block, the complete function \(G(t)\) and the cost \(Q\) are unchanged. In particular every genuine optimal head is preserved, and the actual reduced denominator is unchanged. A sufficient test for a one-color permutation is that both old and new partners arrive no later than the maximum of the two fixed partners. This is the test below.

For the physical seed, all nine token rows are distinct and all nine residue pairs are distinct. The translates of the whole block by \((6n,6m)\), \(n,m\ge0\), are therefore disjoint. At \(m=0\), horizontal translations preserve the actual retiming factors. At \(m\ge1\), all arrivals are ordinary; the three maximum points are already ordinary. Thus both families have completion times
\[
2^{6n}3^{6m}(27648,36864,41472).
\]
The exchange is valid in two dimensions; optimality of a parent at these translated placements remains a separate requirement. — [check_trade](boundary_exchange_check.py).

**BE2. A whole cone of valid weights.** Give a point \((a,b)\) logarithmic weight \(a x+b y\), with \(x>0\) and \(\rho=y/x\). For every \(3/2\le\rho\le8/5\), both families have logarithmic maxima
\[
x(10+3\rho),\quad x(12+2\rho),\quad x(9+4\rho).
\]
These maxima belong to the two partners that are not permuted. The needed inequalities are, successively, \(\rho\le8/5\), \(\rho\ge3/2\), \(\rho\ge1\), \(\rho\le8/5\), \(\rho\le5/3\), and \(\rho\le7/4\); all hold on the stated closed interval. Endpoint ties are permitted.

**BE3. Bounded matrices put any positive Farey basis into that cone.** Let
\[
B=\begin{pmatrix}q&s\\-p&-r\end{pmatrix},\qquad |\det B|=1,
\]
where \(q,s,p,r>0\), and \(q+p,s+r\) are opposite nonzero residues modulo three. Its physical column errors are \(e_1=q\log2-p\log3\), \(e_2=s\log2-r\log3\). If \(|e_1|\ge|e_2|\), choose
\[
M_0=\begin{pmatrix}9&14\\2&3\end{pmatrix};
\]
otherwise choose \(M_1=\begin{pmatrix}2&3\\9&14\end{pmatrix}\). Multiply the resulting matrix by the sign of the dominant error. The new physical column errors are positive and satisfy
\[
\frac{17}{11}\le\frac yx\le\frac{11}{7},
\]
because their ratio is \((14+3t)/(9+2t)\), with \(-1\le t\le1\). This interval lies inside BE2. No assumption about the signs of the original errors is needed.

Both matrices are unimodular. Their color rows are respectively \((1,-1)\) and its negative modulo three. Composition with \(B\), and the overall sign, preserves the three-color condition up to permutation. The resulting map is invertible modulo six, preserving the nine distinct residue pairs. Translate the entire nine-point block by multiples of six so its minimum first coordinate is in \([0,5]\) and its minimum second coordinate in \([2,7]\). The transformed seed and all its positive period-six translates are ordinary, so BE2 proves actual maximum preservation without any low-row exception.

For either physical coordinate, the absolute ratio of the two matrix entries is
\(3/2\le\rho_c\le14/9\); the entries have the same sign. Put \(\delta=\rho_c-3/2\in[0,1/18]\). Direct extrema over the nine fixed seed points give
\[
\max\operatorname{span}(P)=|c_1|(1/2+3\delta),\qquad
\max\operatorname{span}(R)=|c_1|(1-4\delta).
\]
Consequently the **reverse** substitution \(R\to P\) reduces the maximum span on each physical axis by a factor at most \(6/7\). The ordinary-weight interval used for validity and the narrower coordinate-projection interval used for compression are different and both have been checked. — [transformed_trade and exact integer maxima](boundary_exchange_check.py).

### Gaps

- No theorem supplies these parent blocks inside an actual infinite family with a sufficiently long optimal head. Zero-cost substitution cannot create a longer head: it preserves the entire completed-count function. — [BE1; accepted arithmetic target](../adaptive-shape-couplings/REPORT.md).
- A smaller normalized span does not erase old clipping positions or model crossover factors. In particular it cannot reduce the actual denominator of an unchanged rational cost. — [Complete embedding below](boundary_exchange_check.py).

## Can all complementary residues and boundary tails be completed with controlled arithmetic?

### Takeaway

**Yes, using moment balance and an explicitly charged repair.** Two color-cycling averages balance every root moment of total degree at most two. This gives balanced periodic edge flux and only linear corner imbalance; for the parameterized Farey construction, finitely many donor periods suffice uniformly. All clipping positions remain part of the arithmetic cost. — [root_moments, analytic_boundary and repaired](boundary_exchange_check.py).

### Cited Findings

- The checker completes the nine seed residues by grouping the remaining 27 residue nodes into nine three-color triples. It averages horizontal root translations with weights \((1,2,3,2,1)/9\). Every residue has total plane coverage one. All first and quadratic moments agree across colors. — [complete_roots, averaged_roots and root_moments](boundary_exchange_check.py).
- The complete parent and child embeddings have exactly the same rational cost
  \[
  Q=\frac{357544920809}{704310018048}.
  \]
  Their cuts are \(A=24,B=12\), with one donor period; a safe full clearing factor is
  \[
  D=125176966099650799095250944.
  \]
  All four cost pieces and all their infinite tails are included. — [repaired](boundary_exchange_check.py).
- Both embeddings have first deficit at \(t=3\), where \(\tau=1\) but \(G=7/9\). Direct event replay confirms their full completed-count functions agree through \(2^{20}\). This completion is a certificate of repeatability, not a good approximation to \(M\). — [event_profile](boundary_exchange_check.py).

### Inferences

**BE4. Double color averaging balances moments.** For any three-color root family covering each of the 36 residues once, let \(\mathcal A\) average horizontal translations by \(0,1,2\). Translation cycles the colors. The number of root points per color is twelve. The operator \(\mathcal A\) makes both first moments color-independent. Applying \(\mathcal A\) a second time makes \(\sum a^2\), \(\sum ab\), and \(\sum b^2\) color-independent as well: in the expansion of \((a+d)^2\) and \((a+d)b\), the cross terms use already balanced first moments. Thus \(\mathcal A^2\) gives precisely the five shifts and weights above. It pays one denominator nine, not one denominator for every root.

The initially equal zeroth color counts are essential for the pure \(a^2\) assertion. Equivalently, the colored generating function already vanishes at the origin. The double-averaging multiplier has a zero of order two there, so their product vanishes to order at least three. Double averaging would not kill an arbitrary unbalanced collection's second horizontal moment. Mixed \(ab\) balance alone suffices for the corner estimate below.

This averaging is a **construction operation**, not a theorem preserving an existing optimal head. Parent and child costs agree after averaging because every corresponding trade copy agrees separately.

**BE5. Root clipping and edge flux.** Keep whole root triples at nonnegative cell indices \((6n,6m)\). This is not the rule “retain every wholly quadrant-contained normalized child triple.” Write a root coordinate as \(a=6I+u,b=6J+v\), with \(0\le u,v<6\). The residual mass lies in strips bounded by the largest **root coordinates**. Because plane coverage is one and \(\sum a,\sum b\) agree across colors, the two periodic fluxes
\[
n=\sum I,\qquad h=\sum J
\]
agree across colors, with all sums weighted. The fixed residue sums \(\sum u=\sum v=30\) in each color justify these equalities.

For \(A=6N\) and \(B=6M\) exceeding every root coordinate, the corner residual mass in color \(j\) is exactly
\[
c_j=M n+N h-\sum_{\text{color }j} I J.
\]
Quadratic moment balance cancels the leading \(ab\) term in differences of \(\sum IJ\). Since \(u,v\le5\),
\[
\max_jc_j-\min_jc_j\le\frac53(R_a+R_b+5),
\]
where \(R_a,R_b\) bound root coordinates. This is linear rather than quadratic in the root extent.

For the parameterized construction, put \(L=q+s\), and assume \(p+r\le L\), as for sufficiently late convergents of the present logarithmic slope. The explicit matrices and normalization give \(R_a\le11L+9\), \(R_b\le11L+7\). The block footprint has first-coordinate width at least \(2L\), giving \(n\ge L/9-5\). For \(L\ge180\), these estimates give a uniform donor bound \(J_0\le500\). Small specified examples have their exact positive capacities checked directly. The assertion is bounded donor **periods**, not bounded numbers of individual donated tokens.

**BE6. Full repair and clearance.** Move the first \(d_j=\max c-c_j\) units of color \(j\) from the left strip, in period order, into the corner. Couple the enlarged balanced corner by actual ranks. Couple each bottom period by actual ranks. Couple the remaining left lists by equal residual mass index. With all masses in \((1/9)\mathbb Z\), every split remains in that lattice. Once a root period is shifted simultaneously, its completion times scale by 64 or 729, so the infinite sums are geometric. The root bulk formula retains its actual first member, stabilized horizontal continuation and ordinary vertical continuation. A safe complete factor is
\[
D=9\cdot63\cdot728\;2^{A+6}3^{B+6J_0+6},\qquad DQ\in\mathbb Z.
\]
Thus the parameterized completion has \(\log D=O(q+s)\), with every old root position and donor shift charged. No coefficient-two claim relative to the compressed spans follows. — [Explicit four-piece sum and unit-mass repair](boundary_exchange_check.py); [accepted period-index repair](../farey-transport-corrections/boundary_repairs.md).

### Gaps

- At the fixed child spans \(8,5\), the point \((8,6)\) still has residual mass \(1/9\). This explicit interior residual proves that child normalized spans alone do not bound the block-clipped boundary. The old root positions cannot be discarded from a clearing estimate. — [Hardcoded assertion](boundary_exchange_check.py).
- The cost is unchanged by true substitutions; moment averaging and complementary completion do not provide actual parent optimality. The constructed completion deliberately demonstrates this by its deficit already at three. — [Complete cost and event checks](boundary_exchange_check.py).

## Does this establish the adequate infinite arithmetic return?

### Takeaway

**No.** It establishes a repeatable two-dimensional, parameterized local compression and a complete moment-balanced rational embedding. The missing theorem is the presence of such exchanges in a useful parent family, with an independently proved optimal window and denominator advantage. — [Current exact target](../adaptive-shape-couplings/REPORT.md).

### Cited Findings

- The accepted finish requires one family with \(D_HQ_H\in\mathbb Z\), \(Q_H<M\), and \(D_H(M-Q_H)\to0\). Existing finite canonical patches already give rational heads with clearing cost of order the square of the cutoff. — [Prior rational-coupling construction](../rational-coupling-construction/REPORT.md).
- Neither a single successful exchange nor the complete embedding above improves the integer-cleared error. All true zero-cost substitutions leave \(Q\), hence its reduced denominator, unchanged. — [BE1 and exact equal-cost embedding](boundary_exchange_check.py).

### Inferences

The new useful mechanism is geometric: one may exchange partners along finite deadline-preserving cycles, and such cycles can occur in whole periodic families. Double color averaging provides a rigorous way to construct balanced boundaries while exposing their exact cost. A future argument must prove that a parent with the needed head is closed under a controlled family of these exchanges, and then independently derive a cheap complete arithmetic formula. If a fixed parent already has a large reduced denominator, a smaller drawing of its triples cannot change that fact.

### Gaps

- **OPEN:** suitable actual infinite parent supply, an adequate repeated head, and a complete arithmetic estimate that beats the error. No irrationality or historical-priority claim is made.
- Skipped Lean, installations, external review and archived edits. Material risk: mistaking span compression or moment-balanced completion for a cheaper unchanged rational number or a newly proved long head.
