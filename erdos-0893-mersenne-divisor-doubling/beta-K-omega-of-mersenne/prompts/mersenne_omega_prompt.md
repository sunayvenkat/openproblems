# Prompt: prime factors of $2^p-1$ when $2^p+1$ has few divisors

## Your task

You are a research mathematician. You have one job: **prove or disprove the conjecture below**. Nothing else counts as an answer.

## Definitions

- $p$ is always prime. $M_p = 2^p - 1$.
- $\omega(n)$ is the number of distinct prime factors of $n$. $\tau(n)$ is the number of divisors of $n$.
- For an integer $K \ge 4$, define
$$P_K = \{\, p \text{ prime} : \tau(2^p+1) \le K \,\}.$$
- For $p > 3$ we have $3 \parallel 2^p+1$ and $2^p+1 = 3\,\Phi_{2p}(2)$. So $\tau(2^p+1) = 2\,\tau(\Phi_{2p}(2)) \ge 4$. Equality $\tau(2^p+1) = 4$ holds exactly when $\Phi_{2p}(2) = (2^p+1)/3$ is prime.

**The requested constant.** For each $K \ge 4$,
$$\beta_K \;=\; \limsup_{\substack{p \to \infty \\ p \in P_K}} \frac{\log \omega(M_p)\,\cdot\,\log\log p}{\log p} \;\in\; [0, \infty],$$
with $\beta_K := 0$ if $P_K$ is finite.

**Conjecture.** $\beta_K = 0$ for every $K \ge 4$. Equivalently, for every fixed $K$, as $p \to \infty$ through $P_K$,
$$\omega(2^p - 1) = \exp\!\Big( o\Big(\frac{\log p}{\log\log p}\Big) \Big).$$

What counts as a resolution:

- **Proof.** Show $\beta_K = 0$ for every $K \ge 4$.
- **Disproof.** Show that some $K$ has $\beta_K > 0$, and determine the exact value of $\beta_K$ for that $K$.
- Proving that $P_K$ is finite is a valid way to get $\beta_K = 0$ for that $K$. A proof that never uses the condition $\tau(2^p+1) \le K$ is also valid. A disproof must exhibit infinitely many $p \in P_K$.

## Return conditions (non-negotiable)

Return only when the existence and exact value of the requested constant $\beta_K$ have been completely resolved, and the argument has survived the adversarial audit below.

Do **not** return any of the following:

- an order-of-magnitude estimate
- a reduction
- a partial result
- an isolated missing lemma
- a finite computation
- a numerical guess
- a "best effort" summary
- an explanation of why the problem is difficult

If an attempt fails, discard it and start a different attempt. Do not report it.

**Integrity rule.** Never present an argument with a gap as complete. A gapped "proof" is a failure. The audit exists to catch exactly this.

## Mandatory adversarial audit

Run all six checks before returning.

1. **Fake-model test.** Build a model in which, for every $d$, the factorization of $\Phi_d(2)$ is replaced by an arbitrary product of primes $\equiv 1 \pmod d$ that keeps all of the following:
   - the same size;
   - Zsigmondy primitivity;
   - Aurifeuillian splitting;
   - lifting-the-exponent multiplicities;
   - every congruence or power-residue condition of bounded depth (e.g. $q \equiv \pm 1 \pmod 8$);
   - Stewart's bound;
   - Brun–Titchmarsh.

   Models like this exist with $\tau(2^p+1)$ bounded and $\omega(M_p) \ge \max_{m \le 2p}\tau(m)/(\log p)^{3}$ for infinitely many $p$. In those models $\beta_K \ge \log 2$.

   Models with $\beta_K = 0$ also exist.

   The only true property these models violate is exact divisibility: $q \mid 2^p - 1$ if and only if $2$ is a $\frac{q-1}{p}$-th power residue mod $q$. This is a condition of unbounded depth.

   **Requirement:** name the step of your argument that fails in the fake models, and show that this step uses exact divisibility. An argument in which every step survives the models proves nothing. Reject it.
2. **Unconditional.** No GRH, abc, Schinzel's Hypothesis H, Bateman–Horn, Cramér-type or Elliott–Halberstam assumptions. Each one, if used, must be proved.
3. **Explicit uniformity.** Every $o(1)$ and every implied constant must be uniform in $p$ and stated explicitly. No limit may be interchanged without justification.
4. **Citations.** For each cited theorem, state it exactly, with its hypotheses and a reference. Check that the hypotheses hold where you apply it. This matters most when the degree, the level or the number of places grows with $p$.
5. **Data check.** Every intermediate inequality must be consistent with the data below.
6. **Hostile re-read.** Re-read the argument as a hostile referee whose only aim is to find one false line. Repair the argument, or discard it.

## Data (exact factorizations, primes $p \le 293$)

Format: $(p,\ \tau(2^p+1),\ \omega(2^p-1))$.

(3,3,1) (5,4,1) (7,4,1) (11,4,2) (13,4,1) (17,4,1) (19,4,1) (23,4,2) (29,8,3) (31,4,1) (37,8,2) (41,8,2) (43,4,3) (47,8,3) (53,8,3) (59,16,2) (61,4,1) (67,8,2) (71,8,3) (73,8,3) (79,4,3) (83,64,2) (89,16,1) (97,32,2) (101,4,2) (103,8,2) (107,8,1) (109,8,2) (113,32,5) (127,4,1) (131,16,2) (137,32,2) (139,8,2) (149,32,2) (151,8,5) (157,32,4) (163,16,5) (167,4,2) (173,64,4) (179,8,3) (181,16,4) (191,4,5) (193,64,3) (197,16,2) (199,4,2) (211,64,3) (223,8,6) (227,16,2) (229,8,4) (233,16,4) (239,16,6) (241,32,2) (251,8,5) (257,16,3) (263,32,4) (269,8,2) (271,32,2) (277,8,3) (281,16,2) (283,64,3) (293,64,2)

Additional facts:

- For all $d \le 600$: $\max \omega(\Phi_d(2)) = 8$.
- For every $p \in P_4$ with $p \le 293$: $\omega(M_p) \le 5$.

## Tools and facts you should use or rule out

### Elementary and cyclotomic structure

- **Divisors of $M_p$.** If $q \mid M_p$, then $\operatorname{ord}_q 2 = p$. Hence $q \equiv 1 \pmod{2p}$ and $q \equiv \pm 1 \pmod 8$.
- **Bang–Zsigmondy.** $2^n - 1$ has a primitive prime divisor for every $n \ne 1, 6$.
- **Bilu–Hanrot–Voutier.** Primitive divisors of Lucas and Lehmer numbers.
- **Disjoint fibres.** Each prime $q$ divides $M_p$ for at most one prime $p$, namely $p = \operatorname{ord}_q 2$.
- **Lifting the exponent.** $v_q(2^{pk} - 1) = v_q(2^p - 1) + v_q(k)$ for $q \mid M_p$.
- **Exact dictionary.** $\mathbb{Z}[\zeta_p]/(2 - \zeta_p) \cong \mathbb{Z}/M_p$.
  - The prime ideals dividing $(2 - \zeta_p)$ are $(q, \zeta_p - 2)$ for $q \mid M_p$. They have degree 1, and above each such $q$ exactly one of them occurs. So $\omega(M_p)$ equals the number of distinct prime ideal factors of $2 - \zeta_p$.
  - Likewise $\mathbb{Z}[\zeta_p]/(2 + \zeta_p) \cong \mathbb{Z}/\Phi_{2p}(2)$.
  - The relation $(2 - \zeta_p) + (2 + \zeta_p) = 4$ holds, and the two ideals are coprime.
- **Identities.**
  - $2^p + 1 = M_p + 2$.
  - $2^{2p} - 1 = M_p\,(2^p + 1)$.
  - $M_p = -N_{\mathbb{Q}(\sqrt2)/\mathbb{Q}}\big(1 - (\sqrt2)^p\big)$ and $2^p + 1 = N_{\mathbb{Q}(\sqrt{-2})/\mathbb{Q}}\big(1 + (\sqrt{-2})^p\big)$.
- **Fermat-quotient congruence.** Write each prime factor as $q = 1 + 2p\,m_q$. Then
$$\sum_{q \mid M_p} v_q(M_p)\, m_q \equiv \frac{2^{p-1} - 1}{p} \pmod p.$$
  Higher congruences modulo $p^j$ follow from the identity $\prod_q (1 + 2p\,m_q)^{v_q} = 2^p - 1$.

### Size and counting

- **Trivial bound.** $\omega(M_p) \le p \log 2 / \log(2p+1)$.
- **Brun–Titchmarsh** (Montgomery–Vaughan form), applied to primes $\equiv 1 \pmod{2p}$, gives $\omega(M_p) \le (\tfrac{\log 2}{2} + o(1))\,p/\log p$.
- **Wigert.** $\max_{m \le x} \tau(m) = 2^{(1+o(1))\log x/\log\log x}$.
- **Stewart** (Acta Math. 2013): $P(2^n - 1) > n \exp\!\big(\log n/(104 \log\log n)\big)$ for large $n$.
- **Erdős–Murty.** $\operatorname{ord}_q 2$ is large for almost all $q$.
- **Sieve theory.** Large sieve; Bombieri–Vinogradov; Linnik's theorem; the parity barrier (Selberg; Friedlander–Iwaniec, *Opera de Cribro*); Bombieri's asymptotic sieve.

### Kummer theory and Chebotarev

- **Power-residue criterion.** $q \mid M_p$ if and only if $q \equiv 1 \pmod p$ and $q$ splits completely in $\mathbb{Q}(\zeta_m, 2^{1/m})$, where $m = (q-1)/p$.
- **Kummer degree.** $[\mathbb{Q}(\zeta_m, 2^{1/m}) : \mathbb{Q}] = m\,\varphi(m)$, halved when $8 \mid m$.
- **Effective Chebotarev** (Lagarias–Odlyzko, unconditional form). Hooley's method for Artin's conjecture. Burgess and Pólya–Vinogradov bounds for power-residue characters.
- **Cyclotomic arithmetic.** Stickelberger's theorem; Gauss and Jacobi sums; Eisenstein reciprocity; class groups of $\mathbb{Q}(\zeta_p)$; Herbrand–Ribet.

### Subgroups of $\mathbb{F}_q^*$

For $q \mid M_p$, the subgroup $H_q = \langle 2 \rangle$ has order $p$. It contains the genuine small integers $1, 2, 4, \dots, 2^{\lfloor \log_2 q \rfloor}$.

- **Bounds on subgroups.** Stepanov's method; Heath-Brown–Konyagin bounds for $|H \cap (H + a)|$ and for Heilbronn sums; Bourgain–Glibichuk–Konyagin exponential-sum bounds for subgroups; sum–product estimates in $\mathbb{F}_q$.
- **Additive coincidences.** Coincidences $2^a + 2^b \equiv 2^c + 2^d \pmod q$ are equivalent to $q$ dividing a sparse integer. For example, the energy count $E(H_q) \ge |H_q|^4 / q$ alone only reproduces equidistribution. To get anything, use more than this.

### Diophantine approximation and the polynomial method

- **Lower bounds for linear forms in logarithms.** Matveev (archimedean) and Yu (p-adic).
- **Approximation theorems.** Thue–Siegel–Roth; Ridout and Schlickewei (p-adic Roth); Schmidt's Subspace Theorem and its quantitative forms (Evertse–Schlickewei–Schmidt).
- **S-unit equations and gcd bounds.** Corvaja–Zannier gcd theorems; Bugeaud–Corvaja–Zannier: $\gcd(a^n - 1, b^n - 1) \le e^{\varepsilon n}$.
- **Auxiliary polynomials and determinants.** Siegel's lemma; Laurent's interpolation determinants; the Bombieri–Pila and Heath-Brown determinant methods.
- **Lattices and residue classes.** Lenstra, divisors in residue classes (at most 11 divisors in a class mod $s \ge N^{1/3}$); Coppersmith–Howgrave-Graham–Nagaraj (range $s \ge N^{1/4+\varepsilon}$); Coppersmith small roots.

## Directions to try

Each direction below lists the exact property it exploits. Each must still pass the fake-model test.

**A. Auxiliary polynomial across the $q$-adic places**
- *Exact property.* For each $q \mid M_p$, the integer $2$ is $q$-adically within $q^{-v_q(M_p)}$ of a primitive $p$-th root of unity $\omega_q \in \mathbb{Z}_q$. All of these approximations hold at once. Their product equals exactly $1/M_p$; this is the Liouville equality.
- *Strategy.* Build an integer polynomial with controlled height that vanishes to high order at $x = 2$ modulo every $q$ in a set $S \subseteq \{q \mid M_p\}$. Then compare its value at $2$, or at $2^j$, with the product formula.
- *What to find.* The gain must come from the number $|S|$ of places, not from the approximation quality, which is already Liouville-sharp. Find the mechanism by which many places force a contradiction. Thue–Siegel-type pointwise rigidity is the reason to hope it is not distributional.

**B. Sparse multiples and the Subspace Theorem**
- *Correspondence.* Additive coincidences in $H_q$ correspond to $q$ dividing integers $\sum_{i \le T} \pm 2^{e_i}$ with $e_i < p$.
- *Strategy.* Bound $\sum_u \omega(\gcd(u, M_p))$ over such sparse integers $u$ pointwise. Use gcd results of Corvaja–Zannier type, which see the exact shape of $2^p - 1$. Then force coincidences from the size of $H_q$ relative to $q$, using higher energies $E_T$.
- *Warning.* Naive counting only matches equidistribution. You need a structural input of the Subspace Theorem type.

**C. Divisor lattices**
- *Starting point.* If $\omega$ is large, then $M_p$ has $2^\omega$ divisors at all scales.
- *Goal.* Find a modulus $s \ge M_p^{1/4+\varepsilon}$ such that all divisors of $M_p$ fall into few residue classes mod $s$. Then Lenstra and Coppersmith–Howgrave-Graham–Nagaraj bound $\tau(M_p)$.
- *Candidate source.* The complementary-divisor relation $d\,e \equiv -1 \pmod{2^p}$, or the relation $M_p + 2 = 3\,\Phi_{2p}(2)$ with $\Phi_{2p}(2)$ nearly prime.

**D. $p$-adic symmetric-function constraints**
- *Constraint.* Writing $q = 1 + 2p\,m_q$, the elementary symmetric functions of the $m_q$ are fixed by the $p$-adic digits of $2^p - 1$.
- *Strategy.* Combine with Fermat-quotient and Wieferich-type theory to show that many factors force an impossible congruence pattern.

**E. Coupling $2 - \zeta_p$ with $2 + \zeta_p$**
- *Setup.* $(2 - \zeta_p) + (2 + \zeta_p) = 4$, and $(2 + \zeta_p)$ has at most $\log_2(K/2)$ prime-ideal factors.
- *Caveat.* Plain class-group and Eisenstein-reciprocity arguments see no coupling between the two factor counts. Reopen this direction only with a reciprocity law whose degree depends on $q$, namely of order $(q-1)/p$.

**F. Disproof by existence**
- *What is needed.* Infinitely many $p$ for which $\Phi_{2p}(2)$ has a bounded number of prime factors and $M_p$ has many.
- *Obstacle.* This needs a lower-bound sieve for the exponential sequence $2^p + 1$ that beats the parity barrier, for example through bilinear structure, together with a mechanism that forces many $q$ with $\operatorname{ord}_q 2 = p$.

## Output format

1. **Statement.** The exact theorem proved, either $\beta_K = 0$ for all $K$, or $\beta_K = c$ for a specific $K$ with $c > 0$.
2. **Proof.** A complete proof, with numbered lemmas and every constant explicit.
3. **Fake-model step.** A paragraph naming the step that fails in the fake models, and why.
4. **Audit log.** One line per check, each marked passed.
