import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {permanent} from './marcus-block-search.mjs';

const add=(a,b)=>[a[0]+b[0],a[1]+b[1]],mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],conj=a=>[a[0],-a[1]],norm=a=>a[0]**2+a[1]**2;
const scale=(a,t)=>a.map(x=>t*x);
function matrixMultiply(a,b,n){const c=Array.from({length:n*n},()=>[0,0]);for(let i=0;i<n;i++)for(let j=0;j<n;j++)for(let k=0;k<n;k++)c[i*n+j]=add(c[i*n+j],mul(a[i*n+k],b[k*n+j]));return c;}
function tracePower(a,n,m){let p=Array.from({length:n*n},(_,i)=>[Number(Math.floor(i/n)===i%n),0]);while(m){if(m&1)p=matrixMultiply(p,a,n);a=matrixMultiply(a,a,n);m=Math.floor(m/2);}let t=[0,0];for(let i=0;i<n;i++)t=add(t,p[i*n+i]);return t;}
export function transfer(m,a,b){
  assert(m>=3);const A=norm(a),B=norm(b),d=2+A+2*B;
  // All matrices are divided by d to keep large cycle lengths numerically safe.
  const M0=[2,A,B,6,2*A,B,24,6*A,2*B].map(x=>[x/d,0]);
  const x=conj(a),y=mul(a,conj(b));
  const M1=[scale(x,2),y,scale(x,6),scale(y,2)].map(z=>scale(z,1/d));
  const N=[d,4*B,1,0].map(x=>[x/d,0]);
  const diagonal=tracePower(M0,3,m)[0],cross=2*tracePower(M1,2,m)[0],loop=2*tracePower([scale(b,2/d)],1,m)[0];
  const q=tracePower(N,2,m)[0]+loop,p=diagonal+cross+loop;
  return{p,q,d,ratio:p/q,gap:diagonal+cross-(q-loop),diagonal,cross,loop};
}

function direct(m,a,b){
  let terms=new Map([[Array(m).fill(0).join(','),[1,0]]]);
  for(let i=0;i<m;i++){
    const next=new Map();for(const[e,z]of terms)for(let s=0;s<=2;s++){
      const ex=e.split(',').map(Number);ex[i]+=2-s;ex[(i+1)%m]+=s;const key=ex.join(','),w=mul(z,[[1,0],a,b][s]);next.set(key,add(next.get(key)??[0,0],w));
    }terms=next;
  }
  const fac=[1,1,2,6,24];let p=0;for(const[e,z]of terms)p+=norm(z)*e.split(',').reduce((s,x)=>s*fac[Number(x)],1);
  const g=new Float64Array(2*m*m),d=2+norm(a)+2*norm(b);
  for(let i=0;i<m;i++){
    g[2*(i*m+i)]=d;
    const j=(i+1)%m;g[2*(i*m+j)]=2*b[0];g[2*(i*m+j)+1]=-2*b[1];g[2*(j*m+i)]=2*b[0];g[2*(j*m+i)+1]=2*b[1];
  }
  return{p,q:permanent(g,m).value[0]};
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
for(const[a,b]of [[[1,0],[1,0]],[[0,1],[1,-1]],[[1,1],[-1,0]],[[0,0],[0,1]]])for(let m=3;m<=7;m++){
  const e=transfer(m,a,b),f=direct(m,a,b),factor=e.d**m;
  assert(Math.abs(e.p*factor-f.p)<1e-8*Math.max(1,f.p));
  assert(Math.abs(e.q*factor-f.q)<1e-8*Math.max(1,f.q));
}
console.log('Transfer identities agree with independent polynomial expansion and permanent DP.');
const count=Number(process.argv[2]??20000),mode=process.argv[3]??'random';assert(['random','worst'].includes(mode));let seed=18177;
function random(){seed=Math.imul(seed,1664525)+1013904223|0;return(seed>>>0)/4294967296;}
let best={ratio:Infinity};const byLength={};
for(let trial=0;trial<count;trial++){
  const absA=Math.exp(12*random()-6),absB=Math.exp(12*random()-6),m=3+Math.floor(198*random());
  const phaseA=mode==='worst'?Math.PI/m:2*Math.PI*random(),phaseB=mode==='worst'?2*Math.PI/m:2*Math.PI*random();
  const a=[absA*Math.cos(phaseA),absA*Math.sin(phaseA)],b=[absB*Math.cos(phaseB),absB*Math.sin(phaseB)],e=transfer(m,a,b);
  if(e.ratio<best.ratio)best={trial,m,a,b,...e};
  byLength[m]=Math.min(byLength[m]??Infinity,e.ratio);
}
writeFileSync(`marcus-cycle-transfer-${mode}-results.json`,JSON.stringify({samples:count,mode,best,byLength},null,2)+'\n');
console.log(JSON.stringify({samples:count,mode,best}));
}
