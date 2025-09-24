# 🐍 Python Basics: Class-04

**Author:** Muhammad Awais

## 1. Taking Input from the User

The input() function is used to take input from the user.
By default, input() always returns a string.
If we need numbers for mathematical operations, we must convert input into int() or float().
Here, we don’t need conversion since no math is performed.

```python
first_name: str = input("What is your first name: ")  # e.g., Awais
second_name: str = input("What is your second name: ") # e.g., Rajput
age: str = input("What is your age: ")               # e.g., 22
```

**Output:**

```
What is your first name: Awais
What is your second name: Rajput
What is your age: 22
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

**Output:**

```
Awais Rajput , and your age is 22
Awais Rajput, and your age is: 22
```

## 3. Built-in Functions and Operators

```python
print(1 + 1)         # Arithmetic addition
print("1" + "1")   # String concatenation
```

**Output:**

```
2
11
```

## 4. Variables vs Lists

```python
fav_fruit1 = "Mango"
fav_fruit1 = "Orange"
fav_fruit1 = "Grapes"
print(fav_fruit1)
```

**Output:**

```
Grapes
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

**Output:**

```
Before update: ['Mango', 'Orange', 'Banana', 'Grapes']
First fruit: Mango
Mixed list: ['Mango', 1, 2.5, True]
After update: ['Pineapple', 'Orange', 'Banana', 'Grapes']
```

## 6. Common List Methods

```python
fruits_list: list = ["Mango", "Orange", "Banana", "Grapes", "Banana"]
fruits_list.append("Apple")
fruits_list.insert(2, "Cherry")
fruits_list.pop()
fruits_list.pop(1)
fruits_list.remove("Banana")
temp_list = fruits_list.copy()
temp_list.clear()
banana_count = fruits_list.count("Banana")
index_of_grapes = fruits_list.index("Grapes")
fruits_list.sort()
fruits_list.sort(reverse=True)
fruits_list.reverse()
copied_list = fruits_list.copy()
more_fruits = ["Papaya", "Peach"]
fruits_list.extend(more_fruits)
for i in range(len(fruits_list)):
    if fruits_list[i] == "Banana":
        fruits_list[i] = "Kiwi"
```

**Output:**

```
After append: ['Mango', 'Orange', 'Banana', 'Grapes', 'Banana', 'Apple']
After insert: ['Mango', 'Orange', 'Cherry', 'Banana', 'Grapes', 'Banana', 'Apple']
After pop (last removed): ['Mango', 'Orange', 'Cherry', 'Banana', 'Grapes', 'Banana']
After pop(index=1): ['Mango', 'Cherry', 'Banana', 'Grapes', 'Banana']
After remove('Banana'): ['Mango', 'Cherry', 'Grapes', 'Banana']
After clear: []
Banana count: 1
Index of Grapes: 2
After sort: ['Banana', 'Cherry', 'Grapes', 'Mango']
After sort(reverse=True): ['Mango', 'Grapes', 'Cherry', 'Banana']
After reverse: ['Banana', 'Cherry', 'Grapes', 'Mango']
Copied list: ['Banana', 'Cherry', 'Grapes', 'Mango']
After extend: ['Banana', 'Cherry', 'Grapes', 'Mango', 'Papaya', 'Peach']
After replacing Banana → Kiwi: ['Kiwi', 'Cherry', 'Grapes', 'Mango', 'Papaya', 'Peach']
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

**Output:**

```
Students who passed: ['Ali', 'Awais']
```
