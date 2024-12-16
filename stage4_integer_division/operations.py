def add(a, b):
    """Perform addition of two numbers."""
    return a + b


def subtract(a, b):
    """Perform subtraction of two numbers."""
    return a - b


def multiply(a, b):
    """Perform multiplication of two numbers."""
    return a * b


def divide(a, b):
    """Perform division of two numbers."""
    return a / b


def integer_division(a, b):
    """Perform integer division and return quotient and remainder."""
    quotient = a // b
    remainder = a % b
    return quotient, remainder
