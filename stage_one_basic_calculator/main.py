try:
    # when the script is run as part of a package
    from .operations import add
    from .input_validation import validate_input
except ImportError:
    # when the script is run directly
    from operations import add
    from input_validation import validate_input


def main():
    """Stage 1: Basic calculator with only addition and input validation."""
    print("Welcome to the Python calculator!")

    while True:
        try:
            calculation = input("What do you want to calculate? ")

            validation_result = validate_input(calculation)

            is_input_valid = validation_result["success"]

            if not is_input_valid:
                raise validation_result["error"]

            first_num = int(calculation[0])
            second_num = int(calculation[2])
            result = add(first_num, second_num)

            print(f"The answer is {result}")
            break

        except ValueError as e:
            print(f"Invalid input: {e}")
            print("Please try again with a valid single-digit addition (e.g., 4+3)")


if __name__ == "__main__":
    main()
