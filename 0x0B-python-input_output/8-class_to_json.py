#!/usr/bin/python3
"""Definition of a Python class-to-JSON function."""


def class_to_json(obj):
    """This method returns the dictionary representation of
	a simple data structure."""
    return obj.__dict__
