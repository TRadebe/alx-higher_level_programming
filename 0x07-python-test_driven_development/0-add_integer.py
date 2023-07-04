#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added. Defaults to 98.

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    Example:
        >>> add_integer(5, 10)
        15
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
