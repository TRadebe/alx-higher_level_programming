#!/usr/bin/python3
"""This script defines a function for appending a string to a file."""


def append_write(filename="", text=""):
    """
    Append a string to a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
