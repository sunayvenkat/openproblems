import random,sys
from rec import mul,wp,add
OKB={(0,1,(1,0)),(1,1,(1,0)),(2,0,(2,1)),(2,2,(2,0))}
OKS={(1,2,(1,1)),(2,1,(1,0))}
def run(digits):
    # digits a_0=0,a_1,...; track convergents with H via intermediate fractions
    # state: lo,hi fractions as (p,q,H) ; start 0/1,1/1 ; a_0=0, so alpha in (0,1)
    lo=(0,1,(1,0)); hi=(1,1,(1,0))
    def med(L,U): return (L[0]+U[0],L[1]+U[1],add(L[2],mul(wp(L[0]+L[1]),U[2])))
    # Stern-Brocot: digits a_1.. : first go left a_1-1 times? Use standard: path R^{a0} L^{a1} R^{a2}...
    # alpha in (0,1): start at 1/1 node... simpler: generate convergent list, then mediant via neighbors
    conv=[]  # (p,q,H)
    side=0  # 0: moving toward lower (replace hi), alternate
    cur=[lo,hi]
    out=[]
    # alpha=[0;a1,a2,...]: from (0/1,1/1) the mediant 1/2 etc. Path: L^{a1-1} R^{a2} L^{a3}...
    moves=[]
    for i,a in enumerate(digits[1:],start=1):
        cnt=a-1 if i==1 else a
        moves += ['L' if i%2==1 else 'R']*cnt
    pts=[]
    for mv in moves:
        m=med(lo,hi)
        if mv=='L': hi=m   # alpha < m
        else: lo=m
        pts.append((lo,hi))
    return pts
