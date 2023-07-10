#!/usr/bin/python3
"""Define a function that returns the attributes of an object"""


def lookup(obj):
    """ Looks up the details of an object
    Args:
        obj: object to be looked up
    Return:
        obj details
    """
    return (dir(obj))
