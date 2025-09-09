# 🐍 Python Basics: Class-04

**Author: Muhammad Awais**

---

## 📌 1. Taking Input from the User

```python
# The input() function is used to take input from the user.
# By default, input() always returns a string.
# If we need numbers for mathematical operations, we must convert input into int() or float().
# In this example, we only collect string data, so no conversion is needed.
first_name: str = input("What is your first name: ")
second_name: str = input("What is your second name: ")
age: str = input("What is your age: ")
```

---

## 📌 2. String Concatenation and f-Strings

```python
# Method 1: Using commas in print()
# This automatically adds a space between variables and strings.
print(first_name, second_name, ", and your age is", age)

# Method 2: Using f-Strings (preferred modern method)
# f-Strings allow embedding variables directly into strings for cleaner output.
print(f"{first_name} {second_name}, and your age is: {age}")
```

---

## 📌 3. Built-in Functions and Operators

```python
# Demonstrates basic arithmetic addition
print(1 + 1)         # Output: 2

# Demonstrates string concatenation
print("1" + "1")     # Output: "11"

# ❌ Mixing string and integer will raise an error
# print(1 + "1")
```

---

## 📌 4. Variables vs Lists

```python
# Simple variable reassignment example
fav_fruit1 = "Mango"
fav_fruit1 = "Orange"
print(fav_fruit1)   # Output: Orange

# Using separate variables for many items is inefficient.
# Lists provide a better solution for storing multiple items.
```

---

## 📌 5. Lists in Python

```python
# Lists are mutable and ordered collections of items.
# They can contain mixed data types.
fruits_list: list = ["Mango", "Orange", "Banana", "Grapes"]
print("Before update:", fruits_list)
print("First fruit:", fruits_list[0])

# Example of a mixed data type list
mix_list = ["Mango", 1, 2.5, True]
print("Mixed list:", mix_list)

# Updating list elements demonstrates mutability
fruits_list[0] = "Pineapple"
print("After update:", fruits_list)
```

---

## 📌 6. Common List Methods

```python
# Demonstrates commonly used list methods
fruits_list: list = ["Mango", "Orange", "Banana", "Grapes", "Banana"]

# append(): Adds an element at the end of the list
fruits_list.append("Apple")

# insert(): Inserts an element at a specified index
fruits_list.insert(2, "Cherry")

# pop(): Removes the last element by default or element at specified index
fruits_list.pop()
fruits_list.pop(1)

# remove(): Removes the first occurrence of a value
fruits_list.remove("Banana")

# clear(): Removes all elements from the list
fruits_list.clear()

# count(): Counts occurrences of a specific value
banana_count = fruits_list.count("Banana")

# index(): Returns the index of the first occurrence of a value
idx = fruits_list.index("Grapes")

# sort(): Sorts the list in ascending order
fruits_list.sort()

# reverse(): Reverses the order of elements
fruits_list.reverse()

# copy(): Creates a copy of the list
copy_list = fruits_list.copy()

# extend(): Adds elements from another list
fruits_list.extend(["Papaya"])
```

---

## 📌 7. Replace in List (Manual)

```python
# Python lists do not have a direct replace() method.
# We can manually replace elements using a loop.
for i in range(len(fruits_list)):
    if fruits_list[i] == "Banana":
        fruits_list[i] = "Kiwi"
```

---

## 📌 8. Practical Use Case (Removing by Condition)

```python
# Example: Remove failing students conditionally
students = ["Ali", "Sara", "John", "Awais"]
marks = [80, 45, 30, 90]  # Passing mark = 50

passed_students = []
for i in range(len(students)):
    if marks[i] >= 50:
        passed_students.append(students[i])

print("Students who passed:", passed_students)
```
