# Erdős 269: attempted transfer from the 1062 irrationality method

## What is the exact target, and what is already known?

### Takeaway

The eligible target quantifies over every finite prime set with at least two members. The two-prime case is already known to be transcendental. The first new case would therefore have at least three primes; no full proof for that case is established here.

### Cited Findings

- The live entry is `Erdos269.erdos_269.variants.irrational`, status null, zero attempts in the saved 6 November 2026 snapshot. It asks for irrationality of the sum of reciprocals of all running LCMs of the increasing sequence of P-smooth positive integers, with multiplicities retained. [Live target](https://conjectures.io/problems/erdos269-erdos-269-variants-irrational).
- The precise universal quantifier is over finite sets P of primes with cardinality at least two. The formal `series` includes the empty-prefix term 1; that rational additive constant does not affect irrationality. [Primary target source](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/269.lean).
- Steve Fan's 26 June 2026 comment gives the two-prime factorization and transcendence argument. The relevant Hecke–Mahler transcendence theorem was established earlier by Loxton–van der Poorten; Bugeaud–Laurent's Theorem 1.1 includes the needed case. [Fan's primary comment](https://www.erdosproblems.com/forum/thread/269#post-7218), [Bugeaud–Laurent](https://arxiv.org/html/2203.12901).
- Cook's current manuscript explicitly leaves the repeated series for three or more primes open. It distinguishes this from the easier sum obtained by deleting repeated denominators. [Primary manuscript](https://github.com/wcook04/plectis-erdos/blob/main/docs/papers/full-text/erdos-269-three-prime-running-lcm.md).

### Inferences

A proof for only two primes would neither be new nor settle the current entry. Proving irrationality after deleting duplicate summands would change the target.

### Gaps

The public forum page was not directly retrievable in this session; Fan's attribution and exact reference are recorded in Cook's primary manuscript, and the mathematical reduction below was independently derived. The supporting Bugeaud–Laurent theorem was read directly.

## Which exact lemma can be imported from 1062?

### Takeaway

The reusable result is a lower bound for a nonzero linear form in a fixed number of S-units. The hard problem-specific input is a sparse return identity with suitable height and non-cancellation bounds, not merely a series with denominators supported on finitely many primes.

### Cited Findings

Proposition 7.4 of Kohlmeyer–Kruer states: for fixed m, rational coefficients d_1,...,d_m and epsilon>0, there is C>0 such that, for N integral, positive {2,3}-units u_i and 0<t<=min(1,u_1,...,u_m),

    E = sum_i d_i u_i - N != 0
    implies |E| >= C t H(N:u_1:...:u_m)^(-epsilon).

The same conclusion holds for a pure form. Their proof uses a Subspace-Theorem covering statement and induction on the number of terms. In the actual application, the number of terms is at most 404 and the coefficient vector belongs to a fixed finite set. A return scale L supplies a nonzero upper bound exp(-T-L/200), while height is at most exp(27L) and every unit is at least exp(-T). [Proposition 7.4 and Corollary 6.5, primary manuscript](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf).

### Inferences

The ordinary-mathematical argument for the lower bound generalizes to any fixed finite prime set P by replacing the three places {infinity,2,3} with {infinity} union P in the p-adic Subspace Theorem. It does not require a new irrationality theorem. This generalization is mathematical, not a claim that the authors' specific Lean development handles arbitrary P.

The source cannot be invoked with an unbounded number of event terms, or an arbitrary changing coefficient vector, while silently retaining a uniform constant C. Those are distinct hypotheses that a transfer must establish or replace.

### Gaps

No bounded-term return representation with the required exponentially small nonzero error has been proved below for the repeated three-prime series.

## What exact algebraic reductions are available?

### Takeaway

The running LCM has a simple closed formula. This gives convergence, an exact two-prime factorization, and a general integer tail recurrence. None of these identities alone implies irrationality.

### Cited Findings

For x>=1, write H_P(x)=product_{p in P} p^floor(log_p x). The running LCM of all P-smooth integers at most x is exactly H_P(x): every such integer divides this product, and the prefix contains each maximal pure prime power. This identity is also recorded in the [primary three-prime manuscript](https://github.com/wcook04/plectis-erdos/blob/main/docs/papers/full-text/erdos-269-three-prime-running-lcm.md).

### Inferences

The following derivations are independent calculations, not new-priority claims.

Let k=|P| and R_P=sum_{a P-smooth} 1/H_P(a). Since

    H_P(x) > x^k / product_{p in P} p,

the series is absolutely convergent by comparison with

    (product p) product_{p in P} (1-p^(-k))^(-1).

For two primes p<q, set alpha=log_q p, x=1/p and y=1/q. Then

    H_{p,q}(p^i q^j)
      = p^(i+floor(j/alpha)) q^(j+floor(i alpha)).

Consequently R_{p,q}=A B, where

    A=sum_{i>=0} p^(-i) q^(-floor(i alpha)),
    B=sum_{j>=0} q^(-j) p^(-floor(j/alpha)).

Partitioning positive lattice points (i,j) by j<i alpha or i<j/alpha gives

    (p-1) A + (q-1) B = p+q-1.

There are no equality points because alpha is irrational. More explicitly, for the Hecke–Mahler value

    F=sum_{i>=1} x^i sum_{1<=j<=floor(i alpha)} y^j,

we have A=p/(p-1)-(q-1)F. The hypotheses of Bugeaud–Laurent hold: 0<alpha<1 is irrational, x and y are nonzero algebraic numbers, x!=1 and |x y^alpha|<1. Thus A is transcendental. The product AB is a nonconstant quadratic polynomial in A over Q, so it is transcendental as well. This recovers the already-known two-prime argument.

For general P, let q=min P and Q_a=H_P(q^a). Group the repeated series into shells [q^a,q^(a+1)) and define

    s_a = sum_{a_shell P-smooth x} 1/H_P(x),
    m_a = (Q_(a+1)/q) s_a,
    b_a = Q_(a+1)/Q_a,
    X_a = (Q_a/q) sum_{j>=a} s_j.

Every m_a is a positive integer. Each b_a is q times a product of a subset of P\{q}, because at most one power of each larger prime lies between consecutive powers of q. The exact recurrence is

    X_(a+1) = b_a X_a - m_a.

For a>=1, the LCM at every earlier smooth integer divides Q_a/q. Therefore rationality of R_P puts all sufficiently late X_a in a fixed rational lattice. However, m_a and X_a are not bounded: both have order a^(k-1), with constants depending on P. The upper bound follows by choosing the k-1 exponents of the other primes, each at most a, and the unique exponent of q placing the product in the shell. A lower bound follows by allowing each of those exponents to range up to a fixed sufficiently small positive multiple of a. Every resulting odd-to-q part has a unique q-multiple in the shell, and each summand in m_a is at least one.

This proves why the finite-state proof for the distinct-denominator series cannot be copied: a fixed rational lattice intersected with a growing interval is not a finite set of tail states.

### Gaps

The general recurrence is a useful exact interface but supplies no contradiction to a polynomially growing integer orbit. Many bounded-radix recurrences admit such orbits.

## Does a scalar finite difference make the repeated series sparse?

### Takeaway

The most direct attempted bridge fails. Small rotations control floor-crossing carries, but new lattice points enter the counting region and leave boundary terms. A concrete exact counterexample defeats the cubic-cancellation claim.

### Cited Findings

For P={2,3,5}, Cook's Proposition 44 decomposes the weighted cubic difference into interior terms and three new boundary strips. Example 45 has no floor crossings but a nonzero third difference. The paper explicitly warns that polynomial growth of the coefficients is weaker than being a polynomial evaluated at a floor. [Proposition 44, Example 45 and the following comparison](https://github.com/wcook04/plectis-erdos/blob/main/docs/papers/full-text/erdos269-running-lcm-reasoning-surface.md).

### Inferences

Here is the general exact weighted-shift identity, which displays where a new proof would be needed. Put alpha_P=R_P/q, M=product_{p in P\{q}}p, and for integers a,t>=0 define

    gamma_(a,t)=Q_t Q_(a+1)/Q_(a+t+1).

For each p!=q, floor addition makes its exponent in gamma either zero or minus one. Thus gamma is the reciprocal of a product of a subset of P\{q}. Given fixed integers c_0,...,c_sigma and a positive shift r, let

    D_(r,a)=M sum_j c_j gamma_(a,jr) m_(a+jr),
    A_r=M sum_j c_j Q_(jr),
    Z_r=M sum_j c_j Q_(jr) sum_{h<jr} m_h/Q_(h+1).

All three quantities are integral and absolute convergence gives

    A_r alpha_P - Z_r = sum_{a>=0} D_(r,a)/Q_(a+1).

This preserves the actual repeated-series value. It does not show that D_(r,a) vanishes at most indices.

For P={2,3,5}, use r=35 and c=(1,-3,3,-1). At u=0,35,70,105, there is no 3-power or 5-power inside [2^u,2^(u+1)). Exact exponent bounds are respectively

    floor(log_3 2^u)=floor(log_3 2^(u+1)) = 0,22,44,66,
    floor(log_5 2^u)=floor(log_5 2^(u+1)) = 0,15,30,45.

The corresponding integers m_u count pairs (j,k) with 3^j 5^k<2^(u+1), and are

    1, 195, 723, 1582.

All relevant gamma factors equal one and every floor-crossing bit vanishes. Nevertheless

    D_(35,0)=15(1-3*195+3*723-1582)=45 != 0.

The nonzero value comes from strip counts 194,528,859, whose alternating combination is -194+2*528-859=3. This is a direct obstruction to claiming sparse return events solely from simultaneous approximation and quadratic coefficient growth.

An independent Node.js BigInt enumeration in this session verified all four counts and both pairs of endpoint floor equalities using only integer comparisons and divisions. It returned the exact weighted difference 45; no floating-point logarithms were used in that check.

An alternative using exact translations in the exponent lattice was considered. Translation can cancel the common interior, but replacing a scalar shift by a nearby coordinate translation creates a thin boundary strip. For three primes there is no established estimate here forcing only a bounded number of surviving terms on a return-scale interval. Ordinary simultaneous approximation only supplies errors of roughly scale^(-1/2), which does not itself control the number of lattice points along a boundary of length comparable to the scale. This is a limitation of this attempted argument, not a theorem that all such approaches fail.

### Gaps

To turn #1062's Proposition 7.4 into a proof of #269, one still needs a new cancellation or compression theorem for these boundary contributions, a nonzero error guarantee, and compatible height bounds. The supplied identities do not establish those hypotheses. No unconditional proof, disproof, or newly solved target is claimed.
