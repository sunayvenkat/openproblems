# Fake factorization models and a relativization barrier for $\beta_K$

Status labels: **PROVED** (complete proof here, modulo explicitly CITED results), **CITED** (exact statement + reference + hypotheses checked; references are from memory — no internet was available — so theorem/equation *numbers* are flagged where I am not sure), **UNPROVED** (sketch / claim not established here).

Notation: $p\ge5$ prime, $M_p=2^p-1$, $\Phi:=\Phi_{2p}(2)=(2^p+1)/3$. $\mathrm{bl}(N)=\lfloor\log_2N\rfloor+1$ (bit length). $P_D:=\prod_{3\le \ell\le D,\ \ell\text{ prime}}\ell$ (empty product $=1$). $\mathrm{li}(x)=\int_2^x dt/\log t$.

---

## 0. Cited results

**[SW] Siegel–Walfisz.** For every $A>0$ there are constants $C_A,c_A>0$ (ineffective) such that for all $x\ge2$, all integers $1\le k\le(\log x)^A$ and all $a$ with $\gcd(a,k)=1$:
$|\pi(x;k,a)-\mathrm{li}(x)/\varphi(k)|\le C_A\,x\exp(-c_A\sqrt{\log x})$.
Ref: Davenport, *Multiplicative Number Theory*, 3rd ed., GTM 74, Ch. 22 (stated there for $\psi$; the $\pi$-form follows by partial summation); Iwaniec–Kowalski, *Analytic Number Theory*, §5.9 (Cor. 5.29 — number from memory). Hypothesis to check at each use: $k\le(\log x)^A$, $\gcd(a,k)=1$.

**Consequence [SW′] (PROVED from SW).** Fix $A$. If $y\ge y_0(A)$, $k\le(\log y)^A$, $\gcd(a,k)=1$, then
$\pi(2y;k,a)-\pi(y;k,a)\ \ge\ \dfrac{y}{2k\log 2y}.$
*Proof.* $k\le(\log y)^A\le(\log 2y)^A$, so SW applies at $y$ and $2y$: the difference is $\ge(\mathrm{li}(2y)-\mathrm{li}(y))/\varphi(k)-3C_Ay\,e^{-c_A\sqrt{\log y}}\ge \frac{y}{k\log 2y}-3C_Ay\,e^{-c_A\sqrt{\log y}}$, and $6C_A k\log(2y)\le 6C_A(\log 2y)^{A+1}\le e^{c_A\sqrt{\log y}}$ for $y\ge y_0(A)$. $\square$ Similarly $\pi(x;k,a)\ge x/(2k\log x)$ for $x\ge x_0(A)$, $k\le(\log x)^A$.

**[MV] Brun–Titchmarsh (Montgomery–Vaughan).** For integers $1\le k<y$, any $a$ and $x\ge0$: $\pi(x+y;k,a)-\pi(x;k,a)<2y/(\varphi(k)\log(y/k))$. Ref: Montgomery–Vaughan, *The large sieve*, Mathematika 20 (1973) 119–134, Thm 2.

**[BV] Bombieri–Vinogradov.** For every $A>0$ there is $B=B(A)$ with $\sum_{k\le x^{1/2}(\log x)^{-B}}\max_{(a,k)=1}|\pi(x;k,a)-\mathrm{li}(x)/\varphi(k)|\ll_A x(\log x)^{-A}$. Ref: Davenport Ch. 28; Iwaniec–Kowalski Thm 17.1. (Used only in Remark 4.6.)

**[BZ] Bang–Zsigmondy.** For $n\ge2$, $n\ne6$, $2^n-1$ has a prime factor not dividing $2^m-1$ for any $1\le m<n$.

**[St] Stewart** (Acta Math. 211 (2013) 291–314), in the form quoted by the prompt: $P(2^n-1)>n\exp(\log n/(104\log\log n))$ for $n\ge n_S$. (Only enters as an axiom; models satisfy far stronger bounds directly.)

**[HW] ** $\tau(m)\ll_\varepsilon m^\varepsilon$ (Hardy–Wright, Thm 315). **[QR]** Euler's criterion and $(\tfrac2q)=1\iff q\equiv\pm1\pmod 8$. **[PNT]** $\theta(x)\sim x$.

---

## 1. True arithmetic facts (all PROVED, elementary)

**Lemma 1.1.** If $q\mid M_p$ then $\mathrm{ord}_q2=p$, $q\equiv1\pmod{2p}$, $q\equiv\pm1\pmod8$.
*Proof.* $\mathrm{ord}\mid p$, $\ne1$. $p\mid q-1$, $q$ odd. $2=(2^{(p+1)/2})^2$ is a QR, so [QR]. $\square$

**Lemma 1.2.** For $p\ge5$: $3\nmid\Phi$, $\Phi\equiv1\pmod p$, $\Phi\equiv3\pmod8$, $\mathrm{bl}(\Phi)=p-1$, $\mathrm{bl}(M_p)=p$. If $q\mid\Phi$ then $\mathrm{ord}_q2=2p$, $q\equiv1\pmod{2p}$, and with $m=(q-1)/(2p)$: $q\equiv1\pmod 8$ if $m$ even, $q\equiv3\pmod8$ if $m$ odd.
*Proof.* $v_3(2^p+1)=v_3(3)+v_3(p)=1$ (LTE, $p\ne3$). $2^p+1\equiv3\pmod p$ so $\Phi\equiv1$. $2^p+1\equiv1\pmod8$, $3^{-1}\equiv3$, so $\Phi\equiv3$. $2^{p-2}<\Phi<2^{p-1}$. If $q\mid\Phi$: $2^p\equiv-1$, so $\mathrm{ord}\in\{2,2p\}$; $\mathrm{ord}=2$ forces $q=3$, excluded. $-2=2^{p+1}$ is a square mod $q$, so $q\equiv1,3\pmod8$; $m$ even $\iff q\equiv1\pmod 4$. $\square$

**Lemma 1.3 (depth identity).** Let $q$ be prime, $n=\mathrm{ord}_q2$. For every $d\mid q-1$: $2^{(q-1)/d}\equiv1\pmod q\iff d\mid (q-1)/n$.
*Proof.* $2^{(q-1)/d}\equiv1\iff n\mid (q-1)/d\iff nd\mid q-1$. $\square$
*Converse (exact divisibility = unbounded depth).* Let $q\equiv1\pmod p$ be prime and $d=(q-1)/p$. The implication "$d\mid(q-1)/p\Rightarrow 2^{(q-1)/d}\equiv1\pmod q$" (whose hypothesis is trivially true) says exactly $2^p\equiv1$, i.e. $q\mid M_p$. So the residue condition at depth $d=(q-1)/p$ **is** exact divisibility.

**Lemma 1.4.** Each prime lies in at most one of the sets $\{q\mid M_p\}$, $\{q\mid\Phi_{2p}(2)\}$ ($p\ge5$ prime) — its order determines $p$ and the side. If $q^2\mid M_p$ or $q^2\mid\Phi_{2p}(2)$ then $2^{q-1}\equiv1\pmod{q^2}$ (since $\mathrm{ord}_{q^2}2\mid 2p\mid q-1$).

**Lemma 1.5 (Mod-24 obstruction).** If every prime factor $q$ of $M_p$ satisfied $q\equiv7\pmod8$ and $q\equiv2\pmod3$, then with $N=\Omega(M_p)$: $M_p\equiv7^N\pmod8$ forces $N$ odd, $M_p\equiv1\pmod3$ ($p$ odd) forces $2^N\equiv1$, $N$ even — contradiction. Hence **some $q\mid M_p$ has $q\equiv1\pmod3$ or $q\equiv1\pmod8$**; by Lemma 1.3 such $q$ has $2$ a cubic residue (resp. an 8th-power residue, as $8\mid(q-1)/p$). For a fake family obeying (A5) with $D\ge4$, such a prime must satisfy a cubic resp. quartic residue condition — a Chebotarev condition in $\mathbb Q(\zeta_3,2^{1/3})$ resp. $\mathbb Q(\zeta_8,2^{1/4})$ (non-abelian, so not a congruence condition). (For $D\le3$ a prime $\equiv1\pmod 8$, $\not\equiv1\pmod3$ only needs $(\frac2q)=1$, a congruence.) Same argument applies to any multiset satisfying (A2),(A3) below and $\prod\equiv M_p\pmod{24}$. (Checked numerically for $p\le89$: `check_models.py`.)

---

## 2. The axiom system $\mathrm{Ax}_{D,J}$

A **family** is a pair $(F,G)$ of maps assigning to each prime $p\ge5$ finite nonempty multisets $F(p),G(p)$ of primes. Write $\Pi F(p)$ for the product with multiplicity, $\omega_F(p)$ for the number of distinct elements, $\tau_G(p):=2\tau(\Pi G(p))$, $P_K(G)=\{p:\tau_G(p)\le K\}$,
$\beta_K(F,G)=\limsup_{p\to\infty,\,p\in P_K(G)}\log\omega_F(p)\log\log p/\log p$ ($:=0$ if $P_K(G)$ finite).
The **true family** $T=(F_T,G_T)$: prime factorizations of $M_p$ and $\Phi_{2p}(2)$. Since $\tau(2^p+1)=2\tau(\Phi)$ for $p>3$, $\beta_K(T)=\beta_K$.

**On "same size".** Exact equality $\Pi F(p)=M_p$ forces $F(p)=F_T(p)$ by unique factorization, so "same size" must be relaxed. We use **same bit length** (equivalently: within a factor $<2$ of a fixed dyadic window).

$\mathrm{Ax}_{D,J}(F,G)$ ($D,J\ge1$ fixed integers) is the conjunction over all primes $p\ge5$ of:

- **(A1) size:** $\mathrm{bl}(\Pi F(p))=p$, $\mathrm{bl}(\Pi G(p))=p-1$.
- **(A2) congruence:** every $q\in F(p)\cup G(p)$ has $q\equiv1\pmod{2p}$.
- **(A3) mod 8:** $q\in F(p)\Rightarrow q\equiv\pm1\pmod8$; $q\in G(p)\Rightarrow q\equiv1\pmod8$ if $(q-1)/2p$ even, $q\equiv3\pmod8$ if odd.
- **(A4) product congruences (bounded $p$-adic depth; includes the Fermat-quotient congruence at $J=2$ and the overall $\Phi\equiv3\pmod8$):** $\Pi F(p)\equiv M_p$ and $\Pi G(p)\equiv\Phi_{2p}(2)\pmod{8p^J}$.
- **(A5) power residues of depth $\le D$:** for $q\in F(p)$ (resp. $G(p)$) and every $d\le D$ with $d\mid q-1$: $2^{(q-1)/d}\equiv1\pmod q\iff d\mid (q-1)/p$ (resp. $d\mid(q-1)/2p$).
- **(A6) primitivity / disjoint fibres:** all the sets $F(p),G(p)$ ($p\ge5$) are pairwise disjoint; $3\notin G(p)$.
- **(A7) multiplicities (LTE/Wieferich):** if $q$ occurs in $F(p)$ or $G(p)$ with multiplicity $\ge2$ then $2^{q-1}\equiv1\pmod{q^2}$. (For the restricted family $d\in\{p,2p\}$, LTE $v_q(2^{2p}-1)=v_q(M_p)$ for $q\in F(p)$ is equivalent to $q\notin G(p)\cup\{3\}$, contained in (A6).)
- **(A8) Brun–Titchmarsh:** $\#\{q\in F(p)\cup G(p)\text{ distinct}:q\le y\}<2y/((p-1)\log(y/2p))$ for $y>2p$.
- **(A9) Stewart:** for $p\ge n_S$: $\max F(p)>p\,e^{\log p/(104\log\log p)}$ and $\max(F(p)\cup G(p))>2p\,e^{\log 2p/(104\log\log 2p)}$.

Remarks. (A3) is the $d=2$ case of (A5) plus [QR] and (A2). (A8) is implied by (A2)+(A6)+[MV]. Aurifeuillian splitting concerns $2^{4k+2}+1$, not $2^p\pm1$ with $p$ odd: vacuous here. Zsigmondy primitivity = nonemptiness + (A6).

**Theorem 2.1 (PROVED, using [St], [MV]).** $T$ satisfies $\mathrm{Ax}_{D,J}$ for all $D,J$.
*Proof.* (A1),(A4): exact products, Lemma 1.2. (A2),(A3): Lemmas 1.1–1.2. (A5): Lemma 1.3 with $n=p$ resp. $2p$. (A6),(A7): Lemma 1.4. (A8): distinct prime factors are $\equiv1\pmod{2p}$, use [MV] with $x=0,k=2p$. (A9): [St] at $n=p$ and $n=2p$ ($P(2^{2p}-1)=\max(3,P(M_p),P(\Phi))$). $\square$

---

## 3. Key lemma: admissible primes (PROVED from SW)

Fix $D,J\ge1$. For $p>D$ let $k=8p^JP_D$; $\gcd(8p^J,P_D)=1$.

**Lemma 3.1.** There is $p_1=p_1(D,J)$ (ineffective) such that for every prime $p\ge p_1$, every $b$ mod $8p^J$ with $b\equiv1\pmod p$ and $b\equiv3\pmod4$, every real $y$ with $p/12\le\log y\le p$, and every set $U$ of at most $p^3$ integers, there is a prime $Q\in[y,2y)\setminus U$ with $Q\equiv b\pmod{8p^J}$ and $Q\equiv2\pmod\ell$ for all primes $3\le\ell\le D$.
*Proof.* By CRT these conditions define one class $c$ mod $k$, and $\gcd(c,k)=1$ ($b$ odd, $b\equiv1\pmod p$, $2\not\equiv0\pmod\ell$). $k\le 8P_Dp^J\le (p/12)^{J+2}\le(\log y)^{J+2}$ for $p\ge p'(D,J)$. [SW′] with $A=J+2$: at least $y/(2k\log2y)\ge e^{p/12}/(16P_Dp^J(p+1))>p^3$ such primes once $p$ is large. $\square$

**Lemma 3.2.** Fix also $\delta\in(0,1)$, $x=x_p=\exp(p^\delta)$. For $p\ge p_2(D,\delta)$ and $|U|\le p^3$ there are at least $p$ primes $q\le x$, $q\notin U$, with $q\equiv1\pmod{2p}$, $q\equiv7\pmod8$, $q\equiv2\pmod\ell$ ($3\le\ell\le D$).
*Proof.* One class mod $k_0=8pP_D$; $k_0\le p^2=(\log x)^{2/\delta}$ for large $p$; SW with $A=2/\delta$ gives $\ge x/(2k_0\log x)=e^{p^\delta}/(16P_Dp^{1+\delta})>p^3+p$. $\square$

**Lemma 3.3 (depth check).** Let $p>D$, $n\in\{p,2p\}$, $q$ prime with $q\equiv1\pmod n$, $q\equiv3\pmod4$, $q\not\equiv1\pmod\ell$ for all primes $3\le\ell\le D$, and $q\equiv7\pmod8$ if $n=p$, $q\equiv3\pmod8$ if $n=2p$. Then $q$ satisfies (A5) (with $n$) and (A3).
*Proof.* Let $d\le D$, $d\mid q-1$. $\gcd(d,p)=1$. An odd prime $\ell\mid d$ would give $q\equiv1\pmod\ell$; $4\nmid q-1$. So $d\in\{1,2\}$. $d=1$: both sides true. $d=2$: LHS $\iff(\frac2q)=1$ (Euler). RHS: $q-1\equiv2\pmod4$, so $(q-1)/p$ is even and $(q-1)/2p$ is odd. For $n=p$, $q\equiv7$: both true; for $n=2p$, $q\equiv3$: both false. (A3) is immediate ($m=(q-1)/2p$ odd, $q\equiv3$). $\square$

---

## 4. The models

Fix $D,J\ge1$ and $p_*:=\max(p_1,p_2,n_S,D+1,\dots)$ large. For primes $p<p_*$ set $(F,G)(p):=T(p)$ (truth). For $p\ge p_*$ in increasing order, let $U_p$ = all primes used at earlier stages (true ones for $p<p_*$, fake ones after). $|U_p|\le\sum_{p'<p}(p'+2)+\sum_{p'<p_*}p'\le p^3$ (each stage uses $\le p'+2$ primes; true $\omega\le p'$).

**Construction $\mathcal M^{r}$.** Given an even $r=r(p)$ with $0\le r\le p^{1-\delta}/4$:
1. (small primes) pick $q_1,\dots,q_r$ distinct from Lemma 3.2 avoiding $U_p$; $R=\prod q_i\le x^r\le e^{p/4}$.
2. (filler) $y=2^{p-1}/R$, so $\log y\ge(p-1)\log2-p/4\ge p/12$ and $\le p$. Take $b\equiv M_pR^{-1}\pmod{8p^J}$: $b\equiv1\pmod p$ ($M_p\equiv R\equiv1$), $b\equiv7\cdot7^{-r}\equiv7\pmod8$ ($r$ even). Lemma 3.1 gives prime $Q'\in[y,2y)\setminus(U_p\cup\{q_i\})$. $F(p)=\{q_1,\dots,q_r,Q'\}$.
3. (G) $y=2^{p-2}$, $b\equiv\Phi_{2p}(2)\pmod{8p^J}$ ($\equiv1\pmod p$, $\equiv3\pmod8$); Lemma 3.1 gives prime $Q\in[2^{p-2},2^{p-1})$ avoiding everything used; $G(p)=\{Q\}$.

**Theorem 4.1 (PROVED, modulo SW).** For every $D,J,\delta$ and every choice of even $r(p)\in[0,p^{1-\delta}/4]$, $\mathcal M^r$ satisfies $\mathrm{Ax}_{D,J}$, and for $p\ge p_*$: $G(p)$ is one prime, $\tau_G(p)=4$ (so $P_K\supseteq\{p\ge p_*\}$ for all $K\ge4$), $\omega_F(p)=r(p)+1$.
*Proof.* $p<p_*$: Theorem 2.1 (and (A6) across the boundary by avoidance of $U_p$). $p\ge p_*$: (A1) $RQ'\in[2^{p-1},2^p)$, $Q\in[2^{p-2},2^{p-1})$. (A2) all chosen primes are $\equiv1\pmod p$ and odd. (A4) $RQ'\equiv RM_pR^{-1}$, $Q\equiv\Phi$. (A3),(A5): Lemma 3.3 — all $F$-primes are $\equiv7\pmod 8$ and $\equiv2\pmod\ell$, $Q\equiv3\pmod8$, $\equiv2\pmod\ell$ ($b\equiv3\pmod 8\Rightarrow\equiv3\pmod4$). (A6) avoidance of $U_p$; within a stage $F$-primes are $7\bmod8$ and $Q$ is $3\bmod8$; all exceed $2p>3$. (A7) squarefree: vacuous. (A8) from (A2)+[MV]. (A9) $\max F(p)\ge Q'\ge e^{p/12}>p^2$, $Q\ge2^{p-2}$, both exceed Stewart's bound for large $p$. $\square$

**Corollary 4.2 ($\beta=0$ model).** $r\equiv0$: $\omega_F(p)=1$ for $p\ge p_*$, so $\beta_K(\mathcal M^0)=0$ for every $K\ge4$ with $P_K$ cofinite in the primes.

**Corollary 4.3 ($\beta=\infty$ model).** $r=2\lfloor p^{1-\delta}/8\rfloor$: $\omega_F(p)\ge p^{1-\delta}/4-1$ for **all** $p\ge p_*$, and $\tau_G(p)=4$. Hence $\log\omega_F\cdot\log\log p/\log p\ge(1-\delta+o(1))\log\log p\to\infty$: $\beta_K(\mathcal M^r)=\infty$ for every $K\ge4$. In particular $\omega_F(p)\ge\max_{m\le2p}\tau(m)/(\log p)^3$ for all large $p$ (by [HW], $\max_{m\le2p}\tau(m)\le C_\varepsilon(2p)^\varepsilon$).

**Uniformity notes.** The only analytic input is SW at modulus $k\asymp p^{J}$ against $x$ with $\log x\ge p^\delta$ (small primes) or $\log x\asymp p$ (fillers) — always $k\le(\log x)^{A}$ with $A=2/\delta$ or $J+2$. No individual-modulus result at $x=p^{O(1)}$ is needed: the trick is to take the "small" primes up to $\exp(p^\delta)$, which still allows $p^{1-\delta}$ of them inside $2^{p/2}$. Thresholds $p_*$ are ineffective (Siegel); this is harmless for existence.

**Proposition 4.4 (diagonal model; PROVED mod SW).** WLOG $p_*(j)$ (for $D=J=j$, $\delta=\tfrac12$) is increasing in $j$, $>j$. Put $j(p)=\max\{j:p_*(j)\le p\}$ and use parameters $D=J=j(p)$ at stage $p$ (truth for $p<p_*(1)$). The bound $|U_p|\le p^3$ is history-independent, so the construction runs. Result: one family satisfying, for **every** $(D,J)$, all clauses of $\mathrm{Ax}_{D,J}$ at all $p\ge p_*(\max(D,J))$ (depth $\le j(p)$ implies depth $\le D$; mod $8p^{j(p)}$ implies mod $8p^J$), with $\tau_G=4$ and $\omega_F\ge p^{1/2}/4-1$ (or $\omega_F=1$).

**Proposition 4.5 (thresholds; PROVED).** (a) If $8p^J>2^{p-1}$, then (A1)+(A4) force $\Pi F(p)=M_p$ (two integers in $[2^{p-1},2^p)$ congruent mod $N>2^{p-1}$ are equal), hence $F(p)=F_T(p)$; same for $G$. So fake models die at $p$-adic depth $J\ge(p-1)\log2/\log p+O(1)$. (b) Models exist for $J$ fixed or $J(p)\to\infty$ (Prop. 4.4, arbitrarily slowly). (c) **UNPROVED/open here:** existence for $J(p)$ in between, e.g. $J(p)\asymp p/\log p\cdot c$ with $c<\log 2$ — needs primes in a dyadic interval near $2^p$ in a progression of modulus $2^{cp}$ for an individual modulus (GRH would give $c<1/2$; not allowed).

**Remark 4.6 (saturating BT; PROVED mod BV).** For dyadic $P$, $x=(2P)^4$, $k_p=8pP_D$ ($p\in(P,2P]$), distinct and $\le x^{1/2}(\log x)^{-B}$. If $p$ is *bad*, i.e. $\pi(x;k_p,c_p)<\mathrm{li}(x)/2\varphi(k_p)$, the BV summand is $\ge x/(32P_DP\log x)$; BV with $A=3$ gives $\#\text{bad}\ll P/(\log P)^2$. For good $p$ there are $\gg P^3/\log P$ admissible primes $\le x$, far more than $r+|U_p|$ (the actual used count is $\le 2p^2+2p$), so one may take even $r\asymp p/\log p$ ($r\le p/(16\log 2p)$ keeps $R\le(2p)^{4r}\le e^{p/4}$, so the filler step is unchanged). Hence a model with $\omega_F(p)\gg p/\log p$ on a set of primes of relative density 1 (bad $p$: $r=0$). For *all* $p$ one would need a quantitative Linnik theorem ($\pi(x;k,a)\gg x/(\varphi(k)\sqrt k\log x)$ for $x\ge k^L$; I believe this is in IK Ch. 18 / Heath-Brown 1992 but cannot verify the exact statement offline — UNPROVED here). Note also the *true* upper bound: $\omega(M_p)\le(\tfrac{\log2}2+o(1))p/\log p$ follows from size + (A2) **without** BT: at most $y/2p+1$ integers $\equiv1\pmod{2p}$ lie below $y=p^{2-\varepsilon}$, $\varepsilon=1/\log\log p$, and the rest are $\ge y$ (PROVED). So the prompt's attribution to BT is unnecessary (harmless).

---

## 5. The relativization barrier

Work in ZFC (or any consistent $T'\supseteq$ ZFC — e.g. ZFC + GRH + Schinzel's H: extra axioms not mentioning the family variables). $\mathrm{Ax}_{D,J}(F,G)$ and $\varphi_K(F,G):\equiv$ "$\beta_K(F,G)=0$" are formulas of set theory with free variables $F,G$. "Deducing $\beta_K=0$ from the listed properties alone" means proving $\Theta_K^{D,J}:\ \forall F,G\,[\mathrm{Ax}_{D,J}(F,G)\to\varphi_K(F,G)]$ (then specialize to $T$ via Thm 2.1).

**Theorem 5.1 (Barrier; PROVED mod SW).** For all $K\ge4$, $D,J\ge1$: ZFC $\vdash\neg\Theta^{D,J}_K$ and ZFC $\vdash\neg\forall F,G[\mathrm{Ax}_{D,J}\to\neg\varphi_K]$. Hence, if $T'$ is consistent, $T'$ proves neither "$\mathrm{Ax}_{D,J}\Rightarrow\beta_K=0$" nor "$\mathrm{Ax}_{D,J}\Rightarrow\beta_K>0$". The same holds with "$\beta_K>0$" replaced by "$\beta_K\ge c$" for any $c>0$, and with $P_K$ required infinite (both models have $P_4$ cofinite).
*Proof.* Theorem 4.1/Cor. 4.3 is a ZFC proof (SW is a ZFC theorem) of $\exists F,G[\mathrm{Ax}_{D,J}\wedge\beta_K=\infty]$; Cor. 4.2 of $\exists F,G[\mathrm{Ax}_{D,J}\wedge\beta_K=0]$. $\square$

**Corollary 5.2 (schemes).** (i) For the scheme $\Sigma_{\rm fin}=\{\mathrm{Ax}_{D,J}:D,J\in\mathbb N\}$ (each a separate axiom): a proof uses finitely many, all implied by one $\mathrm{Ax}_{D,J}$ ($\mathrm{Ax}_{D,J}\Rightarrow\mathrm{Ax}_{D',J'}$ for $D'\le D,J'\le J$), so 5.1 applies. (ii) For the single "eventual" axiom $\forall D,J\,\exists p_0\,\forall p\ge p_0$ [clauses of $\mathrm{Ax}_{D,J}$ at $p$]: Prop. 4.4 supplies both models. (iii) Adding any property $\Pi$ with ZFC $\vdash \mathrm{Ax}_{D,J}\to\Pi$ (e.g. the BT upper bound, the trivial bound, Fermat-quotient congruence) changes nothing.

**Proposition 5.3 (sharpness: what must be used; PROVED).** Let $E$ = exact divisibility: $v_q(\Pi F(p))\le v_q(M_p)$, $v_q(\Pi G(p))\le v_q(\Phi)$ for all $q$. Then $\mathrm{Ax}_{1,1}+E$ forces $(F,G)=T$ ($\Pi F\mid M_p$ and $\Pi F\ge2^{p-1}>M_p/2$). The unbounded-depth version of (A5) ($D=\infty$) already gives $F(p)\subseteq\{q\mid M_p\}$ (Lemma 1.3, converse), hence $\omega_F\le\omega(M_p)$ — it kills the $\beta=\infty$ models. So any proof of $\beta_K=0$ must contain a step that is false in $\mathcal M^r$ — necessarily one using depth $\to\infty$ (or $p$-adic precision $J\gtrsim p/\log p$, Prop. 4.5(a)), i.e. exact divisibility. Examples of true properties false in the models: the dictionary $\mathbb Z[\zeta_p]/(2-\zeta_p)\cong\mathbb Z/M_p$ *applied to $F$*, $3\Pi G=\Pi F+2$, full $p$-adic digits (Direction D at unbounded precision). The prompt's "only exact divisibility is violated" is informal; the precise content is Prop. 5.3.

---

## 6. Verdict on the prompt's fake-model claims

1. "Models with $\tau(2^p+1)$ bounded and $\omega\ge\max_{m\le2p}\tau(m)/(\log p)^3$ for infinitely many $p$": **VERIFIED, strengthened** (all large $p$, $\omega\ge p^{1-\delta}/4-1$), for the restricted family $d\in\{p,2p\}$ under $\mathrm{Ax}_{D,J}$.
2. "In those models $\beta_K\ge\log2$": **VERIFIED but not sharp** — models give $\beta_K=\infty$. $\log2$ is not a feature of the axioms.
3. "Models with $\beta_K=0$ also exist": **VERIFIED** ($\omega_F=1$).
4. "For every $d$": **UNPROVED here.** Sketch: fake all $\Phi_d(2)$, $d\ge d_0$, in increasing $d$; include the non-primitive prime $q$ in $\Phi_{nq^k}(2)$ when $q$ is in the fake fibre of $n$; Aurifeuillian $d$ get two fillers; SW applies since $\log\Phi_d(2)\asymp\varphi(d)\gg d/\log\log d$ and moduli $\asymp d^J$. Bookkeeping not checked.
5. "Every congruence or power-residue condition of bounded depth": **PROVED for** residue conditions of depth $\le D$ plus product congruences mod $8p^J$. **Not covered:** product congruences mod other fixed moduli together with depth $D\ge4$. Lemma 1.5 shows mod 24 + (A3) forces a prime $\equiv1\pmod3$ (2 a cubic residue) or $\equiv1\pmod8$ (2 a quartic, and for $D\ge8$ 8th-power, residue): genuine Chebotarev conditions in fixed Kummer fields, combined with conductor $\asymp p^J$ at $x\approx2^p$. Lagarias–Odlyzko is useless here (needs $\log x\gg n_L(\log d_L)^2$, with $n_L\asymp p^J$). Siegel–Walfisz for Hecke characters of a fixed number field (L. J. Goldstein, Trans. AMS 149 (1970) — statement not verified offline) should handle it: **UNPROVED here**.
6. Mod-8 facts ($F$: $\pm1$; $G$: $1$ or $3$ with $3\iff m$ odd; $\Phi\equiv3$): **PROVED** (Lemmas 1.1–1.2).

## 7. Calibration (composite $n$)

**PROVED (with [BZ], [PNT]).** For $n\ge2$: the $\Phi_d(2)$, $d\mid n$, have pairwise distinct primitive primes for $d\notin\{1,6\}$, so $\omega(2^n-1)\ge\tau(n)-2$. For primorials $n_k=\prod_{i\le k}p_i$: $\tau=2^k$, $\log n_k=\theta(p_k)\sim p_k$, $k\sim p_k/\log p_k$, so $\log\omega\cdot\log\log n/\log n\ge\log2+o(1)$, matching Wigert's $\max\tau$. This bound uses only primitivity + disjoint fibres, so it holds in **every** all-$d$ fake model: for composite $n$ the axioms *force* ratio $\ge\log2$ along highly composite $n$. For prime $n=p$ they force nothing: ratio can be $0$ ($\mathcal M^0$) or $\to\infty$ ($\mathcal M^r$). The prompt's $\log2$ is the composite calibration transplanted via $\max_{m\le2p}\tau(m)$; Cor. 4.3 overshoots it. (Heuristic, UNPROVED: $\sum_{q\equiv1\,(2p),\,q<2^p}p/(q-1)\approx\log p$, so the true $\omega(M_p)$ is expected to be $\asymp\log p$ on average, i.e. ratio $\to0$; the models show this heuristic is not a consequence of the axioms.)

## 8. Numerical sanity check (finite, illustrative)

`check_models.py`: $\mathrm{Ax}_{12,3}$ holds for $T$ at all $5\le p\le89$ (exact factorizations; $\omega$ agrees with prompt data); Lemma 1.5 witnesses found; $\mathcal M^0$ and $\mathcal M^r$ built with $D=6,J=2$ for $41\le p\le257$ pass all checks (A1)–(A6). Primality of large fillers uses Miller–Rabin (probabilistic above $3\cdot10^{24}$).
