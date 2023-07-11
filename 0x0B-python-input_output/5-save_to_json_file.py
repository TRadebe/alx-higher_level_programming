#!/usr/bin/python3
"""This script defines a function for writing an object to a JSON file."""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a JSON file.

    Args:
        my_obj (object): The object to be written to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
