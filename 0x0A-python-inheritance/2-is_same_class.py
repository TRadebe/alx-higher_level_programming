#!/usr/bin/python3
"""Defien a function check if isnstance"""


def is_same_class(obj, a_class):
    """Return true if obj is instance of a_class"""
    if type(obj) == a_class:
        return True
    return False
