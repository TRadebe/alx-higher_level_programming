#!/usr/bin/python3
"""Define function"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """empty"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
