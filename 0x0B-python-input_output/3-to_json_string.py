#!/usr/bin/python3
"""This script defines a function for converting a string to JSON."""


import json


def to_json_string(my_obj):
    """
    Convert a string object to its JSON representation.

    Args:
        my_obj (str): The string object to be converted.

    Returns:
        str: The JSON representation of the string object.
    """
    return json.dumps(my_obj)
