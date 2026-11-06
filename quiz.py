import random

questions = [
    ["Which language are we learning?", "Python", "Java", "C++", "A"],
    ["What is 5 + 3?", "8", "10", "15", "A"],
    ["Which function displays output?", "input()", "print()", "int()", "B"],
    ["Which symbol is used for comments?", "#", "//", "$", "A"],
    ["Which data type stores True or False?", "int", "str", "bool", "C"]
]

random.shuffle(questions)

score = 0

print("============================")
print("      PYTHON QUIZ GAME")
print("============================")

for q in questions:
    print("\n" + q[0])
    print("A.", q[1])
    print("B.", q[2])
    print("C.", q[3])

    answer = input("Enter A, B, or C: ").upper()

    if answer == q[4]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")

print("\n======= FINAL RESULT =======")
print("Your score:", score, "out of", len(questions))

if score == len(questions):
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practising!")

print("Thank you for playing!")