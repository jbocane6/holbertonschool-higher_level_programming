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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
