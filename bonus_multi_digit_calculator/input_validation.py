def validate_input(calculation):
    """
    Validate input for Bonus Multi-Digit Stage.

    Checks:
    - Contains one of the supported operators
    - Can parse into two integers
    """
    valid_operators = ["+", "-", "*", "/", "~"]

    operator_found = False
    for op in valid_operators:
        if op in calculation:
            operator_found = True
            break

    if not operator_found:
        raise ValueError(
            f"No valid operator found. Supported operators are: {', '.join(valid_operators)}"
        )

    try:
        for op in valid_operators:
            if op in calculation:
                parts = calculation.split(op)
                int(parts[0])
                int(parts[1])
                break
    except (ValueError, IndexError):
        raise ValueError("Invalid number format")

    return True
