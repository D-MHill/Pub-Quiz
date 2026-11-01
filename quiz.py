name = input("enter your name  ")

print(f"Welcome to the pub quiz, {name}! Have fun!")

questions = [
    #Question 1 
    {"question1": "Which of the following is NOT a primary colour?"},
    {"A": "Red", "B": "white", "C": "Blue"}
]

print(questions[0]["question1"])

answer1 = input("Your answer: ") 

if answer1.lower() == questions[1]["B"].lower():
    print("Correct!")

else:
    print(f"Incorrect! The correct answer was {questions[1]["B"]}")