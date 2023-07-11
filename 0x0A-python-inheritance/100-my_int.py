#!/usr/bin/python3
"""Definition of a class MyInt that inherits from int."""


class MyInt(int):
    """This class inverts int operators == and !=."""

    def __eq__(self, value):
        """This method overrides == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """This methods overrides != operator with == behavior."""
        return self.real == value
