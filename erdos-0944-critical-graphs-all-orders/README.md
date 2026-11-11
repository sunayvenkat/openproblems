# Erdős #944 (all-orders form): robust vertex-critical 4-chromatic graphs

**Problem.** A (4,r)-graph has χ = 4, χ(G − v) = 3 for every vertex v, and χ(G − F) = 4 for every set F of at most r edges. Let f₄(N) be the largest such r at order N. Does f₄(N) → ∞? This is Skottová–Steiner Problem 1.1 with k = 4; Kohlmeyer–Kruer give a seed for each r.

## Status: SOLVED, but this argument is not new

- [erdos944-all-orders-transfer.tex](erdos944-all-orders-transfer.tex). **Order-completion theorem:** a (4,r)-graph on g vertices gives (4,r)-graphs on every N ≥ 45g². The proof uses the Skottová–Steiner substitution lemma and Hajós joins of K₄, the wheel W₅ and the Grötzsch graph. Together with the Kohlmeyer–Kruer seed theorem this gives f₄(N) → ∞.
- [novelty-and-audit/REPORT.md](novelty-and-audit/REPORT.md). The argument survived an adversarial audit, and the seed theorem was cross-checked twice. **Prior art:** a public proof dated 2 Oct 2026, acknowledged by Kohlmeyer, uses the same three skeletons and gets 140g². Only the smaller constant 45g² is ours, and its significance is unclear.
- [transfer-investigation/](transfer-investigation/): how the transfer was found and the source-scope check.

The seed paper's PDF, Lean source and page images are not included. They are third-party; see the links in the reports.
