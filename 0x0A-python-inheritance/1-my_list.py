#!/usr/bin/python3
"""Definition of an inherited list class MyList."""

class MyList(list):
    """This class implements sorted printing for the
	built-in class called list.
    """

    def print_sorted(self):
        """This method prints a list in sorted ascending order."""
        print(sorted(self))
