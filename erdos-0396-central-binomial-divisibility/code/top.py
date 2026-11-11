import sys; sys.path.insert(0,'.')
from poly import *
for D in [105,165,195,231,255,1155,15015]:
    if D>2000: continue
    f=list(cyclo(2*D)); xD1=[1]+[0]*(D-1)+[1]
    u,r=divmod_monic(xD1,f); assert not r
    ds=digits(u,f)
    print(D,'deg f',len(f)-1,'deg u',len(u)-1,'digit lead signs',[ (len(d)-1, (1 if d[-1]>0 else -1) if d else 0) for d in ds])
