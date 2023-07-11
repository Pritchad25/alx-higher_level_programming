#!/usr/bin/python3
"""Definition of a class called Student."""


class Student:
    """This class represents a student."""

    def __init__(self, first_name, last_name, age):
        """This method initializes a new Student.

        Args:
            first_name (str): the first name of the student.
            last_name (str): the last name of the student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function gets a dictionary representation
	of the Student."""
        return self.__dict__
