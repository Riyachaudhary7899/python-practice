# 5_lists.py
# This program explains lists in Python.
# A list is used to store multiple values in a single variable.

print("LIST EXAMPLE\n")

# Creating a list
fruits = ["Apple", "Banana", "Mango"]

print("Original list of fruits:")
print(fruits)

# Accessing list elements
print("\nAccessing elements:")
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Using loop with list
print("\nPrinting fruits using for loop:")
for fruit in fruits:
    print(fruit)

# Adding a new item to the list
fruits.append("Orange")

print("\nList after adding a new fruit:")
print(fruits)
