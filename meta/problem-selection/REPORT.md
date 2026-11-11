# Choosing Marcus through exact matrix witnesses

**Marcus’s block-permanent conjecture is the selected problem, and the choice is fixed.** Among the candidates examined, it offers the clearest connection between exploratory computation and a complete mathematical disproof: one explicit positive semidefinite matrix violating the inequality would settle the universal assertion. Its catalog entry and a current investigator’s page both identify it as open. This is a judgment about the availability of a concrete attack, not a claim that the problem is easy or likely to fall. The selection survey produced neither a proof nor a counterexample. ([Conjectures.io](https://conjectures.io/problems/fulloldproblemscatalog-marcusblockpermanent-conjecture), [current research page](https://yair-lavi.com/mincs-list/conjecture-9/index.html))

For an $r\times r$ matrix $C$, define

\[
\operatorname{per}(C)=\sum_{\sigma\in S_r}\prod_{i=1}^{r}c_{i,\sigma(i)}.
\]

Let $m,k$ be positive integers, and let $A\in\mathbb C^{mk\times mk}$ be Hermitian positive semidefinite. Partition $A$ into an $m\times m$ array of $k\times k$ blocks $A_{ij}$, and set $G_{ij}=\operatorname{per}(A_{ij})$. The full conjecture asserts

\[
\operatorname{per}(A)\geq\operatorname{per}(G).
\]

Its equality clause says that, when $k\geq2$ and every diagonal block $A_{ii}$ is positive definite, equality holds exactly when every off-diagonal block is zero. The restriction $k\geq2$ matters: for $k=1$, $G=A$. These are the mathematical assertions being attacked; exploiting a formalization defect would not answer the chosen problem. ([Problem statement](https://conjectures.io/problems/fulloldproblemscatalog-marcusblockpermanent-conjecture))

**Six vectors give a manageable first search.** Represent $A$ as a Gram matrix, $A_{ij}=\langle v_i,v_j\rangle$. Positive semidefiniteness then holds automatically, so an optimization routine cannot create a spurious violation merely by leaving the permitted domain. Group six vectors into three pairs to obtain the first unresolved block configuration, $m=3,k=2$. Yair Lavi’s research page reports a rank reduction and a rank-at-most-two result that restrict a counterexample in this configuration to rank three or four. Those recent claims were read as research reports; their proofs were not independently checked during selection. ([Lavi](https://yair-lavi.com/mincs-list/conjecture-9/index.html))

The proposed objective is the real polynomial difference

\[
F(v_1,\ldots,v_{mk})=\operatorname{per}(A)-\operatorname{per}(G).
\]

A strict negative value is useful because continuity allows sufficiently accurate rational approximations to the real and imaginary vector coordinates while preserving negativity. The resulting rational Gram matrix permits exact evaluation, and clearing denominators gives an integer certificate. Thus numerical discovery can lead to a finite, fully checkable argument. Numerical positivity, convergence to zero, or extensive unsuccessful searching provides no universal proof. A valid proof route must establish the inequality for arbitrary block counts and sizes, and address the equality clause under its stated assumptions.

The conjecture’s history sets a demanding baseline. Lieb proved the two-block case, and the general statement is related to his broader permanental-dominance conjecture. Known counterexamples to stronger permanent conjectures do not automatically transfer to this one. Consequently, the most useful conceptual directions are to identify a tensor or Gaussian-moment identity controlling $F$, or to find phase-dependent cancellations that survive the Gram constraint. These are proposed directions, not established reductions to solved results. ([Wanless’s primary survey](https://arxiv.org/html/2202.01867v1))

The equality statement supplies a separate test: an exact non-block-diagonal Gram matrix with positive definite diagonal blocks and $F=0$ would refute that clause. Merely finding zero on a singular boundary is insufficient, because its hypotheses could fail there. Likewise, a complete proof of the six-vector case would be meaningful progress but would leave the universal problem open. The research record should preserve these distinctions so that neither a numerical artifact nor a special-case theorem is presented as a full solution.

Other surveyed finite-witness targets included Egyptian fractions with all successive denominator gaps at most two, equal least common multiples of disjoint intervals of equal length, and common large prime divisors of binomial coefficients. None supplied a more persuasive concrete mechanism in the bounded survey. ([Erdős 287](https://conjectures.io/problems/erdos287-erdos-287), [Erdős 677](https://conjectures.io/problems/erdos677-erdos-677), [Erdős 699](https://conjectures.io/problems/erdos699-erdos-699))

Status checks also removed tempting alternatives. **Erdős 156 was marked solved on November 4, 2026**, superseding the preliminary combinatorics notes. Several polynomial minimal-graph and lonely-runner targets were already closed. Catalog inclusion and stale source annotations therefore cannot establish that a problem remains unsolved. ([Pool changes](https://conjectures.io/problems/changes))

This report records the selection as of November 6, 2026. The literature screen was bounded, and no mathematical solution has yet been established. Lean formalization was intentionally deferred as requested.
