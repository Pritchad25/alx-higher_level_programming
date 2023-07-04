#!/usr/bin/python3
# 5-text_indentation.py
"""Definition of a text-indentation function."""

def text_indentation(text):
    """This function prints the text with 2 new lines
    after each '.', '?' and ':' character.

    Args:
        text (string): the text to be printed.

    Raises:
        TypeError: is raised if the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

