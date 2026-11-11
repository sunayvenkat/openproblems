# Random-model limit density for a linear-piece family: pieces ~ independent integers of size X (Poisson-Dirichlet anatomy),
# n ~ X^2. Prime q = X^theta of piece j: L = floor(2/theta). theta<1/2: P(bad)=2^(1-L); theta in (1/2,2/3): f_j/2; theta>2/3: f_j.
import random, math, sys
def pd_thetas(eps, rng):
    out=[]; rem=1.0
    while rem>eps:
        u=rng.random(); th=rem*u; rem-=th
        if th>eps: out.append(th)
    return out
def density(fs, S=200000, eps=0.02, seed=1):
    rng=random.Random(seed); tot=0.0
    for _ in range(S):
        p=1.0
        for f in fs:
            for th in pd_thetas(eps, rng):
                L=int(2/th)
                if th>2/3: bad=f
                elif th>1/2: bad=f/2
                else: bad=2.0**(1-L)
                p*=1-bad
        tot+=p
    return tot/S
for name,fs in [('E1 (12x-1)(22x+9)',[0,.2,.2,0]),('E1 2(12x+5)(35x+32)',[0,1/6,1/6,0]),('E1 ThmA',[1/3,0,1/3,0]),('E2 (14x-1)(15x-1)',[1/3,0,0,1/3,0,1/6])]:
    print(name, round(density(fs),4))
