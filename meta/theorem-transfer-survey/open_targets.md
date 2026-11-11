# Open targets and theorem transfer

## Which graph transfers remain new or unresolved?

### Takeaway

The natural transfers from the Kohlmeyer–Kruer solution of Erdős 108 have already been developed substantially in Nguyen–Walczak's September 2026 paper. A clean countable disjoint-union corollary settles the infinite **girth** variant, but it does not settle the main odd-cycle formulation of Erdős 740 and should not be represented as a novel breakthrough.

### Cited Findings

- The published Conjectures.io proof of 108 supplies, for every integer M, a finite graph G_M with chromatic number at least M such that every C4-free subgraph is 6-colourable. The source explicitly defines the arc graph on increasing directed edges and proves `arc_counterexample_family`. [Primary proof](https://conjectures.io/results/8c083793-9c3c-4960-8a23-869e54fcb584/solution)
- Nguyen–Walczak, Theorem 1.4, improves 6 to 3 while retaining triangle-freeness and arbitrarily large chromatic number. Their Theorem 1.5 classifies their finite threshold ell(g,k): it is finite exactly when g=4 or k is 1 or 2. This is an already published result, not a fresh deduction in this investigation. [Primary paper](https://arxiv.org/html/2609.40192)
- The same current paper already contains Theorem 1.6: for all s>=t>=2 and k>=1, there is a triangle-free graph of chromatic number greater than k whose K_(s,t)-free subgraphs are all (t+1)-colourable. Theorem 1.7, attributed to Raphael Steiner, says a graph is chi-avoidable precisely when it is non-bipartite. Therefore the tempting generalisation from C4 to all complete bipartite obstructions is not available as an original result. [Primary paper, introduction](https://arxiv.org/html/2609.40192)
- Their key Theorem 2.1 states that for every q,Delta>=1 there is a floor(4608 q^2 log(4q))-degenerate graph of fractional chromatic number greater than q, all of whose subgraphs of maximum degree at most Delta are 2-degenerate. The paper explicitly notes the consequence of arbitrarily large fractional chromatic number with no cubic subgraph. [Primary paper, Theorem 2.1](https://arxiv.org/html/2609.40192)
- Erdős 740's main formulation asks: given an infinite cardinal m, a graph with chromatic number m, and r>=1, must it contain a subgraph with chromatic number m and no **odd** cycle of length <=r? Its remarks separately ask the analogous question with **all** cycles forbidden, citing Erdős 1981. [Problem statement](https://www.erdosproblems.com/740)
- Nguyen–Walczak cites Steiner's affirmative finite result for the odd-girth analogue of 108. Thus an attempt to transfer the C4 obstruction to short odd cycles contradicts known finite theory. [Primary paper, introduction](https://arxiv.org/html/2609.40192)
- The 740 forum records the distinction between its countable case and Shelah's consistency result at aleph_1, cross-referencing 1175. This is a forum observation about the referenced result, not a new proof supplied here. [Discussion](https://www.erdosproblems.com/forum/thread/740)

### Inferences

**Complete elementary consequence of 108.** Let G be the disjoint union of the finite G_M. It has a countable vertex set and cannot be coloured with any fixed finite number of colours, so chi(G)=aleph_0. If H is a C4-free subgraph of G, each restriction H[V(G_M)] has a 6-colouring. Reusing the same six colours on all components colours H, hence chi(H)<=6. In particular no subgraph of girth at least 5 has infinite chromatic number. The sharper published theorem yields 3 in place of 6. This refutes the all-cycles variant in the remarks of 740 at aleph_0. It leaves the odd-cycle statement untouched, because a graph without short odd cycles can still contain C4.

The above countable consequence is routine once the finite uniform bound is known. No comprehensive priority claim is made. The current Nguyen–Walczak paper does not visibly discuss this infinite disjoint-union formulation, but that absence does not make its novelty established.

### Gaps

- No genuinely open graph target was fully resolved in this bounded search.
- A uniform finite chromatic bound cannot automatically be promoted to a statement for arbitrary uncountable cardinals: the disjoint union constructed above has chromatic number only aleph_0.
- The Conjectures.io explanatory PDF link for 108 returned 404; the actual published proof source remained accessible. The authors' GitHub manuscript and Nguyen–Walczak are preferable for exposition.

## Which arithmetic targets are actually adjacent to the solved results?

### Takeaway

Erdős 197 is a precise unresolved strengthening adjacent to the 4AP-free permutation construction for 196. The factorial-divisor result 18(b) has direct connections to 18(a), 18(c), and 304, but its subpower scale is insufficient for their polylogarithmic targets.

### Cited Findings

- Erdős 197 asks whether the natural numbers can be partitioned into two sets, each admitting a permutation without any increasing or decreasing three-term arithmetic progression. Three sets suffice. [Problem statement](https://www.erdosproblems.com/197)
- Kohlmeyer–Kruer's portfolio explicitly distinguishes the factorial-divisor target 18(b), the linear-error variant of 272, and multiplier-two part 354(i) from broader questions. It credits the mathematics behind its 790 formalization to Samuel Korsky. [Authors' portfolio](https://raw.githubusercontent.com/JENW1N/complete-math-solutions/main/README.md)
- Erdős 18 defines h(m) for a practical number m as the largest minimum number of distinct divisors needed to represent an integer between 1 and m-1. Its questions include infinitely many practical m with h(m) bounded by a fixed power of log log m; h(n!)<n^{o(1)}; and the stronger h(n!)<(log n)^{O(1)}. [Problem statement](https://www.erdosproblems.com/18)
- Erdős 304 asks if the worst-case minimum length N(b) of a distinct-denominator Egyptian fraction expansion of a/b, 1<=a<b, satisfies N(b)=O(log log b). Vose's quoted upper bound is O(sqrt(log b)). [Problem statement](https://www.erdosproblems.com/304)
- Erdős 1192 asks for an asymptotic basis A of each order r>=2 with sum_{n<=x} f_r(n)^2=O(x). Its r=2 case is already affirmative by Ruzsa; the unresolved part is higher order. [Problem statement](https://www.erdosproblems.com/1192)
- Erdős 825, another practical-number-adjacent question, is already recorded as solved by Larsen. It is not a fresh open target. [Problem statement](https://www.erdosproblems.com/825)

### Inferences

For every practical m, N(m)<=h(m): divide a distinct-divisor representation of a<m by m and rewrite each d/m as 1/(m/d). Every divisor used satisfies d<m, so every denominator exceeds 1, and distinct divisors give distinct denominators. Thus 18(b) gives a strong bound along factorial denominators, N(n!)<=n^{o(1)}. Since log(n!) is asymptotic to n log n, this is only (log(n!))^{o(1)}. It does not imply N(n!)=O(log log(n!)), nor the bound for arbitrary b required in 304.

For 197, a 4AP-free permutation would solve the problem if its monotone 3AP hypergraph were 2-colourable: restrict the permutation to each colour class. The universal finite version of this proposed lemma is false, by the following exact argument.

**Ternary-reversal obstruction theorem.** For every positive integer c, there is a finite permutation with no monotone four-term arithmetic progression which cannot be partitioned into c subsequences each avoiding monotone three-term arithmetic progressions.

**Proof.** Take m to be a Hales–Jewett dimension for an alphabet of size three and c colours. Identify the integers from 0 to 3^m-1 with their m ternary digits (x_0,...,x_(m-1)), and order them lexicographically starting at the least significant digit x_0. This is the ternary digit-reversal permutation.

Suppose a,a+d,a+2d,a+3d lie in this interval, with d>0. Write j=v_3(d). Their digits below j coincide. Their digits at position j are, modulo 3, x, x+r, x+2r, x, with r nonzero modulo 3. In the lexicographic order, the class of words with specified digits through j is a convex interval. The first and fourth integers belong to one such class, whereas the two intermediate integers do not. Hence they cannot occur in increasing or decreasing order in the permutation. This proves that it avoids monotone 4APs.

Now c-colour its entries. The Hales–Jewett theorem provides a monochromatic combinatorial line: a nonempty set I of coordinate positions varies simultaneously over t=0,1,2 while all other digits remain fixed. The represented integers are a, a+D, a+2D, where D=sum_(i in I)3^i>0. Their first differing digit, at min(I), is 0,1,2 respectively, so they appear in this increasing order in the ternary-reversal permutation. They form a monochromatic monotone 3AP. Thus no c-colouring splits this permutation into c 3AP-free subsequences. QED.

This is a mathematical obstruction derived here from the standard Hales–Jewett theorem, not a claimed new theorem of independent novelty. It blocks the generic finite coloring implication much more strongly than just at two colours. It does not rule out exploiting additional structure of the specific infinite permutation used in the solution of 196; the finite permutation above has not been shown to be a prefix of that construction.

A useful necessary ordering constraint for 197 is the following. If a is the first element of one colour class and a+d,a+2d are in that class, then a+2d must occur before a+d. Consequently a monochromatic infinite doubling ray {a+2^j d:j>=0}, together with its initial point a, cannot occur within a 3AP-free permutation whose first point is a. Any inductive two-colour construction must actively avoid these infinite descending chains. This identifies a concrete obstruction rather than a solution.

### Gaps

- No way was found to convert the n^{o(1)} bound from 18(b) into a fixed power of log n. Selecting a subsequence alone does not justify that conversion.
- No two-colouring theorem for the monotone-3AP hypergraph of the specific 196 permutation has been proved. The preceding argument shows that a proof cannot rely only on 4AP-freeness of finite prefixes.
- A complete audit of every portfolio manuscript was assigned separately; these notes do not treat the portfolio's presence as independent mathematical verification.

## Can the solution of 14 force the still-open additive basis results?

### Takeaway

The explicit square-root lower bound in the solution of 14 controls the number of sums that fail uniqueness. It does not force their representation multiplicities to grow, and hence cannot alone settle the Erdős–Turán basis conjecture.

### Cited Findings

- The actual 14 proof defines uniqueness up to exchanging the two summands, including diagonal representations. Its `uniform_sqrt_bound` proves sqrt(N)<12000 E_A(N) for all sets A of naturals and N>=2*1000000^4, where E_A(N) counts positive integers up to N that have either zero or at least two unordered representations. [Primary proof source](https://conjectures.io/results/dce3d778-6f52-4c27-8da0-c82d2f391b64/solution)
- The authors' source edition lists both 14(i) and 14(ii) as completed proof targets and distinguishes build wrappers from the preserved submission bodies. [Authors' portfolio](https://raw.githubusercontent.com/JENW1N/complete-math-solutions/main/README.md)
- Conjectures.io's catalog still lists the additive-basis question 28 (unbounded limsup of the representation function for an asymptotic basis) and the higher-order energy question 1192 as open targets. [Catalog](https://conjectures.io/problems)

### Inferences

If A is an asymptotic basis of order 2, its nonrepresented integers contribute only O(1), so the bound for 14 implies at least sqrt(N)/12000-O(1) integers with multiple unordered representations. All of those integers could still have precisely two representations. Accordingly the theorem is compatible with the hypothetical bounded-representation basis whose impossibility is requested in 28. A transfer needs a separate multiplicity amplification lemma, not merely a recounting of the exceptional set.

The same point blocks a naive attack on 1192: sqrt(N) exceptional sums of bounded multiplicity contribute only O(sqrt(N)) to the second moment, far below the O(N) allowance in that problem.

### Gaps

- No multiplicity amplification lemma was found or proved.
- The source screen is bounded, and direct erdosproblems.com page fetches frequently returned 403. Its mathematical statements were retrieved from indexed page and forum text; stale status labels should not override newer primary proofs.
- No new full proof or counterexample to an unsolved catalog statement was obtained by this subtask. The rigorous delivered consequence is the countable girth counterexample above, with its scope and lack of novelty certification explicit.
