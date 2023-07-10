#!/usr/bin/python3
"""Dbclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """uare."""

    def __init__(self, size):
        """Inite."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
