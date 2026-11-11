# Arithmetic transfers to live open conjectures

The detailed and most current #168 arithmetic checkpoint, including Elsner's congruence-restricted approximation theorem and the proved long balanced-return segment, is [168_irrationality.md](./168_irrationality.md). The two main obligations remain exact optimality and irrationality.

## Which different entries are genuinely open, and what do they ask?

### Takeaway

The strongest direct structural transfer found is from Kohlmeyer–Kruer's #1062 to #168(ii), the irrationality of the maximum density of sets avoiding {n,2n,3n}. No complete proof of a different open entry has been established in this investigation. The candidate exact formula for #168 below has substantial computational support, but two mathematical gaps remain.

### Cited Findings

- **#304 is closed.** The individual entry was withdrawn on 6 October 2026 as solved elsewhere, citing an OpenAI corpus proof. An older open catalog/search result is not reliable status evidence. [Individual entry](https://conjectures.io/problems/erdos304-upper-bound).
- **#13 general remains open.** For each integer r≥0, the question is whether there is C_r such that every A⊆[1,N] satisfying a∤(b_1+⋯+b_r) whenever a,b_i∈A and every b_i>a has |A|≤N/(r+1)+C_r. Repeated b_i are allowed. No sufficiently-large qualification weakens the inner universal N beyond the additive constant. [Live entry](https://conjectures.io/problems/erdos13-erdos-13-variants-general), [definition](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/13.lean).
- **#49 primes maximal remains open.** For every N≥2, is the maximum length of a strictly increasing totient subsequence φ(a_1)<⋯<φ(a_k), with 1≤a_1<⋯<a_k≤N, exactly π(N)? The word strictly matters. [Live entry](https://conjectures.io/problems/erdos49-erdos-49-variants-primes-maximal), [definition](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/49.lean).
- **#168(ii) remains open.** If F(N) is the largest size of a subset of [1,N] containing no {n,2n,3n}, is lim F(N)/N irrational? Existence is already known. [Live entry](https://conjectures.io/problems/erdos168-erdos-168-parts-ii), [definition](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/168.lean).
- **#1060(ii) is a polylogarithmic fiber bound**, not merely n^{o(1)}: #{k≤n:kσ(k)=n}=O((log n)^C) for some C. The trivial divisor bound does not settle it. [Live entry](https://conjectures.io/problems/erdos1060-erdos-1060-parts-ii).

### Inferences

- For #49, if a composite n has no prime in (φ(n),n], all primes≤n followed by n form a strictly increasing totient subsequence of length π(n)+1. Thus the conjecture implies, in particular, a prime in [p²−p+1,p²] for each prime p. This is a substantial barrier to proving the exact statement via the present divisor-density inputs.
- For #13, the top interval (rN/(r+1),N] gives the conjectured leading density. Simple residue-class lower intervals did not improve it. A finite set with a small excess would not disprove an O_r(1) assertion without a scalable construction.

### Gaps

- No proof or counterexample for #13, #49, #168(ii), or #1060(ii) was completed.
- No Lean formalization or replay was attempted, as requested.

## What exactly transfers from the #1062 irrationality proof?

### Takeaway

The reusable arithmetic statement is a fixed-dimension S-unit lower bound. Its dimension and coefficient vector must be fixed along the infinite sequence of approximations. A generic sum over all 3-smooth denominators does not meet this hypothesis.

### Cited Findings

- Proposition 7.4 states: for fixed m≥1, d∈Q^m and ε>0, there is C>0 such that, for every integer N, positive {2,3}-units u_i, and 0<t≤min(1,u_1,…,u_m), the nonzero quantity E=Σd_i u_i−N satisfies |E|≥Ct H(N:u_1:⋯:u_m)^{−ε}. A corresponding pure-form statement holds. It is deduced from the p-adic Subspace Theorem by induction over exceptional linear subspaces. [Primary manuscript, §7](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf).
- The #1062 proof produces, under rationality, a fixed m≤404 and fixed rational coefficients along an infinite subsequence, with u_i≥e^{−T}, height≤e^{27L}, and 0<|E|≤e^{−T−L/200}. Choosing ε=1/10800 gives the contradiction. Its essential inputs are finitely many jumps of two rotation-coded step functions, widely separated return events, and a two-cutoff noncancellation argument using 2-adic valuations. [Primary manuscript, §§6–7](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf).

### Inferences

- A valid transfer to #168 would need a replacement for the finite-event return identity, followed by a nonzero truncation argument. Merely recognizing the same primes 2 and 3 does not supply these.
- Boundedly many boundary *exchange templates* would not by itself imply boundedly many values of the color-count discrepancies. The latter are actually unbounded, as proved below.

### Gaps

- No fixed-dimension, fixed-coefficient small-linear-form construction has been obtained for #168.
- The Subspace Theorem black box is standard mathematics; the authors' independent Lean implementation was not audited here.

## What has been established about #168's finite problem?

### Takeaway

The finite problem has a plausible exact formula: choose the cheapest of the three residue color classes, remove an isolated power of 2 when present, and allow one specific 3-to-2 exchange near the bottom boundary. This formula survives extensive published-data and computational checks. Its optimality is unproved.

### Cited Findings

- Write D_t={(a,b)∈Z_{≥0}²:2^a3^b≤t}. The forbidden triples are {(a,b),(a+1,b),(a,b+1)}. If d_k are the increasing 3-smooth numbers and f(k) is the largest admissible subset of the first k, the density is (1/3)Σ_k(f(k)−f(k−1))/d_k. Graham–Spencer–Witsenhausen supplied the classical reduction; Veselinov gives a modern proof and related estimates. [Veselinov, §§3–6](https://arxiv.org/html/2604.15515v1).
- The known decimal starts 0.80096575500655898909042032638808241. [OEIS A386439](https://oeis.org/A386439).
- Veselinov proves f(k)=2k/3+O(√k), that every pure power of 2 insertion increases f by one, and that every other insertion creates exactly one new forbidden triple. He also records that rational reciprocal sums over smooth denominators can have nonperiodic binary coefficients. None of these facts proves irrationality. [Veselinov](https://arxiv.org/html/2604.15515v1).

### Inferences

Let K_j(t)=#{(a,b)∈D_t:a+2b≡j mod3}, j=0,1,2. Every forbidden triple has exactly one vertex of each color, so each color class is a cover.

For t≥3, the only possible isolated vertex is a pure power s=2^a with 2t/3<s≤t; there is at most one. Delete it from its color cover when it occurs.

A second valid exchange is as follows. If s=2^a and 12s≤t<27s/2, begin with color j≡a+1 mod3, remove {2s,9s,12s}, and add {3s,4s}. Every formerly covered triple remains covered. The potentially uncovered triangle anchored at 9s/2 is absent because 27s/2>t; the other constraints are checked directly. This saves one cover vertex. Equivalently, for x=2^{a+1}, the interval is 6x≤t<27x/4 and the improved class is j≡log_2 x mod3.

Define e_j(t)=1 if either of these corrections applies to class j, and zero otherwise. Their t-ranges are disjoint. The candidate is

    τ(D_t) = min_j (K_j(t)−e_j(t)),
    f(k) = k−τ(D_{d_k}).

For t<3 the optimum is simply all available points. The displayed formula supplies a rigorous *upper bound on cover size*, hence a lower bound on f; equality is the missing combinatorial theorem.

Useful negative checks:

- Descending greedy g(v)=1−g(2v)g(3v) first loses at t=162: it selects16 of24 vertices, whereas the complement of {2,9,12,16,54,72,96} selects17. This is an exact witness, independent of solver upper bounds.
- Unmodified color classes also first lose at162 because their counts include isolated128.
- Removing only isolated vertices still loses at t=1536: all color classes have15 active vertices, while {3,4,18,24,32,81,108,144,192,384,486,512,648,864} is a14-vertex cover. This is precisely the 3-to-2 patch at s=128.
- Swapping the axes does not mirror that patch. The reflected removal of4s for s=3^b leaves {4s/3,8s/3,4s} uncovered when b≥1; that entire triangle lies below the removed point, so the upper cutoff cannot eliminate it.

Computational records:

- Sampled finite MILPs at k=3,10,20,30,40,50,70,100,150,200,300,500 gave f=2,7,14,21,27,34,48,67,101,134,201,334. Rounded witnesses were checked by exact integer membership. Solver optimality bounds are conventional floating-point evidence. [Sample output](./check_168_arithmetic_samples.json).
- The graph agent separately matched the patched formula against all1,449 fetched published OEIS first-hit records, spanning through k=5000, f=3335. This evidence and the graph agent's additional MILPs are recorded in its companion notes, not independently replayed here.
- Exact ordering through t≤10^100 contains35,084 smooth numbers. Every candidate f-increment is0 or1. Exact rational summation gives candidate density

    0.80096575500655898909042032638808241322472498911028458781919045603644708044249630021895087751711466454827914033…

  The complete reciprocal tail beyond10^100, divided by3, is <1.015×10^{−98}. These additional digits are conditional on the formula, not a proved evaluation of the actual density. [Computation](./check_168_color_discrepancy.py).
- An independent local-exchange search fixes a color outside a strip along the sloped boundary and optimizes inside it. At height40 and multiplicative width32, all42 exact cutoff configurations and all three colors have no improvement beyond the two known corrections. This search checks all witnesses exactly but uses floating-point MILP bounds. [Computation](./check_168_boundary_exchange.py).

### Gaps

- No combinatorial proof of the patched-color lower bound on cover size.
- Agreement with published data and tiny tail bounds cannot prove the exact infinite formula.
- Even a proof of this formula would leave irrationality unresolved; its minimum of three counting functions is not automatically the finite-step rotation coding used in #1062.

## Can the color-count discrepancy be encoded by finitely many bounded states?

### Takeaway

No: the color spread is unbounded. Consequently f(k)−2k/3 is unbounded as well. This is a rigorous obstruction to the tempting bounded-error simplification, although it does not contradict the patched-color formula.

### Cited Findings

- Kesten's theorem says that for irrational rotation θ, an interval has bounded discrepancy exactly when its length belongs to Zθ+Z. Kelly and Sadun give a primary alternative proof. [Theorem1](https://arxiv.org/html/1404.0455), [Kesten's original article](https://geodesic.mathdoc.fr/articles/10.4064/aa-12-2-193-212/).
- The exact numerical scan finds spread1 at t=1, spread2 first at8, spread3 first at34992, and spread4 first at2^199·3^7 (k=14096), with counts (4701,4697,4698). The largest spread up to10^100 is4. [Exact integer computation](./check_168_color_discrepancy.py), [record values](./check_168_color_discrepancy.json).

### Inferences

Here is a proof of unboundedness, derived in this investigation; no novelty claim is made.

Put β=log_2 3, ω=e^{2πi/3}, t=2^{3m}, and B=⌊3m/β⌋. Summing the geometric series on each horizontal row gives

    (1−ω) Σ_{j=0}² K_j(t)ω^j
      = Σ_{b=0}^B ω^{−b} − ω Σ_{b=0}^B ω^{−⌈(β+1)b⌉}.

Indeed row b runs from a=0 through a=3m−⌈βb⌉, including b=0. The first sum is uniformly bounded.

Let θ=(β+1)/3, which is irrational. For b≥1, the second sum's term is respectively ω², ω, or1 as {bθ} lies in the first, second, or third third of the unit interval. Therefore, if those sums were bounded, the count in the last third minus B/3 would be bounded: its value is 2/3 times the real part of the sum, up to the harmless initial b=0 term. This violates Kesten, since1/3∉Zθ+Z.

The indices B=⌊3m/β⌋ have successive gaps at most2 because1<3/β<2. Thus boundedness along these indices would imply boundedness at every integer index. The contradiction therefore applies on the displayed t=2^{3m} subsequence.

It follows that Σ_jK_j(t)ω^j is unbounded, hence the spread max K_j−min K_j is unbounded. Since Σ_j(K_j−|D_t|/3)=0, the negative deviation |D_t|/3−min K_j is unbounded. Removing the smallest color gives

    f(|D_t|)−2|D_t|/3 ≥ |D_t|/3−min_j K_j(t),

which proves the asserted unboundedness of the extremal error.

### Gaps

- This rules out a bounded color-difference state space. It does not rule out a more elaborate rotation-cocycle description or an alternative S-unit proof.
- No claim that this auxiliary unboundedness result resolves an independently listed catalog target.

## What did the other arithmetic screening establish?

### Takeaway

The searches eliminated easy counterexample routes and clarified barriers, but supplied no other closure.

### Cited Findings

- Kohlmeyer–Kruer's local factorial theorem represents each R by poly(log log R) distinct divisors of a factorial with index O((log R)^{1+η}). It does not directly provide divisors with arbitrary prescribed denominators or the fixed-polylogarithmic bound of18(c). [Primary theorem](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos18b-factorial-divisors.pdf).
- #317 claim2 asks eventual strict inequality |Σ_{k≤n}δ_k/k|>1/lcm[1,n] for every nonzero signed sum, δ_k∈{−1,0,1}. [Live entry](https://conjectures.io/problems/erdos317-erdos-317-variants-claim2).

### Inferences

- The exact totient sieve and strict-LIS screen found f(N)=π(N) for every2≤N≤50,000,000. At the endpoint both are3,001,134. No counterexample was found. [Script](../../../../meta/open-conjecture-survey/check_49.mjs).
- For a #317 equality and a prime p∈(n/2,n], reducing after multiplication by L=lcm[1,n] modulo p requires L/p≡±1 modp. Only denominator p contributes nontrivially. Proving that some p always fails this condition for large n is an unresolved step; the factorial-divisor theorem does not remove it.

### Gaps

- The #49 large sweep has not been independently checked against a separate O(N²) small-prefix dynamic program; it is screening evidence only.
- The deep zero-free assertions in the authors' #1057 work were not used as an unaudited black box.
