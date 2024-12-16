try:
    # For when the script is run as part of a package
    from .operations import add, subtract, multiply, divide
    from .input_validation import (
        validate_calculation_count,
        validate_single_calculation,
    )
except ImportError:
    # For when the script is run directly
    from operations import add, subtract, multiply, divide
    from input_validation import validate_calculation_count, validate_single_calculation


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
    """Stage 3: Calculator supporting multiple calculations with validation."""
    print("Welcome to the Python calculator!")

    # Get number of calculations
    while True:
        try:
            num_calculations = validate_calculation_count(
                input("How many calculations do you want to do? ")
            )
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Perform multiple calculations
    for _ in range(num_calculations):
        while True:
            try:
                calculation = input("What do you want to calculate? ")

                validate_single_calculation(calculation)

                first_num = int(calculation[0])
                operator = calculation[1]
                second_num = int(calculation[2])

                result = calculate(first_num, operator, second_num)

                print(f"The answer is {result}")
                break

            except ValueError as e:
                print(f"Invalid input: {e}")
                print(
                    "Please try again with a valid single-digit calculation (e.g., 4+3, 5*2)"
                )


if __name__ == "__main__":
    main()
