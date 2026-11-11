# Advance the open density irrationality attack

**The requested goal remains unmet and active.** This investigation has not solved a different currently unsolved conjectures.io entry. Its strongest remaining target is **Erdős #168(ii), irrationality of an extremal density**, using Kohlmeyer–Kruer's #1062 work. Two obligations remain: prove the proposed finite formula's sharp lower bound, and construct a nonzero approximation to its reciprocal-weighted density tails using a fixed number of S-units with the required error and height bounds. A corrected finite formula has substantial computational support, and several useful auxiliary lemmas are proved below. Neither an extension of already solved #944 nor an auxiliary construction counts as the requested breakthrough.

## The eligible target requires irrationality

Let $F(N)$ be the largest cardinality of $A\subseteq\{1,\ldots,N\}$ containing no complete triple $\{n,2n,3n\}$. Existence of

\[
c=\lim_{N\to\infty}\frac{F(N)}N
\]

is known; #168(ii) asks whether $c$ is irrational. Its recorded decimal begins $0.80096575500655898909042032638808241$. Computing more digits does not answer that question. ([Live target](https://conjectures.io/problems/erdos168-erdos-168-parts-ii), [OEIS A386439](https://oeis.org/A386439))

The 6 November 2026 catalog snapshot contains 307 entries: 271 with no closure status, one in review, 32 solved, two solved with documentation pending, and one formalization defect. This gives 272 open/in-review candidates, without independently certifying their literature status. Already solved #944 and withdrawn Green entries are excluded. The two-prime case of #269 is already known; its unresolved higher-dimensional extension did not yield a transfer. ([Catalog](https://conjectures.io/problems), [#269 research record](<../../../../meta/open-conjecture-survey/269_irrationality.md>))

Kohlmeyer–Kruer's #1062 forbids the stronger configuration in which one selected integer divides two distinct selected integers. Their Proposition 7.4 supplies the potentially reusable interface: with the number of terms and rational coefficients fixed, a nonzero linear form in positive $\{2,3\}$-units cannot be too small relative to its height and smallest unit. Their application obtains boundedly many terms, exponentially accurate return cancellation, and nonvanishing. Those problem-specific inputs must be proved anew for #168; smooth denominators alone do not satisfy them. ([Primary #1062 manuscript, §§6–7](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf))

## A valid boundary patch suggests the formula

Write each positive integer uniquely as $m2^a3^b$, with $(m,6)=1$. Within one component, put

\[
D_t=\{(a,b)\in\mathbf Z_{\ge0}^2:2^a3^b\le t\}.
\]

Let $\tau(t)$ be the minimum number of vertices meeting every corner $\{(a,b),(a+1,b),(a,b+1)\}$ in $D_t$. The maximum admissible component size is $\alpha(t)=|D_t|-\tau(t)$. Each corner contains exactly one vertex of each color $a+2b\pmod3$; write $C_j(t)$ for color class $j$ and $K_j(t)=|C_j(t)|$. The component reduction and coloring are established background. ([Veselinov, §§3–6](https://arxiv.org/html/2604.15515v1))

For $t\ge3$, define $I_j(t)=1$ when a pure power of two $z$ of color $j$ satisfies $2t/3<z\le t$, and zero otherwise. Such a vertex is isolated: its possible parent corner requires $3z/2\le t$, while it has no parent obtained by dividing by three. Every vertex divisible by three belongs to its parent corner, so there is no other isolate. There is at most one such power of two.

Define $P_j(t)=1$ when $s=2^a$, $a\ge0$, satisfies $12s\le t<27s/2$ and $j\equiv a+1\pmod3$, and zero otherwise. In that class replace

\[
\{2s,9s,12s\}\quad\text{by}\quad\{3s,4s\}.
\]

This saves one vertex. Indeed, the existing corners affected by removing those three vertices are precisely

\[
\{s,2s,3s\},\quad\{2s,4s,6s\},\quad
\{3s,6s,9s\},\quad\{4s,8s,12s\}.
\]

Each contains $3s$ or $4s$. The additional possible corner $\{9s/2,9s,27s/2\}$ is absent because of the strict upper endpoint; other possible corners have larger maxima. The pure-power condition excludes a three-parent for $2s$. Thus the rigorous construction gives

\[
\tau(t)\le\min_{j=0,1,2}\bigl(K_j(t)-I_j(t)-P_j(t)\bigr).
\tag{1}
\]

**Candidate (C) asserts equality in (1) for every $t\ge3$; that assertion is unproved.** The cases $t<3$ have no corners. ([Construction and exact checks](<168_grid.md>))

At $t=1536$, all three raw classes have size 15, but the patch replaces $\{256,1152,1536\}$ by $\{384,512\}$, giving size 14. A rational dual certificate of total weight $53/4$, with incident weight at most one at every vertex, proves $\tau(1536)\ge14$. This refutes the older printed conjecture that only the isolated-point correction is needed. Modern tables already record the optimum; priority for this counterexample or repaired formula has not been established. ([Certificate](<168_1536_simple_dual.json>), [Chung–Erdős–Graham, pp. 8–9](https://www.math.ucsd.edu/~ronspubs/02_04_linear_forms.pdf))

## Extensive checks support equality without proving it

An exhaustive integer dynamic program verifies (C) for **all first 120 smooth prefixes**, through $t=294912$. Its diagonal-mask recurrence includes every cover; its state width grows with $\log t$, so it provides no uniform finite-state theorem. Separately, SciPy/HiGHS agrees at every nontrivial prefix through $10^{12}$: 532 records, ending at 534 vertices. Returned witnesses were checked exactly, but larger-instance optimality is numerical solver evidence. ([Computational provenance](<168_grid.md>))

The candidate also agrees with all 5000 prefixes reconstructed from the full 3335 published first-hit records. Sean Eberhard's September 2025 program uses unrestricted Gurobi optimization, not the color construction; this is independent numerical support, not an exact certificate. ([OEIS A004059](https://oeis.org/A004059), [Published program](https://oeis.org/A004059/a004059.py.txt))

Exact bipartite matching checks agree with (C) at sampled sizes from 5000 through 1,000,000 vertices, but optimize only covers restricted to two colors. They do not exclude better three-color covers. Unrestricted exact checks also cover 4424 rational linear-triangle shapes of width and height at most 25, with slope between one and two. Broader normalizations are false: a 155-vertex Ferrers shape with successive row drops one or two has unrestricted optimum 50 while every two-color optimum is 51. The actual multiplicative boundary geometry matters. ([Adversarial checks and counterexamples](<168_cover_review.md>))

## Rigidity and matching isolate the missing lower bound

A lemma derived here concerns **exact covers: every corner is hit exactly once**. Write $x(v)=1_C(v)$. The six exact-hit corners rooted at $v,2v,3v,4v,6v,9v$ force $x(v)=x(6v)$. If $x(v)=1$ but $x(6v)=0$, the first parent equations force $x(4v)=x(9v)=1$, then $x(12v)=x(18v)=0$, contradicting the corner at $6v$. Conversely, $x(6v)=1$ forces $x(2v)=x(3v)=0$, hence $x(v)=1$.

All six corners exist when $27v\le t$. Further exact corner equations give $x(v)=x(8v)$ when $54v\le t$, and $x(v)=x(27v)$ when $81v\le t$. For $t\ge162$, the nine exponent residues modulo three are determined by $x(1),x(2),x(3)$. Reducing exponents by factors eight and 27 therefore forces one global color phase throughout $v\le4t/27$. Only the band $(4t/27,t]$ can differ; its multiplicative width $27/4<8$ allows at most three vertices per horizontal row. **This does not normalize arbitrary minimum covers**, since the patch can overcover a corner. No priority claim is made for this lemma. ([Proof details](<168_cover_review.md>))

There is also an exact reduction including all three-color competitors. Fix $C_j$ and $U\subseteq C_j$. Form a bipartite graph $B(U)$ by joining the other two vertices of every corner whose $j$-vertex lies in $U$. Bipartite vertex-cover duality gives

\[
\tau(t)=K_j(t)-\max_{U\subseteq C_j}\bigl(|U|-\nu(B(U))\bigr).
\tag{2}
\]

The north-parent edges $\{u/3,2u/3\}$ for $3\mid u$ form a matching, so deficiencies require pure-two-power labels. The patch produces the path $s-3s-6s-4s-8s$, whose matching size is two for three removed labels. An actionable next lemma is: for a class $j$ minimizing (1), prove

\[
\nu(B(U))\ge |U|-I_j(t)-P_j(t)
\quad\text{for every }U\subseteq C_j.
\tag{3}
\]

This would prove (C). Contracted alternating arcs strictly decrease in numerical value, but acyclicity does not prevent several axis roots sharing a bottleneck. Classifying that deficiency remains open. ([Matching reduction](<168_grid.md>))

## Long balanced returns still leave weighted tails

For increasing smooth numbers $d_k$, $f(k)=\alpha(d_k)$, and $f(0)=0$, the known density identity is

\[
c=\frac13\sum_{k\ge1}\frac{f(k)-f(k-1)}{d_k}.
\tag{4}
\]

Set $\omega=e^{2\pi i/3}$ and $W(T)=\sum_j\omega^jK_j(e^T)$. Elsner's restricted rational approximation theorem, applied to the rotation slope $(1+\log2/\log3)/3$, yields infinitely many $Q=3n$ and phases $T_0$ for which

\[
W(T_0+k\log6+Q\log2)=W(T_0+k\log6),
\qquad 0\le k\le M,
\]

where $M=\lfloor(0.08/2.76)n\rfloor$. The proof groups rotation points into triples visiting all three thirds, then excludes the small exceptional sets where successive block sums change. Thus these are rigorously long balanced returns, not merely a numerical observation. Conditional on (C), the boundary corrections also repeat, giving the same identities for $g(t)=\alpha(t)-2|D_t|/3$. ([Elsner, Proposition 2.1](https://www.fq.math.ca/Scanned/38-1/elsner.pdf), [Return proof](<168_irrationality.md>))

**Two obligations remain:** prove the sharp optimality lower bound, such as (3), and derive a nonzero, exponentially accurate approximation to the reciprocal-weighted tail in (4) using a fixed number of S-units with controlled coefficients and height. Equal counts at discrete endpoints do not equate the weighted sums between them: many mixed smooth numbers intervene with different reciprocal weights. The color discrepancies are also unbounded, ruling out an assumed bounded-state shortcut. The next work should attack the deficiency inequality and this weighted-tail identity directly. Until both are established, #168(ii) remains unsolved and the user's goal remains active.
