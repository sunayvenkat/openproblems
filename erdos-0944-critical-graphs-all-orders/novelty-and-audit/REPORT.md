# Erdős 944 survives audit, loses novelty

**The qualitative all-orders result and the single-seed completion theorem are not new.** A public proof by GitHub user peilinliu66-dev, submitted on **2 October 2026**, already obtains the same conclusion using the same three skeletons and the same order increments. Kohlmeyer explicitly acknowledged that extension on 10 October. The present draft gives a smaller sufficient bound, $45g^2$ instead of the located proof's $140g^2$, but the priority and significance of that numerical refinement remain unestablished. On correctness, the transfer survived a detailed adversarial audit, and Kohlmeyer–Kruer's seed theorem survived a complete ordinary-mathematics audit plus two independent source-first crosschecks. **No fatal gap or counterexample was found.** This supports the argument's mathematical validity; it is not a fresh formal certification or a guarantee against every possible error. ([Prior proof, Theorems B4 and B](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/PROOF.md), [acknowledgement](https://github.com/TheJustinSunPrize/awards/pull/4668#issuecomment-6094259665))

## The October proof already contains the same bridge

A $(4,r)$-graph is a finite simple graph with $\chi(G)=4$, $\chi(G-v)=3$ for every vertex, and $\chi(G-F)=4$ for **every** set of at most $r$ unordered edges. Let $f_4(N)$ be the largest available positive tolerance at order $N$, or zero when none exists. The desired limit is the precise statement $\forall r\,\exists N_r\,\forall N\ge N_r:\ f_4(N)\ge r$. Skottová–Steiner's 2025 paper asks this question, proves the higher-color cases, and supplies the substitution lemma valid also for four colors. Kohlmeyer–Kruer supply a finite seed for each $r$; their manuscript expressly declines the prescribed-order conclusion. ([Skottová–Steiner, Problem 1.1 and Lemma 2.1](https://arxiv.org/html/2508.08703v1), [seed theorem, p. 1](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos-944.pdf))

The decisive prior source is commit `34ddb4a51b13e56c39397e1e3855ab8e86bf46af`, dated 2 October 2026, with a public submission that same day. Its Theorem B4 takes one seed of order $g$ and realizes every order at least $140g^2-148g+39$. It uses $K_4$, the five-cycle with a universal hub, and the Grötzsch graph $M(C_5)$, producing exactly

\[
A=5g-2,\qquad B=9g-4,\qquad C=19g-9.
\]

Unequal-seed substitution puts a current graph on one skeleton edge and the fixed seed on the others, adding $A$, $B$, or $C$. The identity $-8A+15B-5C=1$ and a nonnegative residue representation prove its threshold. The definitions and quantifiers match the present target; there is no weaker criticality convention or hidden restriction to a subsequence of orders. The draft packages the increments through Hajós joins, which does not restore qualitative novelty. ([Immutable proof, §§1, 4–7](https://github.com/peilinliu66-dev/jsp785-erdos944-cofinite-orders/blob/34ddb4a51b13e56c39397e1e3855ab8e86bf46af/PROOF.md), [public submission](https://github.com/TheJustinSunPrize/awards/pull/4668))

The public record establishes prior disclosure, **not journal acceptance**: the prize submission remained open and unmerged at the 6 November audit cutoff. The search also could not retrieve the live Erdős Problems pages and did not exhaust paywalled or unindexed sources. Those limitations prevent a claim of earliest worldwide priority, but cannot undo an identified matching prior proof. Attribution should distinguish Skottová–Steiner's substitution, Kruer–Kohlmeyer's seeds, and peilinliu66-dev's explicit all-orders bridge. ([Chronology, source comparison, and search limits](<novelty.md>))

## The local transfer survives the critical failure modes

The [audited draft](<../erdos944-all-orders-transfer.tex>) proves a valid conditional theorem: **one $(4,r)$-seed on $g$ vertices gives every order $N\ge45g^2$**. The crucial distinction is that the seed is vertex-critical and edge-robust, while the skeleton is both vertex-critical and edge-critical. Applying Hajós joins directly to robust seeds would fail vertex-criticality; the draft correctly joins only skeletons. The full step-by-step review found no incorrect coloring certificate, omitted deletion case, or arithmetic obstruction. ([Transfer audit](<transfer.md>))

The strongest deletion attack is to distribute the $r$ removed edges among gadgets. It fails for a local reason. Splitting one seed vertex into two terminals partitions its incident edges without duplication. Equal terminal colors therefore recover the original seed's monochromatic-edge count exactly, forcing at least $r+1$ such edges. Every three-color assignment on the substituted graph gives an equally colored skeleton edge, so **one gadget alone** exceeds the entire deletion budget. The skeleton edge merely identifies that gadget; it is not mistakenly counted as a retained edge. ([Substitution and robustness audit](<transfer.md>))

Vertex-criticality also survives both necessary cases. Deleting an internal gadget vertex allows equal terminal colors using the corresponding punctured seed; a coloring of the edge-deleted skeleton forces precisely that equality. Deleting a skeleton vertex leaves incident gadgets with one terminal, whose surviving boundary color can always be matched. Four-colorability extends independently across disjoint interiors. Every vertex deletion has chromatic number exactly three, since a two-colorable puncture would make the original graph three-colorable after restoring one vertex. ([Deletion-case derivations](<transfer.md>))

Counting gives $N=6g-2+aA+bB+dC$ for arbitrary nonnegative coefficients. Since $9A-5B=2$, odd $g$ gives coprime $A,B$; even $g$ gives coprime $A/2,B/2$ and odd $C$. The two-generator conductor bound, with zero or one $C$ correcting parity, yields exactly

\[
N\ge
\begin{cases}
45g^2-46g+13,&g\text{ odd},\\
\dfrac{45}{2}g^2-8g+1,&g\text{ even}.
\end{cases}
\]

Both imply the advertised $45g^2$ threshold. Choosing one seed separately for each fixed $r$ then proves the limit without assuming monotonicity of $f_4$. An optional variant using variable odd wheels and $M(C_3)$ proves the smaller sufficient bound $20g^2$; its derivation is recorded separately, with **no optimality or novelty claim**. This reinforces why a numerical improvement alone does not establish a new research contribution. ([Arithmetic audit and optional refinement](<transfer.md>))

## The seed's counting and rigidity arguments withstand attack

The checked source is Kruer and Kohlmeyer's *Vertex-critical four-chromatic graphs with no small critical edge set*, printed 10 September 2026, at commit `8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23`. The [local PDF](<./seed-source.pdf>) has SHA-256 `77e311d97357f98fc33db89ddd63ca6fc3fc5c610bf90075cd9dc1077922ecb8`. This pins the audited edition; its printed date alone is not evidence of its public release date. ([Pinned manuscript](https://github.com/JENW1N/complete-math-solutions/blob/8b9db1d8c0ded5398d5e4e4bbdf8f2ec14ce5c23/papers/erdos-944.pdf))

The complete audit covered **every stage of §§2–7**: punctured colorings, height characters, the deficit estimate, winding, recursive CRT parameters, short ratios, periodic rigidity, exact rounding, and witness-word assembly. Two additional reviewers independently began from the source before consulting the first seed audit, dividing the crosscheck between §§2 and 7 and §§3–6. Their interfaces match. The following table records the most plausible attacks and why they fail; the linked notes contain the complete derivations. ([Full seed audit](<seed.md>), [graph and word crosscheck](<seed_core_crosscheck.md>), [algebra crosscheck](<seed_algebra_crosscheck.md>))

| Potential failure | Resolution established in the audits |
|---|---|
| Chord duplication corrupts bad-edge counts | Distinct core direction pairs have disjoint unordered edge sets. Choosing one bad core edge per bad pair is injective, even when chord descriptions coincide. |
| Counting orientations introduces a factor of two | For a fixed nonzero direction $s$, the map $v\mapsto\{v,v+s\}$ is injective unless $2s=0$. The construction explicitly removes that involution. |
| $r$ witness words are insufficient against $r$ bad pairs | A bad target already consumes one bad pair. Its $r$ alternative words avoid that pair and have disjoint pair sets between words, so only $r-1$ other pairs can spoil words. Internal repetition is harmless. |
| The final high-deficit unit is not wholly proper | It need not be. Its selected word supplies valid increments $\pm1$ on proper target edges and $\pm3$ on bad ones. The winding lemma allows these increments. |
| Vertex-criticality is shown only at one vertex | For each deleted $v$, use $i=[v]_q$ and $c_v(u)=[[a_i^{-1}(u-v)]_n]_3$. Same-type chords cannot wrap through the deleted coordinate inside their designated gap; other types have wrap-safe residue 2. |
| CRT incorrectly treats the $a_j=5d_j$ as coprime | All prescriptions agree modulo the shared factor 5. Separating it leaves pairwise coprime moduli $3,q,5,d_1,\ldots,d_{q-1}$; the recursive inverses and growth conditions are compatible. |
| Large character coefficients cancel across coordinates | The CRT coordinates vary independently. Their real phase width is a sum of absolute contributions, forcing at most one active coordinate. All five blocks then fix the remaining frequency. |
| Approximate middle-third membership never becomes exact | Endpoints lie on the exact $1/L$ grid and have error strictly less than $1/L$. A grid point outside the closed middle-third arc cannot be that close. The removed midpoint does not affect the first and last representatives. |

The counting-to-height passage warrants particular care. At most $r$ bad pairs leave a wholly proper unit among the $q=3t+1>r$ selected units, so the proper directions still generate the cyclic group. Pulling their coloring to an integer grid gives increments $\pm1$. Each square sum is even, divisible by three, and has magnitude at most four, hence is zero. The resulting height has a basepoint-independent additive period functional, producing **one common character** $K$. Averaging the selected three-step words gives

\[
\beta_s\ge D_K(s)
=\max\{0,n-3\min([Ks]_n,n-[Ks]_n)\},
\qquad F(K)=\sum_{s\in J}D_K(s)\le r.
\]

Here $\beta_s$ counts distinct bad core edges, and $J$ chooses one orientation per pair. The argument neither assumes translated paths are edge-disjoint nor extends additivity unjustifiably to bad directions. ([Height and deficit crosscheck](<seed_core_crosscheck.md>))

The algebraic bottleneck then forces $Ka_i\equiv\pm(n-1)/3\pmod n$ for some unit, giving deficit exactly one and word-mean magnitude greater than one. Sparsity follows from $\sum_j(d_j-1)|z_j|/(3d_j)\le1/3$, not from assumed small coefficients. In the one-coordinate case, all five blocks are needed; their comparison uses distance to the nearest integer, avoiding a misleading fractional-part estimate. Finite rounding uses an uninterrupted residue progression, a signed integer lift, and $n>1000(r+1)qL^2$ to obtain the strict grid error. The checked bounds are uniform for every $r\ge1$. ([Rigidity and rounding crosscheck](<seed_algebra_crosscheck.md>))

Finally, orient that unit so its mean exceeds one. Its Hamilton cycle partitions into length-$q$ gaps, so some gap has increment sum greater than $q$. Each gap contains the required winding graph with at most $r\le t$ bad edges, contradicting its bound $q=3t+1$. Extra edges do not matter because an induced copy is unnecessary. This rules out every three-color assignment with at most $r$ monochromatic edges; together with the punctured colorings it proves the exact seed theorem. ([Criterion and final assembly](<seed_core_crosscheck.md>))

## Exact checks supplement the proof without certifying it

The transfer checks verified all **20 Grötzsch** edge-deletion certificates, all **12 $M(C_3)$** certificates for the optional refinement, and the arithmetic identities and semigroup bounds for $4\le g\le128$. The seed checker verified the $r=1,2$ parameter arithmetic, **48 three-step words across 31 targets**, and **61,320 normalized winding-graph colorings** for $t=0,1,2,3$. These exact computations catch transcription and small-case errors; the universal claims rest on the arguments above. ([Transfer checker](<transfer_check.py>), [seed checker](<seed_checks.py>), [saved results](<seed-check-results.json>))

No independent Lean build, kernel replay, or exhaustive seed-graph coloring search was performed. The checked $r=1$ seed already has a **78-digit order**. Author-hosted verification logs remain attributed evidence, not executions reproduced here. The earlier report's novelty and source-search language is now outdated; its limited seed-audit scope has also been superseded. The [earlier report](<../transfer-investigation/REPORT.md>) and original draft were left unchanged. ([Audit limits](<seed.md>))

## Conclusion

The defensible output is an independently audited exposition of a prior all-orders construction, with smaller sufficient thresholds whose priority remains open. Any future presentation of the draft should acknowledge the October bridge and remove language suggesting this investigation first closes the all-orders gap. A claim of a new contribution would require a separately established quantitative distinction and its own priority assessment.

This audit does **not** fulfill the broader objective of solving another unsolved catalog target; that objective remains active. What it supplies is a corrected attribution record and a substantially stronger mathematical basis for trusting the seed-dependent implication. No fatal defect was found, while formal replay and exhaustive novelty certification remain unchecked.
