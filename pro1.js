const questions = [
  "Who was Mahatma Gandhi?",
  "What is the capital of India?",
  "What does HTML stand for?",
  "Which planet is known as the Red Planet?",
  "Who wrote the play 'Romeo and Juliet'?",
  "What is the boiling point of water in Celsius?",
  "What is 2 + 2?",
  "What gas do plants absorb from the atmosphere?",
  "Who is known as the father of computers?",
  "What is the largest mammal on Earth?"
];

const answers = [
  "He led India to independence through non-violence.",
  "New Delhi",
  "HyperText Markup Language",
  "Mars",
  "William Shakespeare",
  "100°C",
  "4",
  "Carbon Dioxide",
  "Charles Babbage",
  "Blue Whale",
  "i dont know",
  "i wasnt there",
  "what?"
];
let answer = "";
function shuffle(array){
    for (let x = (array.length+1) - 1; x>0; x--){
        let y = Math.floor(Math.random()* (x+1));
        [array[x], array[y]] = [array[x], array[y]];
    }
    
    
    return array;
}
function loadquestions(Qs, ans){
    let j = Math.floor(Math.random()*Qs.length);
    let question = Qs[j];
    answer = ans[j];
    let options = ans.filter(a=> a!==answer);
    options = shuffle(options).slice(0,3);
    let newoptions = options.slice(0,3);
    let randomIndex = Math.floor(Math.random()*4);
    newoptions.splice(randomIndex, 0, answer);
    document.getElementById("question").innerText = `Q. ${question}`
    document.getElementById("o1").innerText = `A. ${newoptions[0]}`;
    document.getElementById("o2").innerText = `B. ${newoptions[1]}`;
    document.getElementById("o3").innerText = `C. ${newoptions[2]}`;
    document.getElementById("o4").innerText = `D. ${newoptions[3]}`;
}
loadquestions(questions, answers)
function checkAnswer(elm){
    selectedtxt = elm.innerText;
    selectedtxt = selectedtxt.slice(3)
    if (selectedtxt === answer){
        document.getElementById("result").innerText = " result: correct"
        loadquestions(questions, answers)


    }else{
        document.getElementById("result").innerText = "result: incorrect"
        loadquestions(questions, answers)
    }

}
