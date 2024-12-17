try:
    from .operations import add, subtract, multiply, divide, integer_division
    from .input_validation import validate_input
except ImportError:
    # For when the script is run directly
    from operations import add, subtract, multiply, divide, integer_division
    from input_validation import validate_input


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
    elif operator == "~":
        quotient, remainder = integer_division(first_num, second_num)
        return quotient, remainder
    else:
        raise ValueError("Unsupported operation")


def main():
    """Stage 4: Calculator with integer division and input validation."""
    print("Welcome to the Python calculator!")

    while True:
        try:
            num_calculations = int(input("How many calculations do you want to do? "))
            break
        except ValueError:
            print("Please enter a valid number of calculations.")

    for _ in range(num_calculations):
        while True:
            try:
                calculation = input("What do you want to calculate? ")

                validate_input(calculation)

                first_num = int(calculation[0])
                operator = calculation[1]
                second_num = int(calculation[2])

                result = calculate(first_num, operator, second_num)

                if operator == "~":
                    print(f"The answer is {result[0]}")
                    print(f"The remainder is {result[1]}")
                else:
                    print(f"The answer is {result}")
                break

            except ValueError as e:
                print(f"Invalid input: {e}")
                print(
                    "Please try again with a valid single-digit calculation (e.g., 4+3, 5*2, 7~3)"
                )


if __name__ == "__main__":
    main()
