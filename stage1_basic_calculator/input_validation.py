def validate_input(calculation):
    """
    Validate input for Stage 1 (Addition only).

    Checks:
    - Length is exactly 3 characters
    - Middle character is '+'
    - First and last characters are single digits
    """
    if len(calculation) != 3:
        raise ValueError("Invalid input length")

    if calculation[1] != "+":
        raise ValueError("Stage 1 supports only addition (+)")

    try:
        int(calculation[0])
        int(calculation[2])
    except ValueError:
        raise ValueError("Input must be single-digit numbers")

    return True
