#!/usr/bin/python3
"""Definition of a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """This method initializes a new Rectangle.

        Args:
            width (int): the width of the new Rectangle.
            height (int): the height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """This method returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """This method returns the print() and str() representation
	of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
