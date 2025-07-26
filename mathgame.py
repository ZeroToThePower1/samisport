import random
score = 0
answer = ""
answered = True
while True:
    if answered:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        symbols = ["+", "-", "*"]
        symbol = random.choice(symbols)
        equation = f'{a}{symbol}{b} = ?' 
    print(equation)
    answer = input("Give answer: ")
    try:
        answer = float(answer)
        answered = True
        print(f"Your parsed answer: {answer}")
        if symbol == "+":
            correct_answer = a + b
        elif symbol == "-":
            correct_answer = a - b
        elif symbol == "*":
            correct_answer = a * b
        if answer == correct_answer:
            print("Correct answer")
            score += 1
            print("Your score:", score)
        else:
            print(f"Wrong answer, the correct answer is {correct_answer}")
    except ValueError:
        print("Invalid input. Please make sure you are entering a valid numeric answer.")
        answered = False
    answer = ""