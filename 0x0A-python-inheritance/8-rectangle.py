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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
