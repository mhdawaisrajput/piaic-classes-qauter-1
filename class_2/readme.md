# 🐍 Python Class – 02

**Author:** Muhammad Awais
**Topics Covered:** Print Statements, Variables, Data Types, Operators, Collections, Conversion, Range

This Python script demonstrates basic Python concepts including variables, data types, operators, and collections. Each section includes examples and outputs.

---

## 🖨️ 1. Simple Print Method

Demonstrates how to use the `print()` function.

```python
print("Hello, I am Muhammad Awais")
```

---

## 📝 2. Variables in Python

Shows variable declaration and conditional assignment.

```python
name = "Muhammad Awais"   # string
age = 24                  # integer
is_student = True         # boolean
student_status = "Yes" if is_student else "No"

print("Name     : ", name)
print("Age      : ", age)
print("Student  : ", student_status)
```

---

## 📊 3. Data Types in Python

Demonstrates different Python data types.

```python
name = "Muhammad Awais"   # str
salary = 30000            # int
age = 24.5                # float
employee = True           # bool

print(f"Name     : {name}     = ", type(name))
print(f"Salary   : {salary}  = ", type(salary))
print(f"Age      : {age}     = ", type(age))
print(f"Employee : {employee} = ", type(employee))
```

---

## ➕ 4. Arithmetic Operators

Basic arithmetic operations in Python.

```python
print("Addition       : 4 + 2 =", 4 + 2)
print("Subtraction    : 4 - 2 =", 4 - 2)
print("Multiplication : 4 * 2 =", 4 * 2)
print("Division       : 4 / 2 =", 4 / 2)
print("Floor Division : 5 // 2 =", 5 // 2)
print("Modulus        : 5 % 2 =", 5 % 2)
print("Exponent       : 5 ** 2 =", 5 ** 2)
```

---

## ⚖️ 5. Comparison Operators

Comparing values using operators.

```python
num1 = 10
num2 = 15

print("Equal To            :", num1 == num2)
print("Not Equal To        :", num1 != num2)
print("Greater Than        :", num1 > num2)
print("Less Than           :", num1 < num2)
print("Greater or Equal To :", num1 >= num2)
print("Less or Equal To    :", num1 <= num2)
```

---

## 📝 6. Assignment Operators

Updating variable values with operators.

```python
num1 = 30
num1 += 5   # 35
num1 -= 5   # 30
num1 *= 5   # 150
num1 /= 5   # 30.0
num1 //= 5  # 6.0
num1 %= 5   # 1.0
num1 **= 5  # 1.0
print(num1)
```

---

## 🔗 7. Logical Operators

Demonstrates `and`, `or`, `not` operators.

```python
a = 10
b = 20
print("Logical AND :", a < b and b > a)
print("Logical OR  :", a == b or b > a)
print("Logical NOT :", not(a == b))
```

---

## 📚 8. List / Tuple / Set

Shows differences between list, tuple, and set.

```python
a = "Muhammad"
print(list(a))   # ordered, allows duplicates, mutable
print(tuple(a))  # ordered, allows duplicates, immutable
print(set(a))    # unordered, removes duplicates, mutable
```

---

## 🔄 9. Conversion of List into Dict

Converting a list of tuples into a dictionary.

```python
data = [("name", "Ali"), ("age", 20)]
print(dict(data))   # {'name': 'Ali', 'age': 20}
```

---

## 🔢 10. Range in Python

Creating sequences using `range()`.

```python
data = list(range(1, 11))       # numbers 1 to 10
data2 = list(range(1, 9))       # numbers 1 to 8
data3 = list(range(3, 30, 3))   # multiples of 3 up to 27
print(data, data2, data3)
```

---

