#!/usr/bin/python3
"""definition of a class called Square."""

class Square:
    """This class defines a square by using a
    private instance attribute, getters, setters and
    a public instance method.
    """
    def __init__(self, size=0):
        """this init method initializes a new square.

        Args:
            size (int): defines the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """this method Gets/sets the current size of the
        square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the current area of the square."""
        return (self.__size * self.__size)
