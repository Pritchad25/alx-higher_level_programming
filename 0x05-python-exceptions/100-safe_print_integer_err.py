#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """This function prints an integer
    that has "{:d}".format()
    If a ValueError exception is caught, a
    corresponding error message will be printed to
    standard error.

    Args:
    value (int): the integer to print

    Returns:
    True- if the value has been correctly printed
    False- if TypeError or ValueError occurs. """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
