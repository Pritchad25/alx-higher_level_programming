#!/usr/bin/python3
"""the following code defines a class called Square"""

class Square:
    """Defines a square by using a private instance
    attribute. No module is imported.
    """

    def __init__(self, size=0):
        """This init method initializes a new Square.
        No module is imported.

        Args:
            size (int): defines the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
