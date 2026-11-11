# Erdős 944: a complete transfer to every sufficiently large order

Date checked: 6 November 2026. No Lean formalization is attempted here.

## 1. What is the precise remaining statement?

**Takeaway.** The all-orders statement follows from the existing arbitrary-robustness four-color construction, with an explicit transfer bound. If a `(4,r)` graph of order `g` exists, then a `(4,r)` graph of every order `N >= 45g^2` exists. Consequently the Kohlmeyer–Kruer seed theorem implies `f_4(N) -> infinity`.

All graphs below are finite and simple. A `(4,r)` graph `G` satisfies

\[
\chi(G)=4,\qquad \chi(G-v)=3\ (v\in V(G)),\qquad
\chi(G-R)=4\ (R\subseteq E(G),\ |R|\le r).
\]

Here `r` is the number of edge deletions tolerated, so the smallest critical edge set has size **at least `r+1`**. It is not required that a critical edge set be inclusion-minimal.

Skottová–Steiner's [Problem 1.1](https://arxiv.org/html/2508.08703) defines `f_k(n)` to be the largest such tolerance `r >= 1` on order `n`, or zero if no such graph exists, and asks whether `f_k(n) -> infinity`. Their Theorem 1.2 proves this for `k >= 5`, with an `Omega(n^(1/3))` bound.

Kruer–Kohlmeyer's [Theorem 1.1](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-944.pdf) supplies a finite `(4,r)` graph for every integer `r >= 1`. Its introduction expressly excludes a claim for every sufficiently large order. The [Conjectures.io accepted target](https://conjectures.io/results/e7afff2c-bb07-4fa8-92b6-67a530aaad70) is the arbitrary-`r` existence statement, not the all-orders assertion.

**Attribution boundary.** The substitution used below is already Skottová–Steiner's Lemma 2.1, not a new gadget. The contribution of this note is the explicit cofinite order spectrum obtained from three critical skeletons and its combination with the four-color seed theorem. The proof is complete as a deduction from the cited seed theorem. Priority for the corollary has not been established by an exhaustive literature search.

## 2. Why does one seed give every sufficiently large order?

### The transfer theorem

**Theorem.** Let `r >= 1`. If a `(4,r)` graph of order `g` exists, then for every integer `N >= 45g^2` there is a `(4,r)` graph of order `N`.

We provide the construction and all criticality checks. A graph is called **4-critical** below if its chromatic number is four and every proper subgraph is three-colorable. This is stronger than vertex-criticality and is required of the skeletons.

### A. The known substitution, stated with its full mechanism

Fix a seed `G` of order `g`, a vertex `v`, and a proper three-coloring `phi` of `G-v`. Put

\[
A=N_G(v)\cap\phi^{-1}(1),\qquad B=N_G(v)\setminus A.
\]

Replace `v` by two nonadjacent terminals `a,b`, joining `a` to `A` and `b` to `B`. Call the resulting graph `S`. Its `c=g-1` internal vertices are the original vertices of `G-v`.

The following four properties are immediate but essential.

1. **Different terminal colors extend.** Extend `phi` with `a=2,b=1`. Permuting the three colors gives a proper coloring with any prescribed ordered pair of different terminal colors.
2. **Equal terminal colors cost more than `r` bad edges.** In any assignment of three colors to `S` with `a=b`, identifying the two terminals gives a color assignment to `G`, preserving the number of monochromatic edges exactly. If this number were at most `r`, deleting those edges would three-color `G`, contrary to the seed property.
3. **Deleting an internal vertex allows equal terminals.** For an internal vertex `w`, take a proper three-coloring of `G-w` and give both terminals the color of `v`. Any desired common color can be obtained by permutation.
4. **Deleting a terminal leaves the surviving terminal unrestricted.** Restrict a coloring from item 1 and permute colors.

Let `H` be any 4-critical graph. For each edge `xy` of `H`, use a fresh copy of `S`, identify its terminals with `x,y`, and delete the original edge `xy`. Distinct copies have disjoint internal vertices. Denote the resulting graph by `F(H)`; then

\[
|V(F(H))|=|V(H)|+c|E(H)|. \tag{1}
\]

We verify every defining property.

* Given any assignment of three colors to `F(H)`, its restriction to `V(H)` is improper for `H`. Some edge `xy` of `H` has equally colored endpoints. The corresponding copy of `S` has more than `r` monochromatic edges by item 2. Thus deleting any set of at most `r` edges cannot make `F(H)` three-colorable.
* Delete a skeleton vertex `x`. Properly three-color `H-x`. For a sender not incident with `x`, extend by item 1; for a sender incident with `x`, extend by item 4. Therefore `F(H)-x` is three-colorable.
* Delete an internal vertex `w` belonging to the sender replacing `e=xy`. Since `H` is edge-critical, `H-e` is three-colorable; in every such coloring `x,y` have the same color, since otherwise `H` would be three-colorable. Apply item 3 to the damaged sender and item 1 to every other sender. Thus `F(H)-w` is three-colorable.

The deletion statements show `chi(F(H)) <= 4` by adding one deleted vertex in a fourth color; robustness shows `chi(F(H)) >= 4`. Every vertex-deleted graph has chromatic number exactly three: if it were at most two, adding its deleted vertex would three-color `F(H)`. We have proved that `F(H)` is a `(4,r)` graph.

This is the equal-seed specialization of [Skottová–Steiner, Lemma 2.1](https://arxiv.org/html/2508.08703#S2.L1), whose more general version permits a different seed on each skeleton edge.

### B. Hajós joins preserve the required skeleton criticality

Take disjoint 4-critical graphs `H_1,H_2`, with selected edges `x_1y_1,x_2y_2`. Delete those edges, identify `x_1,x_2` to a vertex `x`, and add the edge `y_1y_2`. The resulting Hajós join `J` has

\[
|V(J)|=|V(H_1)|+|V(H_2)|-1,\qquad
|E(J)|=|E(H_1)|+|E(H_2)|-1. \tag{2}
\]

For completeness, `J` is 4-critical. In a hypothetical proper three-coloring, each copy `H_i-x_iy_i` must have `x_i,y_i` equally colored. Consequently `y_1,y_2` have the same color, contradicting their new edge. Four colors suffice: start with proper four-colorings of the two original graphs, align the colors of `x_1,x_2`, then permute the other three colors on the second copy so the colors of `y_1,y_2` differ.

Delete the new edge. Three-color both `H_i-x_iy_i`, where the selected endpoints necessarily have equal colors, and align those colors. Alternatively, delete an old edge `e` from `H_1` (other than its already removed selected edge). Three-color `H_1-e`: the selected endpoints differ because the selected edge is still present in that coloring. Three-color `H_2-x_2y_2`, whose selected endpoints agree, and align the colors at `x`. The new edge then has different endpoint colors. The same argument works for an old edge in `H_2`.

Every vertex of `J` has an incident edge (indeed a 4-critical input has minimum degree at least three, and the construction preserves positive degrees). A three-coloring after deleting an incident edge restricts to a three-coloring after deleting that vertex. Thus all edge and vertex deletions are three-colorable. Every proper subgraph omits an edge or a vertex, so `J` is 4-critical.

### C. Three explicitly verified skeletons

We use the following 4-critical graphs.

| Skeleton | Vertices | Edges | Increment in (1) when attached by a Hajós join |
|---|---:|---:|---:|
| `K_4` | 4 | 6 | `A=3+5c` |
| Odd wheel `W_5=K_1+C_5` | 6 | 10 | `B=5+9c` |
| Grötzsch graph `M(C_5)` | 11 | 20 | `C=10+19c` |

The first is immediate. For `W_5`, the odd rim cannot use only two colors, so a hub requires a fourth. Deleting a rim edge leaves a rim path, which can use two colors while the hub uses the third. Deleting a spoke allows its rim endpoint to share the hub's third color, while the remaining four-vertex rim path alternates the other two colors. There are no isolated vertices, so edge-criticality also implies vertex-criticality.

To remove any reliance on a claim about the Grötzsch graph, define it explicitly. Its vertices are

\[
v_0,\ldots,v_4,\ u_0,\ldots,u_4,\ w,
\]

with indices modulo five and edges `v_i v_(i+1)`, `u_i v_(i-1)`, `u_i v_(i+1)`, and `wu_i`. There are `5+10+5=20` edges. A three-coloring of the rim, copied to corresponding `u_i`, with a fourth color at `w`, proves four-colorability. In a hypothetical three-coloring, rename the color of `w` as 3; each `u_i` has color 1 or 2. Replace color 3 at a rim vertex `v_i` by the color of `u_i`. Two adjacent rim vertices could not both originally have color 3, and `u_i` is adjacent to both neighbors of `v_i`, so this gives a proper two-coloring of the odd cycle, a contradiction.

Rotations and reflections of the five indices are automorphisms and give three edge orbits. The following explicit assignments show that deleting one representative from each orbit allows three colors. A tuple lists colors at `(v_0,...,v_4;u_0,...,u_4;w)`.

| Deleted edge | Proper coloring of the remaining graph |
|---|---|
| `v_0v_1` | `(2,2,0,2,0; 1,1,1,1,1; 0)` |
| `v_0u_1` | `(2,0,1,2,0; 1,2,1,2,1; 0)` |
| `u_0w` | `(0,1,0,1,2; 0,1,2,1,2; 0)` |

Each assignment can be checked directly against the displayed adjacency rule. There are no isolated vertices, so the graph is 4-critical.

### D. The order spectrum is cofinite

Start with `K_4`, and perform any nonnegative numbers `a,b,d` of attachments of the three skeletons, respectively. Equations (1) and (2) give a `(4,r)` graph of every order

\[
N=b_0+aA+bB+dC,\qquad b_0=4+6c, \tag{3}
\]

where

\[
A=3+5c,\qquad B=5+9c,\qquad C=10+19c.
\]

The identity

\[
9A-5B=2 \tag{4}
\]

is the crucial arithmetic point. If `c` is even, both `A,B` are odd, hence they are coprime. If `c` is odd, both are even, `A/2,B/2` are coprime, and `C` is odd.

We use the elementary two-generator bound: for coprime positive integers `p,q`, every integer `m >= (p-1)(q-1)` equals `ap+bq` with `a,b >= 0`. Indeed select `b` in `{0,...,p-1}` so that `bq` has residue `m` modulo `p`. Then `m-bq >= -(p-1)>-p`, and being divisible by `p` it must be nonnegative.

* If `c` is even, every `N >= b_0+(A-1)(B-1)` has form (3), with `d=0`.
* If `c` is odd, put `T=(A/2-1)(B/2-1)`. For `N >= b_0+C+2T`, select `d` in `{0,1}` so that `N-b_0-dC` is even. This difference is at least `2T`; divide it by two and apply the preceding bound to `A/2,B/2`.

In terms of seed order `g=c+1`, these sufficient thresholds are

\[
N_0(g)=
\begin{cases}
45g^2-46g+13,&g\text{ odd},\\
\frac{45}{2}g^2-8g+1,&g\text{ even}.
\end{cases} \tag{5}
\]

Both are at most `45g^2`. This completes the proof of the transfer theorem.

### E. The conclusion for Erdős 944

Fix any integer `r >= 1`. The Kruer–Kohlmeyer theorem supplies a `(4,r)` seed of some finite order `g_r`. The transfer theorem supplies a `(4,r)` graph at **every** order `N >= 45g_r^2`. Thus

\[
\forall r\ge1\ \exists N_r\ \forall N\ge N_r:\quad f_4(N)\ge r.
\]

This is precisely

\[
\boxed{\lim_{N\to\infty}f_4(N)=\infty.}
\]

No monotonicity of `f_4` is assumed or needed. The quantifier order comes directly from the uniform tail produced for each fixed `r`.

## 3. What was checked, and what is the remaining boundary?

**Mathematical status.** The all-orders gap is closed by the displayed deduction, assuming the published seed theorem. There is no missing extension, criticality, congruence, or parity step. This is not a claim that the entire seed construction was independently reverified here; that deep theorem is the imported input, just as one normally uses a cited theorem.

**Novelty status.** The current versions of the two primary papers were compared. Skottová–Steiner's Lemma 2.1 already contains the substitution, and Lemma 2.2 already uses Hajós joins. Their Theorem 2.3 obtains all orders for `k >= 5` using seeds in an arithmetic progression with varying orders; it does not state the above single-seed transfer for `k=4`. Kruer–Kohlmeyer's introduction explicitly does not claim all sufficiently large orders. Targeted searches did not locate the specific corollary, but this establishes a distinction in the checked sources, not global priority.

**Why the deep construction need not be padded directly.** Its order constraints can be avoided entirely. For reference, its seed parameters have `q=3t+1` coprime to 15, `t` equal to `r` or `r+1`; `D=30q`, `M=150q`; `a_0=1`, `a_j=5d_j`, and `d_j=D(kappa_j-1)+1`. With `P=5 product_j d_j` and `L=3P`, the seed order satisfies compatible congruences

\[
n\equiv1\pmod3,\qquad n\equiv0\pmod q,\qquad
n\equiv-\kappa_j^{-1}\pmod{a_j},
\]

and `n>1000(r+1)qL^2`. These orders lie in a fixed arithmetic progression of step `qL`. The theorem above consumes just one such seed; all later control of the order takes place in the critical skeleton. It does not require the cyclic construction to survive isolated padding, vertex duplication, or changed congruences.

**Validation.** The proof includes explicit edge-deletion certificates for all three symmetry classes of the 20-edge Grötzsch skeleton. An independent finite search also confirmed its non-three-colorability and the three-colorability of all 20 edge deletions and all 11 vertex deletions. The mathematical proof does not depend on that search. The polynomial thresholds in (5) were expanded from the exact two-generator conductors, and the identity used is `9A-5B=2`.

**Limits.** Formula (5) is an explicit bound in the size of an available seed, not an optimized bound in `r`. We have not claimed an optimal growth rate for `f_4(N)`, an independent verification of the Lean code, or publication priority for this corollary.
