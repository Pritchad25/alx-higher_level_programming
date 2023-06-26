#!/usr/bin/python3

def safe_print_integer(value):
    """This function prints an integer with
    "{:d}".format().

    Args:
    value (int): The integer to print

    Returns:
    False, if a TypeError or ValueError occurs
    Otherwise, True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

