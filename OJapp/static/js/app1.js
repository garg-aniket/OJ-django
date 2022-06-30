const runCode_btn = document.getElementById("runCode");
const submit_btn = document.getElementById("submit_btn");
const type = document.getElementById("type");
const code = document.getElementById("code");
// const submit_btn = document.getElementById("submit_btn");
const res_div = document.getElementById("cont_result");
const div=document.getElementById("res");
const cusInp=document.getElementById("custominput");
const cusInpVal=document.getElementById("cus_inp_val");
let data={};

// submit_btn.addEventListener("click", () => {
//     eAL.toggle("code");
//     eAL.toggle("code");
//     console.log(code.value);
//     let api=new XMLHttpRequest();
//     api.onload=function (){
//         console.log("ankiet");
//         console.log(JSON.parse(api.response));
//         data=JSON.parse(api.response);
//         console.log(data[0].fields,data[data.length-1].compileMessage);
//     };
//     api.open('post',"/submit",false);
//     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//     api.setRequestHeader("X-CSRFToken", csrftoken);
//     api.send(JSON.stringify({'id': `${submit_btn.value}`,'type':`${type.value}`,'code':`${code.value}`}));
// });

runCode_btn.addEventListener("click", () => {
    eAL.toggle("code");
    eAL.toggle("code");
    let custInpt=cusInpVal.value
    let api=new XMLHttpRequest();
    api.onload=function (){
        console.log("ankiet");
        console.log(JSON.parse(api.response));
        data=JSON.parse(api.response);
        // console.log(data[0].fields,data[data.length-1].compileMessage);
    };
    api.open('post','/runCode',false);
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    api.setRequestHeader("X-CSRFToken", csrftoken);
    api.send(JSON.stringify({'id': `${runCode_btn.value}`,'type':`${type.value}`,'code':`${code.value}`,'custInpt':`${custInpt}`}));

});

cusInp.addEventListener('click',()=>{
    // console.log(toggle);
    // toggle.style.display="none";
    if(cusInp.value==="true"){
        cusInp.value="false";
        div.style.display="none";
    }
    else{
        cusInp.value="true";
        div.style.display="block";
    }
   
});


function tescaseres(value) {
    
    const com_mess = document.getElementById("com_mess");
    console.log(com_mess);
    com_mess.innerHTML="";
    com_mess.innerHTML+=`<span style="color:black">${data[data.length-1].compileMessage[value]}</span>`;
    const inp = document.getElementById("inp");
    const out = document.getElementById("out");
    inp.innerHTML="";
    out.innerHTML="";
    let inputData=data[value].fields.Input.split('\r\n');
    let outputData=data[value].fields.ExpectedOutput.split('\r\n');
    let inpHtml="";
    let outHtml="";
    for(let i=0;i<inputData.length;i++){
        inpHtml+=`<li style="border-left: 1px solid #dfeaec; padding:2px;">
        <span style="color:black">${inputData[i]}</span>
        </li>`
    }
    for(let i=0;i<outputData.length;i++){
        outHtml+=`<li style="border-left: 1px solid #dfeaec; padding:2px;">
        <span style="color:black">${outputData[i]}</span>
        </li>`
    }
    inp.innerHTML=inpHtml;
    out.innerHTML=outHtml;
}

function showResult(){
    eAL.toggle("code");
    eAL.toggle("code");
    console.log(code.value);
    let api=new XMLHttpRequest();
    api.onload=function (){
        console.log("ankiet");
        console.log(JSON.parse(api.response));
        data=JSON.parse(api.response);
        console.log(data[0].fields,data[data.length-1].compileMessage);
    };
    api.open('post',"/submit",false);
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    api.setRequestHeader("X-CSRFToken", csrftoken);
    api.send(JSON.stringify({'id': `${submit_btn.value}`,'type':`${type.value}`,'code':`${code.value}`}));
    
    res_div.innerHTML="";
    console.log(data.length)
    let testCases=data.length-1;
    let li="";
    for(let i=0;i<testCases;i++){
        let result=data[data.length-1].compileMessage[i];
        let color="Red";
        let imgAdd="./static/images/close.png";
        if(result==="Right Answer"){
            color="Green";
            imgAdd="./static/images/check.png";
        }
        li+=`<div style="width: 9em; padding: 0;margin: 0;">    <button id="${i}" style="height: 40px; width: 100%;background-color: white;border-width:0; color:${color}; font-size:large" onclick="tescaseres(${i})" >
        <img src="${imgAdd}" style="width:1em;height:1em;margin-right:1em">
        Test case ${i}
        
    </button>   </div>`;
    }
    res_div.innerHTML+=`<div class="gfg display">
    <div style="font-size:large">
    ${li}
    </div>
    <div style="width:100%;padding:1em;">
        <div style="color:#576871; font-size: large;">
            Compiler Message
            <div class="box" id="com_mess">
            <span style="margin-left:1em;color:black"></span>
            </div>
        </div>
    <div style="color: #576871; font-size:large; margin-top:1em;">
        Input (stdin)
        <div class="box">
            <ol style="margin: 0; padding-left:1.5em;" id="inp">

                <li style="border-left: 1px solid #dfeaec; padding:2px;">
                    <span style="color:black"></span>
                    
                </li>
            </ol>
            </div>
    </div>

    <div style="color: #576871; font-size: large;margin-top:1em;">
        Expected Output
        <div class="box">
            <ol style="margin: 0; padding-left:1.5em;" id="out">
                <li style="border-left: 1px solid #dfeaec; padding:2px;">
                    <span style="color:black">aa</span>
                    
                </li>
            </ol>
            </div>
    </div>
    </div>
</div>
    `;

tescaseres(0);
}

submit_btn.addEventListener('click',showResult);