# =====================================================
# 🐍 Python Basics: Class-04:
# =====================================================

# -----------------------------------------------------
# 1. Taking Input from the User
# -----------------------------------------------------

# The input() function is used to take input from the user.
# By default, input() always returns a string.
# If we need numbers for mathematical operations, 
# we must convert input into int() or float().
# Here, we don’t need conversion since no math is performed.

first_name: str = input("What is your first name: ")
second_name: str = input("What is your second name: ")
age: str = input("What is your age: ")

# ❌ Common Mistake:
# first_name = input  ("What is your first name: ")  
#     ↑↑ Extra spaces between input and () will give error.

#   first_name = input  ("What is your first name: ")   >>> give error
#     ↑↑ Extra spaces after variable will also give error.



# -----------------------------------------------------
# 2. String Concatenation and f-Strings
# -----------------------------------------------------

# 🔹 Method 1: Concatenation with commas in print()
print(first_name, second_name, ", and your age is", age)

# 🔹 Method 2: f-String (modern & preferred way)
# f-Strings allow embedding variables directly in strings.
print(f"{first_name} {second_name}, and your age is: {age}")

# Note: We use snack_case for variable names in Python (e.g., my_name).


# -----------------------------------------------------
# 3. Built-in Functions and Operators
# -----------------------------------------------------

# Always use parentheses/Round-Brackets () when calling a built-in function in python like print(), input(), int(), etc.

print(1 + 1)         # Arithmetic addition (results in 2)
print("1" + "1")     # String concatenation (results in "11")

# ❌ Mixing string + integer raises an error in Python
# print(1 + "1")  
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ⚡ NOTE: In JavaScript, "1" + 1 would give "11" (implicit conversion).


# -----------------------------------------------------
# 4. Variables vs Lists
# -----------------------------------------------------

# Example with simple variable reassignment
fav_fruit1 = "Mango"
fav_fruit1 = "Orange"
fav_fruit1 = "Grapes"
print(fav_fruit1)   # Output: Grapes (last value overrides previous one)

fav_fruit1 = "Mango"
print(fav_fruit1)   # Output: Mango

fav_fruit2 = "Orange"
print(fav_fruit2)  # Output: Orange


# ❌ Problem: If we had 100 fruits, we would need 100 variables.
# ✅ Solution: Use a List (a data structure that stores multiple values).


# -----------------------------------------------------
# 5. Lists in Python
# -----------------------------------------------------

# Lists are:
# - Mutable (can be changed after creation)
# - Ordered (items have fixed order with indexes)
# - Can contain mixed data types

# Index positions:      0        1         2         3
fruits_list: list = ["Mango", "Orange", "Banana", "Grapes"]
print("Before update:", fruits_list)    # Output: ['Mango', 'Orange', 'Banana', 'Grapes']
print("First fruit:", fruits_list[0])  # Access by index → "Mango"

# Example of mixed data types in a list
mix_list = ["Mango", 1, 2.5, True]
print("Mixed list:", mix_list)

# Updating list values (mutability)
fruits_list[0] = "Pineapple"  # Replaces "Mango" with "Pineapple"
print("After update:", fruits_list) # Output: ['Pineapple', 'Orange', 'Banana', 'Grapes']


# -----------------------------------------------------
# 6. Common List Methods
# -----------------------------------------------------


# Let's start with a simple list of fruits:
fruits_list: list = ["Mango", "Orange", "Banana", "Grapes", "Banana"] 
print("Original fruits_list:", fruits_list)            
# Output: ['Mango', 'Orange', 'Banana', 'Grapes', 'Banana']

# -----------------------------------------------------
# 1. append() → Add an element at the end
# -----------------------------------------------------
fruits_list.append("Apple")
print("After append:", fruits_list)
# Output: ['Mango', 'Orange', 'Banana', 'Grapes', 'Banana', 'Apple']

# -----------------------------------------------------
# 2. insert() → Insert element at specific index
# -----------------------------------------------------
fruits_list.insert(2, "Cherry")   # Adds "Cherry" at index 2
print("After insert:", fruits_list)
# Output: ['Mango', 'Orange', 'Cherry', 'Banana', 'Grapes', 'Banana', 'Apple']

# -----------------------------------------------------
# 3. pop() → Remove element by index (default = last)
# -----------------------------------------------------
fruits_list.pop()   # Removes last element "Apple"
print("After pop (last removed):", fruits_list)
# Output: ['Mango', 'Orange', 'Cherry', 'Banana', 'Grapes', 'Banana']

fruits_list.pop(1)  # Removes element at index 1 ("Orange")
print("After pop(index=1):", fruits_list)
# Output: ['Mango', 'Cherry', 'Banana', 'Grapes', 'Banana']

# -----------------------------------------------------
# 4. remove() → Remove first occurrence of a value
# -----------------------------------------------------
fruits_list.remove("Banana")   # Removes the first "Banana"
print("After remove('Banana'):", fruits_list)
# Output: ['Mango', 'Cherry', 'Grapes', 'Banana']

# -----------------------------------------------------
# 5. clear() → Remove all elements (empty the list)
# -----------------------------------------------------
temp_list = fruits_list.copy()  # Make a copy before clearing
temp_list.clear()
print("After clear:", temp_list)
# Output: []

# -----------------------------------------------------
# 6. count() → Count how many times a value appears
# -----------------------------------------------------
banana_count = fruits_list.count("Banana")
print("Banana count:", banana_count)
# Output: 1

# -----------------------------------------------------
# 7. index() → Find the index of the first occurrence
# -----------------------------------------------------
index_of_grapes = fruits_list.index("Grapes")
print("Index of Grapes:", index_of_grapes)
# Output: 2

# -----------------------------------------------------
# 8. sort() → Sorts list in ascending order (A–Z or small→big)
# -----------------------------------------------------
fruits_list.sort()
print("After sort:", fruits_list)
# Output: ['Banana', 'Cherry', 'Grapes', 'Mango']

# Sort in descending order
fruits_list.sort(reverse=True)
print("After sort(reverse=True):", fruits_list)
# Output: ['Mango', 'Grapes', 'Cherry', 'Banana']

# -----------------------------------------------------
# 9. reverse() → Reverse the order of the list
# -----------------------------------------------------
fruits_list.reverse()
print("After reverse:", fruits_list)
# Output: ['Banana', 'Cherry', 'Grapes', 'Mango']

# -----------------------------------------------------
# 10. copy() → Make a duplicate (to avoid modifying original)
# -----------------------------------------------------
copied_list = fruits_list.copy()
print("Copied list:", copied_list)
# Output: ['Banana', 'Cherry', 'Grapes', 'Mango']

# -----------------------------------------------------
# 11. extend() → Join two lists
# -----------------------------------------------------
more_fruits = ["Papaya", "Peach"]
fruits_list.extend(more_fruits)
print("After extend:", fruits_list)
# Output: ['Banana', 'Cherry', 'Grapes', 'Mango', 'Papaya', 'Peach']

# -----------------------------------------------------
# 12. replace (Manual, since no direct replace method)
# -----------------------------------------------------
# Python lists do NOT have a direct replace() method like strings.
# But we can replace elements by index or using a loop.

# Example: Replace "Banana" with "Kiwi"
for i in range(len(fruits_list)):
    if fruits_list[i] == "Banana":
        fruits_list[i] = "Kiwi"

print("After replacing Banana → Kiwi:", fruits_list)
# Output: ['Kiwi', 'Cherry', 'Grapes', 'Mango', 'Papaya', 'Peach']


# -----------------------------------------------------
# 13. Practical Use Case of Removing by Condition
# -----------------------------------------------------

# Example Scenario:
# Suppose we have a list of students' marks and we want to remove those who failed.
# While we could directly remove items from the list,
# in this case, we will remove them conditionally.
# For instance, remove students from the PIAIC portal only if they are failing; 
# otherwise, keep them.


students = ["Ali", "Sara", "John", "Awais"]
marks = [80, 45, 30, 90]  # Passing mark = 50

# Removing failed students conditionally
passed_students = []
for i in range(len(students)):
    if marks[i] >= 50:
        passed_students.append(students[i])

print("Students who passed:", passed_students)
# Output: ['Ali', 'Awais']