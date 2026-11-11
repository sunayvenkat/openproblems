# Number theory candidate selection

## Which listed open statements offer a finite route?

### Takeaway
The number theory catalog offers several clean finite-counterexample targets, but none has an evident short route. I would not rank these above a tractable low-dimensional matrix inequality. Relative shortlist: 287, 677, 699, 647.

### Cited Findings
- **Erdos 287.** If distinct integers 1 < n_1 < ... < n_k satisfy sum_i 1/n_i = 1, must some consecutive gap be at least 3? Live catalog on 6 November 2026 says nobody has attempted the full statement; upstream still labels it research open. [Catalog](https://conjectures.io/problems/erdos287-erdos-287), [current source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/287.lean).
- A gap of at least 2 is known. The representation 1/2+1/3+1/6 shows 3 would be sharp. The source records a conditional reduction to primes p in [N,2N] with (p+1)/2 prime. [Current source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/287.lean).
- **Erdos 677.** Write M(n,k)=lcm(n+1,...,n+k). For k>0 and m>=n+k, is M(m,k) different from M(n,k)? Live catalog still offers a full proof/refutation and lists only a divisibility/API contribution. [Catalog](https://conjectures.io/problems/erdos677-erdos-677), [current source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/677.lean).
- Equal LCMs do occur for unequal lengths, including M(4,3)=M(13,2) and M(3,4)=M(19,2); these do not answer the equal-length question. [Current source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/677.lean).
- **Erdos 699.** For every 1<=i<j<=n/2, is there a prime p>=i dividing both binomial(n,i) and binomial(n,j)? The live catalog lists one Kummer-carry contribution, not a solution, and upstream still labels the full claim open. [Catalog](https://conjectures.io/problems/erdos699-erdos-699), [current source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/699.lean).
- **Erdos 647.** Is there n>24 with max_{m<n}(m+tau(m))<=n+2? A single witness suffices for a positive answer. Both the live catalog and current source treat it as open. [Catalog](https://conjectures.io/problems/erdos647-erdos-647), [current source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/647.lean).

### Inferences
- 287 suggests an exact rational constraint search: choose an interval [a,b], binary indicators selecting endpoints, forbid two consecutive omissions, require sum x_j/j=1. Unique maximal prime powers in selected denominators forbid a solution; propagate those local constraints before any integer-program search. A proof would need a global obstruction surviving all possible intervals.
- 677 suggests encoding each interval by its largest power of every prime. Equal LCM candidates must have identical prime-power signatures. Search interval pairs inside runs of divisors of a chosen highly composite integer, rather than scan all pairs of endpoints. The caveat is that interval lengths cannot be changed independently.
- 699 suggests a Kummer-carry SAT formulation. For every prime p>=i dividing binomial(n,i), require no base-p carry for j+(n-j). Search n with highly smooth nearby products to shrink the constraint set. Elementary Sylvester-Schur only proves each coefficient individually has a large factor and does not force overlap.
- 647 suggests a segmented divisor sieve followed by a record-envelope test. For n>24 a witness must be even: if n is odd, n-1 is even and greater than 4, so tau(n-1)>=4 violates the required bound 3. For even n, tau(n-2)<=4 forces n-2=2q for an odd prime q, since the other even possibilities 2,4,8 are too small. Also tau(n-1)<=3 forces n-1 to be prime or an odd prime square. In the square case n-2 is divisible by 8, contradicting n-2=2q. Hence n-1=2q+1 and q must both be prime. These are necessary filters, not a solution. A stronger modular-covering analysis could be more fruitful than blind scanning.

### Gaps
- No proof or counterexample was produced. These rankings assess the availability of a concrete finite verification target, not likelihood of success.
- Direct access to erdosproblems.com returned HTTP 403, so current upstream source and live conjectures.io pages were used as primary status records.
- Search surfaced a secondary account of an unpublished Van Doorn/Rocca manuscript claiming reduction of 699 to i=3 and finitely many triples with 4<=i<=1475. The primary manuscript was not located; do not use this reduction as established without checking it. The secondary account explicitly calls the bound ineffective and leaves i=3 unresolved.

## What should be excluded before committing?

### Takeaway
An active entry in the task-target list is not enough evidence that a mathematical problem remains open. Several source statuses have changed.

### Cited Findings
- The current upstream 354 source marks the dyadic completeness question solved by Yu and Chen. [Source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/354.lean).
- The current upstream 416 source marks regular variation of the totient counting function solved, while the active target file still names its part i. [Source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/416.lean), [target list](https://github.com/conjectures-io/conjectures-tasks/blob/main/tiers/tier-1/task-targets.json).
- 323 explicitly notes major Waring-problem implications and a substantial historic barrier. 324's admitted quintic variant is equality of two sums of fifth powers, rather than the more flexible question of finding any polynomial with distinct two-term sums. [323 source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/323.lean), [324 source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/324.lean).

### Inferences
- Avoid prime-gap, prime-pattern, general additive-basis and irrationality entries absent a specific new mechanism: their short wording hides substantial established barriers.
- The existing workspace's earlier 243, 686 and 1192 artifacts should not influence the new commitment; no new route to them emerged in this survey.

### Gaps
- The survey read roughly 150 Erdős source files and checked four selected catalog pages live, but was not a complete literature review of every number theory entry.
