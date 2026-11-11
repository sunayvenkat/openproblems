# Green's Problem 15: additive-square-free words

**Problem.** Is there an infinite word over a finite set of integers with no additive square? An additive square is two adjacent blocks of the same length and the same sum.

## Status: RETIRED. Solved externally.

The live check on 6 Nov 2026 showed Green 15 approved on 11 Sep 2026, submitted by JenW1N. That solution uses a six-letter substitution with increments in [1,125] ([solution](https://conjectures.io/results/66df312f-30b4-4331-b1fa-04be52f7f8ca/solution)). The work here was done under a stale "open" status and did **not** solve the problem.

What is kept:
- [notes/green15-spectral-reduction.tex](notes/green15-spectral-reduction.tex): a reviewed **sufficient spectral condition**. A primitive substitution whose incidence matrix has no unimodular eigenvalues and a 2-dimensional expanding space, and whose fixed point is abelian-square-free, admits distinct positive integer weights making the word additive-square-free.
- Finite searches that found no substitution meeting every hypothesis: rank-2, morphism (Routh-exact), parabolic, forest, marker, marker synthesis and Z3. Scripts are in `code/`, outputs in `results/`.
- `notes/green15-projection-review.txt` is the review.

The 3 MB `green15-marker-z3-2-18.smt2` is not included. `code/green15-marker-z3.mjs` regenerates it.
