import{r,o as h,a as c,c as u,b as p,d as n,e as v,F as _}from"./index.S7RG_dfA.js";/* empty css                        */import{_ as b}from"./_plugin-vue_export-helper.x3n3nnut.js";const w={__name:"ImageNav",props:{gallery:{type:Array,required:!1},translations:{type:Object,required:!1}},setup(a,{expose:d}){d();const o=r(!1),e=r(null),s=r(1),i=r(null),f=r(null),y=()=>{window.history.length<1&&(window.location.url="/"),history.go(s.value*-1)};h(()=>{const m=window.location.search,t=new URLSearchParams(m),l=parseInt(t.get("index"));e.value=t.get("gallery")?t.get("gallery").split(","):[],s.value=t.get("history")?parseInt(t.get("history")):1,l+1<e.value.length&&(i.value=`${e.value[l+1]}?index=${l+1}&history=${s.value+1}&gallery=${t.get("gallery")}`),l>0&&(f.value=`${e.value[l-1]}?index=${l-1}&history=${s.value+1}&gallery=${t.get("gallery")}`),setTimeout(()=>{o.value=!0},500)});const g={showButtons:o,gallery:e,historyLength:s,next:i,prev:f,closeWindow:y,props:a,ref:r,onMounted:h};return Object.defineProperty(g,"__isScriptSetup",{enumerable:!1,value:!0}),g}},x=["aria-label"],$={class:"fade-in pointer-events-none absolute bottom-1/2 right-0 z-50 flex w-full justify-between p-2"},k=["href","aria-label"],S=["href","aria-label"];function B(a,d,o,e,s,i){return c(),u(_,null,[p("button",{class:"fade-in absolute right-0 top-0 z-50 m-4 h-10 w-10","aria-label":o.translations.close,onClick:e.closeWindow},[n(a.$slots,"close")],8,x),p("div",$,[e.prev?(c(),u("a",{key:0,href:e.prev,"aria-label":o.translations.prev,class:"pointer-events-auto m-4"},[n(a.$slots,"prev")],8,k)):v("",!0),e.next?(c(),u("a",{key:1,href:e.next,"aria-label":o.translations.next,class:"pointer-events-auto m-4 ml-auto"},[n(a.$slots,"next")],8,S)):v("",!0)]),n(a.$slots,"default")],64)}const P=b(w,[["render",B]]);export{P as default};