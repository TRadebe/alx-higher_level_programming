#!/usr/bin/python3
"""This script defines a function for writing a string to a file."""


def write_file(filename="", text=""):
    """
    Write a string to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
