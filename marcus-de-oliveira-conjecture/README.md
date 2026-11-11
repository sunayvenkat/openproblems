# Marcus–de Oliveira determinant conjecture

**Problem.** For normal n×n matrices A and B with eigenvalues a_i and b_i, det(A + B) lies in the convex hull of the permutation products ∏_i (a_i + b_σ(i)). One exactly certified counterexample would refute it.

## Status: OPEN. No counterexample found.

`code/mdo-search.mjs` samples unitaries U. Half of them come from the Drury skew-conference family and half are random Givens products. It then optimises the spectra, computing the signed gap between det(diag(a) + U diag(b) U*) and the permutation-product polygon. A positive gap would be a numerical candidate. The latest batch ran 1,000 restarts. Its best normalised gap was −0.0024, so it produced no positive candidate. All runs are floating point, with no certificate either way. The method and how to rerun it are in [notes/mdo-search-notes.txt](notes/mdo-search-notes.txt):

```bash
node code/mdo-search.mjs --distinct 1000
```

The batch outputs are in `results/`.
