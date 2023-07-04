#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Prints a name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed. Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name are not strings.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
