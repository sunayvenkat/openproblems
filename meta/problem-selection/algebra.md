# Algebra and original research candidates

## Which live unsolved candidate has the most concrete attack?

### Takeaway
My first choice within this assigned scope is Marcus's block-permanent inequality. It has a small unresolved case admitting exact finite counterexamples, although its long history is a substantial warning against expecting an easy proof. All polynomial-minimal-graph targets and the small lonely-runner and graceful-tree originals are already closed and must not be selected.

### Cited Findings
- **Rank 1: Marcus Block Permanent.** For every complex Hermitian positive semidefinite matrix A of size mk, partitioned into k by k blocks A_ij, define G_ij = per(A_ij). The conjecture is per(A) >= per(G). Additionally, for k >= 2 and positive definite diagonal blocks, equality should hold iff every off-diagonal block vanishes. The live page says no attempts and offers both proof and counterexample modes. [Live problem](https://conjectures.io/problems/fulloldproblemscatalog-marcusblockpermanent-conjecture).
- Lieb proved two blocks for every block size. Yair Lavi's current research page states that three 2 by 2 blocks at rank <= 2 satisfy the stronger inequality per(A)-per(G) >= (14/9) product_i per(A_ii); it also reports a reduction of any first m-block counterexample to rank <= (m-1)k. Consequently a three-block, block-size-two counterexample, if one exists, can be sought at rank 3 or 4. The page also reports validity near positive definite diagonal matrices and for rank-one-plus-nonnegative-diagonal matrices. These are claims on the investigator's own project page; I did not independently verify their proofs. [Researcher's current results](https://yair-lavi.com/mincs-list/conjecture-9/index.html).
- The general inequality is a special case of Lieb's permanental-dominance conjecture. A failure of permanent-on-top does not automatically refute it. Wanless records the implication relationships and the two-block theorem. [Wanless primary survey](https://arxiv.org/html/2202.01867v1).

### Inferences
- Best concrete route: parameterize six vectors in complex dimension 3 or 4, form their Gram matrix, pair them into three blocks, and minimize the exact polynomial difference. Use normalization by row/column scaling. Search structured phases and low-rank boundaries; do not waste effort in rank <=2, rank-one-plus-diagonal, or close to a positive definite diagonal matrix.
- A strict numerical negative can be converted into rational complex coordinates and verified by integer arithmetic. A negative in any dimension resolves the full universal problem. Positive computation in the 6 by 6 case resolves nothing by itself.
- A second route is the equality clause: look for nontrivial orthogonal decompositions of tensor products that annihilate the difference while each paired Gram block remains positive definite. This is a genuine part of the mathematical conjecture, but it should not be confused with exploiting k=1, which the live formulation explicitly excludes.

### Gaps
- No counterexample, or complete proof, was found in this selection survey.
- I have not inspected the complete audited Lean support definition; the displayed ordinary statement and source survey agree.

## What are the remaining ranked alternatives and their barriers?

### Takeaway
The other live algebra candidates are substantially less attractive. Their finite descriptions are useful, but either existing searches have already attacked them or their first unknown sizes are expensive.

### Cited Findings
- **Rank 2: Complex 4 by 4 exact bilinear multiplication with at most 47 products.** Construct complex linear forms l_r(A), m_r(B), and fixed output matrices C_r for r <=47 such that AB=sum_r l_r(A)m_r(B)C_r for every A,B in M_4(C). The live source16 page is open with no attempts. The repository activation description explicitly says exact bilinear algorithms and cites Epoch's matrix-multiplication open problem. [Live problem](https://conjectures.io/problems/math30catalog-source16); [audited activation descriptions](https://github.com/conjectures-io/conjectures-tasks/blob/main/staged/research-targets/ACTIVATION.md); [Epoch source](https://epoch.ai/frontiermath/open-problems/matrix-multiplication).
- **Rank 3: Marcus-de-Oliveira.** For complex normal n by n matrices A,B with eigenvalue multisets a_i,b_i, det(A+B) should belong to conv_R{product_i(a_i+b_sigma(i)): sigma in S_n}. The live page is open and has no attempts. [Live problem](https://conjectures.io/problems/fulloldproblemscatalog-marcusdeoliveira-conjecture).
- **Rank 4: Wang Hadamard permanent nonvanishing.** Every real sign Hadamard matrix H of order n>2 should have per(H) !=0. The live page is open with no attempts. [Live problem](https://conjectures.io/problems/fulloldproblemscatalog-wanghadamardpermanentnonvanishing-conjecture).
- Wang is known for Sylvester-Hadamard matrices by Chabaud's 2018 proof of the exact dyadic valuation. Lavi now reports the stronger exact valuation v_2(per H)=v_2(n!) for all Hadamard matrices of every order below128. This is the investigator's own report, not independently verified here. [Chabaud primary paper](https://arxiv.org/abs/1802.08001); [current investigator page](https://yair-lavi.com/mincs-list/problem-5/index.html).
- **Rank 5: Complex 3 by 3 matrix multiplication border rank >=18.** This is open on source18; it is a lower-bound problem, so a proposed rank17 degeneration would disprove it but proving the inequality requires algebraic-geometric exclusion of all such degenerations. [Live problem](https://conjectures.io/problems/math30catalog-source18); [cited primary source](https://arxiv.org/abs/1911.07981).

### Inferences
- For rank47 multiplication, a useful route would be symmetry-restricted tensor decomposition followed by exact algebraic reconstruction. This is a large polynomial feasibility problem, unlikely to be the easiest overall catalog choice.
- For Marcus-de-Oliveira, parameterize B=U diag(b) U* and separate det(A+B) from the polygon of permutation products. Prior workspace searches already addressed this route, according to the parent; it should not be selected without an appreciably new idea.
- For Wang, the natural route is a uniform 2-adic proof, potentially via row-product codes and Walsh transforms. Direct search needs very large Hadamard orders if the current reported results are correct.

### Gaps
- The ranked alternatives have not received a comprehensive literature search in this short survey.
- No claim of mathematical ease or likely success is justified for any of them.

## Which tempting entries must be excluded on status grounds?

### Takeaway
The live problem page is more reliable than the repository's stale activation matrix or even the public changes log. A target can already be solved while remaining listed in those inputs.

### Cited Findings
- The changes log reports quartic polynomial minimal graphs, both five-leaf graceful-tree targets, and two-entry tight lonely-runner classification solved on October 8; four-speed amended spectrum, six-speed denominator bound, dimension-eight polynomial graphs, and conductor<=4m Wilf solved on October12. [Pool changes](https://conjectures.io/problems/changes).
- The dimension-dependent polynomial minimal-graph degree bound source30 is also solved, with documentation pending. Its live page says a proof was verified and reviewed; it is ineligible for further reward submissions. This closure was absent from the changes log when checked. [Live source30](https://conjectures.io/problems/math30catalog-source30).
- Fourth planar Dirichlet Polya inequality is listed solved October26. [Pool changes](https://conjectures.io/problems/changes).
- The uniform subquadratic sensitivity-versus-exact-real-degree target remains open, but is an asymptotic bound rather than an immediate finite counterexample opportunity. [Live source20](https://conjectures.io/problems/math30catalog-source20).

### Inferences
- Do not commit to any original research target from ACTIVATION.md without a fresh live-page check.

### Gaps
- No comprehensive status screen of every geometry Erdős entry was completed; that is outside this compact algebra-first shortlist.
