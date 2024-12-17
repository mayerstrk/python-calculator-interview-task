def validate_input(calculation):
    """
    Validate input for Stage 1 (Addition only).

    Checks:
    - Length is exactly 3 characters
    - Middle character is '+'
    - First and last characters are single digits
    """
    if len(calculation) != 3:
        return {"success": False, "error": ValueError("Invalid input length")}

    if calculation[1] != "+":
        return {
            "success": False,
            "error": ValueError("Stage 1 supports only addition (+)"),
        }

    try:
        int(calculation[0])
        int(calculation[2])
    except ValueError:
        return {
            "success": False,
            "error": ValueError("Input must be single-digit numbers"),
        }

    return {"success": True, "error": None}
