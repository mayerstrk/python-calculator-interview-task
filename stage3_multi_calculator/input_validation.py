def validate_single_calculation(calculation):
    """
    Validate input for single calculation in Stage 3.

    Checks:
    - Length is exactly 3 characters
    - Middle character is one of '+', '-', '*', '/'
    - First and last characters are single digits
    """
    valid_operators = ["+", "-", "*", "/"]

    if len(calculation) != 3:
        raise ValueError("Invalid input length")

    if calculation[1] not in valid_operators:
        raise ValueError(f"Supported operators are: {', '.join(valid_operators)}")

    try:
        int(calculation[0])
        int(calculation[2])
    except ValueError:
        raise ValueError("Input must be single-digit numbers")

    return True


def validate_calculation_count(count):
    """
    Validate the number of calculations.

    Checks:
    - Input is a positive integer
    """
    try:
        count = int(count)
        if count <= 0:
            raise ValueError("Number of calculations must be a positive integer")
        return count
    except ValueError:
        raise ValueError("Please enter a valid number of calculations")
