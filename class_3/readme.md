# 🐍 Python Class-03: Conditionals & Examples

This repository contains Python examples demonstrating conditionals, practical calculators, and a grading system. It covers `if`, `else`, `elif`, nested conditions, and real-life applications.

---

## 1️⃣ The `if` Statement

The `if` statement executes code only if a condition is **True**.

```python
num: int = 10

if num > 0:
    print("The number is positive.")
```

**Output:**

```
The number is positive.
```

---

## 2️⃣ The `else` Statement

The `else` block runs when the `if` condition is **False**.

```python
num: int = -5

if num > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")
```

**Output:**

```
The number is not positive.
```

---

## 3️⃣ The `elif` Statement

`elif` (else if) allows checking **multiple conditions**.

```python
num: int = 0

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

**Output:**

```
The number is zero.
```

---

## 4️⃣ Nested `if` Statement

`if` statements can be **nested** inside another `if`.

```python
num: int = 10

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")
```

**Output:**

```
The number is positive and even.
```

---

## 5️⃣ Practical Example 1 – Simple Calculator

Supports `+`, `-`, `*`, `/` with **basic error handling**.

```python
operation: str = input("Enter Your Operation (+, -, *, /): ")
num1: float = float(input("Enter Your First Number: "))
num2: float = float(input("Enter Your Second Number: "))

if operation == "+":
    print(f"Result: {num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid Operation! Please select from (+, -, *, /)")
```

---

## 6️⃣ Practical Example 2 – Advanced Calculator

Supports `%`, `//`, `**` operations with validation and loop.

```python
def Advance_Calculator():
    while True:
        operation: str = input("Enter Operation (+, -, *, /, //, %, **, or q to quit): ")
        if operation.lower() == 'q':
            print("Exiting Advance Calculator. 👋")
            break
        if operation not in ("+", "-", "*", "/", "//", "%", "**"):
            print("⚠️ Invalid Operation")
            continue
        try:
            num1: float = float(input("Enter First Number: "))
            num2: float = float(input("Enter Second Number: "))
        except ValueError:
            print("⚠️ Please enter valid numbers!")
            continue

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("❌ Division by zero is not allowed!")
                continue
        elif operation == "//":
            if num2 != 0:
                result = num1 // num2
            else:
                print("❌ Division by zero is not allowed!")
                continue
        elif operation == "%":
            if num2 != 0:
                result = num1 % num2
            else:
                print("❌ Division by zero is not allowed!")
                continue
        elif operation == "**":
            result = num1 ** num2

        print(f"✅ Result: {result}")

Advance_Calculator()
```

---

## 7️⃣ Practical Example 3 – Grading System

Assigns grades based on marks (0-100).

```python
def Grading_System(marks):
    if 90 <= marks <= 100:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    else:
        return "Fail"

while True:
    try:
        marks = int(input("Enter your Marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("⚠️ Marks must be between 0 and 100!")
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")

grade = Grading_System(marks)
print(f"🎓 The grade for {marks} marks is: {grade}")
```

---

## ✅ Key Takeaways

* Use `if` to **check conditions**.
* Use `else` for **alternative actions**.
* Use `elif` for **multiple conditions**.
* Nested `if` allows **complex decisions**.
* Practical examples include **calculators and grading systems**.

---

**Author:** Muhammad Awais
**Technologies:** Python 3 🐍
