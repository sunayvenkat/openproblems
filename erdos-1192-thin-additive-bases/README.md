# Erdős #1192: thin bases with bounded mean-square representations

**Problem.** For each r ≥ 2, is there A ⊆ ℕ₀ such that rA contains all large integers and Σ_{n≤x} f_{r,A}(n)² = O(x)? Here f_{r,A}(n) counts ordered representations. Ruzsa (1990) proved the case r = 2. ([conjectures.io](https://conjectures.io/problems/erdos1192-erdos-1192))

## Status: OPEN

[notes/erdos1192-finite-reduction.tex](notes/erdos1192-finite-reduction.tex) proves two things:
- an energy triangle inequality, E_r(∪B_j)^{1/2r} ≤ Σ E_r(B_j)^{1/2r};
- an **exact finite reformulation**: such an A exists iff there are uniformly bounded-energy finite families at every dyadic scale.

This removes a proposed gluing obstruction, but it does not construct the needed finite families. `code/erdos1192-curves.mjs` is an exploratory construction search, with output in `results/`. `notes/erdos1192-review.txt` is the adversarial review.
