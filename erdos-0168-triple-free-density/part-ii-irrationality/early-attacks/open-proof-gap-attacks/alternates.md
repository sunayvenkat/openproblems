# Alternate exact targets: verified obstructions, no new closure

Checked 7 November 2026 UTC, 6 November in the user's timezone. The coordinator is pursuing #168 separately. Its [live part-ii page](https://conjectures.io/problems/erdos168-erdos-168-parts-ii) was rechecked: no complete attempt or published contribution, and the target remains irrationality of the limsup of F(N)/N. This file records two alternate attacks and a requested follow-up on the audited #944 seed. None settles a different open catalog target; no novelty claim is made for the elementary auxiliary lemmas.

## Can the full convex unit-distance construction refute #982?

### Takeaway

No, when placed in the two sufficiently small disks used by its construction. The exact radial support inequality implies an endpoint of the larger cluster determines at least ceil(n/2) distances. This rules out the whole narrow-two-disk radial-support family, including the source's deletion and rotated-copy operations, rather than merely showing that its unit-degree lower bound is insufficient.

### Cited Findings

- The [live #982 page](https://conjectures.io/problems/erdos982-erdos-982) remains open. Its exact statement requires a vertex with at least floor(n/2) distinct distances in every convex n-gon; it has one API contribution and no complete attempted solution.
- The [pinned Kruer–Kohlmeyer–Price manuscript](https://raw.githubusercontent.com/lkruer/erdos-96-97-proof/0e98f5f9bdaf36007e3eb405cbefe2eda778a9b2/96-97.tex) gives the finite construction with both two-disk localization and the strict inequality <p,q-p><0 for all distinct points. The rotated-copy lemma preserves this inequality and localization. The prescribed-cardinality proposition explicitly retains both properties.
- Endpoint distance monotonicity for caps is classical: the discussion following Definition 5 of [Nivasch–Pach–Pinchasi–Zerbib](https://www.renyi.hu/~pach/publications/distdist042512.pdf) attributes the cap framework to Moser and Dumitrescu and states the increasing endpoint-distance property. Thus the elementary monotonicity below should not be advertised as a novel geometry theorem. The useful new deduction in this search is checking that the source construction falls into this restricted class.

### Inferences

**Quantified no-go lemma.** Let 0<eta<1/4, and let P be a finite set of n>=3 nonzero planar points satisfying

    <p,q-p> < 0                  for all distinct p,q in P,
    P subset B((0,1/2),eta) union B((0,-1/2),eta).

Then some point of P determines at least ceil(n/2) distinct distances to P minus itself. Consequently P satisfies #982.

**Proof of the radial-sector lemma.** First let Q lie in an angular sector of width less than pi/2 and satisfy the displayed support inequality. No two distinct points can lie on the same ray: the support inequalities in both orders would require each radius to be smaller than the other. List its points in increasing polar angle as p_1,...,p_m.

Let J be counterclockwise rotation through pi/2. For i<j, set w=p_j-p_i and Delta=det(p_i,p_j)>0. The support inequalities give

    <p_i,w><0,                 <p_j,w>>0.

The exact decomposition

    w = (<p_j,w>/Delta) J p_i + (-<p_i,w>/Delta) J p_j

therefore expresses each forward chord as a positive linear combination of two radial tangent vectors. All these tangent vectors have pairwise positive dot products because the sector has width less than pi/2. Hence any two forward chords have positive dot product. In particular, for 1<i<j,

    |p_j-p_1|^2
      = |p_i-p_1|^2 + |p_j-p_i|^2
        + 2<p_i-p_1,p_j-p_i>
      > |p_i-p_1|^2.

Thus the m-1 nonzero distances from p_1 to the rest of Q are strictly increasing. Equivalently, Q is a strict cap. The same conclusion holds at its other angular endpoint.

**Application to the two disks.** Each disk subtends angle 2 arcsin(2 eta)<pi/2 at the origin. If both clusters are nonempty, choose the larger cluster Q, of size m>=ceil(n/2), and its angular endpoint p_1. Its m-1 internal distances are distinct and are all less than 2 eta. Every distance from p_1 to the other cluster is greater than 1-2 eta>2 eta, providing one more distinct distance. Thus p_1 has at least m>=ceil(n/2) distances. If one cluster is empty, the endpoint has n-1 distances, also sufficient. This proves the lemma.

**Scope of the exclusion.** Apply the source construction with any eta<1/4. Its exact point sets, induced subsets, and the final prescribed-cardinality rotated unions all satisfy the lemma. No accidental equalities among other distances can defeat this conclusion: the proof counts actual strictly ordered distances, not only the coincidences guaranteed by the construction.

### Gaps

- This proves no unrestricted #982 theorem and rules out no modification that abandons the two narrow disks or radial support condition.
- This does not settle the regular-polygon energy target #94. Its energy threshold is different, and the endpoint argument is not an upper bound on full distance energy.
- No computational or Lean replay was needed or performed for this analytic deduction. Literature priority is not asserted.

## Can the high-chromatic construction refute proportionate dissociation in #774?

### Takeaway

The natural graph-to-integer dependency encoding fails quantitatively. A graph of chromatic number greater than q has an encoded finite subset for which every dissociated subset has relative size less than 2/q. Consequently infinitely many high-chromatic blocks cannot retain the global positive proportional constant required by #774.

### Cited Findings

- [The live #774 page](https://conjectures.io/problems/erdos774-erdos-774) remains offered with no complete attempt. The [formal definition](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/774.lean) requires one c>0 working for every finite B subset A; each such B must contain a dissociated subset of size at least c|B|. Dissociated means distinct finite subsets have distinct sums.
- The Kohlmeyer–Kruer #108 construction supplies arbitrarily high-chromatic graphs. Its additional restriction on C4-free subgraphs and the bounded-degree base-graph lemma are described in [Nguyen–Walczak, current version](https://arxiv.org/html/2609.40192). Those restrictions do not prevent the critical subgraphs used below.

### Inferences

**Exact finite encoding.** Number the vertices of a finite graph G by 0,...,v-1. Choose an integer B>max(Delta(G),2), and attach the positive integer

    a_{ij}=B^j-B^i                 (i<j)

to every edge ij. These integers are distinct. A subset of them is dissociated if and only if its edges form a forest.

To prove this, a signed subset-sum relation becomes

    sum_edges epsilon_ij (B^j-B^i) = sum_i c_i B^i = 0,
    epsilon_ij in {-1,0,1},       |c_i|<=Delta(G)<B.

Reduction modulo B and induction force every c_i=0. A nonzero circulation cannot be supported on a forest, by successively removing leaves. Conversely, an undirected cycle gives a signed telescoping relation with each edge coefficient +1 or -1. The same coefficient-uniqueness argument also proves distinctness of the edge labels.

**Quantitative obstruction.** Suppose chi(G)>q. Choose a vertex-minimal subgraph H with chromatic number k=chi(G); it has minimum degree at least k-1>=q. Therefore

    |E(H)| >= q |V(H)| / 2.

Every dissociated subset of the integer labels for E(H) is a forest and hence has at most |V(H)|-1 elements. The best possible proportional constant on this finite subset is at most

    (|V(H)|-1)/|E(H)| < 2/q.

This tends to zero along the arbitrarily high-chromatic Kohlmeyer–Kruer graphs. Separating integer blocks far apart, to prevent relations between blocks, cannot remove these within-block obstructions. Thus this exact encoding cannot produce a counterexample to #774.

**Stronger structural reason.** If a finite graph's exact forest encoding did have a fixed proportional constant c, then every nonempty subgraph F would satisfy c|E(F)|<=|V(F)|-1. Its average degree is therefore less than 2/c. It is D-degenerate for D=ceil(2/c)-1. Order vertices by a degeneracy ordering and assign different edge colors to the at most D forward edges at each vertex. Each color class is a forest: the earliest vertex on a purported monochromatic cycle would have two forward edges of the same color. The corresponding integer set is a union of D dissociated sets. This shows why this graph encoding cannot contradict the target even before selecting the special source graphs.

### Gaps

- The result concerns the specified difference-of-powers encoding, not every conceivable realization of graph constraints by subset sums.
- A successful transfer would need a different dependency system whose chromatic obstruction persists while every finite part retains a uniform dissociated fraction. The source's bounded-degree suppression alone supplies no such system here.
- No closure of #774 or originality claim for the graphic-matroid argument is made.

## Does the audited #944 seed have a useful additional graph property?

### Takeaway

Yes: the actual parameter construction is triangle-free. However, its total edge count is less than n^2/50. It therefore does not challenge the nearby live #23 or #128 targets. This is a checked feature and a quantified limitation of the seed, not a new solution of #944 or another catalog problem.

### Cited Findings

- The [audited pinned #944 manuscript](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos-944.pdf) defines N_n={1,n-1} union {s:0<s<n, s=2 mod 3}, n=1 mod 3; the core has S subset a_i N_n for each of q=3t+1 unit directions. Chords of type i have differences ell a_i, ell in {4,7,...,q}. Its parameter bounds and CRT blocks are checked in the companion audit notes.
- [#23](https://conjectures.io/problems/erdos23-erdos-23) asks whether a triangle-free graph of order 5m can be made bipartite after deleting at most m^2 edges. [#128](https://conjectures.io/problems/erdos128-erdos-128) asks whether a graph of order n whose every induced subgraph on at least n/2 vertices has more than n^2/50 edges must contain a triangle. Both were rechecked live and remain offered. The exact #128 Lean premise uses 2|V'|+1>=n, equivalently |V'|>=floor(n/2); the distinction from the displayed prose does not affect the full-vertex-set obstruction below.
- A focused primary-source feature check found no occurrence of triangle/girth terminology in the pinned #944 manuscript text or its accompanying Lean file, nor in [Skottova–Steiner's primary paper](https://arxiv.org/html/2508.08703). Targeted searches did not locate an explicit prior statement of this extra seed property. This limited negative search does not certify novelty, and no priority claim is made.
- The saved [live catalog](https://conjectures.io/problems) has no remaining entry asking for triangle-free vertex-critical four-chromatic graphs with arbitrary critical-edge-set size. Its similarly named Vizing independence entry concerns edge-chromatic Delta-criticality. The [precise #600 definition](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/600.lean) assumes every edge lies in a triangle; the [#87 target](https://conjectures.io/problems/erdos87-erdos-87-parts-i) is asymptotic in a growing chromatic number. Neither is a direct consequence of a triangle-free seed with chromatic number four.

### Inferences

**Triangles of the normalization graph.** Every triangle of Cay(Z/nZ,N_n) consists of three cyclically consecutive vertices, so one of its edges has difference +2 or -2. To see this, translate and sort its vertices as 0<a<b<n. If a and b are both 2 modulo 3, then b-a is 0 modulo 3 but is neither 1 nor n-1, a contradiction. The only other possibilities involve a=1 or b=n-1. Checking b-a in N_n leaves exactly {0,1,2}, {0,n-2,n-1}, and {0,1,n-1}.

**No doubled unit direction occurs in the actual seed.** Put R_hi=[a_h a_i^{-1}]_n. For h!=i the audited construction gives R_hi=2 modulo 3 and 0<R_hi<n/q. Fix h.

- A core edge of difference 2a_h would normalize in coordinate i!=h to 2R_hi. This is strictly between 0 and n/2, is 1 modulo 3, and is at least 4. Hence it is not in N_n, contrary to the defining intersection for S. Symmetry excludes -2a_h too.
- A chord of type h cannot have difference +/-2a_h because 4<=ell<=q<n-2.
- For a chord of type i!=h, the equality would require 2R_hi=ell or 2R_hi=n-ell. Neither occurs: q<2R_hi<n-q. The upper bound follows from R_hi<n/q, q>=4 and n>2q. For the lower bound, if i=0, then R_h0=a_h>=750q+5. If i>0, the audited exact ratio formula is R_hi=(a_h+e n)/a_i with a positive residue e, so R_hi>n/a_i>q, since a_i<=L/3 and n>1000(r+1)qL^2. Positivity of e follows from the pairwise coprimality of the d_i and a_i=5d_i; the h=0 case has e=kappa_i>0.

Now suppose G had a triangle. Assign a chord type to each of its edges outside the core. At most three types occur, and q>=4, so choose h outside those types. Every core edge normalizes into N_n by condition (i); each selected chord normalizes into N_n by condition (ii). The normalized triangle must have a +/-2 edge by the preceding classification. Thus G contains an edge of difference +/-2a_h, which was just excluded. This proves triangle-freeness of the actual seed.

Its girth is exactly four: the core contains the cycle 0,a_0,a_0+a_1,a_1,0. Its four vertices are distinct because a_0,a_1 are nonzero and their direction pairs are distinct. All four edges are core edges. Thus this extra property does not supply seeds of arbitrarily large girth.

**Density calculation.** Put m_j=(d_j-1)/3 for the q-1 nontrivial CRT coordinates. The number of generic residue classes modulo L=15 product d_j is

    A = product_j(m_j+1) + 4 product_j m_j.

Since d_j>8 and q>=4,

    A/L <= (1/3) (11/27)^(q-1) <= 1331/59049 < 1/40.

Outside these generic classes at most the 2q special signed unit directions need be included. Counting representatives below n gives

    |S| <= n/40 + L/40 + 2q.

There are n designated chord blocks in total: q types, each with n/q blocks. A block contributes at most

    sum_{j=1}^t (q-3j) = (q-1)(q-2)/6 <= q^2/6

added edges. Identifications only lower this count. Consequently

    |E(G)|/n^2 <= 1/80 + L/(80n) + q/n + q^2/(6n).

The actual parameters satisfy L>q and n>1000(r+1)qL^2. In particular each of L/n, q/n, and q^2/n is less than 1/1000. Therefore

    |E(G)|/n^2
      < 1/80 + 1/80000 + 1/1000 + 1/6000
      = 3283/240000
      < 1/50.

For #23, whenever the order is divisible by five, deleting every edge already costs less than n^2/50<n^2/25. For #128, the full vertex set itself fails the required edge lower bound. Thus the seed's newly checked triangle-freeness does not give either desired counterexample.

### Gaps

- Triangle-freeness was derived from the full quantitative CRT parameters. It is not claimed for every abstract instance satisfying only the four-item construction criterion.
- No exact remaining catalog target was found that is resolved by triangle-free four-chromatic vertex-critical graphs with arbitrary edge robustness.
- A quantitative order estimate would still concern the excluded #944 family. The all-orders existence bridge was already explicit in the [2 October primary proof](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/PROOF.md); improving a seed-size or bridge constant would not meet the request for a different currently open catalog entry.
- No exhaustive computation of the enormous graph or Lean formalization of these auxiliary deductions was performed. These are direct mathematical arguments, with the audited seed assumptions made explicit.
