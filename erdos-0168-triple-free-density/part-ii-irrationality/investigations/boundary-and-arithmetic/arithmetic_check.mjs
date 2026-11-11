// Check the separated color identity against direct counts and the cone rule
// against the previously certified finite optima. No candidate optima are used.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';

const source = new URL('../Open conjecture transfer search/168_exact_diagonal_results.json', import.meta.url);
const rows = JSON.parse(await fs.readFile(source,'utf8')).exactDp;
const add=(z,w)=>[z[0]+w[0],z[1]+w[1]];
const sub=(z,w)=>[z[0]-w[0],z[1]-w[1]];
const rotate=(z,k)=>{
  k=((k%3)+3)%3;
  while(k--) z=[-z[1],z[0]-z[1]];
  return z.map(x=>x===0?0:x);
};
const correction=[[[0,0],[0,0],[0,0]],[[0,0],[1,0],[1,1]],[[0,0],[0,-1],[1,0]]];
const counts=[0,0,0], states=new Map();
for(let i=0;i<rows.length;i++) {
  const row=rows[i];
  let v=row.t,a=0,b=0;
  while(v%2===0){v/=2;a++;}
  while(v%3===0){v/=3;b++;}
  assert.equal(v,1);
  counts[(a+2*b)%3]++;
  states.set(row.t,{a,b,W:[counts[0]-counts[2],counts[1]-counts[2]],eta:row.tau-(i?rows[i-1].tau:0)});
}

let coneChecks=0, recurrenceChecks=0;
for(const [d,{a,b,W,eta}] of states) {
  const A=rotate(states.get(2**a).W,-a);
  const B=rotate(states.get(3**b).W,-2*b);
  const expected=add(sub(add(A,B),[1,0]),correction[a%3][b%3]);
  assert.deepEqual(rotate(W,-a-2*b),expected,`separation at ${d}`);
  if(b>=4) {
    const p3=3**b;
    let p2=1,m=0;
    while(2*p2<=p3){p2*=2;m++;}
    const epsilon=[0,0,0];
    if(3*p2>2*p3) epsilon[((m-2*b)%3+3)%3]=1;
    let patchPower=1,n=0;
    while(12*patchPower<=p3){patchPower*=2;n++;}
    if(6*patchPower<=p3&&4*p3<27*patchPower) epsilon[((n-2*b)%3+3)%3]=1;
    const [x,y]=expected;
    const predicted=Number(x<=epsilon[0]-epsilon[2]&&x-y<=epsilon[0]-epsilon[1]);
    assert.equal(predicted,eta,`cone digit at ${d}`);
    coneChecks++;
  }
  if(b===0&&a>0) {
    let power=1,k=0;
    while(3*power<=d){power*=3;k++;}
    const S=[[1,0],[0,-1],[0,0]][k%3];
    const previous=rotate(states.get(d/2).W,-a+1);
    assert.deepEqual(sub(A,previous),rotate(S,-a),`axis cocycle at ${d}`);
    recurrenceChecks++;
  }
}
export const result={separationChecks:states.size,coneChecks,recurrenceChecks,lastCutoff:rows.at(-1).t};
