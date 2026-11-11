import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
import {init,killThreads} from './.research-tools/node_modules/z3-solver/build/node.js';
import {permanent} from './marcus-block-search.mjs';

// Searches a specified invariant sum-of-squares ansatz for three quadratics.
// A satisfiable sampled system is only a candidate identity, not a proof.
const r=Number(process.argv[2]??3),D=(r+2)*(r-1)*(r+1),n=r*r;
const norm=a=>a.reduce((s,x)=>s+x*x,0);
function inner(a,b){let x=0,y=0;for(let j=0;j<a.length;j+=2){x+=a[j]*b[j]+a[j+1]*b[j+1];y+=a[j]*b[j+1]-a[j+1]*b[j];}return[x,y];}
const combine=(a,b,s=1)=>Float64Array.from(a,(x,j)=>x+s*b[j]);
function adj(a){const b=new Float64Array(2*n);for(let i=0;i<r;i++)for(let j=0;j<r;j++){b[2*(i*r+j)]=a[2*(j*r+i)];b[2*(i*r+j)+1]=-a[2*(j*r+i)+1];}return b;}
function mm(a,b){const c=new Float64Array(2*n);for(let i=0;i<r;i++)for(let j=0;j<r;j++)for(let k=0;k<r;k++){const x=2*(i*r+k),y=2*(k*r+j),z=2*(i*r+j);c[z]+=a[x]*b[y]-a[x+1]*b[y+1];c[z+1]+=a[x]*b[y+1]+a[x+1]*b[y];}return c;}
function scale(a,z){const b=new Float64Array(a.length);for(let j=0;j<a.length;j+=2){b[j]=a[j]*z[0]-a[j+1]*z[1];b[j+1]=a[j]*z[1]+a[j+1]*z[0];}return b;}
function trace(a){let x=0,y=0;for(let i=0;i<r;i++){x+=a[2*(i*r+i)];y+=a[2*(i*r+i)+1];}return[x,y];}
const tid=(a,b,c,d)=>2*(((a*r+b)*r+c)*r+d);
function polynomial(a){const p=new Map();for(let i=0;i<r;i++)for(let j=i;j<r;j++){const e=Array(r).fill(0);e[i]++;e[j]++;const z=2*(i*r+j),f=i===j?1:2;p.set(e.join(','),[f*a[z],f*a[z+1]]);}return p;}
function pmul(a,b){const c=new Map();for(const[x,u]of a)for(const[y,v]of b){const key=x.split(',').map((q,i)=>Number(q)+Number(y.split(',')[i])).join(','),w=c.get(key)??[0,0];w[0]+=u[0]*v[0]-u[1]*v[1];w[1]+=u[0]*v[1]+u[1]*v[0];c.set(key,w);}return c;}
function features(mats){
  const cols=Array(9).fill(0),g=new Float64Array(18);let explicitSOS=0;
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)g.set(inner(mats[i],mats[j]).map(x=>2*x),2*(3*i+j));
  const prod=pmul(pmul(polynomial(mats[0]),polynomial(mats[1])),polynomial(mats[2])),fac=[1,1,2,6,24,120,720];
  let p=0;for(const[e,z]of prod)p+=(z[0]**2+z[1]**2)*e.split(',').reduce((s,x)=>s*fac[Number(x)],1);
  const F=p-permanent(g,3).value[0];
  for(let center=0;center<3;center++){
    const [a,b]=mats.filter((_,i)=>i!==center),c=adj(mats[center]),bc=mm(b,c),ac=mm(a,c);
    const w1=mm(ac,b),w2=mm(bc,a),wp=combine(w1,w2),wm=combine(w1,w2,-1);
    const la=scale(a,trace(bc)),lb=scale(b,trace(ac)),lp=combine(la,lb),lm=combine(la,lb,-1);
    for(const sign of [1,-1]){
      const t=new Float64Array(2*r**4);
      for(let i=0;i<r;i++)for(let j=0;j<r;j++)for(let k=0;k<r;k++)for(let l=0;l<r;l++){
        const x=2*(i*r+j),y=2*(k*r+l),z=tid(i,j,k,l);
        t[z]=a[x]*bc[y]-a[x+1]*bc[y+1]+sign*(b[x]*ac[y]-b[x+1]*ac[y+1]);
        t[z+1]=a[x]*bc[y+1]+a[x+1]*bc[y]+sign*(b[x]*ac[y+1]+b[x+1]*ac[y]);
      }
      const s=new Float64Array(t.length);
      for(let i=0;i<r;i++)for(let j=0;j<r;j++)for(let k=0;k<r;k++)for(let l=0;l<r;l++)for(let z=0;z<2;z++)s[tid(i,j,k,l)+z]=t[tid(i,j,k,l)+z]+t[tid(i,k,j,l)+z]+t[tid(j,k,i,l)+z];
      const h=Float64Array.from(t,(x,j)=>3*x-s[j]);
      const st=sign===1?combine(lp,wp,2):lm;
      const sf=norm(s)-3/(r+2)*norm(st);
      const hf=norm(h)-(sign===1?6/(r-1)*norm(combine(lp,wp,-1)):6/(r-1)*norm(lm)+18/(r+1)*norm(wm));
      assert(sf>-1e-7&&hf>-1e-7,'Trace-free norm formula failed');
      if(sign===1&&r===5){
        const jmat=combine(lp,wp,-1),ss=new Float64Array(s.length),hh=new Float64Array(h.length);
        for(let i=0;i<r;i++)for(let j=0;j<r;j++)for(let k=0;k<r;k++)for(let l=0;l<r;l++)for(let z=0;z<2;z++){
          const e=(i===l?st[2*(j*r+k)+z]:0)+(j===l?st[2*(i*r+k)+z]:0)+(k===l?st[2*(i*r+j)+z]:0);
          const kk=(i===l?jmat[2*(j*r+k)+z]:0)+(j===l?jmat[2*(i*r+k)+z]:0)-2*(k===l?jmat[2*(i*r+j)+z]:0),t=tid(i,j,k,l)+z;
          ss[t]=7*s[t]-e;hh[t]=4*h[t]+kk;
        }
        assert.equal(norm(ss),49*norm(s)-21*norm(st));
        assert.equal(norm(hh),16*norm(h)-24*norm(jmat));
        explicitSOS+=16*norm(ss)+7*norm(hh)+378*norm(wp)+126*norm(combine(scale(lp,[2,0]),wp,5));
      }
      cols[sign===1?0:1]+=sf;cols[sign===1?2:3]+=hf;
    }
    cols[4]+=norm(wm);cols[5]+=norm(lm);cols[6]+=norm(wp);cols[7]+=norm(lp);cols[8]+=2*inner(wp,lp)[0];
  }
  if(r===5)assert.equal(explicitSOS,189*F,'Explicit integer SOS identity failed');
  return{cols:cols.map(x=>{assert(Math.abs(D*x-Math.round(D*x))<1e-6);return Math.round(D*x);}),F:Math.round(D*F),...(r===5?{explicitSOS}:{} )};
}
let seed=18239;function random(){seed=Math.imul(seed,1664525)+1013904223|0;return(seed>>>0)/4294967296;}
function matrix(){const a=new Float64Array(2*n);for(let i=0;i<r;i++)for(let j=i;j<r;j++)for(let z=0;z<2;z++){const x=Math.floor(3*random())-1;a[2*(i*r+j)+z]=x;a[2*(j*r+i)+z]=x;}return a;}
const records=Array.from({length:40},()=>features([matrix(),matrix(),matrix()]));
const api=await init();
try{
  const{Solver,Real}=new api.Context('marcus_sos'),s=new Solver(),v=Array.from({length:9},(_,i)=>Real.const(`c${i}`));
  s.set('timeout',30000);
  for(const row of records){let sum=Real.val(0);row.cols.forEach((x,i)=>{sum=sum.add(v[i].mul(x));});s.add(sum.eq(row.F));}
  const spanStatus=await s.check();console.log('Linear span:',spanStatus);
  if(spanStatus==='sat')console.log('Unconstrained coefficients:',v.map(x=>s.model().eval(x).toString()));
  for(let i=0;i<8;i++)s.add(v[i].ge(0));s.add(v[6].mul(v[7]).ge(v[8].mul(v[8])));
  const status=await s.check(),result={rank:r,spanStatus,status,columns:['symmetric_plus_trace_free','symmetric_minus_trace_free','hook_plus_trace_free','hook_minus_trace_free','Wminus','Lminus','Wplus','Lplus','cross_Wplus_Lplus'],records};
  if(status==='sat')result.coefficients=v.map(x=>s.model().eval(x).toString());
  console.log(JSON.stringify({rank:r,status,coefficients:result.coefficients}));
  writeFileSync(`marcus-quadratic-sos-${r}.json`,JSON.stringify(result,null,2)+'\n');
}finally{await killThreads(api.em);}
