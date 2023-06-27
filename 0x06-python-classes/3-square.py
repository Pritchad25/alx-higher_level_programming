#!/usr/bin/python3
"""definition of a class called Square."""

class Square:
    """This class defines a square by using a private
    instance attribute and a public instance method.
    """
    def __init__(self, size=0):
        """This init method initializes a
        new square.

        Args:
            size (int): defines the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise Value Error("size must be >= 0")
        self.__size = size

    def area(self):
        """This public instance method returns the
        current area of the square.

        """
        return (self.__size * self.__size)
