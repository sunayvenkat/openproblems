# References

Sources consulted during the work (summary from `code/agentU/REPORT.md`). Full texts are not stored in this repository.

| Source | Relevance |
|---|---|
| P. Erdős, R. L. Graham, *Old and New Problems and Results in Combinatorial Number Theory*, Monogr. Enseign. Math. 28 (1980) | Origin of the problem |
| OEIS [A375077](https://oeis.org/A375077) | Smallest n ∈ E_k; 16 terms (k ≤ 16) as of July 2026 |
| [erdosproblems.com/396](https://www.erdosproblems.com/396) / teorth database | Lists #396 as open (2025-08-31) |
| C. Pomerance, "Divisors of the middle binomial coefficient", Amer. Math. Monthly 122 (2015) 636–644 | n−k \| C(2n,n) infinitely often (n = pq + k); n+k divides on a density-1 set |
| C. Pomerance, "Remarks on the middle binomial coefficient" (preprint, 2026) | "+"-side results only |
| K. Ford, S. Konyagin, Trans. AMS 374 (2021) | n^ℓ \| C(2n,n) has positive density; closest model for digit equidistribution |
| A. Balog, T. D. Wooley, J. Austral. Math. Soc. A 64 (1998) | Cyclotomic construction (the "−" family of `code/NOTES.md`) |
| A. Hildebrand (1985, 1989), stable sets; R. McNamara, arXiv:2312.08544 | Stable-set route; shown inapplicable (D₀ is not stable) |
| J. Teräväinen (2018); T. Tao, J. Teräväinen, arXiv:2512.01739 | Correlations of multiplicative functions; 1_{D₀} is not multiplicative |
| Drmota–Tichy, *Sequences, Discrepancies and Applications*, Thm 1.21 | Erdős–Turán–Koksma inequality (Lemma W) |
| R. C. Vaughan, *The Hardy–Littlewood Method*, Lemma 2.2 | Weyl-sum bound (Lemma W) |
| Pomerance; Banks–Luca; Banks–Güloğlu–Nevans; Luca–Pomerance | Upper bounds for n − kφ(n) small (near-Lehmer route, §9.4) |
| dehorty Erdős-396 witness-search repo | Lean proof of the small-prime barrier (= Lemma 1); exhaustive minimal witnesses k = 8–13 |
| lacker/erdos396 (unrefereed) | Conditional k = 1 program, depends on two unproved estimates |
