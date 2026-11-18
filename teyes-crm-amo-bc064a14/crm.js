(()=>{const r=document.documentElement,k='crm-theme';try{const s=localStorage.getItem(k);if(s)r.dataset.theme=s}catch(e){}
const b=document.getElementById('th');if(!b)return;b.onclick=()=>{const d=r.dataset.theme?r.dataset.theme==='dark':matchMedia('(prefers-color-scheme: dark)').matches;r.dataset.theme=d?'light':'dark';try{localStorage.setItem(k,r.dataset.theme)}catch(e){}}})();
