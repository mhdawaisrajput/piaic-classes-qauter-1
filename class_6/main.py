# ================================================
# 🐍 Python Basics: Class-06
# ================================================


# ======================================================
#       1️⃣ Simple def function — add two numbers:
# ======================================================

def add(num1, num2):
   return num1 + num2

result = add(2,5)
print(result)
# Output: 7

# 🟢 What it does:
# 👉 def add(num1, num2): defines a function named add that takes two parameters.
# 👉 return num1 + num2 returns their sum to the caller.
# 👉 result = add(2,5) calls the function with arguments 2 and 5.
# 👉 print(result) prints the returned value.


# ======================================================
#       2️⃣ Lambda Functions / Anonymous Functions:
# ======================================================

# 🟢 What is a Lambda Function?
# 👉In Python, a lambda function is a small, anonymous function.
# 👉"Anonymous" means it has no name unless we assign it to a variable.
# 👉 Useful when you need a short function for a single task.
#
# Syntax:
#   lambda arguments: expression
#
# Note:
# - Lambda can take multiple arguments
# - But it can only have ONE expression (no multiple lines of code)


# -----------------------------------------------------
# 🟢 Norrmal Function Vs Lambda Function:
# -----------------------------------------------------

# Normal function
def add(x, y):
    return x + y
print(add(5, 3))  # Output: 8

# Same thing with lambda
add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))  # Output: 8

# 👉 Both do the same thing, but lambda is a one-liner.


# -----------------------------------------------------
# 🟢 Single Argument Example
# -----------------------------------------------------

# Function to find square of a number
square = lambda n: n * n
print(square(4))  # Output: 16


# -----------------------------------------------------
# 🟢 Lambda with Conditional (if/else)
# -----------------------------------------------------
# Function to check whether a number is Even or Odd
check_even = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check_even(10))  # Output: Even
print(check_even(7))   # Output: Odd


# -----------------------------------------------------
# 🟢 Lambda with Built-in Functions
# -----------------------------------------------------

# (a) map() → Transformation
# Applies function to each element in a list
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]

# (b) filter() → Selection
# Keeps elements that satisfy a condition
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]

# (c) sorted() → Custom Sorting
# Sorting students based on age (index 1 of tuple)
students = [("Alice", 22), ("Bob", 19), ("Charlie", 25)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# Output: [('Bob', 19), ('Alice', 22), ('Charlie', 25)]


# -----------------------------------------------------
# 🟢 Advanced Use Cases
# -----------------------------------------------------

# (a) Multiple Conditions
# Assign grades as Pass/Fail using lambda
grade = lambda marks: "Pass" if marks >= 50 else "Fail"
print(grade(75))  # Output: Pass
print(grade(40))  # Output: Fail

# (b) Lambda inside reduce()
# reduce() applies a function cumulatively to a sequence
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120


# =====================================================
# ✅ Summary
# - Lambda functions are short, inline functions
# - Syntax: lambda args: expression
# - Useful with map(), filter(), sorted(), reduce()
# - Keep lambdas for simple logic (otherwise use def)
# =====================================================

   
# ===================================================
#          3️⃣ Dictionary Concept in Python 
# ===================================================

# 🟢 What is a Dictionary?
# 👉 A dictionary in Python stores data in key-value pairs.
# 👉 Think of it like:
# 👉 Word  = Key
# 👉 Meaning = Value

# ------------------------------
# 🟢 Simple Example
# ------------------------------
student_data = {
    "name": "Muhammad Awais",
    "age": 24,
    "profession": "Student"
}

# Access full dictionary
print(f"User Data: {student_data}")
# Output: User Data: {'name': 'Muhammad Awais', 'age': 24, 'profession': 'Student'}

# Access specific key-value
print("User Name is:", student_data["name"])     
# Output: User Name is: Muhammad Awais

print("User Age is:", student_data["age"])       
# Output: User Age is: 24

print("User Profession is:", student_data["profession"]) 
# Output: User Profession is: Student


# -----------------------------------------------------
# 🟢 In-Class Task
# 👉 Create advanced dictionary:
# 👉 Add → email, phone_number
# 👉 Store → lambda function (squire = square function)
# -----------------------------------------------------

# Lambda function for square
squire = lambda num1: num1 * num1

# Dictionary with multiple keys and lambda function
user_dict = {
    "name": "Muhammad Awais",
    "roll_number": 12345,
    "age": 24,
    "email": "abc@gmail.com",
    "phone_number": 123456789,
    "squire": squire   # function stored as a value
}

# Accessing normal values
print(f"User Dictionary: {user_dict}")
# Output: User Dictionary: {'name': 'Muhammad Awais', 'roll_number': 12345, 'age': 24, 'email': 'abc@gmail.com', 'phone_number': 123456789, 'squire': <function <lambda> at 0x...>}

print("User Email:", user_dict["email"])  
# Output: User Email: abc@gmail.com

print("User Roll Number:", user_dict["roll_number"]) 
# Output: User Roll Number: 12345


# -----------------------------------------------------
# 🟢 Accessing the lambda function inside dictionary
# -----------------------------------------------------
print("User Squire:", user_dict )
# Output: User Squire: 49

# Another way (store result in variable first)
result = user_dict 
print("User Squire:", result)
# Output: User Squire: 49


# ====================================================
#                  4️⃣ Loops: In Python 
# ====================================================

# 🟢 What is a Loop?
# 👉 A loop is used to repeat a block of code multiple times.
# 👉 In Python, the most common loops are:
#    - for loop
#    - while loop
#
# 🔄 For loop → Runs for each item in a sequence (like list, tuple, string, dict, etc.)
# Syntax:
#   for variable in sequence:
#       # code block


# -----------------------------------------------------
# 🔹 🟢 Class Example: Without Loop (using print again & again)
# -----------------------------------------------------
print("with print")
print("=" * 20)

# Here we are writing the same line manually 10 times
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")

# -----------------------------------------------------
# 🔹 With Loop (efficient way)
# -----------------------------------------------------
print("=" * 20)
print("with loop")
print("=" * 20)

# Using for loop to repeat the same line 10 times
for i in range(10):   # range(10) → 0 to 9 (10 times)
    print("Ainda Homework kar ke aana hai")


# -----------------------------------------------------
# 📝 Output:
# -----------------------------------------------------

# with print
# ====================
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# ====================
# with loop
# ====================
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai
# Ainda Homework kar ke aana hai


# -----------------------------------------------------
# 💡 Note:
# -----------------------------------------------------
# - Without loop → More lines of code, less efficient
# - With loop   → Less code, more efficient, easy to scale
# Example: if you need 1000 repetitions → just change range(10) to range(1000)


# ---------------------------------
# 🟢 Simple Example of For Loop
# ---------------------------------

for i in range(5) :  # range(5) generates numbers 0 to 4
    print("Iteration:", i)
# Output: 0, 1, 2, 3, 4 (each on new line)


# -----------------------------------------------------
# 🟢 Looping Through a List
# -----------------------------------------------------

fruits = ["🍎 Apple", "🍌 Banana", "🍇 Grapes"]
for fruit in fruits:
    print("I like", fruit)
# 🖨️ Output:
# I like 🍎 Apple
# I like 🍌 Banana
# I like 🍇 Grapes


# -----------------------------------------------------
# 🟢 Looping Through a String
# -----------------------------------------------------

for chair in "Python":
    print(chair)
# Output: P, y, t, h, o, n (each on new line)


# -----------------------------------------------------
# 🟢 Using range() in For Loop
# -----------------------------------------------------
# range(start, stop, step)

for number in range(1, 12, 2):
    print(number)
# Output: 1, 3, 5, 7, 9, 11 (each on new line)


# -----------------------------------------------------
# 🟢 Nested For Loops: Loop inside loop
# -----------------------------------------------------

# Outer loop → i goes from 1 to 4
for i in range(1, 5):   
    # Inner loop → j goes from 1 to 3
    for j in range(1, 4):   
        print(f"i = {i} j = {j}")   # Print current values


# -----------------------------------------------------
# 📝 How it Works (Step by Step)
# -----------------------------------------------------

# When i = 1 → inner loop runs with j = 1, 2, 3
# Output:
# i = 1 j = 1
# i = 1 j = 2
# i = 1 j = 3

# When i = 2 → inner loop runs with j = 1, 2, 3
# Output:
# i = 2 j = 1
# i = 2 j = 2
# i = 2 j = 3

# When i = 3 → inner loop runs with j = 1, 2, 3
# Output:
# i = 3 j = 1
# i = 3 j = 2
# i = 3 j = 3

# When i = 4 → inner loop runs with j = 1, 2, 3
# Output:
# i = 4 j = 1
# i = 4 j = 2
# i = 4 j = 3


# -----------------------------------------------------
# ✅ Final Output (all together)
# -----------------------------------------------------
# i = 1 j = 1
# i = 1 j = 2
# i = 1 j = 3
# i = 2 j = 1
# i = 2 j = 2
# i = 2 j = 3
# i = 3 j = 1
# i = 3 j = 2
# i = 3 j = 3
# i = 4 j = 1
# i = 4 j = 2
# i = 4 j = 3


# -----------------------------------------------------
# 💡 Easy Trick to Remember:
# -----------------------------------------------------
# Outer loop (i) = Rows
# Inner loop (j) = Columns
# This code creates a "table" with 4 rows and 3 columns.



# -----------------------------------------------------
# 🟢 For Loop with Dictionary
# -----------------------------------------------------

student = {
    "name": "Muhammad Awais",
    "age": 24,
    "profession": "Student"
}

# Loop through keys:
for key in student:
    print(f"Key = {key}")

# Loop through values:
for value in student.values():
    print(f"Value = {value}")

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key} → {value}")

# 🖨️ Output:
# Key: name
# Key: age
# Key: profession
# Value: Muhammad Awais
# Value: 24
# Value: Student
# name → Muhammad Awais
# age → 24
# profession → Student