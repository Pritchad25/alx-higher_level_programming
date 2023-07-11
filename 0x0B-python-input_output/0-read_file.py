#!/usr/bin/python3
"""Definition of a text file-reading function."""

def read_file(filename=""):
    """This function prints the contents of a UTF8 text
	file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
