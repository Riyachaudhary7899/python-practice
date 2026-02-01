# 4_functions.py
# This program explains functions in Python in a simple way.
# A function is a block of code that runs only when it is called.

print("FUNCTION EXAMPLE\n")

# Function to greet a user
def greet(name):
    """
    This function takes a name as input
    and prints a greeting message.
    """
    print("Hello", name)

# Function to add two numbers
def add(a, b):
    """
    This function takes two numbers
    and returns their sum.
    """
    return a + b

# Calling the greet function
greet("Riya")

# Calling the add function
result = add(10, 20)
print("Sum of numbers:", result)
