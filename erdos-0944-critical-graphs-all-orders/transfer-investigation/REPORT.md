# Completing every large order for Erdős 944

**The successful transfer proves the all-orders strengthening associated with Erdős #944:** combining Kohlmeyer–Kruer's existence theorem with the argument below gives $f_4(N)\to\infty$. The precise new deduction is that **one suitable seed graph on $g$ vertices produces suitable graphs on every $N\ge45g^2$ vertices**, with the same edge-deletion tolerance. Their manuscript supplies a seed for every tolerance but explicitly stops short of claiming every sufficiently large order. The construction uses Skottová–Steiner's published substitution lemma, followed by an arithmetic completion using three small critical graphs. The complete proof is supplied in the [standalone mathematical manuscript](<../erdos944-all-orders-transfer.tex>); its dependency is the stated Kohlmeyer–Kruer seed theorem. Publication priority for this combination remains unverified. ([Seed theorem](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-944.pdf), [published substitution and all-orders question](https://arxiv.org/html/2508.08703))

## The seed theorem leaves a precise all-orders gap

Call a finite simple graph a **$(4,r)$-graph** when it has chromatic number four, deleting any vertex lowers that number to three, and deleting any set of at most $r$ edges leaves its chromatic number four. Let $f_4(N)$ be the largest $r\ge1$ for which such a graph on exactly $N$ vertices exists, with value zero if there is none. Here $r$ is the deletion tolerance; the smallest edge set that lowers the chromatic number has size at least $r+1$. Skottová–Steiner ask whether $f_k(N)\to\infty$, and prove a quantitative result for $k\ge5$. Their stated result leaves $k=4$ open. ([Problem 1.1 and Theorem 1.2](https://arxiv.org/html/2508.08703))

Kohlmeyer–Kruer prove that a finite $(4,r)$-graph exists for every $r\ge1$. Existence at some order for each $r$ does not by itself establish a limit over **all** orders. Adding isolated vertices or taking disjoint unions would destroy vertex-criticality. The required additional statement is the following theorem. ([Theorem 1.1 and introductory scope statement](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-944.pdf))

**Order-completion theorem.** If a $(4,r)$-graph on $g$ vertices exists, then a $(4,r)$-graph exists on every integer $N\ge45g^2$.

For any fixed $r$, choose a seed of order $g(r)$. The theorem gives $f_4(N)\ge r$ for every $N\ge45g(r)^2$. Since $r$ is arbitrary, this proves

\[
\boxed{\lim_{N\to\infty}f_4(N)=\infty.}
\]

The proof supplies the missing quantifier over every sufficiently large order. It does not require a uniform or explicit estimate for $g(r)$.

## Three critical graphs fill every sufficiently large order

Write $c=g-1$. A **4-critical skeleton** means a four-chromatic graph that becomes three-colorable after deletion of any edge or any vertex. This stronger criticality condition belongs to the skeleton, not to the robust seed. The equal-seed case of Skottová–Steiner's substitution lemma says that a skeleton $H$ produces a $(4,r)$-graph of order

\[
|V(H)|+c|E(H)|. \tag{1}
\]

Here is the mechanism and its criticality check. Choose a vertex $v$ of the seed $G$, and properly three-color $G-v$. Split $v$ into two nonadjacent terminals: attach the neighbors of color 1 to the first terminal and all other neighbors to the second. The resulting gadget $S$ has $c$ internal vertices. It is three-colorable with distinct terminal colors, by assigning the terminals colors 2 and 1. Any assignment of three colors with equal terminal colors has at least $r+1$ monochromatic edges, because identifying the terminals recovers $G$. Deleting an internal vertex permits equal terminal colors, using a coloring of the corresponding vertex-deleted seed. Deleting either terminal leaves a three-colorable graph. Permuting colors realizes any prescribed distinct pair, common color, or surviving terminal color in these statements. ([Lemma 2.1](https://arxiv.org/html/2508.08703))

Replace every edge of $H$ by a separate copy of $S$, deleting the original skeleton edge and identifying the gadget's terminals with its endpoints. A proper four-coloring of $H$ extends over all gadgets. Every three-color assignment on the resulting graph has a monochromatic skeleton edge when restricted to $V(H)$; its gadget therefore has at least $r+1$ monochromatic edges. Deleting at most $r$ edges cannot produce a three-colorable graph.

Vertex-criticality requires two checks. If an internal vertex of the gadget replacing $xy$ is deleted, properly three-color $H-xy$. Its endpoints necessarily have equal colors, so the punctured gadget can be colored; every other gadget has distinct terminal colors. If a skeleton vertex is deleted, properly three-color the punctured skeleton. Each incident gadget has lost one terminal and can extend the color at its surviving terminal. Thus every vertex deletion is three-colorable, and (1) follows by counting the disjoint interiors. This is the published substitution proof, credited above, rather than a newly claimed gadget.

Use these three skeletons:

| Skeleton | Vertices | Edges |
|---|---:|---:|
| $K_4$ | 4 | 6 |
| A five-cycle with an additional universal hub | 6 | 10 |
| $M(C_5)$, the Grötzsch graph | 11 | 20 |

They are all 4-critical. For the wheel, deleting a rim edge leaves a path that needs two colors, while deleting a spoke allows its endpoint to share the hub's color. For $M(C_5)$, the manuscript gives its full edge definition, the standard proof of four-chromaticity, and explicit three-colorings for each of its three edge-deletion symmetry classes. Thus this small ingredient can be checked without trusting a solver.

A **Hajós join** of two disjoint skeletons deletes one edge $a_ib_i$ from each, identifies $a_1,a_2$, and inserts $b_1b_2$. It remains 4-critical and changes the vertex and edge counts by

\[
v(H_1\mathbin{\star}H_2)=v(H_1)+v(H_2)-1,
\qquad
e(H_1\mathbin{\star}H_2)=e(H_1)+e(H_2)-1.
\]

To see criticality, any three-coloring of an edge-deleted summand forces its distinguished endpoints to agree, which makes the newly inserted edge impossible to color. Deleting that new edge permits both summands to be colored. Deleting an old edge permits a coloring in which the distinguished endpoints in its summand differ, while those in the other summand agree. Matching colors at the identified vertex then colors the join. Every vertex has an incident edge, so edge-deletion colorability also gives vertex-deletion colorability. Four-colorability follows by permuting four colors on one summand. The operation is also used in the cited paper. ([Lemma 2.2](https://arxiv.org/html/2508.08703))

Start with $K_4$, and take any nonnegative numbers $a,b,d$ of Hajós joins with copies of the three displayed skeletons. Formula (1) gives every order

\[
N=6g-2+a(5g-2)+b(9g-4)+d(19g-9). \tag{2}
\]

Put $A=5g-2$, $B=9g-4$, and $C=19g-9$. The essential arithmetic identity is

\[
9A-5B=2.
\]

If $g$ is odd, $A,B$ are odd and coprime. Every integer at least $(A-1)(B-1)$ is a nonnegative combination of $A,B$. Equation (2), with $d=0$, therefore realizes every

\[
N\ge6g-2+(A-1)(B-1)=45g^2-46g+13.
\]

If $g$ is even, $A,B$ are even, $A/2,B/2$ are coprime, and $C$ is odd. For a remainder $t=N-(6g-2)$, subtract either zero or one copy of $C$ to make the remainder even. The same two-generator bound then applies after division by two. It is sufficient that

\[
N\ge6g-2+C+2(A/2-1)(B/2-1)
=\frac{45}{2}g^2-8g+1.
\]

Both thresholds are at most $45g^2$. The elementary conductor fact used here has a short proof: for coprime $u,v$, choose $j\in\{0,\ldots,u-1\}$ with $jv\equiv t\pmod u$. If $t\ge(u-1)(v-1)$, then $t-jv>-u$; since it is a multiple of $u$, it is nonnegative. This completes the order-completion theorem.

## The portfolio screen identifies which other transfers remain open

The inspected portfolio distinguishes original mathematical results, separately solved parts, and formalizations of other authors' work. The table records the relevant scopes rather than treating every numbered problem as wholly settled. It is a substantial verified selection, not a certified exhaustive bibliography. ([Authors' portfolio](https://github.com/JENW1N/complete-math-solutions/blob/main/README.md))

| Source result | Established scope and transfer assessment |
|---|---|
| [#14](https://conjectures.io/results/dce3d778-6f52-4c27-8da0-c82d2f391b64) | At least $\sqrt N/12000$ integers up to $N$ fail unique unordered additive representation, for $N\ge2\cdot10^{24}$. It does not force unbounded multiplicities as required for #28. |
| [#18(b)](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos18b-factorial-divisors.pdf) | $h(n!)=n^{o(1)}$. The stronger fixed-polylogarithmic part (c) still needs a uniform estimate absent from this theorem. |
| [#96 and #97, with Liam Price](https://github.com/lkruer/erdos-96-97-proof/blob/0e98f5f9bdaf36007e3eb405cbefe2eda778a9b2/README.md) | Strictly convex unit-distance constructions with unbounded minimum degree and superlinear edge count. |
| [#108](https://arxiv.org/html/2609.40192) | High-chromatic triangle-free graphs with uniformly colorable $C_4$-free subgraphs. The current Nguyen–Walczak paper already states the $K_{s,t}$ extension and broader avoidability classification. |
| [#196](https://conjectures.io/results/e73b95f7-1d1b-42b5-a442-c07077741d73) | A permutation of all natural numbers avoiding monotone four-term arithmetic progressions. The generic proposed implication to a two-part solution of #197 is false. |
| [#272, strong linear-error variant](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-272.pdf) | An $N^2/2+O(N)$ upper bound. The exact extremum remains beyond the structural theorem's linear losses. |
| [#354(i)](https://github.com/JENW1N/complete-math-solutions/blob/main/proofs/erdos354/PROOF.md) | Completeness of two interleaved doubling sequences with irrational ratio. Other base-related assertions have separate authors and scopes. |
| [#859](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos859-divisor-sums.pdf) | A critical logarithmic exponent and a vanishing normalized density, not a full asymptotic. |
| [#944](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-944.pdf) | Arbitrary-tolerance seed existence. The proof above completes the stronger all-orders implication. |
| [#1062](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf) | The manuscript gives an exact fork-free extremal formula as well as an irrational density, so part (i) is already covered mathematically. |
| [#1057, with Howe and Huffman](https://github.com/JENW1N/erdos1057-lean) | A claimed near-linear-exponent Carmichael counting theorem. Its deep analytic inputs were not audited here and are not used in the successful transfer. |

The #196 obstruction is useful for avoiding a false proof. Ternary digit-reversal order on $\{0,\ldots,3^m-1\}$ contains no monotone four-term progression: at the first ternary digit changed by its common difference, the first and fourth terms have the same digit and the middle terms have the other two digits. Yet Hales–Jewett combinatorial lines force monochromatic monotone three-term progressions under any fixed number of colors for sufficiently large $m$. An exact finite check already finds the two-color obstruction at $m=3$. This disproves the universal finite transfer lemma; it does not disprove #197, whose partition and orderings can have additional structure. ([#197 statement](https://www.erdosproblems.com/197))

A secondary consequence of the exact #1062 formula is the explicit bound

\[
|f(n)-cn|\le\frac{10}{3}\log_4n+\frac83\log_3n+9,
\]

where $c$ is the authors' irrational density. Its proof uses signed jumps of their step function and the discrepancy $\left|\#\{m\le y:(m,6)=1\}-y/3\right|\le2/3$. The full calculation is in the [quantitative proof note](<../../meta/theorem-transfer-survey/1062_quantitative.md>). This is a convergence-rate corollary of an already solved problem, with no asserted optimality or priority.

## Verification and the remaining limits

Two independent mathematical reviews found no gap in the #944 transfer. The small Grötzsch skeleton was checked for all twenty edge deletions, and the manuscript includes explicit certificates and a non-three-colorability proof, so its role is fully inspectable without software. The conductor thresholds were checked in both parity cases. The #1062 calculations separately matched an integer optimization model at 37 sample sizes and two exact formula implementations through $n=400$; those finite checks support the implementation, not the universal theorem by themselves.

The #944 proof uses Kohlmeyer–Kruer's stated seed theorem as its external mathematical input; it does not independently re-prove that construction. Skottová–Steiner receive credit for the substitution lemma. The bounded source search found no published statement of this single-seed order-completion argument, but it does not establish first-discovery priority. No explicit growth rate for $f_4(N)$, Lean formalization, or compiled PDF is claimed. The delivered result is the complete elementary implication from one seed to all sufficiently large orders, and consequently from their seed-existence theorem to the limit $f_4(N)\to\infty$.
