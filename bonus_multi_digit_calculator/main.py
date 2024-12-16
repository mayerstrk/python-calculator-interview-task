from .operations import add, subtract, multiply, divide, integer_division
from .input_validation import validate_input


def parse_calculation(calculation):
    """Parse calculation string with multi-digit numbers."""
    valid_operators = ["+", "-", "*", "/", "~"]

    # Iterate to find the operator in the string
    for op in valid_operators:
        if op in calculation:
            parts = calculation.split(op)

            if len(parts) != 2:
                raise ValueError(
                    "Invalid calculation format. Must include two numbers and one operator."
                )

            try:
                operand1 = int(parts[0].strip())
                operand2 = int(parts[1].strip())
            except ValueError:
                raise ValueError("Operands must be valid integers.")

            return operand1, operand2, op

    raise ValueError("No valid operator found in calculation.")


def main():
    """Main function to process user input and perform calculations."""
    print("Welcome to the Bonus Multi-Digit Calculator!")
    print("Supported operations: +, -, *, /, ~ (integer division)")

    while True:
        calculation = input("Enter your calculation (or 'q' to quit): ").strip()

        if calculation.lower() == "q":
            print("Goodbye!")
            break

        try:
            validate_input(calculation)

            operand1, operand2, operator = parse_calculation(calculation)

            if operator == "+":
                result = add(operand1, operand2)
            elif operator == "-":
                result = subtract(operand1, operand2)
            elif operator == "*":
                result = multiply(operand1, operand2)
            elif operator == "/":
                # Handle division by zero
                if operand2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = divide(operand1, operand2)
            elif operator == "~":
                # Handle integer division and return both quotient and remainder
                if operand2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                quotient, remainder = integer_division(operand1, operand2)
                print(f"Quotient: {quotient}, Remainder: {remainder}")
                continue
            else:
                print(f"Unsupported operator: {operator}")
                continue

            print(f"Result: {result}")
        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
