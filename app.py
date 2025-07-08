# This is a simple Python program that prints "Hello, World!" to the console.

def hello_world():
    print("Hello, World!")

# Call the function to execute it
hello_world()

# --- Another simple example: A function that adds two numbers ---

def add_numbers(a. b):
    """
    This function takes two numbers as input and returns their sum.
    """
    return a

# Call the function with some values
num1 = 10
num2 = 5
sum_result = add_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is: {sum_result}")

# --- Example of a simple loop ---

print("\nCounting from 1 to 5:")
for i in range(1, 6): # range(1, 6) generates numbers from 1 up to (but not including) 6
    print(i)

# --- Example of conditional statements ---

age = 20

if age >= 18:
    print("\nYou are an adult.")
else:
    print("\nYou are a minor.")
