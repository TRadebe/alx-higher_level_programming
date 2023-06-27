#!/usr/bin/python3

class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Initializes a square instance

        Args:
            size (int): The size of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (int): The size value to set

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square with the character '#'
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
