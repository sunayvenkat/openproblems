# Kohlmeyer and Kruer source results

## Which results and scopes can be attributed to them?

### Takeaway

The authors have substantially more relevant work than the headline results on convex unit distances and high-chromatic graphs. Their public portfolio distinguishes original mathematical results from formalizations of others' results. The statements below were checked against primary manuscripts or source files; no Lean replay was performed in this investigation. Current user-facing date: 6 November 2026.

### Cited Findings

- **Portfolio and attribution.** The joint repository lists Erdős 14(i),(ii), 108, 859, 944, 1062(ii), 18(b), the Szabó strong variant of 272, and 354(i). It explicitly credits Samuel Korsky with the mathematics of their 790 formalization, and credits Kenta Kitamura and Jesse Geneson for relevant 354(ii) mathematics. Its scope table must not be treated as a claim to every part of every numbered problem. [Authors' portfolio](https://github.com/JENW1N/complete-math-solutions/blob/main/README.md).

- **Erdős 14.** For any A⊆N, let E_A(N) count integers 1 through N having other than exactly one unordered representation as a sum of two elements of A; equal summands are allowed. Their result is E_A(N)>sqrt(N)/12000 for every A and N≥2×10^24. This proves the N^(1/2−epsilon) lower bound and rules out E_A(N)=o(sqrt N). Conjectures.io certified part (i) on 16 September 2026; the shared manuscript treats both parts. [Primary result record](https://conjectures.io/results/dce3d778-6f52-4c27-8da0-c82d2f391b64).

- **Erdős 18(b).** For practical N, define h(N)=max_{1≤R≤N} min{|D|: D is a set of positive divisors of N and sum D=R}. They prove h(n!)<n^delta eventually for every delta>0. A stronger local theorem says: for each eta>0 there are C_eta,K_eta>0 such that every integer R≥1 is a sum of at most C_eta(1+log log(R+3))^K_eta distinct positive divisors of ceil(C_eta(log(R+3))^(1+eta))!. The paper explicitly says its bounds do not prove the fixed-polylogarithmic question 18(c). [Theorems 1.1–1.2, primary manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos18b-factorial-divisors.pdf).

- **Erdős 96 and 97, with Liam Price.** For all sufficiently large n, uniformly in 0<eta<1/2, there is a strictly convex n-point planar set P in the two disks B((0,±1/2),eta) with min{delta_1(P),u(P)/n}≥(1/4)log_2 log_2 n−7log_2 log_2 log_2 n. Here u counts unordered unit-distance pairs and delta_1 is minimum unit-distance degree. The full unit-distance graph is bipartite. This disproves linearity in 96, the four-neighbor assertion in 97, and every fixed-k analogue. [Pinned authors' README](https://github.com/lkruer/erdos-96-97-proof/blob/0e98f5f9bdaf36007e3eb405cbefe2eda778a9b2/README.md).

- **Erdős 108.** Their original theorem gives, for every k, a triangle-free graph of chromatic number >k whose C4-free subgraphs are all 6-colorable. Nguyen and Walczak explain the argument independently and improve 6 to 3. The CURRENT version additionally proves the K_{s,t} extension as Theorem 1.6 and the full chi-avoidability classification as Theorem 1.7, credited to Steiner. The K_{s,t} consequence is therefore already known, even though it was not stated in version 1. [Current primary exposition](https://arxiv.org/html/2609.40192).

- **Erdős 196.** A bijection of all natural numbers exists containing no four-term arithmetic progression in either increasing or decreasing value order along increasing positions. The accepted record describes finite saturation and an extension lemma producing nested finite stages; injection and surjection are established separately. The source uses orders determined by the first differing low binary digit. This is not just a positive-density subset or an odd-common-difference result. [Primary result and review](https://conjectures.io/results/e73b95f7-1d1b-42b5-a442-c07077741d73), [635-line source](https://conjectures.io/results/e73b95f7-1d1b-42b5-a442-c07077741d73/solution).

- **Erdős 272, Szabó strong variant.** Let t(N) be the maximum size of a family of DISTINCT subsets of [N] such that intersections of distinct members are nonempty finite arithmetic progressions. Singletons and arbitrary two-element sets count as progressions. They prove eventually binom(N,2)+1≤t(N)≤N²/2+30000N. The lower construction consists of all sets of size at most three containing one fixed point. Their theorem does not determine the linear term or exact maximum. [Theorem 1.1, primary manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-272.pdf).

- **Erdős 354(i).** For positive alpha,beta with alpha/beta irrational, the interleaving floor(alpha·2^n), floor(beta·2^n), n≥0, is complete: every sufficiently large integer is a sum of distinct indexed occurrences. Repeated integer values at different indices remain separately available. Kitamura proved an existential base in (1,2), in fact gamma=sqrt(golden ratio) works even for a single sequence. Geneson previously disproved the universal-base assertion; Kohlmeyer's later six-term recurrence gives a separately formalized example. None of these results classifies all bases. [Primary scope and proof note](https://github.com/JENW1N/complete-math-solutions/blob/main/proofs/erdos354/PROOF.md).

- **Erdős 859.** Let d_t be the natural density of positive integers n for which t is a sum of distinct positive divisors of n. Let delta=1−(1+log log 2)/log 2≈0.0860713320. They prove liminf_{t→infinity}(−log d_t)/(log log t)=delta and (log t)^delta d_t→0. These two assertions rule out d_t asymptotic to c/(log t)^p for any positive c,p. The manuscript expressly leaves a full asymptotic and the missing slowly varying factor undetermined; the liminf is not a limit theorem. [Theorem 1.1, primary manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos859-divisor-sums.pdf).

- **Erdős 944.** For every integer r≥1 there is a finite graph G with chi(G)=4, chi(G−v)=3 for every vertex v, and chi(G−E')=4 for EVERY set E' of at most r distinct undirected edges. A critical edge set means any set whose deletion lowers chromatic number, not necessarily an inclusion-minimal set. With Skottova–Steiner's prior theorem for k≥5 this settles existence for every k≥4,r≥1. The manuscript expressly does not establish existence at every sufficiently large order, so the quantitative f_4(n)→infinity question is not automatically settled. [Theorem 1.1 and scope paragraph, primary manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-944.pdf).

- **Erdős 1062, both mathematical components.** A positive-integer set is fork-free when no member divides two distinct other members. Let f(n) be the maximum size in [n]. Put E=(union_{j≥0}[2·4^j,4^(j+1))) intersect (union_{b≥0}[2·3^b,3^(b+1))), and B=(union_{b≥0}[10·3^b,12·3^b)) intersect (union_{j≥0}[4^j,(5/4)4^j)). For x≥1 set R(x)=1+floor(log_4 x)+floor(log_3 x)+1_E(x). Their exact theorem is f(n)=sum_{m≤n,(m,6)=1}[R(n/m)−1_B(n/m)]. An extremal set can lie in (n/8,n]. They prove its density c≈0.67296565119948934747 is irrational. Thus part (i) is mathematically answered in the manuscript even though the formal target is part (ii). [Theorems 1.1–1.3, primary manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf).

- **Erdős 1057, with Will Howe and Grant Huffman.** The repository claims C(x)=x^(1−o(1)) for the Carmichael counting function. It distinguishes its corrected 23/24 zero-free input from an erroneous 7/8 description in the earlier manuscript and reports proof replay, while prize review was pending in the inspected README. The current mathematical account claims nonvanishing for actual nonprincipal Dirichlet L-functions in Re(s)>23/24 and a very strong smooth shifted-prime supply. This investigation did not independently audit those deep inputs and does not use them as an unquestioned new black box. [Repository](https://github.com/JENW1N/erdos1057-lean), [mathematical account](https://github.com/JENW1N/erdos1057-lean/blob/main/MATHEMATICAL-ACCOUNT.md).

### Inferences

- A numbered problem may still show open because other parts remain open; conversely, proving a part whose formal target is absent does not establish novelty if the manuscript already states it.
- Older snapshots are especially dangerous here: reading only arXiv version 1 would rediscover an extension already present in the current version.

### Gaps

- This is a verified substantial portfolio, not a certified exhaustive list of everything under the JenW1N handle.
- Direct erdosproblems.com requests returned HTTP 403 in this session. Source manuscripts and Conjectures.io records support the statements above; no claim is made that the canonical tracker independently endorsed every result.

## Which proof components are reusable?

### Takeaway

The most sharply formulated reusable inputs are the bounded-degree subgraph construction behind 108, the local factorial representation theorem, strict radial support in the unit-distance construction, and the exact fork-free formula. Directly applying them often reproduces an already stated consequence.

### Cited Findings

- **108 base-graph lemma.** For integers q,Delta≥1 there is a graph G which is floor(4608q² ln(4q))-degenerate, has fractional chromatic number >q, and whose every subgraph of maximum degree ≤Delta is 2-degenerate. For an acyclic orientation D with maximum outdegree d, the heavy vertices of a K_{s,t}-free subgraph H of the arc graph—those with H-outdegree ≥t—form base edges Q with maximum degree ≤d+(s−1)binom(d,t). If Q is binom(r,t)-colorable, H is r-colorable. The coloring assigns t-subsets of [r] to base vertices and colors arcs in reverse topological order. [Theorem 2.1, Lemmas 3.2–3.3](https://arxiv.org/html/2609.40192).

- **96/97 finite input.** With v_d=binom(2d,d), m_d=d·v_d/2, N=v_d q^m_d, their construction gives N points and at least (d/2)(1−1/q)N unit pairs, with the strict support inequality inner(x,y−x)<0 for every distinct x,y. Middle-level Boolean incidences, powers-of-five labels, small rotations, and independent radial perturbations yield exact edges. Pairwise distinct bounded rotation products follow from a nonzero mixed derivative of the triangle angle with respect to its two radii. This support condition allows disjoint slightly rotated copies without losing convexity. [Pinned LaTeX source](https://github.com/lkruer/erdos-96-97-proof/blob/0e98f5f9bdaf36007e3eb405cbefe2eda778a9b2/96-97.tex).

- **18(b) modular input.** Binary blocks of genuine factorial divisors provide nonconcentrated residue distributions. Multiplicative Fourier mixing modulo powers of two supplies short representatives with bounded polynomial height, and positive quotient recursion converts these to exact integer sums. A factorial reserve turns multiplicities into distinct summands. The ordinary proof cites Bourgain's general-modulus exponential-sum theorem, while the Lean route proves its required dyadic estimate internally. [Primary manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos18b-factorial-divisors.pdf), [primary Lean source](https://github.com/JENW1N/complete-math-solutions/blob/main/proofs/Erdos18b.lean).

- **272 structural input.** After removing at most 2048N members from a family of size ≥N²/2 and optionally reflecting, either every surviving member contains a point c, or every c-avoiding survivor is an interval containing a common core [L,R], with c<L and 256(L+N−R)(floor(log_2 N)+1)≤N. Private pairs for crooked members and progression matching prove the final linear error. The loss matters: this is not a zero-loss kernel theorem. [Theorem 1.2](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-272.pdf).

- **944 construction input.** The four-color construction combines punctured three-colorings of cyclic graphs, an integral height character, a winding inequality, and a Chinese remainder construction classifying small-deficit characters. Robustness is encoded as every three-color assignment having more than r monochromatic edges. Vertex deletion admits an explicit punctured coloring. [Sections 2–7](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-944.pdf).

- **859 probabilistic input.** The lower bound uses a tilted finite independent-prime model, proper divisor cubes, enlargement of logarithmic support by prime pairs, and a practical divisor reserve. Harmonic averaging before a single change of measure preserves the critical exponent. The upper bound transfers a fixed-ratio divisor-interval saving by dyadic decomposition. [Sections 1.1, 3–5](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos859-divisor-sums.pdf).

### Inferences

- **A quantitative consequence of 1062 worth checking:** the exact formula appears to imply f(n)=cn+O(log n). Write g=R−1_B as a step function. Its discontinuities lie in finitely many geometric sequences; hence up to n there are O(log n) jumps of bounded magnitude, and the reciprocal sum of jumps beyond n is O(1/n). Summation against #{m≤y:(m,6)=1}=y/3+O(1) gives the stated error. Section 5 of the source derives convergence by dominated convergence and does not state this rate. This is an elementary derived corollary, not a claim to a newly solved numbered problem or literature novelty.

### Gaps

- No transfer theorem supplied here resolves the fixed-polylogarithmic 18(c), all-orders 944, exact 272, or full 859 asymptotic.
- The dependence of constants on eta in 18(b) cannot be suppressed or optimized by letting eta vary with n without a new uniform estimate.

## Which nearby gaps remain promising, and which are already closed?

### Takeaway

The best close targets are the exact/kernel conjectures for 272 and the all-orders quantitative form of 944. The obvious 108 extensions and the first part of 1062 are already covered in the literature or authors' own manuscripts.

### Cited Findings

| Existing result | Nearby target | Established obstruction or status |
| --- | --- | --- |
| 108, bounded-degree suppression | K_{s,t}-free subgraphs and chi-avoidability | Already Theorems 1.6–1.7 in the current [Nguyen–Walczak paper](https://arxiv.org/html/2609.40192). |
| 18(b), local short sums | 18(c), h(n!)=(log n)^O(1) | Explicitly not implied by the [source bounds](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos18b-factorial-divisors.pdf). |
| 272, O(N) error | Exact t(N), and common-point kernel | Yang conjectures t(N)=binom(N,2)+1+floor((N−1)/4), proves it for all common-point families and computationally N≤12. [Theorem 1.4 and Conjecture 1.3](https://arxiv.org/html/2607.23004). |
| 944, arbitrary robustness at some order | f_4(n)→infinity for all sufficiently large n | Expressly outside [Kohlmeyer–Kruer's scope](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos-944.pdf). |
| 1062(ii), irrational density | 1062(i), determine f(n) | Already answered exactly by their [Theorem 1.1](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf). |
| 354(i), doubling sequences | Existential or universal base in (1,2) | Both yes/no readings already answered; classification remains beyond the [proof note](https://github.com/JENW1N/complete-math-solutions/blob/main/proofs/erdos354/PROOF.md). |
| 859, critical liminf plus vanishing | Full target-by-target asymptotic | Explicitly left open by [Theorem 1.1's scope paragraph](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos859-divisor-sums.pdf). |

### Inferences

- The rooted-pair theorem in Yang and the 272 long-core alternative are complementary, but the 2048N discard cannot be ignored when seeking an exact maximum.
- Padding or taking disjoint unions will generally destroy vertex-criticality in 944. Any all-orders interpolation must preserve both vertex-criticality and edge robustness.
- A quantitative error theorem for 1062 is a defensible modest output if no genuinely new open-target closure survives scrutiny.

### Gaps

- No breakthrough is established by these source notes. They supply exact interfaces and prevent known results from being misreported as new.
- Full primary PDFs for 859, 1062, 944, 272, and 18(b) were retrieved and extracted into the companion *.pdf.txt files in this notes directory. Those are searchable source extracts, not independently verified proofs.
