# code/ — index

Every claim in [../DRAFT.md](../DRAFT.md) that rests on computation is backed by a script here. Saved outputs (`*_out.txt`, `*.txt`) sit next to the script that produced them. Folder names are the agent/workstream names used in DRAFT.md.

## Running

- Python 3. Dependencies: `sympy`, `numpy`; `python-flint` for the exact certificates in `g4/` and `g/top_exact.py`.
- **Run each script from inside its own folder** (`cd code/aur && python deep.py ...`). Many scripts do `sys.path.insert(0, '..')` or `'../agentV'` and import shared helpers such as `poly.py`, `lemC.py`, `agentV/fastgood.py`.
- Exception: `h2/lemmaSprime.py` hard-codes an absolute Windows path to `h1/`; edit that line before running elsewhere.

## Map: folder → DRAFT section → purpose

| Folder | DRAFT | Purpose | Start with |
|---|---|---|---|
| top level (`poly.py`, `lemC.py`, `fastC.py`, `scanC.py`, `top.py`, `modcheck.py`, `sympy_free.py`) | §4, §6 | shared polynomial/series helpers; early carry-criterion scans | `NOTES.md` (early notes) |
| `agentAC/` | §4–§6 | digit carry criterion (Thm 4.1), A1(a–e), Thm A3, inheritance, Lemma A counterexample 1365, top-piece scans | `REPORT.md` |
| `agentV/` | §1, §3, §5, §10 | referee: Lemma 1 checks, 1365 counterexample on a 709-digit prime, independent piece checks, witnesses in E₁/E₂ | `REPORT.md`, `verify396.py` |
| `agentU/` | — | literature survey and unconditional-route obstructions (full texts not included) | `REPORT.md`; `tools/pdftxt.py` |
| `aur/` | §5.1, §7, §8.4 | Aurifeuillean factor F, carry levels of F(±y), autocorrelation, deep pieces of m₂, trace predictor, coverage audit | `coverage.py`, `deep.py` |
| `g/` | §8.5, §9.1, §11 | localization lemmas L1–L3, inflation, exact top coefficient of m₂, check of Theorems A/B | `LEMMAS.txt`, `verify_g5.py` |
| `g1/` | §9.2–§9.4 | near-Lehmer route: Theorem W, last-level rule, searches for small ρ = m − 2φ(m), heuristic counts | `verify.py`, `search.py` |
| `g2/` | §9.5 | bulk analysis of the top piece: Ramanujan form, peak lemma, saddle predictor | `RESULTS.txt` |
| `g3/` | §5.2, §10 | Lemma X, effective A3 (Thm E), band surveys, float residue method, piece 10023013 of 50115065 | `RESULTS.txt` |
| `g4/` | §8.5 | **exact certificate** of all 127 non-top pieces of m₂ = 59814755 (python-flint + CRT bound) | `exact.py`, `level2.py` |
| `g5/` | §11 | linear-form families: Lemma Q, Theorems A (E₁) and B (E₂) under Dickson | `final_check.py` → `final_check_out.txt` |
| `g6/` | §11, §12.7 | search for E₃/E₄ polynomial families (quartic/cubic routes, composition); found identities use irreducible quadratic pieces, not yet written up in DRAFT | `check.py`, `final_e3.py`, `e4final.py` |
| `h1/` | §12 | **unconditional Theorems C/D**: family search and classification, Lemma S and digit-law tests, brute-force proportions | `search2.py`, `apsq.py`, `verify.py`, `detect.py` |
| `h2/` | §13.2 | cubic/quartic families with many split fibers: Cardano/Eisenstein enumeration of all split cubic fibers per norm (`torus_ap.py`, no 4-term progression or ratio-3 pair to height 300), rational-point grouping (`cubic_ap_rat.py`), quartic e₄ groups (`pte4*.py`), test of a Lemma S′ variant, factor structure of the minimal elements a(k) (`a375077.py`); §13.7–13.8 top-piece signs: exact level coefficients of m₁ = 111546435 (`toppiece_T3.py`), two-scale values for m₁·29, m₁·31 (`toppiece_m1r.py`, ten-prime confirmation `toppiece_m1r_x4.py`), sampled-convolution scan over all prime multipliers (`toppiece_rscan.py m0 e rmin rmax nprimes [check]`; results `rscan_m1.npz`, about 1 h per level with 12 CRT primes, needs ~3 GB RAM); §13.10–13.11 trace formula and peak dominance (`trace_top.py`, `trace_peak.py`, `trace_peak_scan.py MMAX EXACT`, `peak_r7.py MMAX N`; outputs `peak_scan.txt`, `peak_r7.txt`) | `torus_ap.py`, `toppiece_rscan.py 105 2 11 97 3 check` |

## Key result → script

| Claim | Script → output |
|---|---|
| Lemma 1 (49478 random cases) | `agentV/lemmas.py` |
| Thm 4.1 vs direct Kummer (12/12) | `agentAC/verify_kummer.py` → `verify_kummer.txt` |
| 1365 counterexample to Lemma A | `agentAC/check455.py`, `agentV/ce1365.py` |
| 25 deep pieces of m₂ | `aur/deep.py` → `deep_out*.txt`; `aur/strict.py` → `strict_out.txt`; exact: `g4/exact.py` → `exact_out.txt`, `exact_crt_out.txt` |
| 20 A1(e) pieces of m₂ | `aur/checkB.py` → `checkB_out.txt`; exact: `g4/level2.py` → `level2_out.txt` |
| Top coefficient −74322712269080 of m₂ | `g/top_exact.py` |
| All 128 divisors of m₂ accounted for | `aur/coverage.py` |
| Theorems A and B checks | `g5/final_check.py` → `final_check_out.txt`; `g/verify_g5.py` |
| Lemma S (3568/3568, 5696/5696 at x ≈ 10¹⁵) | `h1/detect.py` |
| Digit laws 2^{1−L} | `h1/lawcheck.py`, `h1/rulecheck.py` |
| E₁/E₂ proportions along Theorem C/D families | `h1/verify.py`, `h1/sample.py`, `h1/ek.py` |
| Quadratic-family classification (93 121 E₁ / 4 964 E₂ families) | `h1/apsq.py`, `h1/search2.py`, `h1/search_e2*.py` |
