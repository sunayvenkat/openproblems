# Live catalog cross-connection screen

## Which entries were actually eligible on 6 November 2026?

### Takeaway

The live page contains 307 cards: 271 have null status, one is in review, 32 are solved, two are solved with documentation pending, and one has a formalization defect. The 272 null/in-review cards are the search pool; a repository manifest alone is not evidence that an entry remains open.

### Cited Findings

- The complete card array was extracted from the server-rendered payload of the [live catalog](https://conjectures.io/problems). The original HTML, decoded payload, parser, full JSON, and open-card text extracts are saved alongside this note as `catalog-page.html`, `catalog-decoded.txt`, `extract_catalog.cjs`, `live-catalog.json`, and `live-open-catalog.txt`. The parser checked unique keys and the solved status of `Erdos944.erdos_944`.
- All formerly open Green entries were withdrawn at Ben Green's request; six previously solved entries were retained. They do not supply new eligible Green targets. [Official task repository](https://github.com/conjectures-io/conjectures-tasks).
- The general polynomial minimal graph degree-bound entry, `Math30Catalog.source30`, says solved with documentation pending and disallows further submissions. Its absence from a changes-feed closure list must not be read as open status. [Target page](https://conjectures.io/problems/math30catalog-source30).
- The current pool contains neither Erdős #197, #304, nor #642. It also contains no Brown–Freedman or additive-square target. This is a statement about this snapshot's available entries, not about the mathematics of those problems. [Live catalog](https://conjectures.io/problems).

### Inferences

An extension of #944, a withdrawn Green problem, or a result already covered by a source manuscript cannot meet the user's requirement to resolve a different currently open catalog entry. The live catalog must be checked again before any later claim or submission.

### Gaps

Null status means no closure is recorded in this snapshot; it is not an independent literature certification of openness. The in-review entry #12(iii) may already have a valid pending solution.

## What does Green 15 actually provide?

### Takeaway

The theorem constructs a Lipschitz graph with no nontrivial three-term arithmetic progression. It does not construct a Sidon graph. Confusing these properties would create a false transfer to consecutive-sum uniqueness.

### Cited Findings

- The actual construction is an integer-valued function on the natural numbers with Lipschitz constant 125 and no indices a<b<c satisfying both a+c=2b and f(a)+f(c)=2f(b). Its increments belong to a finite set of sixteen positive integers. [Primary proof source](https://github.com/JENW1N/complete-math-solutions/blob/main/proofs/Green15.lean).
- Different eligible targets involving unique consecutive sums are [#357 finite growth](https://conjectures.io/problems/erdos357-erdos-357-parts-i), [#357 reciprocal summability](https://conjectures.io/problems/erdos357-erdos-357-variants-infinite-set-sum), and the #359 greedy consecutive-sum questions listed in the full snapshot. Their requirements are stronger than double three-term-progression avoidance. [Live catalog](https://conjectures.io/problems).
- Green 51 proves a separator inequality on the Boolean cube: for f taking values in {-1,0,1}, with adjacent vertices never having opposite nonzero signs, Var(f) <= 2 sqrt(n) Pr(f=0). [Primary proof source](https://github.com/JENW1N/complete-math-solutions/blob/main/proofs/Green51OneHalf.lean).

### Inferences

A bounded-increment integer graph cannot be Sidon. There are only finitely many possible adjacent increments, so two adjacent graph differences coincide. Those coincident vector differences give a nontrivial repeated pair sum. This elementary obstruction rules out the proposed direct Sidon interpretation regardless of the details of Green 15.

For positive a_i, distinct consecutive sums are equivalent to distinct positive differences between prefix sums s_n=sum_{i<=n} a_i. The prefix set must therefore be Sidon. Green 15 excludes only repeated averages at equally spaced indices, leaving many other repeated differences possible.

### Gaps

No transformation was found that converts the Green 15 theorem into a dense strictly convex Sidon sequence while preserving the required growth. The cube separator inequality also supplies no demonstrated improvement for the two sensitivity targets below.

## Which different open targets survived the broad screen?

### Takeaway

Several precise overlaps exist, but none in this screen is an established implication. The strongest number-theoretic follow-up is #269, now investigated separately in `269_irrationality.md`.

### Cited Findings

| Eligible target | Exact requirement relevant to this screen | Possible source and missing step |
| --- | --- | --- |
| [#269 irrationality](https://conjectures.io/problems/erdos269-erdos-269-variants-irrational) | For every finite prime set P with at least two members, the reciprocal running-LCM series of all P-smooth integers is irrational. | #1062 supplies an S-unit small-linear-form theorem, but a sparse return identity for repeated smooth-number multiplicities is missing. |
| [#357 reciprocal summability](https://conjectures.io/problems/erdos357-erdos-357-variants-infinite-set-sum) | Every strictly increasing positive sequence with all consecutive sums distinct has convergent reciprocal sum. | Green 15 is only double-3AP avoidance; it does not supply a Sidon prefix set. |
| [#749](https://conjectures.io/problems/erdos749-erdos-749) | For every epsilon>0, a set A has lower density of A+A at least 1-epsilon and uniformly bounded convolution 1_A*1_A. | #14 concerns exceptions to exactly one unordered representation; its square-root exception lower bound does not decide this target. |
| [Riddell–Erdős progression ratio](https://conjectures.io/problems/fulloldproblemscatalog-riddellerdosprogressionratio-conjecture) | For fixed k>=3, the optimal progression-free subset sizes for [1,N] and arbitrary N-element integer sets have ratio tending to one. | A 3AP-free Lipschitz graph does not supply the sharp universal ratio. |
| [#124 nonzero k](https://conjectures.io/problems/erdos124-erdos124-ne-zero) | Completeness of specified unions of mixed-base 0/1-digit sets with divisibility constraints. | #354's two doubling sequences have different generators and allow indexed repeated occurrences; no reduction establishes the mixed-base conclusion. |
| [#1108(i)](https://conjectures.io/problems/erdos1108-erdos-1108-parts-i) | Finitely many kth powers among finite sums of distinct factorials, for every k>=2. | #18's short sums of factorial divisors do not control perfect powers in sums of the factorials themselves. |

The five still-open `Math30Catalog` targets are [source16](https://conjectures.io/problems/math30catalog-source16), exact complex 4x4 matrix multiplication rank at most 47; [source18](https://conjectures.io/problems/math30catalog-source18), complex 3x3 border rank at least 18; [source20](https://conjectures.io/problems/math30catalog-source20), a uniform subquadratic sensitivity-versus-exact-degree bound; [source21](https://conjectures.io/problems/math30catalog-source21), a uniform cubic block-sensitivity bound; and [source27](https://conjectures.io/problems/math30catalog-source27), all Dirichlet Pólya inequalities for convex planar domains. [Source25](https://conjectures.io/problems/math30catalog-source25), the third Dirichlet eigenvalue inequality, is also solved with documentation pending. Their card text and current status are in the saved [live-catalog](https://conjectures.io/problems) snapshot.

### Inferences

The new geometric, minimal-graph and graceful-tree items in the authors' portfolio do not by themselves close the remaining historical or matrix-multiplication entries. Matching subject matter is not a proof interface.

### Gaps

This screen found no full new-target solution. It provides an exact pool, current closure corrections, and concrete failed implications; it does not satisfy the larger breakthrough goal and must not be reported as doing so.
