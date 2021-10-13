#!/usr/bin/python3
"""Write a class Student that defines a student."""


class Student():
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age.
        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        Args:
            attrs : Attributes to retrieve.
        Return:
            dict: A dictionary.
        """
        if attrs is None:
            return self.__dict__
        dict = {}
        for key in attrs:
            if hasattr(self, key):
                dict[key] = getattr(self, key)
        return dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        Args:
            json (dict): Dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
