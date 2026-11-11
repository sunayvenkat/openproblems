import itertools
for p in [5,7]:
  for J in [1,2]:
    for w in [2,3]:
      M=2**p-1; mod=p**(J+1)
      c=sum(1 for m in itertools.product(range(p**J),repeat=w) if eval('*'.join('(1+2*p*%d)'%x for x in m))%mod==M%mod)
      print(p,J,w,c,p**(J*(w-1)))
