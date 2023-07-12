#!/usr/bin/python3
"""Definition of a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """This method inserts text after each line containing
	a given string in a file.

    Args:
        filename (str): the name of the file.
        search_string (str): the string to search for within the file.
        new_string (str): the string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
    return triangles
