#!/usr/bin/python3
"""Definition of a class Student."""


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

    def to_json(self, attrs=None):
        """This method gets a dictionary representation of
	the Student.

        If attrs is a list of strings, it represents only those attributes
        included in the list.

        Args:
            attrs (list): the attributes to represent (optional)
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """This method replaces all attributes of the class Student.

        Args:
            json (dict): the key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
