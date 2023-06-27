#!/usr/bin/python3
"""creat a square class"""


class Square:
    """Creation of Square template"""

    def __init__(self, size=0):
        """Starts a square instance
        Args:
        size (int): size of the square instance
        """
        self.__size = size

    @property
    def size(self):
        """retrieve the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of variable
        Args:
            value (int): size of the Square
        """

        if not isinstance(value, int):
            raise ValueError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0 ')
        self.__size = value

    def area(self):
        """return the area of the square"""
        return self.__size**2

    def my_print(self):
        """Print the square"""

        for i in range(self.__size):
            print('#'*self.__size, end='')
            print()
        if self.__size == 0:
            print()
