// An exact obstruction to gap-monotonicity induction, not to Marcus's inequality.
import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
import {exactCertificate,exactPermanent} from './marcus-block-exact.mjs';
const add=(a,b)=>[a[0]+b[0],a[1]+b[1]];
const mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];
function directPermanent(a){
  let total=[0n,0n];
  function visit(i,used,term){
    if(i===a.length){total=add(total,term);return;}
    for(let j=0;j<a.length;j++)if(!(used&(1<<j)))visit(i+1,used|(1<<j),mul(term,a[i][j]));
  }
  visit(0,0,[1n,0n]);return total;
}
function product(a,b){const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c;}
function factorial(n){let a=1n;for(let j=2;j<=n;j++)a*=BigInt(j);return a;}
function inner(a,b){assert.equal(a.length,b.length);const d=a.length-1;return a.reduce((s,c,j)=>s+c*b[j]*factorial(j)*factorial(d-j),0n);}
function check(t,s){
  const A=2n*t*t,d=s*s;
  const v=[[[t,t],[1n,0n]],[[t,-t],[1n,0n]],[[-t,t],[1n,0n]],[[-t,-t],[1n,0n]],[[1n,0n],[0n,s]],[[1n,0n],[0n,-s]]];
  const full=exactCertificate(v,3,2),previous=exactCertificate(v.slice(0,4),2,2);
  const forms=[[A,2n*t,1n],[A,-2n*t,1n],[1n,0n,d]],f=product(forms[0],forms[1]),all=product(f,forms[2]);
  const g=forms.map(a=>forms.map(b=>[inner(a,b),0n]));
  assert.deepEqual(f,[A*A,0n,0n,0n,1n]);
  assert.equal(full.p,inner(all,all));assert.equal(previous.p,inner(f,f));assert.deepEqual(full.g,g);
  assert.deepEqual(directPermanent(full.a),[full.p,0n]);assert.deepEqual(directPermanent(g),[full.q,0n]);
  const normLast=inner(forms[2],forms[2]),increment=full.difference-previous.difference*normLast;
  const formula=32n*(21n*A**4n+21n*d*d-(A*A+1n)*(A+d)**2n);
  assert.equal(increment,formula);
  const determinants=[];
  for(let b=0;b<3;b++){
    const i=2*b,j=i+1,z=full.a[i][j];
    const det=full.a[i][i][0]*full.a[j][j][0]-z[0]**2n-z[1]**2n;
    assert.ok(det>0n);determinants.push(det);
  }
  return{t,s,A,full,previous,normLast,increment,diagonalBlockDeterminants:determinants};
}
const witness=check(2n,6n);
assert.equal(witness.full.p,258686256n);assert.equal(witness.full.q,93032208n);
assert.equal(witness.previous.difference,64016n);assert.equal(witness.normLast,2594n);
assert.equal(witness.increment,-403456n);assert.ok(witness.full.difference>0n);
let checked=0;for(let t=1n;t<=5n;t++)for(let s=1n;s<=20n;s++){check(t,s);checked++;}
const output={scope:'Disproves the proposed monotonicity of the Marcus gap under addition of a block. All three diagonal blocks of this witness are positive definite. The Marcus gap itself is positive, so this is not a counterexample to the original conjecture.',checked,witness};
writeFileSync('marcus-induction-obstruction.json',JSON.stringify(output,(_,x)=>typeof x==='bigint'?String(x):x,2)+'\n');
console.log(JSON.stringify({checked,p:String(witness.full.p),q:String(witness.full.q),gap:String(witness.full.difference),previousGapTimesLastNorm:String(witness.previous.difference*witness.normLast),increment:String(witness.increment),diagonalBlockDeterminants:witness.diagonalBlockDeterminants.map(String)}));
