#!/usr/bin/python3
"""This script defines a function for serializing a class instance to JSON."""


def class_to_json(obj):
    """
    Serialize a class instance to JSON.

    Args:
        obj (object): The class instance to be serialized.

    Returns:
        dict: A dictionary representing the serialized object.
    """
    return obj.__dict__
