# Erdős #168 part (i): the finite optimum and the constant c

- [PROOF.md](PROOF.md): self-contained proof of the finite min-cover formula (C) τ(t) = min_j (K_j − I_j − P_j), t ≥ 3.
- [REPORT.md](REPORT.md): verdict, increment rule η_{a,b}, formula for c, the 128-digit certified enclosure, and the staircase observation.
- [audit/](audit/): independent referee re-derivation (`AUDIT.md`), with its own scripts and outputs.
- Verification scripts. `tau_dp.py` and `rowdp.py` are exact solvers. `brute_check.py` is a brute-force cross-check. `c_digits.py` computes the enclosure. `eta_rule.py` is the increment rule. `test_*.py` and `lemma_probe.py` are lemma probes. `S3_big.txt` is saved output.
- [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json): SHA-256 of every file at the time it was imported into the part (ii) workspace.
