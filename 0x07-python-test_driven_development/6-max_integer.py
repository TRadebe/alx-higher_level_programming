#!/usr/bin/python3
"""Module to find the maximum integer in a list."""


def max_integer(lst=[]):
    """Find and return the maximum integer in a list of integers.

    Args:
        lst (list, optional): The list of integers. Defaults to an empty list.

    Returns:
        int or None: The maximum integer in the list. If the list is empty, returns None.
    """
    if len(lst) == 0:
        return None
    result = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > result:
            result = lst[i]
        i += 1
    return result
