import random
import os
import time

# List of 50 Hinglish Questions
questions = [
    "Epithelial tissue ka mukhya karya kya hai?",
    "Konsa epithelial tissue alveoli mein paya jata hai?",
    "Tendons kis type ke connective tissue hote hain?",
    "Blood ko connective tissue kyon mana jata hai?",
    "Earthworm ke sharir mein kitne segments hote hain?",
    "Cockroach ka exoskeleton kis substance ka bana hota hai?",
    "Frog ke heart mein kitne chambers hote hain?",
    "Neuron ka kary kya hai?",
    "Konsa muscle involuntary aur striated hota hai?",
    "Adipose tissue ka mukhya karya kya hai?",
    "Earthworm mein digestion ka antim stap kya hai?",
    "Cockroach mein respiration kaise hota hai?",
    "Frog mein external fertilization kahan hota hai?",
    "Konsa epithelial tissue urinary bladder mein paya jata hai?",
    "Cartilage aur bone mein kya antar hai?",
    "Earthworm ke circulatory system ka type kya hai?",
    "Cockroach ke digestive system mein kis organ se food grind hota hai?",
    "Frog ke respiratory organs kaunse hain?",
    "Simple squamous epithelium kahan paya jata hai?",
    "Lymph ka karya kya hai?",
    "Earthworm ke nervous system mein kya hota hai?",
    "Cockroach ke reproductive system kaise identify karte hain?",
    "Frog ke heart mein oxygenated aur deoxygenated blood mix kyon hota hai?",
    "Stratified epithelium kahan paya jata hai?",
    "Bone mein calcium deposit kis form mein hota hai?",
    "Earthworm mein clitellum ka karya kya hai?",
    "Cockroach ke malpighian tubules ka karya kya hai?",
    "Frog ke skin ka color kyon change hota hai?",
    "Columnar epithelium kahan paya jata hai?",
    "Plasma mein paye jane wale proteins ka naam batao",
    "Earthworm ke excretory system ka naam kya hai?",
    "Cockroach ke antennae ka karya kya hai?",
    "Frog ke digestive system ka antim hissa kya hai?",
    "Cuboidal epithelium kahan paya jata hai?",
    "Blood platelets ka karya kya hai?",
    "Earthworm ke setae ka karya kya hai?",
    "Cockroach ke heart ka structure kaisa hota hai?",
    "Frog ke tadpole mein respiration kaise hota hai?",
    "Transitional epithelium kahan paya jata hai?",
    "Osteocytes kahan paye jate hain?",
    "Earthworm ke alimentary canal ka sabse lamba hissa kaun sa hai?",
    "Cockroach ke compound eyes ka karya kya hai?",
    "Frog ke cloaca ka karya kya hai?",
    "Glandular epithelium ka example dijiye",
    "Collagen fibers kis tissue mein paye jate hain?",
    "Earthworm ke reproduction mein clitellum ka role kya hai?",
    "Cockroach ke legs mein kitne segments hote hain?",
    "Frog ke liver ka karya kya hai?",
    "Pseudostratified epithelium kahan paya jata hai?",
    "Areolar tissue kis organ mein paya jata hai?"
]

# Corresponding Answers (same index as questions)
answers = [
    "Protection, secretion, absorption",
    "Simple squamous epithelium",
    "Dense connective tissue",
    "Kyonki ye plasma aur cells ko connect karta hai",
    "100-120 segments",
    "Chitin",
    "3 chambers",
    "Electrical signals transmit karna",
    "Cardiac muscle",
    "Fat store karna",
    "Intestine mein digestion",
    "Tracheal tubes aur spiracles se",
    "Water mein",
    "Transitional epithelium",
    "Cartilage flexible hota hai, bone rigid",
    "Closed circulatory system",
    "Gizzard",
    "Skin, lungs, buccal cavity",
    "Alveoli aur blood vessels mein",
    "Immunity aur fluid balance maintain karna",
    "Ganglia aur ventral nerve cord",
    "Male mein testes, female mein ovaries",
    "Kyonki ventricle ek hi hota hai",
    "Skin mein",
    "Calcium phosphate",
    "Cocoon formation mein help karna",
    "Excretion",
    "Chromatophores ki wajah se",
    "Intestine mein",
    "Albumin, globulin, fibrinogen",
    "Nephridia",
    "Smell aur touch detect karna",
    "Cloaca",
    "Kidney tubules mein",
    "Blood clotting",
    "Movement mein help karna",
    "13-chambered",
    "Gills se",
    "Urinary bladder mein",
    "Bone mein",
    "Intestine",
    "Light detect karna",
    "Waste elimination aur reproduction",
    "Goblet cells",
    "Tendons aur ligaments mein",
    "Cocoon secrete karna",
    "6 segments",
    "Bile produce karna",
    "Trachea mein",
    "Skin ke niche"
]

# Rest of your code remains the same...
total_questions = len(questions)
def choose(list):
    n = random.choice(list)
    list.remove(n)
    return n
def arrange(list, input):
    abcd =["A","B","C","D"]
    ABCD =["a","b","c","d"]
    if input in abcd:
        g = abcd.index(input)
        return list[g]
    if input in ABCD:
        g = ABCD.index(input)
        return list[g]
    else:
        return input
qn = 1
bquestions =[]
os.system("cls" if os.name == "nt" else "clear")
while total_questions != 0:
    question = random.choice(questions)
    if question in bquestions:
         question = random.choice(questions)
        
    indexofquestion = questions.index(question)
    correct_answer = answers[indexofquestion]
    options = [a for a in answers if a != correct_answer]
    options = [choose(options), choose(options), choose(options), correct_answer]
    random.shuffle(options)
    print(f'Q{qn}.{question}')
    print(f'A.{options[0]}')
    print(f'B.{options[1]}')
    print(f'C.{options[2]}')
    print(f'D.{options[3]}')
    INPUT = input('give answer: ')
    INPUT = arrange(options, INPUT)
    if INPUT == correct_answer:
        print("correct answer")
        os.system("cls" if os.name == "nt" else "clear")
    else:
        time.sleep(1)
        print("wrong answer")
        time.sleep(1)
        print("the correct answer is", correct_answer)
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")

    total_questions-=1
    questions.pop(indexofquestion)
    answers.pop(indexofquestion)
    qn+=1