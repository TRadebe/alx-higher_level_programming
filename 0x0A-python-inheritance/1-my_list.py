#!/usr/bin/python3
"""Define a function that inherits a class"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
