import json
import os
import time

# Load data from JSON files
with open('questions.json') as f:
    questions = json.load(f)

with open('options.json') as f:
    options = json.load(f)

with open('winning_amounts.json') as f:
    winning_amounts = json.load(f)

with open('answers.json') as f:
    answers = json.load(f)

def display_question(question, options):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(question)
    time.sleep(3)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    time.sleep(2)

def get_user_answer(options):
    while True:
        answer = input("\nNow enter the number of your answer:\n")
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print("Invalid answer. Please try again.")

def check_answer(answer, correct_answer):
    if answer.lower() == correct_answer.lower():
        return True
    else:
        return False

def play_quiz():
    winning_amount = 0
    for i, question in enumerate(questions):
        display_question(question, options[i])
        answer = get_user_answer(options[i])
        if check_answer(answer, answers[i]):
            print("\nCongrats! It's the correct answer.")
            winning_amount = winning_amounts[i]
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