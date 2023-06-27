#!/usr/bin/python3
"""definition of a class called Square."""

class Square:
    """This class defines a square."""

    def __init__(self, size):
        """This method initializes a new square.

        Args:
            size (int): defines the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """this method gets/sets the current size of
        the square.
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
        """This method returns the current area of the
        square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """This method prints the square using the
        # character.
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
