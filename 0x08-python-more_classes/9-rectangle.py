#!/usr/bin/python3
"""Definition of a Rectangle class."""


class Rectangle:
    """This class represents a rectangle.

    Attributes:
        number_of_instances (int): the number of rectangle instances.
        print_symbol (any): the symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This method initializes a new rectangle.

        Args:
            width (int): the width of the new rectangle.
            height (int): the height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """this method returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method gets/sets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method returns the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """This method returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method returns the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): the first Rectangle.
            rect_2 (Rectangle): the second Rectangle.
        Raises:
            TypeError: is raised if either of rect_1 or rect_2
		is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """This method returns a new Rectangle with width and
	height equal to size.

        Args:
            size (int): the width and height of the new rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """This method returns the printable representation of
	the rectangle using the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """This method returns the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """This method prints a message for every deletion of a rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
