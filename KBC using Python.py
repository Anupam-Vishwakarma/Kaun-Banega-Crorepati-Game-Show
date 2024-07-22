import time
import os
questions_dict = {
    "What is the most popular programming language in the world?": "Python",
    "What is the primary use of the `git` command?": "Version control",
    "What is the output of the expression `5 + 5` in Python?": "10",
    "What is the purpose of the `try-except` block in Python?": "Error handling",
    "What is the difference between `==` and `===` in JavaScript?": "Type checking",
    "What is the most popular framework for building web applications in Python?": "Django",
    "What is the purpose of the `pip` command in Python?": "Package management",
    "What is the output of the expression `True and False` in Python?": "False",
    "What is the purpose of the `break` statement in Python?": "Exit a loop",
    "What is the difference between `var`, `let`, and `const` in JavaScript?": "Scope and mutability",
    "What is the most popular library for data analysis in Python?": "Pandas",
    "What is the purpose of the `lambda` function in Python?": "Anonymous functions",
    "What is the output of the expression `5 ** 2` in Python?": "25",
    "What is the purpose of the `finally` block in Python?": "Cleanup code",
    "What is the most popular database management system for web applications?": "MySQL",
    "What is the purpose of the `async` keyword in Python?": "Asynchronous programming",
    "What is the output of the expression `not True` in Python?": "False"
}

options_list = [
    ["JavaScript", "C++", "Python", "Java"],
    ["Code execution", "Code debugging", "Version control", "Code compilation"],
    ["20", "15", "10", "5"],
    ["Code debugging", "Code compilation", "Error handling", "Code optimization"],
    ["Syntax checking", "Value checking", "Semantics checking", "Type checking"],
    ["Pyramid", "Bottle", "Flask", "Django"],
    ["Code compilation", "Code debugging", "Package management", "Code execution"],
    ["None", "Error", "True", "False"],
    ["Skip a loop", "Break a loop", "Continue a loop", "Exit a loop"],
    ["Syntax checking", "Value checking", "Scope and mutability", "Type checking"],
    ["SciPy", "Matplotlib", "NumPy", "Pandas"],
    ["Generator functions", "Recursive functions", "Higher-order functions", "Anonymous functions"],
    ["30", "25", "20", "35"],
    ["Code debugging", "Code optimization", "Cleanup code", "Error handling"],
    ["Redis", "MongoDB", "PostgreSQL", "MySQL"],
    ["Concurrent programming", "Parallel programming", "Synchronous programming", "Asynchronous programming"],
    ["Error", "None", "False", "True"]
]
winning_amount_list=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]

def display_question(question, options):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(question)
    time.sleep(3)
    print(options)

def get_user_answer(options):
    while True:
        answer = input("\nNow write your answer:\n")
        if answer or answer.lower in options:
            return answer
        else:
            print("Invalid answer. Please try again.")

def check_answer(answer, correct_answer):
    if answer.lower() == correct_answer.lower():
        return True
    else:
        return False

def play_quiz():
    winning_amount = 0
    for i, key in enumerate(questions_dict.keys()):
        display_question(key, options_list[i])
        answer = get_user_answer(options_list[i])
        if check_answer(answer, list(questions_dict.values())[i]):
            print("\nCongrats! It's the correct answer.")
            winning_amount =winning_amount_list[i]
            print(f"\nYour winnings for now is INR {winning_amount}\n\n")
            time.sleep(5)
        else:
            print("\nOops! It's the wrong answer. Now you can't play further.")
            break
    print(f"Now your play is over.\nYou won INR {winning_amount}")

print("Welcome to the quiz game!")
print("You will be asked a series of questions, and if you answer correctly, you will win a certain amount of money.")
print("If you answer incorrectly, the game will end.")
print()

play_quiz()