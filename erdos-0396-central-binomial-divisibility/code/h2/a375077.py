# Inspect minimal elements of E_k: prime factor sizes (theta = log q / log n) and which carry level saves each prime.
import math
from sympy import factorint
A = {1:2,2:2480,3:8178,4:45153,5:3648841,6:7979090,7:101130029,8:339949252,9:1019547844,10:17609764994,11:1070858041585,12:5048891644646,13:18253129921842,14:359503904702190,15:2394789405254721,16:20021368432952099}
def carries(n,q):
    c=0;t=2*n
    while t:
        t//=q
        if t&1:c+=1
    return c
for k in (12,14,16):
    n=A[k]; print('k',k,'n',n,'log10',round(math.log10(n),2),'sqrt(2n)=1e%.2f'%(math.log10(2*n)/2))
    big=[]
    for i in range(k+1):
        f=factorint(n-i)
        for q,e in f.items():
            th=math.log(q)/math.log(n)
            if q>50: big.append((round(th,3),q,e,i,carries(n,q)))
    big.sort(reverse=True)
    print('  largest primes (theta,q,e,i,carries):',big[:8])
    print('  #primes>50:',len(big),' #theta>1/3:',sum(1 for b in big if b[0]>1/3),' #theta>0.4:',sum(1 for b in big if b[0]>0.4))
