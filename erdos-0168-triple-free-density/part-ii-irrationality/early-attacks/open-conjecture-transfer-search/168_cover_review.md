# Erdős 168: adversarial review of the proposed finite cover formula

## What is being asserted, and what has actually been established?

### Takeaway

The candidate formula is a valid upper bound. The required sharp lower bound remains unproved. Large two-color matching checks support it, while several attractive general normal-form lemmas are false.

### Cited Findings

The relevant finite problem is to hit every corner {n,2n,3n} among the 3-smooth integers at most t. In exponent coordinates its vertex set is D_t={(a,b)>=0:2^a3^b<=t}. Veselinov gives the modular coloring construction and the exact decomposition of the full-interval problem into these components, but not the finite formula under review. [Primary paper, Sections 3,4,6](https://arxiv.org/html/2604.15515v1).

### Inferences

Let C_j={2^a3^b<=t:a+2b=j mod3}. Each corner has exactly one vertex in each C_j. The proposed candidate chooses the smallest of three covers obtained from C_j by:

1. Removing an isolated pure power of two greater than 2t/3, if it lies in C_j.
2. If s=2^a and 12s<=t<27s/2, optionally replacing {2s,9s,12s} with {3s,4s}, in the class j=a+1 mod3.

These are upper-bound constructions. Agreement with computed minima does not establish their optimality for all t. The underlying live #168 target additionally requires irrationality of the limiting density, so even a complete finite-formula proof would not alone finish that target.

### Gaps

No proof here normalizes an arbitrary optimal cover to these three constructions. No full solution of #168 is claimed.

## Are the local corrections valid?

### Takeaway

Yes. Their validity can be checked exactly without computation, and the upper endpoint 27s/2 is essential.

### Cited Findings

The modular coloring premise is the elementary unit-corner coloring in [Veselinov, Lemma 3.1](https://arxiv.org/html/2604.15515v1). The following patch and calculations are from the present investigation.

### Inferences

Write d_t(v) for the number of corners containing v. Then

    d_t(v) = 1_(3v<=t)
             + 1_(2 divides v and 3v/2<=t)
             + 1_(3 divides v).

For a pure power of two v>=2, d_t(v)=0 exactly when v>2t/3. Removing it cannot uncover a corner. The cases t<3 can be checked directly; the vertex1 is also isolated there.

For the patch, all three removed vertices have color a+1 and both added vertices have color a+2. Under 12s<=t<27s/2, the existing corners affected by removing {2s,9s,12s} are exactly

    {s,2s,3s}, {2s,4s,6s}, {3s,6s,9s}, {4s,8s,12s}.

Each contains one of the added vertices3s,4s. The otherwise dangerous corner {9s/2,9s,27s/2} is absent by the strict upper bound; the other potential new corners containing9s or12s have still larger maxima. Thus the patch decreases cover size by one.

Let E_t be the corner set. For any cover C, define

    B(C)=sum_(v in C) (3-d_t(v)),
    O(C)=sum_(e in E_t) (|C intersect e|-1).

Double counting gives the exact identity

    3|C|=|E_t|+B(C)+O(C).

A color class has O(C)=0. For a>=1, the patch creates exactly one double-hit corner, anchored at3s/2. Boundary penalty decreases by4 and O increases by1. For a=0 there is no such corner; boundary penalty decreases by3 and O stays zero. Both give the required decrease of3 in the identity. This explains the patch but supplies no global lower bound.

### Gaps

The identity does not imply that an optimal cover has at most one overcovered corner. That would be a new structural theorem, not a consequence of nonnegativity.

## What does exact two-color matching prove, and which normal forms fail?

### Takeaway

If covers are restricted to two colors, the optimum is an ordinary bipartite minimum vertex cover, hence a maximum matching. This is exact for that restricted problem. It is not an automatic normal form for unrestricted covers.

### Cited Findings

This section records independently computed results and explicit counterexamples. The scripts are `check_168_two_color.cjs` and `check_168_ferrers.cjs` in this directory, with their JSON artifacts. No outside theorem beyond bipartite matching duality is being used to infer an unrestricted optimum.

### Inferences

Fix colors j,k. Every corner has one vertex of each, so make an edge between its j-vertex and k-vertex. A selected subset of those two color classes hits every corner if and only if it is a vertex cover of this bipartite graph. The implementation reconstructs a cover from the alternating-reachability sets and checks both that it hits every original corner and that its cardinality equals the matching cardinality.

For the actual 2–3 weighted triangles, the smallest two-color optimum agrees with the patched candidate at sampled prefixes of 5000,10000,20000,50000,100000,200000,500000 and1000000 smooth integers. The last three results are saved in `168_two_color_results.json`; at1000000 the common minimum is333332. These are samples, not a check of every intervening prefix.

Several proposed extensions are false:

- **Arbitrary Ferrers ideals.** Rows (2,2,2,2,2,2,1) have13 vertices and six corners. The three points (0,1),(0,3),(0,5) hit all six. Every point hits at most two corners, so tau=3. Each of the three two-color optima is4.
- **Strict Ferrers ideals with drops1 or2 and final row1 or2.** Rows (21,20,18,16,15,14,12,10,9,8,6,4,2) have155 vertices. Exact row-mask dynamic programming finds a cover of size50, whereas all three pair-color maximum matchings have size51. A reconstructed cover, directly checked against every corner, has row bitmasks (559396,209481,17554,39204,8777,3218,292,585,146,36,9,2,0), with bit a indicating selection at(a,b). The artifact is `168_strict_counterexample.json`. This boundary is not mechanical: its drop word has both11 and22, incompatible with global balance.
- **All genuine linear triangles at arbitrary slopes.** The exact rational triangle 11a+2b<=21 has rows (2,2,2,2,2,2,1,1,1,1,1), hence17 vertices. Its additional tail points are isolated; the same three-point cover works, while each two-color optimum is4. Thus convexity alone is insufficient.

The more focused statement for genuine linear triangles a+beta*b<=A with1<beta<2 survives an exhaustive finite test: all4424 distinct shapes of width,height at most25 had unrestricted optimum equal to the smallest two-color optimum. This enumeration uses exact rational feasibility inequalities, not sampled slopes. For row lengths w_i, a feasible slope must satisfy

    (w_i-w_j-1)/(j-i) < beta < (w_i-w_j+1)/(j-i)  (i<j),

and, for terminal height h, beta>(w_i-1)/(h-i). Intersecting these bounds with(1,2) decides whether the complete shape is realizable. The exact DP uses all row masks and all feasible transitions, so it imposes no color-pattern ansatz. The result is saved in `168_ferrers_balanced_results.json`.

### Gaps

The test of4424 shapes is not a proof for all linear triangles. The counterexamples show exactly why dropping slope or balance assumptions would invalidate a purported proof.

## Can the unrestricted lower bound be reduced to a boundary matching problem?

### Takeaway

Yes. The reduction below is rigorous and includes all three-color competitors. The unresolved part is a uniform boundary deficiency bound.

### Cited Findings

The reduction and its directed matching structure are deductions developed in the present team investigation. They are not statements attributed to Veselinov or Kohlmeyer–Kruer.

### Inferences

Fix a baseline class C_j and let C be an arbitrary cover. Put U=C_j\C. For every corner whose j-colored vertex belongs to U, join the two other vertices by an edge, giving a bipartite graph B(U) on the other two colors. Since C must hit those corners, C\C_j is a vertex cover of B(U). Therefore

    |C| >= |C_j|-|U|+nu(B(U)),

where nu is maximum matching size.

If every u in U has corner degree3, then B(U) has3|U| edges and maximum degree at most3. Every vertex cover consequently has size at least|U|, and bipartite duality gives nu(B(U))>=|U|. All possible saving over C_j is therefore caused by boundary labels, but this observation alone does not bound the total saving.

There is a useful explicit starting matching: for every u in U divisible by3, use the north-parent edge {u/3,2u/3}. These edges are disjoint. Its only missing labels are the pure powers of two in U. Orient nonmatching edges from color j+1 to j+2 and contract each north-parent matched edge to its label. A root-corner edge has the form

    label6u -> label(9u/2),

and an east-parent edge has the form

    label(9u/2) -> label(3u/4),

whenever both labels belong to U; otherwise an endpoint is free. Both arcs strictly decrease numerical value, by ratios3/4 and1/6 respectively. Hence this contracted residual graph is a directed acyclic graph. Free endpoints must still be tracked; acyclicity by itself does not prove a matching bound.

For the patch U={2s,9s,12s}, B(U) is exactly the five-vertex path

    s -- 3s -- 6s -- 4s -- 8s.

Its matching number2 is one below|U|. This is the precise Hall-type obstruction realized by the patch.

Let delta_j be the number of allowed savings for class j in the candidate, and choose j minimizing |C_j|-delta_j. A sufficient sharp lower-bound lemma is

    nu(B(U)) >= |U|-delta_j  for every U subset C_j.

This lemma has not been proved. It is stronger than checking B(C_j), or than checking the optimum among two-color covers.

### Gaps

No classification of all boundary deficient subsets U has been established. In particular, the existence of the five-vertex-path obstruction does not show that it is the only possible obstruction.

## What rigidity can be proved without assuming optimality?

### Takeaway

An exact cover, meaning one hit in every corner, is forced to agree with one global color class throughout a large interior region. Only a boundary band containing at most three vertices in each horizontal row can differ.

### Cited Findings

The following is an elementary lemma proved here. It concerns exact covers and must not be applied to arbitrary minimum covers without a separate normalization argument.

### Inferences

Write x(v)=1_C(v). Suppose the six corners anchored at v,2v,3v,4v,6v,9v are all hit exactly once. Then x(v)=x(6v).

Proof: if x(v)=1, then x(2v)=x(3v)=0. If x(6v)=0 as well, the corners at2v and3v force x(4v)=x(9v)=1. The corners at4v and9v then force x(12v)=x(18v)=0, contradicting the corner at6v. Conversely, x(6v)=1 forces x(2v)=x(3v)=0 and then x(v)=1. All six corners exist whenever27v<=t.

Thus, for an exact cover,

    x(v)=x(6v)  if27v<=t.

Applying this at v and2v, together with the exact equations at v,2v,4v, gives

    x(v)=x(8v)  if54v<=t.

Indeed, x(6v)=x(v), x(12v)=x(2v), x(4v)=x(3v), and the equation at4v finishes the claim. Applying the first identity at v and3v analogously yields

    x(v)=x(27v) if81v<=t.

For t>=162, let A=x(1), B=x(2), C=x(3); exactly one is1. The nine residue representatives1,2,4,3,6,12,9,18,36 have values

    A B C
    C A B
    B C A.

Here x(36)=x(6)=A uses the first identity at6, whose largest required corner endpoint is162. Reducing any a>=3 by a factor8 and any b>=3 by a factor27 preserves x whenever the original vertex n=2^a3^b satisfies n<=4t/27: the factor8 step needs54(n/8)<=t, and the factor27 step needs81(n/27)<=t. Every later reduction is smaller, so the same inequalities remain valid.

Consequently every exact cover agrees with the color class determined by A,B,C on all n<=4t/27. The exceptional band (4t/27,t] has multiplicative width27/4<8, so each horizontal row contains at most three exceptional vertices.

For a general cover, failure of x(v)=x(6v) implies an overcovered corner among those six anchors. This gives a bounded-neighborhood way to detect a phase discrepancy, but does not yet control the number or propagation of defects.

### Gaps

The missing bridge is a proof that a minimum cover can be chosen with zero or one overcovered corner, or another argument controlling many-defect configurations. The thin-band theorem is not a proof of that bridge.

## What is the exact computation checkpoint?

### Takeaway

All searches in this checkpoint have finished. The final restricted competitor check completed successfully after the initial checkpoint.

### Cited Findings

The local scripts and JSON artifacts named above are the computation records. These are research checks, not Lean proofs.

### Inferences

- Session20101 finished: sampled two-color matching checks through1000000 actual smooth vertices.
- Session39680 finished: strict Ferrers enumeration through width18, no counterexample in10944 shapes.
- A subsequent optimized strict enumeration through width21 finished and found the155-vertex counterexample recorded above.
- Session8356 finished: all4424 exact linear-triangle chambers with1<beta<2 and width,height<=25, no normalization counterexample.
- **Session 21423 finished with exit code 0.** Command: `node 'research_notes/Open conjecture transfer search/check_168_third_color.cjs' 10000`. It fixed each possible single vertex of the omitted color and optimized the remaining two-color cover by matching. All 10,000 choices were examined, with no improvement over 3,333; each baseline pair-color optimum was also 3,333. The terminal result is saved in `168_third_color_results.json` with `examined: 10000` and `found: null`. This checks only covers contained in two colors together with one additional vertex, not arbitrary three-color covers. No process from this round remains active.

### Gaps

The sharp lower bound, the proposed two-color theorem for balanced linear triangles, and #168 irrationality all remain unproved. The overall goal remains unmet.
