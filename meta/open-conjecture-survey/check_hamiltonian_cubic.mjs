import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { init } = require('../../.research-tools/node_modules/z3-solver');
const { Context } = await init();
const { Solver, Bool, If, Int, Or, Sum } = new Context('main');

const edgeKey = (a,b) => a < b ? `${a},${b}` : `${b},${a}`;
for (let n=6; n<=16; n++) {
  const pairs = [];
  for (let i=0;i<n;i++) for(let j=i+1;j<n;j++) pairs.push([i,j]);
  const cycle = new Set(Array.from({length:n},(_,i)=>edgeKey(i,(i+1)%n)));
  const x = pairs.map((_,i)=>Bool.const(`g${n}_${i}`));
  const outer = new Solver();
  outer.set('timeout',60000);
  pairs.forEach((p,i)=>{if(cycle.has(edgeKey(...p))) outer.add(x[i]);});
  outer.add(Sum(...x.map(v=>If(v,1,0))).ge(2*n));
  let cuts=0;
  while (true) {
    const status=String(await outer.check());
    if(status!=='sat'){console.log(JSON.stringify({n,status,cuts}));break;}
    const model=outer.model();
    const present=pairs.map((_,i)=>String(model.eval(x[i]))==='true');
    const y=pairs.map((_,i)=>Bool.const(`c${n}_${cuts}_${i}`));
    const inner=new Solver();
    present.forEach((v,i)=>{if(!v)inner.add(y[i].not());});
    for(let v=0;v<n;v++) {
      const degree=Sum(...pairs.flatMap((p,i)=>p.includes(v)?[If(y[i],1,0)]:[]));
      inner.add(Or(degree.eq(0),degree.eq(3)));
    }
    inner.add(Or(...y));
    const cubic=String(await inner.check());
    if(cubic==='unsat') {
      console.log(JSON.stringify({n,status:'counterexample',cuts,edges:pairs.filter((_,i)=>present[i])}));
      process.exit(0);
    }
    if(cubic!=='sat')throw new Error(cubic);
    const im=inner.model();
    const used=y.map((v,i)=>String(im.eval(v))==='true'?i:-1).filter(i=>i>=0);
    const degrees=Array(n).fill(0);
    used.forEach(i=>pairs[i].forEach(v=>degrees[v]++));
    if(!used.length||degrees.some(d=>d!==0&&d!==3))throw new Error('invalid cubic witness');
    outer.add(Or(...used.map(i=>x[i].not())));
    cuts++;
    if(cuts%100===0)console.log(JSON.stringify({n,cuts}));
  }
}
