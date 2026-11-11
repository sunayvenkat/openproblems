# Z[omega] as pairs (x,y)=x+y*w, w^2=-1-w
def mul(u,v):
    a,b=u; c,d=v
    return (a*c-b*d, a*d+b*c-b*d)
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def sub(u,v): return (u[0]-v[0],u[1]-v[1])
W=[(1,0),(0,1),(-1,-1)]
def wp(k): return W[k%3]
S=[(1,0),(0,-1),(0,0)]          # S=(1,-w,0)
def fl(n):  # floor(n*log3 2) exactly: largest b with 3^b<=2^n
    b=0; x=2**n
    while 3**(b+1)<=x: b+=1
    return b
N=3000
A=[(1,0)]
for a in range(N):
    A.append(add(A[-1], mul(wp(-a-1), S[fl(a+1)%3])))
# lemma S(n+1)=w^2 S(n)+1
for n in range(3): assert add(mul(W[2],S[n]),(1,0))==S[(n+1)%3]
for p,q,Q in [(12,19,65),(41,65,84),(53,84,485),(306,485,1054)]:
    u=wp(2*p-q); cp=(0,0)
    for k in range(p): cp=add(cp,wp(2*k))
    good=0; first=None
    for a in range(0,N-3*q):
        geo=(0,0)
        for i in range(1,a+1): pass
        # closed form of sum_{i=1}^a w^-i
        g=[(0,0),wp(-1),add(wp(-1),wp(-2))][a%3]
        pred=add(A[q], add(mul(u,sub(A[a],(1,0))), mul(mul(cp,wp(-q)),g)))
        if pred!=A[a+q] and first is None: first=a
    d3=[sub(A[a+3*q],A[a]) for a in range(0,min(N-3*q,Q))]
    firstd=next((a for a in range(len(d3)) if d3[a]!=d3[0]),None)
    print('p/q',p,q,'twist u=w^%d'%((2*p-q)%3),'affine q-shift lemma first failure a=',first,'(next Q=%d)'%Q,
          '| 3q-drift A_{a+3q}-A_a =',d3[0],'constant until a=',firstd)
