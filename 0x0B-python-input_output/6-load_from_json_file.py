#!/usr/bin/python3
"""This script defines a function for loading an object from a JSON file."""


import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
