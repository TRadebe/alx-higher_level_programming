#!/usr/bin/python3
"""Defines a function for printing squares."""


def print_square(size):
    """Prints a square of a given size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is a negative number.
        TypeError: If size is a float and less than zero.

    Example:
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
