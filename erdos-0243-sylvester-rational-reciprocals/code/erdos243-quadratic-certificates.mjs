// Exhaustive finite-field certificates for five exact quadratic profiles.
import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
const mod=(x,p)=>(x%p+p)%p;
function inverse(x,p) {
  for(let a=1;a<p;a++)if(a*x%p===1)return a;
  throw new Error('Nonunit');
}
function backward(p,table,root,limit) {
  assert.equal(table[root],0);
  assert.notEqual(table[(root+1)%p],0);
  const at=n=>table[mod(n,p)], units=Array.from({length:p-1},(_,i)=>i+1);
  let values=[mod(-at(root+1),p)];
  const rows=[{index:root,C:at(root),values}];
  for(let j=root-1;j>=root-limit;j--) {
    const previous=units.filter(x=>values.some(d=>mod(x*(x+at(j+1))-at(j)*d,p)===0));
    // Check the preimage using the two original recurrences independently.
    const direct=units.filter(x=>values.some(d=>{
      const a=d*inverse(x,p)%p;
      return mod(a*at(j)-x-at(j+1),p)===0;
    }));
    assert.deepEqual(previous,direct);
    values=previous;rows.push({index:j,C:at(j),values});
    if(!values.length)return {empty:true,rows};
  }
  return {empty:false,rows};
}
// Cyclic control: C_j=j, D_j=-1, a_j=1 is a legal modular orbit.
for(const p of [3,7,11]) {
  const control=backward(p,Array.from({length:p},(_,n)=>n),0,2*p);
  assert.equal(control.empty,false);
  assert.ok(control.rows.every(r=>r.values.includes(p-1)));
}
const known=backward(11,Array.from({length:11},(_,n)=>mod(n*n+n-1,11)),7,3);
assert.equal(known.empty,true);
assert.equal(known.rows.length,3);

const cases=[[16,11],[64,13],[252,19],[1932,11],[2700,11]],results=[];
for(const[A,p]of cases) {
  assert.ok(Array.from({length:p-2},(_,i)=>i+2).every(d=>p%d!==0));
  const table=Array.from({length:p},(_,n)=>mod((A%p)*n*(n+1)-1,p));
  const roots=table.flatMap((x,n)=>x===0?[n]:[]);
  const certificates=roots.map(r=>backward(p,table,r,2*p)).filter(c=>c.empty);
  assert.ok(certificates.length);
  certificates.sort((a,b)=>a.rows.length-b.rows.length);
  const result={A,p,table,...certificates[0]};results.push(result);
  console.log(JSON.stringify(result));
}
writeFileSync('erdos243-quadratic-certificates.json',JSON.stringify({
  scope:'Exact necessary finite-field conditions for C_n=A*n(n+1)-1, for the five coefficients returned by the elliptic reduction. No arbitrary-orbit exclusion.',
  results},null,2));
