# 🐍 Python Basics: Class-04

## 1. Taking Input from the User

The input() function is used to take input from the user.
By default, input() always returns a string.
If we need numbers for mathematical operations, we must convert input into int() or float().
Here, we don’t need conversion since no math is performed.

```python
first_name: str = input("What is your first name: ")
second_name: str = input("What is your second name: ")
age: str = input("What is your age: ")
```

**❌ Common Mistake:**

```python
# first_name = input  ("What is your first name: ")  # Extra spaces will give error.
```

## 2. String Concatenation and f-Strings

```python
# Method 1: Concatenation with commas
print(first_name, second_name, ", and your age is", age)

# Method 2: f-String (modern & preferred way)
print(f"{first_name} {second_name}, and your age is: {age}")
```

## 3. Built-in Functions and Operators

```python
print(1 + 1)         # Arithmetic addition
print("1" + "1")   # String concatenation

# ❌ Mixing string + integer raises an error
# print(1 + "1")
```

## 4. Variables vs Lists

```python
fav_fruit1 = "Mango"
fav_fruit1 = "Orange"
fav_fruit1 = "Grapes"
print(fav_fruit1)  # Output: Grapes
```

**Solution for multiple items:** Use a list.

## 5. Lists in Python

```python
fruits_list: list = ["Mango", "Orange", "Banana", "Grapes"]
print("Before update:", fruits_list)
print("First fruit:", fruits_list[0])

mix_list = ["Mango", 1, 2.5, True]
print("Mixed list:", mix_list)

fruits_list[0] = "Pineapple"
print("After update:", fruits_list)
```

## 6. Common List Methods

```python
fruits_list: list = ["Mango", "Orange", "Banana", "Grapes", "Banana"]

# 1. append()
fruits_list.append("Apple")

# 2. insert()
fruits_list.insert(2, "Cherry")

# 3. pop()
fruits_list.pop()
fruits_list.pop(1)

# 4. remove()
fruits_list.remove("Banana")

# 5. clear()
temp_list = fruits_list.copy()
temp_list.clear()

# 6. count()
banana_count = fruits_list.count("Banana")

# 7. index()
index_of_grapes = fruits_list.index("Grapes")

# 8. sort()
fruits_list.sort()
fruits_list.sort(reverse=True)

# 9. reverse()
fruits_list.reverse()

# 10. copy()
copied_list = fruits_list.copy()

# 11. extend()
more_fruits = ["Papaya", "Peach"]
fruits_list.extend(more_fruits)

# 12. replace (manual)
for i in range(len(fruits_list)):
    if fruits_list[i] == "Banana":
        fruits_list[i] = "Kiwi"
```

## 13. Practical Use Case: Removing by Condition

```python
students = ["Ali", "Sara", "John", "Awais"]
marks = [80, 45, 30, 90]

passed_students = []
for i in range(len(students)):
    if marks[i] >= 50:
        passed_students.append(students[i])

print("Students who passed:", passed_students)
```
