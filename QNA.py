import random
import time 
import os
questions = [
    "What does 'ad hoc' mean?",
    "What does 'ad interim' mean?",
    "What does 'à la carte' mean?",
    "What does 'al fresco' mean?",
    "What does 'ad libitum' mean?",
    "What does 'impromptu' mean?",
    "What does 'ad nauseam' mean?",
    "What does 'alibi' mean?",
    "What does 'alter ego' mean?",
    "What does 'au fait' mean?",
    "What does 'erudite' mean?",
    "What does 'prima facie' mean?",
    "What does 'a posteriori' mean?",
    "What does 'déjà vu' mean?",
    "What does 'spouse' mean?",
    "What does 'espouse' mean?",
    "What does 'cara sposa' mean?",
    "What does 'cara sposo' mean?",
    "What does 'bona fide' mean?",
    "What does 'mal fide' mean?",
    "What does 'confidant' mean?",
    "What does 'confidential' mean?",
    "What does 'confidente' mean?",
    "What does 'bête noire' mean?",
    "What does 'café' mean?",
    "What does 'carpe diem' mean?",
    "What does 'casino' mean?",
    "What does 'carte blanche' mean?",
    "What does 'indigent' mean?",
    "What does 'atrocity' mean?",
    "What does 'disseminate' mean?",
    "What does 'sagacious' mean?",
    "What does 'serene' mean?",
    "What does 'pulchritude' mean?",
    "What does 'élan' mean?",
    "What does 'berate' mean?",
    "What does 'surmise' mean?",
    "What does 'covetous' mean?",
    "What does 'deficit' mean?",
    "What does 'integrity' mean?",
    "What does 'normally' mean?",
    "What does 'remedial' mean?",
    "What does 'unnerving' mean?",
    "What does 'remit' mean?",
    "What does 'brazen' mean?",
    "What does 'complacency' mean?",
    "What does 'resorted' mean?",
    "What does 'sparse' mean?",
    "What does 'veteran' mean?",
    "What does 'gossamer' mean?",
    "What does 'soothe' mean?",
    "What does 'grimy' mean?",
    "What does 'stingy' mean?",
    "What does 'sullen' mean?",
    "What does 'anthropogenic' mean?",
    "What does 'daub' mean?",
    "What does 'barbarian' mean?",
    "What does 'adulterate' mean?",
    "What does 'yearn' mean?",
    "What does 'taciturn' mean?",
    "What does 'illegible' mean?",
    "What does 'nabbed' mean?",
    "What does 'inebriated' mean?",
    "What does 'unrelenting' mean?",
    "What does 'anodyne' mean?",
    "What does 'contentious' mean?",
    "What does 'solemn' mean?",
    "What does 'sole' mean?",
    "What does 'scintillant' mean?",
    "What does 'incensed' mean?",
    "What does 'palatial' mean?",
    "What does 'stagger' mean?",
    "What does 'repose' mean?",
    "What does 'grumpy' mean?",
    "What does 'dilatory' mean?",
    "What does 'jeopardy' mean?",
    "What does 'abdicate' mean?",
    "What does 'deluge' mean?",
    "What does 'preponderance' mean?",
    "What does 'barren' mean?",
    "What does 'infamy' mean?",
    "What does 'intrepid' mean?",
    "What does 'prodigal' mean?",
    "What does 'lavish' mean?",
    "What does 'loquacious' mean?",
    "What does 'vindictive' mean?"
]

answers = [
    "Formed for a specific purpose",
    "For the meantime or temporary",
    "Food ordered individually off a menu",
    "In the open air",
    "Freely; at one's pleasure",
    "Done without preparation",
    "To a sickening degree",
    "A claim of being elsewhere when a crime occurred",
    "Another self; close equivalent",
    "Well informed or skilled",
    "Having or showing great knowledge",
    "At first glance; based on first impression",
    "Based on experience",
    "A feeling of having already experienced something",
    "Husband or wife",
    "To support or adopt a cause",
    "Dear wife",
    "Dear husband",
    "Genuine or real",
    "In bad faith; dishonest",
    "A trusted person you share secrets with",
    "Meant to be kept private or secret",
    "A female confidant (also used informally)",
    "A person or thing one strongly dislikes",
    "A small restaurant or coffeehouse",
    "Seize the day",
    "A place for gambling or entertainment",
    "Complete freedom to act as one wishes",
    "Poor or needy",
    "A cruel or violent act",
    "To spread or disperse widely",
    "Wise or having good judgment",
    "Calm and peaceful",
    "Physical beauty",
    "Enthusiasm or flair",
    "To scold angrily",
    "To guess or infer",
    "Greedy or envious",
    "A shortage",
    "Honesty and strong moral principles",
    "In a usual way",
    "Intended to correct or improve",
    "Causing nervousness or anxiety",
    "To send money or payment",
    "Bold and shameless",
    "Self-satisfaction, often without awareness of danger",
    "Turned to as a solution",
    "Scattered or not dense",
    "Experienced and skilled",
    "Light, delicate fabric or texture",
    "To calm or ease pain",
    "Dirty and covered with grime",
    "Unwilling to spend money",
    "Gloomy or bad-tempered",
    "Caused by humans",
    "To smear or coat with a soft substance",
    "A savage or uncivilized person",
    "To make something impure",
    "To long or desire deeply",
    "Habitually silent or uncommunicative",
    "Impossible to read",
    "Caught or arrested suddenly",
    "Drunk or intoxicated",
    "Not giving up or yielding",
    "Not likely to provoke offense; soothing",
    "Causing or likely to cause argument",
    "Serious and dignified",
    "One and only",
    "Sparkling or shining brightly",
    "Very angry",
    "Grand and luxurious",
    "To walk unsteadily",
    "Rest or relaxation",
    "Irritable or in a bad mood",
    "Slow to act or delayed",
    "Danger or risk",
    "To give up power or position",
    "A heavy flood",
    "Greater in number or influence",
    "Unable to produce offspring; lifeless",
    "A state of being well known for a bad reason",
    "Fearless and brave",
    "Wastefully extravagant",
    "Rich and luxurious",
    "Talkative",
    "Revengeful or spiteful"
]

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
        #time.sleep(1)
        print("correct answer")
        #time.sleep(1)
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