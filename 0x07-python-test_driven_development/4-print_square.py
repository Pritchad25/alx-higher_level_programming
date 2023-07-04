#!/usr/bin/python3
# 4-print_square.py
"""Definition of a square printing function."""

def print_square(size):
    """This function prints a square with the #
    character.

    Args:
        size (int): the height or width of the square.

    Raises:
        TypeError: is raised if the size is not an integer.
        ValueError: is raised if the size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

