# =====================================================
#          🐍 Python Conditionals & Examples
# =====================================================

# -----------------------------------------------------
# 1. The if Statement
# -----------------------------------------------------
print("\n=====================================================")
print("================= The if Statement ==================")
print("=====================================================\n")
# 👉 The if statement executes code only if the condition is True.

num: int = 10

if num > 0:   # condition: is num greater than 0?
    print("The number is positive.")   # executes only if condition is True

# Output:
# The number is positive.


# -----------------------------------------------------
# 2. The else Statement
# -----------------------------------------------------
print("\n=====================================================")
print("================= The else Statement ================")
print("=====================================================\n")
# 👉 The else block runs when the if condition is False.

num: int = -5

if num > 0:   # condition: is num greater than 0?
    print("The number is positive.")
else:         # runs when the above condition is False
    print("The number is not positive.")

# Output:
# The number is not positive.


# -----------------------------------------------------
# 3. The elif Statement
# -----------------------------------------------------
print("\n=====================================================")
print("================= The elif Statement ================")
print("=====================================================\n")
# 👉 The Elif stands for 'else if'. It allows checking multiple conditions.

num: int = 0

if num > 0:                 
    print("The number is positive.")
elif num < 0:               
    print("The number is negative.")
else:                       
    print("The number is zero.")

# Output:
# The number is zero.


# -----------------------------------------------------
# 4. Nested if Statement
# -----------------------------------------------------
print("\n=====================================================")
print("================= Nested if Statement ===============")
print("=====================================================\n")
# 👉 if statements can be placed inside another if statement.

num: int = 10
# num: int = -10   # you can test this also

if num > 0:   # check if number is positive
    if num % 2 == 0:   # check if even number
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")

# Output:
# The number is positive and even.


# -----------------------------------------------------
# 5. Practical Example 1 – Simple Calculator
# -----------------------------------------------------
print("\n=====================================================")
print("====== Practical Example 1 – Simple Calculator ======")
print("=====================================================")
# 👉 A calculator that supports +, -, *, / with basic error handling.

# ---- User Input ----
operation: str = input("Enter Your Operation (+, -, *, /): ")
num1: float = float(input("Enter Your First Number: "))
num2: float = float(input("Enter Your Second Number: "))

# ---- Calculator Logic ----
if operation == "+":
    print(f"\nYou selected Addition ({operation})")
    print(f"Result: {num1} + {num2} = {num1 + num2}")

elif operation == "-":
    print(f"\nYou selected Subtraction ({operation})")
    print(f"Result: {num1} - {num2} = {num1 - num2}")

elif operation == "*":
    print(f"\nYou selected Multiplication ({operation})")
    print(f"Result: {num1} * {num2} = {num1 * num2}")

elif operation == "/":
    if num2 != 0:
        print(f"\nYou selected Division ({operation})")
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("\nError: Division by zero is not allowed!")
else:
    print("\nInvalid Operation! Please select from (+, -, *, /)")


# -----------------------------------------------------
# 6. Practical Example 2 – Advance Calculator
# -----------------------------------------------------
print("\n=====================================================")
print("====== Practical Example 2 – Advance Calculator =====")
print("=====================================================")
# 👉 Includes modulus (%), floor division (//), exponentiation (**)

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

        # Perform calculation
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


# -----------------------------------------------------
# 7. Practical Example 3 – Grading System
# -----------------------------------------------------
print("\n=====================================================")
print("====== Practical Example 3 – Grading System =========")
print("=====================================================")
# 👉 Assign grades based on marks.

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

# ---- Input Validation ----
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