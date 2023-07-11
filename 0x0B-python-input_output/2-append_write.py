#!/usr/bin/python3
"""Definition a file-appending function."""


def append_write(filename="", text=""):
    """This function appends a string to the end of a UTF8 text file.

    Args:
        filename (str): the name of the file to append to.
        text (str): the string to append to the file.
    Returns:
        the number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
