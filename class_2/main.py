# ======================================================
#          🐍 Python Class – 02:
# ======================================================

# ----------------------------------
# Simple Print Method
# ----------------------------------
print("\n----------------------------------")
print("------ Simple Print Method ------")
print("----------------------------------\n")

print("Hello, I am Muhammad Awais")


# ----------------------------------
# Variables in Python
# ----------------------------------
print("\n----------------------------------")
print("------ Variables in Python -------")
print("----------------------------------\n")

name = "Muhammad Awais"   # string
age = 24                  # integer
is_student = True         # boolean
student_status = "Yes" if is_student else "No"

print("Name     : ", name)
print("Age      : ", age)
print("Student  : ", student_status)


# ----------------------------------
# Data Types in Python
# ----------------------------------
print("\n----------------------------------")
print("------ Data Types in Python ------")
print("----------------------------------\n")

name = "Muhammad Awais"   # str
salary = 30000            # int
age = 24.5                # float
employee = True           # bool

print(f"Name     : {name}     = ", type(name))
print(f"Salary   : {salary}  = ", type(salary))
print(f"Age      : {age}     = ", type(age))
print(f"Employee : {employee} = ", type(employee))


# ----------------------------------
# Arithmetic Operators
# ----------------------------------
print("\n----------------------------------")
print("------ Arithmetic Operators ------")
print("----------------------------------\n")

print("Addition       :  4 + 2 = ", 4 + 2)
print("Subtraction    :  4 - 2 = ", 4 - 2)
print("Multiplication :  4 * 2 = ", 4 * 2)
print("Division       :  4 / 2 = ", 4 / 2)
print("Floor Division :  5 // 2 = ", 5 // 2)
print("Modulus        :  5 % 2 = ", 5 % 2)
print("Exponent       :  5 ** 2 = ", 5 ** 2)


# ----------------------------------
# Comparison Operators
# ----------------------------------
print("\n----------------------------------")
print("------ Comparison Operators ------")
print("----------------------------------\n")

num1 = 10
num2 = 15

print("Equal To            : 10 == 15  >>> ", num1 == num2,  ">>>", type(num1 == num2))
print("Not Equal To        : 10 != 15  >>> ", num1 != num2,  ">>>", type(num1 != num2))
print("Greater Than        : 10 > 15   >>> ", num1 > num2,   ">>>", type(num1 > num2))
print("Less Than           : 10 < 15   >>> ", num1 < num2,   ">>>", type(num1 < num2))
print("Greater or Equal To : 10 >= 15  >>> ", num1 >= num2,  ">>>", type(num1 >= num2))
print("Less or Equal To    : 10 <= 15  >>> ", num1 <= num2,  ">>>", type(num1 <= num2))


# ----------------------------------
# Assignment Operators
# ----------------------------------
print("\n----------------------------------")
print("------ Assignment Operators ------")
print("----------------------------------\n")

num1 = 30
num1 += 5
print("Addition Assignment       : ", num1)   # 30 + 5 = 35

num1 -= 5
print("Subtraction Assignment    : ", num1)   # 35 - 5 = 30

num1 *= 5
print("Multiplication Assignment : ", num1)   # 30 * 5 = 150

num1 /= 5
print("Division Assignment       : ", num1)   # 150 / 5 = 30.0

num1 //= 5
print("Floor Division Assignment : ", num1)   # 30.0 // 5 = 6.0

num1 %= 5
print("Modulus Assignment        : ", num1)   # 6.0 % 5 = 1.0

num1 **= 5
print("Exponent Assignment       : ", num1)   # 1.0 ** 5 = 1.0


# ----------------------------------
# Logical Operators
# ----------------------------------
print("\n---------------------------------")
print("------- Logical Operators -------")
print("---------------------------------\n")

a = 10
b = 20

print("a = ", a)
print("b = ", b, "\n")

print("Logical AND : a < b and b > a   >>> ", a < b and b > a)   # True
print("Logical AND : a > b and b < a   >>> ", a > b and b < a)   # False

print("\n")

print("Logical OR  : a == b or b > a   >>> ", a == b or b > a)   # True
print("Logical OR  : a != b or b < a   >>> ", a != b or b < a)   # True

print("\n")

print("Logical NOT : not(a == b)       >>> ", not(a == b))       # True
print("Logical NOT : not(a > b)        >>> ", not(a > b))        # True


# ----------------------------------
# List / Tuple / Set
# ----------------------------------
print("\n---------------------------------")
print("------- List / Tuple / Set ------")
print("---------------------------------\n")

a = "Muhammad"

print(list(a))   # list → ordered ✅ + allows duplicates ✅ + mutable ✅
print(tuple(a))  # tuple → ordered ✅ + allows duplicates ✅ + immutable ❌
print(set(a))    # set → unordered ❌ + removes duplicates ✅ + mutable ✅
                 # Note: order in set is NOT guaranteed


# ----------------------------------
# Conversion of List into Dict
# ----------------------------------
print("\n-----------------------------------------")
print("------ Conversion of List into Dict -----")
print("-----------------------------------------\n")

data = [("name", "Ali"), ("age", 20)]
print("Original List      : ", data)
print("After Dict Convert : ", dict(data))   # {'name': 'Ali', 'age': 20}


# ----------------------------------
# Range in Python
# ----------------------------------
print("\n---------------------------------")
print("-------- Range in Python --------")
print("---------------------------------\n")

# range(start, stop, step) → stop is exclusive (not included)

data = list(range(1, 11))       # numbers 1 to 10
print(data)

print("\n")

data2 = list(range(1, 9))       # numbers 1 to 8
print(data2)

print("\n")

data3 = list(range(3, 30, 3))   # multiples of 3 up to 27
print(data3)
