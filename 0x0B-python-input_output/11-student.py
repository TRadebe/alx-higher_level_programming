#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """
    Class that defines properties of a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Creates a new instance of Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is None, return a dictionary representation of all attributes.
        If attrs is a list of strings, return a dictionary representation of
        only those attributes included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.

        Returns:
            dict: A dictionary representing the Student object.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except KeyError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing attribute values.

        Returns:
            None
        """
        self.__dict__.update(json)
