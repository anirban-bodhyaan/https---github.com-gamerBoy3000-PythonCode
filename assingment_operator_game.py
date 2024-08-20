import random

# Initial value
x = random.randint(1, 10)
print("Initial value of x:", x)

# Step 1: Add a random number
add_value = random.randint(1, 10)
print(f"x += {add_value}")
x += add_value

user_answer = int(input("What is the value of x? "))
if user_answer == x:
    print("Correct!")
else:
    print(f"Wrong! The correct value is {x}")

# Step 2: Subtract a random number
sub_value = random.randint(1, 10)
print(f"x -= {sub_value}")
x -= sub_value

user_answer = int(input("What is the value of x? "))
if user_answer == x:
    print("Correct!")
else:
    print(f"Wrong! The correct value is {x}")

# Step 3: Multiply by a random number
mul_value = random.randint(1, 5)
print(f"x *= {mul_value}")
x *= mul_value

user_answer = int(input("What is the value of x? "))
if user_answer == x:
    print("Correct!")
else:
    print(f"Wrong! The correct value is {x}")

# Step 4: Divide by a random number
div_value = random.randint(1, 5)
print(f"x /= {div_value}")
x /= div_value

user_answer = float(input("What is the value of x? (Enter a decimal number) "))
if user_answer == x:
    print("Correct!")
else:
    print(f"Wrong! The correct value is {x}")

# Step 5: Modulus by a random number
mod_value = random.randint(1, 10)
print(f"x %= {mod_value}")
x %= mod_value

user_answer = float(input("What is the value of x? (Enter a decimal number) "))
if user_answer == x:
    print("Correct!")
else:
    print(f"Wrong! The correct value is {x}")

# Step 6: Floor Division by a random number
floor_div_value = random.randint(1, 5)
print(f"x //= {floor_div_value}")
x //= floor_div_value

user_answer = int(input("What is the value of x? "))
if user_answer == x:
    print("Correct!")
else:
    print(f"Wrong! The correct value is {x}")

# Step 7: Exponentiation by a random number
exp_value = random.randint(1, 3)
print(f"x **= {exp_value}")
x **= exp_value

user_answer = int(input("What is the value of x? "))
if user_answer == x:
    print("Correct!")
else:
    print(f"Wrong! The correct value is {x}")

print("Game over! Great job practicing assignment operators.")
