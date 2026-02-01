# 2_if_else.py
# This program explains if-else conditions in Python.
# It checks marks and prints the grade accordingly.

print("IF-ELSE EXAMPLE")
print("This program checks marks and prints the grade\n")

marks = 78   # student marks

print("Marks obtained:", marks)

# Checking conditions
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Fail")
