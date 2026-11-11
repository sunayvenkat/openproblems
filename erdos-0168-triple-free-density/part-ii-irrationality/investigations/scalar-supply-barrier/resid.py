import pickle
digits,P,Q,Hc=pickle.load(open('actual.pkl','rb'))
res=pickle.load(open('res.pkl','rb'))
S={(1,2,(1,1)),(2,1,(1,0))}
mism=0;resn=0;joint_res=0;joint_bal=0
for (n,a,nonres,st,el) in res:
    s0=(P[n-1]+Q[n-1])%3; s1=(P[n]+Q[n])%3
    pred = s1!=0 and ((a+1)*s1+s0)%3==0
    actual = el and st in S
    mism+= pred!=actual
    resn+=actual
    if a>=5 and el: 
        if st in S: joint_res+=1
        else: joint_bal+=1
print('mismatches',mism,'resonant-branch eligible',resn,'joint res/bal',joint_res,joint_bal)
# exact certification of first convergents by integer comparison 2^s vs 3^r
ok=all(((2**Q[n] > 3**P[n]) == (n%2==0)) for n in range(1,14))
print('exact side check first 14 convergents:',ok)
