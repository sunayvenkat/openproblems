# Erdős 168(ii): separated boundary cocycles and exact dyadic-column reduction

**Status: no irrationality proof or bounded-term S-unit compression has been obtained.** This round gives a new exact separation of all smooth-cutoff color counts into two one-dimensional boundary sequences. Conditional on the cover formula (C), it gives an explicit cone coding for every sufficiently high dyadic column and an exact base-8 resummation. It also identifies precisely what an exact finite resummation of an entire column would require: eventual periodicity of its binary birth word. That periodicity has not been proved or disproved.

Only this folder was written. The previous dense-event counterexamples were not repeated as a new research result.

## Can the two-dimensional color state be separated exactly?

### Takeaway

Yes. At d=2^a3^b, after rotating by the color of d, the color discrepancy is the sum of its two axis discrepancies plus a correction depending only on a,b modulo3. This is an exact identity for every a,b≥0, independent of (C).

### Cited Findings

- W(t)=Σ_{2^i3^j≤t}ω^(i+2j), with ω³=1 and ω≠1, records the three color counts. The earlier work established horizontal and vertical strip recurrences but did not state the separated smooth-cutoff identity below. — [Earlier arithmetic notes](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md)
- Direct color enumeration checks the new identity at all120 saved smooth prefixes. The associated cone rule is checked against54 certified finite optima with b≥4. — [Verifier](arithmetic_check.mjs), [results](arithmetic_check.json)

### Inferences

Define

\[
A_a=\omega^{-a}W(2^a),\qquad
B_b=\omega^{-2b}W(3^b),\qquad
Z_{a,b}=\omega^{-a-2b}W(2^a3^b).
\]

Then

\[
\boxed{Z_{a,b}=A_a+B_b-1+C_{a\bmod3,b\bmod3},}
\tag{1}
\]

where rows and columns of C are indexed0,1,2:

\[
C=\begin{pmatrix}
0&0&0\\
0&1&-\omega^2\\
0&-\omega&1
\end{pmatrix}.
\tag{2}
\]

In particular, the correction vanishes whenever a or b is divisible by3.

**Proof.** Partition the exponent triangle at2^a3^b into the rectangle0≤i≤a,0≤j≤b, the arm i>a, and the arm j>b. Both i>a and j>b cannot occur. After multiplying all weights by ω^(−a−2b), the rectangle contributes

\[
P_aQ_b,\qquad
P_a=\sum_{l=0}^a\omega^{-l},\quad Q_b=\sum_{k=0}^b\omega^{-2k}.
\]

For the arm j>b write i=a−l,j=b+y. Its condition is3^y≤2^l, so its contribution depends only on a. The arm i>a similarly depends only on b. Write these contributions U_a and V_b. Then

\[
Z_{a,b}=P_aQ_b+U_a+V_b,
\quad A_a=P_a+U_a,\quad B_b=Q_b+V_b.
\]

Thus Z=A+B−1+(P_a−1)(Q_b−1). The possible values of P−1 are0,ω²,−1; those of Q−1 are0,ω,−1. Their products give (2).

### Gaps

Additive separation of W does not commute with the minimum in (C). The next section makes that remaining nonlinearity explicit rather than discarding it.

## What is the exact birth word in a complete dyadic column?

### Takeaway

Conditional on (C), the birth digit at2^a3^b is membership of A_a in a translated lattice cone, with a finite residue correction. The patch vector, in the same rotating coordinates, is independent of a.

### Cited Findings

- (C) asserts τ(t)=min_j(K_j(t)−e_j(t)); its optimality is not yet proved. The isolated and patch boundary locations have three-exponents0,1, or3. — [Candidate and patch definitions](../../early-attacks/open-conjecture-transfer-search/168_irrationality.md), [finite grid note](../../early-attacks/open-conjecture-transfer-search/168_grid.md)
- The tests use previously certified τ-values, not candidate-generated optima. — [Exact finite dataset](../../early-attacks/open-conjecture-transfer-search/168_exact_diagonal_results.json), [new checks](arithmetic_check.json)

### Inferences

Let η_(a,b)=Δτ(2^a3^b)∈{0,1}; equivalently a_(a,b)=3ΔF(2^a3^b)−2=1−3η_(a,b). Fix b≥4, so no isolated/patch indicator changes at the smooth point d=2^a3^b.

Put m_b=⌊log₂(3^b)⌋ and n_b=⌊log₂(3^b/6)⌋. Define a vector ε_b∈{0,1}³ as follows, with indices reduced modulo3:

- Set its entry m_b−2b to1 if3·2^(m_b)>2·3^b (the isolated vertex).
- Set its entry n_b−2b to1 if6·2^(n_b)≤3^b<(27/4)·2^(n_b) (the patch).
- All other entries are0.

The two conditions do not overlap. Because b≥4, all powers used in the patch have valid nonnegative exponents for every a≥0. At d, the actual indicator e_j(d), after rotating the inserted color a+2b to color0, is exactly ε_b. The factor2^a cancels in both inequalities and in both color differences.

Write

\[
Z_{a,b}=x+y\omega
\]

with integer x,y. In terms of the rotated color counts, x=K₀−K₂ and y=K₁−K₂. Under (C), insertion raises τ precisely when its color0 is a minimum of the adjusted counts **after** insertion. Therefore

\[
\boxed{\eta_{a,b}=1
\iff x\le\varepsilon_{b,0}-\varepsilon_{b,2}
\ \text{and}\ 
x-y\le\varepsilon_{b,0}-\varepsilon_{b,1}.}
\tag{3}
\]

Ties are included: if the new count equals another minimum, its previous count was one smaller, so τ increases by one. If it exceeds another minimum, τ does not increase.

Combining (1) and (3) gives the exact cone test on A_a. Define

\[
\mathcal C_b=\{x+y\omega\in\mathbb Z[\omega]:
x\le\varepsilon_{b,0}-\varepsilon_{b,2},\ 
x-y\le\varepsilon_{b,0}-\varepsilon_{b,1}\}.
\]

Then, conditional on (C),

\[
\eta_{a,b}=1_{\mathcal C_b}
\left(A_a+B_b-1+C_{a\bmod3,b\bmod3}\right).
\tag{4}
\]

This reduction is valid for entire columns, not merely at selected return endpoints. The four columns b=0,1,2,3 can be retained separately; b=2 can also be treated by the cone rule with the small-domain conventions checked explicitly.

### Gaps

- Formula(4) is conditional on the missing global optimality assertion(C). The direct count separation(1) is unconditional.
- The integer state A_a is unbounded. Equation(4) does not turn it into a fixed step function of the rotation phase alone.

## Does complete-column resummation now give finite S-unit forms?

### Takeaway

It gives an exact base-8 series for a concrete planar cocycle, but not finitely many endpoint terms. Exact finite rational evaluation of a whole column is equivalent to eventual periodicity of its binary birth word. Local carries do not by themselves prove that property.

### Cited Findings

- KK obtains two geometric series whose coefficients are fixed step functions of a circle rotation; return differences then have finitely many spaced event families. Its fixed-dimensional arithmetic theorem is not a theorem about arbitrary cone codings of unbounded planar cocycles. — [KK, §§5–7](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf), [saved source](../Erdos%20theorem%20transfer%20investigation/erdos1062-fork-free-density.pdf.txt)
- The earlier exact return identity already supplies an exponential height bound, but not the bounded number of terms, extra exponential tail saving, or nonvanishing needed for that theorem. — [Prior weighted-return proof](../../early-attacks/open-proof-gap-attacks/weighted.md)

### Inferences

**An explicit fixed step-function increment.** Put α=log₃2, and define the3-periodic function

\[
S(m)=\sum_{j=0}^m\omega^{2j},
\qquad S(m)=\begin{cases}1&m\equiv0\pmod3,\\-\omega&m\equiv1\pmod3,\\0&m\equiv2\pmod3.\end{cases}
\]

The axis strip recurrence gives

\[
A_{a+1}-A_a=\omega^{-(a+1)}S(\lfloor(a+1)\alpha\rfloor).
\tag{5}
\]

Set x_n={nα}, Y_n=A_(3n), and

\[
\Psi_r(x)=\sum_{s=1}^r\omega^{-s}S(\lfloor3x+s\alpha\rfloor)
\quad(0\le r\le3),\qquad\Phi=\Psi_3.
\]

Then the exact evolution is

\[
Y_0=1,\qquad x_{n+1}=\{x_n+\alpha\},\qquad
Y_{n+1}=Y_n+\Phi(x_n),\qquad
A_{3n+r}=Y_n+\Psi_r(x_n).
\tag{6}
\]

The cocycle Φ has nine breakpoints. Since1/2<α<2/3, they are ordered as

\[
\frac{2-3\alpha}3,
\frac{1-\alpha}3,
\frac{2-2\alpha}3,
1-\alpha,
\frac{2-\alpha}3,
\frac{3-2\alpha}3,
\frac{4-3\alpha}3,
\frac{3-\alpha}3,
\frac{4-2\alpha}3.
\]

Starting at0, its values on the ten resulting intervals are

\[
-\omega,\ 0,\ \omega,\ -1,\ 0,\ 1,\ -\omega^2,\ 0,\ \omega^2,\ -\omega.
\tag{7}
\]

Each of the six nonzero directions has total interval length(1−α)/3. Thus Φ has mean zero. It also satisfies Φ(x+1/3)=ω²Φ(x). These properties are exact, but do not prove recurrence of the planar state at a specified value, periodicity of a cone coding, or any arithmetic conclusion about its weighted sum.

**The complete column.** Define

\[
R_b=\sum_{a\ge0}\frac{a_{a,b}}{2^a}.
\]

Unconditionally,

\[
\boxed{R_b=2-3\sum_{a\ge0}\frac{\eta_{a,b}}{2^a}.}
\tag{8}
\]

Conditional on(C), for b≥4 equations(4) and(6) yield

\[
R_b=2-3\sum_{r=0}^2 2^{-r}
\sum_{n\ge0}8^{-n}
1_{\mathcal C_b}\left(
Y_n+\Psi_r(x_n)+B_b-1+C_{r,b\bmod3}
\right).
\tag{9}
\]

This is a finite number of well-defined base-8 series per column. It is not a finite number of S-unit terms. The total density remains

\[
9c-6=\sum_{b\ge0}3^{-b}R_b.
\tag{10}
\]

**Exact criterion for a finite full-column evaluation.** For every fixed b, without assuming(C),

\[
R_b\in\mathbb Q
\quad\Longleftrightarrow\quad
(\eta_{a,b})_{a\ge0}\text{ is eventually periodic}.
\tag{11}
\]

Indeed(8) is an ordinary binary expansion with digits0 and1, apart from its integral a=0 digit and a rational affine transformation. Rational binary expansions are exactly the eventually periodic ones; the terminating/all-ones ambiguity also consists of eventually periodic words.

Therefore an exact evaluation of an entire infinite column as finitely many rational multiples of S-units would require eventual periodicity of that column. If one first proved that its cone coding is not eventually periodic, that would instead rule out such a full-column rational evaluation. Neither assertion is currently established. Even rational evaluation of every individual column would leave the infinite outer sum(10) and the need for a uniform finite-coefficient return structure.

**Where a further return theorem would have to act.** In the separated representation, a bounded horizontal return changes Z by an integer vector δ. The cone digit can change only when one of the two integer linear forms x or x−y crosses its corresponding threshold in(3). Thus the unresolved events are intersections of level strips of the two one-dimensional boundary cocycles A and B. A useful new theorem must control their *weighted crossings*, uniformly in both indices, rather than just return the total color counts at selected real cutoffs.

The concrete next obligation is consequently to establish a return or resummation theorem for the cone-coded skew product(6)–(9) that survives the outer sum(10), with a fixed number of rational-coefficient S-unit terms, an additional exponential saving, and nonvanishing. The known fixed step-function theorems cannot be invoked merely because the **increment** Φ is a step function: the output in(9) also depends on its accumulated state Y_n.

### Gaps

- No eventual periodicity or nonperiodicity theorem for the relevant column birth words was proved.
- No fixed-dimensional compression, exponentially improved remainder, or nonvanishing argument was obtained. The nine-breakpoint cocycle is a structural reduction, not a solved arithmetic gap.
- No new decimal expansion, broad literature search, external submission, dependency installation, or Lean work was performed. The open target remains unresolved.
