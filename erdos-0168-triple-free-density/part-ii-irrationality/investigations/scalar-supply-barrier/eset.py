exec(open('tail2.py').read().split('# find actual')[0])
import pickle,random
from collections import Counter
digits,P,Q,Hc=pickle.load(open('actual.pkl','rb'))
def E_of_prefix(ds):
    # eligible residues of next digit at last index n=len(ds)-1, testing digits 5,6,7
    out=set()
    for a in (5,6,7):
        rr=analyze(ds+[a,1,1])
        n=len(ds)-1
        row=[r for r in rr if r[0]==n]
        if row and (row[0][3] or row[0][4]): out.add(a%3)
    return frozenset(out)
cnt=Counter()
for n in range(3,120):
    cnt[len(E_of_prefix(digits[:n+1]))]+=1
print('actual-prefix |E| distribution (n<120):',cnt)
# greedy avoider: from actual prefix, always choose a large digit (5..7) outside E if possible
random.seed(2)
for start in (20,40,60):
    ds=digits[:start+1]; forced=0; large=0
    for step in range(60):
        E=E_of_prefix(ds)
        choices=[a for a in (5,6,7) if a%3 not in E]
        if choices: ds=ds+[random.choice(choices)]; large+=1
        else: ds=ds+[random.choice([1,2,3,4])]; forced+=1
    print('start',start,'large digits used',large,'forced small',forced)
