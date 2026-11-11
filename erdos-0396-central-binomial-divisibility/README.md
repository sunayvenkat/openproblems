# Erdős Problem #396 — working repository

> **Mirror.** This folder is a snapshot of [sunayvenkat/erdos396](https://github.com/sunayvenkat/erdos396) (Nov 2026) plus two later scripts (`code/h2/toppiece_m1r_*.py`). Not mirrored: the 33 MB `code/h2/rscan_m1.npz` (in the original repo) and the >80 MB `rscan_111546435_e*.txt` scan dumps.


**Problem (Erdős–Graham 1980).** Is it true that for every k ≥ 0 there is an n with

  n(n−1)(n−2)⋯(n−k) | C(2n, n) ?

Write **E_k** for the set of such n. By computer E_k is non-empty for k ≤ 16 (OEIS [A375077](https://oeis.org/A375077)). Before this work it was open whether even E₁ is infinite.

## Headline status (November 2026)

| Result | Statement | Status | Where |
|---|---|---|---|
| **Theorem C** | E₁ is infinite; positive proportion of n = (12x−1)(22x+9) in a residue class lie in E₁, so #(E₁ ∩ [1,N]) ≫ N^{1/2} | **Unconditional**; proof written, awaiting independent line-by-line check | [DRAFT.md §12](DRAFT.md) |
| **Theorem D** | E₂ is infinite; positive proportion of n = (14x−1)(15x−1) | **Unconditional**; same caveat | [DRAFT.md §12](DRAFT.md) |
| Theorem A | E₁ infinite | Conditional on Dickson for one 4-tuple | [DRAFT.md §11](DRAFT.md) |
| Theorem B | E₂ infinite | Conditional on Dickson for one 6-tuple | [DRAFT.md §11](DRAFT.md) |
| Theorem 1 | E₁ infinite | Conditional on Schinzel's Hypothesis H (superseded by C) | [DRAFT.md §8](DRAFT.md) |
| Theorem 2 | E_k infinite for all k | Conditional on H **and** Conjecture G | [DRAFT.md §9](DRAFT.md) |
| E_k, k ≥ 3 | infinitely many n | **Open.** Quadratic families cannot work (Fermat: no 4 squares in AP); needs degree ≥ 3 families | [DRAFT.md §11–12.7](DRAFT.md) |

Full ledger of every lemma (proved / conditional / numerical / refuted) and the open-items list: **[STATUS.md](STATUS.md)**.

## Repository layout

```
README.md        this file: problem, headline status, navigation
STATUS.md        ledger of all results + open problems + what still needs checking
DRAFT.md         the working paper (single source of truth for statements and proofs)
REFERENCES.md    literature consulted, with what each source contributes
code/            all scripts and their saved outputs, grouped by agent/workstream
  README.md      index: which folder backs which DRAFT section, how to run
  NOTES.md       early main-thread notes (Kummer facts, cyclotomic families) — historical
```

## How to read this repo (humans and LLMs)

1. **Start with [STATUS.md](STATUS.md)** — one table tells you what is proved, what is conditional, and what is open.
2. **For any statement or proof, go to [DRAFT.md](DRAFT.md).** Section map:
   - §0 results · §1 Kummer / local reduction (Lemma 1) · §2 small primes
   - §3–§8 cyclotomic route under Hypothesis H (family F₊, carry criterion, non-top and top pieces, Aurifeuillean splitting, proof of Theorem 1)
   - §9 Conjecture G and all k (near-Lehmer route, bulk analysis of the top piece)
   - §10 reproducibility table and witnesses
   - §11 linear-form families (Theorems A, B, Lemma Q)
   - **§12 unconditional positive density (Theorems C, D; Lemmas S, W; first-moment theorem; classification; numerics; next steps)**
3. **For the computation behind a claim, go to [code/README.md](code/README.md)**, which maps each DRAFT section to its folder and script. Saved outputs (`*_out.txt`, `*.txt`) sit next to the script that produced them.
4. Agent folders contain their own `REPORT.md` / `RESULTS.txt`. Where a report and DRAFT.md disagree, **DRAFT.md is authoritative** (it records later corrections, e.g. the refutation of Lemma A and the `fastser.py` CRT caveat).

## Key ideas in one paragraph

By Kummer, ν_q(C(2n,n)) is the number of carries when adding n + n in base q. For a prime q > 2k dividing n − i, the condition at q depends only on n − i (Lemma 1). Choose n so that every n − i is a product of a few linear forms in x. A prime q dividing a form gives a carry or not according to its base-q digits: for large q (q ≳ √P) the carry is decided by the **square class of q modulo the form's leading coefficient** (Lemma S); for medium q the relevant digits are **jointly equidistributed** (Lemma W, a quadratic Weyl-sum estimate). A first-moment (union) bound over all prime factors then gives limiting failure probability M_∞ = 0.549·Σf_j + 0.0479·(#forms), which is 0.411 for Theorem C and 0.745 for Theorem D — both < 1, so a positive proportion of x succeed.

## Most useful next steps

- Independent line-by-line check of §12.3–12.4 (constants in Claims 1–2, pairing argument for |𝒯|, PNT-in-progressions uniformity, o(1) bookkeeping).
- Literature check: are Lemma S / Theorems A–D already known?
- E₃: linear-piece families are not expected to exist for k ≥ 3 (§13: Fermat, Yuzvinsky's pencil bound, cubic search via Cardano/Eisenstein parametrization in `code/h2/torus_ap.py`). The open route is §13.3: Ford–Konyagin-type density for the irreducible quadratic members of an E₂ family under Hypothesis BH_u.

## Scope note

This repository holds only the Erdős #396 work. Full-text copies of third-party papers and third-party repositories that were used during research are **not** included (copyright); they are listed in [REFERENCES.md](REFERENCES.md).
