"""Definition of a base geometry class BaseGeometry."""


class BaseGeometry:
    """This class represents base geometry."""

    def area(self):
        """This method will not yet be implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates a parameter as an integer.

        Args:
            name (str): the name of the parameter.
            value (int): the parameter to validate.
        Raises:
            TypeError: is raised if value is not an integer.
            ValueError: is raised if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
