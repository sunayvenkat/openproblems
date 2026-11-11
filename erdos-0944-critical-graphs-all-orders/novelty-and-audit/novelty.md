# Erdős 944: novelty, prior constructions, and priority audit

Audit cutoff: 6 November 2026. Findings below separate public chronology, mathematical scope, and this auditor's inferences. This is a literature/priority audit; the companion seed and transfer audits handle the full correctness investigation.

## 1. Has the single-seed or all-orders theorem already appeared?

### Takeaway

**Yes. The qualitative all-orders conclusion and the single-seed quadratic transfer are already explicit in a public 2 October 2026 proof by GitHub user peilinliu66-dev.** It uses the same three skeletons and the same three additive increments as the present draft. The current draft cannot responsibly be presented as the first all-orders solution or the first single-seed order-completion theorem. The strongest possible remaining distinction is an improvement of the sufficient numerical bound, with its priority still unestablished. [Prior immutable proof, Theorems B4 and B, §§4–7](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/PROOF.md)

### Cited Findings

- Theorem B4 of the prior proof states: from a finite `(4,r)`-graph on `g` vertices, every order at least `140g²−148g+39` is realizable. Theorem B combines this with the credited seed theorem to give prescribed orders for `k=4`, and with Skottová–Steiner for `k≥5`. Its definition uses vertex-criticality and resistance to deleting **any** set of at most `r` unordered edges. Thus there is no criticality or quantifier mismatch that would distinguish our qualitative target. [PROOF.md, §1, Theorems B4 and B](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/PROOF.md)
- The prior skeletons are precisely `K4`, a five-cycle with a universal hub, and `M(C5)`, with vertex/edge counts `(4,6)`, `(6,10)`, `(11,20)`. Applying the unequal-input form of Skottová–Steiner's substitution to one already constructed graph of order `M` and other inputs of order `g` gives `M+(h−1)+(e−1)(g−1)`. Consequently its order increments are exactly `A=5g−2`, `B=9g−4`, `C=19g−9`. [PROOF.md, §§4–5, equations (9)–(12)](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/PROOF.md)
- Its arithmetic uses `−8A+15B−5C=1`. For `T=n−g`, residues `x≡15T (mod A)` and `y≡−5T (mod A)` chosen in `[0,A−1]` give `xB+yC≡T (mod A)` and `xB+yC≤(A−1)(B+C)`. This proves the explicit threshold. [PROOF.md, §6, equations (13)–(17)](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/PROOF.md)
- The formal endpoint `RobustCriticalGluing.prescribed_order_four` has the actual quantifiers `∀r ∃B ∀n≥B ∃ finite V,G`, with `Nat.card V=n` and `IsErdos944 G 4 r`. Its chosen threshold is the simpler `140g²`; it imports and discharges the seed premise. [OptionalAllOrders.lean, theorem beginning at line 71](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/OptionalAllOrders.lean#L71)
- The repository reports source compilation, three module replays, and eight final axiom closures containing only `propext`, `Classical.choice`, and `Quot.sound`. These are the author's reproduction records, not checks rerun in this subtask. [VERIFICATION.md](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/VERIFICATION.md)
- Kohlmeyer's 10 October comment explicitly recognizes the other author's prescribed-order extension and distinguishes it from the original finite-existence proof. The seed authors' own source index separately credits the bridge to the PR author. [Kohlmeyer comment, 05:35:09 UTC](https://github.com/TheJustinSunPrize/awards/pull/4668#issuecomment-6094259665); [authors' SUBMISSIONS.md](https://github.com/JENW1N/complete-math-solutions/blob/caa0b07847cc94a071215de82036be4b5805ee0c/SUBMISSIONS.md)

### Inferences

- This is stronger evidence than a superficially related paper or a search miss: the prior proof matches the target quantifiers, the seed dependence, all three small graphs, and the three generating integers. Our use of Hajós joins packages the same order increments through a different composition route; it does not recover novelty for the qualitative result.
- The prior residue proof checks directly: its congruence and nonnegative-coefficient argument are valid, and the recursive substitution preserves the same fixed `r`. I found no mathematical defect in this part on inspection. Its conditional transfer is independent of whether the external seed proof is correct. The unconditional conclusion in both works still depends on that seed.
- The present `45g²` bound is smaller than the exhibited `140g²` bound, but improvement relative to this one source is different from novelty in the literature. Neither constant is presented here as optimal. The prior recursive construction starts at `g`, so our draft's starting order `6g−2` is unnecessary for its additive semigroup argument.

### Gaps

- No fresh Lean build or independent-kernel replay was performed in this subtask. The open prize-catalogue PR does not establish journal publication, specialist review, or prize acceptance. These limitations do not erase the prior public mathematical statement and argument.
- The search does not establish that `45g²` is a new, best, or significant quantitative bound. It only establishes that the specific current prior package exposes `140g²` and that the qualitative novelty claim is untenable.

## 2. What are the exact chronology and source scopes?

### Takeaway

The evidence supports separate attribution: Skottová–Steiner for substitution and higher-colour all-orders results; Kruer–Kohlmeyer for arbitrary-robustness four-colour seeds; peilinliu66-dev for an explicitly published October all-orders bridge. Manuscript dates, Git commit dates, public hosting dates, and certification dates must not be conflated.

### Cited Findings

| Event | Verified date or status | Primary evidence |
|---|---|---|
| Skottová–Steiner arXiv submission | v1, 12 Aug 2025, 07:46:29 UTC; only version listed in live submission history | [arXiv history](https://arxiv.org/abs/2508.08703) |
| Skottová–Steiner journal status | Author's current research list says submitted | [Steiner research list](https://sites.google.com/view/raphael-mario-steiner/research) |
| Seed service verification | 11 Sep 2026; exact acceptance time 21:06:04 UTC appears in review text and coauthor comment | [Conjectures.io record](https://conjectures.io/results/e7afff2c-bb07-4fa8-92b6-67a530aaad70) |
| Seed public certification | 16 Sep 2026 | [Conjectures.io record](https://conjectures.io/results/e7afff2c-bb07-4fa8-92b6-67a530aaad70) |
| Prior bridge source commit | `34ddb4a51b13e56c39397e1e3855ab8e86bf46af`, 2 Oct 2026, 16:24:03 UTC | [Commit](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/commit/34ddb4a51b13e56c39397e1e3855ab8e86bf46af) |
| Prior bridge repository | Created 2 Oct 2026, 16:24:16 UTC; pushed 16:24:23 UTC; default branch `codex/jsp785` | [Repository metadata](https://api.github.com/repos/peilinliu66-dev/jsp785-erdos944-cofinite-orders) |
| Public submission of bridge | PR #4668 created 2 Oct 2026, 16:30:56 UTC; remains open and unmerged | [Public PR](https://github.com/TheJustinSunPrize/awards/pull/4668) |
| Kohlmeyer's explicit acknowledgement | 10 Oct 2026, 05:35:09 UTC; source-registration follow-up at 05:42:49 UTC | [First comment](https://github.com/TheJustinSunPrize/awards/pull/4668#issuecomment-6094259665), [second comment](https://github.com/TheJustinSunPrize/awards/pull/4668#issuecomment-6094312797) |
| Seed source-edition repository | Created 10 Oct 2026, 05:34:48 UTC; first commit `8b9db1...` at 05:34:47 UTC | [Repository metadata](https://api.github.com/repos/JENW1N/complete-math-solutions), [initial commit](https://github.com/JENW1N/complete-math-solutions/commit/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23) |

- Skottová–Steiner Problem 1.1 asks `f_k(n)→∞`; Theorem 1.2 settles `k≥5`. Lemma 2.1 applies to `k≥4` and gives order `h+Σ(n_i−1)`. Lemma 2.2 uses odd wheels and Hajós joins. Theorem 2.3 needs a progression of seed orders, not an arbitrary single seed, and assumes `k≥5`. Section 5 still leaves `k=4` open. The construction idea credits Wang. [SS, Problem 1.1; Lemmas 2.1–2.2; Theorem 2.3; §5](https://arxiv.org/html/2508.08703v1)
- Wang's 2009 paper establishes an infinite family from each vertex-critical graph without critical edges, an antecedent for the `r=1` construction idea. The publisher's accessible abstract does not claim every sufficiently large order. Full text was subscription-only and was not obtained, so stronger details are unverified. [Wang, COCOA 2009, pp. 238–248, DOI 10.1007/978-3-642-02026-1_22](https://link.springer.com/chapter/10.1007/978-3-642-02026-1_22)
- The accepted Conjectures.io target is existential over the graph for every `k≥4,r≥1`; it does not prescribe its order. The review distinguishes earlier Chan and Kitamura `k=4,r=1` constructions from arbitrary `r`. It expressly disclaims an originality guarantee and states that review did not itself perform a fresh Lean/independent-kernel replay. [Conjectures.io, formal statement and review decision](https://conjectures.io/results/e7afff2c-bb07-4fa8-92b6-67a530aaad70)
- The live seed PDF retrieved by the companion seed auditor is titled *Vertex-critical four-chromatic graphs with no small critical edge set*, by Liam Kruer and Jensen Kohlmeyer, dated 10 September 2026. Its SHA-256 is `77e311d97357f98fc33db89ddd63ca6fc3fc5c610bf90075cd9dc1077922ecb8`, matching the repository manifest. Page 1, Theorem 1.1 gives finite seeds, and the scope paragraph explicitly declines the stronger prescribed-order assertion. [Pinned PDF](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos-944.pdf); [manifest](https://github.com/JENW1N/complete-math-solutions/blob/caa0b07847cc94a071215de82036be4b5805ee0c/SOURCE_MANIFEST.json)
- The October PR instead cites an 18 September exposition, and the coauthor points to an earlier repository manuscript. Therefore editions must be identified by pinned file/hash; their printed dates alone do not prove public disclosure. The source-edition README itself makes that distinction. [PR body](https://github.com/TheJustinSunPrize/awards/pull/4668); [coauthor's earlier manuscript link](https://github.com/lkruer/conjectures/blob/e88dec4c88e42824b4acd3f9559febe67115471b/problems/erdos-944/paper/proof.pdf); [source-edition README](https://github.com/JENW1N/complete-math-solutions/blob/caa0b07847cc94a071215de82036be4b5805ee0c/README.md)

### Inferences

- The safest public chronology is that the single-seed/all-orders bridge was publicly submitted by 2 October, and expressly acknowledged by a seed coauthor by 10 October. Git author timestamps alone would be weaker evidence, but the repository creation, public PR, and separate comments corroborate the ordering well before 6 November.
- SS's stated results do not themselves literally settle four-colour all-orders existence; the later bridge supplies the elementary order arithmetic. Calling the current work a routine corollary of known machinery is a mathematical characterization, not a claim that SS already printed the same theorem. The October source removes the need to guess whether that corollary had been made explicit.
- “Critical” must remain qualified: robust output graphs are vertex-critical, whereas the substitution skeletons must also be edge-critical. An edge-critical output cannot tolerate even one edge deletion. Arbitrarily high robustness at some orders is logically different from a limit over every large order; the prior October work addresses the latter explicitly.

### Gaps

- The live Erdős Problems main page, forum, proof-claims page, and history page could not be fetched: web/search-service returned 403 or restricted-URL responses, and the shell HTTP attempt was network-blocked. I therefore do **not** assert their current status label or the absence of additional forum discussion. Their URLs were attempted directly: [944](https://www.erdosproblems.com/944), [forum](https://www.erdosproblems.com/forum/thread/944), [proof claims](https://www.erdosproblems.com/forum/thread/944/proof-claims), [history](https://www.erdosproblems.com/history/944).
- The original 1989 Erdős page and all older journal papers were not fully reread. Precise modern quantifiers were checked in SS and the primary proof package. No journal publication of the October bridge was found or claimed.

## 3. What can still be claimed, and what did the search exclude?

### Takeaway

Recommended conclusion: **the all-orders result is not new as a publicly stated theorem or construction method.** The present draft gives an independently checked presentation and a smaller sufficient constant than the located October bridge; priority for that quantitative refinement is not established. Its unconditional application must still be described with the correct dependence on Kruer–Kohlmeyer.

### Cited Findings

- The prior source repository currently exposes only the single October 2 commit. The public prize PR contains one commit and exactly two discussion comments, both the October 10 coauthor attribution/source-registration comments; no subsequent constant improvement appears there. [Source commit history](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/commits/codex/jsp785); [PR discussion](https://github.com/TheJustinSunPrize/awards/pull/4668)
- Direct inspection of `PROOF.md`, `CofiniteOrders.lean`, `FiniteGraphOrders.lean`, `OptionalAllOrders.lean`, and `VERIFICATION.md` found the quadratic bound 140 and an older auxiliary cubic argument, with no parity-based 45 improvement or variable-wheel refinement. The source arithmetic includes `coprime_a_b`, but its auxiliary `b` is a constructed composite increment, not our `9g−4`. [CofiniteOrders.lean](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/CofiniteOrders.lean); [FiniteGraphOrders.lean](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/FiniteGraphOrders.lean)
- The seed authors' index is what led to the decisive prior bridge. Their original Lean seed source contains SS credits, but searching its text for all-orders/sufficiently-large/Hajós/cofinite/one-seed/limit terms did not reveal a prescribed-order theorem. Its target was checked against the separately explicit endpoint above. [Seed source](https://github.com/JENW1N/complete-math-solutions/blob/caa0b07847cc94a071215de82036be4b5805ee0c/proofs/Erdos944.lean); [index](https://github.com/JENW1N/complete-math-solutions/blob/caa0b07847cc94a071215de82036be4b5805ee0c/SUBMISSIONS.md)

### Inferences

- Suitable draft language: “We refine the explicit sufficient bound in the October 2026 single-seed completion of peilinliu66-dev, using the Skottová–Steiner substitution and the same small skeletons. The qualitative all-orders conclusion is prior.” If the final mathematical audit changes the bound or proof, the description should track that final result.
- Unsuitable language: “we close the all-orders gap,” “first single-seed order completion,” or “new solution of Erdős 944” without explicitly distinguishing earlier contributions. The current sentence that a source search did not establish whether completion appeared elsewhere is now obsolete.
- No negative search result proves novelty. Even the bounded numerical comparison is only against the inspected source, and easier arithmetic improvements can exist without being written as separate theorems.

### Gaps

- Search scope: live arXiv abstract/history and full HTML; author publication list; SS's relevant references; publisher Wang abstract; Conjectures.io record and review; seed repository README, manifest, source, submission index and commit history; the discovered bridge's immutable mathematical proof, principal arithmetic/order/endpoint source files, verification report, current repository metadata, source commit history, and every PR discussion comment. Queries included the exact paper title, author names with 944, vertex-critical plus all sufficiently large, four-chromatic plus all orders, single seed, cofinite/prescribed orders, and Wang's exact title. Most generic searches were noisy; the decisive evidence came from following primary-source citations.
- The search was not exhaustive across unindexed manuscripts, all repositories, paywalled texts, private correspondence, or inaccessible forum/history pages. It is sufficient to defeat qualitative novelty because a matching prior source was found; it cannot certify earliest worldwide priority or novelty of a threshold improvement.
- No external posting, author contact, formal proof rebuild, or changes to older workspace files were made by this subtask. The seed PDF identity above was independently fetched by the companion seed auditor; this subtask's direct PDF web routes failed, and Conjectures.io's current explanation-PDF link returned 404.
