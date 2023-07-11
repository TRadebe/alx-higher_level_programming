#!/usr/bin/python3
"""This script defines a Student class."""


class Student:
    """
    Class that represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representing the student's attributes.
        """
        return self.__dict__
