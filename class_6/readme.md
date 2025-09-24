# 🐍 Python Basics: Class-06


👨‍💻 **Author:** Muhammad Awais

---

## 1️⃣ Simple `def` function — Add two numbers
```python
def add(num1, num2):
   return num1 + num2

result = add(2,5)
print(result)   # Output: 7
```
👉 Defines a function, returns sum, and prints the result.

---

## 2️⃣ Lambda Functions / Anonymous Functions

🔹 **What is Lambda?**
- Small, anonymous (nameless) function
- Syntax: `lambda arguments: expression`
- Useful for short, one-time functions

### Normal Function vs Lambda
```python
def add(x, y):
    return x + y
print(add(5, 3))  # Output: 8

add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))  # Output: 8
```

### Single Argument Example
```python
square = lambda n: n * n
print(square(4))  # Output: 16
```

### With Conditional (if/else)
```python
check_even = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check_even(10))  # Even
print(check_even(7))   # Odd
```

### With Built-in Functions
```python
numbers = [1, 2, 3, 4, 5]

# map()
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# sorted()
students = [("Alice", 22), ("Bob", 19), ("Charlie", 25)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # [('Bob', 19), ('Alice', 22), ('Charlie', 25)]
```

### Advanced Use Cases
```python
# Pass/Fail
grade = lambda marks: "Pass" if marks >= 50 else "Fail"
print(grade(75))  # Pass
print(grade(40))  # Fail

# reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
```

✅ **Summary:** Lambda = short, inline function, best with `map()`, `filter()`, `sorted()`, `reduce()`.

---

## 3️⃣ Dictionary Concept in Python

### Simple Example
```python
student_data = {
    "name": "Muhammad Awais",
    "age": 24,
    "profession": "Student"
}

print(student_data)
print(student_data["name"])       # Muhammad Awais
print(student_data["age"])        # 24
print(student_data["profession"]) # Student
```

### Advanced Dictionary (with Lambda)
```python
squire = lambda num1: num1 * num1

user_dict = {
    "name": "Muhammad Awais",
    "roll_number": 12345,
    "age": 24,
    "email": "abc@gmail.com",
    "phone_number": 123456789,
    "squire": squire
}

print(user_dict["email"])       # abc@gmail.com
print(user_dict["roll_number"]) # 12345
print(user_dict["squire"](7))   # 49
```

---

## 4️⃣ Loops in Python

🔹 **What is a Loop?**
- Repeat a block of code multiple times.
- Common loops: `for`, `while`.

### Without Loop
```python
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
# (repeated many times...)
```

### With Loop
```python
for i in range(10):
    print("Ainda Homework kar ke aana hai")
```

### Simple For Loop
```python
for i in range(5):
    print("Iteration:", i)
```

### Looping Through List
```python
fruits = ["🍎 Apple", "🍌 Banana", "🍇 Grapes"]
for fruit in fruits:
    print("I like", fruit)
```

### Looping Through String
```python
for ch in "Python":
    print(ch)
```

### Using range(start, stop, step)
```python
for number in range(1, 12, 2):
    print(number)
# 1, 3, 5, 7, 9, 11
```

### Nested For Loops
```python
for i in range(1, 5):
    for j in range(1, 4):
        print(f"i = {i} j = {j}")
```
💡 Outer loop = Rows, Inner loop = Columns (table form).

### For Loop with Dictionary
```python
student = {
    "name": "Muhammad Awais",
    "age": 24,
    "profession": "Student"
}

for key in student:
    print("Key:", key)

for value in student.values():
    print("Value:", value)

for key, value in student.items():
    print(f"{key} → {value}")
