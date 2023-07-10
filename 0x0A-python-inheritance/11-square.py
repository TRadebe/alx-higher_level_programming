#!/usr/bin/python3
"""Definese."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Repr"""

    def __init__(self, size):
        """Ini."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
