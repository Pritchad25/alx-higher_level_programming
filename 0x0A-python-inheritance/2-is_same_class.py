#!/usr/bin/python3
"""Definition of a class-checking function."""


def is_same_class(obj, a_class):
    """This method checks if an object is exactly an instance
	of a given class.

    Args:
        obj (any): the object to check.
        a_class (type): the class to match the type of obj to.
    Returns: True - if obj is exactly an instance of a_class
	otherwise, false.
    """
    if type(obj) == a_class:
        return True
    return False
