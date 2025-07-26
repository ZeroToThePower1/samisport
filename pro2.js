function equation(){
    let operators = ["+", "-","*"];
    let a = Math.floor((Math.random()*100)+1);
    let b = Math.floor((Math.random()*10)+1);
    let c = Math.floor((Math.random()*3));
    let op = operators[c];
    document.getElementById("q").innerText = `${a}${op}${b}=?`;

}
equation()
function checkAnswer(){
    let input = document.getElementById("inputbocsh").value;
    let rightans  = (document.getElementById("q").textContent)
    rightans = rightans.slice(0, rightans.length - 2)
    rightans = Math.floor(eval(rightans))
    input = Math.floor(input)
    if (input == rightans){
        document.getElementById("result").innerText = "result: correct"
        equation()
        document.getElementById("inputbocsh").value = "";
        document.getElementById("inputbocsh").placeholder= "Enter a number"
    }else{
        document.getElementById("result").innerText = "result: incorrect"
    }

}