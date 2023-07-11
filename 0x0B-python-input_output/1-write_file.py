#!/usr/bin/python3
"""Definition a file-writing function."""

def write_file(filename="", text=""):
    """This method writes a string to a UTF8 text file.

    Args:
        filename (str): the name of the file to write to.
        text (str): the text to write to the file.
    Returns:
        the number of characters written in the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
