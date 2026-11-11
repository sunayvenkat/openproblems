# openproblems

Working research on open problems from the [Erdős Problems](https://www.erdosproblems.com) database, Ben Green's open-problems list and the [conjectures.io](https://conjectures.io/problems) catalog. Each problem has its own folder. Every folder starts with a `README.md` that gives the statement, the current status and a map of its files.

Nothing in this repository has been externally refereed. A result marked **proved** has a written proof here, but it still needs independent human checking.

## Problems

| Folder | Problem | Status (November 2026) |
|---|---|---|
| [erdos-0168-triple-free-density](erdos-0168-triple-free-density/) | Erdős #168: maximum density c of subsets of {1..N} with no triple {n,2n,3n}; (i) find c, (ii) is c irrational? | (i) **Proved here**: finite min-cover formula, explicit increment rule, c = 0.800965755006558989090420… certified to 128 digits. (ii) **Open**: six proof routes, each with one missing infinite-supply / separation lemma. |
| [erdos-0243-sylvester-rational-reciprocals](erdos-0243-sylvester-rational-reciprocals/) | Erdős #243: if a_{n+1}/a_n² → 1 and Σ1/a_n is rational, must a_n follow Sylvester's recurrence eventually? | **Open**. Conditional rigidity criterion (log-log rise bound), polynomial / quadratic / periodic-error exclusions, finite counterexample searches. |
| [erdos-0396-central-binomial-divisibility](erdos-0396-central-binomial-divisibility/) | Erdős #396: for every k, is there n with n(n−1)⋯(n−k) \| C(2n,n)? | **Partly proved here**: E₁ and E₂ infinite unconditionally (Theorems C, D; awaiting independent check). E_k for k ≥ 3 open. |
| [erdos-0624-full-palette-set-maps](erdos-0624-full-palette-set-maps/) | Erdős #624: H(n) − log₂ n → ∞? | **Open**. Proved upper bound H(n) ≤ log₂ n + log₂ log₂ n + O(1); several barrier theorems; SAT witnesses for small n. |
| [erdos-0686-consecutive-block-products](erdos-0686-consecutive-block-products/) | Erdős #686, ratio-25 variant: (m+1)⋯(m+k) = 25·(n+1)⋯(n+k) | **Open**. Block length k = 3 excluded via 60 Thue equations (Magma-dependent). |
| [erdos-0893-mersenne-divisor-doubling](erdos-0893-mersenne-divisor-doubling/) | Erdős #893: f(n) = Σ_{k≤n} τ(2^k−1); does f(2n)/f(n) → ∞? Sub-problem: the constant β_K | **Open**. Proved f(2n) ≥ 3f(n), conditional theorems, exact reduction; β_K = 0 conjecture unresolved, barrier theorems. Paper draft included. |
| [erdos-0944-critical-graphs-all-orders](erdos-0944-critical-graphs-all-orders/) | Erdős #944 all-orders form: f₄(N) → ∞ for vertex-critical 4-chromatic edge-robust graphs | **Solved, not new**. Order-completion theorem (N ≥ 45g²) proved and audited; the same bridge was published by others on 2 Oct 2026. |
| [erdos-1192-thin-additive-bases](erdos-1192-thin-additive-bases/) | Erdős #1192: order-r bases A with Σ_{n≤x} f_{r,A}(n)² = O(x), every r ≥ 2 | **Open**. Exact finite reformulation; a gluing obstruction removed. |
| [green-15-additive-square-free-words](green-15-additive-square-free-words/) | Green #15: infinite additive-square-free word over a finite set of integers | **Retired**. Solved externally (approved 11 Sep 2026). Our spectral sufficient condition and searches are kept for reference. |
| [marcus-block-permanent-conjecture](marcus-block-permanent-conjecture/) | Marcus: per(A) ≥ per(G), G = matrix of block permanents of PSD A | **Open in general**. Proved (with equality case) for (m,k) = (3,2), (4,2), (3,3), via exact SOS certificates. |
| [marcus-de-oliveira-conjecture](marcus-de-oliveira-conjecture/) | Marcus–de Oliveira: det(A+B) for normal A, B lies in the convex hull of permutation products | **Open**. Numerical counterexample search; none found. |
| [meta](meta/) | Problem selection and theorem-transfer surveys across the catalogs | Background only. |

## Conventions

- Folder names are `<source>-<number>-<short-topic>`. Erdős numbers are zero-padded to 4 digits so they sort.
- Inside a problem folder: `notes/` holds proofs, write-ups and reviews (`.tex`, `.md`, `.txt`). `code/` holds scripts. `results/` holds their saved outputs. Larger problems have their own `README.md` layout instead.
- Status words: **PROVED** means a written proof exists here; **COND** means conditional on a named hypothesis; **NUM** means numerical evidence only; **OPEN**; **FALSE** means refuted.
- Files named `*review*`, `*audit*` or `codex_review.md` are adversarial checks of the neighbouring work. Read them before relying on a claim.

## What was left out

To keep the repository small, these were omitted. Each one is third-party material or can be regenerated:

- third-party papers and their text extractions (`*.pdf.txt`, `seed-source.*`, `NoPreparata.troff`). Links to them are kept as citations.
- downloaded datasets: `perfect15` for #624, from arXiv:0806.2513 (SHA-256 is recorded in `research_state.json`).
- generated blobs over 2 MB: `rscan_*` scan dumps for #396, one 3 MB Green-15 SMT file. The script that wrote each one is included.
- vendored dependencies, caches and `__pycache__`.

The full #396 history, including the 33 MB `rscan_m1.npz`, is in [sunayvenkat/erdos396](https://github.com/sunayvenkat/erdos396).
