def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def main():
    print("Simple Calculator")

    while True:
        num1 = get_number("Enter first number: ")
        operator = input("Enter an operator (+, -, *, /, %): ").strip()
        num2 = get_number("Enter second number: ")

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
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {result}")
            else:
                print("Error! Division by zero is not allowed.")

        elif operator == "%":
            if num2 != 0:
                result = num1 % num2
                print(f"Remainder: {result}")
            else:
                print("Error! Modulo by zero is not allowed.")

        else:
            print("Error! Invalid operator entered.")

        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
