#!/usr/bin/python3
"""Definition of an object attribute lookup function."""

def lookup(obj):
    """This method returns a list of an object's
	available attributes."""

    return (dir(obj))
