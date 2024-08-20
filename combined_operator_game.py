import random

a = random.randint(1, 20)
b = random.randint(1, 20)
c = random.randint(1, 20)
expression = f"({a} + {b}) > {c} and {a} < {b}"
answer = eval(expression)
print(f"What is {expression}? (True/False)")
user_answer = input("Your answer: ")
if (user_answer.lower() == 'true' and answer) or (user_answer.lower() == 'false' and not answer):
    print("Correct!")
else:
    print(f"Wrong! The correct answer is {answer}")

# Repeat this block as many times as needed
