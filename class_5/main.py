# =====================================================
# 🐍 Python Basics: Class-05
# =====================================================

# -----------------------------------------------------
# 1. Functions: Defining and Calling
# -----------------------------------------------------

# A simple function without parameters
def main():
    print("Hello, World!")
    print("Welcome to Python programming.")

# Function call → executes code inside main()
main()  
# Output:
# Hello, World!
# Welcome to Python programming.


# Function with one parameter
def main(emojy):
    print(f"Hello, {emojy}!")

main("😊")  
# Output: Hello, 😊!


# -----------------------------------------------------
# 2. Returning Values from Functions with Parameters
# -----------------------------------------------------

# Function with two parameters, returns their sum
def add(a, b):
    # Here: a and b are parameters
    return a + b

result = add(2, 4)     # arguments passed → a=2, b=4
print(result)          # Output: 6


# Another function, returns multiplication
def multiply(a, b):
    return a * b

result = multiply(3, 5)
print(result)          # Output: 15


# Function with default parameter
def emojy(value="🔒"):
    return value

result1 = emojy()       # No argument passed → uses default
result2 = emojy("🔑")   # Argument overrides default

print(result1)          # Output: 🔒
print(result2)          # Output: 🔑


# -----------------------------------------------------
# 3. Positional vs Keyword Arguments
# -----------------------------------------------------

def calculator(num1, num2):
    """Returns tuple of (sum, difference, product, division)."""
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2

# --- Using positional arguments (order matters)
result = calculator(10,  5)  
#                 num1, num2
print(result)           
# Output: (15, 5, 50, 2.0)

result = calculator(5,   10)
#                 num1, num2
print(result)
# Output: (15, -5, 50, 0.5)


# --- Using keyword arguments (order does NOT matter)
result = calculator(num1=10, num2=5)  
print(result)           
# Output: (15, 5, 50, 2.0)

result = calculator(num2=5, num1=10)  
print(result)           
# Output: (15, 5, 50, 2.0)


# result = calculator(5, num1=10)
# print(result)

# Error: This part will cause an error in your code:
# Reason: you’re mixing positional(5, bcz here order matter, 5 -> means num1) with keyword (num1=10) for the same parameter num1.
# Python raises: TypeError: calculator() got multiple values for argument 'num1'.

# Valid mixed usage: one positional + one keyword (different parameters)
result = calculator(10, num2=5)  
print(result)
# Output: (15, 5, 50, 2.0)


# --- ❌ Invalid case: positional after keyword → SyntaxError
# result = calculator(num2=5, 10)  
# Error: positional argument cannot appear after keyword


# -----------------------------------------------------
# Parameter Kinds (Python 3.8+) Advanced
# -----------------------------------------------------

# By default, parameters are "positional-or-keyword"
def greet(name, emoji):
    print(f"Hello {name} {emoji}")

greet("Awais", "😊")          # positional
greet(name="Awais", emoji="😊") # keyword


# -----------------------------------------------------
# A) Positional-Only Parameters (using '/')
# -----------------------------------------------------
def add(a, b, /):
    """`/` means all params before it are positional-only."""
    return a + b

print(add(2, 3))          # ✅ OK (positional)
# print(add(a=2, b=3))    # ❌ Error → cannot use keywords here


# -----------------------------------------------------
# B) Keyword-Only Parameters (using '*')
# -----------------------------------------------------
def multiply(*, x, y):
    """`*` means all params after it must be passed as keywords."""
    return x * y

print(multiply(x=4, y=5)) # ✅ OK
# print(multiply(4, 5))   # ❌ Error → must use keyword arguments


# -----------------------------------------------------
# C) Mixed Example (positional-only + normal + keyword-only)
# -----------------------------------------------------

def calculator(a, b, /, c=1, *, d=1):
    """
    Function explanation:
    
    - a, b → must be given in order (positional-only)
    - c    → flexible (can be given by position OR by keyword) → has default = 1
    - d    → must be given by keyword → has default = 1
    
    Formula: (a + b) * c * d
    """
    return (a + b) * c * d


# -----------------------------------------------------
# ✅ Correct Usage Examples
# -----------------------------------------------------

# Here:
# a = 2 (positional)
# b = 3 (positional)
# c = default value 1
# d = default value 1
print(calculator(2, 3))           
# Result = (2 + 3) * 1 * 1 = 5


# Here:
# a = 2 (positional)
# b = 3 (positional)
# c = 2 (positional, overrides default)
# d = default value 1
print(calculator(2, 3, 2))        
# Result = (2 + 3) * 2 * 1 = 10


# Here:
# a = 2 (positional)
# b = 3 (positional)
# c = 2 (given by keyword)
# d = 3 (must be keyword)
print(calculator(2, 3, c=2, d=3)) 
# Result = (2 + 3) * 2 * 3 = 30


# -----------------------------------------------------
# ❌ Wrong Usage Examples
# -----------------------------------------------------

# Error: a and b cannot be passed as keywords
# calculator(a=2, b=3)

# Error: d cannot be passed as positional (must be keyword)
# calculator(2, 3, 2, 3)