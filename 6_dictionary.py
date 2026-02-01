# 6_dictionary.py
# This program explains dictionaries in Python.
# A dictionary stores data in key-value pairs.

print("DICTIONARY EXAMPLE\n")

# Creating a dictionary
student = {
    "name": "Riya",
    "course": "IT & Data Science",
    "year": 3
}

print("Student Dictionary:")
print(student)

# Accessing values using keys
print("\nAccessing individual values:")
print("Name:", student["name"])
print("Course:", student["course"])
print("Year:", student["year"])

# Using loop with dictionary
print("\nPrinting all key-value pairs:")
for key, value in student.items():
    print(key, ":", value)

# Adding a new key-value pair
student["college"] = "NTTF"

print("\nDictionary after adding college:")
print(student)
