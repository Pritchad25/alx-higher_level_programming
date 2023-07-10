#!/usr/bin/python3
"""Definition of an inherited class-checking function."""


def inherits_from(obj, a_class):
    """This method checks if an object is an inherited
	instance of a class.

    Args:
        obj (any): the object to check.
        a_class (type): the class to match the type of obj to.
    Returns:
	True - if obj is an inherited instance of a_class
        otherwise, false.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
