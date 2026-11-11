# Erdős #624: full-palette maps on subsets

**Problem.** For |X| = n, let H(n) be the least h for which there is f : 2^X → X such that every h-set Y ⊆ X has {f(A) : A ⊆ Y} = X. Prove H(n) − log₂ n → ∞. Equivalently, p(h) = max{n : H(n) ≤ h} satisfies p(h)/2^h → 0. ([erdosproblems.com/624](https://www.erdosproblems.com/624))

## Status: OPEN (lower-gap conjecture unproved)

Everything is recorded in [research_state.json](research_state.json): one key per result, each with statement, proof sketch and status. Main entries:

- **Upper bound (proved):** H(n) ≤ ⌈log₂(2n(ln n + 4 ln ln n + 10))⌉ for large n, so H(n) ≤ log₂ n + log₂ log₂ n + O(1). Proof: random low-rank colouring plus Hall matching on (h−1)-faces. `unrestricted_upper_bound`.
- **Outside-valued transfer:** H_unrestricted ≤ H_outside ≤ H_unrestricted + 1.
- **Barriers (proved).** These show which restricted strategies cannot give the lower gap:
  - ordered finite-monoid maps need log₂|M| ≳ (m/2) log₂ m;
  - free-set route;
  - fractional packing;
  - mixed-rank de Caen warning;
  - binary-matroid circuit packing q = O(2^{2r/3});
  - central-cover and sparse-repair inverse barriers;
  - two disjoint efficient covers;
  - rational-derivative orbit obstruction (Hasse–Weil).
- **Reformulations:** outside tree, ordered independence system, squarefree monomial ideals, cooling codes / zero-error dispersers (`source_connections`).
- **Finite search:** exact SAT search (`code/search.py`, PySAT). Witnesses are in `witnesses/witness_<n>_<h>_<q>[_sha].json`, and each one is re-checked directly.
- **Remaining gap** (`remaining_gap`): explicit h-unavoidable antichains of bounded average cost need not contain a binary-matroid circuit family. So no reduction from arbitrary colourings to matroids is known.

## Layout

`research_state.json` is the master record. `code/search.py` is the SAT search. It needs `python-sat`; the vendored copy was not included, so install it with `pip install python-sat`. `witnesses/` holds verified SAT models. `results/` holds the common-circuit and rational-orbit examples. The nonlinear perfect-code experiment used `perfect15` from arXiv:0806.2513 (anc/perfect15). That file is not included; its SHA-256 is in `research_state.json`.
