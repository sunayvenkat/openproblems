# Prime factors of $2^p-1$ when $2^p+1$ has few divisors: a research note

**Status: unresolved.** This note does not prove or disprove the conjecture $\beta_K=0$. It records what was established while attacking it: proved lemmas, two barrier theorems, one genuine (non-fake) obstruction, a function-field analogue that *is* provable, corrections to the problem statement, and a precise description of the single estimate every approach reduces to.

The work was done in two waves of parallel agents (13 attack/verification tasks in all), followed by an independent hostile audit of the key claims. No internet access was used, so all literature statements are from memory and are marked as such. Agent write-ups and scripts are in `mersenne_omega_appendix/`.

Labels used throughout: **PROVED** (proof given or in the appendix), **CITED** (standard theorem, stated from memory), **VERIFIED** (computation), **HEURISTIC** (not a theorem).

---

## 1. Problem

$p$ is prime, $M_p=2^p-1$, $P_K=\{p:\tau(2^p+1)\le K\}$, and

$$\beta_K=\limsup_{p\to\infty,\ p\in P_K}\frac{\log\omega(M_p)\cdot\log\log p}{\log p},\qquad \beta_K:=0 \text{ if } P_K \text{ is finite}.$$

**Conjecture.** $\beta_K=0$ for every $K\ge 4$, i.e. $\omega(M_p)=\exp(o(\log p/\log\log p))$ along $P_K$.

Notation: $\zeta=\zeta_p$, $\mathcal O=\mathbb Z[\zeta]$, $a_p=\Phi_{2p}(2)=(2^p+1)/3$, $F=(2^{p-1}-1)/p$.

## 2. Summary

1. **A disproof is out of reach.** $\beta_K>0$ implies infinitely many composite Mersenne numbers $M_p$ with $p$ prime, and infinitely many $p$ with $\Omega(a_p)\le K/2-1$. Both are open (Theorem 4.1).
2. **Finiteness of $P_K$ is out of reach and believed false.** It would imply finitely many Wagstaff primes. No covering or fixed-family certificate can prove it (Lemma 3.4, Proposition 4.3).
3. **A proof must be pointwise, and it must use exact divisibility of unbounded depth.** Under bounded-depth axioms there are consistent models with $\tau(2^p+1)=4$ for all large $p$ and either $\beta_K=0$ or $\beta_K=\infty$ (Theorem 5.2).
4. **Even exact divisibility at the level of ideals is not enough by itself.** The elements $\alpha_k=2^k-\zeta$ share every algebraic feature of $2-\zeta$ used by the class-group, Stickelberger, Galois and lattice approaches, yet have $\omega\ge\tau(k)$, which reaches ratio $\log 2$ (Theorem 6.1).
5. **Every method tried reduces to one open estimate (§8).** These are auxiliary polynomials, sparse multiples / Subspace, divisor lattices, $p$-adic symmetric functions, reciprocity, subgroup bounds, interpolation of $2^z$, and Kummer–Chebotarev. The estimate is: count $q\equiv1\pmod{2p}$ with $2^p\equiv1\pmod q$, pointwise in $p$, beating $(\tfrac{\log2}{2}+o(1))p/\log p$.
6. **The function-field analogue is true** (Theorem 7.1). The mechanism that proves it, a Frobenius order shared by $a^p-1$ and $a^p+1$, has no counterpart over $\mathbb Z$.
7. **Two statements in the problem are false.** "$\max_{d\le600}\omega(\Phi_d(2))=8$" is false because $\omega(M_{397})=9$. The $p$-adic "symmetric functions are fixed" claim is too strong (§9).

---

## 3. Elementary facts (all PROVED)

**Lemma 3.1 (3-part).** For $p\ge5$, $3\parallel 2^p+1$ and $\tau(2^p+1)=2\tau(a_p)$.
*Proof.* $\operatorname{ord}_9 2=6$, so $2^p+1\equiv 3$ or $6\pmod 9$. ∎

**Lemma 3.2 (mod 8).** For $p\ge5$:
- $a_p\equiv 3\pmod 8$.
- Every prime $Q\mid a_p$ has $\operatorname{ord}_Q2=2p$ and $Q\equiv1\pmod{2p}$.
- $Q\equiv 3\pmod 8$ iff $(Q-1)/(2p)$ is odd, and otherwise $Q\equiv1\pmod 8$.
- The number of prime factors of $a_p$ that are $\equiv3\pmod8$, counted with multiplicity, is odd.

*Proof.* $2^p\equiv 8\pmod{24}$ gives $a_p\equiv3\pmod 8$. Since $2^p\equiv-1\pmod Q$, Euler's criterion gives $(2/Q)=2^{(Q-1)/2}=(-1)^{(Q-1)/(2p)}$. Combining $(2/Q)=1\iff Q\equiv\pm1\pmod 8$ with the parity of $(Q-1)/2$ gives the third point. The last point holds because $3^k\equiv3\pmod 8$ iff $k$ is odd. ∎

**Corollary 3.3.** $a_p$ is never a square, so $4\mid\tau(2^p+1)$, $P_K=P_{4\lfloor K/4\rfloor}$, and $\beta_K=\beta_{4\lfloor K/4\rfloor}$. In particular $P_6=P_7=P_4$.

**Lemma 3.4 (disjoint fibres, no covering).**
- Prime factors of $M_p$ have $\operatorname{ord}_q2=p$. Prime factors of $a_p$ have $\operatorname{ord}_Q 2=2p$.
- So no prime divides two members of $\{M_p\}\cup\{a_p\}$.
- For any finite set $S$ of primes, $\gcd(a_pM_p,\prod S)=1$ once $2p+1>\max S$.
- Hence no covering-congruence argument can force $a_p$ to be composite. ∎

**Lemma 3.5 (trivial bound).** If $q_1<\dots<q_k$ divide $M_p$, then $q_j\ge 2pj+1$, so $(2p)^k k!<2^p$. Hence
$$\omega(M_p)\le\Big(\tfrac{\log 2}{2}+o(1)\Big)\frac{p}{\log p}.$$
Brun–Titchmarsh is not needed for this. ∎

A sharper second-order form (PROVED, citing Montgomery–Vaughan) is in `appendix/second_order_bound.md`. It uses the fact that $q$ lies in only two classes mod $8p$, and gives $\omega(M_p)\le\frac{\log2}{2}\,p/(\log p-1.0298+o(1))$. This does not improve the constant $\log2/2$.

**Remark 3.6 (correcting a natural reduction).**
- At most $p\log2/\log X$ prime factors of $M_p$ exceed $X$.
- With $X=2^{p^{1-\varepsilon}}$ that number is $p^{\varepsilon}$. This is $\exp(o(\log p/\log\log p))$ only if $\varepsilon=o(1/\log\log p)$.
- So the uncovered range is $q\in[p^{1+o(1)},\,2^{p^{1-o(1)}}]$, not a fixed-$\varepsilon$ range.

**Lemma 3.7 (a priori range).** The quantity in $\beta_K$ lies in $[0,(1+o(1))\log\log p]$, so a priori $\beta_K\in[0,\infty]$. Even $\beta_K<\infty$ requires $\omega(M_p)\le p^{O(1/\log\log p)}$ on $P_K$, far beyond Lemma 3.5.

---

## 4. Set-level routes (PROVED implications)

**Theorem 4.1 (what a disproof implies).** Suppose $\beta_K>0$ for some $K$, and let $0<c<\beta_K$. Then there are infinitely many primes $p$ with all of:
- $\Omega(a_p)\le K/2-1$ and $\omega(a_p)\le\log_2(K/2)$;
- $\omega(M_p)\ge\exp(c\log p/\log\log p)$, in particular $M_p$ composite.

*Proof.* $\beta_K>0$ forces $P_K$ to be infinite, by the convention $\beta_K=0$ for finite $P_K$. Then use $\tau(n)\ge\Omega(n)+1$ and $\tau(n)\ge2^{\omega(n)}$ on $\tau(a_p)=\tau(2^p+1)/2\le K/2$. ∎

Both conclusions are open problems (CITED from memory: infinitude of composite $M_p$ with $p$ prime is in Guy, *Unsolved Problems in Number Theory*, A3). A disproof would settle both on one common set of $p$.

**Proposition 4.2 (what finiteness means).** $P_K$ is finite for every $K$ iff $\Omega(a_p)\to\infty$. In particular finiteness of $P_4$ means there are finitely many Wagstaff primes. The standard heuristic predicts about $C\log\log x$ Wagstaff exponents up to $x$ (HEURISTIC), so this route aims at something believed false.

**Proposition 4.3 (no fixed-family certificate).** Fix nonconstant $f_1,\dots,f_r\in\mathbb Z[x]$. Then there is a set of primes $p$ of positive relative density for which no $f_j(p)$ is a nontrivial divisor of $a_p$, and likewise of $M_p$.

*Proof.* Pick small primes $\ell_j$ and residues $r_j\not\equiv0$ with $\ell_j\mid f_j(r_j)$. Take $p\equiv r_j\pmod{\ell_j}$ (CRT plus Dirichlet). Then $\ell_j\mid f_j(p)$, but every prime factor of $a_pM_p$ is at least $2p+1>\ell_j$. ∎

**Sieve breaking point.** Sifting $\{a_p\}_{p\le x}$ by primes below $z=o(x)$ costs nothing, by Lemma 3.4. Bounded $\Omega$ needs $z\approx 2^{p/(C+1)}$. In the range $x<Q<2^{x/(C+1)}$ each count $|\{p\le x: Q\mid a_p\}|$ is 0 or 1, so there is no level of distribution to exploit. Details are in `appendix/set_level_routes.md`.

---

## 5. Barrier theorem for bounded-depth arguments

This makes the problem's "fake-model test" rigorous for the two values that matter, $M_p$ and $a_p$. Full proofs are in `appendix/barrier_fake_models.md`.

**Definition 5.1 (axioms $\mathrm{Ax}_{D,J}$).** A family assigns to each prime $p\ge5$ multisets of primes $F(p)$ (a fake $M_p$) and $G(p)$ (a fake $a_p$) such that:
- **(A1) Size.** $\prod F(p)$ has $p$ bits and $\prod G(p)$ has $p-1$ bits. Exact equality of products would force the true factorization, by unique factorization.
- **(A2) Progression.** Every element is $\equiv1\pmod{2p}$.
- **(A3) Mod 8.** The mod-8 rules of Lemma 3.2 hold.
- **(A4) Product congruences.** $\prod F\equiv M_p$ and $\prod G\equiv a_p\pmod{8p^J}$. This includes the Fermat-quotient congruence.
- **(A5) Residues of depth $\le D$.** For $d\le D$ with $d\mid q-1$: $2^{(q-1)/d}\equiv1\pmod q$ iff $d\mid (q-1)/p$ for $F$-primes, or $d\mid(q-1)/2p$ for $G$-primes.
- **(A6)** Disjoint fibres, and 3 lies in no $G(p)$.
- **(A7)** Repeated primes are Wieferich-type.
- **(A8)** Brun–Titchmarsh holds.
- **(A9)** Stewart's lower bound on the largest prime factor holds.

**Theorem 5.2 (barrier; PROVED modulo Siegel–Walfisz, CITED).**
- The true factorizations satisfy every $\mathrm{Ax}_{D,J}$.
- For every $D,J$ there are families satisfying $\mathrm{Ax}_{D,J}$ with $|G(p)|=1$ (so "$\tau(2^p+1)=4$") for all large $p$, and with either:
  - (a) $|F(p)|=1$ for all large $p$, so $\beta_K=0$; or
  - (b) $|F(p)|\ge p^{1-\delta}/4-1$ for all large $p$, so $\beta_K=\infty$.
- One diagonal family satisfies all $\mathrm{Ax}_{D,J}$ at once, eventually in $p$.
- Consequently no deduction from these axioms can decide $\beta_K$. This holds in any consistent extension of ZFC whose extra axioms do not mention $F$ and $G$.

*Construction.*
- $F(p)$ consists of $r$ primes $q_i\equiv1\pmod{2p}$, $q_i\equiv7\pmod8$, $q_i\equiv2\pmod\ell$ for odd $\ell\le D$, up to $\exp(p^\delta)$, plus one filler prime fixing (A1) and (A4).
- $G(p)$ is a single prime in the right class.
- Siegel–Walfisz applies uniformly because the modulus is at most a power of $\log x$.
- The choice $q\equiv 2\pmod\ell$ makes (A5) automatic.

**Proposition 5.3 (sharpness).** Adding exact divisibility ($\prod F\mid M_p$) recovers the truth, since $\prod F>M_p/2$. Also (A4) with $8p^J>2^{p-1}$ forces the exact product. So fake models die only at $p$-adic depth $J\gtrsim p\log2/\log p$, or at residue depth $(q-1)/p$, which is unbounded.

**Lemma 5.4 (a limit of the construction; PROVED).** No product of primes that are all $\equiv7\pmod8$ and $\equiv2\pmod3$ can be $\equiv M_p$ modulo $24$. Indeed $M_p\equiv7\pmod8$ needs an odd number of factors, while $M_p\equiv1\pmod3$ needs an even number. So adding product congruences mod 3 forces genuine Chebotarev conditions in non-abelian Kummer fields, which the construction does not handle (UNPROVED there).

**Corrections to the problem's fake-model paragraph.**
- Its models give $\beta_K=\infty$, not merely $\beta_K\ge\log2$.
- The value $\log 2$ is the composite-exponent benchmark: Zsigmondy gives $\omega(2^n-1)\ge\tau(n)-2$, and Wigert gives $\max\tau$, which yields ratio $\log2$ along highly composite $n$.
- "For every $d$" is proved here only for $d\in\{p,2p\}$.

**Theorem 5.5 (barrier for the constant; PROVED from Bombieri–Vinogradov and Heath-Brown's Linnik bound, CITED).**
- For all $p$ outside a density-zero set, there are fake $F(p)$ of at least $(\tfrac{\log2}{2}-\varepsilon)p/\log p$ primes in $[p^2,p^2(\log p)^{20}]$ satisfying the bounded-depth axioms.
- So no bounded-depth argument can even improve the constant in Lemma 3.5.
- Lemma C in `appendix/second_order_bound.md` (PROVED) shows the improvement is equivalent to bounding the product of the $q\mid M_p$ in $[p^{2-\eta},p^{2+\eta}]$. This is Hooley's middle range in Artin's conjecture.

---

## 6. A genuine obstruction: honest ideals with many prime factors

The fake models violate exact divisibility. The following family does not: it consists of genuine elements of $\mathcal O$.

**Theorem 6.1 (PROVED; Zsigmondy and Wigert CITED).** Let $p\ge5$, $p\nmid k$, and $\alpha_k=2^k-\zeta$. Then:
1. $N(\alpha_k)=\Phi_p(2^k)=\prod_{d\mid k}\Phi_{dp}(2)$ and $\mathcal O/(\alpha_k)\cong\mathbb Z/\Phi_p(2^k)$.
2. Every prime $q\ne p$ dividing $N(\alpha_k)$ has $\operatorname{ord}_q2=dp$ for some $d\mid k$, so $2^k$ has order exactly $p$ mod $q$. Hence $(\alpha_k)=\prod(q,\zeta-2^k)^{v_q}$: degree-1 primes, one above each $q$, principal, with a single generator.
3. Every structural identity used by the class-group, Stickelberger, Galois-orbit and successive-minima approaches holds for $\alpha_k$ exactly as for $\alpha_1=2-\zeta$. These include the sub-ideal dictionary $\mathcal O/I_T\cong\mathbb Z/d_T$, the Stickelberger relation, free Galois orbits of primes, and successive minima pinned in $[1,2^k+1]$.
4. $\omega(\alpha_k)\ge\tau(k)$, by a primitive prime divisor of each $\Phi_{dp}(2)$. Choosing $k<p$ with $\tau(k)$ maximal gives $\limsup\log\omega(\alpha_k)\log\log p/\log p\ge\log2$.

VERIFIED: $p=13$, $k=12$ gives $\omega(\alpha_{12})=13\ge\tau(12)=6$.

**Meaning.** The only datum separating $2-\zeta$ from $\alpha_k$ is quantitative: house 3 against $2^k+1$, or $\log N\approx p$ against $kp$. So a proof must use the *size* of the generator in a way stronger than the norm bound. Every method in §8 uses size only through the norm, and there the bound is Liouville-tight.

Caveat: $\alpha_k$ does not satisfy the analogue of $p\in P_K$, because $N(2^k+\zeta)$ has at least $\tau(\text{odd part of }k)$ factors. By Lemma 8.6, though, the $P_K$ condition enters these methods only through a residue that needs no factorization.

---

## 7. The function-field analogue is true

**Theorem 7.1 (PROVED).** Let $\ell$ be an odd prime, $a\in\mathbb F_\ell[T]$ of degree $d\ge1$, $p\ne\ell$ an odd prime, and $f=\operatorname{ord}_p\ell$. Then:
1. $\omega(a^p-1)\le d\,(1+(p-1)/f)$;
2. $\omega(a^p+1)\ge (p-1)/f$;
3. so $\tau(a^p+1)\le K$ implies $\omega(a^p-1)\le d\,(1+\log_2K)$.

*Proof.*
- (1) A prime $\pi\mid a^p-1$ with $\pi\nmid a-1$ has $a$ of order $p$ in $(\mathbb F_\ell[T]/\pi)^*$, so $f\mid\deg\pi$. The factors of $a^p-1$ off $a-1$ are the norms $N_{\mathbb F_{\ell^f}/\mathbb F_\ell}(a-\eta)$ over the $(p-1)/f$ Frobenius orbits of $\eta\in\mu_p\setminus\{1\}$. Each norm has degree $df$, so each has at most $d$ prime factors. Add at most $d$ factors from $a-1$.
- (2) The norms of $a+\eta$ over distinct orbits are nonconstant. They are pairwise coprime, because $(a+\eta)-(a+\eta')=\eta-\eta'$ is a nonzero constant.
- (3) $2^{(p-1)/f}\le\tau(a^p+1)\le K$. ∎

**Transfer obstruction.** The constant-field Frobenius order $f$ controls both sides. Over $\mathbb Z$, every prime above $q\mid M_p$ and above $Q\mid a_p$ has residue degree 1 in $\mathbb Q(\zeta_p)$, so there is no shared invariant. Data: $p=43,79,191$ have $a_p$ prime and $\omega(M_p)=3,3,5$.

---

## 8. Method-by-method obstructions

Each item gives the strongest correct statement found and the exact point of failure.

**8.1 Incidence/norm lemma (the core exact-divisibility statement; PROVED, independently audited).** For $q\mid M_p$:
- the primes of $\mathcal O$ above $q$ are $\mathfrak q_{q,j}=(q,\zeta-2^j)$, $1\le j\le p-1$, distinct and of degree 1;
- $v_{\mathfrak q_{q,j}}(\zeta-2^j)=v_q(M_p)$.

Hence for $P\in\mathbb Z[x]$ with $\Phi_p\nmid P$:
$$\sum_{j=1}^{p-1}\log\gcd(P(2^j),M_p)\ \le\ \log|N(P(\zeta))|\ \le\ (p-1)\log\|P\|_1 .$$
This fails in the fake models: for a fake $q$, $(q,\zeta-2)=(1)$.

**8.2 Auxiliary polynomials across $q$-adic places.**
- Exact vanishing at $w_q$ forces $\Phi_p^T\mid P$, by irreducibility. That is independent of $S$.
- Approximate vanishing enters only through $\prod q^{e_q}$, never through $|S|$.
- Lattice-existence (Siegel/Minkowski) arguments cannot bound $|S|$ against 8.1. Both sides agree up to a factor $C_K\,p^{O(p)}$ that does not depend on $|S|$.
- HEURISTIC no-go, not a theorem: for $\mathbb Q(\zeta_p)$ the Minkowski constant has $\log C_K\sim\frac12p\log p$, which exceeds $\log M_p$.
- What would be needed is one polynomial vanishing at powers of 2 modulo many $q$ at once. No mechanism forces that, and in the data each trinomial is hit by at most one $q$. This reduces to 8.3.

**8.3 Sparse multiples / Subspace (PROVED parts).**
- Pigeonhole forces $d\mid\sum_{i\le T}\pm2^{e_i}$ for *every* odd $d<\binom pT$, whether or not $d\mid M_p$.
- So the input needed is a uniform bound on $\gcd(u,M_p)$ over sparse $u$. That bound is false. VERIFIED:
  - $\gcd(2+2^{30}-2^{11}-2^{12},M_{43})=9719$, and $43\in P_4$;
  - $\gcd(2+2^{87}-2^{4}-2^{26},M_{223})=196687$.
- Known gcd theorems (Corvaja–Zannier, Bugeaud–Corvaja–Zannier; CITED) are for a fixed number of terms and are ineffective. Pigeonhole needs about $p/\log p$ terms.
- The surviving form is a statement about where the divisors of $M_p$ lie, which is 8.4.

**8.4 Divisor lattices (Lemma O; PROVED, brute-force audited on 197,262 cases).** Let $s>N^\theta$ with $\gcd(s,N)=1$, and let a nonempty set $D'$ of divisors of $N$ meet $R$ classes mod $s$. Then
$$\theta\,\omega(N)\le 1+\log_2R+\log_2(\tau(N)/|D'|).$$
*Proof.* Let $A$ be the product of the $\lfloor\theta\omega\rfloor$ smallest prime-power parts of $N$, so $A\le N^\theta<s$. Divisors $ab$, $a'b$ with $a,a'\mid A$ in one class mod $s$ force $a=a'$. So each class holds at most $\tau(N)/2^{\lfloor\theta\omega\rfloor}$ divisors. ∎

So a "few classes mod $s\ge N^{1/4+\varepsilon}$" input, which is what Lenstra or Coppersmith–Howgrave-Graham–Nagaraj would need, already gives the conclusion up to a factor 4 in $\omega$. That leaves $\beta_K$ unchanged. The input is the problem itself. The candidate moduli ($2^k$; $a_p$, where $de\equiv-2$) only pair classes and give no collapse.

**8.5 $p$-adic symmetric functions (PROVED).** Write $q_i=1+2pm_i$ with multiplicity, $w=\Omega(M_p)$.
- Mod $p^J$, the whole constraint is one equation $\prod(1+2pm_i)\equiv M_p\pmod{p^{J+1}}$ in the cyclic group $1+p\mathbb Z_p \bmod p^{J+1}$, of order $p^J$.
- Its solution set in $(\mathbb Z/p^J)^w$ has exactly $p^{J(w-1)}$ elements, density $p^{-J}$ for every $w$. So no number of factors is ever excluded.
- The individual $e_k$ are not pinned; only $\sum_k(2p)^{k-1}e_k=F$ is.

**8.6 Reciprocity coupling of $2-\zeta$ and $2+\zeta$ (PROVED).**
- $2+\zeta\equiv4$ modulo every prime of $2-\zeta$, a residue that needs no factorization.
- Every power-reciprocity law of any degree between $\alpha=2-\zeta$ and $\beta=2+\zeta$ reduces to local symbols that need neither factorization. This includes degree $(q-1)/p$.
- For $q\mid M_p$ and $n\mid q-1$ with $p\nmid n$, 2 is automatically an $n$-th power mod $q$. So power-residue information sits only at primes $q\equiv1\pmod{2p}$ that do *not* divide $M_p$.
- Additive couplings ($\alpha+\beta=4$; also $(2-\zeta)+(\zeta-1)=1$ with $\zeta-1$ prime) are abc-type. They bound radicals from below, never $\omega$ from above.
- VERIFIED: $J(\chi,\chi)=\bar\chi(4)J(\chi,\rho)$ for all $q<400$.

**8.7 Subgroup methods (PROVED invariance).**
- $\mathbb F_q^*$ is cyclic, so $\langle2\rangle$ is *the* subgroup of order $p$, which depends on $q$ alone.
- Energies, Gauss/Heilbronn sums and $|H\cap(H+a)|$ are therefore identical for every prime $q\equiv1\pmod{2p}$. So are the bounds of Stepanov, Heath-Brown–Konyagin, Bourgain–Glibichuk–Konyagin and sum–product.
- The 2-dependent versions use exact divisibility but are quantitatively weaker than the trivial bound. Sparse coincidences give $\sum_{q\mid M_p}1/q\ll p/\log p$. The large sieve with $\chi(2)=1$ loses a factor $R/\log R$.
- Stewart (Acta Math. 2013; CITED) bounds multiplicities and forces a large prime factor, but does not bound $\omega$.

**8.8 Interpolation of $2^z$ (PROVED).**
- Schneider–Lang does not apply, because derivatives bring in $\log2$ and $\log_q2$, which are not values of one algebraic number.
- The $q$-adic Schwarz-lemma step $\Delta^sG(0)\equiv0\pmod{M^{\max(0,s-L_1)}}$ holds for every exponent, prime or composite. So it fails the composite calibration ($\omega(2^n-1)\ge\tau(n)-2$).
- The remaining input is the condition of 8.3.

**8.9 Kummer–Chebotarev.** $q\mid M_p$ iff $q$ splits completely in $\mathbb Q(\zeta_m,2^{1/m})$ with $m=(q-1)/p$. The degree is about $m^2\approx(q/p)^2$, which grows with $q$, and for each $m$ there is only one candidate $q$. Lagarias–Odlyzko (CITED) is useless here even under GRH.

### The single open estimate

Every route above stops at:

> For $p\in P_K$ (or all $p$), $\#\{q\le 2^p:\ q\equiv1\ (2p),\ 2^p\equiv1\ (q)\}\le\exp(o(\log p/\log\log p))$.

Known: $(\tfrac{\log 2}{2}+o(1))p/\log p$ (Lemma 3.5). Nothing better is known pointwise, even $o(p/\log p)$, as far as recalled without literature access. Heuristic truth: about $C\log p$, the Poisson model, which would give $\beta_K=0$ (HEURISTIC). By §5 and §6, such a bound must use exact divisibility of unbounded depth *and* the smallness of the generator $2-\zeta$ beyond its norm.

Exhaustive search (VERIFIED, all $p\le6000$): the number of $q\le p^2$ dividing $M_p$ is at most 4, reached at $p=397$. The mean is 0.57, while the extremal configuration would have about 236.

---

## 9. Corrections to the problem statement

1. **False.** "For all $d\le600$: $\max\omega(\Phi_d(2))=8$." In fact
   $M_{397}=2383\cdot6353\cdot50023\cdot53993\cdot202471\cdot5877983\cdot814132872808522587940886856743\cdot1234904213576000272542841146073\cdot6597485910270326519900042655193.$
   VERIFIED: the product is exactly $2^{397}-1$. All factors are $\equiv1\pmod{794}$, pairwise coprime, and strong probable primes to 35 bases. $\omega\ge9$ holds without primality proofs, because the 61-digit product of the two largest pieces was split. $\Phi_{333}(2)$ has 8 prime factors. 332 values of $d\le600$ were not fully factored, so the true maximum is $\ge9$ and unknown.
2. **Too strong.** Direction D says the elementary symmetric functions of the $m_q$ are fixed by the $p$-adic digits of $M_p$. Only $\sum_k(2p)^{k-1}e_k=F$ is fixed (§8.5).
3. **Imprecise.** "$(2+\zeta_p)$ has at most $\log_2(K/2)$ prime-ideal factors" holds for distinct factors. With multiplicity the bound is $K/2-1$.
4. **Fake-model paragraph.** See §5: the models give $\beta_K=\infty$, the $\log2$ is the composite benchmark, and "every $d$" is unproved.
5. **Brun–Titchmarsh** is not needed for the $\frac{\log2}{2}p/\log p$ bound (Lemma 3.5).

## 10. Data verification

- The table $(p,\tau(2^p+1),\omega(M_p))$ matches exactly for 57 of 61 primes, with both sides fully factored.
- The other four are consistent but partly factored:
  - $p=239$: $\tau\ge16$;
  - $p=257$: $\omega\ge3$;
  - $p=277$: $\omega\ge3$;
  - $p=293$: $\tau\ge64$.
- "$\omega(M_p)\le5$ on $P_4$, $p\le293$" is confirmed; the maximum is 5, at $p=191$.
- Wagstaff exponents $3<p\le2000$, found by PRP: 5, 7, 11, 13, 17, 19, 23, 31, 43, 61, 79, 101, 127, 167, 191, 199, 313, 347, 701, 1709.
- The Fermat-quotient congruence holds on every fully factored $M_p$.
- Every $\tau(2^p+1)$ in the table is $\equiv0\pmod4$, as Corollary 3.3 requires.

Primes above about $3\cdot10^{24}$ were certified only as BPSW or strong probable primes.

## 11. Audit log of this note

| Check | Result |
|---|---|
| Fake-model test | The only exact-divisibility steps found are 8.1 and its descendants. Theorem 5.2 proves bounded-depth arguments cannot decide $\beta_K$. Theorem 6.1 shows exact divisibility at the ideal level is still insufficient without a size input beyond the norm. No step of a proof exists to name, because there is no proof. |
| Unconditional | All PROVED items are unconditional. Siegel–Walfisz and Bombieri–Vinogradov are used only in the barrier constructions. GRH appears only in a no-go remark. |
| Uniformity | Constants are explicit in §3, 4, 7 and 8.4–8.6. The barrier constructions are ineffective (Siegel–Walfisz), which is acceptable for an existence result. |
| Citations | Stated from memory without literature access. Theorem numbers are unverified (Washington Ch. 6; Montgomery–Vaughan 1973; Heath-Brown 1992; Stewart 2013; Lenstra 1984; Coppersmith–Howgrave-Graham–Nagaraj 2008). |
| Data | §10. One false statement in the problem was found (§9.1). |
| Hostile re-read | An independent audit of 12 core claims found none false. Two repairs were made: 8.2 is labelled heuristic, and the Wagstaff list is stated for $p>3$. |

## 12. Conclusion

$\beta_K$ is not determined here. The disproof direction provably requires an infinite family of composite Mersenne numbers with $p$ prime that are also near-Wagstaff, which is open. The proof direction requires a pointwise bound on $\omega(M_p)$ that is subpolynomial in $p$, where nothing better than $\frac{\log2}{2}p/\log p$ is known. By Theorems 5.2 and 6.1, such a bound must exploit exact divisibility of unbounded depth together with the archimedean smallness of $2-\zeta_p$ beyond its norm. No current technique does both. The heuristic evidence (Poisson model, data up to $p\le6000$, and the true function-field analogue, Theorem 7.1) supports the conjecture $\beta_K=0$.

---

### Appendix files (`mersenne_omega_appendix/`)

- `barrier_fake_models.md`: axioms, constructions, Theorem 5.2, Proposition 5.3, Lemma 5.4.
- `second_order_bound.md`: second-order trivial bound, concentration Lemma C, Theorem 5.5, breaking points D1–D7.
- `interpolation_and_function_field.md`: §8.8 and Theorem 7.1.
- `padic_and_reciprocity.md`: §8.5 and §8.6.
- `set_level_routes.md`: §4.
- `scripts/`: verification scripts (Python 3, no dependencies). Some write their output to the original scratch locations.
