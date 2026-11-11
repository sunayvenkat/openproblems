# Combinatorics candidate selection

## Which candidates offer concrete routes?

### Takeaway
No candidate in this survey is clearly more tractable than the algebra researcher's Marcus block permanent candidate. Among combinatorial alternatives, the narrow logarithmic gap in Erdős 156 is the best constructive target; Erdős 13 general is the best recent-theorem extension. This ranking is judgment, not evidence of ease or a commitment to a problem.

### Cited Findings
- **Erdős 156.** For every sufficiently large integer N, is there a maximal Sidon subset A of {1,...,N} with |A| = O(N^(1/3))? Sidon means unordered pair sums, including doubles, are unique; maximal means no other member of the interval can be adjoined while preserving this. Current source marks the full result research open. Ruzsa's known upper bound is O((N log N)^(1/3)); a counting argument gives the lower scale N^(1/3). [Live catalog entry](https://conjectures.io/problems/erdos156-erdos-156); [formal source with reference and known bounds](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/156.lean); [Ruzsa original publication DOI](https://doi.org/10.1023/A:1009757824153).
- **Erdős 13 general.** For each fixed nonnegative integer r, does there exist C_r such that every A subset {1,...,N} containing no a,b_1,...,b_r in A with each b_i>a and a dividing their sum satisfies |A|<=N/(r+1)+C_r? Repetition among b_i is allowed. Current source marks this open. The case r=2 was proved by Bedert in 2023. [Catalog](https://conjectures.io/problems/erdos13-erdos-13-variants-general); [full source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/13.lean); [Bedert preprint](https://arxiv.org/abs/2301.07065).
- **Erdős 835.** Does there exist k>2 such that the k-subsets of a 2k-element ground set can be colored with k+1 colors, with every (k+1)-subset containing all k+1 colors among its k-subsets? Equivalent to chi(J(2k,k))=k+1. The current source marks the existence question open, records exclusions for k=3,...,9 and all k for which k+1 is composite, and credits the last result to Ma and Tang. [Catalog](https://conjectures.io/problems/erdos835-erdos-835); [full source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/835.lean); [Ma--Tang paper](https://github.com/QuanyuTang/erdos-problem-835/blob/main/On_Problem_835.pdf).
- **Erdős 617.** For every r>=3, any coloring of the edges of K_(r^2+1) in r colors has an (r+1)-vertex induced complete subgraph missing some color. The full statement remains open in the catalog. Erdős and Gyárfás proved r=3,4; Xia and Szeider's October 2026 preprint proves r=5 via a reduction to sparse color classes, stability, and certified exhaustive computation. [Catalog](https://conjectures.io/problems/erdos617-erdos-617); [source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/617.lean); [Xia--Szeider primary preprint](https://arxiv.org/abs/2610.24484).

### Inferences
- **Rank 1: 156.** Search for algebraic lifts of Singer difference sets whose triple differences cover an interval deterministically. The existing random-lift construction pays a logarithm for covering all targets; a structured covering map or finite-geometric saturating construction could remove that factor. This is a proposed direction, not a proven reduction sufficient for the result. Translation from finite groups to the integer interval must preserve both Sidon uniqueness and full maximality.
- **Rank 2: 13 general.** Study Bedert's r=2 proof for a residue-chain injection or weighted compression that scales to r. An alternative disproof could use periodic/residue-restricted blocks with density above 1/(r+1), but an infinite family is required because an arbitrary additive constant C_r is allowed.
- **Rank 3: 835.** A single successful finite coloring solves the existence problem. First case not excluded by the cited results is k=10, giving 184756 vertices of J(20,10), so naive coloring is huge. Each color class must be a Steiner-system-like independent set attaining the Johnson bound. A finite-geometric construction, large set of designs, or a stronger divisibility obstruction is more promising than unstructured search. This is harder than a six-by-six polynomial counterexample search.
- **Rank 4: 617.** A single balanced coloring for r>=6 refutes the full conjecture. Affine-plane direction colorings naturally provide examples at r^2 vertices; the obstruction is adding one vertex. A structured extension or algebraic switching of such designs could be searched. For a proof, a uniform stability theorem for the sparsest color class would need to replace case enumeration. The first unresolved case is r=6, following the October 2026 r=5 paper.

### Gaps
- The six-minute survey did not exhaust all 64 combinatorics entries or every discrete-geometric entry. The site only server-renders the first 24 entries, and search-index snapshots included stale withdrawn Green targets, so entries were cross-checked against the current task-targets and source files.
- Direct requests to erdosproblems.com returned HTTP 403; primary source files and authors' papers were used where possible.
- No valid novel proof, disproof, or compellingly small candidate construction was found in this selection phase.

## Which apparent candidates should be treated cautiously?

### Takeaway
Short statements can hide major longstanding problems. Catalog inclusion and formalization status alone do not establish current mathematical openness.

### Cited Findings
- Erdős 44 asks whether every finite initial Sidon set can be extended to a Sidon set of size at least (1-epsilon)*sqrt(M) in {1,...,M}. The current source marks this open. [Source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/44.lean).
- A paper titled *Size-4 Counterexamples to the Sidon-Extension Conjecture*, arXiv:2604.25214, was submitted April 28, 2026, but its current page explicitly says withdrawn, with revision dated May 14, 2026. It must not be treated as a resolution without examining the withdrawal and original argument. [Primary arXiv record](https://arxiv.org/abs/2604.25214).
- Many old search results still show Green targets that were withdrawn on September 30, 2026. [Example withdrawn entry](https://conjectures.io/problems/green9-green-9-iii?mode=counterexample).
- The current task audit identifies its screening as comparative feasibility, expressly not a claim of ease or guaranteed solvability. [Audit](https://github.com/conjectures-io/conjectures-tasks/blob/main/tiers/tier-1/selection-audit.json).

### Inferences
- Do not choose a withdrawn target or a solved special case solely because it appears in an old catalog search snippet.
- Marcus block permanent remains preferable to the surveyed combinatorial targets if its exact full statement really admits a finite PSD matrix counterexample route at order six.

### Gaps
- The withdrawal reason for arXiv:2604.25214 was not investigated further because Erdős 44 was already a weaker candidate than the parent team's matrix target.
