#!/usr/bin/python3
"""a square class"""


class Square:
    """begining of Square"""

    def __init__(self, size=0):
        """initiates a square instance
        Args:
        size (int): size of square instance
        """
        self.__size = size

    @property
    def size(self):
        """prevoiussize of a square initiates"""
        return self.__size

    @size.setter
    def size(self, value):
        """initiates value of variable
        Args:
            value (int): size of Square
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """return area of square"""
        return self.__size**2
