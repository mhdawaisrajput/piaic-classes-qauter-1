# 🐍 Python Basics: Class-05

👨‍💻 Author: Muhammad Awais 😊

---

## 📌 1. Functions: Defining and Calling

### A simple function without parameters

```python
def main():
    print("Hello, World!")
    print("Welcome to Python programming.")

main()  # Output → Hello, World! \n Welcome to Python programming.
```

### Function with one parameter

```python
def main(emojy):
    print(f"Hello, {emojy}!")

main("😊")  # Output → Hello, 😊!
```

---

## 📌 2. Returning Values from Functions with Parameters

### Function with two parameters (sum)

```python
def add(a, b):
    return a + b

print(add(2, 4))  # Output → 6
```

### Function with two parameters (multiplication)

```python
def multiply(a, b):
    return a * b

print(multiply(3, 5))  # Output → 15
```

### Function with default parameter

```python
def emojy(value="🔒"):
    return value

print(emojy())       # Output → 🔒
print(emojy("🔑"))   # Output → 🔑
```

---

## 📌 3. Positional vs Keyword Arguments

### Calculator Example

```python
def calculator(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2

# Positional arguments (order matters)
print(calculator(10, 5))   # Output → (15, 5, 50, 2.0)
print(calculator(5, 10))   # Output → (15, -5, 50, 0.5)

# Keyword arguments (order does not matter)
print(calculator(num1=10, num2=5))  # Output → (15, 5, 50, 2.0)
print(calculator(num2=5, num1=10))  # Output → (15, 5, 50, 2.0)

# ❌ Error: mixing same parameter
# calculator(5, num1=10) → TypeError

# ✅ Valid mixed usage
print(calculator(10, num2=5))  # Output → (15, 5, 50, 2.0)

# ❌ Invalid: positional after keyword
# calculator(num2=5, 10) → SyntaxError
```

---

## 📌 4. Parameter Kinds (Python 3.8+)

### Normal Parameters (positional or keyword)

```python
def greet(name, emoji):
    print(f"Hello {name} {emoji}")

# Both work
greet("Awais", "😊")                # Positional
greet(name="Awais", emoji="😊")    # Keyword
```

### A) Positional-Only Parameters (`/`)

```python
def add(a, b, /):
    return a + b

print(add(2, 3))      # ✅ OK
# add(a=2, b=3)       # ❌ Error → cannot use keywords
```

### B) Keyword-Only Parameters (`*`)

```python
def multiply(*, x, y):
    return x * y

print(multiply(x=4, y=5))  # ✅ OK
# multiply(4, 5)           # ❌ Error → must use keywords
```

### C) Mixed Parameters (`/` and `*`)

```python
def calculator(a, b, /, c=1, *, d=1):
    return (a + b) * c * d

print(calculator(2, 3))              # Output → 5
print(calculator(2, 3, 2))           # Output → 10
print(calculator(2, 3, c=2, d=3))    # Output → 30

# ❌ Errors:
# calculator(a=2, b=3) → a & b must be positional
# calculator(2, 3, 2, 3) → d must be keyword
```

---

✨ End of Class-05 Notes — by Muhammad Awais 😊
