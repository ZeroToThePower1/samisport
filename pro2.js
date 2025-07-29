
let inn = document.getElementById('in')
function equation(){

    let operators = ["+", "-","*"];
    let a = Math.floor((Math.random()*100)+1);
    let b = Math.floor((Math.random()*10)+1);
    let c = Math.floor((Math.random()*3));
    let op = operators[c];

    document.getElementById("q").innerText = `${a}${op}${b}=?`;

}
equation()
inn.addEventListener("input", (e)=>{
    let ques = document.getElementById('q').innerText
    ques = ques.substring(0, (ques.length -2))
    const val = inn.value;
    if (val == eval(ques)){
        equation()
        inn.value = '';
    }
})