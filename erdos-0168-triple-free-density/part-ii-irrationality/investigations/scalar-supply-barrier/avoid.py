exec(open('eset.py').read().split('cnt=Counter()')[0])
random.seed(2)
ds=digits[:41]
for step in range(40):
    E=E_of_prefix(ds)
    ch=[a for a in (5,6,7) if a%3 not in E]
    ds=ds+[random.choice(ch) if ch else 4]
rr=[r for r in analyze(ds+[1,1]) if r[0]>40]
print('tail digits',ds[41:])
print('eligible-with-large-digit in tail:',sum((r[3] or r[4]) and r[1]>=5 for r in rr))
def norm(h): x,y=h; return x*x-x*y+y*y
print('mediant (r,s) residues',Counter((r[5][0],r[5][1]) for r in rr))
print('mediant |H|^2 range',min(norm(r[5][2]) for r in rr),max(norm(r[5][2]) for r in rr))
print('t values',Counter(r[2] for r in rr))
