#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is None, return all attributes.

        Args:
            attrs (list): (Optional) The attributes to represent.

        Returns:
            dict: A dictionary representing the Student object.
        """
        if attrs is None:
            return self.__dict__

        result = {}
        try:
            for key in attrs:
                if not isinstance(key, str):
                    raise TypeError("Attribute names must be strings.")
                result[key] = getattr(self, key)
        except AttributeError as e:
            raise AttributeError(f"'Student' object has no attribute '{key}'.") from e

        return result
