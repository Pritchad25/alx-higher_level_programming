#!/usr/bin/python3
"""Definition of a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square."""

    def __init__(self, size):
        """This method initializes a new square.

        Args:
            size (int): the size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
