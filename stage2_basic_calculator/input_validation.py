def validate_input(calculation):
    """
    Validate input for Stage 2 (Basic operations).

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
