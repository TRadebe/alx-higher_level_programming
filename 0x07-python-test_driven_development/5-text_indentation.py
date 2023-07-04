#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text = "Hello. How are you? I am fine."
        >>> text_indentation(text)
        Hello.
        
        How are you?
        
        I am fine.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
