#!/usr/bin/python3
"""Deftributes to objects."""


def add_attribute(obj, att, value):
    """Add a new n """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
