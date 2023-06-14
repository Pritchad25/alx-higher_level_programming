#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """This function returns a list with all
    values multiplied by a number without
    using any loops."""
    return list(map(lambda n: n * number, my_list))
