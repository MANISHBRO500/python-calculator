# Taking integer inputs using the int() function
num1 = int(input("Enter first number: "))
operator = input("Enter an operator (+, -, *, /, %): ")
num2 = int(input("Enter second number: "))

# Conditional statements to perform arithmetic operations
if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")

elif operator == "/":
    # Checking for division by zero error
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error! Division by zero is not allowed.")

elif operator == "%":
    # Checking for modulo by zero error
    if num2 != 0:
        result = num1 % num2
        print(f"Remainder: {result}")
    else:
        print("Error! Modulo by zero is not allowed.")

else:
    print("Error! Invalid operator entered.")
