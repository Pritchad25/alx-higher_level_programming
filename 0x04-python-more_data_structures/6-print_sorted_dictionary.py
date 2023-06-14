#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """This function prints a dictionary
    by ordered keys."""
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for i in list_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
