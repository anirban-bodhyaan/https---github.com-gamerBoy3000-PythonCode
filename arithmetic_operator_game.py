import random

a = random.randint(1, 10)
b = random.randint(1, 10)
operations = ['+', '-', '*', '/', '%', '**', '//']
operation = random.choice(operations)
expression = f"{a} {operation} {b}"
answer = eval(expression)
print(f"What is {expression}?")
user_answer = float(input("Your answer: "))
if user_answer == answer:
    print("Correct!")
else:
    print(f"Wrong! The correct answer is {answer}")

# Repeat this block as many times as needed
