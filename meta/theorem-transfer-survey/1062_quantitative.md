# An explicit error bound for Erdős 1062

## What follows from the exact formula?

### Takeaway

Using the exact formula of Kruer and Kohlmeyer, one obtains the following explicit quantitative corollary for every integer n>=1:

\[
\boxed{\;|f(n)-cn|\leq \frac{10}{3}\log_4 n+
\frac{8}{3}\log_3 n+9.\;}
\]

In particular f(n)=cn+O(log n), with the same irrational density c as in their paper. This is a consequence of their exact theorem, not a solution of another catalog problem. No novelty or optimality claim is established here. [Underlying primary paper](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf)

### Cited Findings

The authors' Theorem 1.1 gives

\[
f(n)=\sum_{m\le n,\,(m,6)=1}g(n/m),\qquad
g(x)=1+\lfloor\log_4x\rfloor+\lfloor\log_3x\rfloor+1_E(x)-1_B(x)
\]

for x>=1, and g(x)=0 for x<1. Here

\[
E=\left(\bigcup_{j\ge0}[2\cdot4^j,4^{j+1})\right)
\cap\left(\bigcup_{b\ge0}[2\cdot3^b,3^{b+1})\right),
\]

\[
B=\left(\bigcup_{b\ge0}[10\cdot3^b,12\cdot3^b)\right)
\cap\left(\bigcup_{j\ge0}[4^j,(5/4)4^j)\right).
\]

Their density formula is c=(1/3) integral from 1 to infinity of g(x)/x^2 dx. The paper displays c=0.672965651199489347471227919852209644752814733132999025108932699233..., and explains that its exact formula's lower bound rests on a finite computation. Its density argument uses convergence; the explicit O(log n) inequality above was not found in its displayed results. [Primary paper, Theorems 1.1–1.3 and Section 5](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf)

### Inferences

**Complete proof of the quantitative corollary.** Define

\[
h(x)=\lfloor\log_4x\rfloor+1_E(x)-1_B(x)\quad(x\ge1),
\qquad h(x)=0\quad(x<1).
\]

The function h is right-continuous and locally a step function, with h(1)=0. Let J be its set of discontinuities and a_s=h(s)-h(s-) its **signed** jump at s. In particular no monotonicity of h or g is assumed. Indeed g has a negative jump at 270.

Put

\[
N_6(y)=\#\{m\le y:(m,6)=1\}.
\]

Writing y=6k+t with 0<=t<6 gives N_6(y)=2k+1_{t>=1}+1_{t>=5}. Hence, for every y>=0,

\[
\left|N_6(y)-\frac y3\right|\le\frac23.\tag{1}
\]

The first cancellation is exact:

\[
\sum_{m\le n,(m,6)=1}\left(1+\lfloor\log_3(n/m)\rfloor\right)
=\sum_{b\ge0}N_6(n/3^b)=\left\lceil\frac n2\right\rceil.\tag{2}
\]

The last equality counts the odd integers up to n by their unique factorisation m3^b with (m,6)=1. Since h(x)=sum_{s<=x} a_s, finite interchange in the remaining part yields

\[
f(n)=\left\lceil\frac n2\right\rceil+
\sum_{s\in J,\,s\le n}a_sN_6(n/s).\tag{3}
\]

We now bound absolute jumps, so all possible negative contributions are covered. The floor term has jumps of absolute value one along 4^j (j>=1). The first factor defining E changes along 2*4^j and 4^{j+1}; the second factor along 2*3^b and 3^{b+1}. The first factor defining B changes along 10*3^b and 12*3^b; the second along 4^j and (5/4)*4^j. For zero-one variables,

\[
|uv-u'v'|\le |u-u'|+|v-v'|,
\]

so the variation of either product is bounded by the sum of the variations of its two factors. Coincident endpoints cause no difficulty: count them with multiplicity in this upper bound. The absolute jump measure of h is therefore dominated by five geometric sequences of ratio 4 and four of ratio 3, each with unit weights.

Counting endpoints individually gives, for n>=1,

\[
\begin{aligned}
V(n):=\sum_{s\le n}|a_s|
&\le \log_4n+(2\log_4n+1)+(2\log_3n+1)\\
&\qquad +(2\log_3n+2)+(2\log_4n+2)\\
&=5\log_4n+4\log_3n+6.\tag{4}
\end{aligned}
\]

For any geometric sequence of ratio r>1, the sum of reciprocal terms strictly greater than n is at most r/((r-1)n). Consequently

\[
\sum_{s>n}\frac{|a_s|}{s}
\le\frac1n\left(5\cdot\frac43+4\cdot\frac32\right)
=\frac{38}{3n}.\tag{5}
\]

In particular sum |a_s|/s converges absolutely. Term-by-term integration of the step-function expansion is legitimate, and (2), or its integral analogue, gives

\[
c=\frac12+\frac13\sum_{s\in J}\frac{a_s}{s}.\tag{6}
\]

Subtract n times (6) from (3), and write epsilon(y)=N_6(y)-y/3:

\[
f(n)-cn=
\left\lceil\frac n2\right\rceil-\frac n2+
\sum_{s\le n}a_s\epsilon(n/s)-\frac n3\sum_{s>n}\frac{a_s}{s}.
\]

Equations (1), (4), and (5) therefore imply

\[
\begin{aligned}
|f(n)-cn|
&\le\frac12+\frac23\left(5\log_4n+4\log_3n+6\right)+\frac{38}{9}\\
&=\frac{10}{3}\log_4n+\frac83\log_3n+\frac{157}{18}\\
&<\frac{10}{3}\log_4n+\frac83\log_3n+9.
\end{aligned}
\]

This proves the claimed bound. The harmless weakened constant 9 avoids carrying 157/18 through subsequent uses.

### Gaps

- This proof invokes the authors' full exact formula. It is not an independent proof of their finite certificate theorem or their irrationality theorem.
- The O(log n) error is proved; optimality is not. The cancellation in (2) shows why simply counting all jumps can overestimate the true discrepancy, so O(1) must not be ruled out without further work.

## What was checked independently?

### Takeaway

Two exact-integer evaluations of the formula agree on all n<=400, and a separate binary optimisation model agrees at 37 sample sizes including the negative jump at 270. These computations check the implementation and small instances; they do not replace the mathematical proof for all n.

### Cited Findings

The primary paper gives f(10^6)=672964, f(10^12)=672965651200, and f(10^24)=672965651199489347471228. The script reproduces all three using signed jumps and integer arithmetic. [Primary paper, Section 1.1](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf)

### Inferences

The reproducible script is `check_1062.py`, with output in `check_1062.json`, in this notes folder. It implements:

- the direct sum over 6-coprime m;
- the signed-jump expression (3), agreeing with the direct expression for n=1,...,400;
- a separate integer optimisation problem with binary x_a for 1<=a<=n.

For the optimisation model, put t_a=floor(n/a)-1. For each a<=n/3 impose

\[
\sum_{k=2}^{\lfloor n/a\rfloor}x_{ka}+(t_a-1)x_a\le t_a.
\]

If x_a=0 the constraint is automatic; if x_a=1 it permits at most one selected proper multiple of a. Thus these constraints are exactly fork-freeness, and maximising sum x_a computes f(n). The SciPy/HiGHS runs returned zero reported optimality gap for n=3,...,30 and n in {50,100,269,270,271,319,320,321,500}. Rounded selected sets were independently checked by integer divisibility; their cardinalities agreed with the formula in every case. This is numerical optimisation evidence, not a formal certificate audit.

The script also sums the rational series (6) through T=10^70 and uses (5) to certify a density tail at most 38/(9T). It samples discrepancies at b^k-1, b^k, b^k+1 for b in {2,3,4,6,10}, k<=64 and b^k<=10^50. The largest observed absolute discrepancy in that sample is about 7.594. Such a bounded finite sample neither proves an O(1) error nor disproves one; its purpose is to avoid assuming exact floor-function cancellation without evidence.

### Gaps

- No asymptotic lower bound on |f(n)-cn| is established.
- No claim is made that this immediate quantitative corollary has not previously been observed elsewhere.
- Lean formalisation was deferred as requested.

## What is the precise research status?

### Takeaway

The finished mathematical deliverable is an explicit convergence rate for an already solved problem, with a complete short proof from the published exact formula. It should be presented as such, rather than as a new solution to an unsolved Erdős problem.

### Cited Findings

The authors explicitly state that their exact formula resolves the first part of 1062 and that the irrationality result resolves its second part. [Primary paper, Section 1.1](https://github.com/JENW1N/complete-math-solutions/blob/main/papers/erdos1062-fork-free-density.pdf)

### Inferences

The rate proved here is mathematically definite once their exact formula is accepted. Its proof depends only on elementary counting and signed step-function summation, not on the Subspace Theorem used in their irrationality argument. This makes the quantitative corollary independently inspectable even while the larger source proof is being reviewed.

### Gaps

Novelty certification and error-term sharpness remain unestablished.
