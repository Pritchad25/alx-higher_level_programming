#!/usr/bin/python3
"""Defines a class called Square"""

class Square:
    """This class defines a square by using a
    private instance attribute called size.

    """

    def __init__(self, size):
        """The init method initializes a
        new Square.

        Args:
            size (int): defines the size of the new square.
        """

        self.__size = size
