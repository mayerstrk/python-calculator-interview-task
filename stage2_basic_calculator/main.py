from .operations import add, subtract, multiply, divide
from .input_validation import validate_input


def calculate(first_num, operator, second_num):
    """Perform calculation based on operator."""
    if operator == "+":
        return add(first_num, second_num)
    elif operator == "-":
        return subtract(first_num, second_num)
    elif operator == "*":
        return multiply(first_num, second_num)
    elif operator == "/":
        return divide(first_num, second_num)
    else:
        raise ValueError("Unsupported operation")


def main():
    """Stage 2: Calculator with multiple operations and input validation."""
    print("Welcome to the Python calculator!")

    # Get input for calculation
    while True:
        try:
            calculation = input("What do you want to calculate? ")

            # Validate input
            validate_input(calculation)

            # Parse calculation
            first_num = int(calculation[0])
            operator = calculation[1]
            second_num = int(calculation[2])

            # Perform calculation
            result = calculate(first_num, operator, second_num)

            # Display result
            print(f"The answer is {result}")
            break

        except ValueError as e:
            print(f"Invalid input: {e}")
            print(
                "Please try again with a valid single-digit calculation (e.g., 4+3, 5*2)"
            )
