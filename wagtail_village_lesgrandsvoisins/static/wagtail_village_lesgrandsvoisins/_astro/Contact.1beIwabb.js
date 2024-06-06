import{i as j,r as i,f as x,w as z,a as p,c as u,b as t,t as n,d as O,m as L,h as M,e as U,j as f,n as g,k as H,q as _,F as J,s as G,u as K,p as Q,l as R}from"./index.S7RG_dfA.js";import{e as W}from"./popper.esm.D0M09MG8.js";import{t as w}from"./translate.yi3aBGOk.js";import{s as k}from"./store.q2AZ-L3y.js";import{u as N,L as X}from"./Loading.ml2CKU1a.js";import{a as q}from"./index.Zkar--a9.js";/* empty css                        */import{_ as Y}from"./_plugin-vue_export-helper.x3n3nnut.js";import{u as A}from"./index.DYBOwIVM.js";import"./index.5btRwMe0.js";const Z={__name:"Contact",props:{contact:{type:Object}},setup(c,{expose:a}){a();const l=c,e=A(k),s=j({email:"",name:"",message:"",phone:""}),{textarea:C,input:o}=q(),d={email:[{type:"email",required:!0}],name:[{type:"string",required:!0}],message:[{type:"string",min:10,required:!0}]},{pass:y,isFinished:S,errorFields:B}=N(s,d),m=i(null),E=i(!1),h=i(!1),b=i(null),v=i(null),P=()=>{k.set({type:e.value.type,slug:e.value.slug,show:!1})},V=r=>{m.value=r.label,v.value=r.email,b.value=r.slack_id};l.contact.topics.length===1&&V(l.contact.topics[0]);const F=x(()=>!h.value&&S.value&&y.value&&!!m.value),T=x(()=>({email:s.email,name:s.name,topicChannel:b.value,topicEmail:v.value,message:`
Topic:  ${m.value}\r

Name: ${s.name}\r

Phone: ${s.phone}\r

Email: ${s.email}\r

Message: ${s.message}\r
            `})),I=()=>{h.value=!0,l.contact.provider&&fetch(`/api/contact-${l.contact.provider}`,{method:"POST",body:JSON.stringify(T.value),headers:{"Content-Type":"application/json"}}).then(r=>r.json()).then(r=>{r.status==="ok"?(_.success(w("contact_thanks")),s.email="",s.name="",s.phone="",s.message="",o.value="",P()):_.error(w("contact_error"))}).catch(r=>{console.log("error",r),_.error(w("contact_error"))}).finally(()=>{h.value=!1})};z(o,r=>{s.message=r},{immediate:!1});const D={props:l,$showDialog:e,form:s,textarea:C,input:o,rules:d,pass:y,isFinished:S,errorFields:B,topic:m,showPopper:E,loading:h,topicChannel:b,topicEmail:v,hide:P,setTopic:V,canSubmit:F,mailData:T,submit:I,ref:i,watch:z,reactive:j,computed:x,get t(){return w},get useStore(){return A},get showDialog(){return k},get useAsyncValidator(){return N},get useTextareaAutosize(){return q},Loading:X,get toast(){return _},get Popper(){return W}};return Object.defineProperty(D,"__isScriptSetup",{enumerable:!1,value:!0}),D}},$=c=>(Q("data-v-d93bb0aa"),c=c(),R(),c),ee={class:"pb-8"},te={class:"subtitle"},oe={key:0,class:"input-group z-20 w-full"},se=["onClick"],ae={class:"peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-primary"},re={class:"input-group"},le={class:"peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-primary"},ne={class:"input-group"},ce={class:"peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-primary"},ie={class:"input-group"},pe={class:"peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-primary"},ue={class:"input-group"},de={class:"peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-primary"},me={class:"pointer-events-none sticky bottom-0 right-5 flex justify-end md:translate-y-10"},he=["disabled"],fe={class:"-mr-1 h-5 w-5",xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink","xml:space":"preserve",style:{"enable-background":"new 0 0 12 12"},viewBox:"0 0 12 12"},ge=$(()=>t("g",{class:"-translate-x-[20%] transition-transform duration-300 group-hover:translate-x-0"},[t("path",{d:"M9.2 6.4 6.4 9.1c-.1.1-.1.4 0 .5s.4.1.5 0l3.4-3.4c.1-.1.1-.4 0-.5L7 2.4c-.1-.1-.4-.1-.5 0-.1.1-.1.4 0 .5l2.7 2.7c.4.4.4.4 0 .8z",fill:"currentColor",stroke:"currentColor","stroke-width":"0.5"}),t("g",null,[t("path",{class:"origin-right -translate-x-[8%] scale-x-0 transition-transform duration-300 group-hover:scale-x-75",d:"M9.6 5.6H1.9c-.2 0-.3.2-.3.4s.2.4.4.4h7.7c.2 0 .4-.2.4-.4s-.3-.4-.5-.4z",fill:"currentColor",stroke:"currentColor","stroke-width":"0.5"})])],-1)),_e=[ge];function we(c,a,l,e,s,C){return p(),u("form",{onSubmit:H(e.submit,["prevent"]),class:"grid gap-4"},[t("div",ee,[t("h2",te,n(l.contact?.title),1),O(c.$slots,"text",{},void 0,!0)]),l.contact.topics.length>1?(p(),u("div",oe,[L(e.Popper,{placement:"bottom-start",offsetDistance:"1",show:e.showPopper,class:"w-full"},{content:M(()=>[t("ul",null,[(p(!0),u(J,null,G(l.contact.topics,(o,d)=>(p(),u("li",{key:d,class:K(e.topic==o.label?"bg-dark bg-opacity-10":"")},[t("button",{type:"button",class:"w-full p-2 text-left hover:bg-dark hover:bg-opacity-10",onClick:y=>{e.setTopic(o),e.showPopper=!1}},n(o.label),9,se)],2))),128))])]),default:M(()=>[t("button",{type:"button",onClick:a[0]||(a[0]=o=>e.showPopper=!e.showPopper),class:"select w-full text-left"},n(e.topic?e.topic:"Select"),1)]),_:1},8,["show"]),t("label",ae,n(e.t("topic"))+" *",1)])):U("",!0),t("div",re,[f(t("input",{type:"text",name:"name",placeholder:" ",class:"peer","onUpdate:modelValue":a[1]||(a[1]=o=>e.form.name=o)},null,512),[[g,e.form.name]]),t("label",le,n(e.t("name"))+" *",1)]),t("div",ne,[f(t("input",{type:"email",name:"email",placeholder:" ",class:"peer","onUpdate:modelValue":a[2]||(a[2]=o=>e.form.email=o)},null,512),[[g,e.form.email]]),t("label",ce,n(e.t("email"))+" *",1)]),t("div",ie,[f(t("input",{type:"text",name:"phone",placeholder:" ",class:"peer","onUpdate:modelValue":a[3]||(a[3]=o=>e.form.phone=o)},null,512),[[g,e.form.phone]]),t("label",pe,n(e.t("phone")),1)]),t("div",ue,[f(t("textarea",{class:"hide-scrollbar peer",name:"message",id:"",placeholder:" ",cols:"30",rows:"2",ref:"textarea","onUpdate:modelValue":a[4]||(a[4]=o=>e.input=o)},null,512),[[g,e.input]]),t("label",de,n(e.t("message"))+" *",1)]),t("div",me,[t("button",{class:"btn surface-primary group pointer-events-auto mb-auto ml-auto",type:"submit",disabled:!e.canSubmit},[t("span",null,n(e.t("submit")),1),(p(),u("svg",fe,_e))],8,he)]),L(e.Loading,{loading:e.loading},null,8,["loading"])],32)}const De=Y(Z,[["render",we],["__scopeId","data-v-d93bb0aa"]]);export{De as default};