#!/usr/bin/python3
"""a sqaure class"""


class Square:
    """begining of Square"""

    def __init__(self, size=0):
        """initiates a square instance
        Args:
        size (int): size of square instance
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """returns area of the suare instance"""
        return (self.__size * self._size)
