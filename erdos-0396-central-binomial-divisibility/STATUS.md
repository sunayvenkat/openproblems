# Status ledger — Erdős #396

Legend: **PROVED** (proof written in DRAFT.md) · **COND** (conditional) · **NUM** (numerical evidence only) · **FALSE** (refuted) · **OPEN**.
Section numbers refer to [DRAFT.md](DRAFT.md). Code paths are relative to `code/`.

## Main theorems

| Item | Status | Hypothesis / caveat | DRAFT | Code |
|---|---|---|---|---|
| Theorem C: E₁ infinite, positive density along n = (12x−1)(22x+9); M_∞ = 0.411 | PROVED | awaiting independent check of §12.3–12.4 | §12.4 | `h1/` |
| Theorem C′: family n = 2(12x+5)(35x+32); M_∞ = 0.375 | PROVED | same | §12.4 | `h1/` |
| Theorem D: E₂ infinite, positive density along n = (14x−1)(15x−1); M_∞ = 0.745 | PROVED | same | §12.4 | `h1/` |
| Theorem A: E₁ via P₁P₂ − 2P₃P₄ = 1 | COND | Dickson, one admissible 4-tuple | §11 | `g5/`, `g/verify_g5.py` |
| Theorem B: E₂ via a 6-tuple | COND | Dickson, one admissible 6-tuple | §11 | `g5/`, `g/verify_g5.py` |
| Theorem 1: E₁ via exponents (123, 59814755) | COND | Schinzel H for 133 polynomials; finite computation done exactly | §8 | `aur/`, `g4/`, `g/top_exact.py` |
| Theorem 2: E_k infinite ∀k | COND | H + Conjecture G | §9 | `g1/`, `g2/`, `g3/` |
| E_k infinite for k ≥ 3 | OPEN | first-moment method needs linear pieces; linear-piece families stop at k = 2 (Fermat, Yuzvinsky, cubic/quartic searches); route via E₂ family + irreducible quadratic members needs Hypothesis BH_u and a Ford–Konyagin-type analysis | §13 | `g6/`, `h2/` |

## Supporting lemmas

| Item | Status | DRAFT | Code |
|---|---|---|---|
| Lemma 1 (local reduction at q > 2i) | PROVED; 49478 random checks | §1 | `agentV/lemmas.py` |
| Small primes by CRT | PROVED | §2 | — |
| Thm 4.1 digit carry criterion | PROVED; 12 Kummer checks | §4 | `agentAC/verify_kummer.py` |
| Binomial reduction (series length ~ s·d) | PROVED | §4 | `aur/deep.py` |
| A1(a)–(e) sufficient conditions for non-top pieces | PROVED | §5 | `agentAC/` |
| Lemma A (all non-top pieces good) | **FALSE** — m = 1365, d = 455 | §5 | `agentAC/check455.py`, `agentV/ce1365.py` |
| Thm A3 (fixed d, all large K good) | PROVED (K₀ not explicit) | §5 | `agentAC/a3check.py` |
| Trace predictor (§5.1) | heuristic, matched 9/9 + d = 319865 | §5.1 | `aur/trace.py` |
| Lemma X (exact low levels) | PROVED | §5.2 | `g3/` |
| Theorem E (effective A3) | proof sketch only | §5.2 | `g3/` |
| Prop F | sketch | §5.2 | `g3/` |
| Thm I (inheritance d → dp) | PROVED | §5 | `agentAC/inherit_test.py` |
| Top-piece autocorrelation formula | PROVED; checked 5 cases | §6.1 | `aur/autocorr.py` |
| "No parametric shortcut" for top piece | PROVED | §6.3 | — |
| Aurifeuillean integrality lemma | PROVED | §7.2 | `aur/aurif3.py` |
| Aurifeuillean splitting with prime exponent | **FAILS** | §7.3 | `aur/scanA.py` |
| At most one Aurifeuillean block member | PROVED | §7.5 | — |
| Exact certificate of all 128 pieces of m₂ = 59814755 | PROVED (exact integers, python-flint + independent CRT) | §8.5 | `g4/exact.py`, `g4/level2.py`, `g/top_exact.py` |
| L1/L2/L3 localization, inflation | PROVED; numerically checked | §9.1 | `g/crossing.py`, `g/inflate.py` |
| Theorem W (near-Lehmer T = 2) | PROVED; 9365 + 4110 checks | §9.2 | `g1/` |
| NL(P) existence | OPEN; Lehmer-strength, likely harder than G | §9.4 | `g1/search.py`, `g1/heur.py` |
| Peak lemma (|Ψ_m| at q-th roots of unity) | PROVED | §9.5 | `g2/peak.py` |
| Conjecture G | OPEN; 17 good / 14 bad among squarefree odd m ≤ 6000 with m/φ ≥ 2; top-goodness depends only on rad(m); the first exponent with two levels, m₁ = 111546435, is top-bad at both levels (exact, six-prime CRT); sampled-convolution identity settles m₁·r for every prime r ≤ 3φ(m₁)+1: 65.5 % top-good (72.7 % while both levels are live), ≈50 % per level, all bad beyond; trace formula and peak dominance for ±3 mod 8 exponents give a candidate sign mechanism (§13.10–13.11) | §9, §13.7, §13.8, §13.11 | `h2/toppiece_scan.py`, `h2/toppiece_T3.py`, `h2/toppiece_rscan.py`, `h2/rscan_m1.npz` |
| Trace formula for the top coefficient c(m) = [y^{m−1}]Φ_m^{−2} | PROVED (partial fractions); exact on 8 cases | §13.10 | `h2/trace_top.py` |
| Peak dominance for m with all primes ≡ ±3 mod 8 | NUM: largest trace term sits at 8a ≡ ±1 mod 8 and predicts sgn c(m) in 41/85 (r=4), 619/705 (r=5), 9/9 (r=6), 8/8 (r=7, exact); bulk sup bound and large-P band sum open | §13.11 | `h2/trace_peak.py`, `h2/trace_peak_scan.py`, `h2/peak_r7.py` |
| Lemma Q | PROVED | §11 | `g5/` |
| Lemma S (square-class rule) | PROVED; 3568/3568, 5696/5696 checks at x ≈ 10¹⁵ | §12.2 | `h1/detect.py` |
| Lemma W (medium primes equidistribution) | PROVED | §12.3 | `h1/lawcheck.py` |
| Lemma W′ (second coin, L = 3) | PROVED | §12.3 | — |
| First-moment theorem | PROVED | §12.4 | — |
| Classification of quadratic families | PROVED + complete enumeration | §12.5 | `h1/apsq.py`, `h1/search2.py` |

## Known caveats in the data

- `agentAC/fastser.py` reconstructs coefficients by CRT from two primes; valid only while |coefficient| < 2.3·10¹⁸. The "738 of 1487 fully good" count (§6.4) and AC's full scans depend on it and **need recheck**.
- Fallback exponent 50115065: 45 of its 46 band pieces rest only on the floating-point residue method `g3/resid.py`; needs exact check before use (§10).
- `agentU/REPORT.md` calls its cofactor lemma "Lemma X" and its size lemma "Lemma W"; these are **not** the Lemma X of §5.2 or the Lemma W of §12.3.
- `code/NOTES.md` is an early snapshot (says k ≤ 14 computed; current is k ≤ 16).

## Open items, in priority order

1. Second reader for §12.3–12.4: constant bookkeeping in Claims 1–2 (η = ε/32, H = ⌊q^{ε/8}⌋), pairing argument for |𝒯| in Case F < q^ε, uniformity of PNT in progressions for the top regime, o(1) accounting of excluded prime windows.
2. Literature search for Lemma S, Theorems A–D, and digit equidistribution of polynomial values at their own prime factors.
3. E₃ / E₄: no linear-piece family is expected (§13.2). Either prove the cubic four-term progression impossible, or carry out the §13.3 program: Ford–Konyagin-type density for the irreducible members n − i (i ≥ 3) of an E₂ family under Hypothesis BH_u (Bateman–Horn uniform in the cofactor).
4. (Conditional route, lower priority) Conjecture G; exact recheck of the `fastser.py`-based counts.
