#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """This function replaces all occurrences of an 
    element by another in a new list."""
    return [replace if search == n else n for n in my_list]
