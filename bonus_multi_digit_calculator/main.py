try:
    from .operations import add, subtract, multiply, divide, integer_division
    from .input_validation import validate_input
except ImportError:
    from operations import add, subtract, multiply, divide, integer_division
    from input_validation import validate_input


def parse_calculation(calculation):
    """Parse a calculation string into operands and operator for multi-digit integers.

    Supports +, -, *, /, ~ operators.
    Returns:
        operand1 (int), operand2 (int), operator (str)
    Raises:
        ValueError: If format is invalid or no valid operator is found.
    """
    valid_operators = ["+", "-", "*", "/", "~"]
    for op in valid_operators:
        if op in calculation:
            parts = calculation.split(op)
            if len(parts) != 2:
                raise ValueError(
                    "Invalid calculation format. Must be 'number operator number'."
                )
            try:
                operand1 = int(parts[0].strip())
                operand2 = int(parts[1].strip())
            except ValueError:
                raise ValueError("Operands must be valid integers.")
            return operand1, operand2, op
    raise ValueError("No valid operator found in calculation.")


def main():
    print("Welcome to the Bonus Multi-Digit Calculator!")
    print("How many calculations do you want to do?")

    # Get number of calculations from the user
    while True:
        user_input = input().strip()
        if not user_input.isdigit():
            print("Please enter a valid integer.")
            continue
        number_of_calculations = int(user_input)
        if number_of_calculations <= 0:
            print("Please enter a positive number.")
            continue
        break

    print(
        "Supported operations: + (add), - (subtract), * (multiply), "
        "/ (divide), ~ (integer division)"
    )

    for _ in range(number_of_calculations):
        calculation = input("What do you want to calculate? ").strip()
        try:
            validate_input(calculation)
            operand1, operand2, operator = parse_calculation(calculation)

            if operator == "+":
                result = add(operand1, operand2)
                print(f"The answer is {result}")
            elif operator == "-":
                result = subtract(operand1, operand2)
                print(f"The answer is {result}")
            elif operator == "*":
                result = multiply(operand1, operand2)
                print(f"The answer is {result}")
            elif operator == "/":
                if operand2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = divide(operand1, operand2)
                print(f"The answer is {result}")
            elif operator == "~":
                if operand2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                quotient, remainder = integer_division(operand1, operand2)
                print(f"The answer is {quotient}")
                print(f"The remainder is {remainder}")
            else:
                # Should not reach here if validate_input and parse are correct
                print(f"Unsupported operator: {operator}")

        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    print("All calculations done. Goodbye!")


if __name__ == "__main__":
    main()
